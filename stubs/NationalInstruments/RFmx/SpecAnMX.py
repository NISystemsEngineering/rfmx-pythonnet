# encoding: utf-8
# module NationalInstruments.RFmx.SpecAnMX calls itself SpecAnMX
# from NationalInstruments.RFmx.SpecAnMX.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RFmxSpecAnMX(object, ISignalConfiguration, IDisposable):
    # no doc
    def AbortMeasurements(self, selectorString):
        """ AbortMeasurements(self: RFmxSpecAnMX, selectorString: str) -> int """
        pass

    def AnalyzeIQ(self, selectorString, resultName, iq, reset, averagingDone):
        """ AnalyzeIQ(self: RFmxSpecAnMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool) -> (int, bool) """
        pass

    def AnalyzeIQ1Waveform(self, selectorString, resultName, iq, reset, reserved):
        """ AnalyzeIQ1Waveform(self: RFmxSpecAnMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool, reserved: Int64) -> int """
        pass

    def AnalyzeSpectrum(self, selectorString, resultName, spectrum, reset, averagingDone):
        """ AnalyzeSpectrum(self: RFmxSpecAnMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool) -> (int, bool) """
        pass

    def AnalyzeSpectrum1Waveform(self, selectorString, resultName, spectrum, reset, reserved):
        """ AnalyzeSpectrum1Waveform(self: RFmxSpecAnMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool, reserved: Int64) -> int """
        pass

    def AutoLevel(self, selectorString, bandwidth, measurementInterval, referenceLevel):
        """ AutoLevel(self: RFmxSpecAnMX, selectorString: str, bandwidth: float, measurementInterval: float) -> (int, float) """
        pass

    @staticmethod
    def BuildCarrierString(resultName, carrierNumber):
        """ BuildCarrierString(resultName: str, carrierNumber: int) -> str """
        pass

    @staticmethod
    def BuildCarrierString2(selectorString, carrierNumber):
        """ BuildCarrierString2(selectorString: str, carrierNumber: int) -> str """
        pass

    @staticmethod
    def BuildHarmonicString(resultName, harmonicNumber):
        """ BuildHarmonicString(resultName: str, harmonicNumber: int) -> str """
        pass

    @staticmethod
    def BuildHarmonicString2(selectorString, harmonicNumber):
        """ BuildHarmonicString2(selectorString: str, harmonicNumber: int) -> str """
        pass

    @staticmethod
    def BuildIntermodString(selectorString, intermodNumber):
        """ BuildIntermodString(selectorString: str, intermodNumber: int) -> str """
        pass

    @staticmethod
    def BuildMarkerString(resultName, markerNumber):
        """ BuildMarkerString(resultName: str, markerNumber: int) -> str """
        pass

    @staticmethod
    def BuildMarkerString2(selectorString, markerNumber):
        """ BuildMarkerString2(selectorString: str, markerNumber: int) -> str """
        pass

    @staticmethod
    def BuildOffsetString(resultName, offsetNumber):
        """ BuildOffsetString(resultName: str, offsetNumber: int) -> str """
        pass

    @staticmethod
    def BuildOffsetString2(selectorString, offsetNumber):
        """ BuildOffsetString2(selectorString: str, offsetNumber: int) -> str """
        pass

    @staticmethod
    def BuildRangeSpurString(resultName, rangeNumber, spurNumber):
        """ BuildRangeSpurString(resultName: str, rangeNumber: int, spurNumber: int) -> str """
        pass

    @staticmethod
    def BuildRangeString(resultName, rangeNumber):
        """ BuildRangeString(resultName: str, rangeNumber: int) -> str """
        pass

    @staticmethod
    def BuildRangeString2(selectorString, rangeNumber):
        """ BuildRangeString2(selectorString: str, rangeNumber: int) -> str """
        pass

    @staticmethod
    def BuildResultString(resultName):
        """ BuildResultString(resultName: str) -> str """
        pass

    @staticmethod
    def BuildSegmentString(selectorString, segmentNumber):
        """ BuildSegmentString(selectorString: str, segmentNumber: int) -> str """
        pass

    @staticmethod
    def BuildSpurString2(selectorString, spurNumber):
        """ BuildSpurString2(selectorString: str, spurNumber: int) -> str """
        pass

    def CacheResult(self, selectorString, selectorStringOut):
        """ CacheResult(self: RFmxSpecAnMX, selectorString: str) -> (int, str) """
        pass

    def CheckMeasurementStatus(self, selectorString, done):
        """ CheckMeasurementStatus(self: RFmxSpecAnMX, selectorString: str) -> (int, bool) """
        pass

    def ClearAllNamedResults(self, selectorString):
        """ ClearAllNamedResults(self: RFmxSpecAnMX, selectorString: str) -> int """
        pass

    def ClearNamedResult(self, selectorString):
        """ ClearNamedResult(self: RFmxSpecAnMX, selectorString: str) -> int """
        pass

    def CloneSignalConfiguration(self, newSignalName, signalConfiguration):
        """ CloneSignalConfiguration(self: RFmxSpecAnMX, newSignalName: str) -> (int, RFmxSpecAnMX) """
        pass

    def Commit(self, selectorString):
        """ Commit(self: RFmxSpecAnMX, selectorString: str) -> int """
        pass

    def ConfigureDigitalEdgeTrigger(self, selectorString, digitalEdgeTriggerSource, digitalEdgeTriggerEdge, triggerDelay, enableTrigger):
        """ ConfigureDigitalEdgeTrigger(self: RFmxSpecAnMX, selectorString: str, digitalEdgeTriggerSource: str, digitalEdgeTriggerEdge: RFmxSpecAnMXDigitalEdgeTriggerEdge, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def ConfigureExternalAttenuation(self, selectorString, externalAttenuation):
        """ ConfigureExternalAttenuation(self: RFmxSpecAnMX, selectorString: str, externalAttenuation: float) -> int """
        pass

    def ConfigureFrequency(self, selectorString, centerFrequency):
        """ ConfigureFrequency(self: RFmxSpecAnMX, selectorString: str, centerFrequency: float) -> int """
        pass

    def ConfigureIQPowerEdgeTrigger(self, selectorString, iqPowerEdgeTriggerSource, iqPowerEdgeTriggerLevel, iqPowerEdgeSlope, triggerDelay, minimumQuietTimeMode, minimumQuietTimeDuration, enableTrigger):
        """ ConfigureIQPowerEdgeTrigger(self: RFmxSpecAnMX, selectorString: str, iqPowerEdgeTriggerSource: str, iqPowerEdgeTriggerLevel: float, iqPowerEdgeSlope: RFmxSpecAnMXIQPowerEdgeTriggerSlope, triggerDelay: float, minimumQuietTimeMode: RFmxSpecAnMXTriggerMinimumQuietTimeMode, minimumQuietTimeDuration: float, enableTrigger: bool) -> int """
        pass

    def ConfigureReferenceLevel(self, selectorString, referenceLevel):
        """ ConfigureReferenceLevel(self: RFmxSpecAnMX, selectorString: str, referenceLevel: float) -> int """
        pass

    def ConfigureReferenceLevelUnits(self, selectorString, referenceLevelUnits):
        """ ConfigureReferenceLevelUnits(self: RFmxSpecAnMX, selectorString: str, referenceLevelUnits: RFmxSpecAnMXReferenceLevelUnits) -> int """
        pass

    def ConfigureRF(self, selectorString, centerFrequency, referenceLevel, externalAttenuation):
        """ ConfigureRF(self: RFmxSpecAnMX, selectorString: str, centerFrequency: float, referenceLevel: float, externalAttenuation: float) -> int """
        pass

    def ConfigureSoftwareEdgeTrigger(self, selectorString, triggerDelay, enableTrigger):
        """ ConfigureSoftwareEdgeTrigger(self: RFmxSpecAnMX, selectorString: str, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def DeleteSignalConfiguration(self):
        """ DeleteSignalConfiguration(self: RFmxSpecAnMX) -> int """
        pass

    def DisableTrigger(self, selectorString):
        """ DisableTrigger(self: RFmxSpecAnMX, selectorString: str) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: RFmxSpecAnMX) """
        pass

    def GetAllNamedResultNames(self, selectorString, resultNames, defaultResultExists):
        """ GetAllNamedResultNames(self: RFmxSpecAnMX, selectorString: str) -> (int, Array[str], bool) """
        pass

    def GetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ GetAttributeBool(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int) -> (int, bool) """
        pass

    def GetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ GetAttributeDouble(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int) -> (int, float) """
        pass

    def GetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ GetAttributeInt(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int) -> (int, int) """
        pass

    def GetAttributeSingleArray(self, selectorString, attributeIdentifier, value):
        """ GetAttributeSingleArray(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetAttributeString(self, selectorString, attributeIdentifier, value):
        """ GetAttributeString(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int) -> (int, str) """
        pass

    def GetAutoLevelInitialReferenceLevel(self, selectorString, value):
        """ GetAutoLevelInitialReferenceLevel(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetCenterFrequency(self, selectorString, value):
        """ GetCenterFrequency(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ GetDigitalEdgeTriggerEdge(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXDigitalEdgeTriggerEdge) """
        pass

    def GetDigitalEdgeTriggerSource(self, selectorString, value):
        """ GetDigitalEdgeTriggerSource(self: RFmxSpecAnMX, selectorString: str) -> (int, str) """
        pass

    def GetError(self, errorCode, errorDescription):
        """ GetError(self: RFmxSpecAnMX) -> (int, int, str) """
        pass

    def GetErrorString(self, errorCode, errorDescription):
        """ GetErrorString(self: RFmxSpecAnMX, errorCode: int) -> (int, str) """
        pass

    def GetExternalAttenuation(self, selectorString, value):
        """ GetExternalAttenuation(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevel(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevelType(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXIQPowerEdgeTriggerLevelType) """
        pass

    def GetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSlope(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXIQPowerEdgeTriggerSlope) """
        pass

    def GetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSource(self: RFmxSpecAnMX, selectorString: str) -> (int, str) """
        pass

    def GetLimitedConfigurationChange(self, selectorString, value):
        """ GetLimitedConfigurationChange(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXLimitedConfigurationChange) """
        pass

    def GetReferenceLevel(self, selectorString, value):
        """ GetReferenceLevel(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetReferenceLevelHeadroom(self, selectorString, value):
        """ GetReferenceLevelHeadroom(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetReferenceLevelUnits(self, selectorString, value):
        """ GetReferenceLevelUnits(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXReferenceLevelUnits) """
        pass

    def GetResultFetchTimeout(self, selectorString, value):
        """ GetResultFetchTimeout(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetSelectedPorts(self, selectorString, value):
        """ GetSelectedPorts(self: RFmxSpecAnMX, selectorString: str) -> (int, str) """
        pass

    def GetTriggerDelay(self, selectorString, value):
        """ GetTriggerDelay(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeDuration(self: RFmxSpecAnMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeMode(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXTriggerMinimumQuietTimeMode) """
        pass

    def GetTriggerType(self, selectorString, value):
        """ GetTriggerType(self: RFmxSpecAnMX, selectorString: str) -> (int, RFmxSpecAnMXTriggerType) """
        pass

    def GetWarning(self, warningCode, warningDescription):
        """ GetWarning(self: RFmxSpecAnMX) -> (int, int, str) """
        pass

    def Initiate(self, selectorString, resultName):
        """ Initiate(self: RFmxSpecAnMX, selectorString: str, resultName: str) -> int """
        pass

    def ResetAttribute(self, selectorString, attributeId):
        """ ResetAttribute(self: RFmxSpecAnMX, selectorString: str, attributeId: RFmxSpecAnMXPropertyId) -> int """
        pass

    def ResetToDefault(self, selectorString):
        """ ResetToDefault(self: RFmxSpecAnMX, selectorString: str) -> int """
        pass

    def SelectMeasurements(self, selectorString, measurement, enableAllTraces):
        """ SelectMeasurements(self: RFmxSpecAnMX, selectorString: str, measurement: RFmxSpecAnMXMeasurementTypes, enableAllTraces: bool) -> int """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RFmxSpecAnMX) -> int """
        pass

    def SetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ SetAttributeBool(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int, value: bool) -> int """
        pass

    def SetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ SetAttributeDouble(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int, value: float) -> int """
        pass

    def SetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ SetAttributeInt(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int, value: int) -> int """
        pass

    def SetAttributeString(self, selectorString, attributeIdentifier, value):
        """ SetAttributeString(self: RFmxSpecAnMX, selectorString: str, attributeIdentifier: int, value: str) -> int """
        pass

    def SetAutoLevelInitialReferenceLevel(self, selectorString, value):
        """ SetAutoLevelInitialReferenceLevel(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetCenterFrequency(self, selectorString, value):
        """ SetCenterFrequency(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ SetDigitalEdgeTriggerEdge(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXDigitalEdgeTriggerEdge) -> int """
        pass

    def SetDigitalEdgeTriggerSource(self, selectorString, value):
        """ SetDigitalEdgeTriggerSource(self: RFmxSpecAnMX, selectorString: str, value: str) -> int """
        pass

    def SetExternalAttenuation(self, selectorString, value):
        """ SetExternalAttenuation(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevel(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevelType(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXIQPowerEdgeTriggerLevelType) -> int """
        pass

    def SetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSlope(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXIQPowerEdgeTriggerSlope) -> int """
        pass

    def SetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSource(self: RFmxSpecAnMX, selectorString: str, value: str) -> int """
        pass

    def SetLimitedConfigurationChange(self, selectorString, value):
        """ SetLimitedConfigurationChange(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXLimitedConfigurationChange) -> int """
        pass

    def SetReferenceLevel(self, selectorString, value):
        """ SetReferenceLevel(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetReferenceLevelHeadroom(self, selectorString, value):
        """ SetReferenceLevelHeadroom(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetReferenceLevelUnits(self, selectorString, value):
        """ SetReferenceLevelUnits(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXReferenceLevelUnits) -> int """
        pass

    def SetResultFetchTimeout(self, selectorString, value):
        """ SetResultFetchTimeout(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetSelectedPorts(self, selectorString, value):
        """ SetSelectedPorts(self: RFmxSpecAnMX, selectorString: str, value: str) -> int """
        pass

    def SetTriggerDelay(self, selectorString, value):
        """ SetTriggerDelay(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeDuration(self: RFmxSpecAnMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeMode(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXTriggerMinimumQuietTimeMode) -> int """
        pass

    def SetTriggerType(self, selectorString, value):
        """ SetTriggerType(self: RFmxSpecAnMX, selectorString: str, value: RFmxSpecAnMXTriggerType) -> int """
        pass

    def WaitForMeasurementComplete(self, selectorString, timeout):
        """ WaitForMeasurementComplete(self: RFmxSpecAnMX, selectorString: str, timeout: float) -> int """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Acp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Acp(self: RFmxSpecAnMX) -> RFmxSpecAnMXAcp

"""

    Ampm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ampm(self: RFmxSpecAnMX) -> RFmxSpecAnMXAmpm

"""

    Ccdf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ccdf(self: RFmxSpecAnMX) -> RFmxSpecAnMXCcdf

"""

    Chp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chp(self: RFmxSpecAnMX) -> RFmxSpecAnMXChp

"""

    Dpd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dpd(self: RFmxSpecAnMX) -> RFmxSpecAnMXDpd

"""

    Fcnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fcnt(self: RFmxSpecAnMX) -> RFmxSpecAnMXFcnt

"""

    Harm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Harm(self: RFmxSpecAnMX) -> RFmxSpecAnMXHarm

"""

    IM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IM(self: RFmxSpecAnMX) -> RFmxSpecAnMXIM

"""

    IQ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQ(self: RFmxSpecAnMX) -> RFmxSpecAnMXIQ

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: RFmxSpecAnMX) -> bool

"""

    Marker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Marker(self: RFmxSpecAnMX) -> RFmxSpecAnMXMarker

"""

    NF = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NF(self: RFmxSpecAnMX) -> RFmxSpecAnMXNF

"""

    Obw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Obw(self: RFmxSpecAnMX) -> RFmxSpecAnMXObw

"""

    Pavt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pavt(self: RFmxSpecAnMX) -> RFmxSpecAnMXPavt

"""

    PhaseNoise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseNoise(self: RFmxSpecAnMX) -> RFmxSpecAnMXPhaseNoise

"""

    Sem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sem(self: RFmxSpecAnMX) -> RFmxSpecAnMXSem

"""

    SignalConfigurationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationName(self: RFmxSpecAnMX) -> str

"""

    SignalConfigurationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationType(self: RFmxSpecAnMX) -> Type

"""

    Spectrum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spectrum(self: RFmxSpecAnMX) -> RFmxSpecAnMXSpectrum

"""

    Spur = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spur(self: RFmxSpecAnMX) -> RFmxSpecAnMXSpur

"""

    Txp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Txp(self: RFmxSpecAnMX) -> RFmxSpecAnMXTxp

"""



class RFmxSpecAnMXSubObject(object):
    # no doc

class RFmxSpecAnMXAcp(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXAcp) -> RFmxSpecAnMXAcpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXAcp) -> RFmxSpecAnMXAcpResults

"""



class RFmxSpecAnMXAcpAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXAcpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2), Vector (5) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RFmxSpecAnMXAcpCarrierMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpCarrierMode, values: Active (1), Passive (0) """
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

    Active = None
    Passive = None
    value__ = None


class RFmxSpecAnMXAcpCarrierRrcFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpCarrierRrcFilterEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXAcpAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXAcpAveragingType) -> int """
        pass

    def ConfigureCarrierAndOffsets(self, selectorString, integrationBandwidth, numberOfOffsets, channelSpacing):
        """ ConfigureCarrierAndOffsets(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, integrationBandwidth: float, numberOfOffsets: int, channelSpacing: float) -> int """
        pass

    def ConfigureCarrierFrequency(self, selectorString, carrierFrequency):
        """ ConfigureCarrierFrequency(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, carrierFrequency: float) -> int """
        pass

    def ConfigureCarrierIntegrationBandwidth(self, selectorString, integrationBandwidth):
        """ ConfigureCarrierIntegrationBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, integrationBandwidth: float) -> int """
        pass

    def ConfigureCarrierMode(self, selectorString, carrierMode):
        """ ConfigureCarrierMode(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, carrierMode: RFmxSpecAnMXAcpCarrierMode) -> int """
        pass

    def ConfigureCarrierRrcFilter(self, selectorString, rrcFilterEnabled, rrcAlpha):
        """ ConfigureCarrierRrcFilter(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, rrcFilterEnabled: RFmxSpecAnMXAcpCarrierRrcFilterEnabled, rrcAlpha: float) -> int """
        pass

    def ConfigureFft(self, selectorString, fftWindow, fftPadding):
        """ ConfigureFft(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXAcpFftWindow, fftPadding: float) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, measurementMethod: RFmxSpecAnMXAcpMeasurementMethod) -> int """
        pass

    def ConfigureNoiseCompensationEnabled(self, selectorString, noiseCompensationEnabled):
        """ ConfigureNoiseCompensationEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, noiseCompensationEnabled: RFmxSpecAnMXAcpNoiseCompensationEnabled) -> int """
        pass

    def ConfigureNumberOfCarriers(self, selectorString, numberOfCarriers):
        """ ConfigureNumberOfCarriers(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, numberOfCarriers: int) -> int """
        pass

    def ConfigureNumberOfOffsets(self, selectorString, numberOfOffsets):
        """ ConfigureNumberOfOffsets(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, numberOfOffsets: int) -> int """
        pass

    def ConfigureOffset(self, selectorString, offsetFrequency, offsetSideband, offsetEnabled):
        """ ConfigureOffset(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, offsetFrequency: float, offsetSideband: RFmxSpecAnMXAcpOffsetSideband, offsetEnabled: RFmxSpecAnMXAcpOffsetEnabled) -> int """
        pass

    def ConfigureOffsetArray(self, selectorString, offsetFrequency, offsetSideband, offsetEnabled):
        """ ConfigureOffsetArray(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, offsetFrequency: Array[float], offsetSideband: Array[RFmxSpecAnMXAcpOffsetSideband], offsetEnabled: Array[RFmxSpecAnMXAcpOffsetEnabled]) -> int """
        pass

    def ConfigureOffsetFrequencyDefinition(self, selectorString, offsetFrequencyDefinition):
        """ ConfigureOffsetFrequencyDefinition(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, offsetFrequencyDefinition: RFmxSpecAnMXAcpOffsetFrequencyDefinition) -> int """
        pass

    def ConfigureOffsetIntegrationBandwidth(self, selectorString, integrationBandwidth):
        """ ConfigureOffsetIntegrationBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, integrationBandwidth: float) -> int """
        pass

    def ConfigureOffsetIntegrationBandwidthArray(self, selectorString, integrationBandwidth):
        """ ConfigureOffsetIntegrationBandwidthArray(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, integrationBandwidth: Array[float]) -> int """
        pass

    def ConfigureOffsetPowerReference(self, selectorString, offsetReferenceCarrier, offsetReferenceSpecific):
        """ ConfigureOffsetPowerReference(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, offsetReferenceCarrier: RFmxSpecAnMXAcpOffsetPowerReferenceCarrier, offsetReferenceSpecific: int) -> int """
        pass

    def ConfigureOffsetPowerReferenceArray(self, selectorString, offsetPowerReferenceCarrier, offsetPowerReferenceSpecific):
        """ ConfigureOffsetPowerReferenceArray(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, offsetPowerReferenceCarrier: Array[RFmxSpecAnMXAcpOffsetPowerReferenceCarrier], offsetPowerReferenceSpecific: Array[int]) -> int """
        pass

    def ConfigureOffsetRelativeAttenuation(self, selectorString, relativeAttenuation):
        """ ConfigureOffsetRelativeAttenuation(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, relativeAttenuation: float) -> int """
        pass

    def ConfigureOffsetRelativeAttenuationArray(self, selectorString, relativeAttenuation):
        """ ConfigureOffsetRelativeAttenuationArray(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, relativeAttenuation: Array[float]) -> int """
        pass

    def ConfigureOffsetRrcFilter(self, selectorString, rrcFilterEnabled, rrcAlpha):
        """ ConfigureOffsetRrcFilter(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, rrcFilterEnabled: RFmxSpecAnMXAcpOffsetRrcFilterEnabled, rrcAlpha: float) -> int """
        pass

    def ConfigureOffsetRrcFilterArray(self, selectorString, rrcFilterEnabled, rrcAlpha):
        """ ConfigureOffsetRrcFilterArray(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, rrcFilterEnabled: Array[RFmxSpecAnMXAcpOffsetRrcFilterEnabled], rrcAlpha: Array[float]) -> int """
        pass

    def ConfigurePowerUnits(self, selectorString, powerUnits):
        """ ConfigurePowerUnits(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, powerUnits: RFmxSpecAnMXAcpPowerUnits) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXAcpRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXAcpRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXAcpSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpAveragingType) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierMode(self, selectorString, value):
        """ GetCarrierMode(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpCarrierMode) """
        pass

    def GetCarrierRrcFilterAlpha(self, selectorString, value):
        """ GetCarrierRrcFilterAlpha(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRrcFilterEnabled(self, selectorString, value):
        """ GetCarrierRrcFilterEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpCarrierRrcFilterEnabled) """
        pass

    def GetFarIFOutputPowerOffset(self, selectorString, value):
        """ GetFarIFOutputPowerOffset(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftPadding(self, selectorString, value):
        """ GetFftPadding(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpFftWindow) """
        pass

    def GetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ GetIFOutputPowerOffsetAuto(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpIFOutputPowerOffsetAuto) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpMeasurementMethod) """
        pass

    def GetNearIFOutputPowerOffset(self, selectorString, value):
        """ GetNearIFOutputPowerOffset(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNoiseCompensationEnabled(self, selectorString, value):
        """ GetNoiseCompensationEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpNoiseCompensationEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfCarriers(self, selectorString, value):
        """ GetNumberOfCarriers(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfOffsets(self, selectorString, value):
        """ GetNumberOfOffsets(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetEnabled(self, selectorString, value):
        """ GetOffsetEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpOffsetEnabled) """
        pass

    def GetOffsetFrequency(self, selectorString, value):
        """ GetOffsetFrequency(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetFrequencyDefinition(self, selectorString, value):
        """ GetOffsetFrequencyDefinition(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpOffsetFrequencyDefinition) """
        pass

    def GetOffsetIntegrationBandwidth(self, selectorString, value):
        """ GetOffsetIntegrationBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetPowerReferenceCarrier(self, selectorString, value):
        """ GetOffsetPowerReferenceCarrier(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpOffsetPowerReferenceCarrier) """
        pass

    def GetOffsetPowerReferenceSpecific(self, selectorString, value):
        """ GetOffsetPowerReferenceSpecific(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetRelativeAttenuation(self, selectorString, value):
        """ GetOffsetRelativeAttenuation(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRrcFilterAlpha(self, selectorString, value):
        """ GetOffsetRrcFilterAlpha(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRrcFilterEnabled(self, selectorString, value):
        """ GetOffsetRrcFilterEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpOffsetRrcFilterEnabled) """
        pass

    def GetOffsetSideband(self, selectorString, value):
        """ GetOffsetSideband(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpOffsetSideband) """
        pass

    def GetPowerUnits(self, selectorString, value):
        """ GetPowerUnits(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpPowerUnits) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpRbwFilterBandwidthDefinition) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpRbwFilterType) """
        pass

    def GetSequentialFftSize(self, selectorString, value):
        """ GetSequentialFftSize(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAcpSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxSpecAnMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpAveragingType) -> int """
        pass

    def SetCarrierFrequency(self, selectorString, value):
        """ SetCarrierFrequency(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierIntegrationBandwidth(self, selectorString, value):
        """ SetCarrierIntegrationBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierMode(self, selectorString, value):
        """ SetCarrierMode(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpCarrierMode) -> int """
        pass

    def SetCarrierRrcFilterAlpha(self, selectorString, value):
        """ SetCarrierRrcFilterAlpha(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierRrcFilterEnabled(self, selectorString, value):
        """ SetCarrierRrcFilterEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpCarrierRrcFilterEnabled) -> int """
        pass

    def SetFarIFOutputPowerOffset(self, selectorString, value):
        """ SetFarIFOutputPowerOffset(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftPadding(self, selectorString, value):
        """ SetFftPadding(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpFftWindow) -> int """
        pass

    def SetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ SetIFOutputPowerOffsetAuto(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpIFOutputPowerOffsetAuto) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpMeasurementMethod) -> int """
        pass

    def SetNearIFOutputPowerOffset(self, selectorString, value):
        """ SetNearIFOutputPowerOffset(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNoiseCompensationEnabled(self, selectorString, value):
        """ SetNoiseCompensationEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpNoiseCompensationEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfCarriers(self, selectorString, value):
        """ SetNumberOfCarriers(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfOffsets(self, selectorString, value):
        """ SetNumberOfOffsets(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetEnabled(self, selectorString, value):
        """ SetOffsetEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpOffsetEnabled) -> int """
        pass

    def SetOffsetFrequency(self, selectorString, value):
        """ SetOffsetFrequency(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetFrequencyDefinition(self, selectorString, value):
        """ SetOffsetFrequencyDefinition(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpOffsetFrequencyDefinition) -> int """
        pass

    def SetOffsetIntegrationBandwidth(self, selectorString, value):
        """ SetOffsetIntegrationBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetPowerReferenceCarrier(self, selectorString, value):
        """ SetOffsetPowerReferenceCarrier(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpOffsetPowerReferenceCarrier) -> int """
        pass

    def SetOffsetPowerReferenceSpecific(self, selectorString, value):
        """ SetOffsetPowerReferenceSpecific(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetRelativeAttenuation(self, selectorString, value):
        """ SetOffsetRelativeAttenuation(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRrcFilterAlpha(self, selectorString, value):
        """ SetOffsetRrcFilterAlpha(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRrcFilterEnabled(self, selectorString, value):
        """ SetOffsetRrcFilterEnabled(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpOffsetRrcFilterEnabled) -> int """
        pass

    def SetOffsetSideband(self, selectorString, value):
        """ SetOffsetSideband(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpOffsetSideband) -> int """
        pass

    def SetPowerUnits(self, selectorString, value):
        """ SetPowerUnits(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpPowerUnits) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpRbwFilterBandwidthDefinition) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpRbwFilterType) -> int """
        pass

    def SetSequentialFftSize(self, selectorString, value):
        """ SetSequentialFftSize(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: RFmxSpecAnMXAcpSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxSpecAnMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXAcpFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXAcpIFOutputPowerOffsetAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpIFOutputPowerOffsetAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpMeasurementMethod, values: DynamicRange (1), Normal (0), SequentialFft (2) """
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

    DynamicRange = None
    Normal = None
    SequentialFft = None
    value__ = None


class RFmxSpecAnMXAcpNoiseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpNoiseCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpOffsetEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpOffsetEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpOffsetFrequencyDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpOffsetFrequencyDefinition, values: CarrierCenterToOffsetCenter (0), CarrierCenterToOffsetEdge (1) """
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

    CarrierCenterToOffsetCenter = None
    CarrierCenterToOffsetEdge = None
    value__ = None


class RFmxSpecAnMXAcpOffsetPowerReferenceCarrier(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpOffsetPowerReferenceCarrier, values: Closest (0), Composite (2), Highest (1), Specific (3) """
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

    Closest = None
    Composite = None
    Highest = None
    Specific = None
    value__ = None


class RFmxSpecAnMXAcpOffsetRrcFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpOffsetRrcFilterEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpOffsetSideband(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpOffsetSideband, values: Both (2), Negative (0), Positive (1) """
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

    Both = None
    Negative = None
    Positive = None
    value__ = None


class RFmxSpecAnMXAcpPowerUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpPowerUnits, values: dBm (0), dBmPerHertz (1) """
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

    dBm = None
    dBmPerHertz = None
    value__ = None


class RFmxSpecAnMXAcpRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXAcpRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinitionBinWidth (2) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinitionBinWidth = None
    value__ = None


class RFmxSpecAnMXAcpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXAcpResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAbsolutePowersTrace(self, selectorString, timeout, traceIndex, absolutePowersTrace):
        """ FetchAbsolutePowersTrace(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float, traceIndex: int, absolutePowersTrace: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchCarrierMeasurement(self, selectorString, timeout, absolutePower, totalRelativePower, carrierFrequency, integrationBandwidth):
        """ FetchCarrierMeasurement(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchFrequencyResolution(self, selectorString, timeout, frequencyResolution):
        """ FetchFrequencyResolution(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchOffsetMeasurement(self, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower):
        """ FetchOffsetMeasurement(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchOffsetMeasurementArray(self, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower):
        """ FetchOffsetMeasurementArray(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float, lowerRelativePower: Array[float], upperRelativePower: Array[float], lowerAbsolutePower: Array[float], upperAbsolutePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchRelativePowersTrace(self, selectorString, timeout, traceIndex, relativePowersTrace):
        """ FetchRelativePowersTrace(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float, traceIndex: int, relativePowersTrace: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchTotalCarrierPower(self, selectorString, timeout, totalCarrierPower):
        """ FetchTotalCarrierPower(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def GetCarrierAbsolutePower(self, selectorString, value):
        """ GetCarrierAbsolutePower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierTotalRelativePower(self, selectorString, value):
        """ GetCarrierTotalRelativePower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyResolution(self, selectorString, value):
        """ GetFrequencyResolution(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetAbsolutePower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetFrequency(self, selectorString, value):
        """ GetLowerOffsetFrequency(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetFrequencyReferenceCarrier(self, selectorString, value):
        """ GetLowerOffsetFrequencyReferenceCarrier(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, int) """
        pass

    def GetLowerOffsetIntegrationBandwidth(self, selectorString, value):
        """ GetLowerOffsetIntegrationBandwidth(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetPowerReferenceCarrier(self, selectorString, value):
        """ GetLowerOffsetPowerReferenceCarrier(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, int) """
        pass

    def GetLowerOffsetRelativePower(self, selectorString, value):
        """ GetLowerOffsetRelativePower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalCarrierPower(self, selectorString, value):
        """ GetTotalCarrierPower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetAbsolutePower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetFrequency(self, selectorString, value):
        """ GetUpperOffsetFrequency(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetFrequencyReferenceCarrier(self, selectorString, value):
        """ GetUpperOffsetFrequencyReferenceCarrier(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, int) """
        pass

    def GetUpperOffsetIntegrationBandwidth(self, selectorString, value):
        """ GetUpperOffsetIntegrationBandwidth(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetPowerReferenceCarrier(self, selectorString, value):
        """ GetUpperOffsetPowerReferenceCarrier(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, int) """
        pass

    def GetUpperOffsetRelativePower(self, selectorString, value):
        """ GetUpperOffsetRelativePower(self: RFmxSpecAnMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, carrierAbsolutePower, offsetCh0LowerRelativePower, offsetCh0UpperRelativePower, offsetCh1LowerRelativePower, offsetCh1UpperRelativePower):
        """ Read(self: RFmxSpecAnMXAcpResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass


class RFmxSpecAnMXAcpSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAcpSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpm(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXAmpm) -> RFmxSpecAnMXAmpmConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXAmpm) -> RFmxSpecAnMXAmpmResults

"""



class RFmxSpecAnMXAmpmAMToAMCurveFitType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmAMToAMCurveFitType, values: Bisquare (2), LeastAbsoluteResidual (1), LeastSquare (0) """
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

    Bisquare = None
    LeastAbsoluteResidual = None
    LeastSquare = None
    value__ = None


class RFmxSpecAnMXAmpmAMToPMCurveFitType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmAMToPMCurveFitType, values: Bisquare (2), LeastAbsoluteResidual (1), LeastSquare (0) """
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

    Bisquare = None
    LeastAbsoluteResidual = None
    LeastSquare = None
    value__ = None


class RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmCompressionPointEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmCompressionPointEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAMToAMCurveFit(self, selectorString, amToAMCurveFitOrder, amToAMCurveFitType):
        """ ConfigureAMToAMCurveFit(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, amToAMCurveFitOrder: int, amToAMCurveFitType: RFmxSpecAnMXAmpmAMToAMCurveFitType) -> int """
        pass

    def ConfigureAMToPMCurveFit(self, selectorString, amToPMCurveFitOrder, amToPMCurveFitType):
        """ ConfigureAMToPMCurveFit(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, amToPMCurveFitOrder: int, amToPMCurveFitType: RFmxSpecAnMXAmpmAMToPMCurveFitType) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXAmpmAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureCompressionPoints(self, selectorString, compressionPointEnabled, compressionLevel):
        """ ConfigureCompressionPoints(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, compressionPointEnabled: RFmxSpecAnMXAmpmCompressionPointEnabled, compressionLevel: Array[float]) -> int """
        pass

    def ConfigureDutAverageInputPower(self, selectorString, dutAverageInputPower):
        """ ConfigureDutAverageInputPower(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, dutAverageInputPower: float) -> int """
        pass

    def ConfigureMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureMeasurementSampleRate(self, selectorString, sampleRateMode, sampleRate):
        """ ConfigureMeasurementSampleRate(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, sampleRateMode: RFmxSpecAnMXAmpmMeasurementSampleRateMode, sampleRate: float) -> int """
        pass

    def ConfigureReferencePowerType(self, selectorString, referencePowerType):
        """ ConfigureReferencePowerType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, referencePowerType: RFmxSpecAnMXAmpmReferencePowerType) -> int """
        pass

    def ConfigureReferenceWaveform(self, selectorString, referenceWaveform, idleDurationPresent, signalType):
        """ ConfigureReferenceWaveform(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, referenceWaveform: ComplexWaveform[ComplexSingle], idleDurationPresent: RFmxSpecAnMXAmpmReferenceWaveformIdleDurationPresent, signalType: RFmxSpecAnMXAmpmSignalType) -> int """
        pass

    def ConfigureSynchronizationMethod(self, selectorString, synchronizationMethod):
        """ ConfigureSynchronizationMethod(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, synchronizationMethod: RFmxSpecAnMXAmpmSynchronizationMethod) -> int """
        pass

    def ConfigureThreshold(self, selectorString, thresholdEnabled, thresholdLevel, thresholdType):
        """ ConfigureThreshold(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, thresholdEnabled: RFmxSpecAnMXAmpmThresholdEnabled, thresholdLevel: float, thresholdType: RFmxSpecAnMXAmpmThresholdType) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAMToAMCurveFitOrder(self, selectorString, value):
        """ GetAMToAMCurveFitOrder(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAMToAMCurveFitType(self, selectorString, value):
        """ GetAMToAMCurveFitType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmAMToAMCurveFitType) """
        pass

    def GetAMToPMCurveFitOrder(self, selectorString, value):
        """ GetAMToPMCurveFitOrder(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAMToPMCurveFitType(self, selectorString, value):
        """ GetAMToPMCurveFitType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmAMToPMCurveFitType) """
        pass

    def GetAutoCarrierDetectionEnabled(self, selectorString, value):
        """ GetAutoCarrierDetectionEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmAveragingEnabled) """
        pass

    def GetCarrierBandwidth(self, selectorString, value):
        """ GetCarrierBandwidth(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierOffset(self, selectorString, value):
        """ GetCarrierOffset(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCompressionPointEnabled(self, selectorString, value):
        """ GetCompressionPointEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmCompressionPointEnabled) """
        pass

    def GetCompressionPointLevel(self, selectorString, value):
        """ GetCompressionPointLevel(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutAverageInputPower(self, selectorString, value):
        """ GetDutAverageInputPower(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetEqualizerFilterLength(self, selectorString, value):
        """ GetEqualizerFilterLength(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetEqualizerMode(self, selectorString, value):
        """ GetEqualizerMode(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmEqualizerMode) """
        pass

    def GetFrequencyOffsetCorrectionEnabled(self, selectorString, value):
        """ GetFrequencyOffsetCorrectionEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled) """
        pass

    def GetIQOriginOffsetCorrectionEnabled(self, selectorString, value):
        """ GetIQOriginOffsetCorrectionEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled) """
        pass

    def GetMaximumTimingError(self, selectorString, value):
        """ GetMaximumTimingError(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementInterval(self, selectorString, value):
        """ GetMeasurementInterval(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementSampleRate(self, selectorString, value):
        """ GetMeasurementSampleRate(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementSampleRateMode(self, selectorString, value):
        """ GetMeasurementSampleRateMode(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmMeasurementSampleRateMode) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfCarriers(self, selectorString, value):
        """ GetNumberOfCarriers(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetReferencePowerType(self, selectorString, value):
        """ GetReferencePowerType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmReferencePowerType) """
        pass

    def GetSignalType(self, selectorString, value):
        """ GetSignalType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmSignalType) """
        pass

    def GetSynchronizationMethod(self, selectorString, value):
        """ GetSynchronizationMethod(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmSynchronizationMethod) """
        pass

    def GetThresholdEnabled(self, selectorString, value):
        """ GetThresholdEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmThresholdEnabled) """
        pass

    def GetThresholdLevel(self, selectorString, value):
        """ GetThresholdLevel(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetThresholdType(self, selectorString, value):
        """ GetThresholdType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXAmpmThresholdType) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAMToAMCurveFitOrder(self, selectorString, value):
        """ SetAMToAMCurveFitOrder(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAMToAMCurveFitType(self, selectorString, value):
        """ SetAMToAMCurveFitType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmAMToAMCurveFitType) -> int """
        pass

    def SetAMToPMCurveFitOrder(self, selectorString, value):
        """ SetAMToPMCurveFitOrder(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAMToPMCurveFitType(self, selectorString, value):
        """ SetAMToPMCurveFitType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmAMToPMCurveFitType) -> int """
        pass

    def SetAutoCarrierDetectionEnabled(self, selectorString, value):
        """ SetAutoCarrierDetectionEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmAutoCarrierDetectionEnabled) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmAveragingEnabled) -> int """
        pass

    def SetCarrierBandwidth(self, selectorString, value):
        """ SetCarrierBandwidth(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierOffset(self, selectorString, value):
        """ SetCarrierOffset(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCompressionPointEnabled(self, selectorString, value):
        """ SetCompressionPointEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmCompressionPointEnabled) -> int """
        pass

    def SetCompressionPointLevel(self, selectorString, value):
        """ SetCompressionPointLevel(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetDutAverageInputPower(self, selectorString, value):
        """ SetDutAverageInputPower(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetEqualizerFilterLength(self, selectorString, value):
        """ SetEqualizerFilterLength(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetEqualizerMode(self, selectorString, value):
        """ SetEqualizerMode(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmEqualizerMode) -> int """
        pass

    def SetFrequencyOffsetCorrectionEnabled(self, selectorString, value):
        """ SetFrequencyOffsetCorrectionEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled) -> int """
        pass

    def SetIQOriginOffsetCorrectionEnabled(self, selectorString, value):
        """ SetIQOriginOffsetCorrectionEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled) -> int """
        pass

    def SetMaximumTimingError(self, selectorString, value):
        """ SetMaximumTimingError(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementInterval(self, selectorString, value):
        """ SetMeasurementInterval(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementSampleRate(self, selectorString, value):
        """ SetMeasurementSampleRate(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementSampleRateMode(self, selectorString, value):
        """ SetMeasurementSampleRateMode(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmMeasurementSampleRateMode) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfCarriers(self, selectorString, value):
        """ SetNumberOfCarriers(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetReferencePowerType(self, selectorString, value):
        """ SetReferencePowerType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmReferencePowerType) -> int """
        pass

    def SetSignalType(self, selectorString, value):
        """ SetSignalType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmSignalType) -> int """
        pass

    def SetSynchronizationMethod(self, selectorString, value):
        """ SetSynchronizationMethod(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmSynchronizationMethod) -> int """
        pass

    def SetThresholdEnabled(self, selectorString, value):
        """ SetThresholdEnabled(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmThresholdEnabled) -> int """
        pass

    def SetThresholdLevel(self, selectorString, value):
        """ SetThresholdLevel(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetThresholdType(self, selectorString, value):
        """ SetThresholdType(self: RFmxSpecAnMXAmpmConfiguration, selectorString: str, value: RFmxSpecAnMXAmpmThresholdType) -> int """
        pass


class RFmxSpecAnMXAmpmEqualizerMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmEqualizerMode, values: Off (0), Train (1) """
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

    Off = None
    Train = None
    value__ = None


class RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmFrequencyOffsetCorrectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmIQOriginOffsetCorrectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmMeasurementSampleRateMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmMeasurementSampleRateMode, values: ReferenceWaveform (1), User (0) """
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

    ReferenceWaveform = None
    User = None
    value__ = None


class RFmxSpecAnMXAmpmReferencePowerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmReferencePowerType, values: Input (0), Output (1) """
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

    Input = None
    Output = None
    value__ = None


class RFmxSpecAnMXAmpmReferenceWaveformIdleDurationPresent(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmReferenceWaveformIdleDurationPresent, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAMToAMTrace(self, selectorString, timeout, referencePowers, measuredAMToAM, curveFitAMToAM):
        """ FetchAMToAMTrace(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, referencePowers: Array[Single], measuredAMToAM: Array[Single], curveFitAMToAM: Array[Single]) -> (int, Array[Single], Array[Single], Array[Single]) """
        pass

    def FetchAMToPMTrace(self, selectorString, timeout, referencePowers, measuredAMToPM, curveFitAMToPM):
        """ FetchAMToPMTrace(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, referencePowers: Array[Single], measuredAMToPM: Array[Single], curveFitAMToPM: Array[Single]) -> (int, Array[Single], Array[Single], Array[Single]) """
        pass

    def FetchCompressionPoints(self, selectorString, timeout, inputCompressionPoint, outputCompressionPoint):
        """ FetchCompressionPoints(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, inputCompressionPoint: Array[float], outputCompressionPoint: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchCurveFitCoefficients(self, selectorString, timeout, amToAMCoefficients, amToPMCoefficients):
        """ FetchCurveFitCoefficients(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, amToAMCoefficients: Array[Single], amToPMCoefficients: Array[Single]) -> (int, Array[Single], Array[Single]) """
        pass

    def FetchCurveFitResidual(self, selectorString, timeout, amToAMResidual, amToPMResidual):
        """ FetchCurveFitResidual(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchDutCharacteristics(self, selectorString, timeout, meanLinearGain, onedBCompressionPoint, meanRmsEvm):
        """ FetchDutCharacteristics(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchError(self, selectorString, timeout, gainErrorRange, phaseErrorRange, meanPhaseError):
        """ FetchError(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchProcessedMeanAcquiredWaveform(self, selectorString, timeout, processedMeanAcquiredWaveform):
        """ FetchProcessedMeanAcquiredWaveform(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, processedMeanAcquiredWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    def FetchProcessedReferenceWaveform(self, selectorString, timeout, processedReferenceWaveform):
        """ FetchProcessedReferenceWaveform(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, processedReferenceWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    def FetchRelativePhaseTrace(self, selectorString, timeout, relativePhase):
        """ FetchRelativePhaseTrace(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, relativePhase: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchRelativePowerTrace(self, selectorString, timeout, relativePower):
        """ FetchRelativePowerTrace(self: RFmxSpecAnMXAmpmResults, selectorString: str, timeout: float, relativePower: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def Get1dBCompressionPoint(self, selectorString, value):
        """ Get1dBCompressionPoint(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetAMToAMCurveFitCoefficients(self, selectorString, value):
        """ GetAMToAMCurveFitCoefficients(self: RFmxSpecAnMXAmpmResults, selectorString: str, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetAMToAMCurveFitResidual(self, selectorString, value):
        """ GetAMToAMCurveFitResidual(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetAMToPMCurveFitCoefficients(self, selectorString, value):
        """ GetAMToPMCurveFitCoefficients(self: RFmxSpecAnMXAmpmResults, selectorString: str, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetAMToPMCurveFitResidual(self, selectorString, value):
        """ GetAMToPMCurveFitResidual(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetGainErrorRange(self, selectorString, value):
        """ GetGainErrorRange(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetInputCompressionPoint(self, selectorString, value):
        """ GetInputCompressionPoint(self: RFmxSpecAnMXAmpmResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetMeanLinearGain(self, selectorString, value):
        """ GetMeanLinearGain(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanPhaseError(self, selectorString, value):
        """ GetMeanPhaseError(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsEvm(self, selectorString, value):
        """ GetMeanRmsEvm(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass

    def GetOutputCompressionPoint(self, selectorString, value):
        """ GetOutputCompressionPoint(self: RFmxSpecAnMXAmpmResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetPhaseErrorRange(self, selectorString, value):
        """ GetPhaseErrorRange(self: RFmxSpecAnMXAmpmResults, selectorString: str) -> (int, float) """
        pass


class RFmxSpecAnMXAmpmSignalType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmSignalType, values: Modulated (0), Tones (1) """
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

    Modulated = None
    Tones = None
    value__ = None


class RFmxSpecAnMXAmpmSynchronizationMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmSynchronizationMethod, values: AliasProtected (2), Direct (1) """
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

    AliasProtected = None
    Direct = None
    value__ = None


class RFmxSpecAnMXAmpmThresholdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmThresholdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXAmpmThresholdType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXAmpmThresholdType, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXCcdf(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXCcdf) -> RFmxSpecAnMXCcdfConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXCcdf) -> RFmxSpecAnMXCcdfResults

"""



class RFmxSpecAnMXCcdfConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureNumberOfRecords(self, selectorString, numberOfRecords):
        """ ConfigureNumberOfRecords(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, numberOfRecords: int) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbw, rbwFilterType, rrcAlpha):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, rbw: float, rbwFilterType: RFmxSpecAnMXCcdfRbwFilterType, rrcAlpha: float) -> int """
        pass

    def ConfigureThreshold(self, selectorString, thresholdEnabled, thresholdLevel, thresholdType):
        """ ConfigureThreshold(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, thresholdEnabled: RFmxSpecAnMXCcdfThresholdEnabled, thresholdLevel: float, thresholdType: RFmxSpecAnMXCcdfThresholdType) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementInterval(self, selectorString, value):
        """ GetMeasurementInterval(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfRecords(self, selectorString, value):
        """ GetNumberOfRecords(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterRrcAlpha(self, selectorString, value):
        """ GetRbwFilterRrcAlpha(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, RFmxSpecAnMXCcdfRbwFilterType) """
        pass

    def GetThresholdEnabled(self, selectorString, value):
        """ GetThresholdEnabled(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, RFmxSpecAnMXCcdfThresholdEnabled) """
        pass

    def GetThresholdLevel(self, selectorString, value):
        """ GetThresholdLevel(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetThresholdType(self, selectorString, value):
        """ GetThresholdType(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str) -> (int, RFmxSpecAnMXCcdfThresholdType) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementInterval(self, selectorString, value):
        """ SetMeasurementInterval(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfRecords(self, selectorString, value):
        """ SetNumberOfRecords(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterRrcAlpha(self, selectorString, value):
        """ SetRbwFilterRrcAlpha(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: RFmxSpecAnMXCcdfRbwFilterType) -> int """
        pass

    def SetThresholdEnabled(self, selectorString, value):
        """ SetThresholdEnabled(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: RFmxSpecAnMXCcdfThresholdEnabled) -> int """
        pass

    def SetThresholdLevel(self, selectorString, value):
        """ SetThresholdLevel(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetThresholdType(self, selectorString, value):
        """ SetThresholdType(self: RFmxSpecAnMXCcdfConfiguration, selectorString: str, value: RFmxSpecAnMXCcdfThresholdType) -> int """
        pass


class RFmxSpecAnMXCcdfRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXCcdfRbwFilterType, values: Flat (2), Gaussian (1), None (5), Rrc (6), SynchTuned4 (3), SynchTuned5 (4) """
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

    Flat = None
    Gaussian = None
    None = None
    Rrc = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXCcdfResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchBasicPowerProbabilities(self, selectorString, timeout, tenPercentPower, onePercentPower, oneTenthPercentPower, oneHundredthPercentPower, oneThousandthPercentPower, oneTenThousandthPercentPower):
        """ FetchBasicPowerProbabilities(self: RFmxSpecAnMXCcdfResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float, float) """
        pass

    def FetchGaussianProbabilitiesTrace(self, selectorString, timeout, gaussianProbabilities):
        """ FetchGaussianProbabilitiesTrace(self: RFmxSpecAnMXCcdfResults, selectorString: str, timeout: float, gaussianProbabilities: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPower(self, selectorString, timeout, meanPower, meanPowerPercentile, peakPower, measuredSamplesCount):
        """ FetchPower(self: RFmxSpecAnMXCcdfResults, selectorString: str, timeout: float) -> (int, float, float, float, int) """
        pass

    def FetchProbabilitiesTrace(self, selectorString, timeout, probabilities):
        """ FetchProbabilitiesTrace(self: RFmxSpecAnMXCcdfResults, selectorString: str, timeout: float, probabilities: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def GetMeanPower(self, selectorString, value):
        """ GetMeanPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanPowerPercentile(self, selectorString, value):
        """ GetMeanPowerPercentile(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetMeasuredSamplesCount(self, selectorString, value):
        """ GetMeasuredSamplesCount(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, int) """
        pass

    def GetOneHundredthPercentPower(self, selectorString, value):
        """ GetOneHundredthPercentPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetOnePercentPower(self, selectorString, value):
        """ GetOnePercentPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetOneTenThousandthPercentPower(self, selectorString, value):
        """ GetOneTenThousandthPercentPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetOneTenthPercentPower(self, selectorString, value):
        """ GetOneTenthPercentPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetOneThousandthPercentPower(self, selectorString, value):
        """ GetOneThousandthPercentPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakPower(self, selectorString, value):
        """ GetPeakPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def GetTenPercentPower(self, selectorString, value):
        """ GetTenPercentPower(self: RFmxSpecAnMXCcdfResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, meanPower, meanPowerPercentile, peakPower, measuredSamplesCount):
        """ Read(self: RFmxSpecAnMXCcdfResults, selectorString: str, timeout: float) -> (int, float, float, float, int) """
        pass


class RFmxSpecAnMXCcdfThresholdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXCcdfThresholdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXCcdfThresholdType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXCcdfThresholdType, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXChp(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXChp) -> RFmxSpecAnMXChpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXChp) -> RFmxSpecAnMXChpResults

"""



class RFmxSpecAnMXChpAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXChpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXChpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2), Vector (5) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RFmxSpecAnMXChpCarrierRrcFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpCarrierRrcFilterEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXChpConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXChpConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXChpAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXChpAveragingType) -> int """
        pass

    def ConfigureCarrierOffset(self, selectorString, carrierFrequency):
        """ ConfigureCarrierOffset(self: RFmxSpecAnMXChpConfiguration, selectorString: str, carrierFrequency: float) -> int """
        pass

    def ConfigureFft(self, selectorString, fftWindow, fftPadding):
        """ ConfigureFft(self: RFmxSpecAnMXChpConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXChpFftWindow, fftPadding: float) -> int """
        pass

    def ConfigureIntegrationBandwidth(self, selectorString, integrationBandwidth):
        """ ConfigureIntegrationBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str, integrationBandwidth: float) -> int """
        pass

    def ConfigureNumberOfCarriers(self, selectorString, numberOfCarriers):
        """ ConfigureNumberOfCarriers(self: RFmxSpecAnMXChpConfiguration, selectorString: str, numberOfCarriers: int) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXChpConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXChpRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXChpRbwFilterType) -> int """
        pass

    def ConfigureRrcFilter(self, selectorString, rrcFilterEnabled, rrcAlpha):
        """ ConfigureRrcFilter(self: RFmxSpecAnMXChpConfiguration, selectorString: str, rrcFilterEnabled: RFmxSpecAnMXChpCarrierRrcFilterEnabled, rrcAlpha: float) -> int """
        pass

    def ConfigureSpan(self, selectorString, span):
        """ ConfigureSpan(self: RFmxSpecAnMXChpConfiguration, selectorString: str, span: float) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxSpecAnMXChpConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXChpSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpAveragingType) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRrcFilterAlpha(self, selectorString, value):
        """ GetCarrierRrcFilterAlpha(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRrcFilterEnabled(self, selectorString, value):
        """ GetCarrierRrcFilterEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpCarrierRrcFilterEnabled) """
        pass

    def GetFftPadding(self, selectorString, value):
        """ GetFftPadding(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpFftWindow) """
        pass

    def GetIntegrationBandwidth(self, selectorString, value):
        """ GetIntegrationBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfCarriers(self, selectorString, value):
        """ GetNumberOfCarriers(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpRbwFilterBandwidthDefinition) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpRbwFilterType) """
        pass

    def GetRrcFilterAlpha(self, selectorString, value):
        """ GetRrcFilterAlpha(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRrcFilterEnabled(self, selectorString, value):
        """ GetRrcFilterEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpRrcFilterEnabled) """
        pass

    def GetSpan(self, selectorString, value):
        """ GetSpan(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXChpSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxSpecAnMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpAveragingType) -> int """
        pass

    def SetCarrierFrequency(self, selectorString, value):
        """ SetCarrierFrequency(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierIntegrationBandwidth(self, selectorString, value):
        """ SetCarrierIntegrationBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierRrcFilterAlpha(self, selectorString, value):
        """ SetCarrierRrcFilterAlpha(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierRrcFilterEnabled(self, selectorString, value):
        """ SetCarrierRrcFilterEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpCarrierRrcFilterEnabled) -> int """
        pass

    def SetFftPadding(self, selectorString, value):
        """ SetFftPadding(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpFftWindow) -> int """
        pass

    def SetIntegrationBandwidth(self, selectorString, value):
        """ SetIntegrationBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfCarriers(self, selectorString, value):
        """ SetNumberOfCarriers(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpRbwFilterBandwidthDefinition) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpRbwFilterType) -> int """
        pass

    def SetRrcFilterAlpha(self, selectorString, value):
        """ SetRrcFilterAlpha(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRrcFilterEnabled(self, selectorString, value):
        """ SetRrcFilterEnabled(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpRrcFilterEnabled) -> int """
        pass

    def SetSpan(self, selectorString, value):
        """ SetSpan(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: RFmxSpecAnMXChpSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxSpecAnMXChpConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXChpFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXChpRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXChpRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinitionBinWidth (2) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinitionBinWidth = None
    value__ = None


class RFmxSpecAnMXChpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXChpResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchCarrierMeasurement(self, selectorString, timeout, absolutePower, psd, relativePower):
        """ FetchCarrierMeasurement(self: RFmxSpecAnMXChpResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchMeasurement(self, selectorString, timeout, averageChannelPower, averageChannelPsd, frequencyResolution):
        """ FetchMeasurement(self: RFmxSpecAnMXChpResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxSpecAnMXChpResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchTotalCarrierPower(self, selectorString, timeout, totalCarrierPower):
        """ FetchTotalCarrierPower(self: RFmxSpecAnMXChpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def GetAverageChannelPower(self, selectorString, value):
        """ GetAverageChannelPower(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetAverageChannelPowerPsd(self, selectorString, value):
        """ GetAverageChannelPowerPsd(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierAbsolutePower(self, selectorString, value):
        """ GetCarrierAbsolutePower(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierPsd(self, selectorString, value):
        """ GetCarrierPsd(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRelativePower(self, selectorString, value):
        """ GetCarrierRelativePower(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyResolution(self, selectorString, value):
        """ GetFrequencyResolution(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalCarrierPower(self, selectorString, value):
        """ GetTotalCarrierPower(self: RFmxSpecAnMXChpResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, absolutePower, psd):
        """ Read(self: RFmxSpecAnMXChpResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass


class RFmxSpecAnMXChpRrcFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpRrcFilterEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXChpSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXChpSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXConstants(object):
    # no doc
    Pfi0 = 'PFI0'
    Pfi1 = 'PFI1'
    PxiStarLine = 'PXI_STAR'
    PxiTriggerLine0 = 'PXI_Trig0'
    PxiTriggerLine1 = 'PXI_Trig1'
    PxiTriggerLine2 = 'PXI_Trig2'
    PxiTriggerLine3 = 'PXI_Trig3'
    PxiTriggerLine4 = 'PXI_Trig4'
    PxiTriggerLine5 = 'PXI_Trig5'
    PxiTriggerLine6 = 'PXI_Trig6'
    PxiTriggerLine7 = 'PXI_Trig7'
    __all__ = [
        'Pfi0',
        'Pfi1',
        'PxiStarLine',
        'PxiTriggerLine0',
        'PxiTriggerLine1',
        'PxiTriggerLine2',
        'PxiTriggerLine3',
        'PxiTriggerLine4',
        'PxiTriggerLine5',
        'PxiTriggerLine6',
        'PxiTriggerLine7',
    ]


class RFmxSpecAnMXDigitalEdgeTriggerEdge(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDigitalEdgeTriggerEdge, values: Falling (1), Rising (0) """
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

    Falling = None
    Rising = None
    value__ = None


class RFmxSpecAnMXDpd(RFmxSpecAnMXSubObject):
    # no doc
    ApplyDpd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyDpd(self: RFmxSpecAnMXDpd) -> RFmxSpecAnMXDpdApplyDpd

"""

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXDpd) -> RFmxSpecAnMXDpdConfiguration

"""

    PreDpd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreDpd(self: RFmxSpecAnMXDpd) -> RFmxSpecAnMXDpdPreDpd

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXDpd) -> RFmxSpecAnMXDpdResults

"""



class RFmxSpecAnMXDpdApplyDpd(RFmxSpecAnMXSubObject):
    # no doc
    def ApplyDigitalPredistortion(self, selectorString, waveformIn, idleDurationPresent, measurementTimeout, waveformOut, papr, powerOffset):
        """ ApplyDigitalPredistortion(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, waveformIn: ComplexWaveform[ComplexSingle], idleDurationPresent: RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, measurementTimeout: float, waveformOut: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle], float, float) """
        pass

    def ApplyDpd(self, selectorString, waveformIn, idleDurationPresent, measurementTimeout, waveformOut, appliedHeadroom):
        """ ApplyDpd(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, waveformIn: ComplexWaveform[ComplexSingle], idleDurationPresent: RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, measurementTimeout: float, waveformOut: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle], float) """
        pass

    def ConfigureConfigurationInput(self, selectorString, configurationInput):
        """ ConfigureConfigurationInput(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, configurationInput: RFmxSpecAnMXDpdApplyDpdConfigurationInput) -> int """
        pass

    def ConfigureHeadroom(self, selectorString, headroomMode, headroom):
        """ ConfigureHeadroom(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, headroomMode: RFmxSpecAnMXDpdApplyDpdHeadroomMode, headroom: float) -> int """
        pass

    def ConfigureLookupTableCorrectionType(self, selectorString, lutCorrectionType):
        """ ConfigureLookupTableCorrectionType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, lutCorrectionType: RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType) -> int """
        pass

    def ConfigureMemoryModelCorrectionType(self, selectorString, memoryModelCorrectionType):
        """ ConfigureMemoryModelCorrectionType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, memoryModelCorrectionType: RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType) -> int """
        pass

    def ConfigureUserDpdPolynomial(self, selectorString, dpdPolynomial):
        """ ConfigureUserDpdPolynomial(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, dpdPolynomial: Array[ComplexSingle]) -> int """
        pass

    def ConfigureUserLookupTable(self, selectorString, lutInputPowers, lutComplexGains):
        """ ConfigureUserLookupTable(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, lutInputPowers: Array[Single], lutComplexGains: Array[ComplexSingle]) -> int """
        pass

    def GetCfrEnabled(self, selectorString, value):
        """ GetCfrEnabled(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdCfrEnabled) """
        pass

    def GetCfrMaximumIterations(self, selectorString, value):
        """ GetCfrMaximumIterations(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetCfrMethod(self, selectorString, value):
        """ GetCfrMethod(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdCfrMethod) """
        pass

    def GetCfrShapingFactor(self, selectorString, value):
        """ GetCfrShapingFactor(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrShapingThreshold(self, selectorString, value):
        """ GetCfrShapingThreshold(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrTargetPapr(self, selectorString, value):
        """ GetCfrTargetPapr(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrTargetPaprType(self, selectorString, value):
        """ GetCfrTargetPaprType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType) """
        pass

    def GetCfrWindowLength(self, selectorString, value):
        """ GetCfrWindowLength(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetCfrWindowType(self, selectorString, value):
        """ GetCfrWindowType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdCfrWindowType) """
        pass

    def GetConfigurationInput(self, selectorString, value):
        """ GetConfigurationInput(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdConfigurationInput) """
        pass

    def GetHeadroom(self, selectorString, value):
        """ GetHeadroom(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, float) """
        pass

    def GetHeadroomMode(self, selectorString, value):
        """ GetHeadroomMode(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdHeadroomMode) """
        pass

    def GetLookupTableCorrectionType(self, selectorString, value):
        """ GetLookupTableCorrectionType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType) """
        pass

    def GetMemoryModelCorrectionType(self, selectorString, value):
        """ GetMemoryModelCorrectionType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType) """
        pass

    def GetUserDpdModel(self, selectorString, value):
        """ GetUserDpdModel(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdUserDpdModel) """
        pass

    def GetUserDutAverageInputPower(self, selectorString, value):
        """ GetUserDutAverageInputPower(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, float) """
        pass

    def GetUserLookupTableInputPower(self, selectorString, value):
        """ GetUserLookupTableInputPower(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetUserMeasurementSampleRate(self, selectorString, value):
        """ GetUserMeasurementSampleRate(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, float) """
        pass

    def GetUserMemoryPolynomialLagMemoryDepth(self, selectorString, value):
        """ GetUserMemoryPolynomialLagMemoryDepth(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialLagOrder(self, selectorString, value):
        """ GetUserMemoryPolynomialLagOrder(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialLeadMemoryDepth(self, selectorString, value):
        """ GetUserMemoryPolynomialLeadMemoryDepth(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialLeadOrder(self, selectorString, value):
        """ GetUserMemoryPolynomialLeadOrder(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialMaximumLag(self, selectorString, value):
        """ GetUserMemoryPolynomialMaximumLag(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialMaximumLead(self, selectorString, value):
        """ GetUserMemoryPolynomialMaximumLead(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialMemoryDepth(self, selectorString, value):
        """ GetUserMemoryPolynomialMemoryDepth(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def GetUserMemoryPolynomialOrder(self, selectorString, value):
        """ GetUserMemoryPolynomialOrder(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str) -> (int, int) """
        pass

    def SetCfrEnabled(self, selectorString, value):
        """ SetCfrEnabled(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdCfrEnabled) -> int """
        pass

    def SetCfrMaximumIterations(self, selectorString, value):
        """ SetCfrMaximumIterations(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetCfrMethod(self, selectorString, value):
        """ SetCfrMethod(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdCfrMethod) -> int """
        pass

    def SetCfrShapingFactor(self, selectorString, value):
        """ SetCfrShapingFactor(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrShapingThreshold(self, selectorString, value):
        """ SetCfrShapingThreshold(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrTargetPapr(self, selectorString, value):
        """ SetCfrTargetPapr(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrTargetPaprType(self, selectorString, value):
        """ SetCfrTargetPaprType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType) -> int """
        pass

    def SetCfrWindowLength(self, selectorString, value):
        """ SetCfrWindowLength(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetCfrWindowType(self, selectorString, value):
        """ SetCfrWindowType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdCfrWindowType) -> int """
        pass

    def SetConfigurationInput(self, selectorString, value):
        """ SetConfigurationInput(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdConfigurationInput) -> int """
        pass

    def SetHeadroom(self, selectorString, value):
        """ SetHeadroom(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: float) -> int """
        pass

    def SetHeadroomMode(self, selectorString, value):
        """ SetHeadroomMode(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdHeadroomMode) -> int """
        pass

    def SetLookupTableCorrectionType(self, selectorString, value):
        """ SetLookupTableCorrectionType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType) -> int """
        pass

    def SetMemoryModelCorrectionType(self, selectorString, value):
        """ SetMemoryModelCorrectionType(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType) -> int """
        pass

    def SetUserDpdModel(self, selectorString, value):
        """ SetUserDpdModel(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdUserDpdModel) -> int """
        pass

    def SetUserDutAverageInputPower(self, selectorString, value):
        """ SetUserDutAverageInputPower(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: float) -> int """
        pass

    def SetUserLookupTableInputPower(self, selectorString, value):
        """ SetUserLookupTableInputPower(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: Array[Single]) -> int """
        pass

    def SetUserMeasurementSampleRate(self, selectorString, value):
        """ SetUserMeasurementSampleRate(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: float) -> int """
        pass

    def SetUserMemoryPolynomialLagMemoryDepth(self, selectorString, value):
        """ SetUserMemoryPolynomialLagMemoryDepth(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialLagOrder(self, selectorString, value):
        """ SetUserMemoryPolynomialLagOrder(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialLeadMemoryDepth(self, selectorString, value):
        """ SetUserMemoryPolynomialLeadMemoryDepth(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialLeadOrder(self, selectorString, value):
        """ SetUserMemoryPolynomialLeadOrder(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialMaximumLag(self, selectorString, value):
        """ SetUserMemoryPolynomialMaximumLag(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialMaximumLead(self, selectorString, value):
        """ SetUserMemoryPolynomialMaximumLead(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialMemoryDepth(self, selectorString, value):
        """ SetUserMemoryPolynomialMemoryDepth(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass

    def SetUserMemoryPolynomialOrder(self, selectorString, value):
        """ SetUserMemoryPolynomialOrder(self: RFmxSpecAnMXDpdApplyDpd, selectorString: str, value: int) -> int """
        pass


class RFmxSpecAnMXDpdApplyDpdCfrEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdCfrEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdApplyDpdCfrMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdCfrMethod, values: Clipping (0), PeakWindowing (1), Sigmoid (2) """
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

    Clipping = None
    PeakWindowing = None
    Sigmoid = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdCfrTargetPaprType, values: Custom (1), InputPapr (0) """
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

    Custom = None
    InputPapr = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdCfrWindowType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdCfrWindowType, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdConfigurationInput(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdConfigurationInput, values: Measurement (0), User (1) """
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

    Measurement = None
    User = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdHeadroomMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdHeadroomMode, values: Auto (1), Manual (2), Off (0) """
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
    Manual = None
    Off = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdIdleDurationPresent(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdLookupTableCorrectionType, values: MagnitudeAndPhase (0), MagnitudeOnly (1), PhaseOnly (2) """
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

    MagnitudeAndPhase = None
    MagnitudeOnly = None
    PhaseOnly = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdMemoryModelCorrectionType, values: MagnitudeAndPhase (0), MagnitudeOnly (1), PhaseOnly (2) """
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

    MagnitudeAndPhase = None
    MagnitudeOnly = None
    PhaseOnly = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdUserDpdModel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdUserDpdModel, values: GeneralizedMemoryPolynomial (2), LookupTable (0), MemoryPolynomial (1) """
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

    GeneralizedMemoryPolynomial = None
    LookupTable = None
    MemoryPolynomial = None
    value__ = None


class RFmxSpecAnMXDpdApplyDpdUserLookupTableType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdApplyDpdUserLookupTableType, values: Linear (1), Log (0) """
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

    Linear = None
    Log = None
    value__ = None


class RFmxSpecAnMXDpdAutoCarrierDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdAutoCarrierDetectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXDpdAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureDpdModel(self, selectorString, dpdModel):
        """ ConfigureDpdModel(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, dpdModel: RFmxSpecAnMXDpdModel) -> int """
        pass

    def ConfigureDutAverageInputPower(self, selectorString, dutAverageInputPower):
        """ ConfigureDutAverageInputPower(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, dutAverageInputPower: float) -> int """
        pass

    def ConfigureGeneralizedMemoryPolynomialCrossTerms(self, selectorString, memoryPolynomialLeadOrder, memoryPolynomialLagOrder, memoryPolynomialLeadMemoryDepth, memoryPolynomialLagMemoryDepth, memoryPolynomialMaximumLead, memoryPolynomialMaximumLag):
        """ ConfigureGeneralizedMemoryPolynomialCrossTerms(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, memoryPolynomialLeadOrder: int, memoryPolynomialLagOrder: int, memoryPolynomialLeadMemoryDepth: int, memoryPolynomialLagMemoryDepth: int, memoryPolynomialMaximumLead: int, memoryPolynomialMaximumLag: int) -> int """
        pass

    def ConfigureIterativeDpdEnabled(self, selectorString, iterativeDpdEnabled):
        """ ConfigureIterativeDpdEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, iterativeDpdEnabled: RFmxSpecAnMXDpdIterativeDpdEnabled) -> int """
        pass

    def ConfigureLookupTableAMToAMCurveFit(self, selectorString, amToAMCurveFitOrder, amToAMCurveFitType):
        """ ConfigureLookupTableAMToAMCurveFit(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, amToAMCurveFitOrder: int, amToAMCurveFitType: RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType) -> int """
        pass

    def ConfigureLookupTableAMToPMCurveFit(self, selectorString, amToPMCurveFitOrder, amToPMCurveFitType):
        """ ConfigureLookupTableAMToPMCurveFit(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, amToPMCurveFitOrder: int, amToPMCurveFitType: RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType) -> int """
        pass

    def ConfigureLookupTableStepSize(self, selectorString, stepSize):
        """ ConfigureLookupTableStepSize(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, stepSize: float) -> int """
        pass

    def ConfigureLookupTableThreshold(self, selectorString, thresholdEnabled, thresholdLevel, thresholdType):
        """ ConfigureLookupTableThreshold(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, thresholdEnabled: RFmxSpecAnMXDpdLookupTableThresholdEnabled, thresholdLevel: float, thresholdType: RFmxSpecAnMXDpdLookupTableThresholdType) -> int """
        pass

    def ConfigureLookupTableType(self, selectorString, lookupTableType):
        """ ConfigureLookupTableType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, lookupTableType: RFmxSpecAnMXDpdLookupTableType) -> int """
        pass

    def ConfigureMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureMeasurementSampleRate(self, selectorString, sampleRateMode, sampleRate):
        """ ConfigureMeasurementSampleRate(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, sampleRateMode: RFmxSpecAnMXDpdMeasurementSampleRateMode, sampleRate: float) -> int """
        pass

    def ConfigureMemoryPolynomial(self, selectorString, memoryPolynomialOrder, memoryPolynomialMemoryDepth):
        """ ConfigureMemoryPolynomial(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, memoryPolynomialOrder: int, memoryPolynomialMemoryDepth: int) -> int """
        pass

    def ConfigurePreviousDpdPolynomial(self, selectorString, previousDpdPolynomial):
        """ ConfigurePreviousDpdPolynomial(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, previousDpdPolynomial: Array[ComplexSingle]) -> int """
        pass

    def ConfigureReferenceWaveform(self, selectorString, referenceWaveform, idleDurationPresent, signalType):
        """ ConfigureReferenceWaveform(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, referenceWaveform: ComplexWaveform[ComplexSingle], idleDurationPresent: RFmxSpecAnMXDpdReferenceWaveformIdleDurationPresent, signalType: RFmxSpecAnMXDpdSignalType) -> int """
        pass

    def ConfigureSynchronizationMethod(self, selectorString, synchronizationMethod):
        """ ConfigureSynchronizationMethod(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, synchronizationMethod: RFmxSpecAnMXDpdSynchronizationMethod) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetApplyDpdUserLookupTableInputPower(self, selectorString, value):
        """ GetApplyDpdUserLookupTableInputPower(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetApplyDpdUserLookupTableType(self, selectorString, value):
        """ GetApplyDpdUserLookupTableType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdApplyDpdUserLookupTableType) """
        pass

    def GetAutoCarrierDetectionEnabled(self, selectorString, value):
        """ GetAutoCarrierDetectionEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdAveragingEnabled) """
        pass

    def GetCarrierBandwidth(self, selectorString, value):
        """ GetCarrierBandwidth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierOffset(self, selectorString, value):
        """ GetCarrierOffset(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDutAverageInputPower(self, selectorString, value):
        """ GetDutAverageInputPower(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyOffsetCorrectionEnabled(self, selectorString, value):
        """ GetFrequencyOffsetCorrectionEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled) """
        pass

    def GetIQOriginOffsetCorrectionEnabled(self, selectorString, value):
        """ GetIQOriginOffsetCorrectionEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled) """
        pass

    def GetIterativeDpdEnabled(self, selectorString, value):
        """ GetIterativeDpdEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdIterativeDpdEnabled) """
        pass

    def GetLookupTableAMToAMCurveFitOrder(self, selectorString, value):
        """ GetLookupTableAMToAMCurveFitOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetLookupTableAMToAMCurveFitType(self, selectorString, value):
        """ GetLookupTableAMToAMCurveFitType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType) """
        pass

    def GetLookupTableAMToPMCurveFitOrder(self, selectorString, value):
        """ GetLookupTableAMToPMCurveFitOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetLookupTableAMToPMCurveFitType(self, selectorString, value):
        """ GetLookupTableAMToPMCurveFitType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType) """
        pass

    def GetLookupTableStepSize(self, selectorString, value):
        """ GetLookupTableStepSize(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetLookupTableThresholdEnabled(self, selectorString, value):
        """ GetLookupTableThresholdEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdLookupTableThresholdEnabled) """
        pass

    def GetLookupTableThresholdLevel(self, selectorString, value):
        """ GetLookupTableThresholdLevel(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetLookupTableThresholdType(self, selectorString, value):
        """ GetLookupTableThresholdType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdLookupTableThresholdType) """
        pass

    def GetLookupTableType(self, selectorString, value):
        """ GetLookupTableType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdLookupTableType) """
        pass

    def GetMaximumTimingError(self, selectorString, value):
        """ GetMaximumTimingError(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementInterval(self, selectorString, value):
        """ GetMeasurementInterval(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementSampleRate(self, selectorString, value):
        """ GetMeasurementSampleRate(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementSampleRateMode(self, selectorString, value):
        """ GetMeasurementSampleRateMode(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdMeasurementSampleRateMode) """
        pass

    def GetMemoryPolynomialLagMemoryDepth(self, selectorString, value):
        """ GetMemoryPolynomialLagMemoryDepth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialLagOrder(self, selectorString, value):
        """ GetMemoryPolynomialLagOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialLeadMemoryDepth(self, selectorString, value):
        """ GetMemoryPolynomialLeadMemoryDepth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialLeadOrder(self, selectorString, value):
        """ GetMemoryPolynomialLeadOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialMaximumLag(self, selectorString, value):
        """ GetMemoryPolynomialMaximumLag(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialMaximumLead(self, selectorString, value):
        """ GetMemoryPolynomialMaximumLead(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialMemoryDepth(self, selectorString, value):
        """ GetMemoryPolynomialMemoryDepth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMemoryPolynomialOrder(self, selectorString, value):
        """ GetMemoryPolynomialOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetModel(self, selectorString, value):
        """ GetModel(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdModel) """
        pass

    def GetNmseEnabled(self, selectorString, value):
        """ GetNmseEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdNmseEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfCarriers(self, selectorString, value):
        """ GetNumberOfCarriers(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSignalType(self, selectorString, value):
        """ GetSignalType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdSignalType) """
        pass

    def GetSynchronizationMethod(self, selectorString, value):
        """ GetSynchronizationMethod(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdSynchronizationMethod) """
        pass

    def GetTargetGainType(self, selectorString, value):
        """ GetTargetGainType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str) -> (int, RFmxSpecAnMXDpdTargetGainType) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetApplyDpdUserLookupTableInputPower(self, selectorString, value):
        """ SetApplyDpdUserLookupTableInputPower(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: Array[Single]) -> int """
        pass

    def SetApplyDpdUserLookupTableType(self, selectorString, value):
        """ SetApplyDpdUserLookupTableType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdApplyDpdUserLookupTableType) -> int """
        pass

    def SetAutoCarrierDetectionEnabled(self, selectorString, value):
        """ SetAutoCarrierDetectionEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdAutoCarrierDetectionEnabled) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdAveragingEnabled) -> int """
        pass

    def SetCarrierBandwidth(self, selectorString, value):
        """ SetCarrierBandwidth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierOffset(self, selectorString, value):
        """ SetCarrierOffset(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetDutAverageInputPower(self, selectorString, value):
        """ SetDutAverageInputPower(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFrequencyOffsetCorrectionEnabled(self, selectorString, value):
        """ SetFrequencyOffsetCorrectionEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled) -> int """
        pass

    def SetIQOriginOffsetCorrectionEnabled(self, selectorString, value):
        """ SetIQOriginOffsetCorrectionEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled) -> int """
        pass

    def SetIterativeDpdEnabled(self, selectorString, value):
        """ SetIterativeDpdEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdIterativeDpdEnabled) -> int """
        pass

    def SetLookupTableAMToAMCurveFitOrder(self, selectorString, value):
        """ SetLookupTableAMToAMCurveFitOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetLookupTableAMToAMCurveFitType(self, selectorString, value):
        """ SetLookupTableAMToAMCurveFitType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType) -> int """
        pass

    def SetLookupTableAMToPMCurveFitOrder(self, selectorString, value):
        """ SetLookupTableAMToPMCurveFitOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetLookupTableAMToPMCurveFitType(self, selectorString, value):
        """ SetLookupTableAMToPMCurveFitType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType) -> int """
        pass

    def SetLookupTableStepSize(self, selectorString, value):
        """ SetLookupTableStepSize(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetLookupTableThresholdEnabled(self, selectorString, value):
        """ SetLookupTableThresholdEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdLookupTableThresholdEnabled) -> int """
        pass

    def SetLookupTableThresholdLevel(self, selectorString, value):
        """ SetLookupTableThresholdLevel(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetLookupTableThresholdType(self, selectorString, value):
        """ SetLookupTableThresholdType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdLookupTableThresholdType) -> int """
        pass

    def SetLookupTableType(self, selectorString, value):
        """ SetLookupTableType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdLookupTableType) -> int """
        pass

    def SetMaximumTimingError(self, selectorString, value):
        """ SetMaximumTimingError(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementInterval(self, selectorString, value):
        """ SetMeasurementInterval(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementSampleRate(self, selectorString, value):
        """ SetMeasurementSampleRate(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementSampleRateMode(self, selectorString, value):
        """ SetMeasurementSampleRateMode(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdMeasurementSampleRateMode) -> int """
        pass

    def SetMemoryPolynomialLagMemoryDepth(self, selectorString, value):
        """ SetMemoryPolynomialLagMemoryDepth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialLagOrder(self, selectorString, value):
        """ SetMemoryPolynomialLagOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialLeadMemoryDepth(self, selectorString, value):
        """ SetMemoryPolynomialLeadMemoryDepth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialLeadOrder(self, selectorString, value):
        """ SetMemoryPolynomialLeadOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialMaximumLag(self, selectorString, value):
        """ SetMemoryPolynomialMaximumLag(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialMaximumLead(self, selectorString, value):
        """ SetMemoryPolynomialMaximumLead(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialMemoryDepth(self, selectorString, value):
        """ SetMemoryPolynomialMemoryDepth(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMemoryPolynomialOrder(self, selectorString, value):
        """ SetMemoryPolynomialOrder(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetModel(self, selectorString, value):
        """ SetModel(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdModel) -> int """
        pass

    def SetNmseEnabled(self, selectorString, value):
        """ SetNmseEnabled(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdNmseEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfCarriers(self, selectorString, value):
        """ SetNumberOfCarriers(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSignalType(self, selectorString, value):
        """ SetSignalType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdSignalType) -> int """
        pass

    def SetSynchronizationMethod(self, selectorString, value):
        """ SetSynchronizationMethod(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdSynchronizationMethod) -> int """
        pass

    def SetTargetGainType(self, selectorString, value):
        """ SetTargetGainType(self: RFmxSpecAnMXDpdConfiguration, selectorString: str, value: RFmxSpecAnMXDpdTargetGainType) -> int """
        pass


class RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdFrequencyOffsetCorrectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdIQOriginOffsetCorrectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdIterativeDpdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdIterativeDpdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdLookupTableAMToAMCurveFitType, values: Bisquare (2), LeastAbsoluteResidual (1), LeastSquare (0) """
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

    Bisquare = None
    LeastAbsoluteResidual = None
    LeastSquare = None
    value__ = None


class RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdLookupTableAMToPMCurveFitType, values: Bisquare (2), LeastAbsoluteResidual (1), LeastSquare (0) """
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

    Bisquare = None
    LeastAbsoluteResidual = None
    LeastSquare = None
    value__ = None


class RFmxSpecAnMXDpdLookupTableThresholdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdLookupTableThresholdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdLookupTableThresholdType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdLookupTableThresholdType, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXDpdLookupTableType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdLookupTableType, values: Linear (1), Log (0) """
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

    Linear = None
    Log = None
    value__ = None


class RFmxSpecAnMXDpdMeasurementSampleRateMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdMeasurementSampleRateMode, values: ReferenceWaveform (1), User (0) """
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

    ReferenceWaveform = None
    User = None
    value__ = None


class RFmxSpecAnMXDpdModel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdModel, values: GeneralizedMemoryPolynomial (2), LookupTable (0), MemoryPolynomial (1) """
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

    GeneralizedMemoryPolynomial = None
    LookupTable = None
    MemoryPolynomial = None
    value__ = None


class RFmxSpecAnMXDpdNmseEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdNmseEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdPreDpd(RFmxSpecAnMXSubObject):
    # no doc
    def ApplyPreDpdSignalConditioning(self, selectorString, waveformIn, idleDurationPresent, waveformOut, PAPR):
        """ ApplyPreDpdSignalConditioning(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, waveformIn: ComplexWaveform[ComplexSingle], idleDurationPresent: RFmxSpecAnMXDpdApplyDpdIdleDurationPresent, waveformOut: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle], float) """
        pass

    def GetCarrierBandwidth(self, selectorString, value):
        """ GetCarrierBandwidth(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, float) """
        pass

    def GetCarrierOffset(self, selectorString, value):
        """ GetCarrierOffset(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrEnabled(self, selectorString, value):
        """ GetCfrEnabled(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdPreDpdCfrEnabled) """
        pass

    def GetCfrFilterEnabled(self, selectorString, value):
        """ GetCfrFilterEnabled(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdPreDpdCfrFilterEnabled) """
        pass

    def GetCfrMaximumIterations(self, selectorString, value):
        """ GetCfrMaximumIterations(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, int) """
        pass

    def GetCfrMethod(self, selectorString, value):
        """ GetCfrMethod(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdPreDpdCfrMethod) """
        pass

    def GetCfrNumberOfCarriers(self, selectorString, value):
        """ GetCfrNumberOfCarriers(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, int) """
        pass

    def GetCfrShapingFactor(self, selectorString, value):
        """ GetCfrShapingFactor(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrShapingThreshold(self, selectorString, value):
        """ GetCfrShapingThreshold(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrTargetPapr(self, selectorString, value):
        """ GetCfrTargetPapr(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, float) """
        pass

    def GetCfrWindowLength(self, selectorString, value):
        """ GetCfrWindowLength(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, int) """
        pass

    def GetCfrWindowType(self, selectorString, value):
        """ GetCfrWindowType(self: RFmxSpecAnMXDpdPreDpd, selectorString: str) -> (int, RFmxSpecAnMXDpdPreDpdCfrWindowType) """
        pass

    def SetCarrierBandwidth(self, selectorString, value):
        """ SetCarrierBandwidth(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: float) -> int """
        pass

    def SetCarrierOffset(self, selectorString, value):
        """ SetCarrierOffset(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrEnabled(self, selectorString, value):
        """ SetCfrEnabled(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: RFmxSpecAnMXDpdPreDpdCfrEnabled) -> int """
        pass

    def SetCfrFilterEnabled(self, selectorString, value):
        """ SetCfrFilterEnabled(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: RFmxSpecAnMXDpdPreDpdCfrFilterEnabled) -> int """
        pass

    def SetCfrMaximumIterations(self, selectorString, value):
        """ SetCfrMaximumIterations(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: int) -> int """
        pass

    def SetCfrMethod(self, selectorString, value):
        """ SetCfrMethod(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: RFmxSpecAnMXDpdPreDpdCfrMethod) -> int """
        pass

    def SetCfrNumberOfCarriers(self, selectorString, value):
        """ SetCfrNumberOfCarriers(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: int) -> int """
        pass

    def SetCfrShapingFactor(self, selectorString, value):
        """ SetCfrShapingFactor(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrShapingThreshold(self, selectorString, value):
        """ SetCfrShapingThreshold(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrTargetPapr(self, selectorString, value):
        """ SetCfrTargetPapr(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: float) -> int """
        pass

    def SetCfrWindowLength(self, selectorString, value):
        """ SetCfrWindowLength(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: int) -> int """
        pass

    def SetCfrWindowType(self, selectorString, value):
        """ SetCfrWindowType(self: RFmxSpecAnMXDpdPreDpd, selectorString: str, value: RFmxSpecAnMXDpdPreDpdCfrWindowType) -> int """
        pass


class RFmxSpecAnMXDpdPreDpdCfrEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdPreDpdCfrEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdPreDpdCfrFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdPreDpdCfrFilterEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdPreDpdCfrMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdPreDpdCfrMethod, values: Clipping (0), PeakWindowing (1), Sigmoid (2) """
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

    Clipping = None
    PeakWindowing = None
    Sigmoid = None
    value__ = None


class RFmxSpecAnMXDpdPreDpdCfrWindowType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdPreDpdCfrWindowType, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    value__ = None


class RFmxSpecAnMXDpdReferenceWaveformIdleDurationPresent(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdReferenceWaveformIdleDurationPresent, values: False (0), True (1) """
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


class RFmxSpecAnMXDpdResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAverageGain(self, selectorString, timeout, averageGain):
        """ FetchAverageGain(self: RFmxSpecAnMXDpdResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchDpdPolynomial(self, selectorString, timeout, dpdPolynomial):
        """ FetchDpdPolynomial(self: RFmxSpecAnMXDpdResults, selectorString: str, timeout: float, dpdPolynomial: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchLookupTable(self, selectorString, timeout, inputPowers, complexGains):
        """ FetchLookupTable(self: RFmxSpecAnMXDpdResults, selectorString: str, timeout: float, inputPowers: Array[Single], complexGains: Array[ComplexSingle]) -> (int, Array[Single], Array[ComplexSingle]) """
        pass

    def FetchNmse(self, selectorString, timeout, nmse):
        """ FetchNmse(self: RFmxSpecAnMXDpdResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchProcessedMeanAcquiredWaveform(self, selectorString, timeout, processedMeanAcquiredWaveform):
        """ FetchProcessedMeanAcquiredWaveform(self: RFmxSpecAnMXDpdResults, selectorString: str, timeout: float, processedMeanAcquiredWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    def FetchProcessedReferenceWaveform(self, selectorString, timeout, processedReferenceWaveform):
        """ FetchProcessedReferenceWaveform(self: RFmxSpecAnMXDpdResults, selectorString: str, timeout: float, processedReferenceWaveform: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    def GetAverageGain(self, selectorString, value):
        """ GetAverageGain(self: RFmxSpecAnMXDpdResults, selectorString: str) -> (int, float) """
        pass

    def GetNmse(self, selectorString, value):
        """ GetNmse(self: RFmxSpecAnMXDpdResults, selectorString: str) -> (int, float) """
        pass


class RFmxSpecAnMXDpdSignalType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdSignalType, values: Modulated (0), Tones (1) """
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

    Modulated = None
    Tones = None
    value__ = None


class RFmxSpecAnMXDpdSynchronizationMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdSynchronizationMethod, values: AliasProtected (2), Direct (1) """
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

    AliasProtected = None
    Direct = None
    value__ = None


class RFmxSpecAnMXDpdTargetGainType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXDpdTargetGainType, values: AverageGain (0), LinearRegionGain (1), PeakInputPowerGain (2) """
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

    AverageGain = None
    LinearRegionGain = None
    PeakInputPowerGain = None
    value__ = None


class RFmxSpecAnMXFcnt(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXFcnt) -> RFmxSpecAnMXFcntConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXFcnt) -> RFmxSpecAnMXFcntResults

"""



class RFmxSpecAnMXFcntAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXFcntAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXFcntAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXFcntAveragingType, values: Maximum (3), Mean (6), Minimum (4), MinMax (7) """
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

    Maximum = None
    Mean = None
    Minimum = None
    MinMax = None
    value__ = None


class RFmxSpecAnMXFcntConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXFcntAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXFcntAveragingType) -> int """
        pass

    def ConfigureMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbw, rbwFilterType, rrcAlpha):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, rbw: float, rbwFilterType: RFmxSpecAnMXFcntRbwFilterType, rrcAlpha: float) -> int """
        pass

    def ConfigureThreshold(self, selectorString, thresholdEnabled, thresholdLevel, thresholdType):
        """ ConfigureThreshold(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, thresholdEnabled: RFmxSpecAnMXFcntThresholdEnabled, thresholdLevel: float, thresholdType: RFmxSpecAnMXFcntThresholdType) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, RFmxSpecAnMXFcntAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, RFmxSpecAnMXFcntAveragingType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementInterval(self, selectorString, value):
        """ GetMeasurementInterval(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterRrcAlpha(self, selectorString, value):
        """ GetRbwFilterRrcAlpha(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, RFmxSpecAnMXFcntRbwFilterType) """
        pass

    def GetThresholdEnabled(self, selectorString, value):
        """ GetThresholdEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, RFmxSpecAnMXFcntThresholdEnabled) """
        pass

    def GetThresholdLevel(self, selectorString, value):
        """ GetThresholdLevel(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetThresholdType(self, selectorString, value):
        """ GetThresholdType(self: RFmxSpecAnMXFcntConfiguration, selectorString: str) -> (int, RFmxSpecAnMXFcntThresholdType) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: RFmxSpecAnMXFcntAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: RFmxSpecAnMXFcntAveragingType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementInterval(self, selectorString, value):
        """ SetMeasurementInterval(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterRrcAlpha(self, selectorString, value):
        """ SetRbwFilterRrcAlpha(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: RFmxSpecAnMXFcntRbwFilterType) -> int """
        pass

    def SetThresholdEnabled(self, selectorString, value):
        """ SetThresholdEnabled(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: RFmxSpecAnMXFcntThresholdEnabled) -> int """
        pass

    def SetThresholdLevel(self, selectorString, value):
        """ SetThresholdLevel(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetThresholdType(self, selectorString, value):
        """ SetThresholdType(self: RFmxSpecAnMXFcntConfiguration, selectorString: str, value: RFmxSpecAnMXFcntThresholdType) -> int """
        pass


class RFmxSpecAnMXFcntRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXFcntRbwFilterType, values: Flat (2), Gaussian (1), None (5), Rrc (6), SynchTuned4 (3), SynchTuned5 (4) """
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

    Flat = None
    Gaussian = None
    None = None
    Rrc = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXFcntResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAllanDeviation(self, selectorString, timeout, allanDeviation):
        """ FetchAllanDeviation(self: RFmxSpecAnMXFcntResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchFrequencyTrace(self, selectorString, timeout, frequencyTrace):
        """ FetchFrequencyTrace(self: RFmxSpecAnMXFcntResults, selectorString: str, timeout: float, frequencyTrace: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchMeasurement(self, selectorString, timeout, averageRelativeFrequency, averageAbsoluteFrequency, meanPhase):
        """ FetchMeasurement(self: RFmxSpecAnMXFcntResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchPhaseTrace(self, selectorString, timeout, phaseTrace):
        """ FetchPhaseTrace(self: RFmxSpecAnMXFcntResults, selectorString: str, timeout: float, phaseTrace: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPowerTrace(self, selectorString, timeout, powerTrace):
        """ FetchPowerTrace(self: RFmxSpecAnMXFcntResults, selectorString: str, timeout: float, powerTrace: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def GetAllanDeviation(self, selectorString, value):
        """ GetAllanDeviation(self: RFmxSpecAnMXFcntResults, selectorString: str) -> (int, float) """
        pass

    def GetAverageAbsoluteFrequency(self, selectorString, value):
        """ GetAverageAbsoluteFrequency(self: RFmxSpecAnMXFcntResults, selectorString: str) -> (int, float) """
        pass

    def GetAverageRelativeFrequency(self, selectorString, value):
        """ GetAverageRelativeFrequency(self: RFmxSpecAnMXFcntResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanPhase(self, selectorString, value):
        """ GetMeanPhase(self: RFmxSpecAnMXFcntResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, averageRelativeFrequency, averageAbsoluteFrequency, meanPhase):
        """ Read(self: RFmxSpecAnMXFcntResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass


class RFmxSpecAnMXFcntThresholdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXFcntThresholdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXFcntThresholdType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXFcntThresholdType, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXHarm(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXHarm) -> RFmxSpecAnMXHarmConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXHarm) -> RFmxSpecAnMXHarmResults

"""



class RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXHarmAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXHarmAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None


class RFmxSpecAnMXHarmConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAutoHarmonics(self, selectorString, autoHarmonicsSetupEnabled):
        """ ConfigureAutoHarmonics(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, autoHarmonicsSetupEnabled: RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXHarmAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXHarmAveragingType) -> int """
        pass

    def ConfigureFundamentalMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureFundamentalMeasurementInterval(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureFundamentalRbw(self, selectorString, rbw, rbwFilterType, rrcAlpha):
        """ ConfigureFundamentalRbw(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, rbw: float, rbwFilterType: RFmxSpecAnMXHarmRbwFilterType, rrcAlpha: float) -> int """
        pass

    def ConfigureHarmonic(self, selectorString, harmonicOrder, harmonicBandwidth, harmonicEnabled, harmonicMeasurementInterval):
        """ ConfigureHarmonic(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, harmonicOrder: int, harmonicBandwidth: float, harmonicEnabled: RFmxSpecAnMXHarmHarmonicEnabled, harmonicMeasurementInterval: float) -> int """
        pass

    def ConfigureHarmonicArray(self, selectorString, harmonicOrder, harmonicBandwidth, harmonicEnabled, harmonicMeasurementInterval):
        """ ConfigureHarmonicArray(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, harmonicOrder: Array[int], harmonicBandwidth: Array[float], harmonicEnabled: Array[RFmxSpecAnMXHarmHarmonicEnabled], harmonicMeasurementInterval: Array[float]) -> int """
        pass

    def ConfigureNumberOfHarmonics(self, selectorString, numberOfHarmonics):
        """ ConfigureNumberOfHarmonics(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, numberOfHarmonics: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAutoSetupEnabled(self, selectorString, value):
        """ GetAutoSetupEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmAveragingType) """
        pass

    def GetFundamentalMeasurementInterval(self, selectorString, value):
        """ GetFundamentalMeasurementInterval(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFundamentalRbwFilterAlpha(self, selectorString, value):
        """ GetFundamentalRbwFilterAlpha(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFundamentalRbwFilterBandwidth(self, selectorString, value):
        """ GetFundamentalRbwFilterBandwidth(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFundamentalRbwFilterType(self, selectorString, value):
        """ GetFundamentalRbwFilterType(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmRbwFilterType) """
        pass

    def GetHarmonicBandwidth(self, selectorString, value):
        """ GetHarmonicBandwidth(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetHarmonicEnabled(self, selectorString, value):
        """ GetHarmonicEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmHarmonicEnabled) """
        pass

    def GetHarmonicMeasurementInterval(self, selectorString, value):
        """ GetHarmonicMeasurementInterval(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetHarmonicOrder(self, selectorString, value):
        """ GetHarmonicOrder(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmMeasurementMethod) """
        pass

    def GetNoiseCompensationEnabled(self, selectorString, value):
        """ GetNoiseCompensationEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, RFmxSpecAnMXHarmNoiseCompensationEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfHarmonics(self, selectorString, value):
        """ GetNumberOfHarmonics(self: RFmxSpecAnMXHarmConfiguration, selectorString: str) -> (int, int) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAutoSetupEnabled(self, selectorString, value):
        """ SetAutoSetupEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmAutoHarmonicsSetupEnabled) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmAveragingType) -> int """
        pass

    def SetFundamentalMeasurementInterval(self, selectorString, value):
        """ SetFundamentalMeasurementInterval(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFundamentalRbwFilterAlpha(self, selectorString, value):
        """ SetFundamentalRbwFilterAlpha(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFundamentalRbwFilterBandwidth(self, selectorString, value):
        """ SetFundamentalRbwFilterBandwidth(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFundamentalRbwFilterType(self, selectorString, value):
        """ SetFundamentalRbwFilterType(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmRbwFilterType) -> int """
        pass

    def SetHarmonicBandwidth(self, selectorString, value):
        """ SetHarmonicBandwidth(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetHarmonicEnabled(self, selectorString, value):
        """ SetHarmonicEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmHarmonicEnabled) -> int """
        pass

    def SetHarmonicMeasurementInterval(self, selectorString, value):
        """ SetHarmonicMeasurementInterval(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetHarmonicOrder(self, selectorString, value):
        """ SetHarmonicOrder(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmMeasurementMethod) -> int """
        pass

    def SetNoiseCompensationEnabled(self, selectorString, value):
        """ SetNoiseCompensationEnabled(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: RFmxSpecAnMXHarmNoiseCompensationEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfHarmonics(self, selectorString, value):
        """ SetNumberOfHarmonics(self: RFmxSpecAnMXHarmConfiguration, selectorString: str, value: int) -> int """
        pass


class RFmxSpecAnMXHarmHarmonicEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmHarmonicEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXHarmMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmMeasurementMethod, values: DynamicRange (2), TimeDomain (0) """
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

    DynamicRange = None
    TimeDomain = None
    value__ = None


class RFmxSpecAnMXHarmNoiseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmNoiseCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXHarmRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXHarmRbwFilterType, values: Flat (2), Gaussian (1), None (5), Rrc (6), SynchTuned4 (3), SynchTuned5 (4) """
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

    Flat = None
    Gaussian = None
    None = None
    Rrc = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXHarmResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchHarmonicMeasurement(self, selectorString, timeout, averageRelativePower, averageAbsolutePower, rbw, frequency):
        """ FetchHarmonicMeasurement(self: RFmxSpecAnMXHarmResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchHarmonicMeasurementArray(self, selectorString, timeout, averageRelativePower, averageAbsolutePower, rbw, frequency):
        """ FetchHarmonicMeasurementArray(self: RFmxSpecAnMXHarmResults, selectorString: str, timeout: float, averageRelativePower: Array[float], averageAbsolutePower: Array[float], rbw: Array[float], frequency: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchHarmonicPowerTrace(self, selectorString, timeout, power):
        """ FetchHarmonicPowerTrace(self: RFmxSpecAnMXHarmResults, selectorString: str, timeout: float, power: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchTotalHarmonicDistortion(self, selectorString, timeout, totalHarmonicDistortion, averageFundamentalPower, fundamentalFrequency):
        """ FetchTotalHarmonicDistortion(self: RFmxSpecAnMXHarmResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def GetAverageFundamentalPower(self, selectorString, value):
        """ GetAverageFundamentalPower(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def GetFundamentalFrequency(self, selectorString, value):
        """ GetFundamentalFrequency(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def GetHarmonicAverageAbsolutePower(self, selectorString, value):
        """ GetHarmonicAverageAbsolutePower(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def GetHarmonicAverageRelativePower(self, selectorString, value):
        """ GetHarmonicAverageRelativePower(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def GetHarmonicFrequency(self, selectorString, value):
        """ GetHarmonicFrequency(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def GetHarmonicRbw(self, selectorString, value):
        """ GetHarmonicRbw(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalHarmonicDistortion(self, selectorString, value):
        """ GetTotalHarmonicDistortion(self: RFmxSpecAnMXHarmResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, totalHarmonicDistortion, averageFundamentalPower):
        """ Read(self: RFmxSpecAnMXHarmResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass


class RFmxSpecAnMXIM(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXIM) -> RFmxSpecAnMXIMConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXIM) -> RFmxSpecAnMXIMResults

"""



class RFmxSpecAnMXIMAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXIMAutoIntermodsSetupEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMAutoIntermodsSetupEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXIMAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXIMAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None


class RFmxSpecAnMXIMConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAutoIntermodsSetup(self, selectorString, autoIntermodsSetupEnabled, maximumIntermodOrder):
        """ ConfigureAutoIntermodsSetup(self: RFmxSpecAnMXIMConfiguration, selectorString: str, autoIntermodsSetupEnabled: RFmxSpecAnMXIMAutoIntermodsSetupEnabled, maximumIntermodOrder: int) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXIMConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXIMAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXIMAveragingType) -> int """
        pass

    def ConfigureFft(self, selectorString, fftWindow, fftPadding):
        """ ConfigureFft(self: RFmxSpecAnMXIMConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXIMFftWindow, fftPadding: float) -> int """
        pass

    def ConfigureFrequencyDefinition(self, selectorString, frequencyDefinition):
        """ ConfigureFrequencyDefinition(self: RFmxSpecAnMXIMConfiguration, selectorString: str, frequencyDefinition: RFmxSpecAnMXIMFrequencyDefinition) -> int """
        pass

    def ConfigureFundamentalTones(self, selectorString, lowerToneFrequency, upperToneFrequency):
        """ ConfigureFundamentalTones(self: RFmxSpecAnMXIMConfiguration, selectorString: str, lowerToneFrequency: float, upperToneFrequency: float) -> int """
        pass

    def ConfigureIntermod(self, selectorString, intermodOrder, lowerIntermodFrequency, upperIntermodFrequency, intermodSide, intermodEnabled):
        """ ConfigureIntermod(self: RFmxSpecAnMXIMConfiguration, selectorString: str, intermodOrder: int, lowerIntermodFrequency: float, upperIntermodFrequency: float, intermodSide: RFmxSpecAnMXIMIntermodSide, intermodEnabled: RFmxSpecAnMXIMIntermodEnabled) -> int """
        pass

    def ConfigureIntermodArray(self, selectorString, intermodOrder, lowerIntermodFrequency, upperIntermodFrequency, intermodSide, intermodEnabled):
        """ ConfigureIntermodArray(self: RFmxSpecAnMXIMConfiguration, selectorString: str, intermodOrder: Array[int], lowerIntermodFrequency: Array[float], upperIntermodFrequency: Array[float], intermodSide: Array[RFmxSpecAnMXIMIntermodSide], intermodEnabled: Array[RFmxSpecAnMXIMIntermodEnabled]) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxSpecAnMXIMConfiguration, selectorString: str, measurementMethod: RFmxSpecAnMXIMMeasurementMethod) -> int """
        pass

    def ConfigureNumberOfIntermods(self, selectorString, numberOfIntermods):
        """ ConfigureNumberOfIntermods(self: RFmxSpecAnMXIMConfiguration, selectorString: str, numberOfIntermods: int) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXIMConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXIMRbwFilterAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXIMRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxSpecAnMXIMConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXIMSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMAmplitudeCorrectionType) """
        pass

    def GetAutoIntermodsSetupEnabled(self, selectorString, value):
        """ GetAutoIntermodsSetupEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMAutoIntermodsSetupEnabled) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMAveragingType) """
        pass

    def GetFarIFOutputPowerOffset(self, selectorString, value):
        """ GetFarIFOutputPowerOffset(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftPadding(self, selectorString, value):
        """ GetFftPadding(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMFftWindow) """
        pass

    def GetFrequencyDefinition(self, selectorString, value):
        """ GetFrequencyDefinition(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMFrequencyDefinition) """
        pass

    def GetFundamentalLowerToneFrequency(self, selectorString, value):
        """ GetFundamentalLowerToneFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFundamentalUpperToneFrequency(self, selectorString, value):
        """ GetFundamentalUpperToneFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ GetIFOutputPowerOffsetAuto(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMIFOutputPowerOffsetAuto) """
        pass

    def GetIntermodEnabled(self, selectorString, value):
        """ GetIntermodEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMIntermodEnabled) """
        pass

    def GetIntermodOrder(self, selectorString, value):
        """ GetIntermodOrder(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetIntermodSide(self, selectorString, value):
        """ GetIntermodSide(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMIntermodSide) """
        pass

    def GetLocalPeakSearchEnabled(self, selectorString, value):
        """ GetLocalPeakSearchEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMLocalPeakSearchEnabled) """
        pass

    def GetLowerIntermodFrequency(self, selectorString, value):
        """ GetLowerIntermodFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMaximumIntermodOrder(self, selectorString, value):
        """ GetMaximumIntermodOrder(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMMeasurementMethod) """
        pass

    def GetNearIFOutputPowerOffset(self, selectorString, value):
        """ GetNearIFOutputPowerOffset(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfIntermods(self, selectorString, value):
        """ GetNumberOfIntermods(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMRbwFilterAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMRbwFilterType) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIMSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetUpperIntermodFrequency(self, selectorString, value):
        """ GetUpperIntermodFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMAmplitudeCorrectionType) -> int """
        pass

    def SetAutoIntermodsSetupEnabled(self, selectorString, value):
        """ SetAutoIntermodsSetupEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMAutoIntermodsSetupEnabled) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMAveragingType) -> int """
        pass

    def SetFarIFOutputPowerOffset(self, selectorString, value):
        """ SetFarIFOutputPowerOffset(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftPadding(self, selectorString, value):
        """ SetFftPadding(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMFftWindow) -> int """
        pass

    def SetFrequencyDefinition(self, selectorString, value):
        """ SetFrequencyDefinition(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMFrequencyDefinition) -> int """
        pass

    def SetFundamentalLowerToneFrequency(self, selectorString, value):
        """ SetFundamentalLowerToneFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFundamentalUpperToneFrequency(self, selectorString, value):
        """ SetFundamentalUpperToneFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ SetIFOutputPowerOffsetAuto(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMIFOutputPowerOffsetAuto) -> int """
        pass

    def SetIntermodEnabled(self, selectorString, value):
        """ SetIntermodEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMIntermodEnabled) -> int """
        pass

    def SetIntermodOrder(self, selectorString, value):
        """ SetIntermodOrder(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetIntermodSide(self, selectorString, value):
        """ SetIntermodSide(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMIntermodSide) -> int """
        pass

    def SetLocalPeakSearchEnabled(self, selectorString, value):
        """ SetLocalPeakSearchEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMLocalPeakSearchEnabled) -> int """
        pass

    def SetLowerIntermodFrequency(self, selectorString, value):
        """ SetLowerIntermodFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMaximumIntermodOrder(self, selectorString, value):
        """ SetMaximumIntermodOrder(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMMeasurementMethod) -> int """
        pass

    def SetNearIFOutputPowerOffset(self, selectorString, value):
        """ SetNearIFOutputPowerOffset(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfIntermods(self, selectorString, value):
        """ SetNumberOfIntermods(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMRbwFilterAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMRbwFilterType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: RFmxSpecAnMXIMSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetUpperIntermodFrequency(self, selectorString, value):
        """ SetUpperIntermodFrequency(self: RFmxSpecAnMXIMConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXIMFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXIMFrequencyDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMFrequencyDefinition, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXIMIFOutputPowerOffsetAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMIFOutputPowerOffsetAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXIMIntermodEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMIntermodEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXIMIntermodSide(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMIntermodSide, values: Both (2), Lower (0), Upper (1) """
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

    Both = None
    Lower = None
    Upper = None
    value__ = None


class RFmxSpecAnMXIMLocalPeakSearchEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMLocalPeakSearchEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXIMMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMMeasurementMethod, values: DynamicRange (1), Normal (0), Segmented (2) """
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

    DynamicRange = None
    Normal = None
    Segmented = None
    value__ = None


class RFmxSpecAnMXIMRbwFilterAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMRbwFilterAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXIMRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXIMResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchFundamentalMeasurement(self, selectorString, timeout, lowerTonePower, upperTonePower):
        """ FetchFundamentalMeasurement(self: RFmxSpecAnMXIMResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchInterceptPower(self, selectorString, timeout, intermodOrder, worstCaseOutputInterceptPower, lowerOutputInterceptPower, upperOutputInterceptPower):
        """ FetchInterceptPower(self: RFmxSpecAnMXIMResults, selectorString: str, timeout: float) -> (int, int, float, float, float) """
        pass

    def FetchInterceptPowerArray(self, selectorString, timeout, intermodOrder, worstCaseOutputInterceptPower, lowerOutputInterceptPower, upperOutputInterceptPower):
        """ FetchInterceptPowerArray(self: RFmxSpecAnMXIMResults, selectorString: str, timeout: float, intermodOrder: Array[int], worstCaseOutputInterceptPower: Array[float], lowerOutputInterceptPower: Array[float], upperOutputInterceptPower: Array[float]) -> (int, Array[int], Array[float], Array[float], Array[float]) """
        pass

    def FetchIntermodMeasurement(self, selectorString, timeout, intermodOrder, lowerIntermodPower, upperIntermodPower):
        """ FetchIntermodMeasurement(self: RFmxSpecAnMXIMResults, selectorString: str, timeout: float) -> (int, int, float, float) """
        pass

    def FetchIntermodMeasurementArray(self, selectorString, timeout, intermodOrder, lowerIntermodPower, upperIntermodPower):
        """ FetchIntermodMeasurementArray(self: RFmxSpecAnMXIMResults, selectorString: str, timeout: float, intermodOrder: Array[int], lowerIntermodPower: Array[float], upperIntermodPower: Array[float]) -> (int, Array[int], Array[float], Array[float]) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrumIndex, spectrum):
        """ FetchSpectrum(self: RFmxSpecAnMXIMResults, selectorString: str, timeout: float, spectrumIndex: int, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def GetFundamentalLowerTonePower(self, selectorString, value):
        """ GetFundamentalLowerTonePower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass

    def GetFundamentalUpperTonePower(self, selectorString, value):
        """ GetFundamentalUpperTonePower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass

    def GetIntermodOrder(self, selectorString, value):
        """ GetIntermodOrder(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, int) """
        pass

    def GetLowerIntermodPower(self, selectorString, value):
        """ GetLowerIntermodPower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOutputInterceptPower(self, selectorString, value):
        """ GetLowerOutputInterceptPower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperIntermodPower(self, selectorString, value):
        """ GetUpperIntermodPower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOutputInterceptPower(self, selectorString, value):
        """ GetUpperOutputInterceptPower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass

    def GetWorstCaseOutputInterceptPower(self, selectorString, value):
        """ GetWorstCaseOutputInterceptPower(self: RFmxSpecAnMXIMResults, selectorString: str) -> (int, float) """
        pass


class RFmxSpecAnMXIMSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIMSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXIQ(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXIQ) -> RFmxSpecAnMXIQConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXIQ) -> RFmxSpecAnMXIQResults

"""



class RFmxSpecAnMXIQBandwidthAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIQBandwidthAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXIQConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAcquisition(self, selectorString, sampleRate, numberOfRecords, acquisitionTime, pretriggerTime):
        """ ConfigureAcquisition(self: RFmxSpecAnMXIQConfiguration, selectorString: str, sampleRate: float, numberOfRecords: int, acquisitionTime: float, pretriggerTime: float) -> int """
        pass

    def ConfigureBandwidth(self, selectorString, bandwidthAuto, bandwidth):
        """ ConfigureBandwidth(self: RFmxSpecAnMXIQConfiguration, selectorString: str, bandwidthAuto: RFmxSpecAnMXIQBandwidthAuto, bandwidth: float) -> int """
        pass

    def GetAcquisitionTime(self, selectorString, value):
        """ GetAcquisitionTime(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetBandwidth(self, selectorString, value):
        """ GetBandwidth(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetBandwidthAuto(self, selectorString, value):
        """ GetBandwidthAuto(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIQBandwidthAuto) """
        pass

    def GetDeleteRecordOnFetch(self, selectorString, value):
        """ GetDeleteRecordOnFetch(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, RFmxSpecAnMXIQDeleteRecordOnFetch) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfRecords(self, selectorString, value):
        """ GetNumberOfRecords(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetPretriggerTime(self, selectorString, value):
        """ GetPretriggerTime(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSampleRate(self, selectorString, value):
        """ GetSampleRate(self: RFmxSpecAnMXIQConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAcquisitionTime(self, selectorString, value):
        """ SetAcquisitionTime(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetBandwidth(self, selectorString, value):
        """ SetBandwidth(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetBandwidthAuto(self, selectorString, value):
        """ SetBandwidthAuto(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: RFmxSpecAnMXIQBandwidthAuto) -> int """
        pass

    def SetDeleteRecordOnFetch(self, selectorString, value):
        """ SetDeleteRecordOnFetch(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: RFmxSpecAnMXIQDeleteRecordOnFetch) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfRecords(self, selectorString, value):
        """ SetNumberOfRecords(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetPretriggerTime(self, selectorString, value):
        """ SetPretriggerTime(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSampleRate(self, selectorString, value):
        """ SetSampleRate(self: RFmxSpecAnMXIQConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXIQDeleteOnFetch(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIQDeleteOnFetch, values: Default (0), False (2), True (1) """
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

    Default = None
    False = None
    True = None
    value__ = None


class RFmxSpecAnMXIQDeleteRecordOnFetch(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIQDeleteRecordOnFetch, values: False (0), True (1) """
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


class RFmxSpecAnMXIQPowerEdgeTriggerLevelType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIQPowerEdgeTriggerLevelType, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXIQPowerEdgeTriggerSlope(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXIQPowerEdgeTriggerSlope, values: Falling (1), Rising (0) """
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

    Falling = None
    Rising = None
    value__ = None


class RFmxSpecAnMXIQResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchData(self, selectorString, timeout, recordToFetch, samplesToRead, data):
        """ FetchData(self: RFmxSpecAnMXIQResults, selectorString: str, timeout: float, recordToFetch: int, samplesToRead: Int64, data: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    def FetchDataOverrideBehavior(self, selectorString, timeout, recordToFetch, samplesToRead, deleteOnFetch, data):
        """ FetchDataOverrideBehavior(self: RFmxSpecAnMXIQResults, selectorString: str, timeout: float, recordToFetch: int, samplesToRead: Int64, deleteOnFetch: RFmxSpecAnMXIQDeleteOnFetch, data: ComplexWaveform[ComplexSingle]) -> (int, ComplexWaveform[ComplexSingle]) """
        pass

    def GetRecordsDone(self, selectorString, recordsDone):
        """ GetRecordsDone(self: RFmxSpecAnMXIQResults, selectorString: str) -> (int, int) """
        pass


class RFmxSpecAnMXLimitedConfigurationChange(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXLimitedConfigurationChange, values: Disabled (0), Frequency (2), FrequencyAndReferenceLevel (4), NoChange (1), ReferenceLevel (3), SelectedPortsFrequencyAndReferenceLevel (5) """
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
    Frequency = None
    FrequencyAndReferenceLevel = None
    NoChange = None
    ReferenceLevel = None
    SelectedPortsFrequencyAndReferenceLevel = None
    value__ = None


class RFmxSpecAnMXMarker(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXMarker) -> RFmxSpecAnMXMarkerConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXMarker) -> RFmxSpecAnMXMarkerResults

"""



class RFmxSpecAnMXMarkerConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureNumberOfMarkers(self, selectorString, numberOfMarkers):
        """ ConfigureNumberOfMarkers(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, numberOfMarkers: int) -> int """
        pass

    def ConfigurePeakExcursion(self, selectorString, peakExcursionEnabled, peakExcursion):
        """ ConfigurePeakExcursion(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, peakExcursionEnabled: RFmxSpecAnMXMarkerPeakExcursionEnabled, peakExcursion: float) -> int """
        pass

    def ConfigureReferenceMarker(self, selectorString, referenceMarker):
        """ ConfigureReferenceMarker(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, referenceMarker: int) -> int """
        pass

    def ConfigureThreshold(self, selectorString, thresholdEnabled, threshold):
        """ ConfigureThreshold(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, thresholdEnabled: RFmxSpecAnMXMarkerThresholdEnabled, threshold: float) -> int """
        pass

    def ConfigureTrace(self, selectorString, trace):
        """ ConfigureTrace(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, trace: RFmxSpecAnMXMarkerTrace) -> int """
        pass

    def ConfigureType(self, selectorString, markerType):
        """ ConfigureType(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, markerType: RFmxSpecAnMXMarkerType) -> int """
        pass

    def ConfigureXLocation(self, selectorString, markerXLocation):
        """ ConfigureXLocation(self: RFmxSpecAnMXMarkerConfiguration, selectorString: str, markerXLocation: float) -> int """
        pass


class RFmxSpecAnMXMarkerNextPeak(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXMarkerNextPeak, values: NextHighest (0), NextLeft (1), NextRight (2) """
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

    NextHighest = None
    NextLeft = None
    NextRight = None
    value__ = None


class RFmxSpecAnMXMarkerPeakExcursionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXMarkerPeakExcursionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXMarkerResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchXY(self, selectorString, markerXLocation, markerYLocation):
        """ FetchXY(self: RFmxSpecAnMXMarkerResults, selectorString: str) -> (int, float, float) """
        pass

    def NextPeak(self, selectorString, nextPeak, nextPeakFound):
        """ NextPeak(self: RFmxSpecAnMXMarkerResults, selectorString: str, nextPeak: RFmxSpecAnMXMarkerNextPeak) -> (int, bool) """
        pass

    def PeakSearch(self, selectorString, numberOfPeaks):
        """ PeakSearch(self: RFmxSpecAnMXMarkerResults, selectorString: str) -> (int, int) """
        pass


class RFmxSpecAnMXMarkerThresholdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXMarkerThresholdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXMarkerTrace(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXMarkerTrace, values: AcpSpectrum (0), CcdfGaussianProbabilitiesTrace (1), CcdfProbabilitiesTrace (2), ChpSpectrum (3), FcntPowerTrace (4), ObwSpectrum (5), SemSpectrum (6), Spectrum (7), TxpPowerTrace (8) """
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

    AcpSpectrum = None
    CcdfGaussianProbabilitiesTrace = None
    CcdfProbabilitiesTrace = None
    ChpSpectrum = None
    FcntPowerTrace = None
    ObwSpectrum = None
    SemSpectrum = None
    Spectrum = None
    TxpPowerTrace = None
    value__ = None


class RFmxSpecAnMXMarkerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXMarkerType, values: Delta (3), Normal (1), Off (0) """
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

    Delta = None
    Normal = None
    Off = None
    value__ = None


class RFmxSpecAnMXMeasurementTypes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RFmxSpecAnMXMeasurementTypes, values: Acp (1), Ampm (1024), Ccdf (2), Chp (4), Dpd (2048), Fcnt (8), Harm (16), IM (8192), IQ (4096), NF (16384), Obw (32), Pavt (65536), PhaseNoise (32768), Sem (64), Spectrum (128), Spur (256), Txp (512) """
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

    Acp = None
    Ampm = None
    Ccdf = None
    Chp = None
    Dpd = None
    Fcnt = None
    Harm = None
    IM = None
    IQ = None
    NF = None
    Obw = None
    Pavt = None
    PhaseNoise = None
    Sem = None
    Spectrum = None
    Spur = None
    Txp = None
    value__ = None


class RFmxSpecAnMXNF(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXNF) -> RFmxSpecAnMXNFConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXNF) -> RFmxSpecAnMXNFResults

"""



class RFmxSpecAnMXNFAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXNFCalibrationDataValid(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFCalibrationDataValid, values: False (0), True (1) """
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


class RFmxSpecAnMXNFCalibrationLossCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFCalibrationLossCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXNFColdSourceMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFColdSourceMode, values: Calibrate (1), Measure (0) """
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

    Calibrate = None
    Measure = None
    value__ = None


class RFmxSpecAnMXNFConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ClearCalibrationDatabase(self, calibrationSetupId):
        """ ClearCalibrationDatabase(self: RFmxSpecAnMXNFConfiguration, calibrationSetupId: str) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxSpecAnMXNFConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXNFAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureCalibrationLoss(self, selectorString, calibrationLossCompensationEnabled, calibrationLossFrequency, calibrationLoss, calibrationLossTemperature):
        """ ConfigureCalibrationLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, calibrationLossCompensationEnabled: RFmxSpecAnMXNFCalibrationLossCompensationEnabled, calibrationLossFrequency: Array[float], calibrationLoss: Array[float], calibrationLossTemperature: float) -> int """
        pass

    def ConfigureColdSourceDutSParameters(self, selectorString, dutSParametersFrequency, dutS21, dutS12, dutS11, dutS22):
        """ ConfigureColdSourceDutSParameters(self: RFmxSpecAnMXNFConfiguration, selectorString: str, dutSParametersFrequency: Array[float], dutS21: Array[float], dutS12: Array[float], dutS11: Array[float], dutS22: Array[float]) -> int """
        pass

    def ConfigureColdSourceInputTermination(self, selectorString, terminationVswr, terminationVswrFrequency, terminationTemperature):
        """ ConfigureColdSourceInputTermination(self: RFmxSpecAnMXNFConfiguration, selectorString: str, terminationVswr: Array[float], terminationVswrFrequency: Array[float], terminationTemperature: float) -> int """
        pass

    def ConfigureColdSourceMode(self, selectorString, coldSourceMode):
        """ ConfigureColdSourceMode(self: RFmxSpecAnMXNFConfiguration, selectorString: str, coldSourceMode: RFmxSpecAnMXNFColdSourceMode) -> int """
        pass

    def ConfigureDutInputLoss(self, selectorString, dutInputLossCompensationEnabled, dutInputLossFrequency, dutInputLoss, dutInputLossTemperature):
        """ ConfigureDutInputLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, dutInputLossCompensationEnabled: RFmxSpecAnMXNFDutInputLossCompensationEnabled, dutInputLossFrequency: Array[float], dutInputLoss: Array[float], dutInputLossTemperature: float) -> int """
        pass

    def ConfigureDutOutputLoss(self, selectorString, dutOutputLossCompensationEnabled, dutOutputLossFrequency, dutOutputLoss, dutOutputLossTemperature):
        """ ConfigureDutOutputLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, dutOutputLossCompensationEnabled: RFmxSpecAnMXNFDutOutputLossCompensationEnabled, dutOutputLossFrequency: Array[float], dutOutputLoss: Array[float], dutOutputLossTemperature: float) -> int """
        pass

    def ConfigureFrequencyList(self, selectorString, frequencyList):
        """ ConfigureFrequencyList(self: RFmxSpecAnMXNFConfiguration, selectorString: str, frequencyList: Array[float]) -> int """
        pass

    def ConfigureFrequencyListStartStopPoints(self, selectorString, startFrequency, stopFrequency, numberOfPoints):
        """ ConfigureFrequencyListStartStopPoints(self: RFmxSpecAnMXNFConfiguration, selectorString: str, startFrequency: float, stopFrequency: float, numberOfPoints: int) -> int """
        pass

    def ConfigureFrequencyListStartStopStep(self, selectorString, startFrequency, stopFrequency, stepSize):
        """ ConfigureFrequencyListStartStopStep(self: RFmxSpecAnMXNFConfiguration, selectorString: str, startFrequency: float, stopFrequency: float, stepSize: float) -> int """
        pass

    def ConfigureMeasurementBandwidth(self, selectorString, measurementBandwidth):
        """ ConfigureMeasurementBandwidth(self: RFmxSpecAnMXNFConfiguration, selectorString: str, measurementBandwidth: float) -> int """
        pass

    def ConfigureMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXNFConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxSpecAnMXNFConfiguration, selectorString: str, measurementMethod: RFmxSpecAnMXNFMeasurementMethod) -> int """
        pass

    def ConfigureYFactorMode(self, selectorString, yFactorMode):
        """ ConfigureYFactorMode(self: RFmxSpecAnMXNFConfiguration, selectorString: str, yFactorMode: RFmxSpecAnMXNFYFactorMode) -> int """
        pass

    def ConfigureYFactorNoiseSourceEnr(self, selectorString, enrFrequency, enr, coldTemperature, offTemperature):
        """ ConfigureYFactorNoiseSourceEnr(self: RFmxSpecAnMXNFConfiguration, selectorString: str, enrFrequency: Array[float], enr: Array[float], coldTemperature: float, offTemperature: float) -> int """
        pass

    def ConfigureYFactorNoiseSourceLoss(self, selectorString, noiseSourceLossCompensationEnabled, noiseSourceLossFrequency, noiseSourceLoss, noiseSourceLossTemperature):
        """ ConfigureYFactorNoiseSourceLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, noiseSourceLossCompensationEnabled: RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled, noiseSourceLossFrequency: Array[float], noiseSourceLoss: Array[float], noiseSourceLossTemperature: float) -> int """
        pass

    def ConfigureYFactorNoiseSourceSettlingTime(self, selectorString, settlingTime):
        """ ConfigureYFactorNoiseSourceSettlingTime(self: RFmxSpecAnMXNFConfiguration, selectorString: str, settlingTime: float) -> int """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFAveragingEnabled) """
        pass

    def GetCalibrationLoss(self, selectorString, value):
        """ GetCalibrationLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetCalibrationLossCompensationEnabled(self, selectorString, value):
        """ GetCalibrationLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFCalibrationLossCompensationEnabled) """
        pass

    def GetCalibrationLossFrequency(self, selectorString, value):
        """ GetCalibrationLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetCalibrationLossTemperature(self, selectorString, value):
        """ GetCalibrationLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCalibrationSetupId(self, selectorString, value):
        """ GetCalibrationSetupId(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, str) """
        pass

    def GetColdSourceDutS11(self, selectorString, value):
        """ GetColdSourceDutS11(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceDutS12(self, selectorString, value):
        """ GetColdSourceDutS12(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceDutS21(self, selectorString, value):
        """ GetColdSourceDutS21(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceDutS22(self, selectorString, value):
        """ GetColdSourceDutS22(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceDutSParametersFrequency(self, selectorString, value):
        """ GetColdSourceDutSParametersFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceInputTerminationTemperature(self, selectorString, value):
        """ GetColdSourceInputTerminationTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetColdSourceInputTerminationVswr(self, selectorString, value):
        """ GetColdSourceInputTerminationVswr(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceInputTerminationVswrFrequency(self, selectorString, value):
        """ GetColdSourceInputTerminationVswrFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourceMode(self, selectorString, value):
        """ GetColdSourceMode(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFColdSourceMode) """
        pass

    def GetDeviceTemperatureTolerance(self, selectorString, value):
        """ GetDeviceTemperatureTolerance(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDutInputLoss(self, selectorString, value):
        """ GetDutInputLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutInputLossCompensationEnabled(self, selectorString, value):
        """ GetDutInputLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFDutInputLossCompensationEnabled) """
        pass

    def GetDutInputLossFrequency(self, selectorString, value):
        """ GetDutInputLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutInputLossTemperature(self, selectorString, value):
        """ GetDutInputLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDutOutputLoss(self, selectorString, value):
        """ GetDutOutputLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutOutputLossCompensationEnabled(self, selectorString, value):
        """ GetDutOutputLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFDutOutputLossCompensationEnabled) """
        pass

    def GetDutOutputLossFrequency(self, selectorString, value):
        """ GetDutOutputLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutOutputLossTemperature(self, selectorString, value):
        """ GetDutOutputLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDutType(self, selectorString, value):
        """ GetDutType(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFDutType) """
        pass

    def GetExternalPreampFrequency(self, selectorString, value):
        """ GetExternalPreampFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetExternalPreampGain(self, selectorString, value):
        """ GetExternalPreampGain(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetExternalPreampPresent(self, selectorString, value):
        """ GetExternalPreampPresent(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFExternalPreampPresent) """
        pass

    def GetFrequencyConverterFrequencyContext(self, selectorString, value):
        """ GetFrequencyConverterFrequencyContext(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFFrequencyConverterFrequencyContext) """
        pass

    def GetFrequencyConverterImageRejection(self, selectorString, value):
        """ GetFrequencyConverterImageRejection(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyConverterLOFrequency(self, selectorString, value):
        """ GetFrequencyConverterLOFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyConverterSideband(self, selectorString, value):
        """ GetFrequencyConverterSideband(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFFrequencyConverterSideband) """
        pass

    def GetFrequencyList(self, selectorString, value):
        """ GetFrequencyList(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetMeasurementBandwidth(self, selectorString, value):
        """ GetMeasurementBandwidth(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementInterval(self, selectorString, value):
        """ GetMeasurementInterval(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFMeasurementMethod) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetYFactorMode(self, selectorString, value):
        """ GetYFactorMode(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFYFactorMode) """
        pass

    def GetYFactorNoiseSourceColdTemperature(self, selectorString, value):
        """ GetYFactorNoiseSourceColdTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetYFactorNoiseSourceEnr(self, selectorString, value):
        """ GetYFactorNoiseSourceEnr(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetYFactorNoiseSourceEnrFrequency(self, selectorString, value):
        """ GetYFactorNoiseSourceEnrFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetYFactorNoiseSourceLoss(self, selectorString, value):
        """ GetYFactorNoiseSourceLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetYFactorNoiseSourceLossCompensationEnabled(self, selectorString, value):
        """ GetYFactorNoiseSourceLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled) """
        pass

    def GetYFactorNoiseSourceLossFrequency(self, selectorString, value):
        """ GetYFactorNoiseSourceLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetYFactorNoiseSourceLossTemperature(self, selectorString, value):
        """ GetYFactorNoiseSourceLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetYFactorNoiseSourceOffTemperature(self, selectorString, value):
        """ GetYFactorNoiseSourceOffTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetYFactorNoiseSourceSettlingTime(self, selectorString, value):
        """ GetYFactorNoiseSourceSettlingTime(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, float) """
        pass

    def RecommendReferenceLevel(self, selectorString, dutMaxGain, dutMaxNoiseFigure, referenceLevel):
        """ RecommendReferenceLevel(self: RFmxSpecAnMXNFConfiguration, selectorString: str, dutMaxGain: float, dutMaxNoiseFigure: float) -> (int, float) """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFAveragingEnabled) -> int """
        pass

    def SetCalibrationLoss(self, selectorString, value):
        """ SetCalibrationLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetCalibrationLossCompensationEnabled(self, selectorString, value):
        """ SetCalibrationLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFCalibrationLossCompensationEnabled) -> int """
        pass

    def SetCalibrationLossFrequency(self, selectorString, value):
        """ SetCalibrationLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetCalibrationLossTemperature(self, selectorString, value):
        """ SetCalibrationLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCalibrationSetupId(self, selectorString, value):
        """ SetCalibrationSetupId(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: str) -> int """
        pass

    def SetColdSourceDutS11(self, selectorString, value):
        """ SetColdSourceDutS11(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceDutS12(self, selectorString, value):
        """ SetColdSourceDutS12(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceDutS21(self, selectorString, value):
        """ SetColdSourceDutS21(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceDutS22(self, selectorString, value):
        """ SetColdSourceDutS22(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceDutSParametersFrequency(self, selectorString, value):
        """ SetColdSourceDutSParametersFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceInputTerminationTemperature(self, selectorString, value):
        """ SetColdSourceInputTerminationTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetColdSourceInputTerminationVswr(self, selectorString, value):
        """ SetColdSourceInputTerminationVswr(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceInputTerminationVswrFrequency(self, selectorString, value):
        """ SetColdSourceInputTerminationVswrFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetColdSourceMode(self, selectorString, value):
        """ SetColdSourceMode(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFColdSourceMode) -> int """
        pass

    def SetDeviceTemperatureTolerance(self, selectorString, value):
        """ SetDeviceTemperatureTolerance(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetDutInputLoss(self, selectorString, value):
        """ SetDutInputLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetDutInputLossCompensationEnabled(self, selectorString, value):
        """ SetDutInputLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFDutInputLossCompensationEnabled) -> int """
        pass

    def SetDutInputLossFrequency(self, selectorString, value):
        """ SetDutInputLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetDutInputLossTemperature(self, selectorString, value):
        """ SetDutInputLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetDutOutputLoss(self, selectorString, value):
        """ SetDutOutputLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetDutOutputLossCompensationEnabled(self, selectorString, value):
        """ SetDutOutputLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFDutOutputLossCompensationEnabled) -> int """
        pass

    def SetDutOutputLossFrequency(self, selectorString, value):
        """ SetDutOutputLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetDutOutputLossTemperature(self, selectorString, value):
        """ SetDutOutputLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetDutType(self, selectorString, value):
        """ SetDutType(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFDutType) -> int """
        pass

    def SetExternalPreampFrequency(self, selectorString, value):
        """ SetExternalPreampFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetExternalPreampGain(self, selectorString, value):
        """ SetExternalPreampGain(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetExternalPreampPresent(self, selectorString, value):
        """ SetExternalPreampPresent(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFExternalPreampPresent) -> int """
        pass

    def SetFrequencyConverterFrequencyContext(self, selectorString, value):
        """ SetFrequencyConverterFrequencyContext(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFFrequencyConverterFrequencyContext) -> int """
        pass

    def SetFrequencyConverterImageRejection(self, selectorString, value):
        """ SetFrequencyConverterImageRejection(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFrequencyConverterLOFrequency(self, selectorString, value):
        """ SetFrequencyConverterLOFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFrequencyConverterSideband(self, selectorString, value):
        """ SetFrequencyConverterSideband(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFFrequencyConverterSideband) -> int """
        pass

    def SetFrequencyList(self, selectorString, value):
        """ SetFrequencyList(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetMeasurementBandwidth(self, selectorString, value):
        """ SetMeasurementBandwidth(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementInterval(self, selectorString, value):
        """ SetMeasurementInterval(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFMeasurementMethod) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetYFactorMode(self, selectorString, value):
        """ SetYFactorMode(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFYFactorMode) -> int """
        pass

    def SetYFactorNoiseSourceColdTemperature(self, selectorString, value):
        """ SetYFactorNoiseSourceColdTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetYFactorNoiseSourceEnr(self, selectorString, value):
        """ SetYFactorNoiseSourceEnr(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetYFactorNoiseSourceEnrFrequency(self, selectorString, value):
        """ SetYFactorNoiseSourceEnrFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetYFactorNoiseSourceLoss(self, selectorString, value):
        """ SetYFactorNoiseSourceLoss(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetYFactorNoiseSourceLossCompensationEnabled(self, selectorString, value):
        """ SetYFactorNoiseSourceLossCompensationEnabled(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled) -> int """
        pass

    def SetYFactorNoiseSourceLossFrequency(self, selectorString, value):
        """ SetYFactorNoiseSourceLossFrequency(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetYFactorNoiseSourceLossTemperature(self, selectorString, value):
        """ SetYFactorNoiseSourceLossTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetYFactorNoiseSourceOffTemperature(self, selectorString, value):
        """ SetYFactorNoiseSourceOffTemperature(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetYFactorNoiseSourceSettlingTime(self, selectorString, value):
        """ SetYFactorNoiseSourceSettlingTime(self: RFmxSpecAnMXNFConfiguration, selectorString: str, value: float) -> int """
        pass

    def ValidateCalibrationData(self, selectorString, calibrationDataValid):
        """ ValidateCalibrationData(self: RFmxSpecAnMXNFConfiguration, selectorString: str) -> (int, RFmxSpecAnMXNFCalibrationDataValid) """
        pass


class RFmxSpecAnMXNFDutInputLossCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFDutInputLossCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXNFDutOutputLossCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFDutOutputLossCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXNFDutType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFDutType, values: Amplifier (0), Downconverter (1), Upconverter (2) """
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

    Amplifier = None
    Downconverter = None
    Upconverter = None
    value__ = None


class RFmxSpecAnMXNFExternalPreampPresent(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFExternalPreampPresent, values: False (0), True (1) """
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


class RFmxSpecAnMXNFFrequencyConverterFrequencyContext(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFFrequencyConverterFrequencyContext, values: IF (1), RF (0) """
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

    IF = None
    RF = None
    value__ = None


class RFmxSpecAnMXNFFrequencyConverterSideband(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFFrequencyConverterSideband, values: Lsb (0), Usb (1) """
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

    Lsb = None
    Usb = None
    value__ = None


class RFmxSpecAnMXNFMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFMeasurementMethod, values: ColdSource (1), YFactor (0) """
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

    ColdSource = None
    value__ = None
    YFactor = None


class RFmxSpecAnMXNFResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAnalyzerNoiseFigure(self, selectorString, timeout, analyzerNoiseFigure):
        """ FetchAnalyzerNoiseFigure(self: RFmxSpecAnMXNFResults, selectorString: str, timeout: float, analyzerNoiseFigure: Array[float]) -> (int, Array[float]) """
        pass

    def FetchColdSourcePower(self, selectorString, timeout, coldSourcePower):
        """ FetchColdSourcePower(self: RFmxSpecAnMXNFResults, selectorString: str, timeout: float, coldSourcePower: Array[float]) -> (int, Array[float]) """
        pass

    def FetchDutNoiseFigureAndGain(self, selectorString, timeout, dutNoiseFigure, dutNoiseTemperature, dutGain):
        """ FetchDutNoiseFigureAndGain(self: RFmxSpecAnMXNFResults, selectorString: str, timeout: float, dutNoiseFigure: Array[float], dutNoiseTemperature: Array[float], dutGain: Array[float]) -> (int, Array[float], Array[float], Array[float]) """
        pass

    def FetchYFactorPowers(self, selectorString, timeout, hotPower, coldPower):
        """ FetchYFactorPowers(self: RFmxSpecAnMXNFResults, selectorString: str, timeout: float, hotPower: Array[float], coldPower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchYFactors(self, selectorString, timeout, measurementYFactor, calibrationYFactor):
        """ FetchYFactors(self: RFmxSpecAnMXNFResults, selectorString: str, timeout: float, measurementYFactor: Array[float], calibrationYFactor: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetAnalyzerNoiseFigure(self, selectorString, value):
        """ GetAnalyzerNoiseFigure(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetCalibrationYFactor(self, selectorString, value):
        """ GetCalibrationYFactor(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetColdSourcePower(self, selectorString, value):
        """ GetColdSourcePower(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutGain(self, selectorString, value):
        """ GetDutGain(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutNoiseFigure(self, selectorString, value):
        """ GetDutNoiseFigure(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetDutNoiseTemperature(self, selectorString, value):
        """ GetDutNoiseTemperature(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetMeasurementYFactor(self, selectorString, value):
        """ GetMeasurementYFactor(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetYFactorColdPower(self, selectorString, value):
        """ GetYFactorColdPower(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetYFactorHotPower(self, selectorString, value):
        """ GetYFactorHotPower(self: RFmxSpecAnMXNFResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass


class RFmxSpecAnMXNFYFactorMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFYFactorMode, values: Calibrate (1), Measure (0) """
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

    Calibrate = None
    Measure = None
    value__ = None


class RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXNFYFactorNoiseSourceLossCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXObw(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXObw) -> RFmxSpecAnMXObwConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXObw) -> RFmxSpecAnMXObwResults

"""



class RFmxSpecAnMXObwAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXObwAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXObwAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2), Vector (5) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RFmxSpecAnMXObwConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXObwConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXObwAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXObwAveragingType) -> int """
        pass

    def ConfigureBandwidthPercentage(self, selectorString, bandwidthPercentage):
        """ ConfigureBandwidthPercentage(self: RFmxSpecAnMXObwConfiguration, selectorString: str, bandwidthPercentage: float) -> int """
        pass

    def ConfigureFft(self, selectorString, fftWindow, fftPadding):
        """ ConfigureFft(self: RFmxSpecAnMXObwConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXObwFftWindow, fftPadding: float) -> int """
        pass

    def ConfigurePowerUnits(self, selectorString, powerUnits):
        """ ConfigurePowerUnits(self: RFmxSpecAnMXObwConfiguration, selectorString: str, powerUnits: RFmxSpecAnMXObwPowerUnits) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXObwConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXObwRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXObwRbwFilterType) -> int """
        pass

    def ConfigureSpan(self, selectorString, span):
        """ ConfigureSpan(self: RFmxSpecAnMXObwConfiguration, selectorString: str, span: float) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxSpecAnMXObwConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXObwSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwAveragingType) """
        pass

    def GetBandwidthPercentage(self, selectorString, value):
        """ GetBandwidthPercentage(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftPadding(self, selectorString, value):
        """ GetFftPadding(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetPowerUnits(self, selectorString, value):
        """ GetPowerUnits(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwPowerUnits) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwRbwFilterBandwidthDefinition) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwRbwFilterType) """
        pass

    def GetSpan(self, selectorString, value):
        """ GetSpan(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, RFmxSpecAnMXObwSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxSpecAnMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwAveragingType) -> int """
        pass

    def SetBandwidthPercentage(self, selectorString, value):
        """ SetBandwidthPercentage(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftPadding(self, selectorString, value):
        """ SetFftPadding(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetPowerUnits(self, selectorString, value):
        """ SetPowerUnits(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwPowerUnits) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwRbwFilterBandwidthDefinition) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwRbwFilterType) -> int """
        pass

    def SetSpan(self, selectorString, value):
        """ SetSpan(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: RFmxSpecAnMXObwSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxSpecAnMXObwConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXObwFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXObwPowerUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwPowerUnits, values: dBm (0), dBmPerHertz (1) """
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

    dBm = None
    dBmPerHertz = None
    value__ = None


class RFmxSpecAnMXObwRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXObwRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinitionBinWidth (2) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinitionBinWidth = None
    value__ = None


class RFmxSpecAnMXObwRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXObwResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, occupiedBandwidth, averagePower, frequencyResolution, startFrequency, stopFrequency):
        """ FetchMeasurement(self: RFmxSpecAnMXObwResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchSpectrumTrace(self, selectorString, timeout, spectrum):
        """ FetchSpectrumTrace(self: RFmxSpecAnMXObwResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def GetAveragePower(self, selectorString, value):
        """ GetAveragePower(self: RFmxSpecAnMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyResolution(self, selectorString, value):
        """ GetFrequencyResolution(self: RFmxSpecAnMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetOccupiedBandwidth(self, selectorString, value):
        """ GetOccupiedBandwidth(self: RFmxSpecAnMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetStartFrequency(self, selectorString, value):
        """ GetStartFrequency(self: RFmxSpecAnMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetStopFrequency(self, selectorString, value):
        """ GetStopFrequency(self: RFmxSpecAnMXObwResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, occupiedBandwidth, averagePower, frequencyResolution, startFrequency, stopFrequency):
        """ Read(self: RFmxSpecAnMXObwResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass


class RFmxSpecAnMXObwSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXObwSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXPavt(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXPavt) -> RFmxSpecAnMXPavtConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXPavt) -> RFmxSpecAnMXPavtResults

"""



class RFmxSpecAnMXPavtConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureMeasurementBandwidth(self, selectorString, measurementBandwidth):
        """ ConfigureMeasurementBandwidth(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, measurementBandwidth: float) -> int """
        pass

    def ConfigureMeasurementInterval(self, selectorString, measurermentOffset, measurermentLength):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, measurermentOffset: float, measurermentLength: float) -> int """
        pass

    def ConfigureMeasurementLocationType(self, selectorString, measurementLocationType):
        """ ConfigureMeasurementLocationType(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, measurementLocationType: RFmxSpecAnMXPavtMeasurementLocationType) -> int """
        pass

    def ConfigureMeasurementStartTimeList(self, selectorString, measurementStartTime):
        """ ConfigureMeasurementStartTimeList(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, measurementStartTime: Array[float]) -> int """
        pass

    def ConfigureMeasurementStartTimeStep(self, selectorString, numberOfSegments, segment0MeasurementStartTime, segmentInterval):
        """ ConfigureMeasurementStartTimeStep(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, numberOfSegments: int, segment0MeasurementStartTime: float, segmentInterval: float) -> int """
        pass

    def ConfigureNumberOfSegments(self, selectorString, numberOfSegments):
        """ ConfigureNumberOfSegments(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, numberOfSegments: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetFrequencyOffsetCorrectionEnabled(self, selectorString, value):
        """ GetFrequencyOffsetCorrectionEnabled(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled) """
        pass

    def GetMeasurementBandwidth(self, selectorString, value):
        """ GetMeasurementBandwidth(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementLength(self, selectorString, value):
        """ GetMeasurementLength(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementLocationType(self, selectorString, value):
        """ GetMeasurementLocationType(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPavtMeasurementLocationType) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementStartTime(self, selectorString, value):
        """ GetMeasurementStartTime(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNumberOfSegments(self, selectorString, value):
        """ GetNumberOfSegments(self: RFmxSpecAnMXPavtConfiguration, selectorString: str) -> (int, int) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetFrequencyOffsetCorrectionEnabled(self, selectorString, value):
        """ SetFrequencyOffsetCorrectionEnabled(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled) -> int """
        pass

    def SetMeasurementBandwidth(self, selectorString, value):
        """ SetMeasurementBandwidth(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementLength(self, selectorString, value):
        """ SetMeasurementLength(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementLocationType(self, selectorString, value):
        """ SetMeasurementLocationType(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: RFmxSpecAnMXPavtMeasurementLocationType) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementStartTime(self, selectorString, value):
        """ SetMeasurementStartTime(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNumberOfSegments(self, selectorString, value):
        """ SetNumberOfSegments(self: RFmxSpecAnMXPavtConfiguration, selectorString: str, value: int) -> int """
        pass


class RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPavtFrequencyOffsetCorrectionEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXPavtMeasurementLocationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPavtMeasurementLocationType, values: Time (0), Trigger (1) """
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

    Time = None
    Trigger = None
    value__ = None


class RFmxSpecAnMXPavtResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAmplitudeTrace(self, selectorString, timeout, traceIndex, amplitude):
        """ FetchAmplitudeTrace(self: RFmxSpecAnMXPavtResults, selectorString: str, timeout: float, traceIndex: int, amplitude: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPhaseAndAmplitude(self, selectorString, timeout, meanRelativePhase, meanRelativeAmplitude, meanAbsolutePhase, meanAbsoluteAmplitude):
        """ FetchPhaseAndAmplitude(self: RFmxSpecAnMXPavtResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPhaseAndAmplitudeArray(self, selectorString, timeout, meanRelativePhase, meanRelativeAmplitude, meanAbsolutePhase, meanAbsoluteAmplitude):
        """ FetchPhaseAndAmplitudeArray(self: RFmxSpecAnMXPavtResults, selectorString: str, timeout: float, meanRelativePhase: Array[float], meanRelativeAmplitude: Array[float], meanAbsolutePhase: Array[float], meanAbsoluteAmplitude: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchPhaseTrace(self, selectorString, timeout, traceIndex, phase):
        """ FetchPhaseTrace(self: RFmxSpecAnMXPavtResults, selectorString: str, timeout: float, traceIndex: int, phase: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def GetMeanAbsoluteAmplitude(self, selectorString, value):
        """ GetMeanAbsoluteAmplitude(self: RFmxSpecAnMXPavtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanAbsolutePhase(self, selectorString, value):
        """ GetMeanAbsolutePhase(self: RFmxSpecAnMXPavtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRelativeAmplitude(self, selectorString, value):
        """ GetMeanRelativeAmplitude(self: RFmxSpecAnMXPavtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRelativePhase(self, selectorString, value):
        """ GetMeanRelativePhase(self: RFmxSpecAnMXPavtResults, selectorString: str) -> (int, float) """
        pass


class RFmxSpecAnMXPhaseNoise(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXPhaseNoise) -> RFmxSpecAnMXPhaseNoiseConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXPhaseNoise) -> RFmxSpecAnMXPhaseNoiseResults

"""



class RFmxSpecAnMXPhaseNoiseCancellationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPhaseNoiseCancellationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXPhaseNoiseConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAutoRange(self, selectorString, startFrequency, stopFrequency, rbwPercentage):
        """ ConfigureAutoRange(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, startFrequency: float, stopFrequency: float, rbwPercentage: float) -> int """
        pass

    def ConfigureAveragingMultiplier(self, selectorString, averagingMultiplier):
        """ ConfigureAveragingMultiplier(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, averagingMultiplier: int) -> int """
        pass

    def ConfigureCancellation(self, selectorString, cancellationEnabled, cancellationThreshold, frequency, referencePhaseNoise):
        """ ConfigureCancellation(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, cancellationEnabled: RFmxSpecAnMXPhaseNoiseCancellationEnabled, cancellationThreshold: float, frequency: Array[Single], referencePhaseNoise: Array[Single]) -> int """
        pass

    def ConfigureIntegratedNoise(self, selectorString, integratedNoiseRangeDefinition, integratedNoiseStartFrequency, integratedNoiseStopFrequency):
        """ ConfigureIntegratedNoise(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, integratedNoiseRangeDefinition: RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition, integratedNoiseStartFrequency: Array[float], integratedNoiseStopFrequency: Array[float]) -> int """
        pass

    def ConfigureNumberOfRanges(self, selectorString, numberOfRanges):
        """ ConfigureNumberOfRanges(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, numberOfRanges: int) -> int """
        pass

    def ConfigureRangeArray(self, selectorString, rangeStartFrequency, rangeStopFrequency, rangeRbwPercentage, rangeAveragingCount):
        """ ConfigureRangeArray(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, rangeStartFrequency: Array[float], rangeStopFrequency: Array[float], rangeRbwPercentage: Array[float], rangeAveragingCount: Array[int]) -> int """
        pass

    def ConfigureRangeDefinition(self, selectorString, rangeDefinition):
        """ ConfigureRangeDefinition(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, rangeDefinition: RFmxSpecAnMXPhaseNoiseRangeDefinition) -> int """
        pass

    def ConfigureSmoothing(self, selectorString, smoothingType, smoothingPercentage):
        """ ConfigureSmoothing(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, smoothingType: RFmxSpecAnMXPhaseNoiseSmoothingType, smoothingPercentage: float) -> int """
        pass

    def ConfigureSpotNoiseFrequencyList(self, selectorString, frequencyList):
        """ ConfigureSpotNoiseFrequencyList(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, frequencyList: Array[float]) -> int """
        pass

    def ConfigureSpurRemoval(self, selectorString, spurRemovalEnabled, peakExcursion):
        """ ConfigureSpurRemoval(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, spurRemovalEnabled: RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled, peakExcursion: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingMultiplier(self, selectorString, value):
        """ GetAveragingMultiplier(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetCancellationEnabled(self, selectorString, value):
        """ GetCancellationEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPhaseNoiseCancellationEnabled) """
        pass

    def GetCancellationFrequency(self, selectorString, value):
        """ GetCancellationFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetCancellationReferencePhaseNoise(self, selectorString, value):
        """ GetCancellationReferencePhaseNoise(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetCancellationThreshold(self, selectorString, value):
        """ GetCancellationThreshold(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPhaseNoiseFftWindow) """
        pass

    def GetIntegratedNoiseRangeDefinition(self, selectorString, value):
        """ GetIntegratedNoiseRangeDefinition(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition) """
        pass

    def GetIntegratedNoiseStartFrequency(self, selectorString, value):
        """ GetIntegratedNoiseStartFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetIntegratedNoiseStopFrequency(self, selectorString, value):
        """ GetIntegratedNoiseStopFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfRanges(self, selectorString, value):
        """ GetNumberOfRanges(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRangeAveragingCount(self, selectorString, value):
        """ GetRangeAveragingCount(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRangeDefinition(self, selectorString, value):
        """ GetRangeDefinition(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPhaseNoiseRangeDefinition) """
        pass

    def GetRangeRbwPercentage(self, selectorString, value):
        """ GetRangeRbwPercentage(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeStartFrequency(self, selectorString, value):
        """ GetRangeStartFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeStopFrequency(self, selectorString, value):
        """ GetRangeStopFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwPercentage(self, selectorString, value):
        """ GetRbwPercentage(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSmoothingPercentage(self, selectorString, value):
        """ GetSmoothingPercentage(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSmoothingType(self, selectorString, value):
        """ GetSmoothingType(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPhaseNoiseSmoothingType) """
        pass

    def GetSpotNoiseFrequencyList(self, selectorString, value):
        """ GetSpotNoiseFrequencyList(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetSpurRemovalEnabled(self, selectorString, value):
        """ GetSpurRemovalEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled) """
        pass

    def GetSpurRemovalPeakExcursion(self, selectorString, value):
        """ GetSpurRemovalPeakExcursion(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetStartFrequency(self, selectorString, value):
        """ GetStartFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetStopFrequency(self, selectorString, value):
        """ GetStopFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingMultiplier(self, selectorString, value):
        """ SetAveragingMultiplier(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetCancellationEnabled(self, selectorString, value):
        """ SetCancellationEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: RFmxSpecAnMXPhaseNoiseCancellationEnabled) -> int """
        pass

    def SetCancellationFrequency(self, selectorString, value):
        """ SetCancellationFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[Single]) -> int """
        pass

    def SetCancellationReferencePhaseNoise(self, selectorString, value):
        """ SetCancellationReferencePhaseNoise(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[Single]) -> int """
        pass

    def SetCancellationThreshold(self, selectorString, value):
        """ SetCancellationThreshold(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: RFmxSpecAnMXPhaseNoiseFftWindow) -> int """
        pass

    def SetIntegratedNoiseRangeDefinition(self, selectorString, value):
        """ SetIntegratedNoiseRangeDefinition(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition) -> int """
        pass

    def SetIntegratedNoiseStartFrequency(self, selectorString, value):
        """ SetIntegratedNoiseStartFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetIntegratedNoiseStopFrequency(self, selectorString, value):
        """ SetIntegratedNoiseStopFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfRanges(self, selectorString, value):
        """ SetNumberOfRanges(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRangeAveragingCount(self, selectorString, value):
        """ SetRangeAveragingCount(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRangeDefinition(self, selectorString, value):
        """ SetRangeDefinition(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: RFmxSpecAnMXPhaseNoiseRangeDefinition) -> int """
        pass

    def SetRangeRbwPercentage(self, selectorString, value):
        """ SetRangeRbwPercentage(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeStartFrequency(self, selectorString, value):
        """ SetRangeStartFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeStopFrequency(self, selectorString, value):
        """ SetRangeStopFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwPercentage(self, selectorString, value):
        """ SetRbwPercentage(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSmoothingPercentage(self, selectorString, value):
        """ SetSmoothingPercentage(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSmoothingType(self, selectorString, value):
        """ SetSmoothingType(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: RFmxSpecAnMXPhaseNoiseSmoothingType) -> int """
        pass

    def SetSpotNoiseFrequencyList(self, selectorString, value):
        """ SetSpotNoiseFrequencyList(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: Array[float]) -> int """
        pass

    def SetSpurRemovalEnabled(self, selectorString, value):
        """ SetSpurRemovalEnabled(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled) -> int """
        pass

    def SetSpurRemovalPeakExcursion(self, selectorString, value):
        """ SetSpurRemovalPeakExcursion(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetStartFrequency(self, selectorString, value):
        """ SetStartFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetStopFrequency(self, selectorString, value):
        """ SetStopFrequency(self: RFmxSpecAnMXPhaseNoiseConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXPhaseNoiseFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPhaseNoiseFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPhaseNoiseIntegratedNoiseRangeDefinition, values: Custom (2), Measurement (1), None (0) """
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

    Custom = None
    Measurement = None
    None = None
    value__ = None


class RFmxSpecAnMXPhaseNoiseRangeDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPhaseNoiseRangeDefinition, values: Auto (1), Manual (0) """
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
    Manual = None
    value__ = None


class RFmxSpecAnMXPhaseNoiseResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchCarrierMeasurement(self, selectorString, timeout, carrierFrequency, carrierPower):
        """ FetchCarrierMeasurement(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchIntegratedNoise(self, selectorString, timeout, integratedPhaseNoise, residualPMInRadian, residualPMInDegree, residualFM, jitter):
        """ FetchIntegratedNoise(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, timeout: float, integratedPhaseNoise: Array[float], residualPMInRadian: Array[float], residualPMInDegree: Array[float], residualFM: Array[float], jitter: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchMeasuredLogPlotTrace(self, selectorString, timeout, frequency, measuredPhaseNoise):
        """ FetchMeasuredLogPlotTrace(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, timeout: float, frequency: Array[Single], measuredPhaseNoise: Array[Single]) -> (int, Array[Single], Array[Single]) """
        pass

    def FetchSmoothedLogPlotTrace(self, selectorString, timeout, frequency, smoothedPhaseNoise):
        """ FetchSmoothedLogPlotTrace(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, timeout: float, frequency: Array[Single], smoothedPhaseNoise: Array[Single]) -> (int, Array[Single], Array[Single]) """
        pass

    def FetchSpotNoise(self, selectorString, timeout, spotPhaseNoise):
        """ FetchSpotNoise(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, timeout: float, spotPhaseNoise: Array[float]) -> (int, Array[float]) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierPower(self, selectorString, value):
        """ GetCarrierPower(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str) -> (int, float) """
        pass

    def GetIntegratedPhaseNoise(self, selectorString, value):
        """ GetIntegratedPhaseNoise(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetJitter(self, selectorString, value):
        """ GetJitter(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetResidualFM(self, selectorString, value):
        """ GetResidualFM(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetResidualPMInDegree(self, selectorString, value):
        """ GetResidualPMInDegree(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetResidualPMInRadian(self, selectorString, value):
        """ GetResidualPMInRadian(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetSpotPhaseNoise(self, selectorString, value):
        """ GetSpotPhaseNoise(self: RFmxSpecAnMXPhaseNoiseResults, selectorString: str, value: Array[float]) -> (int, Array[float]) """
        pass


class RFmxSpecAnMXPhaseNoiseSmoothingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPhaseNoiseSmoothingType, values: Linear (1), Logarithmic (2), Median (3), None (0) """
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

    Linear = None
    Logarithmic = None
    Median = None
    None = None
    value__ = None


class RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPhaseNoiseSpurRemovalEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXPropertyId(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXPropertyId, values: AcpAllTracesEnabled (1052705), AcpAmplitudeCorrectionType (1052729), AcpAveragingCount (1052693), AcpAveragingEnabled (1052694), AcpAveragingType (1052696), AcpCarrierFrequency (1052676), AcpCarrierIntegrationBandwidth (1052677), AcpCarrierMode (1052675), AcpCarrierRrcFilterAlpha (1052679), AcpCarrierRrcFilterEnabled (1052678), AcpFarIFOutputPowerOffset (1052726), AcpFftPadding (1052698), AcpFftWindow (1052697), AcpIFOutputPowerOffsetAuto (1052724), AcpMeasurementEnabled (1052672), AcpMeasurementMethod (1052690), AcpNearIFOutputPowerOffset (1052725), AcpNoiseCompensationEnabled (1052704), AcpNumberOfAnalysisThreads (1052692), AcpNumberOfCarriers (1052674), AcpNumberOfOffsets (1052680), AcpOffsetEnabled (1052681), AcpOffsetFrequency (1052682), AcpOffsetFrequencyDefinition (1052727), AcpOffsetIntegrationBandwidth (1052686), AcpOffsetPowerReferenceCarrier (1052684), AcpOffsetPowerReferenceSpecific (1052685), AcpOffsetRelativeAttenuation (1052687), AcpOffsetRrcFilterAlpha (1052689), AcpOffsetRrcFilterEnabled (1052688), AcpOffsetSideband (1052683), AcpPowerUnits (1052691), AcpRbwFilterAutoBandwidth (1052699), AcpRbwFilterBandwidth (1052700), AcpRbwFilterBandwidthDefinition (1052728), AcpRbwFilterType (1052701), AcpResultsCarrierAbsolutePower (1052710), AcpResultsCarrierFrequency (1052708), AcpResultsCarrierIntegrationBandwidth (1052709), AcpResultsCarrierTotalRelativePower (1052711), AcpResultsFrequencyResolution (1052707), AcpResultsLowerOffsetAbsolutePower (1052716), AcpResultsLowerOffsetFrequency (1052713), AcpResultsLowerOffsetFrequencyReferenceCarrier (1052712), AcpResultsLowerOffsetIntegrationBandwidth (1052714), AcpResultsLowerOffsetPowerReferenceCarrier (1052715), AcpResultsLowerOffsetRelativePower (1052717), AcpResultsTotalCarrierPower (1052706), AcpResultsUpperOffsetAbsolutePower (1052722), AcpResultsUpperOffsetFrequency (1052719), AcpResultsUpperOffsetFrequencyReferenceCarrier (1052718), AcpResultsUpperOffsetIntegrationBandwidth (1052720), AcpResultsUpperOffsetPowerReferenceCarrier (1052721), AcpResultsUpperOffsetRelativePower (1052723), AcpSequentialFftSize (1052730), AcpSweepTimeAuto (1052702), AcpSweepTimeInterval (1052703), AmpmAllTracesEnabled (1105937), AmpmAMToAMCurveFitOrder (1105922), AmpmAMToAMCurveFitType (1105923), AmpmAMToPMCurveFitOrder (1105924), AmpmAMToPMCurveFitType (1105925), AmpmAutoCarrierDetectionEnabled (1105963), AmpmAveragingCount (1105927), AmpmAveragingEnabled (1105926), AmpmCarrierBandwidth (1105966), AmpmCarrierOffset (1105965), AmpmCompressionPointEnabled (1105956), AmpmCompressionPointLevel (1105957), AmpmDutAverageInputPower (1105936), AmpmEqualizerFilterLength (1105968), AmpmEqualizerMode (1105967), AmpmFrequencyOffsetCorrectionEnabled (1105953), AmpmIQOriginOffsetCorrectionEnabled (1105961), AmpmMaximumTimingError (1105954), AmpmMeasurementEnabled (1105920), AmpmMeasurementInterval (1105929), AmpmMeasurementSampleRate (1105932), AmpmMeasurementSampleRateMode (1105931), AmpmNumberOfAnalysisThreads (1105938), AmpmNumberOfCarriers (1105964), AmpmReferencePowerType (1105955), AmpmResults1dBCompressionPoint (1105949), AmpmResultsAMToAMCurveFitCoefficients (1105940), AmpmResultsAMToAMCurveFitResidual (1105945), AmpmResultsAMToPMCurveFitCoefficients (1105941), AmpmResultsAMToPMCurveFitResidual (1105946), AmpmResultsGainErrorRange (1105947), AmpmResultsInputCompressionPoint (1105958), AmpmResultsMeanLinearGain (1105942), AmpmResultsMeanPhaseError (1105943), AmpmResultsMeanRmsEvm (1105944), AmpmResultsOutputCompressionPoint (1105959), AmpmResultsPhaseErrorRange (1105948), AmpmSignalType (1105930), AmpmSynchronizationMethod (1105962), AmpmThresholdEnabled (1105933), AmpmThresholdLevel (1105935), AmpmThresholdType (1105934), AutoLevelInitialReferenceLevel (1048589), CcdfAllTracesEnabled (1056781), CcdfMeasurementEnabled (1056768), CcdfMeasurementInterval (1056770), CcdfNumberOfAnalysisThreads (1056771), CcdfNumberOfRecords (1056772), CcdfRbwFilterBandwidth (1056775), CcdfRbwFilterRrcAlpha (1056774), CcdfRbwFilterType (1056776), CcdfResultsMeanPower (1056782), CcdfResultsMeanPowerPercentile (1056783), CcdfResultsMeasuredSamplesCount (1056791), CcdfResultsOneHundredthPercentPower (1056787), CcdfResultsOnePercentPower (1056785), CcdfResultsOneTenThousandthPercentPower (1056789), CcdfResultsOneTenthPercentPower (1056786), CcdfResultsOneThousandthPercentPower (1056788), CcdfResultsPeakPower (1056790), CcdfResultsTenPercentPower (1056784), CcdfThresholdEnabled (1056777), CcdfThresholdLevel (1056778), CcdfThresholdType (1056779), CenterFrequency (1048577), ChpAllTracesEnabled (1060884), ChpAmplitudeCorrectionType (1060895), ChpAveragingCount (1060870), ChpAveragingEnabled (1060871), ChpAveragingType (1060873), ChpCarrierFrequency (1060889), ChpCarrierIntegrationBandwidth (1060866), ChpCarrierRrcFilterAlpha (1060880), ChpCarrierRrcFilterEnabled (1060879), ChpFftPadding (1060875), ChpFftWindow (1060874), ChpIntegrationBandwidth (1060866), ChpMeasurementEnabled (1060864), ChpNumberOfAnalysisThreads (1060867), ChpNumberOfCarriers (1060888), ChpRbwFilterAutoBandwidth (1060876), ChpRbwFilterBandwidth (1060877), ChpRbwFilterBandwidthDefinition (1060894), ChpRbwFilterType (1060878), ChpResultsAverageChannelPower (1060885), ChpResultsAverageChannelPowerPsd (1060886), ChpResultsCarrierAbsolutePower (1060885), ChpResultsCarrierFrequency (1060891), ChpResultsCarrierIntegrationBandwidth (1060892), ChpResultsCarrierPsd (1060886), ChpResultsCarrierRelativePower (1060893), ChpResultsFrequencyResolution (1060887), ChpResultsTotalCarrierPower (1060890), ChpRrcFilterAlpha (1060880), ChpRrcFilterEnabled (1060879), ChpSpan (1060868), ChpSweepTimeAuto (1060881), ChpSweepTimeInterval (1060882), DigitalEdgeTriggerEdge (1048582), DigitalEdgeTriggerSource (1048581), DpdAllTracesEnabled (1110047), DpdApplyDpdCfrEnabled (1110086), DpdApplyDpdCfrMaximumIterations (1110088), DpdApplyDpdCfrMethod (1110087), DpdApplyDpdCfrShapingFactor (1110109), DpdApplyDpdCfrShapingThreshold (1110110), DpdApplyDpdCfrTargetPapr (1110106), DpdApplyDpdCfrTargetPaprType (1110089), DpdApplyDpdCfrWindowLength (1110108), DpdApplyDpdCfrWindowType (1110107), DpdApplyDpdConfigurationInput (1110049), DpdApplyDpdHeadroom (1110052), DpdApplyDpdHeadroomMode (1110051), DpdApplyDpdLookupTableCorrectionType (1110050), DpdApplyDpdMemoryModelCorrectionType (1110070), DpdApplyDpdUserDpdModel (1110054), DpdApplyDpdUserDutAverageInputPower (1110053), DpdApplyDpdUserLookupTableInputPower (1105960), DpdApplyDpdUserLookupTableType (1110080), DpdApplyDpdUserMeasurementSampleRate (1110055), DpdApplyDpdUserMemoryPolynomialLagMemoryDepth (1110063), DpdApplyDpdUserMemoryPolynomialLagOrder (1110061), DpdApplyDpdUserMemoryPolynomialLeadMemoryDepth (1110062), DpdApplyDpdUserMemoryPolynomialLeadOrder (1110060), DpdApplyDpdUserMemoryPolynomialMaximumLag (1110065), DpdApplyDpdUserMemoryPolynomialMaximumLead (1110064), DpdApplyDpdUserMemoryPolynomialMemoryDepth (1110059), DpdApplyDpdUserMemoryPolynomialOrder (1110058), DpdAutoCarrierDetectionEnabled (1110091), DpdAveragingCount (1110045), DpdAveragingEnabled (1110044), DpdCarrierBandwidth (1110094), DpdCarrierOffset (1110093), DpdDutAverageInputPower (1110023), DpdFrequencyOffsetCorrectionEnabled (1110073), DpdIQOriginOffsetCorrectionEnabled (1110117), DpdIterativeDpdEnabled (1110042), DpdLookupTableAMToAMCurveFitOrder (1110025), DpdLookupTableAMToAMCurveFitType (1110026), DpdLookupTableAMToPMCurveFitOrder (1110027), DpdLookupTableAMToPMCurveFitType (1110028), DpdLookupTableStepSize (1110032), DpdLookupTableThresholdEnabled (1110029), DpdLookupTableThresholdLevel (1110031), DpdLookupTableThresholdType (1110030), DpdLookupTableType (1110072), DpdMaximumTimingError (1110074), DpdMeasurementEnabled (1110016), DpdMeasurementInterval (1110020), DpdMeasurementSampleRate (1110019), DpdMeasurementSampleRateMode (1110018), DpdMemoryPolynomialLagMemoryDepth (1110038), DpdMemoryPolynomialLagOrder (1110036), DpdMemoryPolynomialLeadMemoryDepth (1110037), DpdMemoryPolynomialLeadOrder (1110035), DpdMemoryPolynomialMaximumLag (1110040), DpdMemoryPolynomialMaximumLead (1110039), DpdMemoryPolynomialMemoryDepth (1110034), DpdMemoryPolynomialOrder (1110033), DpdModel (1110024), DpdNmseEnabled (1110075), DpdNumberOfAnalysisThreads (1110048), DpdNumberOfCarriers (1110092), DpdPreDpdCarrierBandwidth (1110116), DpdPreDpdCarrierOffset (1110115), DpdPreDpdCfrEnabled (1110076), DpdPreDpdCfrFilterEnabled (1110112), DpdPreDpdCfrMaximumIterations (1110077), DpdPreDpdCfrMethod (1110078), DpdPreDpdCfrNumberOfCarriers (1110114), DpdPreDpdCfrShapingFactor (1110084), DpdPreDpdCfrShapingThreshold (1110085), DpdPreDpdCfrTargetPapr (1110081), DpdPreDpdCfrWindowLength (1110083), DpdPreDpdCfrWindowType (1110082), DpdResultsAverageGain (1110067), DpdResultsNmse (1110111), DpdSignalType (1110021), DpdSynchronizationMethod (1110090), DpdTargetGainType (1110071), ExternalAttenuation (1048579), FcntAllTracesEnabled (1064976), FcntAveragingCount (1064965), FcntAveragingEnabled (1064966), FcntAveragingType (1064968), FcntMeasurementEnabled (1064960), FcntMeasurementInterval (1064962), FcntNumberOfAnalysisThreads (1064963), FcntRbwFilterBandwidth (1064970), FcntRbwFilterRrcAlpha (1064969), FcntRbwFilterType (1064971), FcntResultsAllanDeviation (1064980), FcntResultsAverageAbsoluteFrequency (1064979), FcntResultsAverageRelativeFrequency (1064977), FcntResultsMeanPhase (1064978), FcntThresholdEnabled (1064972), FcntThresholdLevel (1064973), FcntThresholdType (1064974), HarmAllTracesEnabled (1069072), HarmAutoSetupEnabled (1069064), HarmAveragingCount (1069068), HarmAveragingEnabled (1069069), HarmAveragingType (1069071), HarmFundamentalMeasurementInterval (1069062), HarmFundamentalRbwFilterAlpha (1069059), HarmFundamentalRbwFilterBandwidth (1069060), HarmFundamentalRbwFilterType (1069061), HarmHarmonicBandwidth (1069080), HarmHarmonicEnabled (1069065), HarmHarmonicMeasurementInterval (1069067), HarmHarmonicOrder (1069066), HarmMeasurementEnabled (1069056), HarmMeasurementMethod (1069082), HarmNoiseCompensationEnabled (1069083), HarmNumberOfAnalysisThreads (1069058), HarmNumberOfHarmonics (1069063), HarmResultsAverageFundamentalPower (1069074), HarmResultsFundamentalFrequency (1069073), HarmResultsHarmonicAverageAbsolutePower (1069078), HarmResultsHarmonicAverageRelativePower (1069079), HarmResultsHarmonicFrequency (1069076), HarmResultsHarmonicRbw (1069077), HarmResultsTotalHarmonicDistortion (1069075), IMAllTracesEnabled (1114140), IMAmplitudeCorrectionType (1114155), IMAutoIntermodsSetupEnabled (1114117), IMAveragingCount (1114132), IMAveragingEnabled (1114131), IMAveragingType (1114134), IMFarIFOutputPowerOffset (1114139), IMFftPadding (1114136), IMFftWindow (1114135), IMFrequencyDefinition (1114114), IMFundamentalLowerToneFrequency (1114115), IMFundamentalUpperToneFrequency (1114116), IMIFOutputPowerOffsetAuto (1114137), IMIntermodEnabled (1114120), IMIntermodOrder (1114121), IMIntermodSide (1114122), IMLocalPeakSearchEnabled (1114154), IMLowerIntermodFrequency (1114123), IMMaximumIntermodOrder (1114118), IMMeasurementEnabled (1114112), IMMeasurementMethod (1114125), IMNearIFOutputPowerOffset (1114138), IMNumberOfAnalysisThreads (1114141), IMNumberOfIntermods (1114119), IMRbwFilterAutoBandwidth (1114126), IMRbwFilterBandwidth (1114127), IMRbwFilterType (1114128), IMResultsFundamentalLowerTonePower (1114143), IMResultsFundamentalUpperTonePower (1114145), IMResultsIntermodOrder (1114146), IMResultsLowerIntermodPower (1114148), IMResultsLowerOutputInterceptPower (1114151), IMResultsUpperIntermodPower (1114150), IMResultsUpperOutputInterceptPower (1114152), IMResultsWorstCaseOutputInterceptPower (1114153), IMSweepTimeAuto (1114129), IMSweepTimeInterval (1114130), IMUpperIntermodFrequency (1114124), IQAcquisitionTime (1110276), IQBandwidth (1110281), IQBandwidthAuto (1110280), IQDeleteRecordOnFetch (1110282), IQMeasurementEnabled (1110272), IQNumberOfRecords (1110275), IQPowerEdgeTriggerLevel (1048584), IQPowerEdgeTriggerLevelType (1052671), IQPowerEdgeTriggerSlope (1048585), IQPowerEdgeTriggerSource (1048583), IQPretriggerTime (1110277), IQSampleRate (1110274), LimitedConfigurationChange (1048590), NFAveragingCount (1179656), NFAveragingEnabled (1179655), NFCalibrationLoss (1179678), NFCalibrationLossCompensationEnabled (1179677), NFCalibrationLossFrequency (1179679), NFCalibrationLossTemperature (1179680), NFCalibrationSetupId (1179700), NFColdSourceDutS11 (1179697), NFColdSourceDutS12 (1179696), NFColdSourceDutS21 (1179695), NFColdSourceDutS22 (1179698), NFColdSourceDutSParametersFrequency (1179699), NFColdSourceInputTerminationTemperature (1179694), NFColdSourceInputTerminationVswr (1179692), NFColdSourceInputTerminationVswrFrequency (1179693), NFColdSourceMode (1179691), NFDeviceTemperatureTolerance (1179705), NFDutInputLoss (1179666), NFDutInputLossCompensationEnabled (1179665), NFDutInputLossFrequency (1179667), NFDutInputLossTemperature (1179668), NFDutOutputLoss (1179670), NFDutOutputLossCompensationEnabled (1179669), NFDutOutputLossFrequency (1179671), NFDutOutputLossTemperature (1179672), NFDutType (1179706), NFExternalPreampFrequency (1179702), NFExternalPreampGain (1179703), NFExternalPreampPresent (1179701), NFFrequencyConverterFrequencyContext (1179710), NFFrequencyConverterImageRejection (1179712), NFFrequencyConverterLOFrequency (1179708), NFFrequencyConverterSideband (1179711), NFFrequencyList (1179652), NFMeasurementBandwidth (1179653), NFMeasurementEnabled (1179649), NFMeasurementInterval (1179654), NFMeasurementMethod (1179657), NFNumberOfAnalysisThreads (1179681), NFResultsAnalyzerNoiseFigure (1179685), NFResultsCalibrationYFactor (1179687), NFResultsColdSourcePower (1179690), NFResultsDutGain (1179684), NFResultsDutNoiseFigure (1179682), NFResultsDutNoiseTemperature (1179683), NFResultsMeasurementYFactor (1179686), NFResultsYFactorColdPower (1179689), NFResultsYFactorHotPower (1179688), NFYFactorMode (1179658), NFYFactorNoiseSourceColdTemperature (1179662), NFYFactorNoiseSourceEnr (1179660), NFYFactorNoiseSourceEnrFrequency (1179661), NFYFactorNoiseSourceLoss (1179674), NFYFactorNoiseSourceLossCompensationEnabled (1179673), NFYFactorNoiseSourceLossFrequency (1179675), NFYFactorNoiseSourceLossTemperature (1179676), NFYFactorNoiseSourceOffTemperature (1179663), NFYFactorNoiseSourceSettlingTime (1179664), ObwAllTracesEnabled (1073170), ObwAmplitudeCorrectionType (1073178), ObwAveragingCount (1073158), ObwAveragingEnabled (1073159), ObwAveragingType (1073161), ObwBandwidthPercentage (1073154), ObwFftPadding (1073163), ObwFftWindow (1073162), ObwMeasurementEnabled (1073152), ObwNumberOfAnalysisThreads (1073155), ObwPowerUnits (1073176), ObwRbwFilterAutoBandwidth (1073164), ObwRbwFilterBandwidth (1073165), ObwRbwFilterBandwidthDefinition (1073177), ObwRbwFilterType (1073166), ObwResultsAveragePower (1073172), ObwResultsFrequencyResolution (1073175), ObwResultsOccupiedBandwidth (1073171), ObwResultsStartFrequency (1073173), ObwResultsStopFrequency (1073174), ObwSpan (1073156), ObwSweepTimeAuto (1073167), ObwSweepTimeInterval (1073168), PavtAllTracesEnabled (1077255), PavtFrequencyOffsetCorrectionEnabled (1077260), PavtMeasurementBandwidth (1077261), PavtMeasurementEnabled (1077248), PavtMeasurementLength (1077254), PavtMeasurementLocationType (1077250), PavtMeasurementOffset (1077253), PavtMeasurementStartTime (1077252), PavtNumberOfSegments (1077251), PavtResultsMeanAbsoluteAmplitude (1077262), PavtResultsMeanAbsolutePhase (1077263), PavtResultsMeanRelativeAmplitude (1077259), PavtResultsMeanRelativePhase (1077258), PhaseNoiseAllTracesEnabled (1245203), PhaseNoiseAveragingMultiplier (1245190), PhaseNoiseCancellationEnabled (1245215), PhaseNoiseCancellationFrequency (1245217), PhaseNoiseCancellationReferencePhaseNoise (1245218), PhaseNoiseCancellationThreshold (1245216), PhaseNoiseFftWindow (1245191), PhaseNoiseIntegratedNoiseRangeDefinition (1245200), PhaseNoiseIntegratedNoiseStartFrequency (1245201), PhaseNoiseIntegratedNoiseStopFrequency (1245202), PhaseNoiseMeasurementEnabled (1245184), PhaseNoiseNumberOfRanges (1245192), PhaseNoiseRangeAveragingCount (1245196), PhaseNoiseRangeDefinition (1245186), PhaseNoiseRangeRbwPercentage (1245195), PhaseNoiseRangeStartFrequency (1245193), PhaseNoiseRangeStopFrequency (1245194), PhaseNoiseRbwPercentage (1245189), PhaseNoiseResultsCarrierFrequency (1245206), PhaseNoiseResultsCarrierPower (1245205), PhaseNoiseResultsIntegratedPhaseNoise (1245208), PhaseNoiseResultsJitter (1245212), PhaseNoiseResultsResidualFM (1245211), PhaseNoiseResultsResidualPMInDegree (1245210), PhaseNoiseResultsResidualPMInRadian (1245209), PhaseNoiseResultsSpotPhaseNoise (1245207), PhaseNoiseSmoothingPercentage (1245198), PhaseNoiseSmoothingType (1245197), PhaseNoiseSpotNoiseFrequencyList (1245199), PhaseNoiseSpurRemovalEnabled (1245213), PhaseNoiseSpurRemovalPeakExcursion (1245214), PhaseNoiseStartFrequency (1245187), PhaseNoiseStopFrequency (1245188), ReferenceLevel (1048578), ReferenceLevelHeadroom (1052668), ReferenceLevelUnits (1052670), ResultFetchTimeout (1097728), SelectedPorts (1052669), SemAllTracesEnabled (1081383), SemAmplitudeCorrectionType (1081423), SemAveragingCount (1081374), SemAveragingEnabled (1081375), SemAveragingType (1081377), SemCarrierChannelBandwidth (1081419), SemCarrierEnabled (1081347), SemCarrierFrequency (1081348), SemCarrierIntegrationBandwidth (1081349), SemCarrierRbwFilterAutoBandwidth (1081350), SemCarrierRbwFilterBandwidth (1081351), SemCarrierRbwFilterBandwidthDefinition (1081422), SemCarrierRbwFilterType (1081352), SemCarrierRrcFilterAlpha (1081354), SemCarrierRrcFilterEnabled (1081353), SemFftPadding (1081379), SemFftWindow (1081378), SemMeasurementEnabled (1081344), SemNumberOfAnalysisThreads (1081373), SemNumberOfCarriers (1081346), SemNumberOfOffsets (1081355), SemOffsetAbsoluteLimitMode (1081359), SemOffsetAbsoluteLimitStart (1081360), SemOffsetAbsoluteLimitStop (1081361), SemOffsetBandwidthIntegral (1081356), SemOffsetEnabled (1081362), SemOffsetFrequencyDefinition (1081420), SemOffsetLimitFailMask (1081357), SemOffsetRbwFilterAutoBandwidth (1081366), SemOffsetRbwFilterBandwidth (1081367), SemOffsetRbwFilterBandwidthDefinition (1081421), SemOffsetRbwFilterType (1081368), SemOffsetRelativeAttenuation (1081358), SemOffsetRelativeLimitMode (1081369), SemOffsetRelativeLimitStart (1081370), SemOffsetRelativeLimitStop (1081371), SemOffsetSideband (1081363), SemOffsetStartFrequency (1081364), SemOffsetStopFrequency (1081365), SemPowerUnits (1081372), SemReferenceType (1081380), SemResultsCarrierAbsolutePower (1081389), SemResultsCarrierFrequency (1081387), SemResultsCarrierIntegrationBandwidth (1081388), SemResultsCarrierPeakAbsolutePower (1081391), SemResultsCarrierPeakFrequency (1081392), SemResultsCarrierTotalRelativePower (1081390), SemResultsCompositeMeasurementStatus (1081385), SemResultsFrequencyResolution (1081386), SemResultsLowerOffsetMargin (1081401), SemResultsLowerOffsetMarginAbsolutePower (1081402), SemResultsLowerOffsetMarginFrequency (1081404), SemResultsLowerOffsetMarginRelativePower (1081403), SemResultsLowerOffsetMeasurementStatus (1081405), SemResultsLowerOffsetPeakAbsolutePower (1081398), SemResultsLowerOffsetPeakFrequency (1081400), SemResultsLowerOffsetPeakRelativePower (1081399), SemResultsLowerOffsetPowerReferenceCarrier (1081395), SemResultsLowerOffsetStartFrequency (1081393), SemResultsLowerOffsetStopFrequency (1081394), SemResultsLowerOffsetTotalAbsolutePower (1081396), SemResultsLowerOffsetTotalRelativePower (1081397), SemResultsTotalCarrierPower (1081384), SemResultsUpperOffsetMargin (1081414), SemResultsUpperOffsetMarginAbsolutePower (1081415), SemResultsUpperOffsetMarginFrequency (1081417), SemResultsUpperOffsetMarginRelativePower (1081416), SemResultsUpperOffsetMeasurementStatus (1081418), SemResultsUpperOffsetPeakAbsolutePower (1081411), SemResultsUpperOffsetPeakFrequency (1081413), SemResultsUpperOffsetPeakRelativePower (1081412), SemResultsUpperOffsetPowerReferenceCarrier (1081408), SemResultsUpperOffsetStartFrequency (1081406), SemResultsUpperOffsetStopFrequency (1081407), SemResultsUpperOffsetTotalAbsolutePower (1081409), SemResultsUpperOffsetTotalRelativePower (1081410), SemSweepTimeAuto (1081381), SemSweepTimeInterval (1081382), SpectrumAmplitudeCorrectionType (1085463), SpectrumAveragingCount (1085445), SpectrumAveragingEnabled (1085446), SpectrumAveragingType (1085448), SpectrumDetectorPoints (1085465), SpectrumDetectorType (1085464), SpectrumFftPadding (1085450), SpectrumFftWindow (1085449), SpectrumMeasurementEnabled (1085440), SpectrumNoiseCompensationEnabled (1085456), SpectrumNumberOfAnalysisThreads (1085442), SpectrumPowerUnits (1085461), SpectrumRbwFilterAutoBandwidth (1085451), SpectrumRbwFilterBandwidth (1085452), SpectrumRbwFilterBandwidthDefinition (1085462), SpectrumRbwFilterType (1085453), SpectrumResultsFrequencyResolution (1085460), SpectrumResultsPeakAmplitude (1085458), SpectrumResultsPeakFrequency (1085459), SpectrumSpan (1085443), SpectrumSweepTimeAuto (1085454), SpectrumSweepTimeInterval (1085455), SpectrumVbwFilterAutoBandwidth (1085466), SpectrumVbwFilterBandwidth (1085467), SpectrumVbwFilterVbwToRbwRatio (1085468), SpurAllTracesEnabled (1089560), SpurAmplitudeCorrectionType (1089572), SpurAveragingCount (1089546), SpurAveragingEnabled (1089547), SpurAveragingType (1089549), SpurFftWindow (1089551), SpurMeasurementEnabled (1089536), SpurNumberOfAnalysisThreads (1089539), SpurNumberOfRanges (1089540), SpurRangeAbsoluteLimitMode (1089552), SpurRangeAbsoluteLimitStart (1089553), SpurRangeAbsoluteLimitStop (1089554), SpurRangeDetectorPoints (1089574), SpurRangeDetectorType (1089573), SpurRangeEnabled (1089541), SpurRangeNumberOfSpursToReport (1089543), SpurRangePeakExcursion (1089570), SpurRangePeakThreshold (1089569), SpurRangeRbwFilterAutoBandwidth (1089555), SpurRangeRbwFilterBandwidth (1089556), SpurRangeRbwFilterBandwidthDefinition (1089571), SpurRangeRbwFilterType (1089557), SpurRangeRelativeAttenuation (1089542), SpurRangeStartFrequency (1089544), SpurRangeStopFrequency (1089545), SpurRangeSweepTimeAuto (1089558), SpurRangeSweepTimeInterval (1089559), SpurRangeVbwFilterAutoBandwidth (1089575), SpurRangeVbwFilterBandwidth (1089576), SpurRangeVbwFilterVbwToRbwRatio (1089577), SpurResultsMeasurementStatus (1089561), SpurResultsRangeMeasurementStatus (1089566), SpurResultsRangeSpurAbsoluteLimit (1089564), SpurResultsRangeSpurAmplitude (1089563), SpurResultsRangeSpurFrequency (1089562), SpurResultsRangeSpurMargin (1089565), SpurResultsRangeSpurNumberOfDetectedSpurs (1089567), SpurTraceRangeIndex (1089568), TriggerDelay (1048586), TriggerMinimumQuietTimeDuration (1048588), TriggerMinimumQuietTimeMode (1048587), TriggerType (1048580), TxpAllTracesEnabled (1093648), TxpAveragingCount (1093637), TxpAveragingEnabled (1093638), TxpAveragingType (1093640), TxpMeasurementEnabled (1093632), TxpMeasurementInterval (1093634), TxpNumberOfAnalysisThreads (1093635), TxpRbwFilterAlpha (1093641), TxpRbwFilterBandwidth (1093642), TxpRbwFilterType (1093643), TxpResultsAverageMeanPower (1093649), TxpResultsMaximumPower (1093651), TxpResultsMinimumPower (1093652), TxpResultsPeakToAverageRatio (1093650), TxpThresholdEnabled (1093644), TxpThresholdLevel (1093645), TxpThresholdType (1093646), TxpVbwFilterAutoBandwidth (1093655), TxpVbwFilterBandwidth (1093656), TxpVbwFilterVbwToRbwRatio (1093657) """
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

    AcpAllTracesEnabled = None
    AcpAmplitudeCorrectionType = None
    AcpAveragingCount = None
    AcpAveragingEnabled = None
    AcpAveragingType = None
    AcpCarrierFrequency = None
    AcpCarrierIntegrationBandwidth = None
    AcpCarrierMode = None
    AcpCarrierRrcFilterAlpha = None
    AcpCarrierRrcFilterEnabled = None
    AcpFarIFOutputPowerOffset = None
    AcpFftPadding = None
    AcpFftWindow = None
    AcpIFOutputPowerOffsetAuto = None
    AcpMeasurementEnabled = None
    AcpMeasurementMethod = None
    AcpNearIFOutputPowerOffset = None
    AcpNoiseCompensationEnabled = None
    AcpNumberOfAnalysisThreads = None
    AcpNumberOfCarriers = None
    AcpNumberOfOffsets = None
    AcpOffsetEnabled = None
    AcpOffsetFrequency = None
    AcpOffsetFrequencyDefinition = None
    AcpOffsetIntegrationBandwidth = None
    AcpOffsetPowerReferenceCarrier = None
    AcpOffsetPowerReferenceSpecific = None
    AcpOffsetRelativeAttenuation = None
    AcpOffsetRrcFilterAlpha = None
    AcpOffsetRrcFilterEnabled = None
    AcpOffsetSideband = None
    AcpPowerUnits = None
    AcpRbwFilterAutoBandwidth = None
    AcpRbwFilterBandwidth = None
    AcpRbwFilterBandwidthDefinition = None
    AcpRbwFilterType = None
    AcpResultsCarrierAbsolutePower = None
    AcpResultsCarrierFrequency = None
    AcpResultsCarrierIntegrationBandwidth = None
    AcpResultsCarrierTotalRelativePower = None
    AcpResultsFrequencyResolution = None
    AcpResultsLowerOffsetAbsolutePower = None
    AcpResultsLowerOffsetFrequency = None
    AcpResultsLowerOffsetFrequencyReferenceCarrier = None
    AcpResultsLowerOffsetIntegrationBandwidth = None
    AcpResultsLowerOffsetPowerReferenceCarrier = None
    AcpResultsLowerOffsetRelativePower = None
    AcpResultsTotalCarrierPower = None
    AcpResultsUpperOffsetAbsolutePower = None
    AcpResultsUpperOffsetFrequency = None
    AcpResultsUpperOffsetFrequencyReferenceCarrier = None
    AcpResultsUpperOffsetIntegrationBandwidth = None
    AcpResultsUpperOffsetPowerReferenceCarrier = None
    AcpResultsUpperOffsetRelativePower = None
    AcpSequentialFftSize = None
    AcpSweepTimeAuto = None
    AcpSweepTimeInterval = None
    AmpmAllTracesEnabled = None
    AmpmAMToAMCurveFitOrder = None
    AmpmAMToAMCurveFitType = None
    AmpmAMToPMCurveFitOrder = None
    AmpmAMToPMCurveFitType = None
    AmpmAutoCarrierDetectionEnabled = None
    AmpmAveragingCount = None
    AmpmAveragingEnabled = None
    AmpmCarrierBandwidth = None
    AmpmCarrierOffset = None
    AmpmCompressionPointEnabled = None
    AmpmCompressionPointLevel = None
    AmpmDutAverageInputPower = None
    AmpmEqualizerFilterLength = None
    AmpmEqualizerMode = None
    AmpmFrequencyOffsetCorrectionEnabled = None
    AmpmIQOriginOffsetCorrectionEnabled = None
    AmpmMaximumTimingError = None
    AmpmMeasurementEnabled = None
    AmpmMeasurementInterval = None
    AmpmMeasurementSampleRate = None
    AmpmMeasurementSampleRateMode = None
    AmpmNumberOfAnalysisThreads = None
    AmpmNumberOfCarriers = None
    AmpmReferencePowerType = None
    AmpmResults1dBCompressionPoint = None
    AmpmResultsAMToAMCurveFitCoefficients = None
    AmpmResultsAMToAMCurveFitResidual = None
    AmpmResultsAMToPMCurveFitCoefficients = None
    AmpmResultsAMToPMCurveFitResidual = None
    AmpmResultsGainErrorRange = None
    AmpmResultsInputCompressionPoint = None
    AmpmResultsMeanLinearGain = None
    AmpmResultsMeanPhaseError = None
    AmpmResultsMeanRmsEvm = None
    AmpmResultsOutputCompressionPoint = None
    AmpmResultsPhaseErrorRange = None
    AmpmSignalType = None
    AmpmSynchronizationMethod = None
    AmpmThresholdEnabled = None
    AmpmThresholdLevel = None
    AmpmThresholdType = None
    AutoLevelInitialReferenceLevel = None
    CcdfAllTracesEnabled = None
    CcdfMeasurementEnabled = None
    CcdfMeasurementInterval = None
    CcdfNumberOfAnalysisThreads = None
    CcdfNumberOfRecords = None
    CcdfRbwFilterBandwidth = None
    CcdfRbwFilterRrcAlpha = None
    CcdfRbwFilterType = None
    CcdfResultsMeanPower = None
    CcdfResultsMeanPowerPercentile = None
    CcdfResultsMeasuredSamplesCount = None
    CcdfResultsOneHundredthPercentPower = None
    CcdfResultsOnePercentPower = None
    CcdfResultsOneTenThousandthPercentPower = None
    CcdfResultsOneTenthPercentPower = None
    CcdfResultsOneThousandthPercentPower = None
    CcdfResultsPeakPower = None
    CcdfResultsTenPercentPower = None
    CcdfThresholdEnabled = None
    CcdfThresholdLevel = None
    CcdfThresholdType = None
    CenterFrequency = None
    ChpAllTracesEnabled = None
    ChpAmplitudeCorrectionType = None
    ChpAveragingCount = None
    ChpAveragingEnabled = None
    ChpAveragingType = None
    ChpCarrierFrequency = None
    ChpCarrierIntegrationBandwidth = None
    ChpCarrierRrcFilterAlpha = None
    ChpCarrierRrcFilterEnabled = None
    ChpFftPadding = None
    ChpFftWindow = None
    ChpIntegrationBandwidth = None
    ChpMeasurementEnabled = None
    ChpNumberOfAnalysisThreads = None
    ChpNumberOfCarriers = None
    ChpRbwFilterAutoBandwidth = None
    ChpRbwFilterBandwidth = None
    ChpRbwFilterBandwidthDefinition = None
    ChpRbwFilterType = None
    ChpResultsAverageChannelPower = None
    ChpResultsAverageChannelPowerPsd = None
    ChpResultsCarrierAbsolutePower = None
    ChpResultsCarrierFrequency = None
    ChpResultsCarrierIntegrationBandwidth = None
    ChpResultsCarrierPsd = None
    ChpResultsCarrierRelativePower = None
    ChpResultsFrequencyResolution = None
    ChpResultsTotalCarrierPower = None
    ChpRrcFilterAlpha = None
    ChpRrcFilterEnabled = None
    ChpSpan = None
    ChpSweepTimeAuto = None
    ChpSweepTimeInterval = None
    DigitalEdgeTriggerEdge = None
    DigitalEdgeTriggerSource = None
    DpdAllTracesEnabled = None
    DpdApplyDpdCfrEnabled = None
    DpdApplyDpdCfrMaximumIterations = None
    DpdApplyDpdCfrMethod = None
    DpdApplyDpdCfrShapingFactor = None
    DpdApplyDpdCfrShapingThreshold = None
    DpdApplyDpdCfrTargetPapr = None
    DpdApplyDpdCfrTargetPaprType = None
    DpdApplyDpdCfrWindowLength = None
    DpdApplyDpdCfrWindowType = None
    DpdApplyDpdConfigurationInput = None
    DpdApplyDpdHeadroom = None
    DpdApplyDpdHeadroomMode = None
    DpdApplyDpdLookupTableCorrectionType = None
    DpdApplyDpdMemoryModelCorrectionType = None
    DpdApplyDpdUserDpdModel = None
    DpdApplyDpdUserDutAverageInputPower = None
    DpdApplyDpdUserLookupTableInputPower = None
    DpdApplyDpdUserLookupTableType = None
    DpdApplyDpdUserMeasurementSampleRate = None
    DpdApplyDpdUserMemoryPolynomialLagMemoryDepth = None
    DpdApplyDpdUserMemoryPolynomialLagOrder = None
    DpdApplyDpdUserMemoryPolynomialLeadMemoryDepth = None
    DpdApplyDpdUserMemoryPolynomialLeadOrder = None
    DpdApplyDpdUserMemoryPolynomialMaximumLag = None
    DpdApplyDpdUserMemoryPolynomialMaximumLead = None
    DpdApplyDpdUserMemoryPolynomialMemoryDepth = None
    DpdApplyDpdUserMemoryPolynomialOrder = None
    DpdAutoCarrierDetectionEnabled = None
    DpdAveragingCount = None
    DpdAveragingEnabled = None
    DpdCarrierBandwidth = None
    DpdCarrierOffset = None
    DpdDutAverageInputPower = None
    DpdFrequencyOffsetCorrectionEnabled = None
    DpdIQOriginOffsetCorrectionEnabled = None
    DpdIterativeDpdEnabled = None
    DpdLookupTableAMToAMCurveFitOrder = None
    DpdLookupTableAMToAMCurveFitType = None
    DpdLookupTableAMToPMCurveFitOrder = None
    DpdLookupTableAMToPMCurveFitType = None
    DpdLookupTableStepSize = None
    DpdLookupTableThresholdEnabled = None
    DpdLookupTableThresholdLevel = None
    DpdLookupTableThresholdType = None
    DpdLookupTableType = None
    DpdMaximumTimingError = None
    DpdMeasurementEnabled = None
    DpdMeasurementInterval = None
    DpdMeasurementSampleRate = None
    DpdMeasurementSampleRateMode = None
    DpdMemoryPolynomialLagMemoryDepth = None
    DpdMemoryPolynomialLagOrder = None
    DpdMemoryPolynomialLeadMemoryDepth = None
    DpdMemoryPolynomialLeadOrder = None
    DpdMemoryPolynomialMaximumLag = None
    DpdMemoryPolynomialMaximumLead = None
    DpdMemoryPolynomialMemoryDepth = None
    DpdMemoryPolynomialOrder = None
    DpdModel = None
    DpdNmseEnabled = None
    DpdNumberOfAnalysisThreads = None
    DpdNumberOfCarriers = None
    DpdPreDpdCarrierBandwidth = None
    DpdPreDpdCarrierOffset = None
    DpdPreDpdCfrEnabled = None
    DpdPreDpdCfrFilterEnabled = None
    DpdPreDpdCfrMaximumIterations = None
    DpdPreDpdCfrMethod = None
    DpdPreDpdCfrNumberOfCarriers = None
    DpdPreDpdCfrShapingFactor = None
    DpdPreDpdCfrShapingThreshold = None
    DpdPreDpdCfrTargetPapr = None
    DpdPreDpdCfrWindowLength = None
    DpdPreDpdCfrWindowType = None
    DpdResultsAverageGain = None
    DpdResultsNmse = None
    DpdSignalType = None
    DpdSynchronizationMethod = None
    DpdTargetGainType = None
    ExternalAttenuation = None
    FcntAllTracesEnabled = None
    FcntAveragingCount = None
    FcntAveragingEnabled = None
    FcntAveragingType = None
    FcntMeasurementEnabled = None
    FcntMeasurementInterval = None
    FcntNumberOfAnalysisThreads = None
    FcntRbwFilterBandwidth = None
    FcntRbwFilterRrcAlpha = None
    FcntRbwFilterType = None
    FcntResultsAllanDeviation = None
    FcntResultsAverageAbsoluteFrequency = None
    FcntResultsAverageRelativeFrequency = None
    FcntResultsMeanPhase = None
    FcntThresholdEnabled = None
    FcntThresholdLevel = None
    FcntThresholdType = None
    HarmAllTracesEnabled = None
    HarmAutoSetupEnabled = None
    HarmAveragingCount = None
    HarmAveragingEnabled = None
    HarmAveragingType = None
    HarmFundamentalMeasurementInterval = None
    HarmFundamentalRbwFilterAlpha = None
    HarmFundamentalRbwFilterBandwidth = None
    HarmFundamentalRbwFilterType = None
    HarmHarmonicBandwidth = None
    HarmHarmonicEnabled = None
    HarmHarmonicMeasurementInterval = None
    HarmHarmonicOrder = None
    HarmMeasurementEnabled = None
    HarmMeasurementMethod = None
    HarmNoiseCompensationEnabled = None
    HarmNumberOfAnalysisThreads = None
    HarmNumberOfHarmonics = None
    HarmResultsAverageFundamentalPower = None
    HarmResultsFundamentalFrequency = None
    HarmResultsHarmonicAverageAbsolutePower = None
    HarmResultsHarmonicAverageRelativePower = None
    HarmResultsHarmonicFrequency = None
    HarmResultsHarmonicRbw = None
    HarmResultsTotalHarmonicDistortion = None
    IMAllTracesEnabled = None
    IMAmplitudeCorrectionType = None
    IMAutoIntermodsSetupEnabled = None
    IMAveragingCount = None
    IMAveragingEnabled = None
    IMAveragingType = None
    IMFarIFOutputPowerOffset = None
    IMFftPadding = None
    IMFftWindow = None
    IMFrequencyDefinition = None
    IMFundamentalLowerToneFrequency = None
    IMFundamentalUpperToneFrequency = None
    IMIFOutputPowerOffsetAuto = None
    IMIntermodEnabled = None
    IMIntermodOrder = None
    IMIntermodSide = None
    IMLocalPeakSearchEnabled = None
    IMLowerIntermodFrequency = None
    IMMaximumIntermodOrder = None
    IMMeasurementEnabled = None
    IMMeasurementMethod = None
    IMNearIFOutputPowerOffset = None
    IMNumberOfAnalysisThreads = None
    IMNumberOfIntermods = None
    IMRbwFilterAutoBandwidth = None
    IMRbwFilterBandwidth = None
    IMRbwFilterType = None
    IMResultsFundamentalLowerTonePower = None
    IMResultsFundamentalUpperTonePower = None
    IMResultsIntermodOrder = None
    IMResultsLowerIntermodPower = None
    IMResultsLowerOutputInterceptPower = None
    IMResultsUpperIntermodPower = None
    IMResultsUpperOutputInterceptPower = None
    IMResultsWorstCaseOutputInterceptPower = None
    IMSweepTimeAuto = None
    IMSweepTimeInterval = None
    IMUpperIntermodFrequency = None
    IQAcquisitionTime = None
    IQBandwidth = None
    IQBandwidthAuto = None
    IQDeleteRecordOnFetch = None
    IQMeasurementEnabled = None
    IQNumberOfRecords = None
    IQPowerEdgeTriggerLevel = None
    IQPowerEdgeTriggerLevelType = None
    IQPowerEdgeTriggerSlope = None
    IQPowerEdgeTriggerSource = None
    IQPretriggerTime = None
    IQSampleRate = None
    LimitedConfigurationChange = None
    NFAveragingCount = None
    NFAveragingEnabled = None
    NFCalibrationLoss = None
    NFCalibrationLossCompensationEnabled = None
    NFCalibrationLossFrequency = None
    NFCalibrationLossTemperature = None
    NFCalibrationSetupId = None
    NFColdSourceDutS11 = None
    NFColdSourceDutS12 = None
    NFColdSourceDutS21 = None
    NFColdSourceDutS22 = None
    NFColdSourceDutSParametersFrequency = None
    NFColdSourceInputTerminationTemperature = None
    NFColdSourceInputTerminationVswr = None
    NFColdSourceInputTerminationVswrFrequency = None
    NFColdSourceMode = None
    NFDeviceTemperatureTolerance = None
    NFDutInputLoss = None
    NFDutInputLossCompensationEnabled = None
    NFDutInputLossFrequency = None
    NFDutInputLossTemperature = None
    NFDutOutputLoss = None
    NFDutOutputLossCompensationEnabled = None
    NFDutOutputLossFrequency = None
    NFDutOutputLossTemperature = None
    NFDutType = None
    NFExternalPreampFrequency = None
    NFExternalPreampGain = None
    NFExternalPreampPresent = None
    NFFrequencyConverterFrequencyContext = None
    NFFrequencyConverterImageRejection = None
    NFFrequencyConverterLOFrequency = None
    NFFrequencyConverterSideband = None
    NFFrequencyList = None
    NFMeasurementBandwidth = None
    NFMeasurementEnabled = None
    NFMeasurementInterval = None
    NFMeasurementMethod = None
    NFNumberOfAnalysisThreads = None
    NFResultsAnalyzerNoiseFigure = None
    NFResultsCalibrationYFactor = None
    NFResultsColdSourcePower = None
    NFResultsDutGain = None
    NFResultsDutNoiseFigure = None
    NFResultsDutNoiseTemperature = None
    NFResultsMeasurementYFactor = None
    NFResultsYFactorColdPower = None
    NFResultsYFactorHotPower = None
    NFYFactorMode = None
    NFYFactorNoiseSourceColdTemperature = None
    NFYFactorNoiseSourceEnr = None
    NFYFactorNoiseSourceEnrFrequency = None
    NFYFactorNoiseSourceLoss = None
    NFYFactorNoiseSourceLossCompensationEnabled = None
    NFYFactorNoiseSourceLossFrequency = None
    NFYFactorNoiseSourceLossTemperature = None
    NFYFactorNoiseSourceOffTemperature = None
    NFYFactorNoiseSourceSettlingTime = None
    ObwAllTracesEnabled = None
    ObwAmplitudeCorrectionType = None
    ObwAveragingCount = None
    ObwAveragingEnabled = None
    ObwAveragingType = None
    ObwBandwidthPercentage = None
    ObwFftPadding = None
    ObwFftWindow = None
    ObwMeasurementEnabled = None
    ObwNumberOfAnalysisThreads = None
    ObwPowerUnits = None
    ObwRbwFilterAutoBandwidth = None
    ObwRbwFilterBandwidth = None
    ObwRbwFilterBandwidthDefinition = None
    ObwRbwFilterType = None
    ObwResultsAveragePower = None
    ObwResultsFrequencyResolution = None
    ObwResultsOccupiedBandwidth = None
    ObwResultsStartFrequency = None
    ObwResultsStopFrequency = None
    ObwSpan = None
    ObwSweepTimeAuto = None
    ObwSweepTimeInterval = None
    PavtAllTracesEnabled = None
    PavtFrequencyOffsetCorrectionEnabled = None
    PavtMeasurementBandwidth = None
    PavtMeasurementEnabled = None
    PavtMeasurementLength = None
    PavtMeasurementLocationType = None
    PavtMeasurementOffset = None
    PavtMeasurementStartTime = None
    PavtNumberOfSegments = None
    PavtResultsMeanAbsoluteAmplitude = None
    PavtResultsMeanAbsolutePhase = None
    PavtResultsMeanRelativeAmplitude = None
    PavtResultsMeanRelativePhase = None
    PhaseNoiseAllTracesEnabled = None
    PhaseNoiseAveragingMultiplier = None
    PhaseNoiseCancellationEnabled = None
    PhaseNoiseCancellationFrequency = None
    PhaseNoiseCancellationReferencePhaseNoise = None
    PhaseNoiseCancellationThreshold = None
    PhaseNoiseFftWindow = None
    PhaseNoiseIntegratedNoiseRangeDefinition = None
    PhaseNoiseIntegratedNoiseStartFrequency = None
    PhaseNoiseIntegratedNoiseStopFrequency = None
    PhaseNoiseMeasurementEnabled = None
    PhaseNoiseNumberOfRanges = None
    PhaseNoiseRangeAveragingCount = None
    PhaseNoiseRangeDefinition = None
    PhaseNoiseRangeRbwPercentage = None
    PhaseNoiseRangeStartFrequency = None
    PhaseNoiseRangeStopFrequency = None
    PhaseNoiseRbwPercentage = None
    PhaseNoiseResultsCarrierFrequency = None
    PhaseNoiseResultsCarrierPower = None
    PhaseNoiseResultsIntegratedPhaseNoise = None
    PhaseNoiseResultsJitter = None
    PhaseNoiseResultsResidualFM = None
    PhaseNoiseResultsResidualPMInDegree = None
    PhaseNoiseResultsResidualPMInRadian = None
    PhaseNoiseResultsSpotPhaseNoise = None
    PhaseNoiseSmoothingPercentage = None
    PhaseNoiseSmoothingType = None
    PhaseNoiseSpotNoiseFrequencyList = None
    PhaseNoiseSpurRemovalEnabled = None
    PhaseNoiseSpurRemovalPeakExcursion = None
    PhaseNoiseStartFrequency = None
    PhaseNoiseStopFrequency = None
    ReferenceLevel = None
    ReferenceLevelHeadroom = None
    ReferenceLevelUnits = None
    ResultFetchTimeout = None
    SelectedPorts = None
    SemAllTracesEnabled = None
    SemAmplitudeCorrectionType = None
    SemAveragingCount = None
    SemAveragingEnabled = None
    SemAveragingType = None
    SemCarrierChannelBandwidth = None
    SemCarrierEnabled = None
    SemCarrierFrequency = None
    SemCarrierIntegrationBandwidth = None
    SemCarrierRbwFilterAutoBandwidth = None
    SemCarrierRbwFilterBandwidth = None
    SemCarrierRbwFilterBandwidthDefinition = None
    SemCarrierRbwFilterType = None
    SemCarrierRrcFilterAlpha = None
    SemCarrierRrcFilterEnabled = None
    SemFftPadding = None
    SemFftWindow = None
    SemMeasurementEnabled = None
    SemNumberOfAnalysisThreads = None
    SemNumberOfCarriers = None
    SemNumberOfOffsets = None
    SemOffsetAbsoluteLimitMode = None
    SemOffsetAbsoluteLimitStart = None
    SemOffsetAbsoluteLimitStop = None
    SemOffsetBandwidthIntegral = None
    SemOffsetEnabled = None
    SemOffsetFrequencyDefinition = None
    SemOffsetLimitFailMask = None
    SemOffsetRbwFilterAutoBandwidth = None
    SemOffsetRbwFilterBandwidth = None
    SemOffsetRbwFilterBandwidthDefinition = None
    SemOffsetRbwFilterType = None
    SemOffsetRelativeAttenuation = None
    SemOffsetRelativeLimitMode = None
    SemOffsetRelativeLimitStart = None
    SemOffsetRelativeLimitStop = None
    SemOffsetSideband = None
    SemOffsetStartFrequency = None
    SemOffsetStopFrequency = None
    SemPowerUnits = None
    SemReferenceType = None
    SemResultsCarrierAbsolutePower = None
    SemResultsCarrierFrequency = None
    SemResultsCarrierIntegrationBandwidth = None
    SemResultsCarrierPeakAbsolutePower = None
    SemResultsCarrierPeakFrequency = None
    SemResultsCarrierTotalRelativePower = None
    SemResultsCompositeMeasurementStatus = None
    SemResultsFrequencyResolution = None
    SemResultsLowerOffsetMargin = None
    SemResultsLowerOffsetMarginAbsolutePower = None
    SemResultsLowerOffsetMarginFrequency = None
    SemResultsLowerOffsetMarginRelativePower = None
    SemResultsLowerOffsetMeasurementStatus = None
    SemResultsLowerOffsetPeakAbsolutePower = None
    SemResultsLowerOffsetPeakFrequency = None
    SemResultsLowerOffsetPeakRelativePower = None
    SemResultsLowerOffsetPowerReferenceCarrier = None
    SemResultsLowerOffsetStartFrequency = None
    SemResultsLowerOffsetStopFrequency = None
    SemResultsLowerOffsetTotalAbsolutePower = None
    SemResultsLowerOffsetTotalRelativePower = None
    SemResultsTotalCarrierPower = None
    SemResultsUpperOffsetMargin = None
    SemResultsUpperOffsetMarginAbsolutePower = None
    SemResultsUpperOffsetMarginFrequency = None
    SemResultsUpperOffsetMarginRelativePower = None
    SemResultsUpperOffsetMeasurementStatus = None
    SemResultsUpperOffsetPeakAbsolutePower = None
    SemResultsUpperOffsetPeakFrequency = None
    SemResultsUpperOffsetPeakRelativePower = None
    SemResultsUpperOffsetPowerReferenceCarrier = None
    SemResultsUpperOffsetStartFrequency = None
    SemResultsUpperOffsetStopFrequency = None
    SemResultsUpperOffsetTotalAbsolutePower = None
    SemResultsUpperOffsetTotalRelativePower = None
    SemSweepTimeAuto = None
    SemSweepTimeInterval = None
    SpectrumAmplitudeCorrectionType = None
    SpectrumAveragingCount = None
    SpectrumAveragingEnabled = None
    SpectrumAveragingType = None
    SpectrumDetectorPoints = None
    SpectrumDetectorType = None
    SpectrumFftPadding = None
    SpectrumFftWindow = None
    SpectrumMeasurementEnabled = None
    SpectrumNoiseCompensationEnabled = None
    SpectrumNumberOfAnalysisThreads = None
    SpectrumPowerUnits = None
    SpectrumRbwFilterAutoBandwidth = None
    SpectrumRbwFilterBandwidth = None
    SpectrumRbwFilterBandwidthDefinition = None
    SpectrumRbwFilterType = None
    SpectrumResultsFrequencyResolution = None
    SpectrumResultsPeakAmplitude = None
    SpectrumResultsPeakFrequency = None
    SpectrumSpan = None
    SpectrumSweepTimeAuto = None
    SpectrumSweepTimeInterval = None
    SpectrumVbwFilterAutoBandwidth = None
    SpectrumVbwFilterBandwidth = None
    SpectrumVbwFilterVbwToRbwRatio = None
    SpurAllTracesEnabled = None
    SpurAmplitudeCorrectionType = None
    SpurAveragingCount = None
    SpurAveragingEnabled = None
    SpurAveragingType = None
    SpurFftWindow = None
    SpurMeasurementEnabled = None
    SpurNumberOfAnalysisThreads = None
    SpurNumberOfRanges = None
    SpurRangeAbsoluteLimitMode = None
    SpurRangeAbsoluteLimitStart = None
    SpurRangeAbsoluteLimitStop = None
    SpurRangeDetectorPoints = None
    SpurRangeDetectorType = None
    SpurRangeEnabled = None
    SpurRangeNumberOfSpursToReport = None
    SpurRangePeakExcursion = None
    SpurRangePeakThreshold = None
    SpurRangeRbwFilterAutoBandwidth = None
    SpurRangeRbwFilterBandwidth = None
    SpurRangeRbwFilterBandwidthDefinition = None
    SpurRangeRbwFilterType = None
    SpurRangeRelativeAttenuation = None
    SpurRangeStartFrequency = None
    SpurRangeStopFrequency = None
    SpurRangeSweepTimeAuto = None
    SpurRangeSweepTimeInterval = None
    SpurRangeVbwFilterAutoBandwidth = None
    SpurRangeVbwFilterBandwidth = None
    SpurRangeVbwFilterVbwToRbwRatio = None
    SpurResultsMeasurementStatus = None
    SpurResultsRangeMeasurementStatus = None
    SpurResultsRangeSpurAbsoluteLimit = None
    SpurResultsRangeSpurAmplitude = None
    SpurResultsRangeSpurFrequency = None
    SpurResultsRangeSpurMargin = None
    SpurResultsRangeSpurNumberOfDetectedSpurs = None
    SpurTraceRangeIndex = None
    TriggerDelay = None
    TriggerMinimumQuietTimeDuration = None
    TriggerMinimumQuietTimeMode = None
    TriggerType = None
    TxpAllTracesEnabled = None
    TxpAveragingCount = None
    TxpAveragingEnabled = None
    TxpAveragingType = None
    TxpMeasurementEnabled = None
    TxpMeasurementInterval = None
    TxpNumberOfAnalysisThreads = None
    TxpRbwFilterAlpha = None
    TxpRbwFilterBandwidth = None
    TxpRbwFilterType = None
    TxpResultsAverageMeanPower = None
    TxpResultsMaximumPower = None
    TxpResultsMinimumPower = None
    TxpResultsPeakToAverageRatio = None
    TxpThresholdEnabled = None
    TxpThresholdLevel = None
    TxpThresholdType = None
    TxpVbwFilterAutoBandwidth = None
    TxpVbwFilterBandwidth = None
    TxpVbwFilterVbwToRbwRatio = None
    value__ = None


class RFmxSpecAnMXReferenceLevelUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXReferenceLevelUnits, values: dBm (0) """
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

    dBm = None
    value__ = None


class RFmxSpecAnMXSem(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXSem) -> RFmxSpecAnMXSemConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXSem) -> RFmxSpecAnMXSemResults

"""



class RFmxSpecAnMXSemAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXSemAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSemAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2), Vector (5) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RFmxSpecAnMXSemCarrierEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemCarrierEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSemCarrierRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemCarrierRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinitionBinWidth (2) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinitionBinWidth = None
    value__ = None


class RFmxSpecAnMXSemCarrierRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemCarrierRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXSemCarrierRrcFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemCarrierRrcFilterEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSemCompositeMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemCompositeMeasurementStatus, values: Fail (0), Pass (1) """
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

    Fail = None
    Pass = None
    value__ = None


class RFmxSpecAnMXSemConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXSemConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXSemAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXSemAveragingType) -> int """
        pass

    def ConfigureCarrierChannelBandwidth(self, selectorString, carrierChannelBandwidth):
        """ ConfigureCarrierChannelBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, carrierChannelBandwidth: float) -> int """
        pass

    def ConfigureCarrierEnabled(self, selectorString, carrierEnabled):
        """ ConfigureCarrierEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, carrierEnabled: RFmxSpecAnMXSemCarrierEnabled) -> int """
        pass

    def ConfigureCarrierFrequency(self, selectorString, carrierFrequency):
        """ ConfigureCarrierFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str, carrierFrequency: float) -> int """
        pass

    def ConfigureCarrierIntegrationBandwidth(self, selectorString, integrationBandwidth):
        """ ConfigureCarrierIntegrationBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, integrationBandwidth: float) -> int """
        pass

    def ConfigureCarrierRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureCarrierRbwFilter(self: RFmxSpecAnMXSemConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXSemCarrierRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXSemCarrierRbwFilterType) -> int """
        pass

    def ConfigureCarrierRrcFilter(self, selectorString, rrcFilterEnabled, rrcAlpha):
        """ ConfigureCarrierRrcFilter(self: RFmxSpecAnMXSemConfiguration, selectorString: str, rrcFilterEnabled: RFmxSpecAnMXSemCarrierRrcFilterEnabled, rrcAlpha: float) -> int """
        pass

    def ConfigureFft(self, selectorString, fftWindow, fftPadding):
        """ ConfigureFft(self: RFmxSpecAnMXSemConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXSemFftWindow, fftPadding: float) -> int """
        pass

    def ConfigureNumberOfCarriers(self, selectorString, numberOfCarriers):
        """ ConfigureNumberOfCarriers(self: RFmxSpecAnMXSemConfiguration, selectorString: str, numberOfCarriers: int) -> int """
        pass

    def ConfigureNumberOfOffsets(self, selectorString, numberOfOffsets):
        """ ConfigureNumberOfOffsets(self: RFmxSpecAnMXSemConfiguration, selectorString: str, numberOfOffsets: int) -> int """
        pass

    def ConfigureOffsetAbsoluteLimit(self, selectorString, absoluteLimitMode, absoluteLimitStart, absoluteLimitStop):
        """ ConfigureOffsetAbsoluteLimit(self: RFmxSpecAnMXSemConfiguration, selectorString: str, absoluteLimitMode: RFmxSpecAnMXSemOffsetAbsoluteLimitMode, absoluteLimitStart: float, absoluteLimitStop: float) -> int """
        pass

    def ConfigureOffsetAbsoluteLimitArray(self, selectorString, absoluteLimitMode, absoluteLimitStart, absoluteLimitStop):
        """ ConfigureOffsetAbsoluteLimitArray(self: RFmxSpecAnMXSemConfiguration, selectorString: str, absoluteLimitMode: Array[RFmxSpecAnMXSemOffsetAbsoluteLimitMode], absoluteLimitStart: Array[float], absoluteLimitStop: Array[float]) -> int """
        pass

    def ConfigureOffsetBandwidthIntegral(self, selectorString, bandwidthIntegral):
        """ ConfigureOffsetBandwidthIntegral(self: RFmxSpecAnMXSemConfiguration, selectorString: str, bandwidthIntegral: int) -> int """
        pass

    def ConfigureOffsetFrequency(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetEnabled, offsetSideband):
        """ ConfigureOffsetFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str, offsetStartFrequency: float, offsetStopFrequency: float, offsetEnabled: RFmxSpecAnMXSemOffsetEnabled, offsetSideband: RFmxSpecAnMXSemOffsetSideband) -> int """
        pass

    def ConfigureOffsetFrequencyArray(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetEnabled, offsetSideband):
        """ ConfigureOffsetFrequencyArray(self: RFmxSpecAnMXSemConfiguration, selectorString: str, offsetStartFrequency: Array[float], offsetStopFrequency: Array[float], offsetEnabled: Array[RFmxSpecAnMXSemOffsetEnabled], offsetSideband: Array[RFmxSpecAnMXSemOffsetSideband]) -> int """
        pass

    def ConfigureOffsetFrequencyDefinition(self, selectorString, offsetFrequencyDefinition):
        """ ConfigureOffsetFrequencyDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str, offsetFrequencyDefinition: RFmxSpecAnMXSemOffsetFrequencyDefinition) -> int """
        pass

    def ConfigureOffsetLimitFailMask(self, selectorString, limitFailMask):
        """ ConfigureOffsetLimitFailMask(self: RFmxSpecAnMXSemConfiguration, selectorString: str, limitFailMask: RFmxSpecAnMXSemOffsetLimitFailMask) -> int """
        pass

    def ConfigureOffsetRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureOffsetRbwFilter(self: RFmxSpecAnMXSemConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXSemOffsetRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXSemOffsetRbwFilterType) -> int """
        pass

    def ConfigureOffsetRbwFilterArray(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureOffsetRbwFilterArray(self: RFmxSpecAnMXSemConfiguration, selectorString: str, rbwAuto: Array[RFmxSpecAnMXSemOffsetRbwAutoBandwidth], rbw: Array[float], rbwFilterType: Array[RFmxSpecAnMXSemOffsetRbwFilterType]) -> int """
        pass

    def ConfigureOffsetRelativeAttenuation(self, selectorString, relativeAttenuation):
        """ ConfigureOffsetRelativeAttenuation(self: RFmxSpecAnMXSemConfiguration, selectorString: str, relativeAttenuation: float) -> int """
        pass

    def ConfigureOffsetRelativeAttenuationArray(self, selectorString, relativeAttenuation):
        """ ConfigureOffsetRelativeAttenuationArray(self: RFmxSpecAnMXSemConfiguration, selectorString: str, relativeAttenuation: Array[float]) -> int """
        pass

    def ConfigureOffsetRelativeLimit(self, selectorString, relativeLimitMode, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimit(self: RFmxSpecAnMXSemConfiguration, selectorString: str, relativeLimitMode: RFmxSpecAnMXSemOffsetRelativeLimitMode, relativeLimitStart: float, relativeLimitStop: float) -> int """
        pass

    def ConfigureOffsetRelativeLimitArray(self, selectorString, relativeLimitMode, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimitArray(self: RFmxSpecAnMXSemConfiguration, selectorString: str, relativeLimitMode: Array[RFmxSpecAnMXSemOffsetRelativeLimitMode], relativeLimitStart: Array[float], relativeLimitStop: Array[float]) -> int """
        pass

    def ConfigurePowerUnits(self, selectorString, powerUnits):
        """ ConfigurePowerUnits(self: RFmxSpecAnMXSemConfiguration, selectorString: str, powerUnits: RFmxSpecAnMXSemPowerUnits) -> int """
        pass

    def ConfigureReferenceType(self, selectorString, referenceType):
        """ ConfigureReferenceType(self: RFmxSpecAnMXSemConfiguration, selectorString: str, referenceType: RFmxSpecAnMXSemReferenceType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxSpecAnMXSemConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXSemSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemAveragingType) """
        pass

    def GetCarrierChannelBandwidth(self, selectorString, value):
        """ GetCarrierChannelBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierEnabled(self, selectorString, value):
        """ GetCarrierEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemCarrierEnabled) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetCarrierRbwFilterAutoBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemCarrierRbwAutoBandwidth) """
        pass

    def GetCarrierRbwFilterBandwidth(self, selectorString, value):
        """ GetCarrierRbwFilterBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetCarrierRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition) """
        pass

    def GetCarrierRbwFilterType(self, selectorString, value):
        """ GetCarrierRbwFilterType(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemCarrierRbwFilterType) """
        pass

    def GetCarrierRrcFilterAlpha(self, selectorString, value):
        """ GetCarrierRrcFilterAlpha(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetCarrierRrcFilterEnabled(self, selectorString, value):
        """ GetCarrierRrcFilterEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemCarrierRrcFilterEnabled) """
        pass

    def GetFftPadding(self, selectorString, value):
        """ GetFftPadding(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfCarriers(self, selectorString, value):
        """ GetNumberOfCarriers(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfOffsets(self, selectorString, value):
        """ GetNumberOfOffsets(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetAbsoluteLimitMode(self, selectorString, value):
        """ GetOffsetAbsoluteLimitMode(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetAbsoluteLimitMode) """
        pass

    def GetOffsetAbsoluteLimitStart(self, selectorString, value):
        """ GetOffsetAbsoluteLimitStart(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetAbsoluteLimitStop(self, selectorString, value):
        """ GetOffsetAbsoluteLimitStop(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetBandwidthIntegral(self, selectorString, value):
        """ GetOffsetBandwidthIntegral(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetEnabled(self, selectorString, value):
        """ GetOffsetEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetEnabled) """
        pass

    def GetOffsetFrequencyDefinition(self, selectorString, value):
        """ GetOffsetFrequencyDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetFrequencyDefinition) """
        pass

    def GetOffsetLimitFailMask(self, selectorString, value):
        """ GetOffsetLimitFailMask(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetLimitFailMask) """
        pass

    def GetOffsetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetOffsetRbwFilterAutoBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetRbwAutoBandwidth) """
        pass

    def GetOffsetRbwFilterBandwidth(self, selectorString, value):
        """ GetOffsetRbwFilterBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetOffsetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition) """
        pass

    def GetOffsetRbwFilterType(self, selectorString, value):
        """ GetOffsetRbwFilterType(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetRbwFilterType) """
        pass

    def GetOffsetRelativeAttenuation(self, selectorString, value):
        """ GetOffsetRelativeAttenuation(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRelativeLimitMode(self, selectorString, value):
        """ GetOffsetRelativeLimitMode(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetRelativeLimitMode) """
        pass

    def GetOffsetRelativeLimitStart(self, selectorString, value):
        """ GetOffsetRelativeLimitStart(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRelativeLimitStop(self, selectorString, value):
        """ GetOffsetRelativeLimitStop(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetSideband(self, selectorString, value):
        """ GetOffsetSideband(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemOffsetSideband) """
        pass

    def GetOffsetStartFrequency(self, selectorString, value):
        """ GetOffsetStartFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetStopFrequency(self, selectorString, value):
        """ GetOffsetStopFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPowerUnits(self, selectorString, value):
        """ GetPowerUnits(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemPowerUnits) """
        pass

    def GetReferenceType(self, selectorString, value):
        """ GetReferenceType(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemReferenceType) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSemSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxSpecAnMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemAveragingType) -> int """
        pass

    def SetCarrierChannelBandwidth(self, selectorString, value):
        """ SetCarrierChannelBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierEnabled(self, selectorString, value):
        """ SetCarrierEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemCarrierEnabled) -> int """
        pass

    def SetCarrierFrequency(self, selectorString, value):
        """ SetCarrierFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierIntegrationBandwidth(self, selectorString, value):
        """ SetCarrierIntegrationBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetCarrierRbwFilterAutoBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemCarrierRbwAutoBandwidth) -> int """
        pass

    def SetCarrierRbwFilterBandwidth(self, selectorString, value):
        """ SetCarrierRbwFilterBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetCarrierRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemCarrierRbwFilterBandwidthDefinition) -> int """
        pass

    def SetCarrierRbwFilterType(self, selectorString, value):
        """ SetCarrierRbwFilterType(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemCarrierRbwFilterType) -> int """
        pass

    def SetCarrierRrcFilterAlpha(self, selectorString, value):
        """ SetCarrierRrcFilterAlpha(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetCarrierRrcFilterEnabled(self, selectorString, value):
        """ SetCarrierRrcFilterEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemCarrierRrcFilterEnabled) -> int """
        pass

    def SetFftPadding(self, selectorString, value):
        """ SetFftPadding(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfCarriers(self, selectorString, value):
        """ SetNumberOfCarriers(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfOffsets(self, selectorString, value):
        """ SetNumberOfOffsets(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetAbsoluteLimitMode(self, selectorString, value):
        """ SetOffsetAbsoluteLimitMode(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetAbsoluteLimitMode) -> int """
        pass

    def SetOffsetAbsoluteLimitStart(self, selectorString, value):
        """ SetOffsetAbsoluteLimitStart(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetAbsoluteLimitStop(self, selectorString, value):
        """ SetOffsetAbsoluteLimitStop(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetBandwidthIntegral(self, selectorString, value):
        """ SetOffsetBandwidthIntegral(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetEnabled(self, selectorString, value):
        """ SetOffsetEnabled(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetEnabled) -> int """
        pass

    def SetOffsetFrequencyDefinition(self, selectorString, value):
        """ SetOffsetFrequencyDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetFrequencyDefinition) -> int """
        pass

    def SetOffsetLimitFailMask(self, selectorString, value):
        """ SetOffsetLimitFailMask(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetLimitFailMask) -> int """
        pass

    def SetOffsetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetOffsetRbwFilterAutoBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetRbwAutoBandwidth) -> int """
        pass

    def SetOffsetRbwFilterBandwidth(self, selectorString, value):
        """ SetOffsetRbwFilterBandwidth(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetOffsetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition) -> int """
        pass

    def SetOffsetRbwFilterType(self, selectorString, value):
        """ SetOffsetRbwFilterType(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetRbwFilterType) -> int """
        pass

    def SetOffsetRelativeAttenuation(self, selectorString, value):
        """ SetOffsetRelativeAttenuation(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRelativeLimitMode(self, selectorString, value):
        """ SetOffsetRelativeLimitMode(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetRelativeLimitMode) -> int """
        pass

    def SetOffsetRelativeLimitStart(self, selectorString, value):
        """ SetOffsetRelativeLimitStart(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRelativeLimitStop(self, selectorString, value):
        """ SetOffsetRelativeLimitStop(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetSideband(self, selectorString, value):
        """ SetOffsetSideband(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemOffsetSideband) -> int """
        pass

    def SetOffsetStartFrequency(self, selectorString, value):
        """ SetOffsetStartFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetStopFrequency(self, selectorString, value):
        """ SetOffsetStopFrequency(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPowerUnits(self, selectorString, value):
        """ SetPowerUnits(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemPowerUnits) -> int """
        pass

    def SetReferenceType(self, selectorString, value):
        """ SetReferenceType(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemReferenceType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: RFmxSpecAnMXSemSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxSpecAnMXSemConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXSemFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXSemLowerOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemLowerOffsetMeasurementStatus, values: Fail (0), Pass (1) """
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

    Fail = None
    Pass = None
    value__ = None


class RFmxSpecAnMXSemOffsetAbsoluteLimitMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetAbsoluteLimitMode, values: Couple (1), Manual (0) """
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

    Couple = None
    Manual = None
    value__ = None


class RFmxSpecAnMXSemOffsetEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSemOffsetFrequencyDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetFrequencyDefinition, values: CarrierCenterToMeasurementBandwidthCenter (0), CarrierCenterToMeasurementBandwidthEdge (1), CarrierEdgeToMeasurementBandwidthCenter (2), CarrierEdgeToMeasurementBandwidthEdge (3) """
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

    CarrierCenterToMeasurementBandwidthCenter = None
    CarrierCenterToMeasurementBandwidthEdge = None
    CarrierEdgeToMeasurementBandwidthCenter = None
    CarrierEdgeToMeasurementBandwidthEdge = None
    value__ = None


class RFmxSpecAnMXSemOffsetLimitFailMask(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetLimitFailMask, values: Absolute (2), AbsoluteAndRelative (0), AbsoluteOrRelative (1), Relative (3) """
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

    Absolute = None
    AbsoluteAndRelative = None
    AbsoluteOrRelative = None
    Relative = None
    value__ = None


class RFmxSpecAnMXSemOffsetRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinitionBinWidth (2) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinitionBinWidth = None
    value__ = None


class RFmxSpecAnMXSemOffsetRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXSemOffsetRelativeLimitMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetRelativeLimitMode, values: Couple (1), Manual (0) """
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

    Couple = None
    Manual = None
    value__ = None


class RFmxSpecAnMXSemOffsetSideband(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemOffsetSideband, values: Both (2), Negative (0), Positive (1) """
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

    Both = None
    Negative = None
    Positive = None
    value__ = None


class RFmxSpecAnMXSemPowerUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemPowerUnits, values: dBm (0), dBmPerHertz (1) """
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

    dBm = None
    dBmPerHertz = None
    value__ = None


class RFmxSpecAnMXSemReferenceType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemReferenceType, values: Integration (0), Peak (1) """
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

    Integration = None
    Peak = None
    value__ = None


class RFmxSpecAnMXSemResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAbsoluteMaskTrace(self, selectorString, timeout, absoluteMask):
        """ FetchAbsoluteMaskTrace(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, absoluteMask: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchCarrierMeasurement(self, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, totalRelativePower):
        """ FetchCarrierMeasurement(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchCompositeMeasurementStatus(self, selectorString, timeout, compositeMeasurementStatus):
        """ FetchCompositeMeasurementStatus(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, RFmxSpecAnMXSemCompositeMeasurementStatus) """
        pass

    def FetchFrequencyResolution(self, selectorString, timeout, frequencyResolution):
        """ FetchFrequencyResolution(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchLowerOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMargin(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, RFmxSpecAnMXSemLowerOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchLowerOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMarginArray(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxSpecAnMXSemLowerOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxSpecAnMXSemLowerOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchLowerOffsetPower(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchLowerOffsetPower(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchLowerOffsetPowerArray(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchLowerOffsetPowerArray(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, totalAbsolutePower: Array[float], totalRelativePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], peakRelativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchRelativeMaskTrace(self, selectorString, timeout, relativeMask):
        """ FetchRelativeMaskTrace(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, relativeMask: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchTotalCarrierPower(self, selectorString, timeout, totalCarrierPower):
        """ FetchTotalCarrierPower(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchUpperOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMargin(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, RFmxSpecAnMXSemUpperOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchUpperOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMarginArray(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxSpecAnMXSemUpperOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxSpecAnMXSemUpperOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchUpperOffsetPower(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchUpperOffsetPower(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchUpperOffsetPowerArray(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchUpperOffsetPowerArray(self: RFmxSpecAnMXSemResults, selectorString: str, timeout: float, totalAbsolutePower: Array[float], totalRelativePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], peakRelativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetCarrierAbsolutePower(self, selectorString, value):
        """ GetCarrierAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierFrequency(self, selectorString, value):
        """ GetCarrierFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierPeakAbsolutePower(self, selectorString, value):
        """ GetCarrierPeakAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierPeakFrequency(self, selectorString, value):
        """ GetCarrierPeakFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierTotalRelativePower(self, selectorString, value):
        """ GetCarrierTotalRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositeMeasurementStatus(self, selectorString, value):
        """ GetCompositeMeasurementStatus(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, RFmxSpecAnMXSemCompositeMeasurementStatus) """
        pass

    def GetFrequencyResolution(self, selectorString, value):
        """ GetFrequencyResolution(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMargin(self, selectorString, value):
        """ GetLowerOffsetMargin(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetMarginAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginFrequency(self, selectorString, value):
        """ GetLowerOffsetMarginFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginRelativePower(self, selectorString, value):
        """ GetLowerOffsetMarginRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMeasurementStatus(self, selectorString, value):
        """ GetLowerOffsetMeasurementStatus(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, RFmxSpecAnMXSemLowerOffsetMeasurementStatus) """
        pass

    def GetLowerOffsetPeakAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetPeakAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetPeakFrequency(self, selectorString, value):
        """ GetLowerOffsetPeakFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetPeakRelativePower(self, selectorString, value):
        """ GetLowerOffsetPeakRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetPowerReferenceCarrier(self, selectorString, value):
        """ GetLowerOffsetPowerReferenceCarrier(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, int) """
        pass

    def GetLowerOffsetStartFrequency(self, selectorString, value):
        """ GetLowerOffsetStartFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetStopFrequency(self, selectorString, value):
        """ GetLowerOffsetStopFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetTotalAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetTotalAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetTotalRelativePower(self, selectorString, value):
        """ GetLowerOffsetTotalRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalCarrierPower(self, selectorString, value):
        """ GetTotalCarrierPower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMargin(self, selectorString, value):
        """ GetUpperOffsetMargin(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetMarginAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginFrequency(self, selectorString, value):
        """ GetUpperOffsetMarginFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginRelativePower(self, selectorString, value):
        """ GetUpperOffsetMarginRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMeasurementStatus(self, selectorString, value):
        """ GetUpperOffsetMeasurementStatus(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, RFmxSpecAnMXSemUpperOffsetMeasurementStatus) """
        pass

    def GetUpperOffsetPeakAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetPeakAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetPeakFrequency(self, selectorString, value):
        """ GetUpperOffsetPeakFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetPeakRelativePower(self, selectorString, value):
        """ GetUpperOffsetPeakRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetPowerReferenceCarrier(self, selectorString, value):
        """ GetUpperOffsetPowerReferenceCarrier(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, int) """
        pass

    def GetUpperOffsetStartFrequency(self, selectorString, value):
        """ GetUpperOffsetStartFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetStopFrequency(self, selectorString, value):
        """ GetUpperOffsetStopFrequency(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetTotalAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetTotalAbsolutePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetTotalRelativePower(self, selectorString, value):
        """ GetUpperOffsetTotalRelativePower(self: RFmxSpecAnMXSemResults, selectorString: str) -> (int, float) """
        pass


class RFmxSpecAnMXSemSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXSemUpperOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSemUpperOffsetMeasurementStatus, values: Fail (0), Pass (1) """
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

    Fail = None
    Pass = None
    value__ = None


class RFmxSpecAnMXSpectrum(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXSpectrum) -> RFmxSpecAnMXSpectrumConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXSpectrum) -> RFmxSpecAnMXSpectrumResults

"""



class RFmxSpecAnMXSpectrumAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXSpectrumAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSpectrumAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2), Vector (5) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RFmxSpecAnMXSpectrumConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingtype):
        """ ConfigureAveraging(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXSpectrumAveragingEnabled, averagingCount: int, averagingtype: RFmxSpecAnMXSpectrumAveragingType) -> int """
        pass

    def ConfigureDetector(self, selectorString, detectorType, detectorPoints):
        """ ConfigureDetector(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, detectorType: RFmxSpecAnMXSpectrumDetectorType, detectorPoints: int) -> int """
        pass

    def ConfigureFft(self, selectorString, fftWindow, fftPadding):
        """ ConfigureFft(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXSpectrumFftWindow, fftPadding: float) -> int """
        pass

    def ConfigureFrequencyStartStop(self, selectorString, startFrequency, stopFrequency):
        """ ConfigureFrequencyStartStop(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, startFrequency: float, stopFrequency: float) -> int """
        pass

    def ConfigureNoiseCompensationEnabled(self, selectorString, noiseCompensationEnabled):
        """ ConfigureNoiseCompensationEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, noiseCompensationEnabled: RFmxSpecAnMXSpectrumNoiseCompensationEnabled) -> int """
        pass

    def ConfigurePowerUnits(self, selectorString, powerUnits):
        """ ConfigurePowerUnits(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, powerUnits: RFmxSpecAnMXSpectrumPowerUnits) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXSpectrumRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXSpectrumRbwFilterType) -> int """
        pass

    def ConfigureSpan(self, selectorString, span):
        """ ConfigureSpan(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, span: float) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXSpectrumSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def ConfigureVbwFilter(self, selectorString, vbwAuto, vbw, vbwToRbwRatio):
        """ ConfigureVbwFilter(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, vbwAuto: RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth, vbw: float, vbwToRbwRatio: float) -> int """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumAveragingType) """
        pass

    def GetDetectorPoints(self, selectorString, value):
        """ GetDetectorPoints(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetDetectorType(self, selectorString, value):
        """ GetDetectorType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumDetectorType) """
        pass

    def GetFftPadding(self, selectorString, value):
        """ GetFftPadding(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNoiseCompensationEnabled(self, selectorString, value):
        """ GetNoiseCompensationEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumNoiseCompensationEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetPowerUnits(self, selectorString, value):
        """ GetPowerUnits(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumPowerUnits) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumRbwFilterBandwidthDefinition) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumRbwFilterType) """
        pass

    def GetSpan(self, selectorString, value):
        """ GetSpan(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetVbwFilterAutoBandwidth(self, selectorString, value):
        """ GetVbwFilterAutoBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth) """
        pass

    def GetVbwFilterBandwidth(self, selectorString, value):
        """ GetVbwFilterBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetVbwFilterVbwToRbwRatio(self, selectorString, value):
        """ GetVbwFilterVbwToRbwRatio(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumAveragingType) -> int """
        pass

    def SetDetectorPoints(self, selectorString, value):
        """ SetDetectorPoints(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetDetectorType(self, selectorString, value):
        """ SetDetectorType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumDetectorType) -> int """
        pass

    def SetFftPadding(self, selectorString, value):
        """ SetFftPadding(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNoiseCompensationEnabled(self, selectorString, value):
        """ SetNoiseCompensationEnabled(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumNoiseCompensationEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetPowerUnits(self, selectorString, value):
        """ SetPowerUnits(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumPowerUnits) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumRbwFilterBandwidthDefinition) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumRbwFilterType) -> int """
        pass

    def SetSpan(self, selectorString, value):
        """ SetSpan(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetVbwFilterAutoBandwidth(self, selectorString, value):
        """ SetVbwFilterAutoBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth) -> int """
        pass

    def SetVbwFilterBandwidth(self, selectorString, value):
        """ SetVbwFilterBandwidth(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetVbwFilterVbwToRbwRatio(self, selectorString, value):
        """ SetVbwFilterVbwToRbwRatio(self: RFmxSpecAnMXSpectrumConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXSpectrumDetectorType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumDetectorType, values: AverageLog (7), AverageRms (5), AverageVoltage (6), NegativePeak (4), None (0), Normal (2), Peak (3), Sample (1) """
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

    AverageLog = None
    AverageRms = None
    AverageVoltage = None
    NegativePeak = None
    None = None
    Normal = None
    Peak = None
    Sample = None
    value__ = None


class RFmxSpecAnMXSpectrumFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXSpectrumNoiseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumNoiseCompensationEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSpectrumPowerUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumPowerUnits, values: dBm (0), dBmPerHertz (1), dBmV (4), dBuV (5), dBV (3), dBW (2), ReferenceLevelUnits (9), Volts (7), VoltsSquared (8), Watts (6) """
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

    dBm = None
    dBmPerHertz = None
    dBmV = None
    dBuV = None
    dBV = None
    dBW = None
    ReferenceLevelUnits = None
    value__ = None
    Volts = None
    VoltsSquared = None
    Watts = None


class RFmxSpecAnMXSpectrumRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXSpectrumRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinition6dB (1), BandwidthDefinitionBinWidth (2), BandwidthDefinitionEnbw (3) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinition6dB = None
    BandwidthDefinitionBinWidth = None
    BandwidthDefinitionEnbw = None
    value__ = None


class RFmxSpecAnMXSpectrumRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXSpectrumResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, peakAmplitude, peakFrequency, frequencyResolution):
        """ FetchMeasurement(self: RFmxSpecAnMXSpectrumResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchPowerTrace(self, selectorString, timeout, power):
        """ FetchPowerTrace(self: RFmxSpecAnMXSpectrumResults, selectorString: str, timeout: float, power: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxSpecAnMXSpectrumResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def GetFrequencyResolution(self, selectorString, value):
        """ GetFrequencyResolution(self: RFmxSpecAnMXSpectrumResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakAmplitude(self, selectorString, value):
        """ GetPeakAmplitude(self: RFmxSpecAnMXSpectrumResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakFrequency(self, selectorString, value):
        """ GetPeakFrequency(self: RFmxSpecAnMXSpectrumResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, spectrum):
        """ Read(self: RFmxSpecAnMXSpectrumResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass


class RFmxSpecAnMXSpectrumSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpectrumVbwFilterAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXSpur(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXSpur) -> RFmxSpecAnMXSpurConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXSpur) -> RFmxSpecAnMXSpurResults

"""



class RFmxSpecAnMXSpurAbsoluteLimitMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurAbsoluteLimitMode, values: Couple (1), Manual (0) """
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

    Couple = None
    Manual = None
    value__ = None


class RFmxSpecAnMXSpurAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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

    RFCenterFrequency = None
    SpectrumFrequencyBin = None
    value__ = None


class RFmxSpecAnMXSpurAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSpurAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2), Vector (5) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RFmxSpecAnMXSpurConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXSpurAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXSpurAveragingType) -> int """
        pass

    def ConfigureFftWindowType(self, selectorString, fftWindow):
        """ ConfigureFftWindowType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, fftWindow: RFmxSpecAnMXSpurFftWindow) -> int """
        pass

    def ConfigureNumberOfRanges(self, selectorString, numberOfRanges):
        """ ConfigureNumberOfRanges(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, numberOfRanges: int) -> int """
        pass

    def ConfigureRangeAbsoluteLimit(self, selectorString, absoluteLimitMode, absoluteLimitStart, absoluteLimitStop):
        """ ConfigureRangeAbsoluteLimit(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, absoluteLimitMode: RFmxSpecAnMXSpurAbsoluteLimitMode, absoluteLimitStart: float, absoluteLimitStop: float) -> int """
        pass

    def ConfigureRangeAbsoluteLimitArray(self, selectorString, absoluteLimitMode, absoluteLimitStart, absoluteLimitStop):
        """ ConfigureRangeAbsoluteLimitArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, absoluteLimitMode: Array[RFmxSpecAnMXSpurAbsoluteLimitMode], absoluteLimitStart: Array[float], absoluteLimitStop: Array[float]) -> int """
        pass

    def ConfigureRangeDetector(self, selectorString, detectorType, detectorPoints):
        """ ConfigureRangeDetector(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, detectorType: RFmxSpecAnMXSpurRangeDetectorType, detectorPoints: int) -> int """
        pass

    def ConfigureRangeDetectorArray(self, selectorString, detectorType, detectorPoints):
        """ ConfigureRangeDetectorArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, detectorType: Array[RFmxSpecAnMXSpurRangeDetectorType], detectorPoints: Array[int]) -> int """
        pass

    def ConfigureRangeFrequency(self, selectorString, startFrequency, stopFrequency, rangeEnabled):
        """ ConfigureRangeFrequency(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, startFrequency: float, stopFrequency: float, rangeEnabled: RFmxSpecAnMXSpurRangeEnabled) -> int """
        pass

    def ConfigureRangeFrequencyArray(self, selectorString, startFrequency, stopFrequency, rangeEnabled):
        """ ConfigureRangeFrequencyArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, startFrequency: Array[float], stopFrequency: Array[float], rangeEnabled: Array[RFmxSpecAnMXSpurRangeEnabled]) -> int """
        pass

    def ConfigureRangeNumberOfSpursToReport(self, selectorString, numberOfSpursToReport):
        """ ConfigureRangeNumberOfSpursToReport(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, numberOfSpursToReport: int) -> int """
        pass

    def ConfigureRangeNumberOfSpursToReportArray(self, selectorString, numberOfSpursToReport):
        """ ConfigureRangeNumberOfSpursToReportArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, numberOfSpursToReport: Array[int]) -> int """
        pass

    def ConfigureRangePeakCriteria(self, selectorString, threshold, excursion):
        """ ConfigureRangePeakCriteria(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, threshold: float, excursion: float) -> int """
        pass

    def ConfigureRangePeakCriteriaArray(self, selectorString, threshold, excursion):
        """ ConfigureRangePeakCriteriaArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, threshold: Array[float], excursion: Array[float]) -> int """
        pass

    def ConfigureRangeRbwArray(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRangeRbwArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, rbwAuto: Array[RFmxSpecAnMXSpurRbwAutoBandwidth], rbw: Array[float], rbwFilterType: Array[RFmxSpecAnMXSpurRbwFilterType]) -> int """
        pass

    def ConfigureRangeRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRangeRbwFilter(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, rbwAuto: RFmxSpecAnMXSpurRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxSpecAnMXSpurRbwFilterType) -> int """
        pass

    def ConfigureRangeRelativeAttenuation(self, selectorString, relativeAttenuation):
        """ ConfigureRangeRelativeAttenuation(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, relativeAttenuation: float) -> int """
        pass

    def ConfigureRangeRelativeAttenuationArray(self, selectorString, relativeAttenuation):
        """ ConfigureRangeRelativeAttenuationArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, relativeAttenuation: Array[float]) -> int """
        pass

    def ConfigureRangeSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureRangeSweepTime(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, sweepTimeAuto: RFmxSpecAnMXSpurSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def ConfigureRangeSweepTimeArray(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureRangeSweepTimeArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, sweepTimeAuto: Array[RFmxSpecAnMXSpurSweepTimeAuto], sweepTimeInterval: Array[float]) -> int """
        pass

    def ConfigureRangeVbwFilter(self, selectorString, vbwAuto, vbw, vbwToRbwRatio):
        """ ConfigureRangeVbwFilter(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, vbwAuto: RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth, vbw: float, vbwToRbwRatio: float) -> int """
        pass

    def ConfigureRangeVbwFilterArray(self, selectorString, vbwAuto, vbw, vbwToRbwRatio):
        """ ConfigureRangeVbwFilterArray(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, vbwAuto: Array[RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth], vbw: Array[float], vbwToRbwRatio: Array[float]) -> int """
        pass

    def ConfigureTraceRangeIndex(self, selectorString, traceRangeIndex):
        """ ConfigureTraceRangeIndex(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, traceRangeIndex: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurAveragingType) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfRanges(self, selectorString, value):
        """ GetNumberOfRanges(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRangeAbsoluteLimitMode(self, selectorString, value):
        """ GetRangeAbsoluteLimitMode(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurAbsoluteLimitMode) """
        pass

    def GetRangeAbsoluteLimitStart(self, selectorString, value):
        """ GetRangeAbsoluteLimitStart(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeAbsoluteLimitStop(self, selectorString, value):
        """ GetRangeAbsoluteLimitStop(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeDetectorPoints(self, selectorString, value):
        """ GetRangeDetectorPoints(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRangeDetectorType(self, selectorString, value):
        """ GetRangeDetectorType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurRangeDetectorType) """
        pass

    def GetRangeEnabled(self, selectorString, value):
        """ GetRangeEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurRangeEnabled) """
        pass

    def GetRangeNumberOfSpursToReport(self, selectorString, value):
        """ GetRangeNumberOfSpursToReport(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRangePeakExcursion(self, selectorString, value):
        """ GetRangePeakExcursion(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangePeakThreshold(self, selectorString, value):
        """ GetRangePeakThreshold(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRangeRbwFilterAutoBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurRbwAutoBandwidth) """
        pass

    def GetRangeRbwFilterBandwidth(self, selectorString, value):
        """ GetRangeRbwFilterBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeRbwFilterBandwidthDefinition(self, selectorString, value):
        """ GetRangeRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurRbwFilterBandwidthDefinition) """
        pass

    def GetRangeRbwFilterType(self, selectorString, value):
        """ GetRangeRbwFilterType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurRbwFilterType) """
        pass

    def GetRangeRelativeAttenuation(self, selectorString, value):
        """ GetRangeRelativeAttenuation(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeStartFrequency(self, selectorString, value):
        """ GetRangeStartFrequency(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeStopFrequency(self, selectorString, value):
        """ GetRangeStopFrequency(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeSweepTimeAuto(self, selectorString, value):
        """ GetRangeSweepTimeAuto(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurSweepTimeAuto) """
        pass

    def GetRangeSweepTimeInterval(self, selectorString, value):
        """ GetRangeSweepTimeInterval(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeVbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRangeVbwFilterAutoBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) """
        pass

    def GetRangeVbwFilterBandwidth(self, selectorString, value):
        """ GetRangeVbwFilterBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRangeVbwFilterVbwToRbwRatio(self, selectorString, value):
        """ GetRangeVbwFilterVbwToRbwRatio(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetTraceRangeIndex(self, selectorString, value):
        """ GetTraceRangeIndex(self: RFmxSpecAnMXSpurConfiguration, selectorString: str) -> (int, int) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurAveragingType) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfRanges(self, selectorString, value):
        """ SetNumberOfRanges(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRangeAbsoluteLimitMode(self, selectorString, value):
        """ SetRangeAbsoluteLimitMode(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurAbsoluteLimitMode) -> int """
        pass

    def SetRangeAbsoluteLimitStart(self, selectorString, value):
        """ SetRangeAbsoluteLimitStart(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeAbsoluteLimitStop(self, selectorString, value):
        """ SetRangeAbsoluteLimitStop(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeDetectorPoints(self, selectorString, value):
        """ SetRangeDetectorPoints(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRangeDetectorType(self, selectorString, value):
        """ SetRangeDetectorType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurRangeDetectorType) -> int """
        pass

    def SetRangeEnabled(self, selectorString, value):
        """ SetRangeEnabled(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurRangeEnabled) -> int """
        pass

    def SetRangeNumberOfSpursToReport(self, selectorString, value):
        """ SetRangeNumberOfSpursToReport(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRangePeakExcursion(self, selectorString, value):
        """ SetRangePeakExcursion(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangePeakThreshold(self, selectorString, value):
        """ SetRangePeakThreshold(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRangeRbwFilterAutoBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurRbwAutoBandwidth) -> int """
        pass

    def SetRangeRbwFilterBandwidth(self, selectorString, value):
        """ SetRangeRbwFilterBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeRbwFilterBandwidthDefinition(self, selectorString, value):
        """ SetRangeRbwFilterBandwidthDefinition(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurRbwFilterBandwidthDefinition) -> int """
        pass

    def SetRangeRbwFilterType(self, selectorString, value):
        """ SetRangeRbwFilterType(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurRbwFilterType) -> int """
        pass

    def SetRangeRelativeAttenuation(self, selectorString, value):
        """ SetRangeRelativeAttenuation(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeStartFrequency(self, selectorString, value):
        """ SetRangeStartFrequency(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeStopFrequency(self, selectorString, value):
        """ SetRangeStopFrequency(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeSweepTimeAuto(self, selectorString, value):
        """ SetRangeSweepTimeAuto(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurSweepTimeAuto) -> int """
        pass

    def SetRangeSweepTimeInterval(self, selectorString, value):
        """ SetRangeSweepTimeInterval(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeVbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRangeVbwFilterAutoBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth) -> int """
        pass

    def SetRangeVbwFilterBandwidth(self, selectorString, value):
        """ SetRangeVbwFilterBandwidth(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRangeVbwFilterVbwToRbwRatio(self, selectorString, value):
        """ SetRangeVbwFilterVbwToRbwRatio(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetTraceRangeIndex(self, selectorString, value):
        """ SetTraceRangeIndex(self: RFmxSpecAnMXSpurConfiguration, selectorString: str, value: int) -> int """
        pass


class RFmxSpecAnMXSpurFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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

    Blackman = None
    BlackmanHarris = None
    FlatTop = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    None = None
    value__ = None


class RFmxSpecAnMXSpurMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurMeasurementStatus, values: Fail (0), Pass (1) """
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

    Fail = None
    Pass = None
    value__ = None


class RFmxSpecAnMXSpurRangeDetectorType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRangeDetectorType, values: AverageLog (7), AverageRms (5), AverageVoltage (6), NegativePeak (4), None (0), Normal (2), Peak (3), Sample (1) """
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

    AverageLog = None
    AverageRms = None
    AverageVoltage = None
    NegativePeak = None
    None = None
    Normal = None
    Peak = None
    Sample = None
    value__ = None


class RFmxSpecAnMXSpurRangeEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRangeEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXSpurRangeStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRangeStatus, values: Fail (0), Pass (1) """
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

    Fail = None
    Pass = None
    value__ = None


class RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRangeVbwFilterAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXSpurRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxSpecAnMXSpurRbwFilterBandwidthDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRbwFilterBandwidthDefinition, values: BandwidthDefinition3dB (0), BandwidthDefinitionBinWidth (2), BandwidthDefinitionEnbw (3) """
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

    BandwidthDefinition3dB = None
    BandwidthDefinitionBinWidth = None
    BandwidthDefinitionEnbw = None
    value__ = None


class RFmxSpecAnMXSpurRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1), SynchTuned4 (3), SynchTuned5 (4) """
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

    FftBased = None
    Flat = None
    Gaussian = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXSpurResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchAllSpurs(self, selectorString, timeout, spurFrequency, spurAmplitude, spurMargin, spurAbsoluteLimit, spurRangeTraceIndex):
        """ FetchAllSpurs(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float, spurFrequency: Array[float], spurAmplitude: Array[float], spurMargin: Array[float], spurAbsoluteLimit: Array[float], spurRangeTraceIndex: Array[int]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[int]) """
        pass

    def FetchMeasurementStatus(self, selectorString, timeout, measurementStatus):
        """ FetchMeasurementStatus(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float) -> (int, RFmxSpecAnMXSpurMeasurementStatus) """
        pass

    def FetchRangeAbsoluteLimitTrace(self, selectorString, timeout, absoluteLimit):
        """ FetchRangeAbsoluteLimitTrace(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float, absoluteLimit: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchRangeSpectrumTrace(self, selectorString, timeout, rangeSpectrum):
        """ FetchRangeSpectrumTrace(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float, rangeSpectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchRangeStatus(self, selectorString, timeout, rangeStatus, detectedSpurs):
        """ FetchRangeStatus(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float) -> (int, RFmxSpecAnMXSpurRangeStatus, int) """
        pass

    def FetchRangeStatusArray(self, selectorString, timeout, rangeStatus, numberOfDetectedSpurs):
        """ FetchRangeStatusArray(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float, rangeStatus: Array[RFmxSpecAnMXSpurRangeStatus], numberOfDetectedSpurs: Array[int]) -> (int, Array[RFmxSpecAnMXSpurRangeStatus], Array[int]) """
        pass

    def FetchSpurMeasurement(self, selectorString, timeout, spurFrequency, spurAmplitude, spurMargin, spurAbsoluteLimit):
        """ FetchSpurMeasurement(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchSpurMeasurementArray(self, selectorString, timeout, spurFrequency, spurAmplitude, spurAbsoluteLimit, spurMargin):
        """ FetchSpurMeasurementArray(self: RFmxSpecAnMXSpurResults, selectorString: str, timeout: float, spurFrequency: Array[float], spurAmplitude: Array[float], spurAbsoluteLimit: Array[float], spurMargin: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetMeasurementStatus(self, selectorString, value):
        """ GetMeasurementStatus(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, RFmxSpecAnMXSpurMeasurementStatus) """
        pass

    def GetRangeMeasurementStatus(self, selectorString, value):
        """ GetRangeMeasurementStatus(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, RFmxSpecAnMXSpurRangeStatus) """
        pass

    def GetRangeSpurAbsoluteLimit(self, selectorString, value):
        """ GetRangeSpurAbsoluteLimit(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, float) """
        pass

    def GetRangeSpurAmplitude(self, selectorString, value):
        """ GetRangeSpurAmplitude(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, float) """
        pass

    def GetRangeSpurFrequency(self, selectorString, value):
        """ GetRangeSpurFrequency(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, float) """
        pass

    def GetRangeSpurMargin(self, selectorString, value):
        """ GetRangeSpurMargin(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, float) """
        pass

    def GetRangeSpurNumberOfDetectedSpurs(self, selectorString, value):
        """ GetRangeSpurNumberOfDetectedSpurs(self: RFmxSpecAnMXSpurResults, selectorString: str) -> (int, int) """
        pass


class RFmxSpecAnMXSpurSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXSpurSweepTimeAuto, values: False (0), True (1) """
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


class RFmxSpecAnMXTriggerMinimumQuietTimeMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTriggerMinimumQuietTimeMode, values: Auto (1), Manual (0) """
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
    Manual = None
    value__ = None


class RFmxSpecAnMXTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTriggerType, values: DigitalEdge (1), IQPowerEdge (2), None (0), Software (3) """
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

    DigitalEdge = None
    IQPowerEdge = None
    None = None
    Software = None
    value__ = None


class RFmxSpecAnMXTxp(RFmxSpecAnMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxSpecAnMXTxp) -> RFmxSpecAnMXTxpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxSpecAnMXTxp) -> RFmxSpecAnMXTxpResults

"""



class RFmxSpecAnMXTxpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTxpAveragingEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXTxpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTxpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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

    Log = None
    Maximum = None
    Minimum = None
    Rms = None
    Scalar = None
    value__ = None


class RFmxSpecAnMXTxpConfiguration(RFmxSpecAnMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, averagingEnabled: RFmxSpecAnMXTxpAveragingEnabled, averagingCount: int, averagingType: RFmxSpecAnMXTxpAveragingType) -> int """
        pass

    def ConfigureMeasurementInterval(self, selectorString, measurementInterval):
        """ ConfigureMeasurementInterval(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, measurementInterval: float) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbw, RbwFilterType, rrcAlpha):
        """ ConfigureRbwFilter(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, rbw: float, RbwFilterType: RFmxSpecAnMXTxpRbwFilterType, rrcAlpha: float) -> int """
        pass

    def ConfigureThreshold(self, selectorString, thresholdEnabled, thresholdLevel, thresholdType):
        """ ConfigureThreshold(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, thresholdEnabled: RFmxSpecAnMXTxpThresholdEnabled, thresholdLevel: float, thresholdType: RFmxSpecAnMXTxpThresholdType) -> int """
        pass

    def ConfigureVbwFilter(self, selectorString, vbwAuto, vbw, vbwToRbwRatio):
        """ ConfigureVbwFilter(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, vbwAuto: RFmxSpecAnMXTxpVbwFilterAutoBandwidth, vbw: float, vbwToRbwRatio: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXTxpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXTxpAveragingType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementInterval(self, selectorString, value):
        """ GetMeasurementInterval(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAlpha(self, selectorString, value):
        """ GetRbwFilterAlpha(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXTxpRbwFilterType) """
        pass

    def GetThresholdEnabled(self, selectorString, value):
        """ GetThresholdEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXTxpThresholdEnabled) """
        pass

    def GetThresholdLevel(self, selectorString, value):
        """ GetThresholdLevel(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetThresholdType(self, selectorString, value):
        """ GetThresholdType(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXTxpThresholdType) """
        pass

    def GetVbwFilterAutoBandwidth(self, selectorString, value):
        """ GetVbwFilterAutoBandwidth(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, RFmxSpecAnMXTxpVbwFilterAutoBandwidth) """
        pass

    def GetVbwFilterBandwidth(self, selectorString, value):
        """ GetVbwFilterBandwidth(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetVbwFilterVbwToRbwRatio(self, selectorString, value):
        """ GetVbwFilterVbwToRbwRatio(self: RFmxSpecAnMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: RFmxSpecAnMXTxpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: RFmxSpecAnMXTxpAveragingType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementInterval(self, selectorString, value):
        """ SetMeasurementInterval(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAlpha(self, selectorString, value):
        """ SetRbwFilterAlpha(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: RFmxSpecAnMXTxpRbwFilterType) -> int """
        pass

    def SetThresholdEnabled(self, selectorString, value):
        """ SetThresholdEnabled(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: RFmxSpecAnMXTxpThresholdEnabled) -> int """
        pass

    def SetThresholdLevel(self, selectorString, value):
        """ SetThresholdLevel(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetThresholdType(self, selectorString, value):
        """ SetThresholdType(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: RFmxSpecAnMXTxpThresholdType) -> int """
        pass

    def SetVbwFilterAutoBandwidth(self, selectorString, value):
        """ SetVbwFilterAutoBandwidth(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: RFmxSpecAnMXTxpVbwFilterAutoBandwidth) -> int """
        pass

    def SetVbwFilterBandwidth(self, selectorString, value):
        """ SetVbwFilterBandwidth(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetVbwFilterVbwToRbwRatio(self, selectorString, value):
        """ SetVbwFilterVbwToRbwRatio(self: RFmxSpecAnMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxSpecAnMXTxpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTxpRbwFilterType, values: Flat (2), Gaussian (1), None (5), Rrc (6), SynchTuned4 (3), SynchTuned5 (4) """
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

    Flat = None
    Gaussian = None
    None = None
    Rrc = None
    SynchTuned4 = None
    SynchTuned5 = None
    value__ = None


class RFmxSpecAnMXTxpResults(RFmxSpecAnMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, averageMeanPower, peakToAverageRatio, maximumPower, minimumPower):
        """ FetchMeasurement(self: RFmxSpecAnMXTxpResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPowerTrace(self, selectorString, timeout, power):
        """ FetchPowerTrace(self: RFmxSpecAnMXTxpResults, selectorString: str, timeout: float, power: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def GetAverageMeanPower(self, selectorString, value):
        """ GetAverageMeanPower(self: RFmxSpecAnMXTxpResults, selectorString: str) -> (int, float) """
        pass

    def GetMaximumPower(self, selectorString, value):
        """ GetMaximumPower(self: RFmxSpecAnMXTxpResults, selectorString: str) -> (int, float) """
        pass

    def GetMinimumPower(self, selectorString, value):
        """ GetMinimumPower(self: RFmxSpecAnMXTxpResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakToAverageRatio(self, selectorString, value):
        """ GetPeakToAverageRatio(self: RFmxSpecAnMXTxpResults, selectorString: str) -> (int, float) """
        pass

    def Read(self, selectorString, timeout, averageMeanPower, peakToAverageRatio, maximumPower, minimumPower):
        """ Read(self: RFmxSpecAnMXTxpResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass


class RFmxSpecAnMXTxpThresholdEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTxpThresholdEnabled, values: False (0), True (1) """
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


class RFmxSpecAnMXTxpThresholdType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTxpThresholdType, values: Absolute (1), Relative (0) """
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

    Absolute = None
    Relative = None
    value__ = None


class RFmxSpecAnMXTxpVbwFilterAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxSpecAnMXTxpVbwFilterAutoBandwidth, values: False (0), True (1) """
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


