# To use the .NET assemblies 3 things need to be done
# 1. Add the assembly reference to the clr system
# 2. Import the assembly
# 3. Expose the assembly via the RFmxService (rpyc)

import clr
import colorama
import os
import rpyc
import importlib
from sys import path

# Add search paths for .NET assemblies to system path
path.extend([
    os.environ["ProgramFiles(x86)"] + r"\National Instruments\MeasurementStudioVS2010\DotNET\Assemblies\Current",  # RFmx personalities
    os.environ["ProgramFiles"] + r"\National Instruments\RFmxWC\DotNET",  # waveform creator personalities
    os.path.abspath(__file__ + "\\..\\..\\bin")  # wrappers for wlan and rfsa/rfsg
])

# Add in all of the IVI .NET paths for finding additional assemblies
ivi_dotnet_path = os.environ["ProgramFiles"] + r"\IVI Foundation\IVI\Microsoft.NET\Framework64"
for x in os.walk(ivi_dotnet_path):
    path.append(x[0])

# Prepare terminal for colored printing
colorama.init()


# This function allows for dynamic importation of modules since some modules may not be installed
def import_dotnet_submodule(assembly_name, namespace):
    from System.IO import FileNotFoundException
    submodule = None
    try:
        clr.AddReference(assembly_name)
        __import__(namespace)
        submodule = importlib.import_module(namespace)
        print(colorama.Fore.GREEN + namespace + " imported successfully from " + assembly_name + '.' + colorama.Fore.RESET)
    except FileNotFoundException:
        print(colorama.Fore.YELLOW + assembly_name + " was not found." + colorama.Fore.RESET)
    except Exception as e:
        print(colorama.Fore.RED + "An exception occured loading " + namespace + " from " + assembly_name + ". Module was not loaded.")
        print(e)
        print(colorama.Fore.RESET)
    return submodule


class RFmxService(rpyc.Service):
    exposed_clr = clr

    # Import common modules
    exposed_System = import_dotnet_submodule("System", "System")
    exposed_NationalInstruments = import_dotnet_submodule("NationalInstruments.Common", "NationalInstruments")
    exposed_ModularInstruments = import_dotnet_submodule("NationalInstruments.ModularInstruments.Common", "NationalInstruments.ModularInstruments")

    # Import RFSG generation modules
    exposed_NIRfsg = import_dotnet_submodule("NationalInstruments.ModularInstruments.NIRfsg.Fx40", "NationalInstruments.ModularInstruments.NIRfsg")
    exposed_NIRfsgPlayback = import_dotnet_submodule("NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40", "NationalInstruments.ModularInstruments.NIRfsgPlayback")
    exposed_RFmxWCNR = import_dotnet_submodule("NationalInstruments.RFmx.WC.NR.Fx40", "NationalInstruments.RFmx.WC.NR")

    # Import RFSA acquisition modules
    exposed_NIRfsa = import_dotnet_submodule("NationalInstruments.ModularInstruments.NIRfsa.Fx40", "NationalInstruments.ModularInstruments.NIRfsa")

    # Import RFmx measurement modules
    exposed_InstrMX = import_dotnet_submodule("NationalInstruments.RFmx.InstrMX.Fx40", "NationalInstruments.RFmx.InstrMX")
    exposed_SpecAnMX = import_dotnet_submodule("NationalInstruments.RFmx.SpecAnMX.Fx40", "NationalInstruments.RFmx.SpecAnMX")
    exposed_LteMX = import_dotnet_submodule("NationalInstruments.RFmx.LteMX.Fx40", "NationalInstruments.RFmx.LteMX")
    exposed_NRMX = import_dotnet_submodule("NationalInstruments.RFmx.NRMX.Fx40", "NationalInstruments.RFmx.NRMX")
    exposed_WlanMX = import_dotnet_submodule("NationalInstruments.RFmx.WlanMX.Fx40", "NationalInstruments.RFmx.WlanMX")

    # Import measurement toolkit modules
    exposed_ModularInstrumentsInterop = import_dotnet_submodule("NationalInstruments.ModularInstruments.Interop.Fx40", "NationalInstruments.ModularInstruments.Interop")
    exposed_WlanTK = import_dotnet_submodule("NationalInstruments.RFToolkits.Interop.Fx40", "NationalInstruments.RFToolkits.Interop")

    def complex_waveform(self, net_type, param):
        return self.exposed_NationalInstruments.ComplexWaveform[net_type](param)

    def exec(self, expression):
        exec(expression)

    def eval(self, expression):
        return eval(expression)


# start the server
if __name__ == "__main__":
    port = 18861
    print("Starting RFmxService on port " + str(port) + '.')
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RFmxService, port=port, protocol_config={"allow_all_attrs" : True, "allow_setattr": True})
    try:
        t.start()
    except:
        pass
    t.close()
    print("RFmxService stopped.")
