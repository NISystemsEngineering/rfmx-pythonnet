import clr, os.path
from sys import path

path.append(os.path.abspath(__file__ + "\\..\\..\\..\\bin"))
clr.AddReference("NationalInstruments.RFToolkits.Interop.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.Interop.Fx40")

import NationalInstruments.RFToolkits.Interop as Toolkits
import NationalInstruments.ModularInstruments.Interop as ModInst
import System.Runtime.InteropServices as InteropServices

# Instrument Parameters
rfsaResourceNames = ["VST1_02", "VST1_01"]
externalLOResourceName = None
masterReferenceClockSource = ModInst.niRFSAConstants.PxiClkStr
externalLOReferenceClockSource = ModInst.niRFSGConstants.OnBoardClockStr
carrierFrequency = 5.18e+9
referenceLevels = [0.0, 0.0]
externalAttenuations = [0.0, 0.0]
triggerLines = [2, 3, 4] # PXI trigger lines for routing synchronization lines on VST1 models
LOSource = Toolkits.niWLANAConstants.LOSourceOnboard
LOExportToExternalDeviceEnabled = False
rfsaLODaisyEnabled = False

# Measurement Parameters
standard = Toolkits.niWLANAConstants.Standard80211axMimoOfdm
numRx = len(rfsaResourceNames)
chBW = 80.00e+6
ofdmNoOfAverages = 10
ofdmMaxSymbolsUsed = 16
optimizeReferenceLevelForEVMEnabled = False
optimizeReferenceLevelForEVMMargin = 0
noiseCompensationEnabled = False
autoLevelEnabled = False

# Configure Toolkit Session
wlana = Toolkits.niWLANA(Toolkits.niWLANAConstants.CompatibilityVersion050000)
wlana.SetStandard(None, standard)
wlana.SetNumberOfReceiveChannels(None, numRx)
wlana.SetChannelBandwidth(None, chBW)
wlana.SetCarrierFrequency(None, carrierFrequency)
wlana.SetIQPowerEdgeReferenceTriggerEnabled(None, True)
wlana.SetTClkSynchronizationEnabled(None, True)
wlana.SetOptimizeReferenceLevelForEVMEnabled(None, optimizeReferenceLevelForEVMEnabled)
wlana.SetOptimizeReferenceLevelForEVMMargin(None, optimizeReferenceLevelForEVMMargin)
wlana.SetNoiseCompensationEnabled(None, noiseCompensationEnabled)
wlana.SetLOOffsetMode(None, Toolkits.niWLANAConstants.LOFrequencyOffsetModeAuto)
wlana.SetOfdmDemodEnabled(None, True)
wlana.SetOfdmDemodNumberOfAverages(None, ofdmNoOfAverages)
wlana.SetOfdmDemodMaximumSymbolsUsed(None, ofdmMaxSymbolsUsed)
wlana.SetOFDMDemodAutoComputeMeasurementLengthEnabled(None, True)

# Configure External LO
externalLOHandle = InteropServices.HandleRef()
if externalLOResourceName is not None and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
    externalLOSession = ModInst.niRFSG(externalLOResourceName, True, False)
    externalLOSession.ConfigureRefClock(externalLOReferenceClockSource, 10e6)
    externalLOSession.SetGenerationMode(None, ModInst.niRFSGConstants.Cw)
    externalLOHandle = externalLOSession.Handle

# Configure Analyzer Sessions
rfsaSessions = [ModInst.niRFSA(resourceName, True, False) for resourceName in rfsaResourceNames]
rfsaHandles = [rfsaSession.Handle for rfsaSession in rfsaSessions]
wlana.RFSAConfigureMultipleDeviceSynchronization(rfsaHandles, numRx, masterReferenceClockSource, triggerLines, len(triggerLines))
wlana.RFSAConfigureFrequencySingleLO(rfsaHandles, LOSource, externalLOHandle, carrierFrequency, rfsaLODaisyEnabled, LOExportToExternalDeviceEnabled)
for i in range(numRx):
    rfsaSessions[i].SetExternalGain("0", -externalAttenuations[i])
    if autoLevelEnabled:
        _, actualReferencePowerLevel = wlana.RFSAAutoLevelv2(rfsaHandles[i], None, 10e-3, 5)
    else:
        _, actualReferencePowerLevel = wlana.RFSAConfigureOptimalEVMReferenceLevel(rfsaHandles[i], None, referenceLevels[i], 0.0)
    if i == 0:
        rfsaSessions[i].ConfigureIQPowerEdgeRefTrigger("0", actualReferencePowerLevel - 20.00, ModInst.niRFSAConstants.RisingSlope, 0)
    print(rfsaResourceNames[i] + " actual reference level (dBm): " + str(actualReferencePowerLevel))
if externalLOResourceName is not None:
    externalLOSession.Initiate()
    
# Measure and Print Results
wlana.RFSAMIMOMeasure(rfsaHandles, None, numRx, 10)
_, detectedNumberOfSymbolsUsed = wlana.GetOFDMDemodNumberOfSymbolsUsed(None, 0)
print("Number of Symbols Used: " + str(detectedNumberOfSymbolsUsed))
_, numberOfSpaceTimeStreams = wlana.GetCurrentIterationOFDMDemodNumberOfSpaceTimeStreams(None, 0)
for i in range(numberOfSpaceTimeStreams):
    channelString = "Stream" + str(i)
    _, rmsEvm = wlana.GetResultOfdmDemodRmsEvmAverage(channelString, 0.0)
    print(channelString + " RMS EVM: " + str(rmsEvm))

# Close Sessions
wlana.Close()
if externalLOResourceName is not None:
    externalLOSession.close()
(rfsaSession.Close() for rfsaSession in rfsaSessions)
