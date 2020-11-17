"""
Demonstrates how to get an NIRfsa session from an RFmx Instr session
"""

import clr
import sys
import os

# paths below may vary depending on installed versions on RFmx and RFSA
sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")
sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\IVI Foundation\IVI\Microsoft.NET\Framework32\v4.5.50709\NationalInstruments.ModularInstruments.NIRfsa 19.1.0")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
clr.AddReference("NationalInstruments.ModularInstruments.NIRfsa.Fx45")

import System
import NationalInstruments.RFmx.InstrMX as InstrMX
import NationalInstruments.ModularInstruments.NIRfsa as NIRfsa

instr = InstrMX.RFmxInstrMX("VST2_01", "")

_, rfsa_handle = instr.DangerousGetNIRfsaHandle(System.IntPtr.Zero)
rfsa = NIRfsa.NIRfsa(rfsa_handle)  # construct NIRfsa object from handle

instr.Close()
