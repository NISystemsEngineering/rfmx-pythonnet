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

    @staticmethod
    def complex_waveform(net_type, param):
        return RFmxService.exposed_NationalInstruments.ComplexWaveform[net_type](param)
    
    @staticmethod
    def decompose_trace(trace):
        """ Convenience function that dispatches on type"""
        type_full_name = trace.GetType().FullName
        if type_full_name == 'NationalInstruments.ComplexSingle[]' or type_full_name == 'NationalInstruments.ComplexDouble[]':
            return RFmxService.decompose_complex_array(trace)
        elif 'NationalInstruments.AnalogWaveform' in type_full_name:
            return RFmxService.decompose_analog_waveform(trace)
        elif 'NationalInstruments.Spectrum' in type_full_name:
            return RFmxService.decompose_spectrum(trace)
        raise ValueError('Unknown trace type.') 
        
    @staticmethod
    def decompose_complex_array(complex_array) -> list:
        """ Decomposes an NI ComplexSingle[] or ComplexDouble[] into a list of complex numbers. """
        # use list comprehension instead of DecomposeArray so we don't have to identify a type
        return [complex(iq.Real, iq.Imaginary) for iq in complex_array]

    @staticmethod
    def decompose_complex_waveform(complex_waveform) -> tuple:
        """ Decomposes an NI ComplexWaveform into a tuple of t0, dt, and y values. """
        t0 = complex_waveform.PrecisionTiming.TimeOffset.TotalSeconds
        dt = complex_waveform.PrecisionTiming.SampleInterval.TotalSeconds
        y = RFmxService.decompose_complex_array(complex_waveform.GetRawData())
        return t0, dt, y

    @staticmethod
    def decompose_analog_waveform(analog_waveform) -> tuple:
        """ Decomposes an NI AnalogWaveform into a tuple of t0, dt, and y values. """
        t0 = analog_waveform.PrecisionTiming.TimeOffset.TotalSeconds
        dt = analog_waveform.PrecisionTiming.SampleInterval.TotalSeconds
        y = list(analog_waveform.GetRawData())
        return t0, dt, y

    @staticmethod
    def decompose_spectrum(spectrum) -> tuple:
        """ Decomposes an NI Spectrum into a tuple of f0, dt, and y values. """
        f0 = spectrum.StartFrequency
        df = spectrum.FrequencyIncrement
        y = list(spectrum.GetData())
        return f0, df, y

    @staticmethod
    def exec(expression):
        exec(expression)

    @staticmethod
    def eval(expression):
        return eval(expression)


# start the server
if __name__ == "__main__":
    port = 18861
    print("Starting RFmxService on port " + str(port) + '.')
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RFmxService, port=port, protocol_config={
        "allow_all_attrs" : True,
        "allow_setattr": True,
        "sync_request_timeout": 60,
        "allow_pickle": True
    })    
    try:
        t.start()
    except:
        pass
    t.close()
    print("RFmxService stopped.")
