from sys import path
from os import environ
import clr

path.append(environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.Common")

from NationalInstruments import AnalogWaveform, Spectrum


def __ramp(start, delta, num_samples):
    for i in range(num_samples):
        yield start
        start = start + delta


def decompose_complex_array(complex_array):
    """ Decomposes an NI ComplexSingle[] or ComplexDouble[] into a list of complex numbers. """
    # use list comprehension of DecomposeArray so we don't have to identify a type
    return [complex(iq.Real, iq.Imaginary) for iq in complex_array]


def decompose_complex_waveform(complex_waveform):
    """ Decomposes an NI ComplexWaveform in a tuple of x and y values. """
    t0 = complex_waveform.PrecisionTiming.TimeOffset.TotalSeconds
    dt = complex_waveform.PrecisionTiming.SampleInterval.TotalSeconds
    x = list(__ramp(t0, dt, complex_waveform.SampleCount))
    y = decompose_complex_array(complex_waveform.GetRawData())
    return t0, dt, y


def decompose_analog_waveform(analog_waveform: AnalogWaveform):
    """ Decomposes an NI AnalogWaveform into a tuple of x and y values. """
    t0 = analog_waveform.PrecisionTiming.TimeOffset.TotalSeconds
    dt = analog_waveform.PrecisionTiming.SampleInterval.TotalSeconds
    x = list(__ramp(t0, dt, analog_waveform.SampleCount))
    y = list(analog_waveform.GetRawData())
    return x, y


def decompose_spectrum(spectrum: Spectrum):
    """ Decomposes an NI Spectrum into a tuple of x and y values. """
    f0 = spectrum.StartFrequency
    df = spectrum.FrequencyIncrement
    x = list(__ramp(f0, df, spectrum.SampleCount))
    y = list(spectrum.GetData())
    return x, y
