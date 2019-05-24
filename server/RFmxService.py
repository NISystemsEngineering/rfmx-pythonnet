# To use the .NET assemblies 3 things need to be done
# * Add the assembly reference to the clr system
# * Import the assembly
# * Expose the assembly via the RFmxService (rpyc)

import rpyc
import clr
import sys
import os

programFilesPath64 = os.environ["ProgramFiles"]
programFilesPath32 = os.environ["ProgramFiles(x86)"]

# Add search path for NI .NET Assemblies to system path
sys.path.append(programFilesPath32 + r'\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current')

# Add in all of the IVI .NET paths for finding additional assemblies
IVIdotNetPath = programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64'
for x in os.walk(IVIdotNetPath):
    sys.path.append(x[0])

# These are required for all use cases
clr.AddReference("NationalInstruments.Common")
import System
import NationalInstruments

# Add references to .NET Assemblies, then import the assembly as a module
# The assemblies needed can be found in the component ReadME in the .NET Framework section
# This method uses more lines of code, but is more robust for systems that may not have all modules installed

def init_ModularInstruments():
    ModularInstruments = None
    try:
        clr.AddReference("NationalInstruments.ModularInstruments.Common")
        import NationalInstruments.ModularInstruments as ModularInstruments
        print("NI Modular Instruments Common Initialized")
    except: print("NI Modular Instruments Common not available.")
    return ModularInstruments

def init_NiRfsg():
    NIRfsg = None
    try:
        clr.AddReference("NationalInstruments.ModularInstruments.NIRfsg.Fx40")
        import NationalInstruments.ModularInstruments.NIRfsg as NIRfsg
        print("NiRfsg Initialized")
    except: print("NiRfsg not available.")
    return NIRfsg

def init_NiRfsgPlayback():
    NIRfsgPlayback = None
    try:
        clr.AddReference("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40")
        import NationalInstruments.ModularInstruments.NIRfsgPlayback as NIRfsgPlayback
        print("NiRfsgPlayback Initialized")
    except: print("NiRfsgPlayback not available.")
    return NIRfsgPlayback

def init_InstrMx():
    InstrMX = None
    try:
        clr.AddReference("NationalInstruments.RFmx.InstrMX.Fx40")
        import NationalInstruments.RFmx.InstrMX as InstrMX
        print("InstrMX Initialized")
    except: print("InstrMX not available.")
    return InstrMX

def init_SpecAnMx():
    SpecAnMX = None
    try:
        clr.AddReference("NationalInstruments.RFmx.SpecAnMX.Fx40")
        import NationalInstruments.RFmx.SpecAnMX as SpecAnMX
        print("SpecAnMX Initialized")
    except: print("SpecAnMX not available.")
    return SpecAnMX

def init_LteMx():
    LteMX = None
    try:
        clr.AddReference("NationalInstruments.RFmx.LteMX.Fx40")
        import NationalInstruments.RFmx.LteMX as LteMX
        print("LteMX Initialized")
    except: print("LteMX not available.")
    return LteMX

def init_NRMx():
    NRMX = None
    try:
        clr.AddReference("NationalInstruments.RFmx.NRMX.Fx40")
        import NationalInstruments.RFmx.NRMX as NRMX
        print("NRMX Initialized")
    except: print("NR not available.")
    return NRMX

# Run the initializations
# Names must match the esposed properties in the RFmxService
ModularInstruments = init_ModularInstruments()
NIRfsg = init_NiRfsg()
NIRfsgPlayback = init_NiRfsgPlayback()
InstrMX = init_InstrMx()
SpecAnMX = init_SpecAnMx()
LteMX = init_LteMx()
NRMX = init_NRMx()

# create RFmxServer service that inherits from rpyc.Service

# global variables
instr = None

class RFmxService(rpyc.Service):
    # Required Components
    exposed_System = System
    exposed_NationalInstruments = NationalInstruments
    # Optional Components
    exposed_ModularInstruments = ModularInstruments
    exposed_NIRfsg = NIRfsg
    exposed_NIRfsgPlayback = NIRfsgPlayback
    exposed_InstrMX = InstrMX
    exposed_SpecAnMX = SpecAnMX
    exposed_LteMX = LteMX
    exposed_NRMX = NRMX

    # this function helps keep a global reference to an open RFmx session on the server
    def RFmxRemoteInstrMX(self, resourceName, optionString):
        global instr
        if instr is not None and not instr.IsDisposed:
            return instr
        else:
            instr = InstrMX.RFmxInstrMX(resourceName, optionString)
            return instr

    def ComplexWaveform(self, nettype, param):
        return NationalInstruments.ComplexWaveform[nettype](param)

    def exec(self, source):
        exec(source, globals(), locals())

    def eval(self, expression):
        return eval(expression, globals(), locals())

# start the server
if __name__ == "__main__":
    port = 18861
    print("Starting RFmxService on port " + str(port))
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RFmxService, port = port, protocol_config = {"allow_all_attrs" : True, "allow_setattr": True})
    # t.start()
    try:
        t.start()
    except KeyboardInterrupt:
        print("Keyboard Interrupt Triggered")
    finally:
        t.close()
        print("RFmxService stopped")