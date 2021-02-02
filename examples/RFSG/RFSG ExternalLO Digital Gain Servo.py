import clr, sys, os

sys.path.insert(1,r"C:\Users\LocalAdmin\Documents\stchan\PythonNET_RFmxXC\bin")
clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.NRMX.Fx40")
clr.AddReference("NationalInstruments.RFmx.SpecanMX.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx45")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")
clr.AddReference("NationalInstruments.RFmx.CrossCorrelation.Fx45")
clr.AddReference("NationalInstruments.ModularInstruments.TClock.Fx45")
clr.AddReference("NationalInstruments")
clr.AddReference("NationalInstruments.ModularInstruments.TClock.Fx45")

import NationalInstruments.RFmx.NRMX as NRMX
import NationalInstruments.ModularInstruments.NIRfsg as Rfsg
import NationalInstruments.ModularInstruments.NIRfsgPlayback as RfsgPlayback
import NationalInstruments.RFmx.SpecAnMX as SpecanMX
import time
from NationalInstruments import *
from digitalGainServo import digitalGainServo

centerFrequency = 7e9                                                 # (Hz)

# VSG Settings
sgResourceName = 'BCN_02'
loResourceName = ''  #Leave blank if no externalLO
externalLo = (loResourceName != '')  #If external LO name is specified, set to True
sgExternalAttenuation = 0
sgSelectedPorts = 'if0'
powerLevel = -10
waveformFolder = r"C:\Users\LocalAdmin\Documents\stchan\PythonNET_RFmxXC\WaveformFiles"


waveformPath = waveformFolder + r'\NR_UL_FR2_120kHzSCS_400MHz_64QAM.tdms'
quietTimePath = waveformFolder + r'\quiettime_491p52MSps.tdms'

# Sessions
rfsg = Rfsg.NIRfsg(sgResourceName, True, True, "")
if externalLo:
    lo = Rfsg.NIRfsg(loResourceName, True, True, "")
    lo.FrequencyReference.Configure(Rfsg.RfsgFrequencyReferenceSource.PxiClock, 10e6)



# Configure instruments to share same reference clock
rfsg.FrequencyReference.Configure(Rfsg.RfsgFrequencyReferenceSource.OnboardClock, 10e6)

# Configure instrument ports

rfsg.SignalPath.SelectedPorts = sgSelectedPorts

# Configure center frequency
rfsg.RF.Frequency = centerFrequency

# Configure Power and losses
rfsg.RF.PowerLevel = powerLevel
rfsg.Arb.DigitalGain = 0
rfsg.RF.ExternalGain = -sgExternalAttenuation

# Configure Continuous Generation
rfsgHandle = rfsg.GetInstrumentHandle().DangerousGetHandle()
RfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsgHandle, waveformPath, "ccWfm")
RfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsgHandle, quietTimePath, "qtWfm")
RfsgPlayback.NIRfsgPlayback.StoreWaveformRuntimeScaling(rfsgHandle, "ccWfm", -0.1)
RfsgPlayback.NIRfsgPlayback.StoreWaveformRuntimeScaling(rfsgHandle, "qtWfm", -0.1)
script = "script ccScript\nrepeat forever\ngenerate qtWfm\ngenerate ccWfm\nend repeat\nend script" # no marker, using iq power edge triggers
RfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsgHandle, script)

# Set LO Sharing
# for PXIe - 5830 / PXIe - 5831 IF
if externalLo: #If external LO is specified, drive LO2 for RFSG and export to SAs

    # SG signal configuration
    rfsg.RF.LocalOscillator["lo2"].Source = Rfsg.RfsgLocalOscillatorSource.LOIn  #Use LO_IN for LO2
    loFreq = rfsg.RF.LocalOscillator["lo2"].LOFrequency  #Get requested LO frequency from RFSG
    lo.RF.Frequency = loFreq  #Set output frequency for LO module
    loPower = lo.RF.PowerLevel  #Get LO output power from LO module

    # Check LO Power to make sure it is in range
    if loPower < 6:
        loPower = 6
    elif loPower > 10:
        loPower = 10

    rfsg.RF.LocalOscillator["lo2"].LOInPower = loPower  #Set VST expected LO Input power
    rfsg.Utility.Commit()

else:
    rfsg.RF.LocalOscillator["lo2"].Source = Rfsg.RfsgLocalOscillatorSource.Onboard
    loPower = rfsg.RF.LocalOscillator["lo2"].LOOutPower
    loFreq = rfsg.RF.LocalOscillator["lo2"].LOFrequency



if externalLo:
    lo.Initiate()
rfsg.Initiate()

digitalGainServo(rfsg, powerLevel) #Start Digital Gain Servo
print(rfsg.RF.PowerLevel)
print(rfsg.Arb.DigitalGain)


print("RFSG Generating. Press any key to exit..")
input()
if externalLo:
    lo.Abort()
    lo.Close()
rfsg.Abort()
rfsg.Close()

