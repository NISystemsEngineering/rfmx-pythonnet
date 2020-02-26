import clr, sys, os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.SpecAnMX.Fx40")

import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.RFmx.SpecAnMX as SpecAnMX

# Initialize input variables 
resourceName = "VST2_01"
selectedPorts = ""
centerFrequency = 1.95e+9              # Hz 
referenceLevel = 0.00                  # dBm 
externalAttenuation = 0.00             # dB 

measurementInterval = 1e-3             # seconds 
rbw = 100e+6                           # Hz 
timeout = 10                           # seconds 

averagingEnabled = False
averagingType = SpecAnMX.RFmxSpecAnMXTxpAveragingType.Rms
averagingCount = 10

frequencySource = InstrMX.RFmxInstrMXConstants.OnboardClock
frequency = 10e+6                      # Hz 

rbwFilterType = 5 # SpecAnMX.RFmxSpecAnMXTxpRbwFilterType.None
rrcAlpha = 0.010

vbwAuto = True
vbw = 30.0e3                           # Hz 
vbwToRbwRatio = 3

thresholdEnabled = False
thresholdType = SpecAnMX.RFmxSpecAnMXTxpThresholdType.Relative
thresholdLevel = -20.0                 # (dBm or dBm / Hz) 

digitalEdgeEnabled = True
digitalEdgeSource = "PXI_Trig0"
triggerDelay = 2e-3                     # seconds 

# Create a new RFmx Session 
instrSession = InstrMX.RFmxInstrMX(resourceName, "")

# Get SpecAn signal 
specAn = InstrMX.RFmxSpecAnMXExtension.GetSpecAnSignalConfiguration(instrSession)

# Configure measurement 
instrSession.ConfigureFrequencyReference("", frequencySource, frequency)
specAn.SetSelectedPorts("", selectedPorts)
specAn.ConfigureFrequency("", centerFrequency)
specAn.ConfigureReferenceLevel("", referenceLevel)
specAn.ConfigureExternalAttenuation("", externalAttenuation)
if digitalEdgeEnabled:
    specAn.ConfigureDigitalEdgeTrigger("", digitalEdgeSource, SpecAnMX.RFmxSpecAnMXDigitalEdgeTriggerEdge.Rising, triggerDelay, True)
else:
    specAn.DisableTrigger("")
specAn.SelectMeasurements("", SpecAnMX.RFmxSpecAnMXMeasurementTypes.Txp, False)
specAn.Txp.Configuration.ConfigureMeasurementInterval("", measurementInterval)
specAn.Txp.Configuration.ConfigureRbwFilter("", rbw, rbwFilterType, rrcAlpha)
specAn.Txp.Configuration.ConfigureAveraging("", averagingEnabled, averagingCount, averagingType)
specAn.Txp.Configuration.ConfigureVbwFilter("", vbwAuto, vbw, vbwToRbwRatio)
specAn.Txp.Configuration.ConfigureThreshold("", thresholdEnabled, thresholdLevel, thresholdType)
specAn.Initiate("", "")

# Retrieve results
_, averageMeanPower, peakToAverageRatio, maximumPower, minimumPower = specAn.Txp.Results.FetchMeasurement("", timeout, 0.0, 0.0, 0.0, 0.0)

print("Average Mean Power    : {:.3f}dBm".format(averageMeanPower))
print("Peak to Average Ratio : {:.3f}dB".format(peakToAverageRatio))
print("Maximum Power         : {:.3f}dBm".format(maximumPower))
print("Minimum Power         : {:.3f}dBm".format(minimumPower))

# Close session
specAn.Dispose()
instrSession.Close()
