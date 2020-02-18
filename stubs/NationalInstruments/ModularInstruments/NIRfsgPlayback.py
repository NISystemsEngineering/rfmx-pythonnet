# encoding: utf-8
# module NationalInstruments.ModularInstruments.NIRfsgPlayback calls itself NIRfsgPlayback
# from NationalInstruments.ModularInstruments.NIRfsgPlayback.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class NIRfsgPlayback(object):
    # no doc
    @staticmethod
    def ClearAllWaveforms(rfsgSession):
        """ ClearAllWaveforms(rfsgSession: IntPtr) -> int """
        pass

    @staticmethod
    def ClearWaveform(rfsgSession, waveformName):
        """ ClearWaveform(rfsgSession: IntPtr, waveformName: str) -> int """
        pass

    @staticmethod
    def DownloadUserWaveform(rfsgSession, waveformName, waveform, burstPresent):
        """
        DownloadUserWaveform(rfsgSession: IntPtr, waveformName: str, waveform: ComplexWaveform[ComplexSingle], burstPresent: bool) -> int
        DownloadUserWaveform(rfsgSession: IntPtr, waveformName: str, waveform: ComplexWaveform[ComplexDouble], burstPresent: bool) -> int
        """
        pass

    @staticmethod
    def GetError(errorCode, errorDescription):
        """ GetError() -> (int, int, str) """
        pass

    @staticmethod
    def ReadAndDownloadWaveformFromFile(rfsgSession, filePath, rfsgWaveformName):
        """ ReadAndDownloadWaveformFromFile(rfsgSession: IntPtr, filePath: str, rfsgWaveformName: str) -> int """
        pass

    @staticmethod
    def ReadAndDownloadWaveformsFromFile(rfsgSessions, filePath, rfsgWaveformName):
        """ ReadAndDownloadWaveformsFromFile(rfsgSessions: Array[IntPtr], filePath: str, rfsgWaveformName: str) -> int """
        pass

    @staticmethod
    def ReadBurstStartLocationsFromFile(filePath, waveformIndex, burstStartLocations):
        """ ReadBurstStartLocationsFromFile(filePath: str, waveformIndex: int, burstStartLocations: Array[int]) -> (int, Array[int]) """
        pass

    @staticmethod
    def ReadBurstStopLocationsFromFile(filePath, waveformIndex, burstStopLocations):
        """ ReadBurstStopLocationsFromFile(filePath: str, waveformIndex: int, burstStopLocations: Array[int]) -> (int, Array[int]) """
        pass

    @staticmethod
    def ReadPaprFromFile(filePath, waveformIndex, papr):
        """ ReadPaprFromFile(filePath: str, waveformIndex: int) -> (int, float) """
        pass

    @staticmethod
    def ReadPeakPowerAdjustmentFromFile(filePath, waveformIndex, peakPowerAdjustment):
        """ ReadPeakPowerAdjustmentFromFile(filePath: str, waveformIndex: int) -> (int, float) """
        pass

    @staticmethod
    def ReadRFBlankingEnabledFromFile(filePath, waveformIndex, rfBlankingEnabled):
        """ ReadRFBlankingEnabledFromFile(filePath: str, waveformIndex: int) -> (int, bool) """
        pass

    @staticmethod
    def ReadRFBlankingMarkerLocationsFromFile(filePath, waveformIndex, markerLocations):
        """ ReadRFBlankingMarkerLocationsFromFile(filePath: str, waveformIndex: int, markerLocations: Array[int]) -> (int, Array[int]) """
        pass

    @staticmethod
    def ReadRFBlankingMarkerSourceFromFile(filePath, waveformIndex, markerSource):
        """ ReadRFBlankingMarkerSourceFromFile(filePath: str, waveformIndex: int) -> (int, str) """
        pass

    @staticmethod
    def ReadRuntimeScalingFromFile(filePath, waveformIndex, runtimeScaling):
        """ ReadRuntimeScalingFromFile(filePath: str, waveformIndex: int) -> (int, float) """
        pass

    @staticmethod
    def ReadSampleRateFromFile(filePath, waveformIndex, sampleRate):
        """ ReadSampleRateFromFile(filePath: str, waveformIndex: int) -> (int, float) """
        pass

    @staticmethod
    def ReadSignalBandwidthFromFile(filePath, waveformIndex, signalBandwidth):
        """ ReadSignalBandwidthFromFile(filePath: str, waveformIndex: int) -> (int, float) """
        pass

    @staticmethod
    def ReadWaveformFileVersionFromFile(filePath, waveformFileVersion):
        """ ReadWaveformFileVersionFromFile(filePath: str) -> (int, str) """
        pass

    @staticmethod
    def ReadWaveformFromFileByIndexComplex(filePath, waveformIndex, outputWaveform):
        """
        ReadWaveformFromFileByIndexComplex(filePath: str, waveformIndex: int, outputWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle])
        ReadWaveformFromFileByIndexComplex(filePath: str, waveformIndex: int, outputWaveform: ComplexWaveform[ComplexDouble]) -> (int, ComplexWaveform[ComplexDouble])
        """
        pass

    @staticmethod
    def ReadWaveformFromFileComplex(filePath, outputWaveform):
        """
        ReadWaveformFromFileComplex(filePath: str, outputWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle])
        ReadWaveformFromFileComplex(filePath: str, outputWaveform: ComplexWaveform[ComplexDouble]) -> (int, ComplexWaveform[ComplexDouble])
        """
        pass

    @staticmethod
    def ReadWaveformsFromFileComplex(filePath, numberOfWaveforms, outputWaveforms):
        """
        ReadWaveformsFromFileComplex(filePath: str, numberOfWaveforms: int, outputWaveforms: Array[ComplexWaveform[ComplexSingle]]) -> (int, Array[ComplexWaveform[ComplexSingle]])
        ReadWaveformsFromFileComplex(filePath: str, numberOfWaveforms: int, outputWaveforms: Array[ComplexWaveform[ComplexDouble]]) -> (int, Array[ComplexWaveform[ComplexDouble]])
        """
        pass

    @staticmethod
    def ReadWaveformSizeFromFile(filePath, waveformIndex, waveformSize):
        """ ReadWaveformSizeFromFile(filePath: str, waveformIndex: int) -> (int, int) """
        pass

    @staticmethod
    def RetrieveAutomaticSGSASharedLO(rfsgSession, channelName, automaticSGSASharedLO):
        """ RetrieveAutomaticSGSASharedLO(rfsgSession: IntPtr, channelName: str) -> (int, RfsgPlaybackAutomaticSGSASharedLO) """
        pass

    @staticmethod
    def RetrieveDownloadedWaveformNames(rfsgSession, waveformNames):
        """ RetrieveDownloadedWaveformNames(rfsgSession: IntPtr) -> (int, Array[str]) """
        pass

    @staticmethod
    def RetrieveWaveformBurstStartLocations(rfsgSession, waveformName, burstStartLocations):
        """ RetrieveWaveformBurstStartLocations(rfsgSession: IntPtr, waveformName: str, burstStartLocations: Array[int]) -> (int, Array[int]) """
        pass

    @staticmethod
    def RetrieveWaveformBurstStopLocations(rfsgSession, waveformName, burstStopLocations):
        """ RetrieveWaveformBurstStopLocations(rfsgSession: IntPtr, waveformName: str, burstStopLocations: Array[int]) -> (int, Array[int]) """
        pass

    @staticmethod
    def RetrieveWaveformFileVersion(rfsgSession, waveformName, waveformFileVersion):
        """ RetrieveWaveformFileVersion(rfsgSession: IntPtr, waveformName: str) -> (int, str) """
        pass

    @staticmethod
    def RetrieveWaveformLOOffsetMode(rfsgSession, waveformName, value):
        """ RetrieveWaveformLOOffsetMode(rfsgSession: IntPtr, waveformName: str) -> (int, NIRfsgPlaybackLOOffsetMode) """
        pass

    @staticmethod
    def RetrieveWaveformPapr(rfsgSession, waveformName, papr):
        """ RetrieveWaveformPapr(rfsgSession: IntPtr, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def RetrieveWaveformPeakPowerAdjustment(rfsgSession, waveformName, peakPowerAdjustment):
        """ RetrieveWaveformPeakPowerAdjustment(rfsgSession: IntPtr, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def RetrieveWaveformRFBlankingEnabled(rfsgSession, waveformName, rfBlankingEnabled):
        """ RetrieveWaveformRFBlankingEnabled(rfsgSession: IntPtr, waveformName: str) -> (int, bool) """
        pass

    @staticmethod
    def RetrieveWaveformRFBlankingMarkerLocations(rfsgSession, waveformName, markerLocations):
        """ RetrieveWaveformRFBlankingMarkerLocations(rfsgSession: IntPtr, waveformName: str, markerLocations: Array[int]) -> (int, Array[int]) """
        pass

    @staticmethod
    def RetrieveWaveformRFBlankingMarkerSource(rfsgSession, waveformName, markerSource):
        """ RetrieveWaveformRFBlankingMarkerSource(rfsgSession: IntPtr, waveformName: str) -> (int, str) """
        pass

    @staticmethod
    def RetrieveWaveformRuntimeScaling(rfsgSession, waveformName, runtimeScaling):
        """ RetrieveWaveformRuntimeScaling(rfsgSession: IntPtr, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def RetrieveWaveformSampleRate(rfsgSession, waveformName, sampleRate):
        """ RetrieveWaveformSampleRate(rfsgSession: IntPtr, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def RetrieveWaveformSignalBandwidth(rfsgSession, waveformName, signalBandwidth):
        """ RetrieveWaveformSignalBandwidth(rfsgSession: IntPtr, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def RetrieveWaveformSize(rfsgSession, waveformName, waveformSize):
        """ RetrieveWaveformSize(rfsgSession: IntPtr, waveformName: str) -> (int, int) """
        pass

    @staticmethod
    def SetScriptToGenerateMultipleRfsg(rfsgSessions, scriptText):
        """ SetScriptToGenerateMultipleRfsg(rfsgSessions: Array[IntPtr], scriptText: str) -> int """
        pass

    @staticmethod
    def SetScriptToGenerateSingleRfsg(rfsgSession, scriptText):
        """ SetScriptToGenerateSingleRfsg(rfsgSession: IntPtr, scriptText: str) -> int """
        pass

    @staticmethod
    def StoreAutomaticSGSASharedLO(rfsgSession, channelName, automaticSGSASharedLO):
        """ StoreAutomaticSGSASharedLO(rfsgSession: IntPtr, channelName: str, automaticSGSASharedLO: RfsgPlaybackAutomaticSGSASharedLO) -> int """
        pass

    @staticmethod
    def StoreWaveformBurstStartLocations(rfsgSession, waveformName, burstStartLocations):
        """ StoreWaveformBurstStartLocations(rfsgSession: IntPtr, waveformName: str, burstStartLocations: Array[int]) -> int """
        pass

    @staticmethod
    def StoreWaveformBurstStopLocations(rfsgSession, waveformName, burstStopLocations):
        """ StoreWaveformBurstStopLocations(rfsgSession: IntPtr, waveformName: str, burstStopLocations: Array[int]) -> int """
        pass

    @staticmethod
    def StoreWaveformLOOffsetMode(rfsgSession, waveformName, value):
        """ StoreWaveformLOOffsetMode(rfsgSession: IntPtr, waveformName: str, value: NIRfsgPlaybackLOOffsetMode) -> int """
        pass

    @staticmethod
    def StoreWaveformPapr(rfsgSession, waveformName, papr):
        """ StoreWaveformPapr(rfsgSession: IntPtr, waveformName: str, papr: float) -> int """
        pass

    @staticmethod
    def StoreWaveformPeakPowerAdjustment(rfsgSession, waveformName, peakPowerAdjustment):
        """ StoreWaveformPeakPowerAdjustment(rfsgSession: IntPtr, waveformName: str, peakPowerAdjustment: float) -> int """
        pass

    @staticmethod
    def StoreWaveformRFBlankingEnabled(rfsgSession, waveformName, rfBlankingEnabled):
        """ StoreWaveformRFBlankingEnabled(rfsgSession: IntPtr, waveformName: str, rfBlankingEnabled: bool) -> int """
        pass

    @staticmethod
    def StoreWaveformRFBlankingMarkerLocations(rfsgSession, waveformName, markerLocations):
        """ StoreWaveformRFBlankingMarkerLocations(rfsgSession: IntPtr, waveformName: str, markerLocations: Array[int]) -> int """
        pass

    @staticmethod
    def StoreWaveformRFBlankingMarkerSource(rfsgSession, waveformName, markerSource):
        """ StoreWaveformRFBlankingMarkerSource(rfsgSession: IntPtr, waveformName: str, markerSource: str) -> int """
        pass

    @staticmethod
    def StoreWaveformRuntimeScaling(rfsgSession, waveformName, runtimeScaling):
        """ StoreWaveformRuntimeScaling(rfsgSession: IntPtr, waveformName: str, runtimeScaling: float) -> int """
        pass

    @staticmethod
    def StoreWaveformSampleRate(rfsgSession, waveformName, sampleRate):
        """ StoreWaveformSampleRate(rfsgSession: IntPtr, waveformName: str, sampleRate: float) -> int """
        pass

    @staticmethod
    def StoreWaveformSignalBandwidth(rfsgSession, waveformName, signalBandwidth):
        """ StoreWaveformSignalBandwidth(rfsgSession: IntPtr, waveformName: str, signalBandwidth: float) -> int """
        pass

    @staticmethod
    def StoreWaveformSize(rfsgSession, waveformName, waveformSize):
        """ StoreWaveformSize(rfsgSession: IntPtr, waveformName: str, waveformSize: int) -> int """
        pass

    __all__ = [
        'ClearAllWaveforms',
        'ClearWaveform',
        'DownloadUserWaveform',
        'GetError',
        'ReadAndDownloadWaveformFromFile',
        'ReadAndDownloadWaveformsFromFile',
        'ReadBurstStartLocationsFromFile',
        'ReadBurstStopLocationsFromFile',
        'ReadPaprFromFile',
        'ReadPeakPowerAdjustmentFromFile',
        'ReadRFBlankingEnabledFromFile',
        'ReadRFBlankingMarkerLocationsFromFile',
        'ReadRFBlankingMarkerSourceFromFile',
        'ReadRuntimeScalingFromFile',
        'ReadSampleRateFromFile',
        'ReadSignalBandwidthFromFile',
        'ReadWaveformFileVersionFromFile',
        'ReadWaveformFromFileByIndexComplex',
        'ReadWaveformFromFileComplex',
        'ReadWaveformsFromFileComplex',
        'ReadWaveformSizeFromFile',
        'RetrieveAutomaticSGSASharedLO',
        'RetrieveDownloadedWaveformNames',
        'RetrieveWaveformBurstStartLocations',
        'RetrieveWaveformBurstStopLocations',
        'RetrieveWaveformFileVersion',
        'RetrieveWaveformLOOffsetMode',
        'RetrieveWaveformPapr',
        'RetrieveWaveformPeakPowerAdjustment',
        'RetrieveWaveformRFBlankingEnabled',
        'RetrieveWaveformRFBlankingMarkerLocations',
        'RetrieveWaveformRFBlankingMarkerSource',
        'RetrieveWaveformRuntimeScaling',
        'RetrieveWaveformSampleRate',
        'RetrieveWaveformSignalBandwidth',
        'RetrieveWaveformSize',
        'SetScriptToGenerateMultipleRfsg',
        'SetScriptToGenerateSingleRfsg',
        'StoreAutomaticSGSASharedLO',
        'StoreWaveformBurstStartLocations',
        'StoreWaveformBurstStopLocations',
        'StoreWaveformLOOffsetMode',
        'StoreWaveformPapr',
        'StoreWaveformPeakPowerAdjustment',
        'StoreWaveformRFBlankingEnabled',
        'StoreWaveformRFBlankingMarkerLocations',
        'StoreWaveformRFBlankingMarkerSource',
        'StoreWaveformRuntimeScaling',
        'StoreWaveformSampleRate',
        'StoreWaveformSignalBandwidth',
        'StoreWaveformSize',
    ]


class NIRfsgPlaybackLOOffsetMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum NIRfsgPlaybackLOOffsetMode, values: Auto (0), Disabled (2), NoOffset (1) """
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

    Auto = None
    Disabled = None
    NoOffset = None
    value__ = None


class RfsgPlaybackAutomaticSGSASharedLO(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgPlaybackAutomaticSGSASharedLO, values: Disabled (0), Enabled (1) """
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

    Disabled = None
    Enabled = None
    value__ = None


class RfsgPlaybackConstants(object):
    # no doc
    Marker0 = 'marker0'
    Marker1 = 'marker1'
    Marker2 = 'marker2'
    Marker3 = 'marker3'
    __all__ = [
        'Marker0',
        'Marker1',
        'Marker2',
        'Marker3',
    ]


