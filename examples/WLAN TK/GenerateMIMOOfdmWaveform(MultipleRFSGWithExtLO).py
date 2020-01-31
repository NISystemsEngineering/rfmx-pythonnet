
import clr, os.path
from sys import path

path.append(os.path.abspath(__file__ + "\\..\\..\\..\\bin"))
clr.AddReference("NationalInstruments.RFToolkits.Interop.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.Interop.Fx40")

import NationalInstruments.RFToolkits.Interop as Toolkits
import NationalInstruments.ModularInstruments.Interop as ModInst
import System.Runtime.InteropServices as InteropServices

# Generator Parameters
rfsgResourceNames = ["VST1_01", "VST1_02"]
powerLevels = [-10, -10]
externalAttenuation = [0, 0]
referenceClockSource = ModInst.niRFSGConstants.PxiClkStr
syncTriggerLines = [0, 1]

# LO Parameters
LOSource = Toolkits.niWLANGConstants.LOSourceOnboard
rfsgLODaisyChainEnabled = False
LOExportToExternalDevicesEnabled = False

# Parameters
carrierFrequency = 5.18e+9
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
wlang.SetRFBlankingEnabled(None, True)

# Configure Generator Sessions
rfsgSessions = [ModInst.niRFSG] * numTx
for i in range(numTx):
    rfsgSessions[i] = ModInst.niRFSG(rfsgResourceNames[i], True, False)
    rfsgSessions[i].ConfigurePowerLevelType(ModInst.niRFSGConstants.PeakPower)
    rfsgSessions[i].ConfigureGenerationMode(ModInst.niRFSGConstants.Script)
    rfsgSessions[i].SetExternalGain("", -(externalAttenuation[i]))

# Create and Download Waveform
rfsgHandles = [rfsgSession.Handle for rfsgSession in rfsgSessions]
wlang.ConfigureMultipleDeviceSynchronization(rfsgHandles, numTx, referenceClockSource, syncTriggerLines, len(syncTriggerLines))
wlang.RFSGConfigureFrequencySingleLO(rfsgHandles, LOSource, InteropServices.HandleRef(), carrierFrequency, rfsgLODaisyChainEnabled, LOExportToExternalDevicesEnabled)
wlang.RFSGCreateAndDownloadMIMOWaveforms(rfsgHandles, None, numTx, "wlan")
for i in range(numTx):
    script = "script GenerateWlan\nrepeat forever\ngenerate wlan\nend repeat\nend script"
    Toolkits.niWLANG.WLANG_RFSGConfigureScript(rfsgHandles[i], None, script, powerLevels[i])
wlang.RFSGMultipleDeviceInitiate(rfsgHandles)

input("Press any key to exit.")
for i in range(numTx):
    rfsgSessions[i].close()

wlang.Close()