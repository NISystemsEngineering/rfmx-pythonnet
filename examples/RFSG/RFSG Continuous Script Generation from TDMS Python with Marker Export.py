# -------------------------------------------------------------------------
# Example Python script for RFSG TDMS waveform generation with Marker Export
# -------------------------------------------------------------------------
# Steps to getting this example to run on a system aside from typical Python environment and driver setup:
# 1) Change "assy_path" and "assy_path2" to reflect absolute path to the DLL folders as placed on your specific system
# 2) Change "wfmFilePath" to reflect absolute path to the "waveforms" folder as placed on your specific system

# Import CLR through Python .NET
import clr

# Import native Python System assembly
import sys

# Location of assemblies
assy_path = r'C:\Windows\Microsoft.NET\assembly\GAC_MSIL\NationalInstruments.ModularInstruments.NIRfsg.Fx40\v4.0_19.2.0.49152__dc6ad606294fc298' #1
assy_path2 = r'C:\Program Files (x86)\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\19.1.0.49152'  #1
sys.path.append(assy_path)
sys.path.append(assy_path2)

clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")


# Import from NationalInstruments.ModularInstruments.NIRfsg.Fx40
from NationalInstruments.ModularInstruments.NIRfsg import *

# Import from NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40
import NationalInstruments.ModularInstruments.NIRfsgPlayback



# -------------------------------------------------------------------------
# RFSG Settings

resourceName = '5840'
centerFreq = 5.18e9;                                                       # (Hz)
powerLevel = -10;                                                        # (dBm)

frequencyReferenceSource = NationalInstruments.ModularInstruments.NIRfsg.RfsgFrequencyReferenceSource.PxiClock;
frequencyReferenceFrequency = 10e6;                                     # (Hz)

wfmFilePath = r'C:\Users\AE-STEG\Desktop\Stegemann Project Code\QCA-Algo\Blanking\Test Wfms\AX 80M MCS11 4038 bytes 32us Idle Nss1.tdms' #2
wfmFilePathList = wfmFilePath.split('\\')
wfmFileName = wfmFilePathList[-1]
waveformName = 'wlan'

script = """script s
            repeat forever
            generate wlan marker0(0)
            end repeat
            end script"""

# -----------------------------------------------------------------------
# Configure RFSG Session

# Intialize Session
rfsg = NIRfsg(resourceName, True, True)
rfsgHandle = rfsg.GetInstrumentHandle().DangerousGetHandle()


rfsg.RF.Configure(centerFreq, powerLevel)
rfsg.FrequencyReference.Configure(frequencyReferenceSource, frequencyReferenceFrequency)

rfsg.Arb.GenerationMode = NationalInstruments.ModularInstruments.NIRfsg.RfsgWaveformGenerationMode.Script
rfsg.RF.PowerLevelType = NationalInstruments.ModularInstruments.NIRfsg.RfsgRFPowerLevelType.PeakPower

#Export Marker Event to PXI Trig line
rfsg.DeviceEvents.MarkerEvents[0].ExportedOutputTerminal = NationalInstruments.ModularInstruments.NIRfsg.RfsgMarkerEventExportedOutputTerminal.PxiTriggerLine0;

# -------------------------------------------------------------------------
# Load TDMS waveform data from file

NationalInstruments.ModularInstruments.NIRfsgPlayback.NIRfsgPlayback.ReadAndDownloadWaveformFromFile(rfsgHandle, wfmFilePath, waveformName)
NationalInstruments.ModularInstruments.NIRfsgPlayback.NIRfsgPlayback.SetScriptToGenerateSingleRfsg(rfsgHandle, script)


# Initiate generation
rfsg.Initiate()
print("Generating " + wfmFileName + "...")

# Keep generating until user presses key
input("Press Enter to Stop Generation")

# -------------------------------------------------------------------------
# Stop generation and disable output

rfsg.Abort()
rfsg.RF.OutputEnabled = False

# -------------------------------------------------------------------------
# Close the RFSG NIRfsg session

rfsg.Close()

