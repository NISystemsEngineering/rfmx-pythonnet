import clr, sys, os

dotNetFWDirectory = r"C:\Program Files (x86)\IVI Foundation\IVI\Microsoft.NET\Framework32"
dotNetClassLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.NIRfsa 20.0.0'
assy_path = os.path.join(dotNetFWDirectory, dotNetClassLibrary)

sys.path.append(assy_path)

dotNetFWDirectory = r"C:\Program Files (x86)\IVI Foundation\IVI\Microsoft.NET\Framework32"
dotNetClassLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.NIRfsg 20.0.0'
assy_path = os.path.join(dotNetFWDirectory, dotNetClassLibrary)
print(".NET Library: " + dotNetClassLibrary)

sys.path.append(assy_path)

clr.AddReference("NationalInstruments.ModularInstruments.NIRfsa.Fx40")
clr.AddReference("NationalInstruments.Common")
from NationalInstruments import *
import Support.SignalAnalyzer as sa
import Support.SignalGenerator as sg


phase_offset = 0
phase_step = 5
centerFrequency = 9e9                                                 # (Hz)
power_Level = 10
phase_offsets = range(0 + phase_offset, 270 + phase_offset, phase_step)


# VSG Settings
sgResourceName0 = 'BCN_02'
sgResourceName1 = 'BCN_01'
sgExternalAttenuation = 0
sgSelectedPorts = 'if0'

# VSA Settings
ch0ResourceName = 'BCN_02'
ch1ResourceName = 'BCN_01'
saSelectedPorts = 'if1'
ch0ExternalAttenuation = 0
ch1ExternalAttenuation = 0

lo_offset = 100e6
iq_rate = 10e6
acq_time = 10e-4


rfsg = sg.SignalGenerators(sgResourceName0, sgResourceName1)
rfsg.configure_rfsg(centerFrequency, sgExternalAttenuation, power_Level, lo_offset, sgSelectedPorts)

rfsg.sync_initiate_sg()

rfsa = sa.SignalAnalyzers(ch0ResourceName, ch1ResourceName)
rfsa.configure_rfsa(lo_offset, saSelectedPorts, centerFrequency, iq_rate, power_Level, acq_time)

rfsa.sync_sa()

mag_delta = []
phase_delta = []

for phase in phase_offsets:
    rfsg.adjust_sg_phase(phase)
    rfsa.init_sa()
    waveforms = rfsa.fetch_sa()
    data_pro = sa.DataPostProcessor(waveforms)
    temp_mag, temp_phase = data_pro.calculate_deltas()
    mag_delta.append(temp_mag)
    phase_delta.append(temp_phase)

print("Expected Phase Steps = " + str(phase_step))
for phase in phase_delta:

    string = "Phase delta between two channels is: "
    if phase < 0:
        print(string + str((phase+360)) + " degrees") #unwrapping
    else:
        print(string + str(phase) + " degrees")

rfsg.abort()
rfsa.abort()