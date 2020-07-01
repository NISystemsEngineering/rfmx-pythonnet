import clr, sys, os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.SpecAnMX.Fx40")

import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.RFmx.SpecAnMX as SpecAnMX

# Initialize input variables 
resource_name = "VST2_01"
selected_ports = ""
center_frequency = 1.95e+9              # Hz
reference_level = 0.00                  # dBm
external_attenuation = 0.00             # dB

measurement_interval = 1e-3             # seconds
rbw = 100e+6                           # Hz 
timeout = 10                           # seconds 

averaging_enabled = False
averaging_type = SpecAnMX.RFmxSpecAnMXTxpAveragingType.Rms
averaging_count = 10

frequency_source = InstrMX.RFmxInstrMXConstants.OnboardClock
frequency = 10e+6                      # Hz 

rbw_filter_type = 5 # SpecAnMX.RFmxSpecAnMXTxpRbwFilterType.None
rrc_alpha = 0.010

vbw_auto = True
vbw = 30.0e3                           # Hz 
vbw_to_rbw_ratio = 3

threshold_enabled = False
threshold_type = SpecAnMX.RFmxSpecAnMXTxpThresholdType.Relative
threshold_level = -20.0                 # (dBm or dBm / Hz)

digital_edge_enabled = True
digital_edge_source = "PXI_Trig0"
trigger_delay = 2e-3                     # seconds

# Create a new RFmx Session 
instr = InstrMX.RFmxInstrMX(resource_name, "")

# Get SpecAn signal 
specAn = InstrMX.RFmxSpecAnMXExtension.GetSpecAnSignalConfiguration(instr)

# Configure measurement 
instr.ConfigureFrequencyReference("", frequency_source, frequency)
specAn.SetSelectedPorts("", selected_ports)
specAn.ConfigureFrequency("", center_frequency)
specAn.ConfigureReferenceLevel("", reference_level)
specAn.ConfigureExternalAttenuation("", external_attenuation)
if digital_edge_enabled:
    specAn.ConfigureDigitalEdgeTrigger("", digital_edge_source, SpecAnMX.RFmxSpecAnMXDigitalEdgeTriggerEdge.Rising, trigger_delay, True)
else:
    specAn.DisableTrigger("")
specAn.SelectMeasurements("", SpecAnMX.RFmxSpecAnMXMeasurementTypes.Txp, False)
specAn.Txp.Configuration.ConfigureMeasurementInterval("", measurement_interval)
specAn.Txp.Configuration.ConfigureRbwFilter("", rbw, rbw_filter_type, rrc_alpha)
specAn.Txp.Configuration.ConfigureAveraging("", averaging_enabled, averaging_count, averaging_type)
specAn.Txp.Configuration.ConfigureVbwFilter("", vbw_auto, vbw, vbw_to_rbw_ratio)
specAn.Txp.Configuration.ConfigureThreshold("", threshold_enabled, threshold_level, threshold_type)
specAn.Initiate("", "")

# Retrieve results
_, average_mean_power, peak_to_average_ratio, maximum_power, minimum_power = specAn.Txp.Results.FetchMeasurement("", timeout, 0.0, 0.0, 0.0, 0.0)

print("Average Mean Power    : {:.3f}dBm".format(average_mean_power))
print("Peak to Average Ratio : {:.3f}dB".format(peak_to_average_ratio))
print("Maximum Power         : {:.3f}dBm".format(maximum_power))
print("Minimum Power         : {:.3f}dBm".format(minimum_power))

# Close session
specAn.Dispose()
instr.Close()
