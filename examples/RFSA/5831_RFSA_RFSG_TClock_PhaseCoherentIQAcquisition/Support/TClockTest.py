import clr, sys, os

bin_path = r"C:\Users\LocalAdmin\Documents\GitHub\stchan-sandbox\BarcelonaSweepSGPhase_ContinuousSA\bin"
sys.path.insert(1, bin_path)

print(clr.FindAssembly("NationalInstruments.Common"))
print(clr.AddReference(bin_path + r"\NationalInstruments.ModularInstruments.NIRfsa.Fx45.dll"))
print(clr.AddReference(bin_path + r"\NationalInstruments.ModularInstruments.TClock.Fx40.dll"))
print(clr.AddReference(bin_path + r"\NationalInstruments.ModularInstruments.Common.dll"))
print(clr.AddReference(bin_path + r"\NationalInstruments.Common.dll"))


import NationalInstruments.ModularInstruments.NIRfsa as Rfsa
import NationalInstruments.ModularInstruments.SystemServices.TimingServices as TClock