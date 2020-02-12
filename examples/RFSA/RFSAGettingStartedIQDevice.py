import clr
import sys
import time
import os
import argparse
import csv

import numpy as np
import matplotlib.pyplot as plt

# Argparse section
parser = argparse.ArgumentParser()
parser.add_argument('--resource', \
    help="enter instrument resource name")
parser.add_argument('--trigger', \
    help="enable trigger on requested terminal") 
parser.add_argument('--iqrate', default=1e6, type=float, \
    help="enter IQ rate")
parser.add_argument('--samples', default=1000, type=int, \
    help="enter number of samples to fetch")
parser.add_argument("--reference", default="OnboardClock", \
    help="select 10 MHZ reference source")

args = parser.parse_args()

# Location of assemblies
dotNetFWDirectory = r"C:\Program Files (x86)\IVI Foundation\IVI\Microsoft.NET\Framework32"
dotNetClassLibrary = r'v4.0.30319\NationalInstruments.ModularInstruments.NIRfsa 17.1.0'
assy_path = os.path.join(dotNetFWDirectory, dotNetClassLibrary)
print(".NET Library: " + dotNetClassLibrary)

sys.path.append(assy_path)

clr.AddReference("NationalInstruments.ModularInstruments.NIRfsa.Fx40")
clr.AddReference("NationalInstruments.Common")

# Import .NET drivers
from NationalInstruments.ModularInstruments.NIRfsa import *
from NationalInstruments import PrecisionTimeSpan
from NationalInstruments import ComplexDouble

# Instrument Settings
ResourceName = args.resource # Instrument alias in MAX
IQinVerticalRange = 0.5 # Vpp
IQinCarrierFrequency = 0.0 # FPGA DSP Frequencyshift
IQinRate = args.iqrate
SamplesPerRecord = args.samples # Samples per second
IQinTriggerSource = args.trigger
ReferenceSource = args.reference

# Initialize Instrument
instrSession = NIRfsa(ResourceName, True, False)

# Configure Instrument
print("Reference Clock Source: " + instrSession.Configuration.ReferenceClock.Source.ToString())
instrSession.Configuration.ReferenceClock.Configure(RfsaReferenceClockSource.PxiClock, 10e6)
print("Reference Clock Source: " + instrSession.Configuration.ReferenceClock.Source.ToString())

print("Acquisition Type: " + str(instrSession.Configuration.AcquisitionType))
instrSession.Configuration.AcquisitionType = RfsaAcquisitionType.IQ
print("Acquisition Type: " + str(instrSession.Configuration.AcquisitionType))

print("IQ In Input Port: " + str(instrSession.Configuration.SignalPath.Advanced.InputPort))
instrSession.Configuration.SignalPath.Advanced.InputPort = RfsaInputPort.IQIn
print("IQ In Input Port: " + str(instrSession.Configuration.SignalPath.Advanced.InputPort))

print("IQ In Carrier Frequency: " + str(instrSession.Configuration.IQInPortChannels.CarrierFrequency))
instrSession.Configuration.IQInPortChannels.CarrierFrequency = IQinCarrierFrequency
print("IQ In Carrier Frequency: " + str(instrSession.Configuration.IQInPortChannels.CarrierFrequency))

print("IQ In Rate: " + str(instrSession.Configuration.IQ.IQRate))
instrSession.Configuration.IQ.IQRate = IQinRate
print("IQ In Rate: " + str(instrSession.Configuration.IQ.IQRate))

print("Number of record is finite: " + str(instrSession.Configuration.IQ.NumberOfRecordsIsFinite))
instrSession.Configuration.IQ.NumberOfRecordsIsFinite = True
print("Number of record is finite: " + str(instrSession.Configuration.IQ.NumberOfRecordsIsFinite))

print("Number of Samples per Record: " + str(instrSession.Configuration.IQ.NumberOfSamples))
instrSession.Configuration.IQ.NumberOfSamples = SamplesPerRecord
print("Number of Samples per Record: " + str(instrSession.Configuration.IQ.NumberOfSamples))

if args.trigger:
    print("IQ In Start Trigger Source: " +
    str(instrSession.Configuration.Triggers.StartTrigger.DigitalEdge.Source))
    instrSession.Configuration.Triggers.StartTrigger.DigitalEdge.Source = \
        RfsaDigitalEdgeStartTriggerSource.FromString(IQinTriggerSource)
    print("IQ In Start Trigger Source: " +
    str(instrSession.Configuration.Triggers.StartTrigger.DigitalEdge.Source))
    print("IQ In Start Trigger Type: " +
    str(instrSession.Configuration.Triggers.StartTrigger.Type))
    instrSession.Configuration.Triggers.StartTrigger.Type = \
        RfsaStartTriggerType.DigitalEdge
    print("IQ In Start Trigger Type: " +
    str(instrSession.Configuration.Triggers.StartTrigger.Type))

    print("Waiting for tigger, you have 10 seconds before a time out, hurry .........")

# Begin Acquisition and read data
timeout = PrecisionTimeSpan(10.0)
nicomplexdoublearray = instrSession.Acquisition.IQ.ReadIQSingleRecordComplex(timeout)

# Helper Prints for Data structure peek
print("")
print("NI ComplexDoubleArray Type: " + str(type(nicomplexdoublearray)))
print("NI ComplexDoubleArray[0]: "+ str(nicomplexdoublearray[0]))
print("NI ComplexDouble.[0]Real Type: "+ str(type(nicomplexdoublearray[0].Real)))
print("NI ComplexDouble[0].Real: " +str(nicomplexdoublearray[0].Real))

# Using NI DecomposeArray to split real and imaginary
# This is not necessary and you can use complexdoublearray[i].Real directly
# but other NI functions may returns more complex structures and using the
# NI common methods should prove to be easier
iTemp = []
qTemp = []
_, iTemp, qTemp = ComplexDouble.DecomposeArray(nicomplexdoublearray, iTemp, qTemp)

print("NI ComplexDouble.DecomposeArray Type: " + str(type(iTemp)))
print("NI Syste.Double[0]: " + str(iTemp[0]))

# Convert System.Double to floats
iData = []
qData = []
for i in iTemp:
    iData.append(float(i))

for q in qTemp:
    qData.append(float(q))

# Plot Data
fig = plt.figure()

ax0 = fig.add_subplot(2,1,1)
ax0.plot(iData)

ax1 = fig.add_subplot(2,1,2)
ax1.plot(qData)

plt.show()

# Close Instrument
instrSession.Close()
