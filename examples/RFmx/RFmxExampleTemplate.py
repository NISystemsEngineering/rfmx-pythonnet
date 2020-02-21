import clr, sys, os

sys.path.append(os.environ["PROGRAMFILES(X86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")

clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")

import NationalInstruments.RFmx.InstrMX as InstrMX
# import NationalInstruments.RFmx.SpecAnMX as SpecAnMX
# import NationalInstruments.RFmx.NRMX as NRMX
# import NationalInstruments.RFmx.LteMX as LteMX

instr = InstrMX.RFmxInstrMX("VST_01", "")
# specan = InstrMX.RFmxSpecAnMXExtension.GetSpecAnSignalConfiguration(instr)
# nr = InstrMX.RFmxNRMXExtension.GetNRSignalConfiguration(instr)
# lte = InstrMX.RFmxLteMXExtension.GetLteSignalConfiguration(instr)

instr.Close()
