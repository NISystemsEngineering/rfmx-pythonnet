import clr, sys, os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")

import NationalInstruments.RFmx.InstrMX as InstrMX

instr = InstrMX.RFmxInstrMX("VST_01", "")

instr.Close()
