# encoding: utf-8
# module NationalInstruments.RFmx.InstrMX calls itself InstrMX
# from NationalInstruments.RFmx.InstrMX.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ISignalConfiguration:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SignalConfigurationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationName(self: ISignalConfiguration) -> str"""

    SignalConfigurationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationType(self: ISignalConfiguration) -> Type"""


class RFmxException(Exception, ISerializable, _Exception):
    """
    RFmxException()

    RFmxException(message: str)

    RFmxException(message: str, innerException: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: RFmxException, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)

        __new__(cls: type, message: str)

        __new__(cls: type, message: str, innerException: Exception)

        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class RFmxInstrMX(object, IDisposable):
    """
    RFmxInstrMX(instrumentHandle: IntPtr)

    RFmxInstrMX(resourceName: str, optionString: str)
    """
    @staticmethod
    def BuildCalibrationPlaneString(calibrationPlaneName):
        """ BuildCalibrationPlaneString(calibrationPlaneName: str) -> str """
        pass

    @staticmethod
    def BuildLOString(selectorString, loIndex):
        """ BuildLOString(selectorString: str, loIndex: int) -> str """
        pass

    @staticmethod
    def BuildModuleString(selectorString, moduleName):
        """ BuildModuleString(selectorString: str, moduleName: str) -> str """
        pass

    @staticmethod
    def BuildPortString(selectorString, portName):
        """ BuildPortString(selectorString: str, portName: str) -> str """
        pass

    def CheckAcquisitionStatus(self, done):
        """ CheckAcquisitionStatus(self: RFmxInstrMX) -> (int, bool) """
        pass

    def CheckIfSignalExists(self, signalName, signalConfigurationExists, personality):
        """ CheckIfSignalExists(self: RFmxInstrMX, signalName: str) -> (int, bool, RFmxInstrMXPersonalities) """
        pass

    def Close(self):
        """ Close(self: RFmxInstrMX) """
        pass

    def ConfigureAutomaticSGSASharedLO(self, selectorString, automaticSGSASharedLO):
        """ ConfigureAutomaticSGSASharedLO(self: RFmxInstrMX, selectorString: str, automaticSGSASharedLO: RFmxInstrMXAutomaticSGSASharedLO) -> int """
        pass

    def ConfigureExternalAttenuationInterpolationLinear(self, selectorString, tableName, format):
        """ ConfigureExternalAttenuationInterpolationLinear(self: RFmxInstrMX, selectorString: str, tableName: str, format: RFmxInstrMXLinearInterpolationFormat) -> int """
        pass

    def ConfigureExternalAttenuationInterpolationNearest(self, selectorString, tableName):
        """ ConfigureExternalAttenuationInterpolationNearest(self: RFmxInstrMX, selectorString: str, tableName: str) -> int """
        pass

    def ConfigureExternalAttenuationInterpolationSpline(self, selectorString, tableName):
        """ ConfigureExternalAttenuationInterpolationSpline(self: RFmxInstrMX, selectorString: str, tableName: str) -> int """
        pass

    def ConfigureExternalAttenuationTable(self, selectorString, tableName, frequency, externalAttenuation):
        """ ConfigureExternalAttenuationTable(self: RFmxInstrMX, selectorString: str, tableName: str, frequency: Array[float], externalAttenuation: Array[float]) -> int """
        pass

    def ConfigureFrequencyReference(self, channelName, frequencyReferenceSource, frequencyReferenceFrequency):
        """ ConfigureFrequencyReference(self: RFmxInstrMX, channelName: str, frequencyReferenceSource: str, frequencyReferenceFrequency: float) -> int """
        pass

    def ConfigureMechanicalAttenuation(self, channelName, mechanicalAttenuationAuto, mechanicalAttenuationValue):
        """ ConfigureMechanicalAttenuation(self: RFmxInstrMX, channelName: str, mechanicalAttenuationAuto: RFmxInstrMXMechanicalAttenuationAuto, mechanicalAttenuationValue: float) -> int """
        pass

    def ConfigureRFAttenuation(self, channelName, attenuationAuto, attenuationValue):
        """ ConfigureRFAttenuation(self: RFmxInstrMX, channelName: str, attenuationAuto: RFmxInstrMXRFAttenuationAuto, attenuationValue: float) -> int """
        pass

    def ConfigureSParameterExternalAttenuationTable(self, selectorString, tableName, frequency, sParameters, sParameterOrientation):
        """ ConfigureSParameterExternalAttenuationTable(self: RFmxInstrMX, selectorString: str, tableName: str, frequency: Array[float], sParameters: Array[ComplexDouble], sParameterOrientation: RFmxInstrMXSParameterOrientation) -> int """
        pass

    def ConfigureSParameterExternalAttenuationType(self, selectorString, sParameterType):
        """ ConfigureSParameterExternalAttenuationType(self: RFmxInstrMX, selectorString: str, sParameterType: RFmxInstrMXSParameterType) -> int """
        pass

    def ConvertForPowerUnitsUtility(self, referenceOrTriggerLevelIn, inputPowerUnits, outputPowerUnits, terminalConfiguration, bandwidth, referenceOrTriggerLevelOut):
        """ ConvertForPowerUnitsUtility(self: RFmxInstrMX, referenceOrTriggerLevelIn: float, inputPowerUnits: RFmxInstrMXPowerUnits, outputPowerUnits: RFmxInstrMXPowerUnits, terminalConfiguration: RFmxInstrMXTerminalConfiguration, bandwidth: float) -> (int, float) """
        pass

    def DangerousGetInstrumentHandle(self):
        """ DangerousGetInstrumentHandle(self: RFmxInstrMX) -> IntPtr """
        pass

    def DangerousGetNIRfsaHandle(self, niRfsaHandle):
        """ DangerousGetNIRfsaHandle(self: RFmxInstrMX) -> (int, IntPtr) """
        pass

    def DangerousGetNIRfsaHandleArray(self, niRfsaSessions):
        """ DangerousGetNIRfsaHandleArray(self: RFmxInstrMX, niRfsaSessions: Array[IntPtr]) -> (int, Array[IntPtr]) """
        pass

    def DeleteAllExternalAttenuationTables(self, selectorString):
        """ DeleteAllExternalAttenuationTables(self: RFmxInstrMX, selectorString: str) -> int """
        pass

    def DeleteExternalAttenuationTable(self, selectorString, tableName):
        """ DeleteExternalAttenuationTable(self: RFmxInstrMX, selectorString: str, tableName: str) -> int """
        pass

    def DeleteSnapshot(self, personalityID, selectorString):
        """ DeleteSnapshot(self: RFmxInstrMX, personalityID: int, selectorString: str) -> int """
        pass

    def DisableCalibrationPlane(self, selectorString):
        """ DisableCalibrationPlane(self: RFmxInstrMX, selectorString: str) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: RFmxInstrMX) """
        pass

    def EnableCalibrationPlane(self, selectorString):
        """ EnableCalibrationPlane(self: RFmxInstrMX, selectorString: str) -> int """
        pass

    def ExportSignal(self, exportSignalSource, exportSignalOutputTerminal):
        """ ExportSignal(self: RFmxInstrMX, exportSignalSource: RFmxInstrMXExportSignalSource, exportSignalOutputTerminal: str) -> int """
        pass

    def ForceClose(self):
        """ ForceClose(self: RFmxInstrMX) """
        pass

    def GetActiveResultName(self, signalName, personality, resultName, resultState):
        """ GetActiveResultName(self: RFmxInstrMX, signalName: str, personality: RFmxInstrMXPersonalities) -> (int, str, int) """
        pass

    def GetActiveTableName(self, selectorString, activeTableName):
        """ GetActiveTableName(self: RFmxInstrMX, selectorString: str) -> (int, str) """
        pass

    def GetAllLoadedPersonalities(self, selectorString, personality):
        """ GetAllLoadedPersonalities(self: RFmxInstrMX, selectorString: str, personality: Array[RFmxInstrMXPersonalities]) -> (int, Array[RFmxInstrMXPersonalities]) """
        pass

    def GetAmplitudeSettling(self, channelName, value):
        """ GetAmplitudeSettling(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetAttributeAuthor(self, selectorString, attributeIdentifier, value):
        """ GetAttributeAuthor(self: RFmxInstrMX, selectorString: str, attributeIdentifier: int) -> (int, RFmxInstrMXAttributeAuthor) """
        pass

    def GetAttributeBool(self, channelName, attributeIdentifier, value):
        """ GetAttributeBool(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, bool) """
        pass

    def GetAttributeByte(self, channelName, attributeIdentifier, value):
        """ GetAttributeByte(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Byte) """
        pass

    def GetAttributeByteArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeByteArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Byte]) -> (int, Array[Byte]) """
        pass

    def GetAttributeComplexDoubleArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeComplexDoubleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[ComplexDouble]) -> (int, Array[ComplexDouble]) """
        pass

    def GetAttributeComplexSingleArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeComplexSingleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def GetAttributeDesiredBool(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredBool(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, bool) """
        pass

    def GetAttributeDesiredByte(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredByte(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Byte) """
        pass

    def GetAttributeDesiredByteArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredByteArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Byte]) -> (int, Array[Byte]) """
        pass

    def GetAttributeDesiredComplexDoubleArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredComplexDoubleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[ComplexDouble]) -> (int, Array[ComplexDouble]) """
        pass

    def GetAttributeDesiredComplexSingleArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredComplexSingleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def GetAttributeDesiredDouble(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredDouble(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, float) """
        pass

    def GetAttributeDesiredDoubleArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredDoubleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetAttributeDesiredFloat(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredFloat(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Single) """
        pass

    def GetAttributeDesiredFloatArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredFloatArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetAttributeDesiredInt(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredInt(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, int) """
        pass

    def GetAttributeDesiredIntArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredIntArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[int]) -> (int, Array[int]) """
        pass

    def GetAttributeDesiredLong(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredLong(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Int64) """
        pass

    def GetAttributeDesiredLongArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredLongArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Int64]) -> (int, Array[Int64]) """
        pass

    def GetAttributeDesiredSByte(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredSByte(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, SByte) """
        pass

    def GetAttributeDesiredSByteArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredSByteArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[SByte]) -> (int, Array[SByte]) """
        pass

    def GetAttributeDesiredShort(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredShort(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Int16) """
        pass

    def GetAttributeDesiredString(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredString(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, str) """
        pass

    def GetAttributeDesiredUInt(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredUInt(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, UInt32) """
        pass

    def GetAttributeDesiredUIntArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredUIntArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[UInt32]) -> (int, Array[UInt32]) """
        pass

    def GetAttributeDesiredULongArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredULongArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[UInt64]) -> (int, Array[UInt64]) """
        pass

    def GetAttributeDesiredUShort(self, channelName, attributeIdentifier, value):
        """ GetAttributeDesiredUShort(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, UInt16) """
        pass

    def GetAttributeDouble(self, channelName, attributeIdentifier, value):
        """ GetAttributeDouble(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, float) """
        pass

    def GetAttributeDoubleArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeDoubleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[float]) -> (int, Array[float]) """
        pass

    def GetAttributeFloat(self, channelName, attributeIdentifier, value):
        """ GetAttributeFloat(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Single) """
        pass

    def GetAttributeFloatArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeFloatArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Single]) -> (int, Array[Single]) """
        pass

    def GetAttributeInt(self, channelName, attributeIdentifier, value):
        """ GetAttributeInt(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, int) """
        pass

    def GetAttributeIntArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeIntArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[int]) -> (int, Array[int]) """
        pass

    def GetAttributeLong(self, channelName, attributeIdentifier, value):
        """ GetAttributeLong(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Int64) """
        pass

    def GetAttributeLongArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeLongArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Int64]) -> (int, Array[Int64]) """
        pass

    def GetAttributeSByte(self, channelName, attributeIdentifier, value):
        """ GetAttributeSByte(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, SByte) """
        pass

    def GetAttributeSByteArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeSByteArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[SByte]) -> (int, Array[SByte]) """
        pass

    def GetAttributeShort(self, channelName, attributeIdentifier, value):
        """ GetAttributeShort(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, Int16) """
        pass

    def GetAttributeString(self, channelName, attributeIdentifier, value):
        """ GetAttributeString(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, str) """
        pass

    def GetAttributeUInt(self, channelName, attributeIdentifier, value):
        """ GetAttributeUInt(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, UInt32) """
        pass

    def GetAttributeUIntArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeUIntArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[UInt32]) -> (int, Array[UInt32]) """
        pass

    def GetAttributeULongArray(self, channelName, attributeIdentifier, value):
        """ GetAttributeULongArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[UInt64]) -> (int, Array[UInt64]) """
        pass

    def GetAttributeUShort(self, channelName, attributeIdentifier, value):
        """ GetAttributeUShort(self: RFmxInstrMX, channelName: str, attributeIdentifier: int) -> (int, UInt16) """
        pass

    def GetAutomaticSGSASharedLO(self, channelName, value):
        """ GetAutomaticSGSASharedLO(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXAutomaticSGSASharedLO) """
        pass

    def GetAvailablePorts(self, *__args):
        """
        GetAvailablePorts(self: RFmxInstrMX) -> (int, Array[str])

        GetAvailablePorts(self: RFmxInstrMX, selectorString: str, availablePorts: Array[str]) -> (int, Array[str])
        """
        pass

    def GetCalibrationPlaneEnabled(self, selectorString, calibrationPlaneEnabled):
        """ GetCalibrationPlaneEnabled(self: RFmxInstrMX, selectorString: str) -> (int, RFmxInstrMXCalibrationPlaneEnabled) """
        pass

    def GetCalibrationPlaneNames(self, selectorString, calibrationPlaneNames):
        """ GetCalibrationPlaneNames(self: RFmxInstrMX, selectorString: str, calibrationPlaneNames: Array[str]) -> (int, Array[str]) """
        pass

    def GetChannelCoupling(self, channelName, value):
        """ GetChannelCoupling(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXChannelCoupling) """
        pass

    def GetCleanerSpectrum(self, channelName, value):
        """ GetCleanerSpectrum(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXCleanerSpectrum) """
        pass

    def GetCommonModeLevel(self, channelName, value):
        """ GetCommonModeLevel(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetDebugForNamedResultsEnabled(self, debugForNamedResultsEnabled):
        """ GetDebugForNamedResultsEnabled(self: RFmxInstrMX) -> (int, bool) """
        pass

    def GetDeviceTemperature(self, channelName, value):
        """ GetDeviceTemperature(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetDigitizerDitherEnabled(self, channelName, value):
        """ GetDigitizerDitherEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXDigitizerDitherEnabled) """
        pass

    def GetDigitizerTemperature(self, channelName, value):
        """ GetDigitizerTemperature(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetDownconverterCenterFrequency(self, channelName, value):
        """ GetDownconverterCenterFrequency(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetDownconverterFrequencyOffset(self, channelName, value):
        """ GetDownconverterFrequencyOffset(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetDownconverterGain(self, channelName, value):
        """ GetDownconverterGain(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetDownconverterPreselectorEnabled(self, channelName, value):
        """ GetDownconverterPreselectorEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXDownconverterPreselectorEnabled) """
        pass

    def GetError(self, errorCode, errorDescription):
        """ GetError(self: RFmxInstrMX) -> (int, int, str) """
        pass

    def GetErrorInfoFromSnapshot(self, personality, selectorString, errorCode, errorDescription):
        """ GetErrorInfoFromSnapshot(self: RFmxInstrMX, personality: RFmxInstrMXPersonalities, selectorString: str) -> (int, int, str) """
        pass

    def GetErrorString(self, errorCode, errorDescription):
        """ GetErrorString(self: RFmxInstrMX, errorCode: int) -> (int, str) """
        pass

    def GetExternalAttenuationTableNames(self, selectorString, externalAttenuationTableNames):
        """ GetExternalAttenuationTableNames(self: RFmxInstrMX, selectorString: str, externalAttenuationTableNames: Array[str]) -> (int, Array[str]) """
        pass

    def GetExternalAttenuationTableType(self, selectorString, tableName, calibrationTableType):
        """ GetExternalAttenuationTableType(self: RFmxInstrMX, selectorString: str, tableName: str) -> (int, RFmxInstrMXCalibrationTableType) """
        pass

    def GetFftWidth(self, channelName, value):
        """ GetFftWidth(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetForceAllTracesEnabled(self, channelName, allTracesEnabled):
        """ GetForceAllTracesEnabled(self: RFmxInstrMX, channelName: str) -> (int, bool) """
        pass

    def GetFrequencyReferenceExportedTerminal(self, channelName, value):
        """ GetFrequencyReferenceExportedTerminal(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetFrequencyReferenceFrequency(self, channelName, value):
        """ GetFrequencyReferenceFrequency(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetFrequencyReferenceSource(self, channelName, value):
        """ GetFrequencyReferenceSource(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetFrequencySettling(self, channelName, value):
        """ GetFrequencySettling(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetFrequencySettlingUnits(self, channelName, value):
        """ GetFrequencySettlingUnits(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXFrequencySettlingUnits) """
        pass

    def GetIFFilterBandwidth(self, channelName, value):
        """ GetIFFilterBandwidth(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetIFOutputPowerLevelOffset(self, channelName, value):
        """ GetIFOutputPowerLevelOffset(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetInitiaitedSnapshotStrings(self, personalityIDArray, signalNames, resultNames, snapshotIdentifiers, signalTimestampArray):
        """ GetInitiaitedSnapshotStrings(self: RFmxInstrMX, personalityIDArray: Array[int], signalTimestampArray: Array[UInt64]) -> (int, Array[int], str, str, str, Array[UInt64]) """
        pass

    def GetInputIsolationEnabled(self, channelName, value):
        """ GetInputIsolationEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXInputIsolationEnabled) """
        pass

    def GetInstrumentFirmwareRevision(self, channelName, value):
        """ GetInstrumentFirmwareRevision(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetInstrumentHandle(self):
        """ GetInstrumentHandle(self: RFmxInstrMX) -> SafeHandle """
        pass

    def GetInstrumentModel(self, channelName, value):
        """ GetInstrumentModel(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetIQFrequencyOffset(self, channelName, value):
        """ GetIQFrequencyOffset(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetLatestConfigurationSnapshot(self, personalityID, signalNames, snapshotIdentifier, signalConfigurationState, signalTimestamp):
        """ GetLatestConfigurationSnapshot(self: RFmxInstrMX) -> (int, int, str, str, int, UInt64) """
        pass

    def GetLO2ExportEnabled(self, channelName, value):
        """ GetLO2ExportEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXLO2ExportEnabled) """
        pass

    def GetLOExportEnabled(self, channelName, value):
        """ GetLOExportEnabled(self: RFmxInstrMX, channelName: str) -> (int, bool) """
        pass

    def GetLOFrequency(self, channelName, value):
        """ GetLOFrequency(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetLOFrequencyStepSize(self, selectorString, value):
        """ GetLOFrequencyStepSize(self: RFmxInstrMX, selectorString: str) -> (int, float) """
        pass

    def GetLOInjectionSide(self, channelName, value):
        """ GetLOInjectionSide(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXLOInjectionSide) """
        pass

    def GetLOInPower(self, channelName, value):
        """ GetLOInPower(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetLOLeakageAvoidanceEnabled(self, channelName, value):
        """ GetLOLeakageAvoidanceEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXLOLeakageAvoidanceEnabled) """
        pass

    def GetLOOutPower(self, channelName, value):
        """ GetLOOutPower(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetLOPllFractionalMode(self, channelName, value):
        """ GetLOPllFractionalMode(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXLOPllFractionalMode) """
        pass

    def GetLOSource(self, channelName, value):
        """ GetLOSource(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetLOTemperature(self, channelName, value):
        """ GetLOTemperature(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetLOVcoFrequencyStepSize(self, selectorString, value):
        """ GetLOVcoFrequencyStepSize(self: RFmxInstrMX, selectorString: str) -> (int, float) """
        pass

    def GetMechanicalAttenuationAuto(self, channelName, value):
        """ GetMechanicalAttenuationAuto(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXMechanicalAttenuationAuto) """
        pass

    def GetMechanicalAttenuationValue(self, channelName, value):
        """ GetMechanicalAttenuationValue(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetMixerLevel(self, channelName, value):
        """ GetMixerLevel(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetMixerLevelOffset(self, channelName, value):
        """ GetMixerLevelOffset(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetModuleRevision(self, channelName, value):
        """ GetModuleRevision(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    @staticmethod
    def GetOpenSessionsInformation(resourceName, infoJson):
        """ GetOpenSessionsInformation(resourceName: str) -> (int, str) """
        pass

    def GetOptimizePathForSignalBandwidth(self, channelName, value):
        """ GetOptimizePathForSignalBandwidth(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXOptimizePathForSignalBandwidth) """
        pass

    def GetOspDelayEnabled(self, channelName, value):
        """ GetOspDelayEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXOspDelayEnabled) """
        pass

    def GetOverflowErrorReporting(self, channelName, value):
        """ GetOverflowErrorReporting(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXOverflowErrorReporting) """
        pass

    def GetPhaseOffset(self, channelName, value):
        """ GetPhaseOffset(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetPreampEnabled(self, channelName, value):
        """ GetPreampEnabled(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXPreampEnabled) """
        pass

    def GetPreselectorPresent(self, channelName, value):
        """ GetPreselectorPresent(self: RFmxInstrMX, channelName: str) -> (int, bool) """
        pass

    def GetPrivilegeLevel(self, isConnectionAlive, privilegeLevel):
        """ GetPrivilegeLevel(self: RFmxInstrMX) -> (int, bool, RFmxInstrMXClientPrivilegeLevel) """
        pass

    def GetRecommendedAcquisitionType(self, channelName, value):
        """ GetRecommendedAcquisitionType(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXRecommendedAcquisitionType) """
        pass

    def GetRecommendedCenterFrequency(self, channelName, value):
        """ GetRecommendedCenterFrequency(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedIQAcquisitionTime(self, channelName, value):
        """ GetRecommendedIQAcquisitionTime(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedIQMeasurementBandwidth(self, channelName, value):
        """ GetRecommendedIQMeasurementBandwidth(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedIQMinimumSampleRate(self, channelName, value):
        """ GetRecommendedIQMinimumSampleRate(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedIQPreTriggerTime(self, channelName, value):
        """ GetRecommendedIQPreTriggerTime(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedNumberOfRecords(self, channelName, value):
        """ GetRecommendedNumberOfRecords(self: RFmxInstrMX, channelName: str) -> (int, int) """
        pass

    def GetRecommendedSpectralAcquisitionSpan(self, channelName, value):
        """ GetRecommendedSpectralAcquisitionSpan(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedSpectralFftWindow(self, channelName, value):
        """ GetRecommendedSpectralFftWindow(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXRecommendedSpectralFftWindow) """
        pass

    def GetRecommendedSpectralResolutionBandwidth(self, channelName, value):
        """ GetRecommendedSpectralResolutionBandwidth(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRecommendedTriggerMinimumQuietTime(self, channelName, value):
        """ GetRecommendedTriggerMinimumQuietTime(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRFAttenuationAuto(self, channelName, value):
        """ GetRFAttenuationAuto(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXRFAttenuationAuto) """
        pass

    def GetRFAttenuationStepSize(self, channelName, value):
        """ GetRFAttenuationStepSize(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRFAttenuationValue(self, channelName, value):
        """ GetRFAttenuationValue(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetRFHighpassFilterFrequency(self, selectorString, value):
        """ GetRFHighpassFilterFrequency(self: RFmxInstrMX, selectorString: str) -> (int, float) """
        pass

    def GetRFmxVersion(self, RFmxVersion):
        """ GetRFmxVersion(self: RFmxInstrMX) -> (int, str) """
        pass

    def GetRFPreampPresent(self, channelName, value):
        """ GetRFPreampPresent(self: RFmxInstrMX, channelName: str) -> (int, bool) """
        pass

    def GetSelfCalibrateLastDateAndTime(self, selectorString, selfCalibrateStep, timestamp):
        """ GetSelfCalibrateLastDateAndTime(self: RFmxInstrMX, selectorString: str, selfCalibrateStep: RFmxInstrMXSelfCalibrateSteps) -> (int, DateTime) """
        pass

    def GetSelfCalibrateLastTemperature(self, selectorString, selfCalibrateStep, temperature):
        """ GetSelfCalibrateLastTemperature(self: RFmxInstrMX, selectorString: str, selfCalibrateStep: RFmxInstrMXSelfCalibrateSteps) -> (int, float) """
        pass

    def GetSerialNumber(self, channelName, value):
        """ GetSerialNumber(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    @staticmethod
    def GetSession(resourceName, optionString, isNewSession=None):
        """
        GetSession(resourceName: str, optionString: str) -> RFmxInstrMX

        GetSession(resourceName: str, optionString: str) -> (RFmxInstrMX, bool)
        """
        pass

    @staticmethod
    def GetSessionFromNIRfsaHandle(niRfsaHandle):
        """ GetSessionFromNIRfsaHandle(niRfsaHandle: IntPtr) -> RFmxInstrMX """
        pass

    def GetSignalConfigurationNames(self, selectorString, personalityFilter, signalNames, personality):
        """ GetSignalConfigurationNames(self: RFmxInstrMX, selectorString: str, personalityFilter: RFmxInstrMXPersonalities, signalNames: Array[str], personality: Array[RFmxInstrMXPersonalities]) -> (int, Array[str], Array[RFmxInstrMXPersonalities]) """
        pass

    def GetSignalConfigurationState(self, signalName, personality, signalState, timeStamp):
        """
        GetSignalConfigurationState(self: RFmxInstrMX, signalName: str, personality: RFmxInstrMXPersonalities) -> (int, RFmxInstrMXSignalConfigurationState, UInt64)

        GetSignalConfigurationState(self: RFmxInstrMX, signalName: str, personality: RFmxInstrMXPersonalities) -> (int, RFmxInstrMXSignalConfigurationState, UInt32)
        """
        pass

    def GetSmuChannel(self, channelName, value):
        """ GetSmuChannel(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetSmuResourceName(self, channelName, value):
        """ GetSmuResourceName(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetSnapshotState(self, personality, selectorString, snapshotState):
        """ GetSnapshotState(self: RFmxInstrMX, personality: RFmxInstrMXPersonalities, selectorString: str) -> (int, RFmxInstrMXSignalConfigurationState) """
        pass

    def GetSParameterExternalAttenuationType(self, selectorString, sParameterType):
        """ GetSParameterExternalAttenuationType(self: RFmxInstrMX, selectorString: str) -> (int, RFmxInstrMXSParameterType) """
        pass

    def GetSubSpanOverlap(self, channelName, value):
        """ GetSubSpanOverlap(self: RFmxInstrMX, channelName: str) -> (int, float) """
        pass

    def GetThermalCorrectionHeadroomRange(self, selectorString, value):
        """ GetThermalCorrectionHeadroomRange(self: RFmxInstrMX, selectorString: str) -> (int, float) """
        pass

    def GetTracesInfoForMonitorSnapshot(self, selectorString, allTracesEnabled):
        """ GetTracesInfoForMonitorSnapshot(self: RFmxInstrMX, selectorString: str) -> (int, bool) """
        pass

    def GetTriggerExportOutputTerminal(self, channelName, value):
        """ GetTriggerExportOutputTerminal(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetTriggerTerminalName(self, channelName, value):
        """ GetTriggerTerminalName(self: RFmxInstrMX, channelName: str) -> (int, str) """
        pass

    def GetTuningSpeed(self, channelName, value):
        """ GetTuningSpeed(self: RFmxInstrMX, channelName: str) -> (int, RFmxInstrMXTuningSpeed) """
        pass

    def GetWarning(self, warningCode, warningDescription):
        """ GetWarning(self: RFmxInstrMX) -> (int, int, str) """
        pass

    def IsSelfCalibrateValid(self, selectorString, selfCalibrateValid, validSteps):
        """ IsSelfCalibrateValid(self: RFmxInstrMX, selectorString: str) -> (int, bool, RFmxInstrMXSelfCalibrateSteps) """
        pass

    def LoadAllConfigurations(self, filePath, loadRFInstrConfiguration):
        """ LoadAllConfigurations(self: RFmxInstrMX, filePath: str, loadRFInstrConfiguration: bool) -> int """
        pass

    def LoadAllForRevert(self, filePath):
        """ LoadAllForRevert(self: RFmxInstrMX, filePath: str) -> int """
        pass

    def LoadSParameterExternalAttenuationTableFromS2pFile(self, selectorString, tableName, s2pFilePath, sParameterOrientation):
        """ LoadSParameterExternalAttenuationTableFromS2pFile(self: RFmxInstrMX, selectorString: str, tableName: str, s2pFilePath: str, sParameterOrientation: RFmxInstrMXSParameterOrientation) -> int """
        pass

    def PingServer(self, isConnectionAlive):
        """ PingServer(self: RFmxInstrMX) -> (int, bool) """
        pass

    def RegisterExternalRFSubsystemCallbacks(self, externalRFSubsystemContext, callbacks, callbackVersion):
        """ RegisterExternalRFSubsystemCallbacks(self: RFmxInstrMX, externalRFSubsystemContext: IntPtr, callbacks: Array[IntPtr], callbackVersion: int) -> int """
        pass

    def RequestPrivilege(self, privilegeLevel):
        """ RequestPrivilege(self: RFmxInstrMX, privilegeLevel: RFmxInstrMXClientPrivilegeLevel) -> int """
        pass

    def ResetAttribute(self, channelName, attributeId):
        """ ResetAttribute(self: RFmxInstrMX, channelName: str, attributeId: RFmxInstrMXPropertyId) -> int """
        pass

    def ResetDriver(self):
        """ ResetDriver(self: RFmxInstrMX) -> int """
        pass

    def ResetEntireSession(self):
        """ ResetEntireSession(self: RFmxInstrMX) -> int """
        pass

    def ResetToDefault(self):
        """ ResetToDefault(self: RFmxInstrMX) -> int """
        pass

    def SaveAllConfigurations(self, filePath):
        """ SaveAllConfigurations(self: RFmxInstrMX, filePath: str) -> int """
        pass

    def SaveAllForRevert(self, filePath):
        """ SaveAllForRevert(self: RFmxInstrMX, filePath: str) -> int """
        pass

    def SelectActiveExternalAttenuationTable(self, selectorString, tableName):
        """ SelectActiveExternalAttenuationTable(self: RFmxInstrMX, selectorString: str, tableName: str) -> int """
        pass

    def SelfCalibrate(self, selectorString, stepsToOmit):
        """ SelfCalibrate(self: RFmxInstrMX, selectorString: str, stepsToOmit: RFmxInstrMXSelfCalibrateSteps) -> int """
        pass

    def SelfCalibrateRange(self, selectorString, stepsToOmit, minimumFrequency, maximumFrequency, minimumReferenceLevel, maximumReferenceLevel):
        """ SelfCalibrateRange(self: RFmxInstrMX, selectorString: str, stepsToOmit: RFmxInstrMXSelfCalibrateSteps, minimumFrequency: float, maximumFrequency: float, minimumReferenceLevel: float, maximumReferenceLevel: float) -> int """
        pass

    def SetAmplitudeSettling(self, channelName, value):
        """ SetAmplitudeSettling(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetAttributeBool(self, channelName, attributeIdentifier, value):
        """ SetAttributeBool(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: bool) -> int """
        pass

    def SetAttributeByte(self, channelName, attributeIdentifier, value):
        """ SetAttributeByte(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Byte) -> int """
        pass

    def SetAttributeByteArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeByteArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Byte]) -> int """
        pass

    def SetAttributeComplexDoubleArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeComplexDoubleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[ComplexDouble]) -> int """
        pass

    def SetAttributeComplexSingleArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeComplexSingleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[ComplexSingle]) -> int """
        pass

    def SetAttributeDouble(self, channelName, attributeIdentifier, value):
        """ SetAttributeDouble(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: float) -> int """
        pass

    def SetAttributeDoubleArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeDoubleArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[float]) -> int """
        pass

    def SetAttributeFloat(self, channelName, attributeIdentifier, value):
        """ SetAttributeFloat(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Single) -> int """
        pass

    def SetAttributeFloatArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeFloatArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Single]) -> int """
        pass

    def SetAttributeInt(self, channelName, attributeIdentifier, value):
        """ SetAttributeInt(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: int) -> int """
        pass

    def SetAttributeIntArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeIntArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[int]) -> int """
        pass

    def SetAttributeLong(self, channelName, attributeIdentifier, value):
        """ SetAttributeLong(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Int64) -> int """
        pass

    def SetAttributeLongArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeLongArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[Int64]) -> int """
        pass

    def SetAttributeSByte(self, channelName, attributeIdentifier, value):
        """ SetAttributeSByte(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: SByte) -> int """
        pass

    def SetAttributeSByteArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeSByteArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[SByte]) -> int """
        pass

    def SetAttributeShort(self, channelName, attributeIdentifier, value):
        """ SetAttributeShort(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Int16) -> int """
        pass

    def SetAttributeString(self, channelName, attributeIdentifier, value):
        """ SetAttributeString(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: str) -> int """
        pass

    def SetAttributeUInt(self, channelName, attributeIdentifier, value):
        """ SetAttributeUInt(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: UInt32) -> int """
        pass

    def SetAttributeUIntArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeUIntArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[UInt32]) -> int """
        pass

    def SetAttributeULongArray(self, channelName, attributeIdentifier, value):
        """ SetAttributeULongArray(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: Array[UInt64]) -> int """
        pass

    def SetAttributeUShort(self, channelName, attributeIdentifier, value):
        """ SetAttributeUShort(self: RFmxInstrMX, channelName: str, attributeIdentifier: int, value: UInt16) -> int """
        pass

    def SetAutomaticSGSASharedLO(self, channelName, value):
        """ SetAutomaticSGSASharedLO(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXAutomaticSGSASharedLO) -> int """
        pass

    def SetChannelCoupling(self, channelName, value):
        """ SetChannelCoupling(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXChannelCoupling) -> int """
        pass

    def SetCleanerSpectrum(self, channelName, value):
        """ SetCleanerSpectrum(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXCleanerSpectrum) -> int """
        pass

    def SetCommonModeLevel(self, channelName, value):
        """ SetCommonModeLevel(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetDigitizerDitherEnabled(self, channelName, value):
        """ SetDigitizerDitherEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXDigitizerDitherEnabled) -> int """
        pass

    def SetDownconverterCenterFrequency(self, channelName, value):
        """ SetDownconverterCenterFrequency(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetDownconverterFrequencyOffset(self, channelName, value):
        """ SetDownconverterFrequencyOffset(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetDownconverterPreselectorEnabled(self, channelName, value):
        """ SetDownconverterPreselectorEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXDownconverterPreselectorEnabled) -> int """
        pass

    def SetFftWidth(self, channelName, value):
        """ SetFftWidth(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetForceAllTracesEnabled(self, channelName, allTracesEnabled):
        """ SetForceAllTracesEnabled(self: RFmxInstrMX, channelName: str, allTracesEnabled: bool) -> int """
        pass

    def SetFrequencyReferenceExportedTerminal(self, channelName, value):
        """ SetFrequencyReferenceExportedTerminal(self: RFmxInstrMX, channelName: str, value: str) -> int """
        pass

    def SetFrequencyReferenceFrequency(self, channelName, value):
        """ SetFrequencyReferenceFrequency(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetFrequencyReferenceSource(self, channelName, value):
        """ SetFrequencyReferenceSource(self: RFmxInstrMX, channelName: str, value: str) -> int """
        pass

    def SetFrequencySettling(self, channelName, value):
        """ SetFrequencySettling(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetFrequencySettlingUnits(self, channelName, value):
        """ SetFrequencySettlingUnits(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXFrequencySettlingUnits) -> int """
        pass

    def SetIFFilterBandwidth(self, channelName, value):
        """ SetIFFilterBandwidth(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetIFOutputPowerLevelOffset(self, channelName, value):
        """ SetIFOutputPowerLevelOffset(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetInputIsolationEnabled(self, channelName, value):
        """ SetInputIsolationEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXInputIsolationEnabled) -> int """
        pass

    def SetIOTraceStatus(self, IOTraceStatus):
        """ SetIOTraceStatus(self: RFmxInstrMX, IOTraceStatus: bool) -> int """
        pass

    def SetIQFrequencyOffset(self, channelName, value):
        """ SetIQFrequencyOffset(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetLO2ExportEnabled(self, channelName, value):
        """ SetLO2ExportEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXLO2ExportEnabled) -> int """
        pass

    def SetLOExportEnabled(self, channelName, value):
        """ SetLOExportEnabled(self: RFmxInstrMX, channelName: str, value: bool) -> int """
        pass

    def SetLOFrequency(self, channelName, value):
        """ SetLOFrequency(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetLOFrequencyStepSize(self, selectorString, value):
        """ SetLOFrequencyStepSize(self: RFmxInstrMX, selectorString: str, value: float) -> int """
        pass

    def SetLOInjectionSide(self, channelName, value):
        """ SetLOInjectionSide(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXLOInjectionSide) -> int """
        pass

    def SetLOInPower(self, channelName, value):
        """ SetLOInPower(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetLOLeakageAvoidanceEnabled(self, channelName, value):
        """ SetLOLeakageAvoidanceEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXLOLeakageAvoidanceEnabled) -> int """
        pass

    def SetLOOutPower(self, channelName, value):
        """ SetLOOutPower(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetLOPllFractionalMode(self, channelName, value):
        """ SetLOPllFractionalMode(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXLOPllFractionalMode) -> int """
        pass

    def SetLOSource(self, channelName, value):
        """ SetLOSource(self: RFmxInstrMX, channelName: str, value: str) -> int """
        pass

    def SetLOVcoFrequencyStepSize(self, selectorString, value):
        """ SetLOVcoFrequencyStepSize(self: RFmxInstrMX, selectorString: str, value: float) -> int """
        pass

    def SetMechanicalAttenuationAuto(self, channelName, value):
        """ SetMechanicalAttenuationAuto(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXMechanicalAttenuationAuto) -> int """
        pass

    def SetMechanicalAttenuationValue(self, channelName, value):
        """ SetMechanicalAttenuationValue(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetMixerLevel(self, channelName, value):
        """ SetMixerLevel(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetMixerLevelOffset(self, channelName, value):
        """ SetMixerLevelOffset(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetOptimizePathForSignalBandwidth(self, channelName, value):
        """ SetOptimizePathForSignalBandwidth(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXOptimizePathForSignalBandwidth) -> int """
        pass

    def SetOspDelayEnabled(self, channelName, value):
        """ SetOspDelayEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXOspDelayEnabled) -> int """
        pass

    def SetOverflowErrorReporting(self, channelName, value):
        """ SetOverflowErrorReporting(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXOverflowErrorReporting) -> int """
        pass

    def SetPhaseOffset(self, channelName, value):
        """ SetPhaseOffset(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetPreampEnabled(self, channelName, value):
        """ SetPreampEnabled(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXPreampEnabled) -> int """
        pass

    def SetRFAttenuationAuto(self, channelName, value):
        """ SetRFAttenuationAuto(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXRFAttenuationAuto) -> int """
        pass

    def SetRFAttenuationStepSize(self, channelName, value):
        """ SetRFAttenuationStepSize(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetRFAttenuationValue(self, channelName, value):
        """ SetRFAttenuationValue(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetRFHighpassFilterFrequency(self, selectorString, value):
        """ SetRFHighpassFilterFrequency(self: RFmxInstrMX, selectorString: str, value: float) -> int """
        pass

    def SetSmuChannel(self, channelName, value):
        """ SetSmuChannel(self: RFmxInstrMX, channelName: str, value: str) -> int """
        pass

    def SetSmuResourceName(self, channelName, value):
        """ SetSmuResourceName(self: RFmxInstrMX, channelName: str, value: str) -> int """
        pass

    def SetSubSpanOverlap(self, channelName, value):
        """ SetSubSpanOverlap(self: RFmxInstrMX, channelName: str, value: float) -> int """
        pass

    def SetThermalCorrectionHeadroomRange(self, selectorString, value):
        """ SetThermalCorrectionHeadroomRange(self: RFmxInstrMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerExportOutputTerminal(self, channelName, value):
        """ SetTriggerExportOutputTerminal(self: RFmxInstrMX, channelName: str, value: str) -> int """
        pass

    def SetTuningSpeed(self, channelName, value):
        """ SetTuningSpeed(self: RFmxInstrMX, channelName: str, value: RFmxInstrMXTuningSpeed) -> int """
        pass

    def StopMonitoringAndClearAllSnapshots(self):
        """ StopMonitoringAndClearAllSnapshots(self: RFmxInstrMX) -> int """
        pass

    def UnRegisterExternalRFSubsystemCallbacks(self):
        """ UnRegisterExternalRFSubsystemCallbacks(self: RFmxInstrMX) -> int """
        pass

    def WaitForAcquisitionComplete(self, timeout):
        """ WaitForAcquisitionComplete(self: RFmxInstrMX, timeout: float) -> int """
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

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, instrumentHandle: IntPtr)

        __new__(cls: type, resourceName: str, optionString: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: RFmxInstrMX) -> bool"""

    NumberOfSignalConfigurations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSignalConfigurations(self: RFmxInstrMX) -> int"""


class RFmxNRMXExtension(object):
    # no doc
    @staticmethod
    def GetNRSignalConfiguration(instrSession, signalName=None):
        """
        GetNRSignalConfiguration(instrSession: RFmxInstrMX) -> RFmxNRMX

        GetNRSignalConfiguration(instrSession: RFmxInstrMX, signalName: str) -> RFmxNRMX
        """
        from .NRMX import RFmxNRMX
        return RFmxNRMX()

    __all__ = [
        'GetNRSignalConfiguration',
    ]


class RFmxLteMXExtension(object):
    # no doc
    @staticmethod
    def GetLteSignalConfiguration(instrSession, signalName=None):
        """
        GetLteSignalConfiguration(instrSession: RFmxInstrMX) -> RFmxLteMX

        GetLteSignalConfiguration(instrSession: RFmxInstrMX, signalName: str) -> RFmxLteMX
        """
        from .LteMX import RFmxLteMX
        return RFmxLteMX()

    __all__ = [
        'GetLteSignalConfiguration',
    ]


class RFmxInstrMXAttributeAuthor(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXAttributeAuthor, values: System (2), Unwritten (0), User (1) """
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

    System = None
    Unwritten = None
    User = None
    value__ = None


class RFmxInstrMXAutomaticSGSASharedLO(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXAutomaticSGSASharedLO, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXCalibrationPlaneEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXCalibrationPlaneEnabled, values: False (0), True (1) """
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


class RFmxInstrMXCalibrationTableType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXCalibrationTableType, values: ExternalAttenuation (0), SParameter (1) """
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

    ExternalAttenuation = None
    SParameter = None
    value__ = None


class RFmxInstrMXChannelCoupling(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXChannelCoupling, values: ACCoupled (0), DCCoupled (1) """
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

    ACCoupled = None
    DCCoupled = None
    value__ = None


class RFmxInstrMXCleanerSpectrum(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXCleanerSpectrum, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXClientPrivilegeLevel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXClientPrivilegeLevel, values: Monitor (1), None (0), RevokableControl (2), UnrevokableControl (3) """
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

    Monitor = None
    None = None
    RevokableControl = None
    UnrevokableControl = None
    value__ = None


class RFmxInstrMXConstants(object):
    # no doc
    ClockIn = 'ClkIn'
    ClockOut = 'ClkOut'
    DoNotExportSignal = ''
    LOSourceLOIn = 'LO_In'
    LOSourceNone = 'None'
    LOSourceOnboard = 'Onboard'
    LOSourceSecondary = 'Secondary'
    LOSourceSGSAShared = 'SG_SA_Shared'
    None = ''
    OnboardClock = 'OnboardClock'
    Pfi0 = 'PFI0'
    Pfi1 = 'PFI1'
    PxiClock = 'PXI_Clk'
    PxiClockMaster = 'PXI_ClkMaster'
    PxiStarLine = 'PXI_STAR'
    PxiTriggerLine0 = 'PXI_Trig0'
    PxiTriggerLine1 = 'PXI_Trig1'
    PxiTriggerLine2 = 'PXI_Trig2'
    PxiTriggerLine3 = 'PXI_Trig3'
    PxiTriggerLine4 = 'PXI_Trig4'
    PxiTriggerLine5 = 'PXI_Trig5'
    PxiTriggerLine6 = 'PXI_Trig6'
    PxiTriggerLine7 = 'PXI_Trig7'
    ReferenceIn = 'RefIn'
    ReferenceIn2 = 'RefIn2'
    ReferenceOut = 'RefOut'
    ReferenceOut2 = 'RefOut2'
    __all__ = [
        'ClockIn',
        'ClockOut',
        'DoNotExportSignal',
        'LOSourceLOIn',
        'LOSourceNone',
        'LOSourceOnboard',
        'LOSourceSecondary',
        'LOSourceSGSAShared',
        'None',
        'OnboardClock',
        'Pfi0',
        'Pfi1',
        'PxiClock',
        'PxiClockMaster',
        'PxiStarLine',
        'PxiTriggerLine0',
        'PxiTriggerLine1',
        'PxiTriggerLine2',
        'PxiTriggerLine3',
        'PxiTriggerLine4',
        'PxiTriggerLine5',
        'PxiTriggerLine6',
        'PxiTriggerLine7',
        'ReferenceIn',
        'ReferenceIn2',
        'ReferenceOut',
        'ReferenceOut2',
    ]


class RFmxInstrMXDigitizerDitherEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXDigitizerDitherEnabled, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXDownconverterPreselectorEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXDownconverterPreselectorEnabled, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXExportSignalSource(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXExportSignalSource, values: ReferenceClock (8), ReferenceTrigger (1) """
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

    ReferenceClock = None
    ReferenceTrigger = None
    value__ = None


class RFmxInstrMXFrequencySettlingUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXFrequencySettlingUnits, values: Ppm (0), SecondsAfterIO (2), SecondsAfterLock (1) """
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

    Ppm = None
    SecondsAfterIO = None
    SecondsAfterLock = None
    value__ = None


class RFmxInstrMXInputIsolationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXInputIsolationEnabled, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXLinearInterpolationFormat(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXLinearInterpolationFormat, values: Magnitude_dB_AndPhase (2), MagnitudeAndPhase (1), RealAndImaginary (0) """
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
    Magnitude_dB_AndPhase = None
    RealAndImaginary = None
    value__ = None


class RFmxInstrMXLO2ExportEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXLO2ExportEnabled, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXLOInjectionSide(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXLOInjectionSide, values: HighSide (0), LowSide (1) """
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

    HighSide = None
    LowSide = None
    value__ = None


class RFmxInstrMXLOLeakageAvoidanceEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXLOLeakageAvoidanceEnabled, values: False (0), True (1) """
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


class RFmxInstrMXLOPllFractionalMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXLOPllFractionalMode, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXMechanicalAttenuationAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXMechanicalAttenuationAuto, values: False (0), True (1) """
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


class RFmxInstrMXOptimizePathForSignalBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXOptimizePathForSignalBandwidth, values: Automatic (2), Disabled (0), Enabled (1) """
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

    Automatic = None
    Disabled = None
    Enabled = None
    value__ = None


class RFmxInstrMXOspDelayEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXOspDelayEnabled, values: Disabled (0), Enabled (1) """
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


class RFmxInstrMXOverflowErrorReporting(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXOverflowErrorReporting, values: Disabled (1), Warning (0) """
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
    value__ = None
    Warning = None


class RFmxInstrMXPersonalities(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RFmxInstrMXPersonalities, values: All (2147483647), BT (1024), Cdma2k (32), Demod (2), Evdo (128), Gsm (8), Lte (4), None (0), NR (256), SpecAn (1), Tdscdma (64), Wcdma (16), Wlan (512) """
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

    All = None
    BT = None
    Cdma2k = None
    Demod = None
    Evdo = None
    Gsm = None
    Lte = None
    None = None
    NR = None
    SpecAn = None
    Tdscdma = None
    value__ = None
    Wcdma = None
    Wlan = None


class RFmxInstrMXPowerUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXPowerUnits, values: dBm (0), dBmV (4), dBuV (5), dBV (3), dBW (2), Volts (7), VoltsSquared (8), Vpp (10), W (6) """
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
    dBmV = None
    dBuV = None
    dBV = None
    dBW = None
    value__ = None
    Volts = None
    VoltsSquared = None
    Vpp = None
    W = None


class RFmxInstrMXPreampEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXPreampEnabled, values: Automatic (3), Disabled (0), Enabled (1) """
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

    Automatic = None
    Disabled = None
    Enabled = None
    value__ = None


class RFmxInstrMXPropertyId(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXPropertyId, values: AmplitudeSettling (56), AutomaticSGSASharedLO (74), ChannelCoupling (11), CleanerSpectrum (37), CommonModeLevel (70), DeviceTemperature (24), DigitizerDitherEnabled (21), DigitizerTemperature (25), DownconverterCenterFrequency (13), DownconverterFrequencyOffset (53), DownconverterGain (52), DownconverterPreselectorEnabled (12), FftWidth (22), FrequencyReferenceExportedTerminal (34), FrequencyReferenceFrequency (3), FrequencyReferenceSource (2), FrequencySettling (10), FrequencySettlingUnits (9), IFFilterBandwidth (48), IFOutputPowerLevelOffset (17), InputIsolationEnabled (92), InstrumentFirmwareRevision (27), InstrumentModel (28), IQFrequencyOffset (69), LO2ExportEnabled (58), LOExportEnabled (33), LOFrequency (60), LOFrequencyStepSize (95), LOInjectionSide (18), LOInPower (78), LOLeakageAvoidanceEnabled (55), LOOutPower (79), LOPllFractionalMode (90), LOSource (59), LOTemperature (26), LOVcoFrequencyStepSize (80), MechanicalAttenuationAuto (6), MechanicalAttenuationValue (7), MixerLevel (16), MixerLevelOffset (15), ModuleRevision (29), OptimizePathForSignalBandwidth (91), OspDelayEnabled (23), OverflowErrorReporting (77), PhaseOffset (19), PreampEnabled (14), PreselectorPresent (31), RecommendedAcquisitionType (39), RecommendedCenterFrequency (57), RecommendedIQAcquisitionTime (42), RecommendedIQMeasurementBandwidth (51), RecommendedIQMinimumSampleRate (43), RecommendedIQPreTriggerTime (44), RecommendedNumberOfRecords (40), RecommendedSpectralAcquisitionSpan (45), RecommendedSpectralFftWindow (46), RecommendedSpectralResolutionBandwidth (47), RecommendedTriggerMinimumQuietTime (41), RFAttenuationAuto (4), RFAttenuationStepSize (54), RFAttenuationValue (5), RFHighpassFilterFrequency (49), RFPreampPresent (32), SerialNumber (30), SmuChannel (72), SmuResourceName (71), SubSpanOverlap (50), ThermalCorrectionHeadroomRange (94), TriggerExportOutputTerminal (35), TriggerTerminalName (36), TuningSpeed (8) """
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

    AmplitudeSettling = None
    AutomaticSGSASharedLO = None
    ChannelCoupling = None
    CleanerSpectrum = None
    CommonModeLevel = None
    DeviceTemperature = None
    DigitizerDitherEnabled = None
    DigitizerTemperature = None
    DownconverterCenterFrequency = None
    DownconverterFrequencyOffset = None
    DownconverterGain = None
    DownconverterPreselectorEnabled = None
    FftWidth = None
    FrequencyReferenceExportedTerminal = None
    FrequencyReferenceFrequency = None
    FrequencyReferenceSource = None
    FrequencySettling = None
    FrequencySettlingUnits = None
    IFFilterBandwidth = None
    IFOutputPowerLevelOffset = None
    InputIsolationEnabled = None
    InstrumentFirmwareRevision = None
    InstrumentModel = None
    IQFrequencyOffset = None
    LO2ExportEnabled = None
    LOExportEnabled = None
    LOFrequency = None
    LOFrequencyStepSize = None
    LOInjectionSide = None
    LOInPower = None
    LOLeakageAvoidanceEnabled = None
    LOOutPower = None
    LOPllFractionalMode = None
    LOSource = None
    LOTemperature = None
    LOVcoFrequencyStepSize = None
    MechanicalAttenuationAuto = None
    MechanicalAttenuationValue = None
    MixerLevel = None
    MixerLevelOffset = None
    ModuleRevision = None
    OptimizePathForSignalBandwidth = None
    OspDelayEnabled = None
    OverflowErrorReporting = None
    PhaseOffset = None
    PreampEnabled = None
    PreselectorPresent = None
    RecommendedAcquisitionType = None
    RecommendedCenterFrequency = None
    RecommendedIQAcquisitionTime = None
    RecommendedIQMeasurementBandwidth = None
    RecommendedIQMinimumSampleRate = None
    RecommendedIQPreTriggerTime = None
    RecommendedNumberOfRecords = None
    RecommendedSpectralAcquisitionSpan = None
    RecommendedSpectralFftWindow = None
    RecommendedSpectralResolutionBandwidth = None
    RecommendedTriggerMinimumQuietTime = None
    RFAttenuationAuto = None
    RFAttenuationStepSize = None
    RFAttenuationValue = None
    RFHighpassFilterFrequency = None
    RFPreampPresent = None
    SerialNumber = None
    SmuChannel = None
    SmuResourceName = None
    SubSpanOverlap = None
    ThermalCorrectionHeadroomRange = None
    TriggerExportOutputTerminal = None
    TriggerTerminalName = None
    TuningSpeed = None
    value__ = None


class RFmxInstrMXRecommendedAcquisitionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXRecommendedAcquisitionType, values: IQ (0), IQOrSpectral (2), Spectral (1) """
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

    IQ = None
    IQOrSpectral = None
    Spectral = None
    value__ = None


class RFmxInstrMXRecommendedSpectralFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXRecommendedSpectralFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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


class RFmxInstrMXRFAttenuationAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXRFAttenuationAuto, values: False (0), True (1) """
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


class RFmxInstrMXSelfCalibrateSteps(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RFmxInstrMXSelfCalibrateSteps, values: AmplitudeAccuracy (32), DCOffset (512), DigitizerSelfcal (8), GainReference (2), IFFlatness (4), ImageSuppression (128), LOSelfCal (16), None (0), PreselectorAlignment (1), ResidualLOPower (64), SynthesizerAlignment (256) """
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

    AmplitudeAccuracy = None
    DCOffset = None
    DigitizerSelfcal = None
    GainReference = None
    IFFlatness = None
    ImageSuppression = None
    LOSelfCal = None
    None = None
    PreselectorAlignment = None
    ResidualLOPower = None
    SynthesizerAlignment = None
    value__ = None


class RFmxInstrMXSignalConfigurationState(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXSignalConfigurationState, values: CommitInProgress (3), CommittedError (5), CommittedNoError (4), InitiatedError (8), InitiatedNoError (7), InitiateInProgress (6), Invalid (-1), Uncommitted (2), Unconfigured (1), Unknown (-2), Valid (0), Verified (9) """
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

    CommitInProgress = None
    CommittedError = None
    CommittedNoError = None
    InitiatedError = None
    InitiatedNoError = None
    InitiateInProgress = None
    Invalid = None
    Uncommitted = None
    Unconfigured = None
    Unknown = None
    Valid = None
    value__ = None
    Verified = None


class RFmxInstrMXSParameterOrientation(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXSParameterOrientation, values: Port1TowardsDut (0), Port2TowardsDut (1) """
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

    Port1TowardsDut = None
    Port2TowardsDut = None
    value__ = None


class RFmxInstrMXSParameterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXSParameterType, values: Scalar (1), Vector (2) """
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

    Scalar = None
    value__ = None
    Vector = None


class RFmxInstrMXTerminalConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXTerminalConfiguration, values: Differential (0), SingleEnded (1) """
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

    Differential = None
    SingleEnded = None
    value__ = None


class RFmxInstrMXTuningSpeed(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxInstrMXTuningSpeed, values: Fast (2), Medium (1), Normal (0) """
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

    Fast = None
    Medium = None
    Normal = None
    value__ = None


