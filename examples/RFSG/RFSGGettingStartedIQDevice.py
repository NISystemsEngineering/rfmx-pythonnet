import clr
import sys
import time
import os
import argparse
import csv

import numpy as np

# Argparse section
parser = argparse.ArgumentParser()
parser.add_argument('--resource', \
    help="enter instrument resource name")
parser.add_argument('--trigger', default="none", \
    help="enable trigger on requested terminal")
parser.add_argument('--iqrate', default=1e6, type=float, \
    help="enter IQ rate")

args = parser.parse_args()

# Location of assemblies
dotNetFWDirectory = r"C:\Program Files (x86)\IVI Foundation\IVI\Microsoft.NET\Framework32"
dotNetClassLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.NIRfsg 17.1.0'
assy_path = os.path.join(dotNetFWDirectory, dotNetClassLibrary)
print(".NET Library: " + dotNetClassLibrary)

sys.path.append(assy_path)

clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx40")
clr.AddReference("NationalInstruments.Common")

# Import .NET drivers
from NationalInstruments.ModularInstruments.NIRfsg import *
from NationalInstruments import PrecisionTimeSpan
from NationalInstruments import ComplexDouble

# Instrument Settings
ResourceName = args.resource # Instrument alias in MAX
IQOutCarrierFrequency = 1000.0 # FPGA DSP Frequencyshift
IQOutPortLevel = 0.5
IQOutIQRate = args.iqrate
IQOutTriggerDestination = args.trigger

# Initialize Instrument
instrSession = NIRfsg(ResourceName, True, False)

# Configure Instrument
print("Reference Clock Source: " + instrSession.FrequencyReference.Source.ToString())
instrSession.FrequencyReference.Configure(RfsgFrequencyReferenceSource.PxiClock, 10e6)
print("Reference Clock Source: " + instrSession.FrequencyReference.Source.ToString())

print("IQ Out Output Port: " + str(instrSession.Arb.OutputPort))
instrSession.Arb.OutputPort = RfsgOutputPort.IQOut
print("IQ Out Output Port: " + str(instrSession.Arb.OutputPort))

print("IQ Out Carrier Frequency: " + str(instrSession.IQOutPort.CarrierFrequency))
instrSession.IQOutPort.CarrierFrequency = IQOutCarrierFrequency
print("IQ Out Carrier Frequency: " + str(instrSession.IQOutPort.CarrierFrequency))

print("IQ Out Port Level: " + str(instrSession.IQOutPort[""].Level))
instrSession.IQOutPort[""].Level = IQOutPortLevel
print("IQ Out Port Level: " + str(instrSession.IQOutPort[""].Level))

print("IQ Out Generation Mode: " + str(instrSession.Arb.GenerationMode))
instrSession.Arb.GenerationMode = RfsgWaveformGenerationMode.ArbitraryWaveform
print("IQ Out Generation Mode: " + str(instrSession.Arb.GenerationMode))

print("IQ Out Power Level Type: " + str(instrSession.RF.PowerLevelType))
instrSession.RF.PowerLevelType = RfsgRFPowerLevelType.PeakPower
print("IQ Out Power Level Type: " + str(instrSession.RF.PowerLevelType))

print("IQ Out IQ Rate: " + str(instrSession.Arb.IQRate))
instrSession.Arb.IQRate = IQOutIQRate
print("IQ Out IQ Rate: " + str(instrSession.Arb.IQRate))

print("IQ Out isWaveformRepeatCountFinite: " + str(instrSession.Arb.IsWaveformRepeatCountFinite))
instrSession.Arb.IsWaveformRepeatCountFinite = False
print("IQ Out isWaveformRepeatCountFinite: " + str(instrSession.Arb.IsWaveformRepeatCountFinite))

print("IQ Out WaveformRepeatCount: " + str(instrSession.Arb.WaveformRepeatCount))
instrSession.Arb.WaveformRepeatCount = 1
print("IQ Out WaveformRepeatCount: " + str(instrSession.Arb.WaveformRepeatCount))

# Write DC values to I
iData = np.ones(1000)
qData = np.zeros(1000)
instrSession.Arb.WriteWaveform("wfm0", iData, qData)

if args.trigger is not "none":
    print("IQ Out Export Start Trigger: " +
    str(instrSession.Triggers.StartTrigger.ExportedOutputTerminal))
    instrSession.Triggers.StartTrigger.ExportedOutputTerminal = \
        RfsgStartTriggerExportedOutputTerminal.FromString(IQOutTriggerDestination)
    print("IQ Out Export Start Trigger: " +
    str(instrSession.Triggers.StartTrigger.ExportedOutputTerminal))

# Start Generation
instrSession.Initiate()

# Wait for user to stop script
input("Press Enter to continue...")

# Abort Generation
instrSession.Abort()

# Close Instrument
instrSession.Close()
