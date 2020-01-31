import clr, os.path
from sys import path

path.append(os.path.abspath(__file__ + "\\..\\..\\..\\bin"))
clr.AddReference("NationalInstruments.RFToolkits.Interop.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.Interop.Fx40")

import NationalInstruments.RFToolkits.Interop as Toolkits
import NationalInstruments.ModularInstruments.Interop as ModInst
import System.Runtime.InteropServices as InteropServices

# Instrument Parameters
rfsaResourceNames = ["VST_01", "VST_02"]
masterReferenceClockSource = ModInst.niRFSAConstants.PxiClkStr
carrierFrequency = 5.18e+9
referenceLevels = [0.0, 0.0]
externalAttenuations = [0.0, 0.0]
triggerLines = [2, 3, 4] # PXI trigger lines for routing synchronization lines on VST1 models

# LO Distribution Parameters
LOSource = Toolkits.niWLANAConstants.LOSourceExternal # sets LO source to LO_in for each analyzer
externalLOResourceName = "LO_01" # implies WLANA will control the external LO
externalLOReferenceClockSource = ModInst.niRFSGConstants.OnBoardClockStr
LOChannelName = "lo2"
rfsaLODaisyEnabled = True
LOExportToExternalDeviceEnabled = False # specifies whether to export the LO on last analyzer in the daisy chain

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
    rfsaSessions[i].SetExternalGain(None, -externalAttenuations[i])
    if autoLevelEnabled:
        _, actualReferencePowerLevel = wlana.RFSAAutoLevelv2(rfsaHandles[i], None, 10e-3, 5)
    else:
        _, actualReferencePowerLevel = wlana.RFSAConfigureOptimalEVMReferenceLevel(rfsaHandles[i], None, referenceLevels[i], 0.0)
    if i == 0:
        rfsaSessions[i].ConfigureIQPowerEdgeRefTrigger('0', actualReferencePowerLevel - 20.00, ModInst.niRFSAConstants.RisingSlope, 0)
    print(rfsaResourceNames[i] + " actual reference level (dBm): " + str(actualReferencePowerLevel))

# # Cascade LO Power Levels for Optimal Performance
# if rfsaLODaisyEnabled:
#     if externalLOResourceName is not None and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
#         _, loOutPower = externalLOSession.GetPowerLevel(None, 0.0)
#         rfsaSessions[0].SetLoInPower(LOChannelName, loOutPower)
#         rfsaSessions[0].SetLoOutPower(LOChannelName, loOutPower)
#     for i in range(numRx - 1):
#         _, loOutPower = rfsaSessions[i].GetLoOutPower(LOChannelName, 0.0)
#         rfsaSessions[i + 1].SetLoInPower(LOChannelName, loOutPower)
#         _, loInPower = rfsaSessions[i + 1].GetLoInPower(LOChannelName, 0.0)
# else:
#     pass # loss through splitter will need to be considered

# Measure and Print Results
if externalLOResourceName is not None and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
    externalLOSession.Initiate()
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
if externalLOResourceName is not None and LOSource == Toolkits.niWLANAConstants.LOSourceExternal:
    externalLOSession.close()
for rfsaSession in rfsaSessions:
    rfsaSession.Close()
