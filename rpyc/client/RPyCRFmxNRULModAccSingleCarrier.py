# DEMO EXAMPLE: Client side execution of RFmx NR on a remote server
from pathlib import Path, PureWindowsPath
import rpyc

# # # # # User Parameters # # # # # #
host_name = 'localhost'                # Name or IP address of the RPyC server
host_port = 18861                    # Port number of the RPyC server
generator_resource_name = 'BCN_01'      # Resource name of the Generator on the Host
analyzer_resource_name = 'BCN_01'       # Resource name of the Analyzer on the Host
waveform_folder = Path('../waveforms') # Example: waveformFolder = "c:/niremote/waveforms" , '.' denotes same directory as this .py file, if running on the server
waveform_file_name = 'nr100.tdms'     # Name of the .tdms waveform to play
                                    # Note that in this example all of the waveforms are on the server and need to be pathed as such

# # # # # RPyC Configuration # # # # #
# Open connection to the service
print("Opening connection to RFmxService on " + host_name)
conn = rpyc.connect(host_name, host_port)
print("Connection opened successfully")

# Instantiate exported classes from the service
print("Importing classes from service..", end='')
System = conn.root.System
NationalInstruments = conn.root.NationalInstruments
NIRfsg = conn.root.NIRfsg
NIRfsgPlayback = conn.root.NIRfsgPlayback
InstrMX = conn.root.InstrMX
NRMX = conn.root.NRMX
print("done")

print("Setting measurement parameters..", end='')
# # # # # Global settings # # # # #
center_frequency = 28e9

# # # # # Generation settings # # # # #
rfsg_selected_ports = "rf1/port1"
rfsg_power_level = -10
rfsg_external_attenuation = 0
rfsg_reference_clock_source = NIRfsg.RfsgFrequencyReferenceSource.OnboardClock
rfsg_waveform_name = "waveform"
rfsg_script = 'script GenerateWaveform repeat forever generate waveform marker0(0) end repeat end script'
rfsg_automatic_shared_lo = NIRfsgPlayback.RfsgPlaybackAutomaticSGSASharedLO.Enabled

# # # # # Analysis settings # # # # #
instr_selected_ports = "rf0/port1"
instr_frequency_reference_source = InstrMX.RFmxInstrMXConstants.OnboardClock
instr_frequency_reference_frequency = 10e6
instr_automatic_shared_lo = InstrMX.RFmxInstrMXAutomaticSGSASharedLO.Enabled

nr_reference_level = 0.0
nr_external_attenuation = 0.0

nr_enable_trigger = True
nr_digital_edge_source = NRMX.RFmxNRMXConstants.PxiTriggerLine0
nr_digital_edge = NRMX.RFmxNRMXDigitalEdgeTriggerEdge.Rising
nr_trigger_delay = 0.0

nr_frequency_range = NRMX.RFmxNRMXFrequencyRange.Range1
nr_band = 78
nr_cell_id = 0
nr_carrier_bandwidth = 100e6
nr_subcarrier_spacing = 30e3
                                
nr_auto_resource_block_detection_enabled = True

nr_pusch_transform_precoding_enabled = False
nr_pusch_modulation_type = NRMX.RFmxNRMXPuschModulationType.Qpsk
nr_number_of_resource_block_clusters = 1
nr_pusch_resource_block_offset = [0]
nr_pusch_number_of_resource_blocks = [-1]
nr_pusch_slot_allocation = "0-Last"
nr_pusch_symbol_allocation = "0-Last"

nr_pusch_dmrs_power_mode = NRMX.RFmxNRMXPuschDmrsPowerMode.CdmGroups
nr_pusch_dmrs_power = 0.0
nr_pusch_dmrs_configuration_type = NRMX.RFmxNRMXPuschDmrsConfigurationType.Type1
nr_pusch_mapping_type = NRMX.RFmxNRMXPuschMappingType.TypeA
nr_pusch_dmrs_type_a_position = 2
nr_pusch_dmrs_duration = NRMX.RFmxNRMXPuschDmrsDuration.SingleSymbol
nr_pusch_dmrs_additional_positions = 0

nr_synchronization_mode = NRMX.RFmxNRMXModAccSynchronizationMode.Slot

nr_measurement_length_unit = NRMX.RFmxNRMXModAccMeasurementLengthUnit.Slot
nr_measurement_offset = 0
nr_measurement_length = 1

nr_averaging_enabled = False
nr_averaging_count = 10

nr_measurement_timeout = 10.0
print("done")

# # # # # Execute Measurements # # # # #

# Initialize Generator
print("Initializing generator..", end='')
rfsg_session = NIRfsg.NIRfsg(generator_resource_name, True, False, "")
rfsg_session.SignalPath.SelectedPorts = rfsg_selected_ports
rfsg_handle = rfsg_session.GetInstrumentHandle().DangerousGetHandle()
print("done")

# Initialize Analyzer
print("Initializing analyzer..", end='')
instr_session = InstrMX.RFmxInstrMX.GetSession(analyzer_resource_name, "")
instr_session.ResetEntireSession()
print("done")

# Generation configuration
print("Configuring generator..", end='')
rfsg_session.RF.Configure(center_frequency, rfsg_power_level)
rfsg_session.FrequencyReference.Configure(rfsg_reference_clock_source, 10e6)
rfsg_session.RF.ExternalGain = -rfsg_external_attenuation
# The server will be running on Windows and needs a PureWindowsPath to locate the waveform
NIRfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsg_handle, str(PureWindowsPath(waveform_folder / waveform_file_name)), rfsg_waveform_name)
NIRfsgPlayback.NIRfsgPlayback.StoreAutomaticSGSASharedLO(rfsg_handle, "", rfsg_automatic_shared_lo)
NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsg_handle, rfsg_script)
rfsg_session.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal = NIRfsg.RfsgMarkerEventExportedOutputTerminal.PxiTriggerLine0
print("done")

# Measurement configuration
print("Configuring analyzer..", end='')

# Get NR Handle
nr = InstrMX.RFmxNRMXExtension.GetNRSignalConfiguration(instr_session)
instr_session.ConfigureFrequencyReference("", instr_frequency_reference_source, instr_frequency_reference_frequency)
instr_session.ConfigureAutomaticSGSASharedLO("", instr_automatic_shared_lo)

# Configure the NR Measurement
nr.SetSelectedPorts("", instr_selected_ports)
nr.ConfigureRF("", center_frequency, nr_reference_level, nr_external_attenuation)
nr.ConfigureDigitalEdgeTrigger("", nr_digital_edge_source, nr_digital_edge, nr_trigger_delay, nr_enable_trigger)

nr.SetFrequencyRange("", nr_frequency_range)
nr.ComponentCarrier.SetBandwidth("", nr_carrier_bandwidth)
nr.ComponentCarrier.SetCellID("", nr_cell_id)
nr.SetBand("", nr_band)
nr.ComponentCarrier.SetBandwidthPartSubcarrierSpacing("", nr_subcarrier_spacing)
nr.SetAutoResourceBlockDetectionEnabled("", nr_auto_resource_block_detection_enabled)

nr.ComponentCarrier.SetPuschTransformPrecodingEnabled("", nr_pusch_transform_precoding_enabled)
nr.ComponentCarrier.SetPuschSlotAllocation("", nr_pusch_slot_allocation)
nr.ComponentCarrier.SetPuschSymbolAllocation("", nr_pusch_symbol_allocation)
nr.ComponentCarrier.SetPuschModulationType("", nr_pusch_modulation_type)

nr.ComponentCarrier.SetPuschNumberOfResourceBlockClusters("", nr_number_of_resource_block_clusters)

nr_subblock_string = NRMX.RFmxNRMX.BuildSubblockString("", 0)
nr_carrier_string = NRMX.RFmxNRMX.BuildCarrierString(nr_subblock_string, 0)
nr_bandwidth_part_string = NRMX.RFmxNRMX.BuildBandwidthPartString(nr_carrier_string, 0)
nr_user_string = NRMX.RFmxNRMX.BuildUserString(nr_bandwidth_part_string, 0)
nr_pusch_string = NRMX.RFmxNRMX.BuildPuschString(nr_user_string, 0)
for i in range(nr_number_of_resource_block_clusters):
    nr_pusch_cluster_string = NRMX.RFmxNRMX.BuildPuschClusterString(nr_pusch_string, i)
    nr.ComponentCarrier.SetPuschResourceBlockOffset(nr_pusch_cluster_string, nr_pusch_resource_block_offset[i])
    nr.ComponentCarrier.SetPuschNumberOfResourceBlocks(nr_pusch_cluster_string, nr_pusch_number_of_resource_blocks[i])

nr.ComponentCarrier.SetPuschDmrsPowerMode("", nr_pusch_dmrs_power_mode)
nr.ComponentCarrier.SetPuschDmrsPower("", nr_pusch_dmrs_power)
nr.ComponentCarrier.SetPuschDmrsConfigurationType("", nr_pusch_dmrs_configuration_type)
nr.ComponentCarrier.SetPuschMappingType("", nr_pusch_mapping_type)
nr.ComponentCarrier.SetPuschDmrsTypeAPosition("", nr_pusch_dmrs_type_a_position)
nr.ComponentCarrier.SetPuschDmrsDuration("", nr_pusch_dmrs_duration)
nr.ComponentCarrier.SetPuschDmrsAdditionalPositions("", nr_pusch_dmrs_additional_positions)
nr.SelectMeasurements("", NRMX.RFmxNRMXMeasurementTypes.ModAcc, True)

nr.ModAcc.Configuration.SetSynchronizationMode("", nr_synchronization_mode)
nr.ModAcc.Configuration.SetAveragingEnabled("", nr_averaging_enabled)
nr.ModAcc.Configuration.SetAveragingCount("", nr_averaging_count)

nr.ModAcc.Configuration.SetMeasurementLengthUnit("", nr_measurement_length_unit)
nr.ModAcc.Configuration.SetMeasurementOffset("", nr_measurement_offset)
nr.ModAcc.Configuration.SetMeasurementLength("", nr_measurement_length)

print("done")

# Initiate and fetch results
print("Initiating and fetching results..", end='')
rfsg_session.Initiate()
nr.Initiate("", "")
instr_session.WaitForAcquisitionComplete(10)
rfsg_session.Abort()

# _ Ignores the first returned value of the function. In this case it is an error code. Errors will still throw exceptions.
_, composite_rms_evm_mean = nr.ModAcc.Results.GetCompositeRmsEvmMean("", 0.0)
_, composite_peak_evm_maximum = nr.ModAcc.Results.GetCompositePeakEvmMaximum("", 0.0)
_, composite_peak_evm_slot_index = nr.ModAcc.Results.GetCompositePeakEvmSlotIndex("", 0)
_, composite_peak_evm_symbol_index = nr.ModAcc.Results.GetCompositePeakEvmSymbolIndex("", 0)
_, composite_peak_evm_subcarrier_index = nr.ModAcc.Results.GetCompositePeakEvmSubcarrierIndex("", 0)

_, component_carrier_frequency_error_mean = nr.ModAcc.Results.GetComponentCarrierFrequencyErrorMean("", 0.0)
_, component_carrier_iq_origin_offset_mean = nr.ModAcc.Results.GetComponentCarrierIQOriginOffsetMean("", 0.0)
_, component_carrier_iq_gain_imbalance_mean = nr.ModAcc.Results.GetComponentCarrierIQGainImbalanceMean("", 0.0)
_, component_carrier_quadrature_error_mean = nr.ModAcc.Results.GetComponentCarrierQuadratureErrorMean("", 0.0)
_, in_band_emission_margin = nr.ModAcc.Results.GetInBandEmissionMargin("", 0.0)

# These could be visualized using various visualization tools.
# nr.ModAcc.Results.FetchPuschDataConstellationTrace("", timeout, ref puschDataConstellation)
# nr.ModAcc.Results.FetchPuschDmrsConstellationTrace("", timeout, ref puschDmrsConstellation)
# nr.ModAcc.Results.FetchRmsEvmPerSubcarrierMeanTrace("", timeout, ref rmsEvmPerSubcarrierMean)
# nr.ModAcc.Results.FetchRmsEvmPerSymbolMeanTrace("", timeout, ref rmsEvmPerSymbolMean)
# nr.ModAcc.Results.FetchSpectralFlatnessTrace("", timeout, ref spectralFlatness,
# ref spectralFlatnessLowerMask, ref spectralFlatnessUpperMask)

print("done")

# print scalar results

print("------------------Measurement------------------")
print("Composite RMS EVM Mean (%)                     : {0}".format(composite_rms_evm_mean))
print("Composite Peak EVM Maximum (%)                 : {0}".format(composite_peak_evm_maximum))
print("Composite Peak EVM Slot Index                  : {0}".format(composite_peak_evm_slot_index))
print("Composite Peak EVM Symbol Index                : {0}".format(composite_peak_evm_symbol_index))
print("Composite Peak EVM Subcarrier Index            : {0}".format(composite_peak_evm_subcarrier_index))
print("Component Carrier Frequency Error Mean (Hz)    : {0}".format(component_carrier_frequency_error_mean))
print("Component Carrier IQ Origin Offset Mean (dBc)  : {0}".format(component_carrier_iq_origin_offset_mean))
print("Component Carrier IQ Gain Imbalance Mean (dB)  : {0}".format(component_carrier_iq_gain_imbalance_mean))
print("Component Carrier Quadrature Error Mean (deg)  : {0}".format(component_carrier_quadrature_error_mean))

#Close instrument session
instr_session.Close()
rfsg_session.Close()
