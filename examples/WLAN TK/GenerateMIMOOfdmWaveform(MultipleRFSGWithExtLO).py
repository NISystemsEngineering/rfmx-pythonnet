import clr, os.path, time, re
from sys import path

path.append(os.path.abspath(__file__ + "\\..\\..\\..\\bin"))
clr.AddReference("NationalInstruments.RFToolkits.Interop.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.Interop.Fx40")

import NationalInstruments.RFToolkits.Interop as Toolkits
import NationalInstruments.ModularInstruments.Interop as ModInst
import System.Runtime.InteropServices as InteropServices

# Generator Parameters
rfsgResourceNames = ["VST_01", "VST_02"]
rfsgReferenceClockSource = ModInst.niRFSGConstants.PxiClkStr
carrierFrequency = 5.18e+9
powerLevels = [-10, -10]
externalAttenuation = [0, 0]
syncTriggerLines = [0, 1]
rfBlankingEnabled = False

# LO Distribution Parameters
LOSource = Toolkits.niWLANGConstants.LOSourceExternal
externalLOResourceName = "LO_01"
externalLOReferenceClockSource = ModInst.niRFSAConstants.OnboardClockStr
rfsgLODaisyChainEnabled = True
LOExportToExternalDevicesEnabled = False

# Measurement Parameters
standard = Toolkits.niWLANGConstants.Standard80211AxMimoOfdm
channelBandwidth = 80e+6
numTx = len(rfsgResourceNames)
mCSIndex = 0
mappingMatrixType = Toolkits.niWLANGConstants.MappingMatrixTypeDirect
numOfSpaceTimeStreams = numTx
frameFormat = Toolkits.niWLANGConstants._80211nPlcpFrameFormatMixed
ahPreambleType = Toolkits.niWLANGConstants.PreambleTypeShortPreamble

# Configure Toolkit Session
wlang = Toolkits.niWLANG(Toolkits.niWLANGConstants.CompatibilityVersion050000)
wlang.SetStandard(None, standard)
wlang.SetChannelBandwidth(None, channelBandwidth)
wlang.SetNumberOfTransmitChannels(None, numTx)
wlang.SetMcsIndex(None, mCSIndex)
wlang.SetMappingMatrixType(None, mappingMatrixType)
wlang.Set_80211nPlcpFrameFormat(None, frameFormat)
wlang.SetNumberOfSpaceTimeStreams(None, numOfSpaceTimeStreams)
wlang.Set_80211ahPreambleType(None, ahPreambleType)
wlang.SetLOFrequencyOffsetMode(None, Toolkits.niWLANGConstants.LOFrequencyOffsetModeAuto)
wlang.SetRFBlankingEnabled(None, rfBlankingEnabled)

# Configure External LO
externalLOHandle = InteropServices.HandleRef()
if externalLOResourceName is not None and LOSource == Toolkits.niWLANGConstants.LOSourceExternal:
    externalLOSession = ModInst.niRFSG(externalLOResourceName, True, False)
    externalLOSession.ConfigureRefClock(externalLOReferenceClockSource, 10e+6)
    externalLOSession.SetGenerationMode(None, ModInst.niRFSGConstants.Cw)
    externalLOHandle = externalLOSession.Handle

# Configure Generator Sessions
rfsgSessions = [ModInst.niRFSG] * numTx
for i in range(numTx):
    rfsgSessions[i] = ModInst.niRFSG(rfsgResourceNames[i], True, False)
    rfsgSessions[i].ConfigurePowerLevelType(ModInst.niRFSGConstants.PeakPower)
    rfsgSessions[i].ConfigureGenerationMode(ModInst.niRFSGConstants.Script)
    rfsgSessions[i].SetExternalGain(None, -(externalAttenuation[i]))

# Create and Download Waveform
rfsgHandles = [rfsgSession.Handle for rfsgSession in rfsgSessions]
wlang.ConfigureMultipleDeviceSynchronization(rfsgHandles, numTx, rfsgReferenceClockSource, syncTriggerLines, len(syncTriggerLines))
wlang.RFSGConfigureFrequencySingleLO(rfsgHandles, LOSource, externalLOHandle, carrierFrequency, rfsgLODaisyChainEnabled, LOExportToExternalDevicesEnabled)
wlang.RFSGCreateAndDownloadMIMOWaveforms(rfsgHandles, None, numTx, "wlan")
for rfsgHandle, powerLevel in zip(rfsgHandles, powerLevels):
    script = "script GenerateWlan\nrepeat forever\ngenerate wlan\nend repeat\nend script"
    Toolkits.niWLANG.WLANG_RFSGConfigureScript(rfsgHandle, None, script, powerLevel)

# Cascade LO Power Levels for Optimal Performance
if rfsgLODaisyChainEnabled:
    _, instrumentModel = rfsgSessions[0].GetInstrumentModel(None, None)
    if (re.match(r"NI PXIe-583\d", instrumentModel)):
        LOChannelName = "lo2"
    else:
        LOChannelName = None
    if externalLOResourceName is not None and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
        _, loOutPower = externalLOSession.GetPowerLevel(None, 0.0)
        rfsgSessions[0].SetLoInPower(LOChannelName, loOutPower)
        rfsgSessions[0].SetDouble(ModInst.niRFSGProperties.LoOutPower, LOChannelName, loOutPower)
    for i in range(numTx - 1):
        _, loOutPower = rfsgSessions[i].GetLoOutPower(LOChannelName, 0.0)
        rfsgSessions[i + 1].SetLoInPower(LOChannelName, loOutPower)
        _, loInPower = rfsgSessions[i + 1].GetLoInPower(LOChannelName, 0.0)
else:
    pass # loss through splitter will need to be considered

# Initiate
if externalLOResourceName is not None and LOSource == Toolkits.niWLANGConstants.LOSourceExternal:
    externalLOSession.Initiate()
wlang.RFSGMultipleDeviceInitiate(rfsgHandles)

# Wait on User
print("Generation in progress. Press to ctrl+c to stop.")
try:
    isDone = False
    while(not isDone):
        time.sleep(10e-3)
        for rfsgSession in rfsgSessions:
            isDone = isDone or rfsgSession.CheckGenerationStatus(False)[1]
except KeyboardInterrupt:
    pass

# Close Sessions
wlang.Close()
if externalLOResourceName is not None and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
    externalLOSession.close()
for rfsgSession in rfsgSessions:
    rfsgSession.close()
print ("Generation aborted.")
