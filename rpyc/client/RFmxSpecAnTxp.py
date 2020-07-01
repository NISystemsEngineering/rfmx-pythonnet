"""
Example for taking a transmit power measurement with RFmx SpecAn.
Settings configured for 100M 5GNR signal
"""

import rpyc

# connect and import libraries
host_name = 'localhost'
host_port = 18861
conn = rpyc.connect(host_name, host_port)
clr = conn.root.clr
System = conn.root.System
InstrMX = conn.root.InstrMX
SpecAnMX = conn.root.SpecAnMX

# Initialize input variables
resource_name = "VST2_01"
selected_ports = ""
center_frequency = 3.5e+9              # Hz
reference_level = 0.00                 # dBm
external_attenuation = 0.00            # dB

measurement_interval = 10e-3           # seconds
rbw = 100e+6                           # Hz
timeout = 10.0                         # seconds

averaging_enabled = False
averaging_type = SpecAnMX.RFmxSpecAnMXTxpAveragingType.Rms
averaging_count = 10

frequency_source = InstrMX.RFmxInstrMXConstants.OnboardClock
frequency = 10e+6                      # Hz

rbw_filter_type = System.Enum.Parse(clr.GetClrType(SpecAnMX.RFmxSpecAnMXTxpRbwFilterType), 'None')  # None is reserved python keyword
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

# create session objects
instr = InstrMX.RFmxInstrMX.GetSession(resource_name, "")
specAn = InstrMX.RFmxSpecAnMXExtension.GetSpecAnSignalConfiguration(instr)

try:
    # configure measurement
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

    # initiate and fetch results
    specAn.Initiate("", "")
    _, average_mean_power, peak_to_average_ratio, maximum_power, minimum_power = specAn.Txp.Results.FetchMeasurement("", timeout, 0.0, 0.0, 0.0, 0.0)

    # print to console
    print("Average Mean Power    : {:.3f}dBm".format(average_mean_power))
    print("Peak to Average Ratio : {:.3f}dB".format(peak_to_average_ratio))
    print("Maximum Power         : {:.3f}dBm".format(maximum_power))
    print("Minimum Power         : {:.3f}dBm".format(minimum_power))
finally:
    # close sessions and connection to server
    instr.Close()
    conn.close()
