# encoding: utf-8
# module NationalInstruments.RFmx.WC.NR calls itself NR
# from NationalInstruments.RFmx.WC.NR.Fx40, Version=20.0.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RFmxWCNR(object):
    # no doc
    @staticmethod
    def CreateAndDownloadWaveformComplexSingle(rfsgSessionHandle, configurationName, waveformName):
        """ CreateAndDownloadWaveformComplexSingle(rfsgSessionHandle: IntPtr, configurationName: str, waveformName: str) -> int """
        pass

    @staticmethod
    def CreateAndSaveWaveformToFileComplexSingle(rfsgSessionHandle, configurationName, waveformFilePath, runtimeScaling, description):
        """ CreateAndSaveWaveformToFileComplexSingle(rfsgSessionHandle: IntPtr, configurationName: str, waveformFilePath: str, runtimeScaling: float, description: str) -> int """
        pass

    @staticmethod
    def CreateWaveformComplexSingle(rfsgSessionHandle, configurationName):
        """ CreateWaveformComplexSingle(rfsgSessionHandle: IntPtr, configurationName: str) -> int """
        pass

    @staticmethod
    def DeleteWaveformConfiguration(rfsgSessionHandle, configurationName):
        """ DeleteWaveformConfiguration(rfsgSessionHandle: IntPtr, configurationName: str) -> int """
        pass

    @staticmethod
    def GetPhaseCompensationEnabled(rfsgSessionHandle, configurationName, phaseCompensationEnabled):
        """ GetPhaseCompensationEnabled(rfsgSessionHandle: IntPtr, configurationName: str) -> (int, RFmxWCNRPhaseCompensationEnabled) """
        pass

    @staticmethod
    def GetPhaseCompensationFrequency(rfsgSessionHandle, configurationName, phaseCompensationFrequency):
        """ GetPhaseCompensationFrequency(rfsgSessionHandle: IntPtr, configurationName: str) -> (int, float) """
        pass

    @staticmethod
    def GetWaveformBurstLocations(rfsgSessionHandle, configurationName, burstStartLocations, burstStopLocations):
        """ GetWaveformBurstLocations(rfsgSessionHandle: IntPtr, configurationName: str, burstStartLocations: Array[int], burstStopLocations: Array[int]) -> (int, Array[int], Array[int]) """
        pass

    @staticmethod
    def GetWaveformComplex(rfsgSessionHandle, configurationName, outputWaveform):
        """ GetWaveformComplex(rfsgSessionHandle: IntPtr, configurationName: str, outputWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    @staticmethod
    def GetWaveformPapr(rfsgSessionHandle, configurationName, papr):
        """ GetWaveformPapr(rfsgSessionHandle: IntPtr, configurationName: str) -> (int, float) """
        pass

    @staticmethod
    def GetWaveformSignalBandwidth(rfsgSessionHandle, configurationName, signalBandWidth):
        """ GetWaveformSignalBandwidth(rfsgSessionHandle: IntPtr, configurationName: str) -> (int, float) """
        pass

    @staticmethod
    def LoadWaveformConfiguration(rfsgSessionHandle, rfwsFilePath, configurationName):
        """ LoadWaveformConfiguration(rfsgSessionHandle: IntPtr, rfwsFilePath: str, configurationName: str) -> int """
        pass

    @staticmethod
    def SetPhaseCompensationEnabled(rfsgSessionHandle, configurationName, phaseCompensationEnabled):
        """ SetPhaseCompensationEnabled(rfsgSessionHandle: IntPtr, configurationName: str, phaseCompensationEnabled: RFmxWCNRPhaseCompensationEnabled) -> int """
        pass

    @staticmethod
    def SetPhaseCompensationFrequency(rfsgSessionHandle, configurationName, phaseCompensationFrequency):
        """ SetPhaseCompensationFrequency(rfsgSessionHandle: IntPtr, configurationName: str, phaseCompensationFrequency: float) -> int """
        pass

    __all__ = [
        'CreateAndDownloadWaveformComplexSingle',
        'CreateAndSaveWaveformToFileComplexSingle',
        'CreateWaveformComplexSingle',
        'DeleteWaveformConfiguration',
        'GetPhaseCompensationEnabled',
        'GetPhaseCompensationFrequency',
        'GetWaveformBurstLocations',
        'GetWaveformComplex',
        'GetWaveformPapr',
        'GetWaveformSignalBandwidth',
        'LoadWaveformConfiguration',
        'SetPhaseCompensationEnabled',
        'SetPhaseCompensationFrequency',
    ]


class RFmxWCNRException(Exception, ISerializable, _Exception):
    """
    RFmxWCNRException()
    RFmxWCNRException(message: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class RFmxWCNRPhaseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWCNRPhaseCompensationEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    False = None
    True = None
    value__ = None


