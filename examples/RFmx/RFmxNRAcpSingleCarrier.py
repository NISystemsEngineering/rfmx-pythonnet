import clr, sys, os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.NRMX.Fx40")

import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.RFmx.NRMX as NRMX

# Initialize VSA Settings
resourceName = '5831'
selectedPorts = 'rf1/port0'

centerFrequency = 28e9                                                 # (Hz)
referenceLevel = 0.0                                                   # (dBm)
externalAttenuation = 0.0                                              # (dB)
autoLevel = False
measurementInterval = 0.010                                            # (Seconds)

rfAttenuationAuto = True
rfAttenuation = 10

frequencyReferenceSource = InstrMX.RFmxInstrMXConstants.PxiClock
frequencyReferenceFrequency = 10e6                                     # (Hz)

# Triggering
iqPowerEdgeEnabled = False
iqPowerEdgeLevel = -20.0                                              # (dB)
triggerDelay = 0.0                                                     # (s)
minimumQuietTimeMode = NRMX.RFmxNRMXTriggerMinimumQuietTimeMode.Auto
minimumQuietTime = 5.0e-6                                              # (s)

sweepTimeAuto = True
sweepTimeInterval = 0.001                                               # (Seconds)

averagingEnabled = False
averagingCount = 10
averagingType = NRMX.RFmxNRMXAcpAveragingType.Rms

timeout = 10.0                                                          # (Seconds)

# Initialize NR Settings
frequencyRange = NRMX.RFmxNRMXFrequencyRange.Range2
carrierBandwidth = 100e6
subcarrierSpacing = 120e3
linkDirection = NRMX.RFmxNRMXLinkDirection.Downlink
measurementMethod = NRMX.RFmxNRMXAcpMeasurementMethod.Normal
noiseCompensationEnabled = False

# NR Offsets Configuration
numberOfNROffsets = 1
numberOfUtraOffsets = 0

# Init session
instrSession = InstrMX.RFmxInstrMX(resourceName, "")

# Configure RFmx NR acquisition
nr = NRMX.RFmxNRMXExtension.GetNRSignalConfiguration(instrSession)
instrSession.ConfigureFrequencyReference("", frequencyReferenceSource, frequencyReferenceFrequency)
nr.SetSelectedPorts("", selectedPorts)
nr.ConfigureFrequency("", centerFrequency)
nr.ConfigureExternalAttenuation("", externalAttenuation)
instrSession.ConfigureRFAttenuation("", rfAttenuationAuto, rfAttenuation)
nr.ConfigureIQPowerEdgeTrigger("", "0", NRMX.RFmxNRMXIQPowerEdgeTriggerSlope.Rising, iqPowerEdgeLevel,
                               triggerDelay, minimumQuietTimeMode, minimumQuietTime,
                               NRMX.RFmxNRMXIQPowerEdgeTriggerLevelType.Relative,
                               iqPowerEdgeEnabled)
nr.SetLinkDirection("", linkDirection)
nr.SetFrequencyRange("", frequencyRange)
nr.ComponentCarrier.SetBandwidth("", carrierBandwidth)
nr.ComponentCarrier.SetBandwidthPartSubcarrierSpacing("", subcarrierSpacing)

nr.ConfigureReferenceLevel("", referenceLevel)
nr.SelectMeasurements("", NRMX.RFmxNRMXMeasurementTypes.Acp, True)

nr.Acp.Configuration.ConfigureMeasurementMethod("", measurementMethod)
nr.Acp.Configuration.ConfigureNoiseCompensationEnabled("", noiseCompensationEnabled)
nr.Acp.Configuration.ConfigureSweepTime("", sweepTimeAuto, sweepTimeInterval)
nr.Acp.Configuration.ConfigureAveraging("", averagingEnabled, averagingCount, averagingType)
nr.Acp.Configuration.ConfigureNumberOfNROffsets("", numberOfNROffsets)
nr.Acp.Configuration.ConfigureNumberOfUtraOffsets("", numberOfUtraOffsets)

# Execute acquisition
nr.Initiate("", "")

# Result Variables
lowerRelativePower = []
upperRelativePower = []
lowerAbsolutePower = []
upperAbsolutePower = []
totalAggregatedPower = 0.0
carrierFrequency = 0.0
integrationBandwidth = 0.0
totalNumberOfOffsets = numberOfUtraOffsets + numberOfNROffsets

# Fetch results
_, totalAggregatedPower = nr.Acp.Results.FetchTotalAggregatedPower("", timeout, totalAggregatedPower)
_, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower = nr.Acp.Results.FetchOffsetMeasurementArray("", timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower)

# Report results to the user
print("-------Carrier Measurements-------\n")
print("Absolute Power (dBm or dBm/Hz): ", totalAggregatedPower,"\n")
for i in range(totalNumberOfOffsets):
    print(i)
    print("-------Offset Measurements-------\n")
    print("Lower Relative Power (dB) ", lowerRelativePower[i],"\n")
    print("Upper Relative Power(dB) ", upperRelativePower[i], "\n")
    print("Lower Absolute Power (dBm or dBm/Hz) ", lowerAbsolutePower[i],"\n")
    print("Upper Absolute Power (dBm or dBm/Hz) ", upperAbsolutePower[i],"\n")

instrSession.Close()
