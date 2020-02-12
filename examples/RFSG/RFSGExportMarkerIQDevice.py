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
parser.add_argument('--marker', \
    help="where to output the marker")
parser.add_argument('--iqrate', default=1e6, type=float, \
    help="enter IQ rate")
parser.add_argument("--iqcsv", \
    help="enter IQ file absolute path")
parser.add_argument("--reference", default="OnboardClock", \
    help="select 10 MHZ reference source")

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
IQOutCarrierFrequency = 0.0 # FPGA DSP Frequencyshift
IQOutPortLevel = 0.5
IQOutIQRate = args.iqrate
IQOutMarkerOutput = args.marker
ReferenceSource = args.reference

# Initialize Instrument
instrSession = NIRfsg(ResourceName, True, False)

# Configure Instrument
print("Reference Clock Source: " + instrSession.FrequencyReference.Source.ToString())
instrSession.FrequencyReference. \
    Configure(RfsgFrequencyReferenceSource.FromString(args.reference), 10e6)
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
instrSession.Arb.GenerationMode = RfsgWaveformGenerationMode.Script
print("IQ Out Generation Mode: " + str(instrSession.Arb.GenerationMode))

print("IQ Out Marker Output Terminal: " + \
    str(instrSession.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal))
instrSession.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal = \
    RfsgMarkerEventExportedOutputTerminal.FromString(IQOutMarkerOutput)
print("IQ Out Marker Output Terminal: " + \
    str(instrSession.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal))

print("IQ Out IQ Rate: " + str(instrSession.Arb.IQRate))
instrSession.Arb.IQRate = IQOutIQRate
print("IQ Out IQ Rate: " + str(instrSession.Arb.IQRate))

print("IQ Out isWaveformRepeatCountFinite: " + str(instrSession.Arb.IsWaveformRepeatCountFinite))
instrSession.Arb.IsWaveformRepeatCountFinite = False
print("IQ Out isWaveformRepeatCountFinite: " + str(instrSession.Arb.IsWaveformRepeatCountFinite))

print("IQ Out WaveformRepeatCount: " + str(instrSession.Arb.WaveformRepeatCount))
instrSession.Arb.WaveformRepeatCount = 1
print("IQ Out WaveformRepeatCount: " + str(instrSession.Arb.WaveformRepeatCount))

# Create waveform to write either from file or default to one
iData, qData = [], []
if args.iqcsv is not None:
    # Import CSV File
    with open(args.iqcsv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            iData.append(row[0]);
        iData = np.asarray(iData, dtype=np.float32)
    qData = np.zeros(len(iData))
    qData = np.asarray(qData, dtype=np.float32)
else:
    # Write DC values to I
    iData = np.ones(1000)
    qData = np.zeros(1000)

instrSession.Arb.WriteWaveform("waveformWithMarkers", iData, qData)

# Write Marler Script
instrSession.Arb.Scripting.WriteScript( \
"script generateWaveformWithMarkers \n" \
"   repeat forever \n" \
"      generate waveformWithMarkers marker0(0)\n" \
"   end repeat \n" \
"end script")

# Start Generation
instrSession.Initiate()

# Wait for user to stop script
input("Press Enter to continue...")

# Abort Generation
instrSession.Abort()

# Close Instrument
instrSession.Close()
