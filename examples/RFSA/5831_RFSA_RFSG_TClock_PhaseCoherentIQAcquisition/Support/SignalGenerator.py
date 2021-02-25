import clr, sys, os

sys.path.insert(1,r"C:\Users\LocalAdmin\Documents\stchan\PythonNET_RFmxXC\bin")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx45")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.TClock.Fx45")
clr.AddReference("NationalInstruments")
clr.AddReference("NationalInstruments.Common")

import System
import NationalInstruments.ModularInstruments.NIRfsg as Rfsg
import NationalInstruments.ModularInstruments.NIRfsgPlayback as RfsgPlayback
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
