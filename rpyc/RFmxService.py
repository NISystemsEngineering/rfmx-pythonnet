# To use the .NET assemblies 3 things need to be done
# 1. Add the assembly reference to the clr system
# 2. Import the assembly
# 3. Expose the assembly via the RFmxService (rpyc)

import rpyc
import clr
import sys
import os

# Add search paths for .NET assemblies to system path
sys.path.append(os.environ["ProgramFiles(x86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current")
sys.path.append(os.path.abspath(os.getcwd() + "\\..\\bin"))

# Add in all of the IVI .NET paths for finding additional assemblies
iviDotNetPath = os.environ["ProgramFiles"] + r"\IVI Foundation\IVI\Microsoft.NET\Framework64"
for x in os.walk(iviDotNetPath):
    sys.path.append(x[0])

# This function allows for dynamic importation of modules since some modules may not be installed
def ImportDotNetSubmodule(assemblyName, namespace):
    from System.IO import FileNotFoundException
    submodule = None
    try:
        clr.AddReference(assemblyName)
        submoduleName = namespace.split('.')[-1]
        exec("import " + namespace + " as " + submoduleName)
        submodule = eval(submoduleName)
        print(namespace + " imported successfully from " + assemblyName + '.')
    except FileNotFoundException:
        print(assemblyName + " was not found.")
    except Exception as e:
        print("An exception occured loading " + namespace + " from " + assemblyName + ". Module was not loaded.")
        print(e)
    return submodule

# Global variables
instr = None

class RFmxService(rpyc.Service):
    # Import common modules
    exposed_System = ImportDotNetSubmodule("System", "System")
    exposed_NationalInstruments = ImportDotNetSubmodule("NationalInstruments.Common", "NationalInstruments")
    exposed_ModularInstruments = ImportDotNetSubmodule("NationalInstruments.ModularInstruments.Common", "NationalInstruments.ModularInstruments")

    # Import RFSG generation modules
    exposed_NIRfsg = ImportDotNetSubmodule("NationalInstruments.ModularInstruments.NIRfsg.Fx40", "NationalInstruments.ModularInstruments.NIRfsg")
    exposed_NIRfsgPlayback = ImportDotNetSubmodule("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40", "NationalInstruments.ModularInstruments.NIRfsgPlayback")

    # Import RFmx measurement modules
    exposed_InstrMX = ImportDotNetSubmodule("NationalInstruments.RFmx.InstrMX.Fx40", "NationalInstruments.RFmx.InstrMX")
    exposed_SpecAnMX = ImportDotNetSubmodule("NationalInstruments.RFmx.SpecAnMX.Fx40", "NationalInstruments.RFmx.SpecAnMX")
    exposed_LteMX = ImportDotNetSubmodule("NationalInstruments.RFmx.LteMX.Fx40", "NationalInstruments.RFmx.LteMX")
    exposed_NRMX = ImportDotNetSubmodule("NationalInstruments.RFmx.NRMX.Fx40", "NationalInstruments.RFmx.NRMX")
    exposed_WlanMX = ImportDotNetSubmodule("NationalInstruments.RFmx.WlanMX.Fx40", "NationalInstruments.RFmx.WlanMX")

    # Import measurement toolkit modules
    exposed_WlanTK = ImportDotNetSubmodule("NationalInstruments.RFToolkits.Interop.Fx40", "NationalInstruments.RFToolkits.Interop")

    # This function helps keep a global reference to an open RFmx session on the server
    def GetGlobalInstrMX(self, resourceName, optionString):
        global instr
        if instr is not None and not instr.IsDisposed:
            return instr
        else:
            instr = self.exposed_InstrMX.RFmxInstrMX(resourceName, optionString)
            return instr

    def ComplexWaveform(self, nettype, param):
        return self.exposed_NationalInstruments.ComplexWaveform[nettype](param)

    def exec(self, expression):
        exec(expression)

    def eval(self, expression):
        return eval(expression)

# start the server
if __name__ == "__main__":
    port = 18861
    print("Starting RFmxService on port " + str(port) + '.')
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RFmxService, port = port, protocol_config = {"allow_all_attrs" : True, "allow_setattr": True})
    try:
        t.start()
    except:
        pass
    t.close()
    print("RFmxService stopped.")