
from pathlib import Path, PureWindowsPath
import rpyc

# # # # # User Parameters # # # # # #
hostName = 'NI-RFSE'                # Name or IP address of the RPyC server
hostPort = 18861                    # Port number of the RPyC server
generatorResourceName = '5840'      # Resource name of the Generator on the Host
analyzerResourceName = '5840'       # Resource name of the Analyzer on the Host
waveformFolder = Path('../waveforms')          # Example: waveformFolder = "c:/niremote/waveforms" , '.' denotes same directory as this .py file, if running on the server
waveformFileName = 'nr100.tdms'     # Name of the .tdms waveform to play
                                    # Note that in this example all of the waveforms are on the server and need to be pathed as such

# # # # # RPyC Configuration # # # # #
# Open connection to the service
print("Opening connection to RFmxService on " + hostName)
conn = rpyc.connect(hostName, hostPort)
print("Connection opened successfully")

# Instantiate exported classes from the service
print("Importing classes from service..", end = '')
System = conn.root.System
NationalInstruments = conn.root.NationalInstruments
NIRfsg = conn.root.NIRfsg
NIRfsgPlayback = conn.root.NIRfsgPlayback
InstrMX = conn.root.InstrMX
NRMX = conn.root.NRMX
print("done")

# # # # # Global settings # # # # #
centerFrequency = 3.5e9

# # # # # Generation settings # # # # #
powerLevel = -10
externalAttenuation = 0
referenceClockSource = NIRfsg.RfsgFrequencyReferenceSource.OnboardClock
waveformName = "waveform"
script = 'script GenerateWaveform repeat forever generate waveform marker0(0) end repeat end script'

# # # # # Analysis settings # # # # #
print("Setting measurement parameters..", end = '')

frequencyReferenceSource = InstrMX.RFmxInstrMXConstants.OnboardClock
frequencyReferenceFrequency = 10e6

selectedPorts = ""
referenceLevel = 0.0
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

print("done")

# # # # # Execute Measurements # # # # #

# Initialize Generator
print("Initializing generator..", end = '')
rfsgSession = NIRfsg.NIRfsg(generatorResourceName, True, False, '')
rfsgHandle = rfsgSession.GetInstrumentHandle().DangerousGetHandle()
print("done")

# Initialize Analyzer
print("Initializing analzer..", end = '')
instrSession = conn.root.RFmxRemoteInstrMX(analyzerResourceName, "")
instrSession.ResetDriver()
instrSession.ResetEntireSession()
print("done")

# Generation configuration
print("Configuring generator..", end = '')
rfsgSession.RF.Configure(centerFrequency, powerLevel)
rfsgSession.FrequencyReference.Configure(referenceClockSource, 10e6)
rfsgSession.RF.ExternalGain = -externalAttenuation
# The server will be running on Windows and needs a PureWindowsPath to locate the waveform
NIRfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsgHandle, str(PureWindowsPath(waveformFolder / waveformFileName)), waveformName)
NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsgHandle, script)
rfsgSession.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal = NIRfsg.RfsgMarkerEventExportedOutputTerminal.PxiTriggerLine0
print("done")

# Measurement configuration
print("Configuring analyzer..", end = '')

nr = InstrMX.RFmxNRMXExtension.GetNRSignalConfiguration(instrSession)

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

print("done")

# Initiate and fetch results
print("Initiating and fetching results..", end = '')

rfsgSession.Initiate()
nr.Initiate("", "")

instrSession.WaitForAcquisitionComplete(10)
rfsgSession.Abort()

# _ Ignores the first returned value of the function. In this case it is an error code. Errors will still throw exceptions.
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

# These could be visulaized using various viszualization tools.
# nr.ModAcc.Results.FetchPuschDataConstellationTrace("", timeout, ref puschDataConstellation)
# nr.ModAcc.Results.FetchPuschDmrsConstellationTrace("", timeout, ref puschDmrsConstellation)
# nr.ModAcc.Results.FetchRmsEvmPerSubcarrierMeanTrace("", timeout, ref rmsEvmPerSubcarrierMean)
# nr.ModAcc.Results.FetchRmsEvmPerSymbolMeanTrace("", timeout, ref rmsEvmPerSymbolMean)
# nr.ModAcc.Results.FetchSpectralFlatnessTrace("", timeout, ref spectralFlatness,
# ref spectralFlatnessLowerMask, ref spectralFlatnessUpperMask)

print("done")

# print scalar results

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

#Close instrument session
instrSession.Close()
