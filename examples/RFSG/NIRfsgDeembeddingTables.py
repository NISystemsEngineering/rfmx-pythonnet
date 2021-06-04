"""
Demonstrates how to use multidimensional .NET arrays to configure 2-port de-embedding tables from Python
"""

import clr
import sys

# directories below may change depending on installed packages and version numbers
sys.path.append(r'C:\Program Files (x86)\National Instruments\Measurement Studio\DotNET\v4.0\AnyCPU\NationalInstruments.Common 19.0.40')
sys.path.append(r'C:\Program Files\IVI Foundation\IVI\Microsoft.NET\Framework64\v4.5.50709\NationalInstruments.ModularInstruments.NIRfsg 20.0.0')

# add references to .NET assemblies
clr.AddReference('System')
clr.AddReference('NationalInstruments.Common')  # contains ComplexDouble type
clr.AddReference('NationalInstruments.ModularInstruments.NIRfsg.Fx45')

# import .NET assemblies
import System
import NationalInstruments
import NationalInstruments.ModularInstruments.NIRfsg as NIRfsg

# create python native de-embedding lists, assuming port 2 is towards the DUT
freq = [1e9, 2e9, 3e9]
fwd_ref_gain = [complex(-1, 0), complex(-2, 0), complex(-3, 0)]  # s11
fwd_gain = [complex(-4, 0), complex(-5, 0), complex(-6, 0)]  # s21
reverse_gain = [complex(-7, 0), complex(-8, 0), complex(-9, 0)]  # s12
reverse_ref_gain = [complex(-10, 0), complex(-11, 0), complex(-12, 0)]  # s22

# create 3-dimensional .NET array type using System.Array
s2p = System.Array.CreateInstance(NationalInstruments.ComplexDouble, len(freq), 2, 2)

# populate .NET s-paramater array from Python types
for i, s11, s21, s12, s22 in zip(range(len(freq)), fwd_ref_gain, fwd_gain, reverse_gain, reverse_ref_gain):
    s11 = NationalInstruments.ComplexDouble(s11.real, s11.imag)
    s21 = NationalInstruments.ComplexDouble(s21.real, s21.imag)
    s12 = NationalInstruments.ComplexDouble(s12.real, s12.imag)
    s22 = NationalInstruments.ComplexDouble(s22.real, s22.imag)

    # indexes correspond to [freq, towards port, away port]
    s2p.SetValue(s11, i, 0, 0)
    s2p.SetValue(s21, i, 1, 0)
    s2p.SetValue(s12, i, 0, 1)
    s2p.SetValue(s22, i, 1, 1)

# create a simulated VST to demonstrate de-embedding configuration
rfsg = NIRfsg.NIRfsg('sim', True, False, 'Simulate=1, DriverSetup=Model:5840')

# load s-parameter array into RFSG with orientation of port 2 towards the DUT, use indexer to select instrument port
rfsg.Deembedding[""].CreateDeembeddingSParameterTableArray('exampleTable', freq, s2p, NIRfsg.RfsgSParameterOrientation.Port2TowardsDut)

rfsg.RF.PowerLevel = 0  # if running on real hardware, the power level needs to be set to prevent potential errors
rfsg.RF.Frequency = 1.5e9  # change this value to observe effect on returned de-emdedding table below

# fetch and index individual s-parameters
s_param = rfsg.Deembedding.GetDeembeddingSParameters(None)  # looks to sg configuration for selected port, etc.
s11 = s_param.GetValue(0, 0)
s21 = s_param.GetValue(1, 0)
s12 = s_param.GetValue(0, 1)
s22 = s_param.GetValue(1, 1)

# convert .NET ComplexDouble types to Python complex types
s11 = complex(s11.Real, s11.Imaginary)
s21 = complex(s21.Real, s21.Imaginary)
s12 = complex(s12.Real, s12.Imaginary)
s22 = complex(s22.Real, s22.Imaginary)

# print interpolated values to console
print(f'Interpolated s11: {s11}')
print(f'Interpolated s21: {s21}')
print(f'Interpolated s12: {s12}')
print(f'Interpolated s22: {s22}')

# close the simulated NIRfsg session
rfsg.Close()
