import clr, sys, os

dotNetFWDirectory = r"C:\Program Files (x86)\IVI Foundation\IVI\Microsoft.NET\Framework32"
dotNetClassLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.NIRfsa 20.0.0'
dotNetTClockLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.TClock 3.2.0'
assy_path = os.path.join(dotNetFWDirectory, dotNetClassLibrary)
assy_path2 = os.path.join(dotNetFWDirectory, dotNetTClockLibrary)

sys.path.append(assy_path)
sys.path.append(assy_path2)

clr.AddReference("NationalInstruments.ModularInstruments.TClock.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsa.Fx40")
clr.AddReference("NationalInstruments.Common")
clr.AddReference("NationalInstruments.ModularInstruments.Common")

import NationalInstruments.ModularInstruments.SystemServices.TimingServices as TClck
import NationalInstruments.ModularInstruments.NIRfsa as NIRfsa
from NationalInstruments import PrecisionTimeSpan
from NationalInstruments import ComplexDouble
import math
from statistics import mean


class SignalAnalyzers:
    def __init__(self, rfsa_name0, rfsa_name1):
        self.instrSession0 = NIRfsa.NIRfsa(rfsa_name0, True, False)
        self.instrSession1 = NIRfsa.NIRfsa(rfsa_name1, True, False)
        self.instrSessions = [self.instrSession0, self.instrSession1]

    def configure_rfsa(self, lo_offset, selected_port, center_frequency, iq_rate, reference_level, acq_time):
        #Master configuration
        self.instrSession0.Configuration.SignalPath.LocalOscillator["lo2"].LOExportEnabled = True
        #Slave configuration
        self.instrSession1.Configuration.SignalPath.LocalOscillator["lo2"].LOSource = NIRfsa.RfsaLOSource.LOIn

        for instrSession in self.instrSessions:
            instrSession.Configuration.ReferenceClock.Source = NIRfsa.RfsaReferenceClockSource.PxiClock
            instrSession.Configuration.SignalPath.SelectedPorts = selected_port
            instrSession.Configuration.AcquisitionType = NIRfsa.RfsaAcquisitionType.IQ
            instrSession.Configuration.IQ.CarrierFrequency = center_frequency
            instrSession.Configuration.IQ.IQRate = iq_rate
            instrSession.Configuration.IQ.NumberOfSamples = iq_rate * acq_time
            instrSession.Configuration.Vertical.ReferenceLevel = reference_level
            instrSession.Acquisition.Advanced.DownconverterFrequencyOffsetMode = NIRfsa.RfsaDownconverterFrequencyOffsetMode.UserDefined
            instrSession.Acquisition.Advanced.DownconverterFrequencyOffset = lo_offset
            instrSession.Utility.Commit()

    def sync_sa(self):
        sessions = [self.instrSession0, self.instrSession1]
        Tclk = TClck.TClock(sessions)
        Tclk.ConfigureForHomogeneousTriggers()
        Tclk.Synchronize()
        self.TClk = Tclk

    def init_sa(self):
        self.TClk.Initiate()

    def fetch_sa(self):
        iq_waveforms = []
        timeout = PrecisionTimeSpan(10.0)
        dummy = ComplexDouble.ComposeArray([], [])
        for instrSession in self.instrSessions:
            _, iq_waveform = instrSession.Acquisition.IQ.FetchIQSingleRecordComplex(0, 100, timeout, dummy)
            iq_waveforms.append(iq_waveform)
        return iq_waveforms

    def abort(self):
        for instrSession in self.instrSessions:
            instrSession.Close()

class DataPostProcessor:
    def __init__(self, dataset):
        self.waveforms = dataset

    def calculate_deltas(self):
        _, r0, phi0 = ComplexDouble.DecomposeArrayPolar(self.waveforms[0], None, None)
        _, r1, phi1 = ComplexDouble.DecomposeArrayPolar(self.waveforms[1], None, None)
        r_delta =[]
        phi_delta = []
        for x in range(len(phi0)):
            phi_delta.append((phi1[x] - phi0[x]) * 180 / math.pi)
            r_delta.append(r1[x] - r0[x])

        average_r_delta = mean(r_delta)
        average_phi_delta = mean(phi_delta)
        return average_r_delta, average_phi_delta