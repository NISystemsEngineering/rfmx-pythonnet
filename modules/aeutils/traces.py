
def decompose_complex_array(complex_array) -> list:
    """ Decomposes an NI ComplexSingle[] or ComplexDouble[] into a list of complex numbers. """
    # use list comprehension of DecomposeArray so we don't have to identify a type
    return [complex(iq.Real, iq.Imaginary) for iq in complex_array]


def decompose_complex_waveform(complex_waveform) -> tuple:
    """ Decomposes an NI ComplexWaveform into a tuple of t0, dt, and y values. """
    t0 = complex_waveform.PrecisionTiming.TimeOffset.TotalSeconds
    dt = complex_waveform.PrecisionTiming.SampleInterval.TotalSeconds
    y = decompose_complex_array(complex_waveform.GetRawData())
    return t0, dt, y


def decompose_analog_waveform(analog_waveform) -> tuple:
    """ Decomposes an NI AnalogWaveform into a tuple of t0, dt, and y values. """
    t0 = analog_waveform.PrecisionTiming.TimeOffset.TotalSeconds
    dt = analog_waveform.PrecisionTiming.SampleInterval.TotalSeconds
    y = list(analog_waveform.GetRawData())
    return t0, dt, y


def decompose_spectrum(spectrum) -> tuple:
    """ Decomposes an NI Spectrum into a tuple of f0, dt, and y values. """
    f0 = spectrum.StartFrequency
    df = spectrum.FrequencyIncrement
    y = list(spectrum.GetData())
    return f0, df, y
