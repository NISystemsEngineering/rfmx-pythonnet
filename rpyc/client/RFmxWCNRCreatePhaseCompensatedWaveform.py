"""
Example creating a 5GNR phase compensated waveform from an RFmx Waveform Creator .rfws file.
"""

import rpyc

# connect and import libraries
host_name = 'localhost'
host_port = 18861
conn = rpyc.connect(host_name, host_port)
NIRfsg = conn.root.NIRfsg
RFmxWCNR = conn.root.RFmxWCNR
NIRfsgPlayback = conn.root.NIRfsgPlayback

# local variables
resource_name = 'VST2_01'
carrier_frequency = 3.5e9
power_level = -10.0
frequency_reference_source = NIRfsg.RfsgFrequencyReferenceSource.FromString('OnboardClock')
external_attenuation = 0.0
rfws_file_path = r'c:\niremote\waveforms\NR_UL_FR1_100M_30k_QPSK.rfws'
phase_compensation_enabled = True
phase_compensation_frequency = 1e6
waveform_name = 'waveform'
script = f'script GenerateWfm\nrepeat forever\ngenerate {waveform_name}\nend repeat\nend script'

rfsg = NIRfsg.NIRfsg(resource_name, True, False)
rfsg_handle = rfsg.GetInstrumentHandle().DangerousGetHandle()

try:
    rfsg.Abort()
    rfsg.RF.Configure(carrier_frequency, power_level)
    rfsg.FrequencyReference.Configure(frequency_reference_source, 10e6)
    rfsg.RF.ExternalGain = -external_attenuation

    # Loads waveform configuration in.rfws file.
    RFmxWCNR.RFmxWCNR.LoadWaveformConfiguration(rfsg_handle, rfws_file_path, '')
    # The configurationName should be passed as empty which is the default name.
    # Only last loaded configuration will be in memory.

    RFmxWCNR.RFmxWCNR.SetPhaseCompensationEnabled(rfsg_handle, '', phase_compensation_enabled)
    # Sets PhaseCompensationFrequency on first subblock in first carrier set
    RFmxWCNR.RFmxWCNR.SetPhaseCompensationFrequency(rfsg_handle, '', phase_compensation_frequency)

    # This API internally uses playback library
    RFmxWCNR.RFmxWCNR.CreateAndDownloadWaveformComplexSingle(rfsg_handle, '', waveform_name)
    NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsg_handle, script)
    rfsg.Initiate()

    # Alternatively, you can use niRFmxWCNR_CreateWaveformComplexF32  API to create the waveform and WaveformComplex API to get the waveform
    # Alternatively, you can use CreateAndSaveWaveformToFileComplexF32 API to save waveform to a .TDMS file

    input("Generating phase compensated waveform. Press any key to stop..")

finally:
    # close sessions and connection to server
    rfsg.Abort()
    NIRfsgPlayback.NIRfsgPlayback.ClearAllWaveforms(rfsg_handle)
    RFmxWCNR.RFmxWCNR.DeleteWaveformConfiguration(rfsg_handle, '')
    rfsg.Close()
    conn.close()
