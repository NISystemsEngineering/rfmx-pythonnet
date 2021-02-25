import clr, sys, os

dotNetFWDirectory = r"C:\Program Files (x86)\IVI Foundation\IVI\Microsoft.NET\Framework32"
dotNetClassLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.NIRfsg 20.0.0'
dotNetTClockLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.TClock 3.2.0'
assy_path = os.path.join(dotNetFWDirectory, dotNetClassLibrary)
assy_path2 = os.path.join(dotNetFWDirectory, dotNetTClockLibrary)

sys.path.append(assy_path)
sys.path.append(assy_path2)


clr.AddReference("NationalInstruments.ModularInstruments.TClock.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx40")
clr.AddReference("NationalInstruments.Common")
clr.AddReference("NationalInstruments.ModularInstruments.Common")

import NationalInstruments.ModularInstruments.NIRfsg as Rfsg
from NationalInstruments import *
import NationalInstruments.ModularInstruments.SystemServices.TimingServices as TClck

class SignalGenerators:
    def __init__(self, sg_resource_name0, sg_resource_name1):
        self.rfsg0 = Rfsg.NIRfsg(sg_resource_name0, True, False, "")
        self.rfsg1 = Rfsg.NIRfsg(sg_resource_name1, True, False, "")
        self.rfsg_sessions = [self.rfsg0, self.rfsg1]

    def configure_rfsg(self, frequency, external_attenuation, power_level, lo_offset, port):
        #Common Config
        for rfsg in self.rfsg_sessions:
            rfsg.RF.Frequency = frequency
            rfsg.RF.ExternalGain = -external_attenuation
            rfsg.RF.PowerLevel = power_level
            rfsg.SignalPath.SelectedPorts = port
            rfsg.RF.Upconverter.FrequencyOffsetMode = Rfsg.UpconverterFrequencyOffsetMode.UserDefined
            rfsg.RF.Upconverter.FrequencyOffset = lo_offset
            rfsg.Arb.GenerationMode = Rfsg.RfsgWaveformGenerationMode.ContinuousWave

        #Master Config
        self.rfsg0.FrequencyReference.Source = Rfsg.RfsgFrequencyReferenceSource.PxiClock
        self.rfsg0.FrequencyReference.ExportedOutputTerminal = Rfsg.RfsgFrequencyReferenceExportedOutputTerminal.ReferenceOut
        self.rfsg0.RF.LocalOscillator["lo2"].LOOutEnabled = True

#        self.rfsg0.Utility.Commit()

#        lo_power = self.rfsg0.RF.LocalOscillator["lo2"].LOOutPower
#        if lo_power < 6: lo_power = 6
#        if lo_power >10: lo_power = 10


        #Slave Config
        self.rfsg1.FrequencyReference.Source = Rfsg.RfsgFrequencyReferenceSource.PxiClock
        self.rfsg1.RF.LocalOscillator["lo2"].Source = Rfsg.RfsgLocalOscillatorSource.LOIn
        self.rfsg1.RF.LocalOscillator["lo2"].LOInPower = 6

#        self.rfsg1.Utility.Commit()

    def sync_initiate_sg(self):
        Tclk = TClck.TClock(self.rfsg_sessions)
        Tclk.ConfigureForHomogeneousTriggers()
        Tclk.Synchronize()
        Tclk.Initiate()

    def adjust_sg_phase(self, phase_offset):
        self.rfsg1.RF.PhaseOffset = phase_offset


    def abort(self):
        for rfsg in self.rfsg_sessions:
            rfsg.Abort()
            rfsg.RF.OutputEnabled = False
            rfsg.Close()
