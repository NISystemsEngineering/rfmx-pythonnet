# DEMO EXAMPLE: Client side execution of RFmx WLAN on a remote server
from pathlib import Path, PureWindowsPath
import rpyc

# # # # # User Parameters # # # # # #
hostName = 'NI-RFSE'                # Name or IP address of the RPyC server
hostPort = 18861                    # Port number of the RPyC server
generatorResourceName = '5840'      # Resource name of the Generator on the Host
analyzerResourceName = '5840'       # Resource name of the Analyzer on the Host
waveformFolder = Path('../waveforms')  # Example: waveformFolder = "c:/niremote/waveforms" , '.' denotes same directory as this .py file, if running on the server
waveformFileName = 'wlan80ax.tdms'  # Name of the .tdms waveform to play
                                    # Note that in this example all of the waveforms are on the server and need to be pathed as such

# # # # # RPyC Configuration # # # # #
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
WlanMX = conn.root.WlanMX
print("done")

# # # # # Global settings # # # # #
centerFrequency = 5.2e9

# # # # # Generation settings # # # # #
powerLevel = -10
externalAttenuation = 0
referenceClockSource = NIRfsg.RfsgFrequencyReferenceSource.OnboardClock
waveformName = "waveform"
script = 'script GenerateWaveform repeat forever generate waveform marker0(0) end repeat end script'

# # # # # Analysis settings # # # # #
print("Setting measurement parameters..", end = '')

referenceLevel = 0.0
externalAttenuation = 0.0

frequencyReferenceSource = InstrMX.RFmxInstrMXConstants.OnboardClock
frequencyReferenceFrequency = 10e6          #   /* (Hz) */

iqPowerEdgeEnabled = True
iqPowerEdgeLevel = -20.0            #   /*(dB) */
triggerDelay = 0.0                  #   /* (s) */
minimumQuietTimeMode = WlanMX.RFmxWlanMXTriggerMinimumQuietTimeMode.Auto
minimumQuietTime = 5.0e-6           #   /* (s) */

standard = WlanMX.RFmxWlanMXStandard.Standard802_11ax

channelBandwidth = 80e6             #   /*(Hz) */

phaseTrackingEnabled = 1
amplitudeTrackingEnabled = 0
symbolClockErrorCorrectionEnabled = 1
channelEstimationType = WlanMX.RFmxWlanMXOfdmModAccChannelEstimationType.ChannelEstimationReference

averagingEnabled = 1
averagingCount = 20

measurementOffset = 0               #   /* (symbols) */
maximumMeasurementLength = 16       #   /* (symbols) */
frequencyErrorEstimationMethod = WlanMX.RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod.PreambleAndPilots

timeout = 10.0

print("done")

# # # # # Execute Measurements # # # # #

# Initialize Generator
print("Initializing generator..", end = '')
rfsgSession = NIRfsg.NIRfsg(generatorResourceName, True, False, '')
rfsgHandle = rfsgSession.GetInstrumentHandle().DangerousGetHandle()
print("done")

# Initialize Analyzer
print("Initializing analyzer..", end = '')

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

# Get WLAN handle
wlan = InstrMX.RFmxWlanMXExtension.GetWlanSignalConfiguration(instrSession)
instrSession.ConfigureFrequencyReference("", frequencyReferenceSource, frequencyReferenceFrequency)

# Configure WLAN Measurement
wlan.ConfigureFrequency("", centerFrequency)
wlan.ConfigureReferenceLevel("", referenceLevel)
wlan.ConfigureExternalAttenuation("", externalAttenuation)

wlan.ConfigureIQPowerEdgeTrigger("", "0", WlanMX.RFmxWlanMXIQPowerEdgeTriggerSlope.Rising, iqPowerEdgeLevel,
            triggerDelay, minimumQuietTimeMode, minimumQuietTime, WlanMX.RFmxWlanMXIQPowerEdgeTriggerLevelType.Relative,
            iqPowerEdgeEnabled)
wlan.ConfigureStandard("", standard)
wlan.ConfigureChannelBandwidth("", channelBandwidth)
wlan.SelectMeasurements("", WlanMX.RFmxWlanMXMeasurementTypes.OfdmModAcc, True)

wlan.OfdmModAcc.Configuration.ConfigureMeasurementLength("", measurementOffset, maximumMeasurementLength)
wlan.OfdmModAcc.Configuration.ConfigureFrequencyErrorEstimationMethod("", frequencyErrorEstimationMethod)
wlan.OfdmModAcc.Configuration.ConfigureAmplitudeTrackingEnabled("", amplitudeTrackingEnabled)
wlan.OfdmModAcc.Configuration.ConfigurePhaseTrackingEnabled("", phaseTrackingEnabled)
wlan.OfdmModAcc.Configuration.ConfigureSymbolClockErrorCorrectionEnabled("",
              symbolClockErrorCorrectionEnabled)
wlan.OfdmModAcc.Configuration.ConfigureChannelEstimationType("", channelEstimationType)
wlan.OfdmModAcc.Configuration.ConfigureAveraging("", averagingEnabled, averagingCount)

print("done")

# Initiate and fetch results
print("Initiating and fetching results..", end = '')
rfsgSession.Initiate()
wlan.Initiate("", "")
instrSession.WaitForAcquisitionComplete(10)
rfsgSession.Abort()

#Fetch results

# Result variables
compositeRmsEvmMean = 0.0
compositeDataRmsEvmMean = 0.0
compositePilotRmsEvmMean = 0.0
numberOfSymbolsUsed = 0
frequencyErrorMean = 0.0
symbolClockErrorMean = 0.0

ppduType = WlanMX.RFmxWlanMXOfdmPpduType.NonHT
mcsIndex = 0
guardIntervalType = WlanMX.RFmxWlanMXOfdmGuardIntervalType.OneByFour

relativeIQOriginOffsetMean = 0.0
iqGainImbalanceMean = 0.
iqQuadratureErrorMean = 0.0
absoluteIQOriginOffsetMean = 0.0
iqTimingSkewMean = 0.0  


_, compositeRmsEvmMean, compositeDataRmsEvmMean, compositePilotRmsEvmMean = wlan.OfdmModAcc.Results.FetchCompositeRmsEvm("", timeout, 
            compositeRmsEvmMean, compositeDataRmsEvmMean, compositePilotRmsEvmMean)
_, numberOfSymbolsUsed =  wlan.OfdmModAcc.Results.FetchNumberOfSymbolsUsed("", timeout,  numberOfSymbolsUsed)
_, ppduType = wlan.OfdmModAcc.Results.FetchPpduType("", timeout, ppduType)
_, mcsIndex =  wlan.OfdmModAcc.Results.FetchMcsIndex("", timeout, mcsIndex)
_, guardIntervalType =  wlan.OfdmModAcc.Results.FetchGuardIntervalType("", timeout,  guardIntervalType)
_, frequencyErrorMean = wlan.OfdmModAcc.Results.FetchFrequencyErrorMean("", timeout, frequencyErrorMean)
_, symbolClockErrorMean = wlan.OfdmModAcc.Results.FetchSymbolClockErrorMean("", timeout, symbolClockErrorMean)
_, relativeIQOriginOffsetMean, iqGainImbalanceMean, iqQuadratureErrorMean, absoluteIQOriginOffsetMean, iqTimingSkewMean = wlan.OfdmModAcc.Results.FetchIQImpairments("", timeout, relativeIQOriginOffsetMean, 
            iqGainImbalanceMean, iqQuadratureErrorMean, absoluteIQOriginOffsetMean, iqTimingSkewMean)

print("done")

# Print Results
print("------------------EVM------------------\n")
print("------------------Composite EVM------------------\n")
print("RMS EVM Mean (dB)                      :{0}".format( compositeRmsEvmMean))
print("Data RMS EVM Mean (dB)                 :{0}".format(compositeDataRmsEvmMean))
print("Pilot RMS EVM Mean (dB)                :{0}".format(compositePilotRmsEvmMean))
print("\n------------------Impairments & PPDU Info------------------\n")
print("Frequency Error Mean(Hz)               :{0}".format(frequencyErrorMean))
print("Symbol Clock Error Mean(ppm)            :{0}".format( symbolClockErrorMean))
print("\n------------------IQ Impairments------------------")
print("Relative I/Q Origin Offset Mean (dB)    :{0}".format( relativeIQOriginOffsetMean))
print("Absolute I/Q Origin Offset Mean (dBm)   :{0}".format( absoluteIQOriginOffsetMean))
print("I/Q Gain Imbalance Mean (dB)            :{0}".format( iqGainImbalanceMean))
print("I/Q Quadrature Error Mean (deg)         :{0}".format( iqQuadratureErrorMean))
print("I/Q Timing Skew Mean (s)                :{0}".format( iqTimingSkewMean))
print("Number of Symbols Used                  :{0}".format( numberOfSymbolsUsed))
print("\n------------------PPDU Info------------------\n")
print("PPDU Type                               :{0}".format( ppduType))
print("MCS Index                               :{0}".format( mcsIndex))
print("Guard Interval Type                     :{0}".format( guardIntervalType))
print("")

#Close instrument session
instrSession.Close()

