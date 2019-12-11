# To use the .NET assemblies 3 things need to be done
# 1. Add the assembly reference to the clr system
# 2. Import the assembly
# 3. Expose the assembly via the RFmxService (rpyc)

import rpyc
import clr
import sys
import os

programFilesPath64 = os.environ["ProgramFiles"]
programFilesPath32 = os.environ["ProgramFiles(x86)"]

# Add search path for NI .NET assemblies to system path
sys.path.append(programFilesPath32 + r'\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current')

# Add in all of the IVI .NET paths for finding additional assemblies
iviDotNetPath = programFilesPath64 + r'\IVI Foundation\IVI\Microsoft.NET\Framework64'
for x in os.walk(iviDotNetPath):
    sys.path.append(x[0])

# This function allows for dynamic importation of modules since some modules may not be installed
def ImportDotNetModule(assemblyName, namespace):
    from System.IO import FileNotFoundException
    module = None
    try:
        clr.AddReference(assemblyName)
        module = __import__(namespace)
        print(namespace + " imported successfully from " + assemblyName + '.')
    except FileNotFoundException:
        print(assemblyName + " was not found.")
    except:
        print("An exception occured loading " + namespace + " from " + assemblyName + ". Module was not loaded.")
    return module

# Global variables
instr = None

class RFmxService(rpyc.Service):
    # Import common modules
    exposed_System = System = ImportDotNetModule("System", "System")
    exposed_NationalInstruments = ImportDotNetModule("NationalInstruments.Common", "NationalInstruments")
    exposed_ModularInstruments = ImportDotNetModule("NationalInstruments.ModularInstruments.Common", "NationalInstruments.ModularInstruments")

    # Import generation modules
    exposed_NIRfsg = ImportDotNetModule("NationalInstruments.ModularInstruments.NIRfsg.Fx40", "NationalInstruments.ModularInstruments.NIRfsg")
    exposed_NIRfsgPlayback = ImportDotNetModule("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40", "NationalInstruments.ModularInstruments.NIRfsgPlayback")

    # Import measurement modules
    exposed_InstrMX = ImportDotNetModule("NationalInstruments.RFmx.InstrMX.Fx40", "NationalInstruments.RFmx.InstrMX")
    exposed_SpecAnMX = ImportDotNetModule("NationalInstruments.RFmx.SpecAnMX.Fx40", "NationalInstruments.RFmx.SpecAnMX")
    exposed_LteMX = ImportDotNetModule("NationalInstruments.RFmx.LteMX.Fx40", "NationalInstruments.RFmx.LteMX")
    exposed_NRMX = ImportDotNetModule("NationalInstruments.RFmx.NRMX.Fx40", "NationalInstruments.RFmx.NRMX")
    exposed_WlanMX = ImportDotNetModule("NationalInstruments.RFmx.WlanMX.Fx40", "NationalInstruments.RFmx.WlanMX")

    # This function helps keep a global reference to an open RFmx session on the server
    def GetGlobalInstrMX(self, resourceName, optionString):
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
    try:
        t.start()
    except:
        pass
    t.close()
    print("RFmxService stopped")