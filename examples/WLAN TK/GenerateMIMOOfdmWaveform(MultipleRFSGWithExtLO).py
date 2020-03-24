import clr, os.path, time, re, math
from sys import path

path.append(os.path.abspath(__file__ + "\\..\\..\\..\\bin"))
clr.AddReference("NationalInstruments.RFToolkits.Interop.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.Interop.Fx40")

import NationalInstruments.RFToolkits.Interop as Toolkits
import NationalInstruments.ModularInstruments.Interop as ModInst
import System.Runtime.InteropServices as InteropServices

# Generator Parameters
rfsgResourceNames = ["VST1_01", "VST1_02"] # defined in order of transmit channel number, first element is sync master
rfsgReferenceClockSource = ModInst.niRFSGConstants.PxiClkStr
carrierFrequency = 5.18e+9
powerLevels = [-10, -10]
externalAttenuation = [0, 0]
syncTriggerLines = [0, 1]
rfBlankingEnabled = False

# LO Distribution Parameters
loDaisyChainConfig = (rfsgResourceNames,) # tuple of lo daisy chains, external LO will be split to first element in each list, else first element in each list is lo master
LOSource = Toolkits.niWLANGConstants.LOSourceOnboard
externalLOResourceName = ""
externalLOReferenceClockSource = ModInst.niRFSAConstants.OnboardClockStr
LOExportToExternalDevicesEnabled = False # defines whether LO should be exported on last resource in each daisy chain

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
if externalLOResourceName and LOSource == Toolkits.niWLANGConstants.LOSourceExternal:
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

# Configure Synchronous Generation
rfsgHandles = [rfsgSession.Handle for rfsgSession in rfsgSessions]
wlang.ConfigureMultipleDeviceSynchronization(rfsgHandles, numTx, rfsgReferenceClockSource, syncTriggerLines, len(syncTriggerLines))

# Distribute LO(s) and Configure for Optimal Performance
rfsgSessionDict = dict(zip(rfsgResourceNames, rfsgSessions))
for daisyChain in loDaisyChainConfig:
    daisyChainSessions = [rfsgSessionDict[resourceName] for resourceName in daisyChain]
    daisyChainHandles = [rfsgSession.Handle for rfsgSession in daisyChainSessions]
    wlang.RFSGConfigureFrequencySingleLO(daisyChainHandles, LOSource, externalLOHandle, carrierFrequency, True, LOExportToExternalDevicesEnabled)
    _, instrumentModel = daisyChainSessions[0].GetInstrumentModel(None, None)
    match = re.match(r"NI PXIe-58(\d)", instrumentModel)
    if match: # only 58xx models of VST support power cascading
        if match.group(1) == '3': # 583x models have multiple lo channels
            LOChannelName = "lo2"
        else:
            LOChannelName = None
        if externalLOResourceName and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
            _, loOutPower = externalLOSession.GetPowerLevel(None, 0.0)
            loOutPower = loOutPower - 10 * math.log10(len(loDaisyChainConfig)) # approximation of splitter loss
            daisyChainSessions[0].SetLoInPower(LOChannelName, loOutPower)
            daisyChainSessions[0].SetDouble(ModInst.niRFSGProperties.LoOutPower, LOChannelName, loOutPower)
        elif LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
            print("External LO input power not set for chain " + str(daisyChain))
        for i in range(numTx - 1):
            _, loOutPower = daisyChainSessions[i].GetLoOutPower(LOChannelName, 0.0)
            daisyChainSessions[i + 1].SetLoInPower(LOChannelName, loOutPower) # approximating that cable loss is negligible
            daisyChainSessions[i + 1].SetDouble(ModInst.niRFSGProperties.LoOutPower, LOChannelName, loOutPower)

# Download Waveforms and Configure Script
wlang.RFSGCreateAndDownloadMIMOWaveforms(rfsgHandles, None, numTx, "wlan")
for rfsgHandle, powerLevel in zip(rfsgHandles, powerLevels):
    script = "script GenerateWlan\nrepeat forever\ngenerate wlan\nend repeat\nend script"
    Toolkits.niWLANG.WLANG_RFSGConfigureScript(rfsgHandle, None, script, powerLevel)

# Initiate
if externalLOResourceName and LOSource == Toolkits.niWLANGConstants.LOSourceExternal:
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
if externalLOResourceName and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
    externalLOSession.close()
for rfsgSession in rfsgSessions:
    rfsgSession.close()
print ("Generation aborted.")
