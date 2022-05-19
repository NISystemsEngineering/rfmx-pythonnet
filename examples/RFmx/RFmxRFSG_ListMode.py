""" 
Abinash Sinha
Applications Engineer
National Instruments (NI)
"""


from pathlib import Path, PureWindowsPath
import os
import sys
import clr # use pip install pythonnet


### Defining path references for NI assemblies ###
print("Defining path references and importing NI assemblies.. ", end='')
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
print("Done")


# Define the instrument and RF parameters
print("Setting measurement parameters.. ", end='')
centerFrequency = 3.5e9
rfsgResourceName = 'VST_5840_SG'    
rfsgSelectedPorts = ""                                              
waveformFolder = Path(r'C:\Users\BF8880\Documents\asinha\Waveforms\NR_FR1_1CC_100M_QPSK_30kHz_UL.tdms')
rfsgWaveformName = "wfm"
rfsgExternalAttenuation = 0.0
rfsgFrequencyReferenceSource = NIRfsg.RfsgFrequencyReferenceSource.OnboardClock
rfsgTriggerEdge = NIRfsg.RfsgTriggerEdge.RisingEdge
rfsgFrequency = 10.0e6
rfsaResourceName = 'VST_5840_SA'   
rfsaSelectedPorts = ""
rfsaExternalAttenuation = 0.0
rfsaFrequencyReferenceSource = InstrMX.RFmxInstrMXConstants.OnboardClock
rfsaFrequency = 10.0e6
linkDirection = NRMX.RFmxNRMXLinkDirection.Uplink
frequencyRange = NRMX.RFmxNRMXFrequencyRange.Range1
carrierBandwidth = 100e6
subcarrierSpacing = 30e3
startReferenceLevel = -20.0
stopReferenceLevel = 0.0
step0IQPowerEdgeLevel = -10
step0MinimumQuietTime = 0.0
triggerDelay = 0.0
chpSweepTime = False
sweepTimeInterval = 1.0e-3
listStepTimerUnit = NRMX.RFmxNRMXListStepTimerUnit.Time
listStepTimerDuration = 1.50e-3
listStepTimerOffset = 0.0
numberOfSteps = 10
traceStepNumber = 0
inRampPattern = [0]*numberOfSteps
rampPattern = []

def linearRampPattern(start, end, samples, includeEnd, rampPattern):
    if (includeEnd):
        m = samples
    else:
        m = (samples-1)
    delta = (end-start)/m
    for s in range(samples):
        rampPattern[s] = (start + (s*delta))
    return (rampPattern)

timeout = 10.0
configListProperties = []
step = [0]*numberOfSteps
totalAggregatedPower = [0]*numberOfSteps
rampPattern = linearRampPattern(startReferenceLevel, stopReferenceLevel, numberOfSteps, False, inRampPattern)            
print("Done")


### Configuring RFSG parameters ###
print("Configuring RFSG parameters.. ", end='')
rfsgSession = NIRfsg.NIRfsg(rfsgResourceName, True, False, "")
rfsgSession.FrequencyReference.Configure(rfsgFrequencyReferenceSource, rfsgFrequency)
rfsgSession.RF.ExternalGain = -rfsgExternalAttenuation
rfsgSession.SignalPath.SelectedPorts = rfsgSelectedPorts
rfsgSession.RF.Frequency = centerFrequency
triggerSource = NIRfsg.RfsgDigitalEdgeConfigurationListStepTriggerSource.FromString("Marker0Event")
rfsgSession.Triggers.ConfigurationListStepTrigger.DigitalEdge.Configure(triggerSource, rfsgTriggerEdge)
rfsgHandle = rfsgSession.DangerousGetInstrumentHandle()
NIRfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsgHandle, str(PureWindowsPath(waveformFolder)), rfsgWaveformName)
_, sampleRate = NIRfsgPlayback.NIRfsgPlayback.RetrieveWaveformSampleRate(rfsgHandle, rfsgWaveformName, 0.0)
_, papr = NIRfsgPlayback.NIRfsgPlayback.RetrieveWaveformPapr(rfsgHandle, rfsgWaveformName, 0.0)
numberOfSamples = int(sampleRate * listStepTimerDuration)
markerLocation = int(sampleRate * sweepTimeInterval)
script = f"script GenerateWaveform\nrepeat forever\ngenerate {rfsgWaveformName} subset(0, {numberOfSamples}) marker0({markerLocation})\nend repeat\nend script"
NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsgHandle, script)
configListProperties.append(NIRfsg.RfsgConfigurationListProperties.PowerLevel)
rfsgSession.BasicConfigurationList.CreateConfigurationList("PowerLevelList", configListProperties, True)
for s in range(numberOfSteps):
    rfsgSession.BasicConfigurationList.CreateStep(True)
    rfsgSession.RF.PowerLevel = rampPattern[s]
print("Done")


### Configuring RFmx parameters ###
print("Configuring RFmx parameters.. ", end='')
instrSession = InstrMX.RFmxInstrMX.GetSession(rfsaResourceName, "")
instrSession.ConfigureFrequencyReference("", rfsaFrequencyReferenceSource, rfsaFrequency)
nrList = InstrMX.RFmxNRMXExtension.GetNRList(instrSession, "CHP_List")
for s in range(numberOfSteps):
    step[s] = nrList.CreateListStep()
    step[s].SetReferenceLevel("", papr + rampPattern[s])
    if (s == 0):
        step[s].ConfigureIQPowerEdgeTrigger("", "0", NRMX.RFmxNRMXIQPowerEdgeTriggerSlope.Rising, step0IQPowerEdgeLevel, 
            triggerDelay, NRMX.RFmxNRMXTriggerMinimumQuietTimeMode.Manual, step0MinimumQuietTime,
            NRMX.RFmxNRMXIQPowerEdgeTriggerLevelType.Relative, True)            
    else:
        step[s].ConfigureDigitalEdgeTrigger("", "TimerEvent", NRMX.RFmxNRMXDigitalEdgeTriggerEdge.Rising, triggerDelay, True)
        step[s].SetListStepTimerOffset("", listStepTimerOffset)        
    step[s].SetListStepTimerDuration("", listStepTimerDuration);
stepAll = nrList.GetListStepAll()
stepAll.ConfigureFrequency("", centerFrequency);
stepAll.SetSelectedPorts("", rfsaSelectedPorts);
stepAll.ConfigureExternalAttenuation("", rfsaExternalAttenuation);
stepAll.SetListStepTimerUnit("", listStepTimerUnit);
stepAll.SetLinkDirection("", linkDirection);
stepAll.SetFrequencyRange("", frequencyRange);
stepAll.ComponentCarrier.SetBandwidth("", carrierBandwidth);
stepAll.ComponentCarrier.SetBandwidthPartSubcarrierSpacing("", subcarrierSpacing);
stepAll.SelectMeasurements("", NRMX.RFmxNRMXMeasurementTypes.Chp, True)
stepAll.Chp.Configuration.ConfigureSweepTime("", chpSweepTime, sweepTimeInterval)

nrList.Initiate("", "")
rfsgSession.Initiate()
instrSession.WaitForAcquisitionComplete(timeout)
print("Done")    
    

### Retrieve and print results ###
print('\n'"------------------Measurement------------------")
for s in range(numberOfSteps):
    _, totalAggregatedPower[s] = step[s].Chp.Results.FetchTotalAggregatedPower("", timeout, 0.0)
    print("Total Aggregated Power (dBm)     : {0}".format(totalAggregatedPower[s]))


### CLosing all active sessions ###
print('\n'"Closing all active sessions.. ", end='')
nrList.Dispose()
instrSession.Close()
rfsgSession.Abort()
rfsgSession.BasicConfigurationList.DeleteConfigurationList("PowerLevelList")
NIRfsgPlayback.NIRfsgPlayback.ClearWaveform(rfsgHandle, rfsgWaveformName)
rfsgSession.Close()
print("Done")


















