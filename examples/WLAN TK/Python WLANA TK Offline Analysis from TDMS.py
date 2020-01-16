# -------------------------------------------------------------------------
#Example Python script for WLAN TK Mod Acc using WLAN TK C# wrapper built into .NET assembly
# -------------------------------------------------------------------------
# Steps to getting this example to run on a system outside Python environment and driver setup:
# 1) Change "assy_path" to reflect absolute path to the "bin" folder as placed on your specific system
# 2) Change "wfmFilePath" to reflect absolute path to the "waveforms" folder as placed on your specific system

# Import CLR through Python .NET
import clr

# Import native Python System assembly
import sys

# Location of assemblies
assy_path = r'C:\Users\LocalAdmin\Documents\GitHub\rfmx-pythonnet\bin' #1
assy_path2 = r'C:\Program Files (x86)\National Instruments\Measurement Studio\DotNET\v4.0\AnyCPU\NationalInstruments.Common 19.0.40'
assy_path3 = r'C:\Program Files (x86)\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\19.1.0.49152'
sys.path.append(assy_path)
sys.path.append(assy_path2)
sys.path.append(assy_path3)

clr.AddReference("NationalInstruments.ModularInstruments.Interop.Fx40")
clr.AddReference("NationalInstruments.RFToolkits.Interop.Fx40")
clr.AddReference("NationalInstruments.Common")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")

# Import from created assembly "WLANA_TK for Python NET"
from NationalInstruments.RFToolkits.Interop import *
from NationalInstruments.ModularInstruments.Interop import *

# Import from NationalInstruments.Common
import NationalInstruments

# Import from NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40
import NationalInstruments.ModularInstruments.NIRfsgPlayback


# -------------------------------------------------------------------------
# VSA Settings

standard = niWLANAConstants.Standard80211axMimoOfdm;
chBW = 80.00e6;
ofdmMaximumSymbolsUsed = 16;
timeout = 10;

t0 = [0];
dt = [0];
numSamp = 0;
reset = 1;
avgDone = 1;

# Result Variables

rmsEVM = 0.0;                                               # (dB)
detectedNumSymUsed = 0;
carrierFrequencyLeakage = 0.0;                              # (Hz)
spectralFlatnessMargin = 0.0;                               # (dB)

sampRate = 0;
wfmIndex = 0;

# -------------------------------------------------------------------------
# Load TDMS waveform data from file

# Create NI ComplexWaveform<ComplexDouble> type
wfmComplexDoubleType = NationalInstruments.ComplexDouble.ComposeArray([0],[0])
wfmData = NationalInstruments.ComplexWaveform[NationalInstruments.ComplexDouble].FromArray1D(wfmComplexDoubleType)

wfmFilePath = r'C:\Users\LocalAdmin\Documents\GitHub\rfmx-pythonnet\waveforms\wlan80ax.tdms' #2

_, wfmData = NationalInstruments.ModularInstruments.NIRfsgPlayback.NIRfsgPlayback.ReadWaveformFromFileComplex(wfmFilePath, wfmData)
_, sampRate = NationalInstruments.ModularInstruments.NIRfsgPlayback.NIRfsgPlayback.ReadSampleRateFromFile(wfmFilePath,  wfmIndex, sampRate)

dt[0] = 1/sampRate;


realArray = []
realArray = wfmData.GetRealDataArray(True)
numSamp = realArray.Length;

imagArray = []
imagArray = wfmData.GetImaginaryDataArray(True)

wfmArray = [NationalInstruments.ModularInstruments.Interop.niComplexNumber() for i in range(numSamp)]

for i in range(numSamp):
    wfmArray[i].Real = realArray[i]
    wfmArray[i].Imaginary = imagArray[i]

# -------------------------------------------------------------------------
# Init WLANA session
aSession = niWLANA(niWLANAConstants.CompatibilityVersion050000)

# -------------------------------------------------------------------------
# Configure WLANA acquisition
aSession.SetStandard(None, standard)
aSession.SetChannelBandwidth(None, chBW)
aSession.SetOfdmDemodMaximumSymbolsUsed(None, ofdmMaximumSymbolsUsed)
aSession.SetOfdmDemodAutoComputeAcquisitionLengthEnabled(None, True)
aSession.SelectMeasurements(niWLANAConstants.OfdmDemodMeasurement)
aSession.SetOfdmDemodBurstStartDetectionEnabled('', 0)


# -------------------------------------------------------------------------
# Execute measurement
_, avgDone = aSession.AnalyzeMIMOIQComplexF64(t0, dt, wfmArray, 1, numSamp, reset, avgDone)

# -------------------------------------------------------------------------
# Fetch results

channelString = "stream0"
_, rmsEVM = aSession.GetResultOfdmDemodRmsEvm(channelString, rmsEVM)
_, detectedNumSymUsed = aSession.GetOFDMDemodNumberOfSymbolsUsed(None, detectedNumSymUsed)

channelString = "channel0"
_, carrierFrequencyLeakage = aSession.GetResultOfdmDemodCarrierFrequencyLeakage(channelString, carrierFrequencyLeakage)

channelString = "channel0/stream0"
_, spectralFlatnessMargin = aSession.GetResultOfdmDemodSpectralFlatnessMargin(channelString, spectralFlatnessMargin)


# -------------------------------------------------------------------------
# Report results to the user
print("\nMeasurement Success!\n")
print("Results\n-----------------------------------")
print("Composite RMS EVM (dB): %.2f" %(rmsEVM))
print("Number of OFDM symbols used: ",detectedNumSymUsed)
print("Spectral Flatness Margin (dB): %.2f" %(spectralFlatnessMargin))
print("OFDM Carrier Frequency Leakage (dB): %.2f" %(carrierFrequencyLeakage))


# -------------------------------------------------------------------------
# Close instrument session
aSession.Close()
