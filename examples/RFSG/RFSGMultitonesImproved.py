# -*- coding: utf-8 -*-
# -------------------------------------------------
# Generate any number and power of tones.
# -------------------------------------------------
# At least one tone needs to be at 0 dB. Use Power level to sett he power of all the tones relative to their selected power.
# The minimum separation is mandated by a variable below. A smaller number needs more samples to meet the needs.
# The maximum separation is mandated by the instrument used.
# Steps to getting this example to run on a system aside from typical Python environment and driver setup:
# 1) Change resource name



# Importing python libraries
from pathlib import Path, PureWindowsPath
import os
import sys
import clr # use pip install pythonnet
import time
import numpy as np
import math

### Defining path references for NI assemblies ###
print("Defining path references and importing NI assemblies..", end='')
programFilesPath64 = os.environ["ProgramFiles"]
programFilesPath32 = os.environ["ProgramFiles(x86)"]
sys.path.append(programFilesPath32 + r'\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current')
sys.path.append(programFilesPath32 + r'\National Instruments\Measurement Studio\DotNET\v4.0\AnyCPU\NationalInstruments.Common 19.1.40')
sys.path.append(programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64\v4.0.30319\NationalInstruments.ModularInstruments.Common 21.5.0')
sys.path.append(programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64\v4.0.30319\NationalInstruments.ModularInstruments.ModularInstrumentsSystem 1.4.40')
sys.path.append(programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64\v4.0.30319\NationalInstruments.ModularInstruments.NIRfsa 21.5.0')
sys.path.append(programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64\v4.0.30319\NationalInstruments.ModularInstruments.NIRfsg 21.5.0')
sys.path.append(programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64\v4.0.30319\NationalInstruments.ModularInstruments.TClock 21.5.0')
clr.AddReference('NationalInstruments.Common')
clr.AddReference('NationalInstruments.ModularInstruments.Common')
clr.AddReference('NationalInstruments.RFmx.InstrMX.Fx40')
clr.AddReference('NationalInstruments.RFmx.NRMX.Fx40')
clr.AddReference('NationalInstruments.RFmx.SpecAnMX.Fx40')
clr.AddReference('NationalInstruments.ModularInstruments.NIRfsa.Fx40')
clr.AddReference('NationalInstruments.ModularInstruments.NIRfsg.Fx40')
clr.AddReference('NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40')

### Importing NI assemblies ###
import System
import NationalInstruments
import NationalInstruments.ModularInstruments as ModularInstruments
import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.RFmx.NRMX as NRMX
import NationalInstruments.RFmx.SpecAnMX as SpecAnMX
import NationalInstruments.ModularInstruments.NIRfsa as NIRfsa
import NationalInstruments.ModularInstruments.NIRfsg as NIRfsg
import NationalInstruments.ModularInstruments.NIRfsgPlayback as NIRfsgPlayback
print("done")


#Tones to Generate
class Tone:
    def __init__(self,offsetHz, gaindB):
        self.offsetHz = offsetHz
        self.gaindB = gaindB
    def __repr__(self):
        return 'Offset: {0} Hz and Gain: {1} dB'.format(self.offsetHz,self.gaindB)

def gcd(my_list):
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result

#Documentation
#Tones power is relative to the generated power.

#Tested Cases
#Tones = [Tone(0, 0)]
Tones = [Tone(-1E6, 0), Tone(1E6, 0)]
#Tones = [Tone(-1E6, 0), Tone(1E6, -5), Tone(2.5E6, -10), Tone(3.9E6, -20)]
#Tones = [Tone(100E3, 0), Tone(-835E3, -6)]
#Tones = [Tone(10E6, -3), Tone(-100.1E6, -6)]
#Tones = [Tone(1E6, 2.45), Tone(-50E6, -6)]
#Tones = [Tone(499E6, 0), Tone(-499E6, -6)]
#Tones = [Tone(1E6, 0), Tone(-50E6, -6)] + [Tone(499E6, 0), Tone(-499E6, -6)]
#Tones = [Tone(0, 0), Tone(-835E3, -6)]
#Tones = [Tone(2501200001-3e9, 0), Tone(3405200000-3e9, 0), Tone(3305300000-3e9, 0)]

#Error Test Cases
#Tones = [Tone(0, -6)]
#Tones = [Tone(100E6, -10), Tone(-100E6, -10)]
#Tones = [Tone(1E9, 0), Tone(-100.1E6, -6)]
#Tones = [Tone(100E6, -20)]
#Tones = [Tone(1, 0), Tone(10E6, -6)]

minSamplingRateHz = 4e6
minFrequencyStepHz = 5000
minWaveformSize = 100000
print(Tones)


# Define the instrument and RF parameters
print("Setting measurement parameters.. ", end='')
centerFrequency = 3e9
rfsgResourceName = '5840_1'    
rfsgSelectedPorts = ""                                              
rfsgWaveformName = "wfm"
rfsg_script = 'script GenerateWaveform repeat forever generate wfm end repeat end script'
rfsgExternalAttenuation = 0.0
rfsgPowerLevel = -10
rfsgFrequencyReferenceSource = NIRfsg.RfsgFrequencyReferenceSource.OnboardClock
rfsgAutomaticSharedLO = NIRfsgPlayback.RfsgPlaybackAutomaticSGSASharedLO.Disabled

#Multitone settings validation
SamplingRateHz = max([abs(tone.offsetHz) for tone in Tones] + [minSamplingRateHz]) * 2.5 #Max rate 2.5x the max offset
#Greatest common denominator of the tones we need to make it divisible by Sampling Rate so we add it to the list it and then we divide it by a minimum resolution
FrequencyStepHz = max(gcd([abs(tone.offsetHz) for tone in Tones] + [SamplingRateHz])/minFrequencyStepHz, SamplingRateHz/minWaveformSize) 
#Sum all the tones power for scaling on the SG power
TonesPower = 10*math.log(sum([math.pow(10,tone.gaindB/10) for tone in Tones]),10)
print("FrequencyStep = {} Hz and Sampling Frequency = {} Hz".format(FrequencyStepHz, SamplingRateHz))


# Initialize Generator
print("Initializing generator..", end='')
rfsgSession = NIRfsg.NIRfsg(rfsgResourceName, True, False, "")
rfsgSession.SignalPath.SelectedPorts = rfsgSelectedPorts
#rfsg_session.Arb.OutputPort = sgPorts
rfsgHandle = rfsgSession.DangerousGetInstrumentHandle()
print("done")


#Coarce Settings
for item in Tones:
    item.offsetHz = np.floor(item.offsetHz/FrequencyStepHz)*FrequencyStepHz
    print(item)


#Init initial waveform
waveform = np.full(int(1/FrequencyStepHz * SamplingRateHz), 0+0j)
Buffer = np.full(int(1/FrequencyStepHz * SamplingRateHz), 1+0j)
#Create Tones on waveform
for item in Tones:
    phaseDrif = item.offsetHz/SamplingRateHz * 2 * np.pi
    OffsetWaveform = [1*np.exp(i*phaseDrif*1j) for i in np.arange(0,len(waveform))]
    waveform = waveform + np.array(OffsetWaveform) * math.pow(10,item.gaindB/20)

# convert back to complex waveform
real = [sample.real for sample in waveform]
imag = [sample.imag for sample in waveform]
iq_net = NationalInstruments.ComplexSingle.ComposeArray(real, imag)
waveform_net = NationalInstruments.ComplexWaveform[NationalInstruments.ComplexSingle].FromArray1D(iq_net)
t0_net = NationalInstruments.PrecisionTimeSpan.FromSeconds(0)
dt_net = NationalInstruments.PrecisionTimeSpan.FromSeconds(1/SamplingRateHz)
waveform_net.PrecisionTiming = NationalInstruments.PrecisionWaveformTiming.CreateWithRegularInterval(dt_net, t0_net)
print("samples = {}".format(waveform_net.SampleCount))

# Generation configuration
print("Configuring generator..", end='')
rfsgSession.RF.Frequency = centerFrequency
rfsgSession.FrequencyReference.Configure(rfsgFrequencyReferenceSource, 10e6)
rfsgSession.RF.ExternalGain = -rfsgExternalAttenuation
rfsgSession.RF.PowerLevel = rfsgPowerLevel

rfsgSession.RF.PowerLevelType = NIRfsg.RfsgRFPowerLevelType.PeakPower
NIRfsgPlayback.NIRfsgPlayback.DownloadUserWaveform(rfsgHandle, rfsgWaveformName, waveform_net, False)
_, papr = NIRfsgPlayback.NIRfsgPlayback.RetrieveWaveformPapr(rfsgHandle, rfsgWaveformName, 0.0)
NIRfsgPlayback.NIRfsgPlayback.StoreWaveformPapr(rfsgHandle, rfsgWaveformName, papr + TonesPower)
NIRfsgPlayback.NIRfsgPlayback.StoreAutomaticSGSASharedLO(rfsgHandle, "", rfsgAutomaticSharedLO)
NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsgHandle, rfsg_script)


print("done")


# Start signal generation
print("Generating radio signal via RFSG Playback Library..", end='')
rfsgSession.Initiate()

input("Press Any Key to Stop Generation")
print("done")
rfsgSession.Abort()
rfsgSession.Close()