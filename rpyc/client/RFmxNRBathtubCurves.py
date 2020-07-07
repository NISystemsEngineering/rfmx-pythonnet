"""
Demonstrates 5GNR bathtub curves collection using an optional reference level optimization sweep
Written for use with NI mmWave VST (PXIe-5831)

Assumptions:
    External LO (PXIe-5653) is associated in NI MAX
    Downlink shared channels are user defined
    For multi-carrier, each carrier has unique and consecutive cell IDs starting from zero
    For multi-carrier, all carriers have the same carrier definition
"""

import rpyc
import enum
import math


class LocalOscillatorDistributionType(enum.Enum):
    Shared = 0
    Independent = 1


# connect and import libraries
host_name = 'localhost'
host_port = 18861
conn = rpyc.connect(host_name, host_port)
clr = conn.root.clr
System = conn.root.System
InstrMX = conn.root.InstrMX
NRMX = conn.root.NRMX
NIRfsg = conn.root.NIRfsg
NIRfsgPlayback = conn.root.NIRfsgPlayback

# common
frequencies = [28e9, 39e9]  # list of frequencies that will be swept
lo2_distribution_type = LocalOscillatorDistributionType.Shared

# RF signal generator
rfsg_resource_name = "BCN_01"
rfsg_reference_clock_source = "OnboardClock"
rfsg_selected_ports = "rf0/port0"
rfsg_power_levels = range(5, -50, -1)
rfsg_external_attenuations = [0.0] * len(frequencies)

# RF signal analyzer
rfsa_resource_name = "BCN_01"
rfsa_reference_clock_source = "OnboardClock"
rfsa_selected_ports = "rf1/port0"
rfsa_optimize_reference_level = True
rfsa_auto_level_enabled = True
rfsa_reference_level_headroom = 0.0  # applied after auto-level and before level optimization
rfsa_external_attenuations = [0.0] * len(frequencies)

# NR measurement
nr_link_direction = NRMX.RFmxNRMXLinkDirection.Downlink
nr_frequency_range = NRMX.RFmxNRMXFrequencyRange.Range2
nr_number_component_carriers = 1
nr_carrier_bandwidth = 400e6
nr_subcarrier_spacing = 120e3
nr_uplink_modulation_type = NRMX.RFmxNRMXPuschModulationType.Qam256
nr_downlink_modulation_type = NRMX.RFmxNRMXPdschModulationType.Qam256
nr_averaging_enabled = True
nr_averaging_count = 10

# file i/o
file_path_base = r'c:\niremote\waveforms\NR_DL_FR2_400M_120k_256QAM'  # path to waveform on the server
waveform_file_path = file_path_base + '.tdms'
results_file_path = 'results.csv'  # path to results file on the client

# open sessions
instr = InstrMX.RFmxInstrMX.GetSession(rfsa_resource_name, "")
rfsg = NIRfsg.NIRfsg(rfsg_resource_name, True, False)

# configure generator
rfsg.SignalPath.SelectedPorts = rfsg_selected_ports
rfsg.RF.Frequency = frequencies[0]
rfsg_handle = rfsg.GetInstrumentHandle().DangerousGetHandle()
NIRfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsg_handle, waveform_file_path, "wfm")
NIRfsgPlayback.NIRfsgPlayback.StoreWaveformLOOffsetMode(rfsg_handle, "wfm", NIRfsgPlayback.NIRfsgPlaybackLOOffsetMode.Auto)
NIRfsgPlayback.NIRfsgPlayback.StoreAutomaticSGSASharedLO(rfsg_handle, "", NIRfsgPlayback.RfsgPlaybackAutomaticSGSASharedLO.Disabled)
NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsg_handle, "script genWfm\nrepeat forever\ngenerate wfm marker0(0)\nend repeat\nend script")
_, waveform_papr = NIRfsgPlayback.NIRfsgPlayback.ReadPaprFromFile(waveform_file_path, 0, 0.0)
_, waveform_sample_rate = NIRfsgPlayback.NIRfsgPlayback.ReadSampleRateFromFile(waveform_file_path, 0, 0.0)
_, waveform_size = NIRfsgPlayback.NIRfsgPlayback.ReadWaveformSizeFromFile(waveform_file_path, 0, 0)
waveform_length_sec = waveform_size / waveform_sample_rate
rfsg.RF.LocalOscillator["LO1"].Source = NIRfsg.RfsgLocalOscillatorSource.FromString("Onboard")
if lo2_distribution_type == LocalOscillatorDistributionType.Shared:
    rfsg.RF.LocalOscillator["LO2"].Source = NIRfsg.RfsgLocalOscillatorSource.FromString("SG_SA_Shared")
else:
    rfsg.RF.LocalOscillator["LO2"].Souce = NIRfsg.RfsgLocalOscillatorSource.FromString("Onboard")

# configure analyzer
instr.ConfigureAutomaticSGSASharedLO("", InstrMX.RFmxInstrMXAutomaticSGSASharedLO.Disabled)
instr.SetLOSource("LO1", "Onboard")
if lo2_distribution_type == LocalOscillatorDistributionType.Shared:
    instr.SetLOSource("LO2", "SG_SA_Shared")
else:
    instr.SetLOSource("LO2", "Onboard")
instr.SetDownconverterFrequencyOffset("", rfsg.RF.Upconverter.FrequencyOffset)
nr = InstrMX.RFmxNRMXExtension.GetNRSignalConfiguration(instr)
nr.SetSelectedPorts("", rfsa_selected_ports)
nr.ConfigureFrequency("", frequencies[0])
nr.SetReferenceLevelHeadroom("", rfsa_reference_level_headroom)
nr.SetLinkDirection("", nr_link_direction)
nr.SetFrequencyRange("", nr_frequency_range)
nr.SetDownlinkChannelConfigurationMode("", NRMX.RFmxNRMXDownlinkChannelConfigurationMode.UserDefined)
nr.ConfigureDigitalEdgeTrigger("", rfsg.DeviceEvents.MarkerEvents[0].TerminalName, NRMX.RFmxNRMXDigitalEdgeTriggerEdge.Rising, 0.0, True)
nr.SetAutoResourceBlockDetectionEnabled("", False)  # use configuration from user rather than auto-detection
nr.SetAutoIncrementCellIDEnabled("", True)
nr.ComponentCarrier.SetNumberOfComponentCarriers("", nr_number_component_carriers)
carrier_string = NRMX.RFmxNRMX.BuildCarrierString("", -1)  # configure all carriers with the same settings
nr.ComponentCarrier.SetBandwidth(carrier_string, nr_carrier_bandwidth)
nr.ComponentCarrier.SetBandwidthPartSubcarrierSpacing(carrier_string, nr_subcarrier_spacing)
nr.ComponentCarrier.SetPuschModulationType(carrier_string, nr_uplink_modulation_type)
nr.ComponentCarrier.SetPdschModulationType(carrier_string, nr_downlink_modulation_type)
nr.ModAcc.Configuration.SetSynchronizationMode("", NRMX.RFmxNRMXModAccSynchronizationMode.Frame)
nr.ModAcc.Configuration.SetAveragingEnabled("", nr_averaging_enabled)
nr.ModAcc.Configuration.SetAveragingCount("", nr_averaging_count)
nr.Acp.Configuration.ConfigureAveraging("", nr_averaging_enabled, nr_averaging_count, NRMX.RFmxNRMXAcpAveragingType.Rms)
nr.Chp.Configuration.ConfigureAveraging("", nr_averaging_enabled, nr_averaging_count, NRMX.RFmxNRMXChpAveragingType.Rms)
nr.ModAcc.Configuration.SetMeasurementEnabled("", True)
nr.Chp.Configuration.SetMeasurementEnabled("", True)
nr.Commit("")

# write configuration information to file
f = open(results_file_path, 'w')
_, instrument_model = instr.GetInstrumentModel("", "")
_, lo1_source = instr.GetLOSource("LO1", "")
_, lo2_source = instr.GetLOSource("LO2", "")
_, downconverter_frequency_offset = instr.GetDownconverterFrequencyOffset("", 0.0)
f.write("Signal Analyzer\n")
f.write(f"Instrument Model,{instrument_model}\n")
f.write(f"LO1 Source,{lo1_source}\n")
f.write(f"LO2 Source,{lo2_source}\n")
f.write(f"Downconverter Frequency Offset (Hz),{downconverter_frequency_offset}\n")
f.write(f"External Attenuations (dB),{','.join([str(external_attenuation) for external_attenuation in rfsa_external_attenuations])}\n")

f.write("\nSignal Generator\n")
f.write(f"Instrument Model,{rfsg.Identity.InstrumentModel}\n")
f.write(f"Selected Ports,{rfsg.SignalPath.SelectedPorts}\n")
f.write(f'LO1 Source,{rfsg.RF.LocalOscillator["LO1"].Source}\n')
f.write(f'LO2 Source,{rfsg.RF.LocalOscillator["LO2"].Source}\n')
f.write(f"Upconverter Frequency Offset (Hz),{rfsg.RF.Upconverter.FrequencyOffset}\n")
f.write(f"External Attenuations (dB),{','.join([str(external_attenuation) for external_attenuation in rfsg_external_attenuations])}\n")

f.write("\nWaveform\n")
f.write('PAPR (dB),' + '{:1.3f}\n'.format(waveform_papr))
f.write(f"Sample Rate (Hz),{waveform_sample_rate}\n")
f.write(f"Length (s),{waveform_length_sec}\n")

_, selected_port = nr.GetSelectedPorts("", "")
_, reference_level_headroom = nr.GetReferenceLevelHeadroom("", 0.0)
_, external_attenuation = nr.GetExternalAttenuation("", 0.0)
_, limited_configuration_change = nr.GetLimitedConfigurationChange("", 0)
_, frequency_range = nr.GetFrequencyRange("", 0)
frequency_range = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXFrequencyRange), frequency_range)
_, link_direction = nr.GetLinkDirection("", 0)
link_direction = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXLinkDirection), link_direction)
_, num_component_carriers = nr.ComponentCarrier.GetNumberOfComponentCarriers("", 0)
_, component_carrier_bandwidth = nr.ComponentCarrier.GetBandwidth("", 0.0)
_, subcarrier_spacing = nr.ComponentCarrier.GetBandwidthPartSubcarrierSpacing("", 0.0)
_, pusch_modulation_type = nr.ComponentCarrier.GetPuschModulationType("", 0)
_, pdsch_modulation_type = nr.ComponentCarrier.GetPdschModulationType("", 1)
if link_direction == NRMX.RFmxNRMXLinkDirection.Uplink:
    modulation_type = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXPdschModulationType), pusch_modulation_type)
else:
    modulation_type = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXPdschModulationType), pdsch_modulation_type)
_, sync_mode = nr.ModAcc.Configuration.GetSynchronizationMode("", 5)
sync_mode = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXModAccSynchronizationMode), sync_mode)
_, modacc_averaging_enabled = nr.ModAcc.Configuration.GetAveragingEnabled("", 0)
_, modacc_averaging_count = nr.ModAcc.Configuration.GetAveragingCount("", 0)
_, chp_averaging_enabled = nr.Chp.Configuration.GetAveragingEnabled("", 0)
_, chp_averaging_count = nr.Chp.Configuration.GetAveragingCount("", 0)
_, chp_averaging_type = nr.Chp.Configuration.GetAveragingType("", 0)
chp_averaging_type = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXChpAveragingType), chp_averaging_type)
_, acp_averaging_enabled = nr.Acp.Configuration.GetAveragingEnabled("", 0)
_, acp_averaging_count = nr.Acp.Configuration.GetAveragingCount("", 0)
_, acp_averaging_type = nr.Acp.Configuration.GetAveragingType("", 0)
acp_averaging_type = System.Enum.GetName(clr.GetClrType(NRMX.RFmxNRMXAcpAveragingType), acp_averaging_type)
_, acp_noise_comp_enabled = nr.Acp.Configuration.GetNoiseCompensationEnabled("", 0)
f.write("\nMeasurement\n")
f.write(f"Selected Port,{selected_port}\n")
f.write(f"Autolevel Enabled,{rfsa_auto_level_enabled}\n")
f.write(f"Reference Level Optimization Enabled,{rfsa_optimize_reference_level}\n")
f.write(f"Reference Level Headroom (dB),{reference_level_headroom}\n")
f.write("External Attenuation (dB)," + '{:1.3f}\n'.format(external_attenuation))
f.write(f"Limited Configuration Change,{limited_configuration_change != 0}\n")
f.write(f"Frequency Range,{frequency_range}\n")
f.write(f"Link Direction,{link_direction}\n")
f.write(f"Number of Carriers,{num_component_carriers}\n")
f.write(f"Carrier Bandwidth (Hz)," + '{:.0f}\n'.format(component_carrier_bandwidth))
f.write(f"Subcarrier Spacing (Hz)," + '{:.0f}\n'.format(subcarrier_spacing))
f.write(f"Modulation Type,{modulation_type}\n")
f.write(f"ModAcc Sync Mode,{sync_mode}\n")
f.write(f"ModAcc Averaging Enabled,{modacc_averaging_enabled != 0}\n")
f.write(f"ModAcc Averaging Count,{modacc_averaging_count}\n")
f.write(f"CHP Averaging Enabled,{chp_averaging_enabled != 0}\n")
f.write(f"CHP Averaging Count,{chp_averaging_count}\n")
f.write(f"CHP Averaging Type,{chp_averaging_type}\n")
f.write(f"ACP Averaging Enabled,{acp_averaging_enabled != 0}\n")
f.write(f"ACP Averaging Count,{acp_averaging_count}\n")
f.write(f"ACP Averaging Type,{acp_averaging_type}\n")
f.write(f"ACP Noise Comp Enabled,{acp_noise_comp_enabled != 0}\n")

# sweep
f.write('\nResults\n')
f.write('Frequency (Hz),Reference Level (dBm),EVM (%),EVM (dB),Channel Power (dBm)')
rfsg.Initiate()
for frequency, rfsa_ext_atten, rfsg_ext_atten in zip(frequencies, rfsa_external_attenuations, rfsg_external_attenuations):
    nr.SetCenterFrequency("", frequency)
    nr.SetExternalAttenuation("", rfsa_ext_atten)
    rfsg.RF.Frequency = frequency
    rfsg.RF.ExternalGain = -rfsg_ext_atten
    rfsg.Utility.WaitUntilSettled(10000)
    rfsg.CheckGenerationStatus()

    for power in rfsg_power_levels:
        rfsg.RF.PowerLevel = power
        rfsg.Utility.WaitUntilSettled(10000)
        rfsg.CheckGenerationStatus()

        if rfsa_auto_level_enabled:
            nr.AutoLevel("", waveform_length_sec, 0.0)
        else:
            nr.SetReferenceLevel("", power + waveform_papr)

        nr.Initiate("", "")
        _, reference_level = nr.GetReferenceLevel("", 0.0)
        nr.WaitForMeasurementComplete("", -1)
        _, evm_percent = nr.ModAcc.Results.GetCompositeRmsEvmMean("", 0.0)

        if rfsa_optimize_reference_level:
            evm_percent_list = [evm_percent]
            reference_level_optimization_sweep = [-0.5 * offset for offset in range(1, 10)]
            for reference_level_optimization_offset in reference_level_optimization_sweep:
                nr.SetReferenceLevel("", reference_level - reference_level_optimization_offset)
                nr.Initiate("", "")
                if nr.WaitForMeasurementComplete("", -1) > 0:  # warnings are positive numbers
                    break
                _, evm_percent = nr.ModAcc.Results.GetCompositeRmsEvmMean("", 0.0)
            min_index = min(range(len(evm_percent_list)), key=evm_percent_list.__getitem__)
            evm_percent = evm_percent_list[min_index]
            reference_level = reference_level + reference_level_optimization_sweep[min_index]

        evm_dB = 20 * math.log10(evm_percent) - 40.0
        _, channel_power = nr.Chp.Results.GetTotalAggregatedPower("", 0.0)

        configuration_results = '{:.0f}'.format(frequency) + ',{:.3f}'.format(reference_level)
        scalar_results = ','.join(['{:.3f}'.format(result) for result in [evm_percent, evm_dB, channel_power]])
        result_line = ','.join([configuration_results, scalar_results])
        f.write(result_line + '\n')
        print(result_line)

f.close()
instr.Close()
rfsg.Close()
