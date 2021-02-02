import clr, sys, os

sys.path.insert(1,r"C:\Users\LocalAdmin\Documents\stchan\PythonNET_RFmxXC\bin")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx45")
clr.AddReference("NationalInstruments")


import NationalInstruments.ModularInstruments.NIRfsg as Rfsg
from NationalInstruments import *
import time

overflow = False

def digitalGainServo(rfsg, powerLevel):
    def outputWarning(source, args):
        if "Warning code: 1073366001" in args.Message: #Check for error code for IQ overflow
            global overflow
            overflow = True
    rfsg.DriverOperation.Warning += outputWarning
    digGain = 0.5 #Define initial digitalGain value
    stop = 12
    stepSize = 0.5
    rfsg.Abort() #Abort existing acquisition
    #Servos digital gain
    while digGain <= stop and not overflow:
        rfsg.Arb.DigitalGain = digGain
        rfsg.RF.PowerLevel = powerLevel - digGain
        rfsg.Initiate()
        time.sleep(0.02) #Let RFSG settle
        rfsg.Abort() #When abort is called, warning event may trigger
        if overflow: #If overflow error is detected, back off digital gain by a step size
            rfsg.Arb.DigitalGain -= stepSize
            rfsg.RF.PowerLevel += stepSize
            rfsg.Initiate()
            break
        else: #If no overflow error detected, increase digital gain by a step size
            digGain += stepSize

    rfsg.DriverOperation.Warning -= outputWarning

