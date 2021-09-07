import sys
import os
import clr

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\Measurement Studio\DotNET\v4.0\AnyCPU\NationalInstruments.Common 19.1.40")
sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.Common")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")

import NationalInstruments  # noqa
import NationalInstruments.ModularInstruments.NIRfsgPlayback as NIRfsgPlayback  # noqa

# read waveform from file
waveform_path = os.path.abspath(r"../../waveforms/nr100.tdms")
waveform = NationalInstruments.ComplexWaveform[NationalInstruments.ComplexDouble](0)  # for selecting correct overload
_, waveform = NIRfsgPlayback.NIRfsgPlayback.ReadWaveformFromFileComplex(waveform_path, waveform)

# convert to python types
iq = [complex(sample.Real, sample.Imaginary) for sample in waveform.GetScaledData()]
dt = waveform.PrecisionTiming.SampleInterval.TotalSeconds
t0 = waveform.PrecisionTiming.TimeOffset.TotalSeconds
