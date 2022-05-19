"""
Demonstrates how to take a single carrier ACP measurement with two offsets using RFmx SpecAn.
"""

import clr
import sys
import os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.SpecAnMX.Fx40")
clr.AddReference("NationalInstruments.Common")

import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.RFmx.SpecAnMX as SpecAnMX

# VSA Settings
resource_name = '5831'
selected_ports = "rf1/port0"

center_frequency = 28e9                                                 # (Hz)
reference_level = 0.0                                                   # (dBm)
external_attenuation = 0.0                                              # (dB)

frequency_reference_source = InstrMX.RFmxInstrMXConstants.PxiClock
frequency_reference_frequency = 10e6                                      # (Hz)

# Carrier Channels
carrier_integration_bandwidth = 98300000                                  # (Hz)
carrier_rrc_filter_enabled = False
carrier_rrc_filter_alpha = 0.22

power_units = SpecAnMX.RFmxSpecAnMXAcpPowerUnits.dBm  # Set to dBm or dBm/Hz
noise_compensation_enabled = False

# Sweep Time
sweep_time_auto = True
sweep_time_interval = 0.001                                               # (Seconds)

# RBW Filter
rbw = 10000                                                             # (Hz)
rbw_filter_type = SpecAnMX.RFmxSpecAnMXAcpRbwFilterType.Gaussian
rbw_auto = True

# Offset Channels
offset_integration_bandwidth = 98300000                                  # (Hz)
offset_rrc_filter_enabled = False
offset_rrc_filter_alpha = 0.22

number_of_offsets = 2
frequency_offset = [100000000.0, 200000000.0]
offset_sideband = [SpecAnMX.RFmxSpecAnMXAcpOffsetSideband.Both, SpecAnMX.RFmxSpecAnMXAcpOffsetSideband.Both]
offset_enabled = [True, True]

averagingEnabled = False
averagingCount = 10
averagingType = SpecAnMX.RFmxSpecAnMXAcpAveragingType.Rms

# Triggering
iqPowerEdgeEnabled = False
iqPowerEdgeLevel = -20.0                                               # (dB)
triggerDelay = 0.0                                                     # (s)
minimumQuietTimeMode = SpecAnMX.RFmxSpecAnMXTriggerMinimumQuietTimeMode.Auto
minimumQuietTime = 5.0e-6                                              # (s)

timeout = 10.0                                                         # (s)

# --------------------------------------------------------------------------
# Init session

instr_session = InstrMX.RFmxInstrMX(resource_name, '')

# --------------------------------------------------------------------------
# Configure RFmx SpecAn acquisition

specAn = InstrMX.RFmxSpecAnMXExtension.GetSpecAnSignalConfiguration(instr_session)

instr_session.ConfigureFrequencyReference("", frequency_reference_source, frequency_reference_frequency)
instr_session.SetLOSource("lo1", "Secondary")

specAn.SetSelectedPorts("", selected_ports)

specAn.ConfigureFrequency("", center_frequency)
specAn.ConfigureReferenceLevel("", reference_level)
specAn.ConfigureExternalAttenuation("", external_attenuation)
specAn.ConfigureIQPowerEdgeTrigger("", "0",iqPowerEdgeLevel, SpecAnMX.RFmxSpecAnMXIQPowerEdgeTriggerSlope.Rising,
                                   triggerDelay, minimumQuietTimeMode, minimumQuietTime, iqPowerEdgeEnabled)

specAn.SelectMeasurements("", SpecAnMX.RFmxSpecAnMXMeasurementTypes.Acp, True)

specAn.ConfigureReferenceLevel("", reference_level)
specAn.Acp.Configuration.ConfigurePowerUnits("", power_units)
specAn.Acp.Configuration.ConfigureAveraging("",averagingEnabled, averagingCount, averagingType)
specAn.Acp.Configuration.ConfigureRbwFilter("", rbw_auto, rbw, rbw_filter_type)
specAn.Acp.Configuration.ConfigureNoiseCompensationEnabled("", noise_compensation_enabled)
specAn.Acp.Configuration.ConfigureCarrierIntegrationBandwidth("", carrier_integration_bandwidth)
specAn.Acp.Configuration.ConfigureCarrierRrcFilter("", carrier_rrc_filter_enabled, carrier_rrc_filter_alpha)
specAn.Acp.Configuration.ConfigureNumberOfOffsets("", number_of_offsets)
specAn.Acp.Configuration.ConfigureOffsetArray("", frequency_offset, offset_sideband, offset_enabled)
specAn.Acp.Configuration.ConfigureOffsetIntegrationBandwidth("offset::all", offset_integration_bandwidth)
specAn.Acp.Configuration.ConfigureOffsetRrcFilter("offset::all", offset_rrc_filter_enabled, offset_rrc_filter_alpha)

# Execute acquisition
specAn.Initiate('', '')

# Fetch results
_, absolute_power, total_relative_power, carrier_frequency, integration_bandwidth = specAn.Acp.Results.FetchCarrierMeasurement("", timeout, 0.0, 0.0, 0.0, 0.0)
_, lower_relative_power, upper_relative_power, lower_absolute_power, upper_absolute_power = specAn.Acp.Results.FetchOffsetMeasurementArray("", timeout, None, None, None, None)

# Report results to the user
print("-------Carrier Measurements-------\n")
print("Absolute Power (dBm or dBm/Hz): ", absolute_power, "\n")
for offset_idx in range(len(frequency_offset)):
    print("-------Offset Measurements-------\n")
    print(f"Offset {offset_idx} Lower Relative Power: {lower_relative_power[offset_idx]} dB")
    print(f"Offset {offset_idx} Upper Relative Power: {upper_relative_power[offset_idx]} dB")
    print(f"Offset {offset_idx} Lower Absolute Power: {lower_absolute_power[offset_idx]} dBm or dBm/Hz")
    print(f"Offset {offset_idx} Upper Absolute Power: {upper_absolute_power[offset_idx]} dBm or dBm/Hz")

# Close instrument session
instr_session.Close()
