import clr, sys, os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")
sys.path.append(os.path.abspath(__file__ + "\\..\\..\\..\\lib"))

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.NRMX.Fx40")
clr.AddReference("NationalInstruments.Common")

import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.RFmx.NRMX as NRMX
from matplotlib import pyplot
from aeutils.nicommon import traces

# Initialize input variables
resourceName = "VST2_01"
selectedPorts = ""

frequencyReferenceSource = InstrMX.RFmxInstrMXConstants.OnboardClock
frequencyReferenceFrequency = 10e6

centerFrequency = 1.95e9
referenceLevel = -20.0
externalAttenuation = 0.0

enableTrigger = True
digitalEdgeSource = NRMX.RFmxNRMXConstants.PxiTriggerLine0
digitalEdge = NRMX.RFmxNRMXDigitalEdgeTriggerEdge.Rising
triggerDelay = 0.0

frequencyRange = NRMX.RFmxNRMXFrequencyRange.Range1
band = 78
cellID = 0
carrierBandwidth = 100e6                                        
subcarrierSpacing = 30e3
                                
autoResourceBlockDetectionEnabled = True

puschTransformPrecodingEnabled = False
puschModulationType = NRMX.RFmxNRMXPuschModulationType.Qpsk
NumberOfResourceBlockClusters = 1
puschResourceBlockOffset = [0]
puschNumberOfResourceBlocks = [-1]
puschSlotAllocation = "0-Last"
puschSymbolAllocation = "0-Last"

puschDmrsPowerMode = NRMX.RFmxNRMXPuschDmrsPowerMode.CdmGroups
puschDmrsPower = 0.0
puschDmrsConfigurationType = NRMX.RFmxNRMXPuschDmrsConfigurationType.Type1
puschMappingType = NRMX.RFmxNRMXPuschMappingType.TypeA
puschDmrsTypeAPosition = 2
puschDmrsDuration = NRMX.RFmxNRMXPuschDmrsDuration.SingleSymbol
puschDmrsAdditionalPositions = 0

synchronizationMode = NRMX.RFmxNRMXModAccSynchronizationMode.Slot

measurementLengthUnit = NRMX.RFmxNRMXModAccMeasurementLengthUnit.Slot
measurementOffset = 0
measurementLength = 1

averagingEnabled = False
averagingCount = 10

timeout = 10.0

# Create a new RFmx Session 
instrSession = InstrMX.RFmxInstrMX(resourceName, "")

# Get NR signal 
nr = InstrMX.RFmxNRMXExtension.GetNRSignalConfiguration(instrSession)

# Configure measurement 
instrSession.ConfigureFrequencyReference("", frequencyReferenceSource, frequencyReferenceFrequency)
nr.SetSelectedPorts("", selectedPorts)

nr.ConfigureRF("", centerFrequency, referenceLevel, externalAttenuation)
nr.ConfigureDigitalEdgeTrigger("", digitalEdgeSource, digitalEdge, triggerDelay, enableTrigger)

nr.SetFrequencyRange("", frequencyRange)
nr.ComponentCarrier.SetBandwidth("", carrierBandwidth)
nr.ComponentCarrier.SetCellID("", cellID)
nr.SetBand("", band)
nr.ComponentCarrier.SetBandwidthPartSubcarrierSpacing("", subcarrierSpacing)
nr.SetAutoResourceBlockDetectionEnabled("", autoResourceBlockDetectionEnabled)

nr.ComponentCarrier.SetPuschTransformPrecodingEnabled("", puschTransformPrecodingEnabled)
nr.ComponentCarrier.SetPuschSlotAllocation("", puschSlotAllocation)
nr.ComponentCarrier.SetPuschSymbolAllocation("", puschSymbolAllocation)
nr.ComponentCarrier.SetPuschModulationType("", puschModulationType)

nr.ComponentCarrier.SetPuschNumberOfResourceBlockClusters("", NumberOfResourceBlockClusters)

subblockString = NRMX.RFmxNRMX.BuildSubblockString("", 0)
carrierString = NRMX.RFmxNRMX.BuildCarrierString(subblockString, 0)
bandwidthPartString = NRMX.RFmxNRMX.BuildBandwidthPartString(carrierString, 0)
userString = NRMX.RFmxNRMX.BuildUserString(bandwidthPartString, 0)
puschString = NRMX.RFmxNRMX.BuildPuschString(userString, 0)
for i in range(NumberOfResourceBlockClusters):
    puschClusterString = NRMX.RFmxNRMX.BuildPuschClusterString(puschString, i)
    nr.ComponentCarrier.SetPuschResourceBlockOffset(puschClusterString, puschResourceBlockOffset[i])
    nr.ComponentCarrier.SetPuschNumberOfResourceBlocks(puschClusterString, puschNumberOfResourceBlocks[i])

nr.ComponentCarrier.SetPuschDmrsPowerMode("", puschDmrsPowerMode)
nr.ComponentCarrier.SetPuschDmrsPower("", puschDmrsPower)
nr.ComponentCarrier.SetPuschDmrsConfigurationType("", puschDmrsConfigurationType)
nr.ComponentCarrier.SetPuschMappingType("", puschMappingType)
nr.ComponentCarrier.SetPuschDmrsTypeAPosition("", puschDmrsTypeAPosition)
nr.ComponentCarrier.SetPuschDmrsDuration("", puschDmrsDuration)
nr.ComponentCarrier.SetPuschDmrsAdditionalPositions("", puschDmrsAdditionalPositions)
nr.SelectMeasurements("", NRMX.RFmxNRMXMeasurementTypes.ModAcc, True)

nr.ModAcc.Configuration.SetSynchronizationMode("", synchronizationMode)
nr.ModAcc.Configuration.SetAveragingEnabled("", averagingEnabled)
nr.ModAcc.Configuration.SetAveragingCount("", averagingCount)

nr.ModAcc.Configuration.SetMeasurementLengthUnit("", measurementLengthUnit)
nr.ModAcc.Configuration.SetMeasurementOffset("", measurementOffset)
nr.ModAcc.Configuration.SetMeasurementLength("", measurementLength)

nr.Initiate("", "")

# Retrieve scalar results
# note: _ ignores the first returned value of the function. In this case it is an error code. Errors will still throw exceptions.
_, compositeRmsEvmMean = nr.ModAcc.Results.GetCompositeRmsEvmMean("", 0.0)
_, compositePeakEvmMaximum = nr.ModAcc.Results.GetCompositePeakEvmMaximum("", 0.0)
_, compositePeakEvmSlotIndex = nr.ModAcc.Results.GetCompositePeakEvmSlotIndex("", 0)
_, compositePeakEvmSymbolIndex = nr.ModAcc.Results.GetCompositePeakEvmSymbolIndex("", 0)
_, compositePeakEvmSubcarrierIndex = nr.ModAcc.Results.GetCompositePeakEvmSubcarrierIndex("", 0)

_, componentCarrierFrequencyErrorMean = nr.ModAcc.Results.GetComponentCarrierFrequencyErrorMean("", 0.0)
_, componentCarrierIQOriginOffsetMean = nr.ModAcc.Results.GetComponentCarrierIQOriginOffsetMean("", 0.0)
_, componentCarrierIQGainImbalanceMean = nr.ModAcc.Results.GetComponentCarrierIQGainImbalanceMean("", 0.0)
_, componentCarrierQuadratureErrorMean = nr.ModAcc.Results.GetComponentCarrierQuadratureErrorMean("", 0.0)
_, inBandEmissionMargin = nr.ModAcc.Results.GetInBandEmissionMargin("", 0.0)

# Print scalar results
print("------------------Measurement------------------")
print("Composite RMS EVM Mean (%)                     : {0}".format(compositeRmsEvmMean))
print("Composite Peak EVM Maximum (%)                 : {0}".format(compositePeakEvmMaximum))
print("Composite Peak EVM Slot Index                  : {0}".format(compositePeakEvmSlotIndex))
print("Composite Peak EVM Symbol Index                : {0}".format(compositePeakEvmSymbolIndex))
print("Composite Peak EVM Subcarrier Index            : {0}".format(compositePeakEvmSubcarrierIndex))
print("Component Carrier Frequency Error Mean (Hz)    : {0}".format(componentCarrierFrequencyErrorMean))
print("Component Carrier IQ Origin Offset Mean (dBc)  : {0}".format(componentCarrierIQOriginOffsetMean))
print("Component Carrier IQ Gain Imbalance Mean (dB)  : {0}".format(componentCarrierIQGainImbalanceMean))
print("Component Carrier Quadrature Error Mean (deg)  : {0}".format(componentCarrierQuadratureErrorMean))

# Fetch traces
_, puschDataConstellation = nr.ModAcc.Results.FetchPuschDataConstellationTrace("", timeout, None)
_, puschDmrsConstellation = nr.ModAcc.Results.FetchPuschDmrsConstellationTrace("", timeout, None)
_, rmsEvmPerSubcarrierMean = nr.ModAcc.Results.FetchRmsEvmPerSubcarrierMeanTrace("", timeout, None)
_, rmsEvmPerSymbolMean = nr.ModAcc.Results.FetchRmsEvmPerSymbolMeanTrace("", timeout, None)
_, spectralFlatness, spectralFlatnessLowerMask, spectralFlatnessUpperMask = nr.ModAcc.Results.FetchSpectralFlatnessTrace("", timeout, None, None, None)

#Close instrument session
instrSession.Close()

# Post-process traces
puschDataConstellation = traces.decompose_complex_array(puschDataConstellation)
puschDmrsConstellation = traces.decompose_complex_array(puschDmrsConstellation)
rmsEvmPerSubcarrierMean = traces.decompose_analog_waveform(rmsEvmPerSubcarrierMean)
rmsEvmPerSymbolMean = traces.decompose_analog_waveform(rmsEvmPerSymbolMean)
spectralFlatness = traces.decompose_spectrum(spectralFlatness)
spectralFlatnessLowerMask = traces.decompose_spectrum(spectralFlatnessLowerMask) 
spectralFlatnessUpperMask = traces.decompose_spectrum(spectralFlatnessUpperMask)

# Plot traces
fig, axs = pyplot.subplots(2, 2)
axs[0, 0].set_title("PUSCH Constellation")
axs[0, 0].plot(puschDataConstellation[0], puschDataConstellation[1], "ro")
axs[0, 0].plot(puschDmrsConstellation[0], puschDmrsConstellation[1], "bo")
axs[0, 1].set_title("RMS EVM per Subcarrier Mean")
axs[0, 1].plot(rmsEvmPerSubcarrierMean[0], rmsEvmPerSubcarrierMean[1])
axs[1, 0].set_title("RMS EVM per Symbol Mean")
axs[1, 0].plot(rmsEvmPerSymbolMean[0], rmsEvmPerSymbolMean[1])
axs[1, 1].set_title("Spectral Flatness")
axs[1, 1].plot(spectralFlatness[0], spectralFlatness[1])
axs[1, 1].plot(spectralFlatnessLowerMask[0], spectralFlatnessLowerMask[1])
axs[1, 1].plot(spectralFlatnessUpperMask[0], spectralFlatnessUpperMask[1])
pyplot.show()
