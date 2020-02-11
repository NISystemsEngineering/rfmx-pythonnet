# encoding: utf-8
# module NationalInstruments.RFmx.NRMX calls itself NRMX
# from NationalInstruments.RFmx.NRMX.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RFmxNRMX(object, ISignalConfiguration, IDisposable):
    # no doc
    def AbortMeasurements(self, selectorString):
        """ AbortMeasurements(self: RFmxNRMX, selectorString: str) -> int """
        pass

    def AnalyzeIQ(self, selectorString, resultName, iq, reset, averagingDone):
        """ AnalyzeIQ(self: RFmxNRMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool) -> (int, bool) """
        pass

    def AnalyzeIQ1Waveform(self, selectorString, resultName, iq, reset, reserved):
        """ AnalyzeIQ1Waveform(self: RFmxNRMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool, reserved: Int64) -> int """
        pass

    def AnalyzeSpectrum(self, selectorString, resultName, spectrum, reset, averagingDone):
        """ AnalyzeSpectrum(self: RFmxNRMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool) -> (int, bool) """
        pass

    def AnalyzeSpectrum1Waveform(self, selectorString, resultName, spectrum, reset, reserved):
        """ AnalyzeSpectrum1Waveform(self: RFmxNRMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool, reserved: Int64) -> int """
        pass

    def AutoLevel(self, selectorString, measurementInterval, referenceLevel):
        """ AutoLevel(self: RFmxNRMX, selectorString: str, measurementInterval: float) -> (int, float) """
        pass

    @staticmethod
    def BuildBandwidthPartString(selectorString, bandwidthPartNumber):
        """ BuildBandwidthPartString(selectorString: str, bandwidthPartNumber: int) -> str """
        pass

    @staticmethod
    def BuildCarrierString(selectorString, carrierNumber):
        """ BuildCarrierString(selectorString: str, carrierNumber: int) -> str """
        pass

    @staticmethod
    def BuildCoresetClusterString(selectorString, coresetClusterNumber):
        """ BuildCoresetClusterString(selectorString: str, coresetClusterNumber: int) -> str """
        pass

    @staticmethod
    def BuildCoresetString(selectorString, coresetNumber):
        """ BuildCoresetString(selectorString: str, coresetNumber: int) -> str """
        pass

    @staticmethod
    def BuildOffsetString(selectorString, offsetNumber):
        """ BuildOffsetString(selectorString: str, offsetNumber: int) -> str """
        pass

    @staticmethod
    def BuildPdcchString(selectorString, pdcchNumber):
        """ BuildPdcchString(selectorString: str, pdcchNumber: int) -> str """
        pass

    @staticmethod
    def BuildPdschClusterString(selectorString, pdschClusterNumber):
        """ BuildPdschClusterString(selectorString: str, pdschClusterNumber: int) -> str """
        pass

    @staticmethod
    def BuildPdschString(selectorString, pdschNumber):
        """ BuildPdschString(selectorString: str, pdschNumber: int) -> str """
        pass

    @staticmethod
    def BuildPuschClusterString(selectorString, puschClusterNumber):
        """ BuildPuschClusterString(selectorString: str, puschClusterNumber: int) -> str """
        pass

    @staticmethod
    def BuildPuschString(selectorString, puschNumber):
        """ BuildPuschString(selectorString: str, puschNumber: int) -> str """
        pass

    @staticmethod
    def BuildResultString(resultName):
        """ BuildResultString(resultName: str) -> str """
        pass

    @staticmethod
    def BuildSubblockString(selectorString, subblockNumber):
        """ BuildSubblockString(selectorString: str, subblockNumber: int) -> str """
        pass

    @staticmethod
    def BuildUserString(selectorString, userNumber):
        """ BuildUserString(selectorString: str, userNumber: int) -> str """
        pass

    def CheckMeasurementStatus(self, selectorString, isDone):
        """ CheckMeasurementStatus(self: RFmxNRMX, selectorString: str) -> (int, bool) """
        pass

    def ClearAllNamedResults(self, selectorString):
        """ ClearAllNamedResults(self: RFmxNRMX, selectorString: str) -> int """
        pass

    def ClearNamedResult(self, selectorString):
        """ ClearNamedResult(self: RFmxNRMX, selectorString: str) -> int """
        pass

    def CloneSignalConfiguration(self, newSignalName, signalConfiguration):
        """ CloneSignalConfiguration(self: RFmxNRMX, newSignalName: str) -> (int, RFmxNRMX) """
        pass

    def Commit(self, selectorString):
        """ Commit(self: RFmxNRMX, selectorString: str) -> int """
        pass

    def ConfigureDigitalEdgeTrigger(self, selectorString, digitalEdgeTriggerSource, digitalEdgeTriggerEdge, triggerDelay, enableTrigger):
        """ ConfigureDigitalEdgeTrigger(self: RFmxNRMX, selectorString: str, digitalEdgeTriggerSource: str, digitalEdgeTriggerEdge: RFmxNRMXDigitalEdgeTriggerEdge, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def ConfigureExternalAttenuation(self, selectorString, externalAttenuation):
        """ ConfigureExternalAttenuation(self: RFmxNRMX, selectorString: str, externalAttenuation: float) -> int """
        pass

    def ConfigureFrequency(self, selectorString, centerFrequency):
        """ ConfigureFrequency(self: RFmxNRMX, selectorString: str, centerFrequency: float) -> int """
        pass

    def ConfiguregNodeBCategory(self, selectorString, gNodeBCategory):
        """ ConfiguregNodeBCategory(self: RFmxNRMX, selectorString: str, gNodeBCategory: RFmxNRMXgNodeBCategory) -> int """
        pass

    def ConfigureIQPowerEdgeTrigger(self, selectorString, iqPowerEdgeTriggerSource, iqPowerEdgeTriggerSlope, iqPowerEdgeTriggerLevel, triggerDelay, minimumQuietTimeMode, minimumQuietTimeDuration, iqPowerEdgeTriggerLevelType, enableTrigger):
        """ ConfigureIQPowerEdgeTrigger(self: RFmxNRMX, selectorString: str, iqPowerEdgeTriggerSource: str, iqPowerEdgeTriggerSlope: RFmxNRMXIQPowerEdgeTriggerSlope, iqPowerEdgeTriggerLevel: float, triggerDelay: float, minimumQuietTimeMode: RFmxNRMXTriggerMinimumQuietTimeMode, minimumQuietTimeDuration: float, iqPowerEdgeTriggerLevelType: RFmxNRMXIQPowerEdgeTriggerLevelType, enableTrigger: bool) -> int """
        pass

    def ConfigureReferenceLevel(self, selectorString, referenceLevel):
        """ ConfigureReferenceLevel(self: RFmxNRMX, selectorString: str, referenceLevel: float) -> int """
        pass

    def ConfigureReferenceLevelUnits(self, selectorString, referenceLevelUnits):
        """ ConfigureReferenceLevelUnits(self: RFmxNRMX, selectorString: str, referenceLevelUnits: RFmxNRMXReferenceLevelUnits) -> int """
        pass

    def ConfigureRF(self, selectorString, centerFrequency, referenceLevel, externalAttenuation):
        """ ConfigureRF(self: RFmxNRMX, selectorString: str, centerFrequency: float, referenceLevel: float, externalAttenuation: float) -> int """
        pass

    def ConfigureSoftwareEdgeTrigger(self, selectorString, triggerDelay, enableTrigger):
        """ ConfigureSoftwareEdgeTrigger(self: RFmxNRMX, selectorString: str, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def DeleteSignalConfiguration(self):
        """ DeleteSignalConfiguration(self: RFmxNRMX) -> int """
        pass

    def DisableTrigger(self, selectorString):
        """ DisableTrigger(self: RFmxNRMX, selectorString: str) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: RFmxNRMX) """
        pass

    def GetAcquisitionBandwidthOptimizationEnabled(self, selectorString, value):
        """ GetAcquisitionBandwidthOptimizationEnabled(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXAcquisitionBandwidthOptimizationEnabled) """
        pass

    def GetAllNamedResultNames(self, selectorString, resultNames, defaultResultExists):
        """ GetAllNamedResultNames(self: RFmxNRMX, selectorString: str) -> (int, Array[str], bool) """
        pass

    def GetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ GetAttributeBool(self: RFmxNRMX, selectorString: str, attributeIdentifier: int) -> (int, bool) """
        pass

    def GetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ GetAttributeDouble(self: RFmxNRMX, selectorString: str, attributeIdentifier: int) -> (int, float) """
        pass

    def GetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ GetAttributeInt(self: RFmxNRMX, selectorString: str, attributeIdentifier: int) -> (int, int) """
        pass

    def GetAttributeSbyte(self, selectorString, attributeIdentifier, value):
        """ GetAttributeSbyte(self: RFmxNRMX, selectorString: str, attributeIdentifier: int) -> (int, SByte) """
        pass

    def GetAttributeString(self, selectorString, attributeIdentifier, value):
        """ GetAttributeString(self: RFmxNRMX, selectorString: str, attributeIdentifier: int) -> (int, str) """
        pass

    def GetAutoIncrementCellIDEnabled(self, selectorString, value):
        """ GetAutoIncrementCellIDEnabled(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXAutoIncrementCellIDEnabled) """
        pass

    def GetAutoResourceBlockDetectionEnabled(self, selectorString, value):
        """ GetAutoResourceBlockDetectionEnabled(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXAutoResourceBlockDetectionEnabled) """
        pass

    def GetBand(self, selectorString, value):
        """ GetBand(self: RFmxNRMX, selectorString: str) -> (int, int) """
        pass

    def GetCenterFrequency(self, selectorString, value):
        """ GetCenterFrequency(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetChannelRaster(self, selectorString, value):
        """ GetChannelRaster(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetComponentCarrierAtCenterFrequency(self, selectorString, value):
        """ GetComponentCarrierAtCenterFrequency(self: RFmxNRMX, selectorString: str) -> (int, int) """
        pass

    def GetComponentCarrierSpacingType(self, selectorString, value):
        """ GetComponentCarrierSpacingType(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXComponentCarrierSpacingType) """
        pass

    def GetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ GetDigitalEdgeTriggerEdge(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXDigitalEdgeTriggerEdge) """
        pass

    def GetDigitalEdgeTriggerSource(self, selectorString, value):
        """ GetDigitalEdgeTriggerSource(self: RFmxNRMX, selectorString: str) -> (int, str) """
        pass

    def GetDownlinkChannelConfigurationMode(self, selectorString, value):
        """ GetDownlinkChannelConfigurationMode(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXDownlinkChannelConfigurationMode) """
        pass

    def GetError(self, errorCode, errorDescription):
        """ GetError(self: RFmxNRMX) -> (int, int, str) """
        pass

    def GetErrorString(self, errorCode, errorDescription):
        """ GetErrorString(self: RFmxNRMX, errorCode: int) -> (int, str) """
        pass

    def GetExternalAttenuation(self, selectorString, value):
        """ GetExternalAttenuation(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyRange(self, selectorString, value):
        """ GetFrequencyRange(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXFrequencyRange) """
        pass

    def GetgNodeBCategory(self, selectorString, value):
        """ GetgNodeBCategory(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXgNodeBCategory) """
        pass

    def GetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevel(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevelType(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXIQPowerEdgeTriggerLevelType) """
        pass

    def GetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSlope(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXIQPowerEdgeTriggerSlope) """
        pass

    def GetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSource(self: RFmxNRMX, selectorString: str) -> (int, str) """
        pass

    def GetLimitedConfigurationChange(self, selectorString, value):
        """ GetLimitedConfigurationChange(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXLimitedConfigurationChange) """
        pass

    def GetLinkDirection(self, selectorString, value):
        """ GetLinkDirection(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXLinkDirection) """
        pass

    def GetNumberOfSubblocks(self, selectorString, value):
        """ GetNumberOfSubblocks(self: RFmxNRMX, selectorString: str) -> (int, int) """
        pass

    def GetPhaseCompensation(self, selectorString, value):
        """ GetPhaseCompensation(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXPhaseCompensation) """
        pass

    def GetPhaseCompensationFrequency(self, selectorString, value):
        """ GetPhaseCompensationFrequency(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetPiBy2BpskPowerBoostEnabled(self, selectorString, value):
        """ GetPiBy2BpskPowerBoostEnabled(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXPiBy2BpskPowerBoostEnabled) """
        pass

    def GetPowerClass(self, selectorString, value):
        """ GetPowerClass(self: RFmxNRMX, selectorString: str) -> (int, int) """
        pass

    def GetReferenceGridAlignmentMode(self, selectorString, value):
        """ GetReferenceGridAlignmentMode(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXReferenceGridAlignmentMode) """
        pass

    def GetReferenceLevel(self, selectorString, value):
        """ GetReferenceLevel(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetReferenceLevelHeadroom(self, selectorString, value):
        """ GetReferenceLevelHeadroom(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetResultFetchTimeout(self, selectorString, value):
        """ GetResultFetchTimeout(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetSelectedPorts(self, selectorString, value):
        """ GetSelectedPorts(self: RFmxNRMX, selectorString: str) -> (int, str) """
        pass

    def GetSubblockEndcNominalSpacingAdjustment(self, selectorString, value):
        """ GetSubblockEndcNominalSpacingAdjustment(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetSubblockFrequencyDefinition(self, selectorString, value):
        """ GetSubblockFrequencyDefinition(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXSubblockFrequencyDefinition) """
        pass

    def GetSubblockTransmitLOFrequency(self, selectorString, value):
        """ GetSubblockTransmitLOFrequency(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetTransmitAntennaToAnalyze(self, selectorString, value):
        """ GetTransmitAntennaToAnalyze(self: RFmxNRMX, selectorString: str) -> (int, int) """
        pass

    def GetTransmitterArchitecture(self, selectorString, value):
        """ GetTransmitterArchitecture(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXTransmitterArchitecture) """
        pass

    def GetTriggerDelay(self, selectorString, value):
        """ GetTriggerDelay(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeDuration(self: RFmxNRMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeMode(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXTriggerMinimumQuietTimeMode) """
        pass

    def GetTriggerType(self, selectorString, value):
        """ GetTriggerType(self: RFmxNRMX, selectorString: str) -> (int, RFmxNRMXTriggerType) """
        pass

    def GetWarning(self, warningCode, warningDescription):
        """ GetWarning(self: RFmxNRMX) -> (int, int, str) """
        pass

    def Initiate(self, selectorString, resultName):
        """ Initiate(self: RFmxNRMX, selectorString: str, resultName: str) -> int """
        pass

    def ResetAttribute(self, selectorString, attributeId):
        """ ResetAttribute(self: RFmxNRMX, selectorString: str, attributeId: RFmxNRMXPropertyId) -> int """
        pass

    def ResetToDefault(self, selectorString):
        """ ResetToDefault(self: RFmxNRMX, selectorString: str) -> int """
        pass

    def SelectMeasurements(self, selectorString, measurement, enableAllTraces):
        """ SelectMeasurements(self: RFmxNRMX, selectorString: str, measurement: RFmxNRMXMeasurementTypes, enableAllTraces: bool) -> int """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RFmxNRMX) -> int """
        pass

    def SetAcquisitionBandwidthOptimizationEnabled(self, selectorString, value):
        """ SetAcquisitionBandwidthOptimizationEnabled(self: RFmxNRMX, selectorString: str, value: RFmxNRMXAcquisitionBandwidthOptimizationEnabled) -> int """
        pass

    def SetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ SetAttributeBool(self: RFmxNRMX, selectorString: str, attributeIdentifier: int, value: bool) -> int """
        pass

    def SetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ SetAttributeDouble(self: RFmxNRMX, selectorString: str, attributeIdentifier: int, value: float) -> int """
        pass

    def SetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ SetAttributeInt(self: RFmxNRMX, selectorString: str, attributeIdentifier: int, value: int) -> int """
        pass

    def SetAttributeSbyte(self, selectorString, attributeIdentifier, value):
        """ SetAttributeSbyte(self: RFmxNRMX, selectorString: str, attributeIdentifier: int, value: SByte) -> int """
        pass

    def SetAttributeString(self, selectorString, attributeIdentifier, value):
        """ SetAttributeString(self: RFmxNRMX, selectorString: str, attributeIdentifier: int, value: str) -> int """
        pass

    def SetAutoIncrementCellIDEnabled(self, selectorString, value):
        """ SetAutoIncrementCellIDEnabled(self: RFmxNRMX, selectorString: str, value: RFmxNRMXAutoIncrementCellIDEnabled) -> int """
        pass

    def SetAutoResourceBlockDetectionEnabled(self, selectorString, value):
        """ SetAutoResourceBlockDetectionEnabled(self: RFmxNRMX, selectorString: str, value: RFmxNRMXAutoResourceBlockDetectionEnabled) -> int """
        pass

    def SetBand(self, selectorString, value):
        """ SetBand(self: RFmxNRMX, selectorString: str, value: int) -> int """
        pass

    def SetCenterFrequency(self, selectorString, value):
        """ SetCenterFrequency(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetChannelRaster(self, selectorString, value):
        """ SetChannelRaster(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetComponentCarrierAtCenterFrequency(self, selectorString, value):
        """ SetComponentCarrierAtCenterFrequency(self: RFmxNRMX, selectorString: str, value: int) -> int """
        pass

    def SetComponentCarrierSpacingType(self, selectorString, value):
        """ SetComponentCarrierSpacingType(self: RFmxNRMX, selectorString: str, value: RFmxNRMXComponentCarrierSpacingType) -> int """
        pass

    def SetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ SetDigitalEdgeTriggerEdge(self: RFmxNRMX, selectorString: str, value: RFmxNRMXDigitalEdgeTriggerEdge) -> int """
        pass

    def SetDigitalEdgeTriggerSource(self, selectorString, value):
        """ SetDigitalEdgeTriggerSource(self: RFmxNRMX, selectorString: str, value: str) -> int """
        pass

    def SetDownlinkChannelConfigurationMode(self, selectorString, value):
        """ SetDownlinkChannelConfigurationMode(self: RFmxNRMX, selectorString: str, value: RFmxNRMXDownlinkChannelConfigurationMode) -> int """
        pass

    def SetExternalAttenuation(self, selectorString, value):
        """ SetExternalAttenuation(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetFrequencyRange(self, selectorString, value):
        """ SetFrequencyRange(self: RFmxNRMX, selectorString: str, value: RFmxNRMXFrequencyRange) -> int """
        pass

    def SetgNodeBCategory(self, selectorString, value):
        """ SetgNodeBCategory(self: RFmxNRMX, selectorString: str, value: RFmxNRMXgNodeBCategory) -> int """
        pass

    def SetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevel(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevelType(self: RFmxNRMX, selectorString: str, value: RFmxNRMXIQPowerEdgeTriggerLevelType) -> int """
        pass

    def SetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSlope(self: RFmxNRMX, selectorString: str, value: RFmxNRMXIQPowerEdgeTriggerSlope) -> int """
        pass

    def SetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSource(self: RFmxNRMX, selectorString: str, value: str) -> int """
        pass

    def SetLimitedConfigurationChange(self, selectorString, value):
        """ SetLimitedConfigurationChange(self: RFmxNRMX, selectorString: str, value: RFmxNRMXLimitedConfigurationChange) -> int """
        pass

    def SetLinkDirection(self, selectorString, value):
        """ SetLinkDirection(self: RFmxNRMX, selectorString: str, value: RFmxNRMXLinkDirection) -> int """
        pass

    def SetNumberOfSubblocks(self, selectorString, value):
        """ SetNumberOfSubblocks(self: RFmxNRMX, selectorString: str, value: int) -> int """
        pass

    def SetPhaseCompensation(self, selectorString, value):
        """ SetPhaseCompensation(self: RFmxNRMX, selectorString: str, value: RFmxNRMXPhaseCompensation) -> int """
        pass

    def SetPhaseCompensationFrequency(self, selectorString, value):
        """ SetPhaseCompensationFrequency(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetPiBy2BpskPowerBoostEnabled(self, selectorString, value):
        """ SetPiBy2BpskPowerBoostEnabled(self: RFmxNRMX, selectorString: str, value: RFmxNRMXPiBy2BpskPowerBoostEnabled) -> int """
        pass

    def SetPowerClass(self, selectorString, value):
        """ SetPowerClass(self: RFmxNRMX, selectorString: str, value: int) -> int """
        pass

    def SetReferenceGridAlignmentMode(self, selectorString, value):
        """ SetReferenceGridAlignmentMode(self: RFmxNRMX, selectorString: str, value: RFmxNRMXReferenceGridAlignmentMode) -> int """
        pass

    def SetReferenceLevel(self, selectorString, value):
        """ SetReferenceLevel(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetReferenceLevelHeadroom(self, selectorString, value):
        """ SetReferenceLevelHeadroom(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetResultFetchTimeout(self, selectorString, value):
        """ SetResultFetchTimeout(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetSelectedPorts(self, selectorString, value):
        """ SetSelectedPorts(self: RFmxNRMX, selectorString: str, value: str) -> int """
        pass

    def SetSubblockEndcNominalSpacingAdjustment(self, selectorString, value):
        """ SetSubblockEndcNominalSpacingAdjustment(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetSubblockFrequencyDefinition(self, selectorString, value):
        """ SetSubblockFrequencyDefinition(self: RFmxNRMX, selectorString: str, value: RFmxNRMXSubblockFrequencyDefinition) -> int """
        pass

    def SetSubblockTransmitLOFrequency(self, selectorString, value):
        """ SetSubblockTransmitLOFrequency(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetTransmitAntennaToAnalyze(self, selectorString, value):
        """ SetTransmitAntennaToAnalyze(self: RFmxNRMX, selectorString: str, value: int) -> int """
        pass

    def SetTransmitterArchitecture(self, selectorString, value):
        """ SetTransmitterArchitecture(self: RFmxNRMX, selectorString: str, value: RFmxNRMXTransmitterArchitecture) -> int """
        pass

    def SetTriggerDelay(self, selectorString, value):
        """ SetTriggerDelay(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeDuration(self: RFmxNRMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeMode(self: RFmxNRMX, selectorString: str, value: RFmxNRMXTriggerMinimumQuietTimeMode) -> int """
        pass

    def SetTriggerType(self, selectorString, value):
        """ SetTriggerType(self: RFmxNRMX, selectorString: str, value: RFmxNRMXTriggerType) -> int """
        pass

    def WaitForMeasurementComplete(self, selectorString, timeout):
        """ WaitForMeasurementComplete(self: RFmxNRMX, selectorString: str, timeout: float) -> int """
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
    """Get: Acp(self: RFmxNRMX) -> RFmxNRMXAcp

"""

    Chp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chp(self: RFmxNRMX) -> RFmxNRMXChp

"""

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMX) -> RFmxNRMXComponentCarrier

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: RFmxNRMX) -> bool

"""

    ModAcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModAcc(self: RFmxNRMX) -> RFmxNRMXModAcc

"""

    Obw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Obw(self: RFmxNRMX) -> RFmxNRMXObw

"""

    Pvt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pvt(self: RFmxNRMX) -> RFmxNRMXPvt

"""

    Sem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sem(self: RFmxNRMX) -> RFmxNRMXSem

"""

    SignalConfigurationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationName(self: RFmxNRMX) -> str

"""

    SignalConfigurationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationType(self: RFmxNRMX) -> Type

"""



class RFmxNRMXSubObject(object):
    # no doc

class RFmxNRMXAcp(RFmxNRMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxNRMXAcp) -> RFmxNRMXAcpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxNRMXAcp) -> RFmxNRMXAcpResults

"""



class RFmxNRMXAcpAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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


class RFmxNRMXAcpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpAveragingEnabled, values: False (0), True (1) """
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


class RFmxNRMXAcpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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


class RFmxNRMXAcpComponentCarrierConfiguration(RFmxNRMXSubObject):
    # no doc
    def GetIntegrationBandwidth(self, selectorString, value):
        """ GetIntegrationBandwidth(self: RFmxNRMXAcpComponentCarrierConfiguration, selectorString: str) -> (int, float) """
        pass


class RFmxNRMXAcpComponentCarrierResults(RFmxNRMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurement(self: RFmxNRMXAcpComponentCarrierResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurementArray(self: RFmxNRMXAcpComponentCarrierResults, selectorString: str, timeout: float, absolutePower: Array[float], relativePower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetAbsolutePower(self, selectorString, value):
        """ GetAbsolutePower(self: RFmxNRMXAcpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetRelativePower(self, selectorString, value):
        """ GetRelativePower(self: RFmxNRMXAcpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass


class RFmxNRMXAcpConfiguration(RFmxNRMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxNRMXAcpConfiguration, selectorString: str, averagingEnabled: RFmxNRMXAcpAveragingEnabled, averagingCount: int, averagingType: RFmxNRMXAcpAveragingType) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxNRMXAcpConfiguration, selectorString: str, measurementMethod: RFmxNRMXAcpMeasurementMethod) -> int """
        pass

    def ConfigureNoiseCompensationEnabled(self, selectorString, noiseCompensationEnabled):
        """ ConfigureNoiseCompensationEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str, noiseCompensationEnabled: RFmxNRMXAcpNoiseCompensationEnabled) -> int """
        pass

    def ConfigureNumberOfEndcOffsets(self, selectorString, numberOfEndcOffsets):
        """ ConfigureNumberOfEndcOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, numberOfEndcOffsets: int) -> int """
        pass

    def ConfigureNumberOfEutraOffsets(self, selectorString, numberOfEutraOffsets):
        """ ConfigureNumberOfEutraOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, numberOfEutraOffsets: int) -> int """
        pass

    def ConfigureNumberOfNROffsets(self, selectorString, numberOfNROffsets):
        """ ConfigureNumberOfNROffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, numberOfNROffsets: int) -> int """
        pass

    def ConfigureNumberOfUtraOffsets(self, selectorString, numberOfUtraOffsets):
        """ ConfigureNumberOfUtraOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, numberOfUtraOffsets: int) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxNRMXAcpConfiguration, selectorString: str, rbwAuto: RFmxNRMXAcpRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxNRMXAcpRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxNRMXAcpConfiguration, selectorString: str, sweepTimeAuto: RFmxNRMXAcpSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpAveragingType) """
        pass

    def GetFarIFOutputPowerOffset(self, selectorString, value):
        """ GetFarIFOutputPowerOffset(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpFftWindow) """
        pass

    def GetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ GetIFOutputPowerOffsetAuto(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpIFOutputPowerOffsetAuto) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpMeasurementMethod) """
        pass

    def GetNearIFOutputPowerOffset(self, selectorString, value):
        """ GetNearIFOutputPowerOffset(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNoiseCompensationEnabled(self, selectorString, value):
        """ GetNoiseCompensationEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpNoiseCompensationEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfEndcOffsets(self, selectorString, value):
        """ GetNumberOfEndcOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfEutraOffsets(self, selectorString, value):
        """ GetNumberOfEutraOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfNROffsets(self, selectorString, value):
        """ GetNumberOfNROffsets(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfUtraOffsets(self, selectorString, value):
        """ GetNumberOfUtraOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetChannelSpacingAdjustment(self, selectorString, value):
        """ GetOffsetChannelSpacingAdjustment(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetFrequency(self, selectorString, value):
        """ GetOffsetFrequency(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetIntegrationBandwidth(self, selectorString, value):
        """ GetOffsetIntegrationBandwidth(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpRbwFilterType) """
        pass

    def GetSequentialFftSize(self, selectorString, value):
        """ GetSequentialFftSize(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, RFmxNRMXAcpSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxNRMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpAveragingType) -> int """
        pass

    def SetFarIFOutputPowerOffset(self, selectorString, value):
        """ SetFarIFOutputPowerOffset(self: RFmxNRMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpFftWindow) -> int """
        pass

    def SetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ SetIFOutputPowerOffsetAuto(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpIFOutputPowerOffsetAuto) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpMeasurementMethod) -> int """
        pass

    def SetNearIFOutputPowerOffset(self, selectorString, value):
        """ SetNearIFOutputPowerOffset(self: RFmxNRMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNoiseCompensationEnabled(self, selectorString, value):
        """ SetNoiseCompensationEnabled(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpNoiseCompensationEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfEndcOffsets(self, selectorString, value):
        """ SetNumberOfEndcOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfEutraOffsets(self, selectorString, value):
        """ SetNumberOfEutraOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfNROffsets(self, selectorString, value):
        """ SetNumberOfNROffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfUtraOffsets(self, selectorString, value):
        """ SetNumberOfUtraOffsets(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetChannelSpacingAdjustment(self, selectorString, value):
        """ SetOffsetChannelSpacingAdjustment(self: RFmxNRMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxNRMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpRbwFilterType) -> int """
        pass

    def SetSequentialFftSize(self, selectorString, value):
        """ SetSequentialFftSize(self: RFmxNRMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxNRMXAcpConfiguration, selectorString: str, value: RFmxNRMXAcpSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxNRMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMXAcpConfiguration) -> RFmxNRMXAcpComponentCarrierConfiguration

"""



class RFmxNRMXAcpFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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


class RFmxNRMXAcpIFOutputPowerOffsetAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpIFOutputPowerOffsetAuto, values: False (0), True (1) """
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


class RFmxNRMXAcpMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpMeasurementMethod, values: DynamicRange (1), Normal (0), SequentialFft (2) """
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


class RFmxNRMXAcpNoiseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpNoiseCompensationEnabled, values: False (0), True (1) """
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


class RFmxNRMXAcpRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxNRMXAcpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
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
    value__ = None


class RFmxNRMXAcpResults(RFmxNRMXSubObject):
    # no doc
    def FetchAbsolutePowersTrace(self, selectorString, timeout, traceIndex, absolutePowersTrace):
        """ FetchAbsolutePowersTrace(self: RFmxNRMXAcpResults, selectorString: str, timeout: float, traceIndex: int, absolutePowersTrace: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchOffsetMeasurement(self, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower):
        """ FetchOffsetMeasurement(self: RFmxNRMXAcpResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchOffsetMeasurementArray(self, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower):
        """ FetchOffsetMeasurementArray(self: RFmxNRMXAcpResults, selectorString: str, timeout: float, lowerRelativePower: Array[float], upperRelativePower: Array[float], lowerAbsolutePower: Array[float], upperAbsolutePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchRelativePowersTrace(self, selectorString, timeout, traceIndex, relativePowersTrace):
        """ FetchRelativePowersTrace(self: RFmxNRMXAcpResults, selectorString: str, timeout: float, traceIndex: int, relativePowersTrace: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxNRMXAcpResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSubblockPower(self, selectorString, timeout, subblockPower):
        """ FetchSubblockPower(self: RFmxNRMXAcpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxNRMXAcpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def GetLowerOffsetAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetAbsolutePower(self: RFmxNRMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativePower(self, selectorString, value):
        """ GetLowerOffsetRelativePower(self: RFmxNRMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockPower(self, selectorString, value):
        """ GetSubblockPower(self: RFmxNRMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalAggregatedPower(self, selectorString, value):
        """ GetTotalAggregatedPower(self: RFmxNRMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetAbsolutePower(self: RFmxNRMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativePower(self, selectorString, value):
        """ GetUpperOffsetRelativePower(self: RFmxNRMXAcpResults, selectorString: str) -> (int, float) """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMXAcpResults) -> RFmxNRMXAcpComponentCarrierResults

"""



class RFmxNRMXAcpSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcpSweepTimeAuto, values: False (0), True (1) """
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


class RFmxNRMXAcquisitionBandwidthOptimizationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAcquisitionBandwidthOptimizationEnabled, values: False (0), True (1) """
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


class RFmxNRMXAutoIncrementCellIDEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAutoIncrementCellIDEnabled, values: False (0), True (1) """
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


class RFmxNRMXAutoResourceBlockDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXAutoResourceBlockDetectionEnabled, values: False (0), True (1) """
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


class RFmxNRMXBandwidthPartCyclicPrefixMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXBandwidthPartCyclicPrefixMode, values: Extended (1), Normal (0) """
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

    Extended = None
    Normal = None
    value__ = None


class RFmxNRMXChp(RFmxNRMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxNRMXChp) -> RFmxNRMXChpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxNRMXChp) -> RFmxNRMXChpResults

"""



class RFmxNRMXChpAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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


class RFmxNRMXChpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpAveragingEnabled, values: False (0), True (1) """
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


class RFmxNRMXChpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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


class RFmxNRMXChpComponentCarrierConfiguration(RFmxNRMXSubObject):
    # no doc
    def GetIntegrationBandwidth(self, selectorString, value):
        """ GetIntegrationBandwidth(self: RFmxNRMXChpComponentCarrierConfiguration, selectorString: str) -> (int, float) """
        pass


class RFmxNRMXChpComponentCarrierResults(RFmxNRMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurement(self: RFmxNRMXChpComponentCarrierResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurementArray(self: RFmxNRMXChpComponentCarrierResults, selectorString: str, timeout: float, absolutePower: Array[float], relativePower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetAbsolutePower(self, selectorString, value):
        """ GetAbsolutePower(self: RFmxNRMXChpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetRelativePower(self, selectorString, value):
        """ GetRelativePower(self: RFmxNRMXChpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass


class RFmxNRMXChpConfiguration(RFmxNRMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxNRMXChpConfiguration, selectorString: str, averagingEnabled: RFmxNRMXChpAveragingEnabled, averagingCount: int, averagingType: RFmxNRMXChpAveragingType) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxNRMXChpConfiguration, selectorString: str, rbwAuto: RFmxNRMXChpRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxNRMXChpRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxNRMXChpConfiguration, selectorString: str, sweepTimeAuto: RFmxNRMXChpSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpAveragingType) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpRbwFilterType) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, RFmxNRMXChpSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxNRMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxNRMXChpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxNRMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpAveragingType) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxNRMXChpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxNRMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxNRMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpRbwFilterType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxNRMXChpConfiguration, selectorString: str, value: RFmxNRMXChpSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxNRMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMXChpConfiguration) -> RFmxNRMXChpComponentCarrierConfiguration

"""



class RFmxNRMXChpFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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


class RFmxNRMXChpRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxNRMXChpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
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
    value__ = None


class RFmxNRMXChpResults(RFmxNRMXSubObject):
    # no doc
    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxNRMXChpResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSubblockPower(self, selectorString, timeout, subblockPower):
        """ FetchSubblockPower(self: RFmxNRMXChpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxNRMXChpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def GetSubblockPower(self, selectorString, value):
        """ GetSubblockPower(self: RFmxNRMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalAggregatedPower(self, selectorString, value):
        """ GetTotalAggregatedPower(self: RFmxNRMXChpResults, selectorString: str) -> (int, float) """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMXChpResults) -> RFmxNRMXChpComponentCarrierResults

"""



class RFmxNRMXChpSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXChpSweepTimeAuto, values: False (0), True (1) """
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


class RFmxNRMXComponentCarrier(RFmxNRMXSubObject):
    # no doc
    def GetBandwidth(self, selectorString, value):
        """ GetBandwidth(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetBandwidthPartCyclicPrefixMode(self, selectorString, value):
        """ GetBandwidthPartCyclicPrefixMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXBandwidthPartCyclicPrefixMode) """
        pass

    def GetBandwidthPartNumberOfResourceBlocks(self, selectorString, value):
        """ GetBandwidthPartNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetBandwidthPartResourceBlockOffset(self, selectorString, value):
        """ GetBandwidthPartResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetBandwidthPartSubcarrierSpacing(self, selectorString, value):
        """ GetBandwidthPartSubcarrierSpacing(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetCellID(self, selectorString, value):
        """ GetCellID(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetCceToRegMappingType(self, selectorString, value):
        """ GetCoresetCceToRegMappingType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXCoresetCceToRegMappingType) """
        pass

    def GetCoresetInterleaverSize(self, selectorString, value):
        """ GetCoresetInterleaverSize(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetNumberOfResourceBlockClusters(self, selectorString, value):
        """ GetCoresetNumberOfResourceBlockClusters(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetNumberOfResourceBlocks(self, selectorString, value):
        """ GetCoresetNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetNumberOfSymbols(self, selectorString, value):
        """ GetCoresetNumberOfSymbols(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetPrecodingGranularity(self, selectorString, value):
        """ GetCoresetPrecodingGranularity(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXCoresetPrecodingGranularity) """
        pass

    def GetCoresetRegBundleSize(self, selectorString, value):
        """ GetCoresetRegBundleSize(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetResourceBlockOffset(self, selectorString, value):
        """ GetCoresetResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetShiftIndex(self, selectorString, value):
        """ GetCoresetShiftIndex(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCoresetSymbolOffset(self, selectorString, value):
        """ GetCoresetSymbolOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetDownlinkTestModel(self, selectorString, value):
        """ GetDownlinkTestModel(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXDownlinkTestModel) """
        pass

    def GetDownlinkTestModelDuplexScheme(self, selectorString, value):
        """ GetDownlinkTestModelDuplexScheme(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXDownlinkTestModelDuplexScheme) """
        pass

    def GetEpreRatioPort(self, selectorString, value):
        """ GetEpreRatioPort(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetFrequency(self, selectorString, value):
        """ GetFrequency(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetGridStart(self, selectorString, value):
        """ GetGridStart(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfBandwidthParts(self, selectorString, value):
        """ GetNumberOfBandwidthParts(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfComponentCarriers(self, selectorString, value):
        """ GetNumberOfComponentCarriers(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfCoresets(self, selectorString, value):
        """ GetNumberOfCoresets(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfPdcchConfigurations(self, selectorString, value):
        """ GetNumberOfPdcchConfigurations(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfPdschConfigurations(self, selectorString, value):
        """ GetNumberOfPdschConfigurations(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfPtrsGroups(self, selectorString, value):
        """ GetNumberOfPtrsGroups(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfPuschConfigurations(self, selectorString, value):
        """ GetNumberOfPuschConfigurations(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfUsers(self, selectorString, value):
        """ GetNumberOfUsers(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPbchDmrsPower(self, selectorString, value):
        """ GetPbchDmrsPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPbchPower(self, selectorString, value):
        """ GetPbchPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPdcchCceAggregationLevel(self, selectorString, value):
        """ GetPdcchCceAggregationLevel(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdcchCceOffset(self, selectorString, value):
        """ GetPdcchCceOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdcchSlotAllocation(self, selectorString, value):
        """ GetPdcchSlotAllocation(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPdschDmrsAdditionalPositions(self, selectorString, value):
        """ GetPdschDmrsAdditionalPositions(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschDmrsAntennaPorts(self, selectorString, value):
        """ GetPdschDmrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPdschDmrsConfigurationType(self, selectorString, value):
        """ GetPdschDmrsConfigurationType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschDmrsConfigurationType) """
        pass

    def GetPdschDmrsDuration(self, selectorString, value):
        """ GetPdschDmrsDuration(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschDmrsDuration) """
        pass

    def GetPdschDmrsnScid(self, selectorString, value):
        """ GetPdschDmrsnScid(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschDmrsNumberOfCdmGroups(self, selectorString, value):
        """ GetPdschDmrsNumberOfCdmGroups(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschDmrsPower(self, selectorString, value):
        """ GetPdschDmrsPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPdschDmrsPowerMode(self, selectorString, value):
        """ GetPdschDmrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschDmrsPowerMode) """
        pass

    def GetPdschDmrsScramblingID(self, selectorString, value):
        """ GetPdschDmrsScramblingID(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschDmrsScramblingIDMode(self, selectorString, value):
        """ GetPdschDmrsScramblingIDMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschDmrsScramblingIDMode) """
        pass

    def GetPdschDmrsTypeAPosition(self, selectorString, value):
        """ GetPdschDmrsTypeAPosition(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschMappingType(self, selectorString, value):
        """ GetPdschMappingType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschMappingType) """
        pass

    def GetPdschModulationType(self, selectorString, value):
        """ GetPdschModulationType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschModulationType) """
        pass

    def GetPdschNumberOfResourceBlockClusters(self, selectorString, value):
        """ GetPdschNumberOfResourceBlockClusters(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschNumberOfResourceBlocks(self, selectorString, value):
        """ GetPdschNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschPresentInSsbResourceBlock(self, selectorString, value):
        """ GetPdschPresentInSsbResourceBlock(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschPresentInSsbResourceBlock) """
        pass

    def GetPdschPtrsAntennaPorts(self, selectorString, value):
        """ GetPdschPtrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPdschPtrsEnabled(self, selectorString, value):
        """ GetPdschPtrsEnabled(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschPtrsEnabled) """
        pass

    def GetPdschPtrsFrequencyDensity(self, selectorString, value):
        """ GetPdschPtrsFrequencyDensity(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschPtrsPower(self, selectorString, value):
        """ GetPdschPtrsPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPdschPtrsPowerMode(self, selectorString, value):
        """ GetPdschPtrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPdschPtrsPowerMode) """
        pass

    def GetPdschPtrsREOffset(self, selectorString, value):
        """ GetPdschPtrsREOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschPtrsTimeDensity(self, selectorString, value):
        """ GetPdschPtrsTimeDensity(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschResourceBlockOffset(self, selectorString, value):
        """ GetPdschResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPdschSlotAllocation(self, selectorString, value):
        """ GetPdschSlotAllocation(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPdschSymbolAllocation(self, selectorString, value):
        """ GetPdschSymbolAllocation(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPssPower(self, selectorString, value):
        """ GetPssPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPuschDmrsAdditionalPositions(self, selectorString, value):
        """ GetPuschDmrsAdditionalPositions(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschDmrsAntennaPorts(self, selectorString, value):
        """ GetPuschDmrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPuschDmrsConfigurationType(self, selectorString, value):
        """ GetPuschDmrsConfigurationType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsConfigurationType) """
        pass

    def GetPuschDmrsDuration(self, selectorString, value):
        """ GetPuschDmrsDuration(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsDuration) """
        pass

    def GetPuschDmrsGroupHoppingEnabled(self, selectorString, value):
        """ GetPuschDmrsGroupHoppingEnabled(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsGroupHoppingEnabled) """
        pass

    def GetPuschDmrsNscid(self, selectorString, value):
        """ GetPuschDmrsNscid(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschDmrsNumberOfCdmGroups(self, selectorString, value):
        """ GetPuschDmrsNumberOfCdmGroups(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschDmrsPower(self, selectorString, value):
        """ GetPuschDmrsPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPuschDmrsPowerMode(self, selectorString, value):
        """ GetPuschDmrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsPowerMode) """
        pass

    def GetPuschDmrsPuschID(self, selectorString, value):
        """ GetPuschDmrsPuschID(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschDmrsPuschIDMode(self, selectorString, value):
        """ GetPuschDmrsPuschIDMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsPuschIDMode) """
        pass

    def GetPuschDmrsScramblingID(self, selectorString, value):
        """ GetPuschDmrsScramblingID(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschDmrsScramblingIDMode(self, selectorString, value):
        """ GetPuschDmrsScramblingIDMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsScramblingIDMode) """
        pass

    def GetPuschDmrsSequenceHoppingEnabled(self, selectorString, value):
        """ GetPuschDmrsSequenceHoppingEnabled(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschDmrsSequenceHoppingEnabled) """
        pass

    def GetPuschDmrsTypeAPosition(self, selectorString, value):
        """ GetPuschDmrsTypeAPosition(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschMappingType(self, selectorString, value):
        """ GetPuschMappingType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschMappingType) """
        pass

    def GetPuschModulationType(self, selectorString, value):
        """ GetPuschModulationType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschModulationType) """
        pass

    def GetPuschNumberOfResourceBlockClusters(self, selectorString, value):
        """ GetPuschNumberOfResourceBlockClusters(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschNumberOfResourceBlocks(self, selectorString, value):
        """ GetPuschNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschPtrsAntennaPorts(self, selectorString, value):
        """ GetPuschPtrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPuschPtrsEnabled(self, selectorString, value):
        """ GetPuschPtrsEnabled(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschPtrsEnabled) """
        pass

    def GetPuschPtrsFrequencyDensity(self, selectorString, value):
        """ GetPuschPtrsFrequencyDensity(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschPtrsPower(self, selectorString, value):
        """ GetPuschPtrsPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPuschPtrsPowerMode(self, selectorString, value):
        """ GetPuschPtrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschPtrsPowerMode) """
        pass

    def GetPuschPtrsREOffset(self, selectorString, value):
        """ GetPuschPtrsREOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschPtrsTimeDensity(self, selectorString, value):
        """ GetPuschPtrsTimeDensity(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschResourceBlockOffset(self, selectorString, value):
        """ GetPuschResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschSlotAllocation(self, selectorString, value):
        """ GetPuschSlotAllocation(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPuschSymbolAllocation(self, selectorString, value):
        """ GetPuschSymbolAllocation(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPuschTransformPrecodingEnabled(self, selectorString, value):
        """ GetPuschTransformPrecodingEnabled(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXPuschTransformPrecodingEnabled) """
        pass

    def GetRadioAccessType(self, selectorString, value):
        """ GetRadioAccessType(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXComponentCarrierRadioAccessType) """
        pass

    def GetReferenceGridStart(self, selectorString, value):
        """ GetReferenceGridStart(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetReferenceGridSubcarrierSpacing(self, selectorString, value):
        """ GetReferenceGridSubcarrierSpacing(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetRnti(self, selectorString, value):
        """ GetRnti(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSamplesPerPtrsGroup(self, selectorString, value):
        """ GetSamplesPerPtrsGroup(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSsbActiveBlocks(self, selectorString, value):
        """ GetSsbActiveBlocks(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetSsbCrbOffset(self, selectorString, value):
        """ GetSsbCrbOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSsbEnabled(self, selectorString, value):
        """ GetSsbEnabled(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXSsbEnabled) """
        pass

    def GetSsbPattern(self, selectorString, value):
        """ GetSsbPattern(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, RFmxNRMXSsbPattern) """
        pass

    def GetSsbPeriodicity(self, selectorString, value):
        """ GetSsbPeriodicity(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetSsbSubcarrierOffset(self, selectorString, value):
        """ GetSsbSubcarrierOffset(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSssPower(self, selectorString, value):
        """ GetSssPower(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetSubcarrierSpacingCommon(self, selectorString, value):
        """ GetSubcarrierSpacingCommon(self: RFmxNRMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def SetBandwidth(self, selectorString, value):
        """ SetBandwidth(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetBandwidthPartCyclicPrefixMode(self, selectorString, value):
        """ SetBandwidthPartCyclicPrefixMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXBandwidthPartCyclicPrefixMode) -> int """
        pass

    def SetBandwidthPartNumberOfResourceBlocks(self, selectorString, value):
        """ SetBandwidthPartNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetBandwidthPartResourceBlockOffset(self, selectorString, value):
        """ SetBandwidthPartResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetBandwidthPartSubcarrierSpacing(self, selectorString, value):
        """ SetBandwidthPartSubcarrierSpacing(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetCellID(self, selectorString, value):
        """ SetCellID(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetCceToRegMappingType(self, selectorString, value):
        """ SetCoresetCceToRegMappingType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXCoresetCceToRegMappingType) -> int """
        pass

    def SetCoresetInterleaverSize(self, selectorString, value):
        """ SetCoresetInterleaverSize(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetNumberOfResourceBlockClusters(self, selectorString, value):
        """ SetCoresetNumberOfResourceBlockClusters(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetNumberOfResourceBlocks(self, selectorString, value):
        """ SetCoresetNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetNumberOfSymbols(self, selectorString, value):
        """ SetCoresetNumberOfSymbols(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetPrecodingGranularity(self, selectorString, value):
        """ SetCoresetPrecodingGranularity(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXCoresetPrecodingGranularity) -> int """
        pass

    def SetCoresetRegBundleSize(self, selectorString, value):
        """ SetCoresetRegBundleSize(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetResourceBlockOffset(self, selectorString, value):
        """ SetCoresetResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetShiftIndex(self, selectorString, value):
        """ SetCoresetShiftIndex(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCoresetSymbolOffset(self, selectorString, value):
        """ SetCoresetSymbolOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetDownlinkTestModel(self, selectorString, value):
        """ SetDownlinkTestModel(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXDownlinkTestModel) -> int """
        pass

    def SetDownlinkTestModelDuplexScheme(self, selectorString, value):
        """ SetDownlinkTestModelDuplexScheme(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXDownlinkTestModelDuplexScheme) -> int """
        pass

    def SetEpreRatioPort(self, selectorString, value):
        """ SetEpreRatioPort(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetFrequency(self, selectorString, value):
        """ SetFrequency(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetGridStart(self, selectorString, value):
        """ SetGridStart(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfBandwidthParts(self, selectorString, value):
        """ SetNumberOfBandwidthParts(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfComponentCarriers(self, selectorString, value):
        """ SetNumberOfComponentCarriers(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfCoresets(self, selectorString, value):
        """ SetNumberOfCoresets(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfPdcchConfigurations(self, selectorString, value):
        """ SetNumberOfPdcchConfigurations(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfPdschConfigurations(self, selectorString, value):
        """ SetNumberOfPdschConfigurations(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfPtrsGroups(self, selectorString, value):
        """ SetNumberOfPtrsGroups(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfPuschConfigurations(self, selectorString, value):
        """ SetNumberOfPuschConfigurations(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfUsers(self, selectorString, value):
        """ SetNumberOfUsers(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPbchDmrsPower(self, selectorString, value):
        """ SetPbchDmrsPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPbchPower(self, selectorString, value):
        """ SetPbchPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPdcchCceAggregationLevel(self, selectorString, value):
        """ SetPdcchCceAggregationLevel(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdcchCceOffset(self, selectorString, value):
        """ SetPdcchCceOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdcchSlotAllocation(self, selectorString, value):
        """ SetPdcchSlotAllocation(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPdschDmrsAdditionalPositions(self, selectorString, value):
        """ SetPdschDmrsAdditionalPositions(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschDmrsAntennaPorts(self, selectorString, value):
        """ SetPdschDmrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPdschDmrsConfigurationType(self, selectorString, value):
        """ SetPdschDmrsConfigurationType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschDmrsConfigurationType) -> int """
        pass

    def SetPdschDmrsDuration(self, selectorString, value):
        """ SetPdschDmrsDuration(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschDmrsDuration) -> int """
        pass

    def SetPdschDmrsnScid(self, selectorString, value):
        """ SetPdschDmrsnScid(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschDmrsNumberOfCdmGroups(self, selectorString, value):
        """ SetPdschDmrsNumberOfCdmGroups(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschDmrsPower(self, selectorString, value):
        """ SetPdschDmrsPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPdschDmrsPowerMode(self, selectorString, value):
        """ SetPdschDmrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschDmrsPowerMode) -> int """
        pass

    def SetPdschDmrsScramblingID(self, selectorString, value):
        """ SetPdschDmrsScramblingID(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschDmrsScramblingIDMode(self, selectorString, value):
        """ SetPdschDmrsScramblingIDMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschDmrsScramblingIDMode) -> int """
        pass

    def SetPdschDmrsTypeAPosition(self, selectorString, value):
        """ SetPdschDmrsTypeAPosition(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschMappingType(self, selectorString, value):
        """ SetPdschMappingType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschMappingType) -> int """
        pass

    def SetPdschModulationType(self, selectorString, value):
        """ SetPdschModulationType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschModulationType) -> int """
        pass

    def SetPdschNumberOfResourceBlockClusters(self, selectorString, value):
        """ SetPdschNumberOfResourceBlockClusters(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschNumberOfResourceBlocks(self, selectorString, value):
        """ SetPdschNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschPresentInSsbResourceBlock(self, selectorString, value):
        """ SetPdschPresentInSsbResourceBlock(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschPresentInSsbResourceBlock) -> int """
        pass

    def SetPdschPtrsAntennaPorts(self, selectorString, value):
        """ SetPdschPtrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPdschPtrsEnabled(self, selectorString, value):
        """ SetPdschPtrsEnabled(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschPtrsEnabled) -> int """
        pass

    def SetPdschPtrsFrequencyDensity(self, selectorString, value):
        """ SetPdschPtrsFrequencyDensity(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschPtrsPower(self, selectorString, value):
        """ SetPdschPtrsPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPdschPtrsPowerMode(self, selectorString, value):
        """ SetPdschPtrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPdschPtrsPowerMode) -> int """
        pass

    def SetPdschPtrsREOffset(self, selectorString, value):
        """ SetPdschPtrsREOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschPtrsTimeDensity(self, selectorString, value):
        """ SetPdschPtrsTimeDensity(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschResourceBlockOffset(self, selectorString, value):
        """ SetPdschResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPdschSlotAllocation(self, selectorString, value):
        """ SetPdschSlotAllocation(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPdschSymbolAllocation(self, selectorString, value):
        """ SetPdschSymbolAllocation(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPssPower(self, selectorString, value):
        """ SetPssPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPuschDmrsAdditionalPositions(self, selectorString, value):
        """ SetPuschDmrsAdditionalPositions(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschDmrsAntennaPorts(self, selectorString, value):
        """ SetPuschDmrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPuschDmrsConfigurationType(self, selectorString, value):
        """ SetPuschDmrsConfigurationType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsConfigurationType) -> int """
        pass

    def SetPuschDmrsDuration(self, selectorString, value):
        """ SetPuschDmrsDuration(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsDuration) -> int """
        pass

    def SetPuschDmrsGroupHoppingEnabled(self, selectorString, value):
        """ SetPuschDmrsGroupHoppingEnabled(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsGroupHoppingEnabled) -> int """
        pass

    def SetPuschDmrsNscid(self, selectorString, value):
        """ SetPuschDmrsNscid(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschDmrsNumberOfCdmGroups(self, selectorString, value):
        """ SetPuschDmrsNumberOfCdmGroups(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschDmrsPower(self, selectorString, value):
        """ SetPuschDmrsPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPuschDmrsPowerMode(self, selectorString, value):
        """ SetPuschDmrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsPowerMode) -> int """
        pass

    def SetPuschDmrsPuschID(self, selectorString, value):
        """ SetPuschDmrsPuschID(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschDmrsPuschIDMode(self, selectorString, value):
        """ SetPuschDmrsPuschIDMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsPuschIDMode) -> int """
        pass

    def SetPuschDmrsScramblingID(self, selectorString, value):
        """ SetPuschDmrsScramblingID(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschDmrsScramblingIDMode(self, selectorString, value):
        """ SetPuschDmrsScramblingIDMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsScramblingIDMode) -> int """
        pass

    def SetPuschDmrsSequenceHoppingEnabled(self, selectorString, value):
        """ SetPuschDmrsSequenceHoppingEnabled(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschDmrsSequenceHoppingEnabled) -> int """
        pass

    def SetPuschDmrsTypeAPosition(self, selectorString, value):
        """ SetPuschDmrsTypeAPosition(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschMappingType(self, selectorString, value):
        """ SetPuschMappingType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschMappingType) -> int """
        pass

    def SetPuschModulationType(self, selectorString, value):
        """ SetPuschModulationType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschModulationType) -> int """
        pass

    def SetPuschNumberOfResourceBlockClusters(self, selectorString, value):
        """ SetPuschNumberOfResourceBlockClusters(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschNumberOfResourceBlocks(self, selectorString, value):
        """ SetPuschNumberOfResourceBlocks(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschPtrsAntennaPorts(self, selectorString, value):
        """ SetPuschPtrsAntennaPorts(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPuschPtrsEnabled(self, selectorString, value):
        """ SetPuschPtrsEnabled(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschPtrsEnabled) -> int """
        pass

    def SetPuschPtrsFrequencyDensity(self, selectorString, value):
        """ SetPuschPtrsFrequencyDensity(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschPtrsPower(self, selectorString, value):
        """ SetPuschPtrsPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPuschPtrsPowerMode(self, selectorString, value):
        """ SetPuschPtrsPowerMode(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschPtrsPowerMode) -> int """
        pass

    def SetPuschPtrsREOffset(self, selectorString, value):
        """ SetPuschPtrsREOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschPtrsTimeDensity(self, selectorString, value):
        """ SetPuschPtrsTimeDensity(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschResourceBlockOffset(self, selectorString, value):
        """ SetPuschResourceBlockOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschSlotAllocation(self, selectorString, value):
        """ SetPuschSlotAllocation(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPuschSymbolAllocation(self, selectorString, value):
        """ SetPuschSymbolAllocation(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPuschTransformPrecodingEnabled(self, selectorString, value):
        """ SetPuschTransformPrecodingEnabled(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXPuschTransformPrecodingEnabled) -> int """
        pass

    def SetRadioAccessType(self, selectorString, value):
        """ SetRadioAccessType(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXComponentCarrierRadioAccessType) -> int """
        pass

    def SetReferenceGridStart(self, selectorString, value):
        """ SetReferenceGridStart(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetReferenceGridSubcarrierSpacing(self, selectorString, value):
        """ SetReferenceGridSubcarrierSpacing(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetRnti(self, selectorString, value):
        """ SetRnti(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSamplesPerPtrsGroup(self, selectorString, value):
        """ SetSamplesPerPtrsGroup(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSsbActiveBlocks(self, selectorString, value):
        """ SetSsbActiveBlocks(self: RFmxNRMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetSsbCrbOffset(self, selectorString, value):
        """ SetSsbCrbOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSsbEnabled(self, selectorString, value):
        """ SetSsbEnabled(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXSsbEnabled) -> int """
        pass

    def SetSsbPattern(self, selectorString, value):
        """ SetSsbPattern(self: RFmxNRMXComponentCarrier, selectorString: str, value: RFmxNRMXSsbPattern) -> int """
        pass

    def SetSsbPeriodicity(self, selectorString, value):
        """ SetSsbPeriodicity(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetSsbSubcarrierOffset(self, selectorString, value):
        """ SetSsbSubcarrierOffset(self: RFmxNRMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSssPower(self, selectorString, value):
        """ SetSssPower(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetSubcarrierSpacingCommon(self, selectorString, value):
        """ SetSubcarrierSpacingCommon(self: RFmxNRMXComponentCarrier, selectorString: str, value: float) -> int """
        pass


class RFmxNRMXComponentCarrierRadioAccessType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXComponentCarrierRadioAccessType, values: Eutra (1), NR (0) """
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

    Eutra = None
    NR = None
    value__ = None


class RFmxNRMXComponentCarrierSpacingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXComponentCarrierSpacingType, values: Nominal (0), User (2) """
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

    Nominal = None
    User = None
    value__ = None


class RFmxNRMXConstants(object):
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


class RFmxNRMXCoresetCceToRegMappingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXCoresetCceToRegMappingType, values: Interleaved (1), NonInterleaved (0) """
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

    Interleaved = None
    NonInterleaved = None
    value__ = None


class RFmxNRMXCoresetPrecodingGranularity(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXCoresetPrecodingGranularity, values: AllContiguousResourceBlocks (1), SameAsRegBundle (0) """
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

    AllContiguousResourceBlocks = None
    SameAsRegBundle = None
    value__ = None


class RFmxNRMXDigitalEdgeTriggerEdge(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXDigitalEdgeTriggerEdge, values: Falling (1), Rising (0) """
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


class RFmxNRMXDownlinkChannelConfigurationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXDownlinkChannelConfigurationMode, values: TestModel (2), UserDefined (1) """
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

    TestModel = None
    UserDefined = None
    value__ = None


class RFmxNRMXDownlinkTestModel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXDownlinkTestModel, values: TM1_1 (0), TM1_2 (1), TM2 (2), TM2a (3), TM3_1 (4), TM3_1a (5), TM3_2 (6), TM3_3 (7) """
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

    TM1_1 = None
    TM1_2 = None
    TM2 = None
    TM2a = None
    TM3_1 = None
    TM3_1a = None
    TM3_2 = None
    TM3_3 = None
    value__ = None


class RFmxNRMXDownlinkTestModelDuplexScheme(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXDownlinkTestModelDuplexScheme, values: Fdd (0), Tdd (1) """
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

    Fdd = None
    Tdd = None
    value__ = None


class RFmxNRMXFrequencyRange(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXFrequencyRange, values: Range1 (0), Range2 (1) """
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

    Range1 = None
    Range2 = None
    value__ = None


class RFmxNRMXgNodeBCategory(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXgNodeBCategory, values: FR2CategoryA (6), FR2CategoryB (7), LocalAreaBaseStation (3), MediumRangeBaseStation (5), WideAreaBaseStationCategoryA (0), WideAreaBaseStationCategoryBOption1 (1), WideAreaBaseStationCategoryBOption2 (2) """
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

    FR2CategoryA = None
    FR2CategoryB = None
    LocalAreaBaseStation = None
    MediumRangeBaseStation = None
    value__ = None
    WideAreaBaseStationCategoryA = None
    WideAreaBaseStationCategoryBOption1 = None
    WideAreaBaseStationCategoryBOption2 = None


class RFmxNRMXIQPowerEdgeTriggerLevelType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXIQPowerEdgeTriggerLevelType, values: Absolute (1), Relative (0) """
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


class RFmxNRMXIQPowerEdgeTriggerSlope(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXIQPowerEdgeTriggerSlope, values: Falling (1), Rising (0) """
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


class RFmxNRMXLimitedConfigurationChange(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXLimitedConfigurationChange, values: Disabled (0), Frequency (2), FrequencyAndReferenceLevel (4), NoChange (1), ReferenceLevel (3), SelectedPortsFrequencyAndReferenceLevel (5) """
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


class RFmxNRMXLinkDirection(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXLinkDirection, values: Downlink (0), Uplink (1) """
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

    Downlink = None
    Uplink = None
    value__ = None


class RFmxNRMXMeasurementTypes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RFmxNRMXMeasurementTypes, values: Acp (4), Chp (8), ModAcc (1), Obw (16), Pvt (32), Sem (2) """
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
    Chp = None
    ModAcc = None
    Obw = None
    Pvt = None
    Sem = None
    value__ = None


class RFmxNRMXModAcc(RFmxNRMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxNRMXModAcc) -> RFmxNRMXModAccConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxNRMXModAcc) -> RFmxNRMXModAccResults

"""



class RFmxNRMXModAccAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccAveragingEnabled, values: False (0), True (1) """
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


class RFmxNRMXModAccChannelEstimationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccChannelEstimationType, values: Reference (0), ReferenceAndData (1) """
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

    Reference = None
    ReferenceAndData = None
    value__ = None


class RFmxNRMXModAccCommonClockSourceEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccCommonClockSourceEnabled, values: False (0), True (1) """
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


class RFmxNRMXModAccCompositeResultsIncludeDmrs(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccCompositeResultsIncludeDmrs, values: False (0), True (1) """
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


class RFmxNRMXModAccCompositeResultsIncludePtrs(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccCompositeResultsIncludePtrs, values: False (0), True (1) """
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


class RFmxNRMXModAccConfiguration(RFmxNRMXSubObject):
    # no doc
    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccAveragingEnabled) """
        pass

    def GetChannelEstimationType(self, selectorString, value):
        """ GetChannelEstimationType(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccChannelEstimationType) """
        pass

    def GetCommonClockSourceEnabled(self, selectorString, value):
        """ GetCommonClockSourceEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccCommonClockSourceEnabled) """
        pass

    def GetCompositeResultsIncludeDmrs(self, selectorString, value):
        """ GetCompositeResultsIncludeDmrs(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccCompositeResultsIncludeDmrs) """
        pass

    def GetCompositeResultsIncludePtrs(self, selectorString, value):
        """ GetCompositeResultsIncludePtrs(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccCompositeResultsIncludePtrs) """
        pass

    def GetDCSubcarrierRemovalEnabled(self, selectorString, value):
        """ GetDCSubcarrierRemovalEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccDCSubcarrierRemovalEnabled) """
        pass

    def GetEvmUnit(self, selectorString, value):
        """ GetEvmUnit(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccEvmUnit) """
        pass

    def GetEvmWithExclusionPeriodEnabled(self, selectorString, value):
        """ GetEvmWithExclusionPeriodEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccEvmWithExclusionPeriodEnabled) """
        pass

    def GetFftWindowLength(self, selectorString, value):
        """ GetFftWindowLength(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindowOffset(self, selectorString, value):
        """ GetFftWindowOffset(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindowType(self, selectorString, value):
        """ GetFftWindowType(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccFftWindowType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementLength(self, selectorString, value):
        """ GetMeasurementLength(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementLengthUnit(self, selectorString, value):
        """ GetMeasurementLengthUnit(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccMeasurementLengthUnit) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMulticarrierFilterEnabled(self, selectorString, value):
        """ GetMulticarrierFilterEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccMulticarrierFilterEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetPhaseTrackingEnabled(self, selectorString, value):
        """ GetPhaseTrackingEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccPhaseTrackingEnabled) """
        pass

    def GetSpectralFlatnessCondition(self, selectorString, value):
        """ GetSpectralFlatnessCondition(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccSpectralFlatnessCondition) """
        pass

    def GetSpectrumInverted(self, selectorString, value):
        """ GetSpectrumInverted(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccSpectrumInverted) """
        pass

    def GetSynchronizationMode(self, selectorString, value):
        """ GetSynchronizationMode(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModAccSynchronizationMode) """
        pass

    def GetTimingTrackingEnabled(self, selectorString, value):
        """ GetTimingTrackingEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str) -> (int, RFmxNRMXModTimingTrackingEnabled) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxNRMXModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccAveragingEnabled) -> int """
        pass

    def SetChannelEstimationType(self, selectorString, value):
        """ SetChannelEstimationType(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccChannelEstimationType) -> int """
        pass

    def SetCommonClockSourceEnabled(self, selectorString, value):
        """ SetCommonClockSourceEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccCommonClockSourceEnabled) -> int """
        pass

    def SetCompositeResultsIncludeDmrs(self, selectorString, value):
        """ SetCompositeResultsIncludeDmrs(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccCompositeResultsIncludeDmrs) -> int """
        pass

    def SetCompositeResultsIncludePtrs(self, selectorString, value):
        """ SetCompositeResultsIncludePtrs(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccCompositeResultsIncludePtrs) -> int """
        pass

    def SetDCSubcarrierRemovalEnabled(self, selectorString, value):
        """ SetDCSubcarrierRemovalEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccDCSubcarrierRemovalEnabled) -> int """
        pass

    def SetEvmUnit(self, selectorString, value):
        """ SetEvmUnit(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccEvmUnit) -> int """
        pass

    def SetEvmWithExclusionPeriodEnabled(self, selectorString, value):
        """ SetEvmWithExclusionPeriodEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccEvmWithExclusionPeriodEnabled) -> int """
        pass

    def SetFftWindowLength(self, selectorString, value):
        """ SetFftWindowLength(self: RFmxNRMXModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindowOffset(self, selectorString, value):
        """ SetFftWindowOffset(self: RFmxNRMXModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindowType(self, selectorString, value):
        """ SetFftWindowType(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccFftWindowType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementLength(self, selectorString, value):
        """ SetMeasurementLength(self: RFmxNRMXModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementLengthUnit(self, selectorString, value):
        """ SetMeasurementLengthUnit(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccMeasurementLengthUnit) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxNRMXModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMulticarrierFilterEnabled(self, selectorString, value):
        """ SetMulticarrierFilterEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccMulticarrierFilterEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxNRMXModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetPhaseTrackingEnabled(self, selectorString, value):
        """ SetPhaseTrackingEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccPhaseTrackingEnabled) -> int """
        pass

    def SetSpectralFlatnessCondition(self, selectorString, value):
        """ SetSpectralFlatnessCondition(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccSpectralFlatnessCondition) -> int """
        pass

    def SetSpectrumInverted(self, selectorString, value):
        """ SetSpectrumInverted(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccSpectrumInverted) -> int """
        pass

    def SetSynchronizationMode(self, selectorString, value):
        """ SetSynchronizationMode(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModAccSynchronizationMode) -> int """
        pass

    def SetTimingTrackingEnabled(self, selectorString, value):
        """ SetTimingTrackingEnabled(self: RFmxNRMXModAccConfiguration, selectorString: str, value: RFmxNRMXModTimingTrackingEnabled) -> int """
        pass


class RFmxNRMXModAccDCSubcarrierRemovalEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccDCSubcarrierRemovalEnabled, values: False (0), True (1) """
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


class RFmxNRMXModAccEvmUnit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccEvmUnit, values: dB (1), Percentage (0) """
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

    dB = None
    Percentage = None
    value__ = None


class RFmxNRMXModAccEvmWithExclusionPeriodEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccEvmWithExclusionPeriodEnabled, values: False (0), True (1) """
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


class RFmxNRMXModAccFftWindowType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccFftWindowType, values: Type3GPP (0), TypeCustom (1) """
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

    Type3GPP = None
    TypeCustom = None
    value__ = None


class RFmxNRMXModAccFrequencyErrorEstimation(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccFrequencyErrorEstimation, values: Normal (1), Wide (2) """
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

    Normal = None
    value__ = None
    Wide = None


class RFmxNRMXModAccMeasurementLengthUnit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccMeasurementLengthUnit, values: Slot (1), Subframe (3), Time (6) """
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

    Slot = None
    Subframe = None
    Time = None
    value__ = None


class RFmxNRMXModAccMulticarrierFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccMulticarrierFilterEnabled, values: False (0), True (1) """
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


class RFmxNRMXModAccPhaseTrackingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccPhaseTrackingEnabled, values: False (0), True (1) """
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


class RFmxNRMXModAccResults(RFmxNRMXSubObject):
    # no doc
    def FetchComponentCarrierIQImpairments(self, selectorString, timeout, componentCarrierIQOriginOffsetMean, componentCarrierIQGainImbalanceMean, componentCarrierIQQuadratureErrorMean):
        """ FetchComponentCarrierIQImpairments(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchCompositeEvm(self, selectorString, timeout, compositeRmsEvmMean, compositePeakEvmMaximum):
        """ FetchCompositeEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchCompositeMagnitudeAndPhaseError(self, selectorString, timeout, compositeRmsMagnitudeErrorMean, compositePeakMagnitudeErrorMaximum, compositeRmsPhaseErrorMean, compositePeakPhaseErrorMaximum):
        """ FetchCompositeMagnitudeAndPhaseError(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchCompositeMagnitudeAndPhaseErrorArray(self, selectorString, timeout, compositeRmsMagnitudeErrorMean, compositePeakMagnitudeErrorMaximum, compositeRmsPhaseErrorMean, compositePeakPhaseErrorMaximum):
        """ FetchCompositeMagnitudeAndPhaseErrorArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, compositeRmsMagnitudeErrorMean: Array[float], compositePeakMagnitudeErrorMaximum: Array[float], compositeRmsPhaseErrorMean: Array[float], compositePeakPhaseErrorMaximum: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchFrequencyErrorMean(self, selectorString, timeout, frequencyErrorMean):
        """ FetchFrequencyErrorMean(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchInBandEmissionMargin(self, selectorString, timeout, inBandEmissionMargin):
        """ FetchInBandEmissionMargin(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchInBandEmissionMarginArray(self, selectorString, timeout, inBandEmissionMargin):
        """ FetchInBandEmissionMarginArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, inBandEmissionMargin: Array[float]) -> (int, Array[float]) """
        pass

    def FetchInBandEmissionTrace(self, selectorString, timeout, inBandEmission, inBandEmissionMask):
        """ FetchInBandEmissionTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, inBandEmission: AnalogWaveform[Single], inBandEmissionMask: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchPdsch16QamConstellationTrace(self, selectorString, timeout, qam16Constellation):
        """ FetchPdsch16QamConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, qam16Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdsch256QamConstellationTrace(self, selectorString, timeout, qam256Constellation):
        """ FetchPdsch256QamConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, qam256Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdsch64QamConstellationTrace(self, selectorString, timeout, qam64Constellation):
        """ FetchPdsch64QamConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, qam64Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdschDataConstellationTrace(self, selectorString, timeout, pdschDataConstellation):
        """ FetchPdschDataConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschDataConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdschDataEvm(self, selectorString, timeout, pdschDataRmsEvmMean, pdschDataPeakEvmMaximum):
        """ FetchPdschDataEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPdschDataEvmArray(self, selectorString, timeout, pdschDataRmsEvmMean, pdschDataPeakEvmMaximum):
        """ FetchPdschDataEvmArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschDataRmsEvmMean: Array[float], pdschDataPeakEvmMaximum: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPdschDemodulatedBits(self, selectorString, timeout, bits):
        """ FetchPdschDemodulatedBits(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, bits: Array[SByte]) -> (int, Array[SByte]) """
        pass

    def FetchPdschDmrsConstellationTrace(self, selectorString, timeout, pdschDmrsConstellation):
        """ FetchPdschDmrsConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschDmrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdschDmrsEvm(self, selectorString, timeout, pdschDmrsRmsEvmMean, pdschDmrsPeakEvmMaximum):
        """ FetchPdschDmrsEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPdschDmrsEvmArray(self, selectorString, timeout, pdschDmrsRmsEvmMean, pdschDmrsPeakEvmMaximum):
        """ FetchPdschDmrsEvmArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschDmrsRmsEvmMean: Array[float], pdschDmrsPeakEvmMaximum: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPdschPtrsConstellationTrace(self, selectorString, timeout, pdschPtrsConstellation):
        """ FetchPdschPtrsConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschPtrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdschPtrsEvm(self, selectorString, timeout, pdschPtrsRmsEvmMean, pdschPtrsPeakEvmMaximum):
        """ FetchPdschPtrsEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPdschPtrsEvmArray(self, selectorString, timeout, pdschPtrsRmsEvmMean, pdschPtrsPeakEvmMaximum):
        """ FetchPdschPtrsEvmArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschPtrsRmsEvmMean: Array[float], pdschPtrsPeakEvmMaximum: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPdschQpskConstellationTrace(self, selectorString, timeout, qpskConstellation):
        """ FetchPdschQpskConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, qpskConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdschSymbolPower(self, selectorString, timeout, pdschDataPowerMean, pdschDmrsPowerMean, pdschPtrsPowerMean):
        """ FetchPdschSymbolPower(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchPdschSymbolPowerArray(self, selectorString, timeout, pdschDataPowerMean, pdschDmrsPowerMean, pdschPtrsPowerMean):
        """ FetchPdschSymbolPowerArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, pdschDataPowerMean: Array[float], pdschDmrsPowerMean: Array[float], pdschPtrsPowerMean: Array[float]) -> (int, Array[float], Array[float], Array[float]) """
        pass

    def FetchPeakEvmPerSlotMaximumTrace(self, selectorString, timeout, peakEvmPerSlotMaximum):
        """ FetchPeakEvmPerSlotMaximumTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, peakEvmPerSlotMaximum: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPeakEvmPerSubcarrierMaximumTrace(self, selectorString, timeout, peakEvmPerSubcarrierMaximum):
        """ FetchPeakEvmPerSubcarrierMaximumTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, peakEvmPerSubcarrierMaximum: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPeakEvmPerSymbolMaximumTrace(self, selectorString, timeout, peakEvmPerSymbolMaximum):
        """ FetchPeakEvmPerSymbolMaximumTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, peakEvmPerSymbolMaximum: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPuschDataConstellationTrace(self, selectorString, timeout, puschDataConstellation):
        """ FetchPuschDataConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, puschDataConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPuschDataEvm(self, selectorString, timeout, puschDataRmsEvmMean, puschDataPeakEvmMaximum):
        """ FetchPuschDataEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPuschDemodulatedBits(self, selectorString, timeout, bits):
        """ FetchPuschDemodulatedBits(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, bits: Array[SByte]) -> (int, Array[SByte]) """
        pass

    def FetchPuschDmrsConstellationTrace(self, selectorString, timeout, puschDmrsConstellation):
        """ FetchPuschDmrsConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, puschDmrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPuschDmrsEvm(self, selectorString, timeout, puschDmrsRmsEvmMean, puschDmrsPeakEvmMaximum):
        """ FetchPuschDmrsEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPuschPtrsConstellationTrace(self, selectorString, timeout, puschPtrsConstellation):
        """ FetchPuschPtrsConstellationTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, puschPtrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPuschPtrsEvm(self, selectorString, timeout, puschPtrsRmsEvmMean, puschPtrsPeakEvmMaximum):
        """ FetchPuschPtrsEvm(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPuschSymbolPower(self, selectorString, timeout, puschDataPowerMean, puschDmrsPowerMean, puschPtrsPowerMean):
        """ FetchPuschSymbolPower(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchRmsEvmHighPerSymbolMeanTrace(self, selectorString, timeout, rmsEvmHighPerSymbolMean):
        """ FetchRmsEvmHighPerSymbolMeanTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, rmsEvmHighPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchRmsEvmLowPerSymbolMeanTrace(self, selectorString, timeout, rmsEvmLowPerSymbolMean):
        """ FetchRmsEvmLowPerSymbolMeanTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, rmsEvmLowPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchRmsEvmPerSlotMeanTrace(self, selectorString, timeout, rmsEvmPerSlotMean):
        """ FetchRmsEvmPerSlotMeanTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, rmsEvmPerSlotMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchRmsEvmPerSubcarrierMeanTrace(self, selectorString, timeout, rmsEvmPerSubcarrierMean):
        """ FetchRmsEvmPerSubcarrierMeanTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, rmsEvmPerSubcarrierMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, rmsEvmPerSymbolMean):
        """ FetchRmsEvmPerSymbolMeanTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, rmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSpectralFlatness(self, selectorString, timeout, range1MaximumToRange1Minimum, range2MaximumToRange2Minimum, range1MaximumToRange2Minimum, range2MaximumToRange1Minimum):
        """ FetchSpectralFlatness(self: RFmxNRMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchSpectralFlatnessArray(self, selectorString, timeout, range1MaximumToRange1Minimum, range2MaximumToRange2Minimum, range1MaximumToRange2Minimum, range2MaximumToRange1Minimum):
        """ FetchSpectralFlatnessArray(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, range1MaximumToRange1Minimum: Array[float], range2MaximumToRange2Minimum: Array[float], range1MaximumToRange2Minimum: Array[float], range2MaximumToRange1Minimum: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchSpectralFlatnessTrace(self, selectorString, timeout, spectralFlatness, spectralFlatnessLowerMask, spectralFlatnessUpperMask):
        """ FetchSpectralFlatnessTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, spectralFlatness: Spectrum[Single], spectralFlatnessLowerMask: Spectrum[Single], spectralFlatnessUpperMask: Spectrum[Single]) -> (int, Spectrum[Single], Spectrum[Single], Spectrum[Single]) """
        pass

    def FetchSubblockInBandEmissionTrace(self, selectorString, timeout, SubblockInBandEmission, SubblockInBandEmissionMask, SubblockInBandEmissionRBIndices):
        """ FetchSubblockInBandEmissionTrace(self: RFmxNRMXModAccResults, selectorString: str, timeout: float, SubblockInBandEmission: Array[float], SubblockInBandEmissionMask: Array[float], SubblockInBandEmissionRBIndices: Array[float]) -> (int, Array[float], Array[float], Array[float]) """
        pass

    def GetComponentCarrierFrequencyErrorMean(self, selectorString, value):
        """ GetComponentCarrierFrequencyErrorMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetComponentCarrierIQGainImbalanceMean(self, selectorString, value):
        """ GetComponentCarrierIQGainImbalanceMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetComponentCarrierIQOriginOffsetMean(self, selectorString, value):
        """ GetComponentCarrierIQOriginOffsetMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetComponentCarrierQuadratureErrorMean(self, selectorString, value):
        """ GetComponentCarrierQuadratureErrorMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetComponentCarrierSymbolClockErrorMean(self, selectorString, value):
        """ GetComponentCarrierSymbolClockErrorMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositePeakEvmBwpIndex(self, selectorString, value):
        """ GetCompositePeakEvmBwpIndex(self: RFmxNRMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetCompositePeakEvmMaximum(self, selectorString, value):
        """ GetCompositePeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositePeakEvmSlotIndex(self, selectorString, value):
        """ GetCompositePeakEvmSlotIndex(self: RFmxNRMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetCompositePeakEvmSubcarrierIndex(self, selectorString, value):
        """ GetCompositePeakEvmSubcarrierIndex(self: RFmxNRMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetCompositePeakEvmSymbolIndex(self, selectorString, value):
        """ GetCompositePeakEvmSymbolIndex(self: RFmxNRMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetCompositePeakMagnitudeErrorMaximum(self, selectorString, value):
        """ GetCompositePeakMagnitudeErrorMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositePeakPhaseErrorMaximum(self, selectorString, value):
        """ GetCompositePeakPhaseErrorMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositeRmsEvmMean(self, selectorString, value):
        """ GetCompositeRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositeRmsMagnitudeErrorMean(self, selectorString, value):
        """ GetCompositeRmsMagnitudeErrorMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositeRmsPhaseErrorMean(self, selectorString, value):
        """ GetCompositeRmsPhaseErrorMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetInBandEmissionMargin(self, selectorString, value):
        """ GetInBandEmissionMargin(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdsch16QamRmsEvmMean(self, selectorString, value):
        """ GetPdsch16QamRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdsch256QamRmsEvmMean(self, selectorString, value):
        """ GetPdsch256QamRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdsch64QamRmsEvmMean(self, selectorString, value):
        """ GetPdsch64QamRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschDataPeakEvmMaximum(self, selectorString, value):
        """ GetPdschDataPeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschDataRmsEvmMean(self, selectorString, value):
        """ GetPdschDataRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschDmrsPeakEvmMaximum(self, selectorString, value):
        """ GetPdschDmrsPeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschDmrsRmsEvmMean(self, selectorString, value):
        """ GetPdschDmrsRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschPtrsPeakEvmMaximum(self, selectorString, value):
        """ GetPdschPtrsPeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschPtrsRmsEvmMean(self, selectorString, value):
        """ GetPdschPtrsRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschQpskRmsEvmMean(self, selectorString, value):
        """ GetPdschQpskRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschDataPeakEvmMaximum(self, selectorString, value):
        """ GetPuschDataPeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschDataRmsEvmMean(self, selectorString, value):
        """ GetPuschDataRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschDmrsPeakEvmMaximum(self, selectorString, value):
        """ GetPuschDmrsPeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschDmrsRmsEvmMean(self, selectorString, value):
        """ GetPuschDmrsRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschPtrsPeakEvmMaximum(self, selectorString, value):
        """ GetPuschPtrsPeakEvmMaximum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschPtrsRmsEvmMean(self, selectorString, value):
        """ GetPuschPtrsRmsEvmMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSchDetectedModulationType(self, selectorString, value):
        """ GetSchDetectedModulationType(self: RFmxNRMXModAccResults, selectorString: str) -> (int, RFmxNRMXSchDetectedModulationType) """
        pass

    def GetSchSymbolPowerMean(self, selectorString, value):
        """ GetSchSymbolPowerMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange1MaximumToRange1Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange1MaximumToRange1Minimum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange1MaximumToRange2Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange1MaximumToRange2Minimum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange2MaximumToRange1Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange2MaximumToRange1Minimum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange2MaximumToRange2Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange2MaximumToRange2Minimum(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockInBandEmissionMargin(self, selectorString, value):
        """ GetSubblockInBandEmissionMargin(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockIQOriginOffsetMean(self, selectorString, value):
        """ GetSubblockIQOriginOffsetMean(self: RFmxNRMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockLOComponentCarrierIndex(self, selectorString, value):
        """ GetSubblockLOComponentCarrierIndex(self: RFmxNRMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetSubblockLOSubcarrierIndex(self, selectorString, value):
        """ GetSubblockLOSubcarrierIndex(self: RFmxNRMXModAccResults, selectorString: str) -> (int, int) """
        pass


class RFmxNRMXModAccSpectralFlatnessCondition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccSpectralFlatnessCondition, values: Extreme (1), Normal (0) """
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

    Extreme = None
    Normal = None
    value__ = None


class RFmxNRMXModAccSpectrumInverted(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccSpectrumInverted, values: False (0), True (1) """
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


class RFmxNRMXModAccSynchronizationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModAccSynchronizationMode, values: Frame (5), Slot (1) """
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

    Frame = None
    Slot = None
    value__ = None


class RFmxNRMXModTimingTrackingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXModTimingTrackingEnabled, values: False (0), True (1) """
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


class RFmxNRMXObw(RFmxNRMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxNRMXObw) -> RFmxNRMXObwConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxNRMXObw) -> RFmxNRMXObwResults

"""



class RFmxNRMXObwAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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


class RFmxNRMXObwAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwAveragingEnabled, values: False (0), True (1) """
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


class RFmxNRMXObwAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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


class RFmxNRMXObwConfiguration(RFmxNRMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxNRMXObwConfiguration, selectorString: str, averagingEnabled: RFmxNRMXObwAveragingEnabled, averagingCount: int, averagingType: RFmxNRMXObwAveragingType) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxNRMXObwConfiguration, selectorString: str, rbwAuto: RFmxNRMXObwRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxNRMXObwRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxNRMXObwConfiguration, selectorString: str, sweepTimeAuto: RFmxNRMXObwSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwAveragingType) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwRbwFilterType) """
        pass

    def GetSpan(self, selectorString, value):
        """ GetSpan(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, RFmxNRMXObwSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxNRMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxNRMXObwConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxNRMXObwConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwAveragingType) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxNRMXObwConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxNRMXObwConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxNRMXObwConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwRbwFilterType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxNRMXObwConfiguration, selectorString: str, value: RFmxNRMXObwSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxNRMXObwConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxNRMXObwFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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


class RFmxNRMXObwRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwRbwAutoBandwidth, values: False (0), True (1) """
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


class RFmxNRMXObwRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
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
    value__ = None


class RFmxNRMXObwResults(RFmxNRMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, occupiedBandwidth, absolutePower, startFrequency, stopFrequency):
        """ FetchMeasurement(self: RFmxNRMXObwResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxNRMXObwResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def GetAbsolutePower(self, selectorString, value):
        """ GetAbsolutePower(self: RFmxNRMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetOccupiedBandwidth(self, selectorString, value):
        """ GetOccupiedBandwidth(self: RFmxNRMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetStartFrequency(self, selectorString, value):
        """ GetStartFrequency(self: RFmxNRMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetStopFrequency(self, selectorString, value):
        """ GetStopFrequency(self: RFmxNRMXObwResults, selectorString: str) -> (int, float) """
        pass


class RFmxNRMXObwSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXObwSweepTimeAuto, values: False (0), True (1) """
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


class RFmxNRMXPdschDmrsConfigurationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschDmrsConfigurationType, values: Type1 (0), Type2 (1) """
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

    Type1 = None
    Type2 = None
    value__ = None


class RFmxNRMXPdschDmrsDuration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschDmrsDuration, values: DoubleSymbol (2), SingleSymbol (1) """
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

    DoubleSymbol = None
    SingleSymbol = None
    value__ = None


class RFmxNRMXPdschDmrsPowerMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschDmrsPowerMode, values: CdmGroups (0), UserDefined (1) """
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

    CdmGroups = None
    UserDefined = None
    value__ = None


class RFmxNRMXPdschDmrsScramblingIDMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschDmrsScramblingIDMode, values: CellID (0), UserDefined (1) """
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

    CellID = None
    UserDefined = None
    value__ = None


class RFmxNRMXPdschMappingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschMappingType, values: TypeA (0), TypeB (1) """
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

    TypeA = None
    TypeB = None
    value__ = None


class RFmxNRMXPdschModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschModulationType, values: Qam16 (2), Qam256 (4), Qam64 (3), Qpsk (1) """
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

    Qam16 = None
    Qam256 = None
    Qam64 = None
    Qpsk = None
    value__ = None


class RFmxNRMXPdschPresentInSsbResourceBlock(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschPresentInSsbResourceBlock, values: False (0), True (1) """
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


class RFmxNRMXPdschPtrsEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschPtrsEnabled, values: False (0), True (1) """
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


class RFmxNRMXPdschPtrsPowerMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPdschPtrsPowerMode, values: Standard (0), UserDefined (1) """
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

    Standard = None
    UserDefined = None
    value__ = None


class RFmxNRMXPhaseCompensation(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPhaseCompensation, values: Auto (1), Disabled (0), UserDefined (2) """
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
    UserDefined = None
    value__ = None


class RFmxNRMXPiBy2BpskPowerBoostEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPiBy2BpskPowerBoostEnabled, values: False (0), True (1) """
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


class RFmxNRMXPropertyId(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPropertyId, values: AcpAllTracesEnabled (9441321), AcpAmplitudeCorrectionType (9441320), AcpAveragingCount (9441311), AcpAveragingEnabled (9441310), AcpAveragingType (9441313), AcpComponentCarrierIntegrationBandwidth (9441286), AcpFarIFOutputPowerOffset (9441318), AcpFftWindow (9441314), AcpIFOutputPowerOffsetAuto (9441316), AcpMeasurementEnabled (9441280), AcpMeasurementMethod (9441308), AcpNearIFOutputPowerOffset (9441317), AcpNoiseCompensationEnabled (9441309), AcpNumberOfAnalysisThreads (9441322), AcpNumberOfEndcOffsets (9441347), AcpNumberOfEutraOffsets (9441290), AcpNumberOfNROffsets (9441291), AcpNumberOfUtraOffsets (9441289), AcpOffsetChannelSpacingAdjustment (9441349), AcpOffsetFrequency (9441294), AcpOffsetIntegrationBandwidth (9441298), AcpRbwFilterAutoBandwidth (9441302), AcpRbwFilterBandwidth (9441303), AcpRbwFilterType (9441304), AcpResultsComponentCarrierAbsolutePower (9441331), AcpResultsComponentCarrierRelativePower (9441332), AcpResultsLowerOffsetAbsolutePower (9441338), AcpResultsLowerOffsetRelativePower (9441339), AcpResultsSubblockPower (9441328), AcpResultsTotalAggregatedPower (9441324), AcpResultsUpperOffsetAbsolutePower (9441345), AcpResultsUpperOffsetRelativePower (9441346), AcpSequentialFftSize (9441319), AcpSubblockIntegrationBandwidth (9441282), AcpSweepTimeAuto (9441305), AcpSweepTimeInterval (9441306), AcquisitionBandwidthOptimizationEnabled (9490433), AutoIncrementCellIDEnabled (9437343), AutoResourceBlockDetectionEnabled (9437215), Band (9437202), BandwidthPartCyclicPrefixMode (9437210), BandwidthPartNumberOfResourceBlocks (9437247), BandwidthPartResourceBlockOffset (9437246), BandwidthPartSubcarrierSpacing (9437211), CellID (9437209), CenterFrequency (9437185), ChannelRaster (9437336), ChpAllTracesEnabled (9449491), ChpAmplitudeCorrectionType (9449490), ChpAveragingCount (9449486), ChpAveragingEnabled (9449485), ChpAveragingType (9449488), ChpComponentCarrierIntegrationBandwidth (9449478), ChpFftWindow (9449489), ChpMeasurementEnabled (9449472), ChpNumberOfAnalysisThreads (9449492), ChpRbwFilterAutoBandwidth (9449481), ChpRbwFilterBandwidth (9449482), ChpRbwFilterType (9449483), ChpResultsComponentCarrierAbsolutePower (9449501), ChpResultsComponentCarrierRelativePower (9449503), ChpResultsSubblockPower (9449498), ChpResultsTotalAggregatedPower (9449494), ChpSubblockIntegrationBandwidth (9449477), ChpSweepTimeAuto (9449474), ChpSweepTimeInterval (9449475), ComponentCarrierAtCenterFrequency (9437204), ComponentCarrierBandwidth (9437206), ComponentCarrierFrequency (9437207), ComponentCarrierRadioAccessType (9437442), ComponentCarrierSpacingType (9437203), CoresetCceToRegMappingType (9437453), CoresetInterleaverSize (9437455), CoresetNumberOfResourceBlockClusters (9437449), CoresetNumberOfResourceBlocks (9437451), CoresetNumberOfSymbols (9437448), CoresetPrecodingGranularity (9437452), CoresetRegBundleSize (9437454), CoresetResourceBlockOffset (9437450), CoresetShiftIndex (9437456), CoresetSymbolOffset (9437447), DigitalEdgeTriggerEdge (9437190), DigitalEdgeTriggerSource (9437189), DownlinkChannelConfigurationMode (9437326), DownlinkTestModel (9437440), DownlinkTestModelDuplexScheme (9437441), EpreRatioPort (9437330), ExternalAttenuation (9437187), FrequencyRange (9437237), gNodeBCategory (9437279), GridStart (9437334), IQPowerEdgeTriggerLevel (9437192), IQPowerEdgeTriggerLevelType (9441279), IQPowerEdgeTriggerSlope (9437193), IQPowerEdgeTriggerSource (9437191), LimitedConfigurationChange (9490434), LinkDirection (9437198), ModAccAllTracesEnabled (9453587), ModAccAveragingCount (9453586), ModAccAveragingEnabled (9453585), ModAccChannelEstimationType (9453577), ModAccCommonClockSourceEnabled (9453582), ModAccCompositeResultsIncludeDmrs (9437240), ModAccCompositeResultsIncludePtrs (9437241), ModAccDCSubcarrierRemovalEnabled (9437231), ModAccEvmUnit (9453578), ModAccEvmWithExclusionPeriodEnabled (9453583), ModAccFftWindowLength (9453581), ModAccFftWindowOffset (9453580), ModAccFftWindowType (9453579), ModAccFrequencyErrorEstimation (9453681), ModAccMeasurementEnabled (9453568), ModAccMeasurementLength (9453575), ModAccMeasurementLengthUnit (9453573), ModAccMeasurementOffset (9453574), ModAccMulticarrierFilterEnabled (9453570), ModAccNumberOfAnalysisThreads (9453588), ModAccPhaseTrackingEnabled (9453649), ModAccResultsComponentCarrierFrequencyErrorMean (9453613), ModAccResultsComponentCarrierIQGainImbalanceMean (9453615), ModAccResultsComponentCarrierIQOriginOffsetMean (9453614), ModAccResultsComponentCarrierQuadratureErrorMean (9453616), ModAccResultsComponentCarrierSymbolClockErrorMean (9453619), ModAccResultsCompositePeakEvmBwpIndex (9453652), ModAccResultsCompositePeakEvmMaximum (9453591), ModAccResultsCompositePeakEvmSlotIndex (9453596), ModAccResultsCompositePeakEvmSubcarrierIndex (9453598), ModAccResultsCompositePeakEvmSymbolIndex (9453597), ModAccResultsCompositePeakMagnitudeErrorMaximum (9453593), ModAccResultsCompositePeakPhaseErrorMaximum (9453595), ModAccResultsCompositeRmsEvmMean (9453590), ModAccResultsCompositeRmsMagnitudeErrorMean (9453592), ModAccResultsCompositeRmsPhaseErrorMean (9453594), ModAccResultsInBandEmissionMargin (9453607), ModAccResultsPdsch16QamRmsEvmMean (9453654), ModAccResultsPdsch256QamRmsEvmMean (9453656), ModAccResultsPdsch64QamRmsEvmMean (9453655), ModAccResultsPdschDataPeakEvmMaximum (9453658), ModAccResultsPdschDataRmsEvmMean (9453657), ModAccResultsPdschDmrsPeakEvmMaximum (9453660), ModAccResultsPdschDmrsRmsEvmMean (9453659), ModAccResultsPdschPtrsPeakEvmMaximum (9453662), ModAccResultsPdschPtrsRmsEvmMean (9453661), ModAccResultsPdschQpskRmsEvmMean (9453653), ModAccResultsPuschDataPeakEvmMaximum (9453600), ModAccResultsPuschDataRmsEvmMean (9453599), ModAccResultsPuschDmrsPeakEvmMaximum (9453604), ModAccResultsPuschDmrsRmsEvmMean (9453603), ModAccResultsPuschPtrsPeakEvmMaximum (9453641), ModAccResultsPuschPtrsRmsEvmMean (9453640), ModAccResultsSchDetectedModulationType (9453680), ModAccResultsSchSymbolPowerMean (9453679), ModAccResultsSpectralFlatnessRange1MaximumToRange1Minimum (9453608), ModAccResultsSpectralFlatnessRange1MaximumToRange2Minimum (9453610), ModAccResultsSpectralFlatnessRange2MaximumToRange1Minimum (9453611), ModAccResultsSpectralFlatnessRange2MaximumToRange2Minimum (9453609), ModAccResultsSubblockInBandEmissionMargin (9453612), ModAccResultsSubblockIQOriginOffsetMean (9453622), ModAccResultsSubblockLOComponentCarrierIndex (9453666), ModAccResultsSubblockLOSubcarrierIndex (9453667), ModAccSpectralFlatnessCondition (9453584), ModAccSpectrumInverted (9453576), ModAccSynchronizationMode (9453572), ModAccTimingTrackingEnabled (9453650), NumberOfBandwidthParts (9437245), NumberOfComponentCarriers (9437205), NumberOfCoresets (9437446), NumberOfPdcchConfigurations (9437458), NumberOfPdschConfigurations (9437328), NumberOfPtrsGroups (9437274), NumberOfPuschConfigurations (9437259), NumberOfSubblocks (9437200), NumberOfUsers (9437284), ObwAllTracesEnabled (9461778), ObwAmplitudeCorrectionType (9461777), ObwAveragingCount (9461772), ObwAveragingEnabled (9461771), ObwAveragingType (9461774), ObwFftWindow (9461775), ObwMeasurementEnabled (9461760), ObwNumberOfAnalysisThreads (9461779), ObwRbwFilterAutoBandwidth (9461766), ObwRbwFilterBandwidth (9461767), ObwRbwFilterType (9461768), ObwResultsAbsolutePower (9461782), ObwResultsOccupiedBandwidth (9461781), ObwResultsStartFrequency (9461783), ObwResultsStopFrequency (9461784), ObwSpan (9461763), ObwSweepTimeAuto (9461769), ObwSweepTimeInterval (9461770), PbchDmrsPower (9437321), PbchPower (9437320), PdcchCceAggregationLevel (9437459), PdcchCceOffset (9437460), PdcchSlotAllocation (9437461), PdschDmrsAdditionalPositions (9437304), PdschDmrsAntennaPorts (9437291), PdschDmrsConfigurationType (9437300), PdschDmrsDuration (9437303), PdschDmrsnScid (9437297), PdschDmrsNumberOfCdmGroups (9437294), PdschDmrsPower (9437293), PdschDmrsPowerMode (9437292), PdschDmrsScramblingID (9437296), PdschDmrsScramblingIDMode (9437295), PdschDmrsTypeAPosition (9437302), PdschMappingType (9437301), PdschModulationType (9437290), PdschNumberOfResourceBlockClusters (9437287), PdschNumberOfResourceBlocks (9437289), PdschPresentInSsbResourceBlock (9437335), PdschPtrsAntennaPorts (9437306), PdschPtrsEnabled (9437305), PdschPtrsFrequencyDensity (9437310), PdschPtrsPower (9437308), PdschPtrsPowerMode (9437307), PdschPtrsREOffset (9437311), PdschPtrsTimeDensity (9437309), PdschResourceBlockOffset (9437288), PdschSlotAllocation (9437312), PdschSymbolAllocation (9437313), PhaseCompensation (9438269), PhaseCompensationFrequency (9437281), PiBy2BpskPowerBoostEnabled (9437342), PowerClass (9437340), PssPower (9437318), PuschDmrsAdditionalPositions (9437234), PuschDmrsAntennaPorts (9437249), PuschDmrsConfigurationType (9437233), PuschDmrsDuration (9437235), PuschDmrsGroupHoppingEnabled (9437217), PuschDmrsNscid (9437254), PuschDmrsNumberOfCdmGroups (9437250), PuschDmrsPower (9437232), PuschDmrsPowerMode (9437265), PuschDmrsPuschID (9437256), PuschDmrsPuschIDMode (9437255), PuschDmrsScramblingID (9437253), PuschDmrsScramblingIDMode (9437252), PuschDmrsSequenceHoppingEnabled (9437218), PuschDmrsTypeAPosition (9437258), PuschMappingType (9437236), PuschModulationType (9437222), PuschNumberOfResourceBlockClusters (9437223), PuschNumberOfResourceBlocks (9437225), PuschPtrsAntennaPorts (9437270), PuschPtrsEnabled (9437269), PuschPtrsFrequencyDensity (9437277), PuschPtrsPower (9437272), PuschPtrsPowerMode (9437271), PuschPtrsREOffset (9437278), PuschPtrsTimeDensity (9437276), PuschResourceBlockOffset (9437224), PuschSlotAllocation (9437260), PuschSymbolAllocation (9437261), PuschTransformPrecodingEnabled (9437214), PvtAllTracesEnabled (9474057), PvtAveragingCount (9474052), PvtAveragingEnabled (9474051), PvtAveragingType (9474053), PvtMeasurementEnabled (9474048), PvtMeasurementMethod (9474050), PvtNumberOfAnalysisThreads (9474059), PvtOffPowerExclusionAfter (9474056), PvtOffPowerExclusionBefore (9474055), PvtResultsAbsoluteOffPowerAfter (9474062), PvtResultsAbsoluteOffPowerBefore (9474061), PvtResultsAbsoluteONPower (9474063), PvtResultsBurstWidth (9474064), PvtResultsMeasurementStatus (9474060), ReferenceGridAlignmentMode (9437239), ReferenceGridStart (9437283), ReferenceGridSubcarrierSpacing (9437282), ReferenceLevel (9437186), ReferenceLevelHeadroom (9441276), ResultFetchTimeout (9486336), Rnti (9437285), SamplesPerPtrsGroup (9437275), SelectedPorts (9441277), SemAllTracesEnabled (9469976), SemAmplitudeCorrectionType (9469975), SemAveragingCount (9469973), SemAveragingEnabled (9469972), SemAveragingType (9469974), SemComponentCarrierIntegrationBandwidth (9469957), SemComponentCarrierRatedOutputPower (9470010), SemDeltaFMaximum (9470009), SemDownlinkMaskType (9470008), SemFftWindow (9470016), SemMeasurementEnabled (9469952), SemNumberOfAnalysisThreads (9469977), SemNumberOfOffsets (9469958), SemOffsetAbsoluteLimitStart (9469966), SemOffsetAbsoluteLimitStop (9469967), SemOffsetBandwidthIntegral (9469964), SemOffsetLimitFailMask (9469965), SemOffsetRbwFilterBandwidth (9469962), SemOffsetRbwFilterType (9469963), SemOffsetRelativeLimitStart (9469968), SemOffsetRelativeLimitStop (9469969), SemOffsetSideband (9469961), SemOffsetStartFrequency (9469959), SemOffsetStopFrequency (9469960), SemResultsComponentCarrierAbsoluteIntegratedPower (9469984), SemResultsComponentCarrierAbsolutePeakPower (9469986), SemResultsComponentCarrierPeakFrequency (9469987), SemResultsComponentCarrierRelativeIntegratedPower (9469985), SemResultsLowerOffsetAbsoluteIntegratedPower (9469989), SemResultsLowerOffsetAbsolutePeakPower (9469991), SemResultsLowerOffsetMargin (9469994), SemResultsLowerOffsetMarginAbsolutePower (9469995), SemResultsLowerOffsetMarginFrequency (9469997), SemResultsLowerOffsetMarginRelativePower (9469996), SemResultsLowerOffsetMeasurementStatus (9469988), SemResultsLowerOffsetPeakFrequency (9469993), SemResultsLowerOffsetRelativeIntegratedPower (9469990), SemResultsLowerOffsetRelativePeakPower (9469992), SemResultsMeasurementStatus (9469980), SemResultsSubblockPower (9469983), SemResultsTotalAggregatedPower (9469979), SemResultsUpperOffsetAbsoluteIntegratedPower (9469999), SemResultsUpperOffsetAbsolutePeakPower (9470001), SemResultsUpperOffsetMargin (9470004), SemResultsUpperOffsetMarginAbsolutePower (9470005), SemResultsUpperOffsetMarginFrequency (9470007), SemResultsUpperOffsetMarginRelativePower (9470006), SemResultsUpperOffsetMeasurementStatus (9469998), SemResultsUpperOffsetPeakFrequency (9470003), SemResultsUpperOffsetRelativeIntegratedPower (9470000), SemResultsUpperOffsetRelativePeakPower (9470002), SemSubblockAggregatedChannelBandwidth (9469956), SemSubblockIntegrationBandwidth (9469955), SemSweepTimeAuto (9469970), SemSweepTimeInterval (9469971), SemUplinkMaskType (9469954), SsbActiveBlocks (9437333), SsbCrbOffset (9437315), SsbEnabled (9437314), SsbPattern (9437317), SsbPeriodicity (9437332), SsbSubcarrierOffset (9437316), SssPower (9437319), SubblockEndcNominalSpacingAdjustment (9437443), SubblockFrequencyDefinition (9437201), SubblockTransmitLOFrequency (9437280), SubcarrierSpacingCommon (9437337), TransmitAntennaToAnalyze (9437339), TransmitterArchitecture (9438267), TriggerDelay (9437194), TriggerMinimumQuietTimeDuration (9437196), TriggerMinimumQuietTimeMode (9437195), TriggerType (9437188) """
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
    AcpComponentCarrierIntegrationBandwidth = None
    AcpFarIFOutputPowerOffset = None
    AcpFftWindow = None
    AcpIFOutputPowerOffsetAuto = None
    AcpMeasurementEnabled = None
    AcpMeasurementMethod = None
    AcpNearIFOutputPowerOffset = None
    AcpNoiseCompensationEnabled = None
    AcpNumberOfAnalysisThreads = None
    AcpNumberOfEndcOffsets = None
    AcpNumberOfEutraOffsets = None
    AcpNumberOfNROffsets = None
    AcpNumberOfUtraOffsets = None
    AcpOffsetChannelSpacingAdjustment = None
    AcpOffsetFrequency = None
    AcpOffsetIntegrationBandwidth = None
    AcpRbwFilterAutoBandwidth = None
    AcpRbwFilterBandwidth = None
    AcpRbwFilterType = None
    AcpResultsComponentCarrierAbsolutePower = None
    AcpResultsComponentCarrierRelativePower = None
    AcpResultsLowerOffsetAbsolutePower = None
    AcpResultsLowerOffsetRelativePower = None
    AcpResultsSubblockPower = None
    AcpResultsTotalAggregatedPower = None
    AcpResultsUpperOffsetAbsolutePower = None
    AcpResultsUpperOffsetRelativePower = None
    AcpSequentialFftSize = None
    AcpSubblockIntegrationBandwidth = None
    AcpSweepTimeAuto = None
    AcpSweepTimeInterval = None
    AcquisitionBandwidthOptimizationEnabled = None
    AutoIncrementCellIDEnabled = None
    AutoResourceBlockDetectionEnabled = None
    Band = None
    BandwidthPartCyclicPrefixMode = None
    BandwidthPartNumberOfResourceBlocks = None
    BandwidthPartResourceBlockOffset = None
    BandwidthPartSubcarrierSpacing = None
    CellID = None
    CenterFrequency = None
    ChannelRaster = None
    ChpAllTracesEnabled = None
    ChpAmplitudeCorrectionType = None
    ChpAveragingCount = None
    ChpAveragingEnabled = None
    ChpAveragingType = None
    ChpComponentCarrierIntegrationBandwidth = None
    ChpFftWindow = None
    ChpMeasurementEnabled = None
    ChpNumberOfAnalysisThreads = None
    ChpRbwFilterAutoBandwidth = None
    ChpRbwFilterBandwidth = None
    ChpRbwFilterType = None
    ChpResultsComponentCarrierAbsolutePower = None
    ChpResultsComponentCarrierRelativePower = None
    ChpResultsSubblockPower = None
    ChpResultsTotalAggregatedPower = None
    ChpSubblockIntegrationBandwidth = None
    ChpSweepTimeAuto = None
    ChpSweepTimeInterval = None
    ComponentCarrierAtCenterFrequency = None
    ComponentCarrierBandwidth = None
    ComponentCarrierFrequency = None
    ComponentCarrierRadioAccessType = None
    ComponentCarrierSpacingType = None
    CoresetCceToRegMappingType = None
    CoresetInterleaverSize = None
    CoresetNumberOfResourceBlockClusters = None
    CoresetNumberOfResourceBlocks = None
    CoresetNumberOfSymbols = None
    CoresetPrecodingGranularity = None
    CoresetRegBundleSize = None
    CoresetResourceBlockOffset = None
    CoresetShiftIndex = None
    CoresetSymbolOffset = None
    DigitalEdgeTriggerEdge = None
    DigitalEdgeTriggerSource = None
    DownlinkChannelConfigurationMode = None
    DownlinkTestModel = None
    DownlinkTestModelDuplexScheme = None
    EpreRatioPort = None
    ExternalAttenuation = None
    FrequencyRange = None
    gNodeBCategory = None
    GridStart = None
    IQPowerEdgeTriggerLevel = None
    IQPowerEdgeTriggerLevelType = None
    IQPowerEdgeTriggerSlope = None
    IQPowerEdgeTriggerSource = None
    LimitedConfigurationChange = None
    LinkDirection = None
    ModAccAllTracesEnabled = None
    ModAccAveragingCount = None
    ModAccAveragingEnabled = None
    ModAccChannelEstimationType = None
    ModAccCommonClockSourceEnabled = None
    ModAccCompositeResultsIncludeDmrs = None
    ModAccCompositeResultsIncludePtrs = None
    ModAccDCSubcarrierRemovalEnabled = None
    ModAccEvmUnit = None
    ModAccEvmWithExclusionPeriodEnabled = None
    ModAccFftWindowLength = None
    ModAccFftWindowOffset = None
    ModAccFftWindowType = None
    ModAccFrequencyErrorEstimation = None
    ModAccMeasurementEnabled = None
    ModAccMeasurementLength = None
    ModAccMeasurementLengthUnit = None
    ModAccMeasurementOffset = None
    ModAccMulticarrierFilterEnabled = None
    ModAccNumberOfAnalysisThreads = None
    ModAccPhaseTrackingEnabled = None
    ModAccResultsComponentCarrierFrequencyErrorMean = None
    ModAccResultsComponentCarrierIQGainImbalanceMean = None
    ModAccResultsComponentCarrierIQOriginOffsetMean = None
    ModAccResultsComponentCarrierQuadratureErrorMean = None
    ModAccResultsComponentCarrierSymbolClockErrorMean = None
    ModAccResultsCompositePeakEvmBwpIndex = None
    ModAccResultsCompositePeakEvmMaximum = None
    ModAccResultsCompositePeakEvmSlotIndex = None
    ModAccResultsCompositePeakEvmSubcarrierIndex = None
    ModAccResultsCompositePeakEvmSymbolIndex = None
    ModAccResultsCompositePeakMagnitudeErrorMaximum = None
    ModAccResultsCompositePeakPhaseErrorMaximum = None
    ModAccResultsCompositeRmsEvmMean = None
    ModAccResultsCompositeRmsMagnitudeErrorMean = None
    ModAccResultsCompositeRmsPhaseErrorMean = None
    ModAccResultsInBandEmissionMargin = None
    ModAccResultsPdsch16QamRmsEvmMean = None
    ModAccResultsPdsch256QamRmsEvmMean = None
    ModAccResultsPdsch64QamRmsEvmMean = None
    ModAccResultsPdschDataPeakEvmMaximum = None
    ModAccResultsPdschDataRmsEvmMean = None
    ModAccResultsPdschDmrsPeakEvmMaximum = None
    ModAccResultsPdschDmrsRmsEvmMean = None
    ModAccResultsPdschPtrsPeakEvmMaximum = None
    ModAccResultsPdschPtrsRmsEvmMean = None
    ModAccResultsPdschQpskRmsEvmMean = None
    ModAccResultsPuschDataPeakEvmMaximum = None
    ModAccResultsPuschDataRmsEvmMean = None
    ModAccResultsPuschDmrsPeakEvmMaximum = None
    ModAccResultsPuschDmrsRmsEvmMean = None
    ModAccResultsPuschPtrsPeakEvmMaximum = None
    ModAccResultsPuschPtrsRmsEvmMean = None
    ModAccResultsSchDetectedModulationType = None
    ModAccResultsSchSymbolPowerMean = None
    ModAccResultsSpectralFlatnessRange1MaximumToRange1Minimum = None
    ModAccResultsSpectralFlatnessRange1MaximumToRange2Minimum = None
    ModAccResultsSpectralFlatnessRange2MaximumToRange1Minimum = None
    ModAccResultsSpectralFlatnessRange2MaximumToRange2Minimum = None
    ModAccResultsSubblockInBandEmissionMargin = None
    ModAccResultsSubblockIQOriginOffsetMean = None
    ModAccResultsSubblockLOComponentCarrierIndex = None
    ModAccResultsSubblockLOSubcarrierIndex = None
    ModAccSpectralFlatnessCondition = None
    ModAccSpectrumInverted = None
    ModAccSynchronizationMode = None
    ModAccTimingTrackingEnabled = None
    NumberOfBandwidthParts = None
    NumberOfComponentCarriers = None
    NumberOfCoresets = None
    NumberOfPdcchConfigurations = None
    NumberOfPdschConfigurations = None
    NumberOfPtrsGroups = None
    NumberOfPuschConfigurations = None
    NumberOfSubblocks = None
    NumberOfUsers = None
    ObwAllTracesEnabled = None
    ObwAmplitudeCorrectionType = None
    ObwAveragingCount = None
    ObwAveragingEnabled = None
    ObwAveragingType = None
    ObwFftWindow = None
    ObwMeasurementEnabled = None
    ObwNumberOfAnalysisThreads = None
    ObwRbwFilterAutoBandwidth = None
    ObwRbwFilterBandwidth = None
    ObwRbwFilterType = None
    ObwResultsAbsolutePower = None
    ObwResultsOccupiedBandwidth = None
    ObwResultsStartFrequency = None
    ObwResultsStopFrequency = None
    ObwSpan = None
    ObwSweepTimeAuto = None
    ObwSweepTimeInterval = None
    PbchDmrsPower = None
    PbchPower = None
    PdcchCceAggregationLevel = None
    PdcchCceOffset = None
    PdcchSlotAllocation = None
    PdschDmrsAdditionalPositions = None
    PdschDmrsAntennaPorts = None
    PdschDmrsConfigurationType = None
    PdschDmrsDuration = None
    PdschDmrsnScid = None
    PdschDmrsNumberOfCdmGroups = None
    PdschDmrsPower = None
    PdschDmrsPowerMode = None
    PdschDmrsScramblingID = None
    PdschDmrsScramblingIDMode = None
    PdschDmrsTypeAPosition = None
    PdschMappingType = None
    PdschModulationType = None
    PdschNumberOfResourceBlockClusters = None
    PdschNumberOfResourceBlocks = None
    PdschPresentInSsbResourceBlock = None
    PdschPtrsAntennaPorts = None
    PdschPtrsEnabled = None
    PdschPtrsFrequencyDensity = None
    PdschPtrsPower = None
    PdschPtrsPowerMode = None
    PdschPtrsREOffset = None
    PdschPtrsTimeDensity = None
    PdschResourceBlockOffset = None
    PdschSlotAllocation = None
    PdschSymbolAllocation = None
    PhaseCompensation = None
    PhaseCompensationFrequency = None
    PiBy2BpskPowerBoostEnabled = None
    PowerClass = None
    PssPower = None
    PuschDmrsAdditionalPositions = None
    PuschDmrsAntennaPorts = None
    PuschDmrsConfigurationType = None
    PuschDmrsDuration = None
    PuschDmrsGroupHoppingEnabled = None
    PuschDmrsNscid = None
    PuschDmrsNumberOfCdmGroups = None
    PuschDmrsPower = None
    PuschDmrsPowerMode = None
    PuschDmrsPuschID = None
    PuschDmrsPuschIDMode = None
    PuschDmrsScramblingID = None
    PuschDmrsScramblingIDMode = None
    PuschDmrsSequenceHoppingEnabled = None
    PuschDmrsTypeAPosition = None
    PuschMappingType = None
    PuschModulationType = None
    PuschNumberOfResourceBlockClusters = None
    PuschNumberOfResourceBlocks = None
    PuschPtrsAntennaPorts = None
    PuschPtrsEnabled = None
    PuschPtrsFrequencyDensity = None
    PuschPtrsPower = None
    PuschPtrsPowerMode = None
    PuschPtrsREOffset = None
    PuschPtrsTimeDensity = None
    PuschResourceBlockOffset = None
    PuschSlotAllocation = None
    PuschSymbolAllocation = None
    PuschTransformPrecodingEnabled = None
    PvtAllTracesEnabled = None
    PvtAveragingCount = None
    PvtAveragingEnabled = None
    PvtAveragingType = None
    PvtMeasurementEnabled = None
    PvtMeasurementMethod = None
    PvtNumberOfAnalysisThreads = None
    PvtOffPowerExclusionAfter = None
    PvtOffPowerExclusionBefore = None
    PvtResultsAbsoluteOffPowerAfter = None
    PvtResultsAbsoluteOffPowerBefore = None
    PvtResultsAbsoluteONPower = None
    PvtResultsBurstWidth = None
    PvtResultsMeasurementStatus = None
    ReferenceGridAlignmentMode = None
    ReferenceGridStart = None
    ReferenceGridSubcarrierSpacing = None
    ReferenceLevel = None
    ReferenceLevelHeadroom = None
    ResultFetchTimeout = None
    Rnti = None
    SamplesPerPtrsGroup = None
    SelectedPorts = None
    SemAllTracesEnabled = None
    SemAmplitudeCorrectionType = None
    SemAveragingCount = None
    SemAveragingEnabled = None
    SemAveragingType = None
    SemComponentCarrierIntegrationBandwidth = None
    SemComponentCarrierRatedOutputPower = None
    SemDeltaFMaximum = None
    SemDownlinkMaskType = None
    SemFftWindow = None
    SemMeasurementEnabled = None
    SemNumberOfAnalysisThreads = None
    SemNumberOfOffsets = None
    SemOffsetAbsoluteLimitStart = None
    SemOffsetAbsoluteLimitStop = None
    SemOffsetBandwidthIntegral = None
    SemOffsetLimitFailMask = None
    SemOffsetRbwFilterBandwidth = None
    SemOffsetRbwFilterType = None
    SemOffsetRelativeLimitStart = None
    SemOffsetRelativeLimitStop = None
    SemOffsetSideband = None
    SemOffsetStartFrequency = None
    SemOffsetStopFrequency = None
    SemResultsComponentCarrierAbsoluteIntegratedPower = None
    SemResultsComponentCarrierAbsolutePeakPower = None
    SemResultsComponentCarrierPeakFrequency = None
    SemResultsComponentCarrierRelativeIntegratedPower = None
    SemResultsLowerOffsetAbsoluteIntegratedPower = None
    SemResultsLowerOffsetAbsolutePeakPower = None
    SemResultsLowerOffsetMargin = None
    SemResultsLowerOffsetMarginAbsolutePower = None
    SemResultsLowerOffsetMarginFrequency = None
    SemResultsLowerOffsetMarginRelativePower = None
    SemResultsLowerOffsetMeasurementStatus = None
    SemResultsLowerOffsetPeakFrequency = None
    SemResultsLowerOffsetRelativeIntegratedPower = None
    SemResultsLowerOffsetRelativePeakPower = None
    SemResultsMeasurementStatus = None
    SemResultsSubblockPower = None
    SemResultsTotalAggregatedPower = None
    SemResultsUpperOffsetAbsoluteIntegratedPower = None
    SemResultsUpperOffsetAbsolutePeakPower = None
    SemResultsUpperOffsetMargin = None
    SemResultsUpperOffsetMarginAbsolutePower = None
    SemResultsUpperOffsetMarginFrequency = None
    SemResultsUpperOffsetMarginRelativePower = None
    SemResultsUpperOffsetMeasurementStatus = None
    SemResultsUpperOffsetPeakFrequency = None
    SemResultsUpperOffsetRelativeIntegratedPower = None
    SemResultsUpperOffsetRelativePeakPower = None
    SemSubblockAggregatedChannelBandwidth = None
    SemSubblockIntegrationBandwidth = None
    SemSweepTimeAuto = None
    SemSweepTimeInterval = None
    SemUplinkMaskType = None
    SsbActiveBlocks = None
    SsbCrbOffset = None
    SsbEnabled = None
    SsbPattern = None
    SsbPeriodicity = None
    SsbSubcarrierOffset = None
    SssPower = None
    SubblockEndcNominalSpacingAdjustment = None
    SubblockFrequencyDefinition = None
    SubblockTransmitLOFrequency = None
    SubcarrierSpacingCommon = None
    TransmitAntennaToAnalyze = None
    TransmitterArchitecture = None
    TriggerDelay = None
    TriggerMinimumQuietTimeDuration = None
    TriggerMinimumQuietTimeMode = None
    TriggerType = None
    value__ = None


class RFmxNRMXPuschDmrsConfigurationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsConfigurationType, values: Type1 (0), Type2 (1) """
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

    Type1 = None
    Type2 = None
    value__ = None


class RFmxNRMXPuschDmrsDuration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsDuration, values: DoubleSymbol (2), SingleSymbol (1) """
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

    DoubleSymbol = None
    SingleSymbol = None
    value__ = None


class RFmxNRMXPuschDmrsGroupHoppingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsGroupHoppingEnabled, values: False (0), True (1) """
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


class RFmxNRMXPuschDmrsPowerMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsPowerMode, values: CdmGroups (0), UserDefined (1) """
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

    CdmGroups = None
    UserDefined = None
    value__ = None


class RFmxNRMXPuschDmrsPuschIDMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsPuschIDMode, values: CellID (0), UserDefined (1) """
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

    CellID = None
    UserDefined = None
    value__ = None


class RFmxNRMXPuschDmrsScramblingIDMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsScramblingIDMode, values: CellID (0), UserDefined (1) """
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

    CellID = None
    UserDefined = None
    value__ = None


class RFmxNRMXPuschDmrsSequenceHoppingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschDmrsSequenceHoppingEnabled, values: False (0), True (1) """
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


class RFmxNRMXPuschMappingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschMappingType, values: TypeA (0), TypeB (1) """
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

    TypeA = None
    TypeB = None
    value__ = None


class RFmxNRMXPuschModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschModulationType, values: PiBy2_Bpsk (0), Qam16 (2), Qam256 (4), Qam64 (3), Qpsk (1) """
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

    PiBy2_Bpsk = None
    Qam16 = None
    Qam256 = None
    Qam64 = None
    Qpsk = None
    value__ = None


class RFmxNRMXPuschPtrsEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschPtrsEnabled, values: False (0), True (1) """
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


class RFmxNRMXPuschPtrsPowerMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschPtrsPowerMode, values: Standard (0), UserDefined (1) """
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

    Standard = None
    UserDefined = None
    value__ = None


class RFmxNRMXPuschTransformPrecodingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPuschTransformPrecodingEnabled, values: False (0), True (1) """
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


class RFmxNRMXPvt(RFmxNRMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxNRMXPvt) -> RFmxNRMXPvtConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxNRMXPvt) -> RFmxNRMXPvtResults

"""



class RFmxNRMXPvtAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPvtAveragingEnabled, values: False (0), True (1) """
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


class RFmxNRMXPvtAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPvtAveragingType, values: Log (1), Rms (0) """
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
    Rms = None
    value__ = None


class RFmxNRMXPvtConfiguration(RFmxNRMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxNRMXPvtConfiguration, selectorString: str, averagingEnabled: RFmxNRMXPvtAveragingEnabled, averagingCount: int, averagingType: RFmxNRMXPvtAveragingType) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxNRMXPvtConfiguration, selectorString: str, measurementMethod: RFmxNRMXPvtMeasurementMethod) -> int """
        pass

    def ConfigureOffPowerExclusionPeriods(self, selectorString, offPowerExclusionBefore, offPowerExclusionAfter):
        """ ConfigureOffPowerExclusionPeriods(self: RFmxNRMXPvtConfiguration, selectorString: str, offPowerExclusionBefore: float, offPowerExclusionAfter: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, RFmxNRMXPvtAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, RFmxNRMXPvtAveragingType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, RFmxNRMXPvtMeasurementMethod) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffPowerExclusionAfter(self, selectorString, value):
        """ GetOffPowerExclusionAfter(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffPowerExclusionBefore(self, selectorString, value):
        """ GetOffPowerExclusionBefore(self: RFmxNRMXPvtConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxNRMXPvtConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxNRMXPvtConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxNRMXPvtConfiguration, selectorString: str, value: RFmxNRMXPvtAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxNRMXPvtConfiguration, selectorString: str, value: RFmxNRMXPvtAveragingType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxNRMXPvtConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxNRMXPvtConfiguration, selectorString: str, value: RFmxNRMXPvtMeasurementMethod) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxNRMXPvtConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffPowerExclusionAfter(self, selectorString, value):
        """ SetOffPowerExclusionAfter(self: RFmxNRMXPvtConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffPowerExclusionBefore(self, selectorString, value):
        """ SetOffPowerExclusionBefore(self: RFmxNRMXPvtConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxNRMXPvtMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPvtMeasurementMethod, values: DynamicRange (1), Normal (0) """
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
    value__ = None


class RFmxNRMXPvtMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXPvtMeasurementStatus, values: Fail (0), Pass (1) """
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


class RFmxNRMXPvtResults(RFmxNRMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, measurementStatus, absoluteOffPowerBefore, absoluteOffPowerAfter, absoluteONPower, burstWidth):
        """ FetchMeasurement(self: RFmxNRMXPvtResults, selectorString: str, timeout: float) -> (int, RFmxNRMXPvtMeasurementStatus, float, float, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, measurementStatus, absoluteOffPowerBefore, absoluteOffPowerAfter, absoluteONPower, burstWidth):
        """ FetchMeasurementArray(self: RFmxNRMXPvtResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxNRMXPvtMeasurementStatus], absoluteOffPowerBefore: Array[float], absoluteOffPowerAfter: Array[float], absoluteONPower: Array[float], burstWidth: Array[float]) -> (int, Array[RFmxNRMXPvtMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchSignalPowerTrace(self, selectorString, timeout, signalPower, absoluteLimit):
        """ FetchSignalPowerTrace(self: RFmxNRMXPvtResults, selectorString: str, timeout: float, signalPower: AnalogWaveform[Single], absoluteLimit: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def GetAbsoluteOffPowerAfter(self, selectorString, value):
        """ GetAbsoluteOffPowerAfter(self: RFmxNRMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetAbsoluteOffPowerBefore(self, selectorString, value):
        """ GetAbsoluteOffPowerBefore(self: RFmxNRMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetAbsoluteONPower(self, selectorString, value):
        """ GetAbsoluteONPower(self: RFmxNRMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetBurstWidth(self, selectorString, value):
        """ GetBurstWidth(self: RFmxNRMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementStatus(self, selectorString, value):
        """ GetMeasurementStatus(self: RFmxNRMXPvtResults, selectorString: str) -> (int, RFmxNRMXPvtMeasurementStatus) """
        pass


class RFmxNRMXReferenceGridAlignmentMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXReferenceGridAlignmentMode, values: Auto (1), Manual (0) """
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


class RFmxNRMXReferenceLevelUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXReferenceLevelUnits, values: dBm (0), dBmV (4), dBuV (5), dBV (3), dBW (2), Volts (7), VoltsSquared (8), Watts (6) """
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
    Watts = None


class RFmxNRMXSchDetectedModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSchDetectedModulationType, values: PiBy2_Bpsk (0), Qam16 (2), Qam256 (4), Qam64 (3), Qpsk (1) """
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

    PiBy2_Bpsk = None
    Qam16 = None
    Qam256 = None
    Qam64 = None
    Qpsk = None
    value__ = None


class RFmxNRMXSem(RFmxNRMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxNRMXSem) -> RFmxNRMXSemConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxNRMXSem) -> RFmxNRMXSemResults

"""



class RFmxNRMXSemAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
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


class RFmxNRMXSemAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemAveragingEnabled, values: False (0), True (1) """
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


class RFmxNRMXSemAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
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


class RFmxNRMXSemComponentCarrierConfiguration(RFmxNRMXSubObject):
    # no doc
    def ConfigureRatedOutputPower(self, selectorString, componentCarrierRatedOutputPower):
        """ ConfigureRatedOutputPower(self: RFmxNRMXSemComponentCarrierConfiguration, selectorString: str, componentCarrierRatedOutputPower: float) -> int """
        pass

    def ConfigureRatedOutputPowerArray(self, selectorString, componentCarrierRatedOutputPower):
        """ ConfigureRatedOutputPowerArray(self: RFmxNRMXSemComponentCarrierConfiguration, selectorString: str, componentCarrierRatedOutputPower: Array[float]) -> int """
        pass

    def GetIntegrationBandwidth(self, selectorString, value):
        """ GetIntegrationBandwidth(self: RFmxNRMXSemComponentCarrierConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRatedOutputPower(self, selectorString, value):
        """ GetRatedOutputPower(self: RFmxNRMXSemComponentCarrierConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetRatedOutputPower(self, selectorString, value):
        """ SetRatedOutputPower(self: RFmxNRMXSemComponentCarrierConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxNRMXSemComponentCarrierResults(RFmxNRMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, relativePower):
        """ FetchMeasurement(self: RFmxNRMXSemComponentCarrierResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, absolutePower, peakAbsolutePower, peakFrequency, relativePower):
        """ FetchMeasurementArray(self: RFmxNRMXSemComponentCarrierResults, selectorString: str, timeout: float, absolutePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], relativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetAbsoluteIntegratedPower(self: RFmxNRMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetAbsolutePeakPower(self, selectorString, value):
        """ GetAbsolutePeakPower(self: RFmxNRMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakFrequency(self, selectorString, value):
        """ GetPeakFrequency(self: RFmxNRMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetRelativeIntegratedPower(self, selectorString, value):
        """ GetRelativeIntegratedPower(self: RFmxNRMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass


class RFmxNRMXSemConfiguration(RFmxNRMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxNRMXSemConfiguration, selectorString: str, averagingEnabled: RFmxNRMXSemAveragingEnabled, averagingCount: int, averagingType: RFmxNRMXSemAveragingType) -> int """
        pass

    def ConfigureNumberOfOffsets(self, selectorString, numberOfOffsets):
        """ ConfigureNumberOfOffsets(self: RFmxNRMXSemConfiguration, selectorString: str, numberOfOffsets: int) -> int """
        pass

    def ConfigureOffsetAbsoluteLimit(self, selectorString, absoluteLimitStart, absoluteLimitStop):
        """ ConfigureOffsetAbsoluteLimit(self: RFmxNRMXSemConfiguration, selectorString: str, absoluteLimitStart: float, absoluteLimitStop: float) -> int """
        pass

    def ConfigureOffsetAbsoluteLimitArray(self, selectorString, absoluteLimitStart, absoluteLimitStop):
        """ ConfigureOffsetAbsoluteLimitArray(self: RFmxNRMXSemConfiguration, selectorString: str, absoluteLimitStart: Array[float], absoluteLimitStop: Array[float]) -> int """
        pass

    def ConfigureOffsetBandwidthIntegral(self, selectorString, bandwidthIntegral):
        """ ConfigureOffsetBandwidthIntegral(self: RFmxNRMXSemConfiguration, selectorString: str, bandwidthIntegral: int) -> int """
        pass

    def ConfigureOffsetBandwidthIntegralArray(self, selectorString, bandwidthIntegral):
        """ ConfigureOffsetBandwidthIntegralArray(self: RFmxNRMXSemConfiguration, selectorString: str, bandwidthIntegral: Array[int]) -> int """
        pass

    def ConfigureOffsetFrequency(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband):
        """ ConfigureOffsetFrequency(self: RFmxNRMXSemConfiguration, selectorString: str, offsetStartFrequency: float, offsetStopFrequency: float, offsetSideband: RFmxNRMXSemOffsetSideband) -> int """
        pass

    def ConfigureOffsetFrequencyArray(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband):
        """ ConfigureOffsetFrequencyArray(self: RFmxNRMXSemConfiguration, selectorString: str, offsetStartFrequency: Array[float], offsetStopFrequency: Array[float], offsetSideband: Array[RFmxNRMXSemOffsetSideband]) -> int """
        pass

    def ConfigureOffsetLimitFailMask(self, selectorString, limitFailMask):
        """ ConfigureOffsetLimitFailMask(self: RFmxNRMXSemConfiguration, selectorString: str, limitFailMask: RFmxNRMXSemOffsetLimitFailMask) -> int """
        pass

    def ConfigureOffsetLimitFailMaskArray(self, selectorString, limitFailMask):
        """ ConfigureOffsetLimitFailMaskArray(self: RFmxNRMXSemConfiguration, selectorString: str, limitFailMask: Array[RFmxNRMXSemOffsetLimitFailMask]) -> int """
        pass

    def ConfigureOffsetRbwFilter(self, selectorString, offsetRbw, offsetRbwFilterType):
        """ ConfigureOffsetRbwFilter(self: RFmxNRMXSemConfiguration, selectorString: str, offsetRbw: float, offsetRbwFilterType: RFmxNRMXSemOffsetRbwFilterType) -> int """
        pass

    def ConfigureOffsetRbwFilterArray(self, selectorString, offsetRbw, offsetRbwFilterType):
        """ ConfigureOffsetRbwFilterArray(self: RFmxNRMXSemConfiguration, selectorString: str, offsetRbw: Array[float], offsetRbwFilterType: Array[RFmxNRMXSemOffsetRbwFilterType]) -> int """
        pass

    def ConfigureOffsetRelativeLimit(self, selectorString, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimit(self: RFmxNRMXSemConfiguration, selectorString: str, relativeLimitStart: float, relativeLimitStop: float) -> int """
        pass

    def ConfigureOffsetRelativeLimitArray(self, selectorString, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimitArray(self: RFmxNRMXSemConfiguration, selectorString: str, relativeLimitStart: Array[float], relativeLimitStop: Array[float]) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxNRMXSemConfiguration, selectorString: str, sweepTimeAuto: RFmxNRMXSemSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def ConfigureUplinkMaskType(self, selectorString, uplinkMaskType):
        """ ConfigureUplinkMaskType(self: RFmxNRMXSemConfiguration, selectorString: str, uplinkMaskType: RFmxNRMXSemUplinkMaskType) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemAveragingType) """
        pass

    def GetDeltaFMaximum(self, selectorString, value):
        """ GetDeltaFMaximum(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDownlinkMaskType(self, selectorString, value):
        """ GetDownlinkMaskType(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemDownlinkMaskType) """
        pass

    def GetFftWindow(self, selectorString, value):
        """ GetFftWindow(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemFftWindow) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfOffsets(self, selectorString, value):
        """ GetNumberOfOffsets(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetAbsoluteLimitStart(self, selectorString, value):
        """ GetOffsetAbsoluteLimitStart(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetAbsoluteLimitStop(self, selectorString, value):
        """ GetOffsetAbsoluteLimitStop(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetBandwidthIntegral(self, selectorString, value):
        """ GetOffsetBandwidthIntegral(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetLimitFailMask(self, selectorString, value):
        """ GetOffsetLimitFailMask(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemOffsetLimitFailMask) """
        pass

    def GetOffsetRbwFilterBandwidth(self, selectorString, value):
        """ GetOffsetRbwFilterBandwidth(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRbwFilterType(self, selectorString, value):
        """ GetOffsetRbwFilterType(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemOffsetRbwFilterType) """
        pass

    def GetOffsetRelativeLimitStart(self, selectorString, value):
        """ GetOffsetRelativeLimitStart(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRelativeLimitStop(self, selectorString, value):
        """ GetOffsetRelativeLimitStop(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetSideband(self, selectorString, value):
        """ GetOffsetSideband(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemOffsetSideband) """
        pass

    def GetOffsetStartFrequency(self, selectorString, value):
        """ GetOffsetStartFrequency(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetStopFrequency(self, selectorString, value):
        """ GetOffsetStopFrequency(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSubblockAggregatedChannelBandwidth(self, selectorString, value):
        """ GetSubblockAggregatedChannelBandwidth(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetUplinkMaskType(self, selectorString, value):
        """ GetUplinkMaskType(self: RFmxNRMXSemConfiguration, selectorString: str) -> (int, RFmxNRMXSemUplinkMaskType) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxNRMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxNRMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemAveragingType) -> int """
        pass

    def SetDeltaFMaximum(self, selectorString, value):
        """ SetDeltaFMaximum(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetDownlinkMaskType(self, selectorString, value):
        """ SetDownlinkMaskType(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemDownlinkMaskType) -> int """
        pass

    def SetFftWindow(self, selectorString, value):
        """ SetFftWindow(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemFftWindow) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxNRMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxNRMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfOffsets(self, selectorString, value):
        """ SetNumberOfOffsets(self: RFmxNRMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetAbsoluteLimitStart(self, selectorString, value):
        """ SetOffsetAbsoluteLimitStart(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetAbsoluteLimitStop(self, selectorString, value):
        """ SetOffsetAbsoluteLimitStop(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetBandwidthIntegral(self, selectorString, value):
        """ SetOffsetBandwidthIntegral(self: RFmxNRMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetLimitFailMask(self, selectorString, value):
        """ SetOffsetLimitFailMask(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemOffsetLimitFailMask) -> int """
        pass

    def SetOffsetRbwFilterBandwidth(self, selectorString, value):
        """ SetOffsetRbwFilterBandwidth(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRbwFilterType(self, selectorString, value):
        """ SetOffsetRbwFilterType(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemOffsetRbwFilterType) -> int """
        pass

    def SetOffsetRelativeLimitStart(self, selectorString, value):
        """ SetOffsetRelativeLimitStart(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRelativeLimitStop(self, selectorString, value):
        """ SetOffsetRelativeLimitStop(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetSideband(self, selectorString, value):
        """ SetOffsetSideband(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemOffsetSideband) -> int """
        pass

    def SetOffsetStartFrequency(self, selectorString, value):
        """ SetOffsetStartFrequency(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetStopFrequency(self, selectorString, value):
        """ SetOffsetStopFrequency(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxNRMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetUplinkMaskType(self, selectorString, value):
        """ SetUplinkMaskType(self: RFmxNRMXSemConfiguration, selectorString: str, value: RFmxNRMXSemUplinkMaskType) -> int """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMXSemConfiguration) -> RFmxNRMXSemComponentCarrierConfiguration

"""



class RFmxNRMXSemDownlinkMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemDownlinkMaskType, values: Custom (2), Standard (0) """
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
    Standard = None
    value__ = None


class RFmxNRMXSemFftWindow(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemFftWindow, values: Blackman (5), BlackmanHarris (6), FlatTop (1), Gaussian (4), Hamming (3), Hanning (2), KaiserBessel (7), None (0) """
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


class RFmxNRMXSemLowerOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemLowerOffsetMeasurementStatus, values: Fail (0), Pass (1) """
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


class RFmxNRMXSemMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemMeasurementStatus, values: Fail (0), Pass (1) """
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


class RFmxNRMXSemOffsetLimitFailMask(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemOffsetLimitFailMask, values: AbsAndRel (0), Absolute (2), AbsOrRel (1), Relative (3) """
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

    AbsAndRel = None
    Absolute = None
    AbsOrRel = None
    Relative = None
    value__ = None


class RFmxNRMXSemOffsetRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemOffsetRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
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
    value__ = None


class RFmxNRMXSemOffsetSideband(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemOffsetSideband, values: Both (2), Negative (0), Positive (1) """
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


class RFmxNRMXSemResults(RFmxNRMXSubObject):
    # no doc
    def FetchLowerOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMargin(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, RFmxNRMXSemLowerOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchLowerOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMarginArray(self: RFmxNRMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxNRMXSemLowerOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxNRMXSemLowerOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchLowerOffsetPower(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchLowerOffsetPower(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchLowerOffsetPowerArray(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchLowerOffsetPowerArray(self: RFmxNRMXSemResults, selectorString: str, timeout: float, totalAbsolutePower: Array[float], totalRelativePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], peakRelativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchMeasurementStatus(self, selectorString, timeout, measurementStatus):
        """ FetchMeasurementStatus(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, RFmxNRMXSemMeasurementStatus) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum, compositeMask):
        """ FetchSpectrum(self: RFmxNRMXSemResults, selectorString: str, timeout: float, spectrum: Spectrum[Single], compositeMask: Spectrum[Single]) -> (int, Spectrum[Single], Spectrum[Single]) """
        pass

    def FetchSubblockPower(self, selectorString, timeout, subblockPower):
        """ FetchSubblockPower(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchUpperOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMargin(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, RFmxNRMXSemUpperOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchUpperOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMarginArray(self: RFmxNRMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxNRMXSemUpperOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxNRMXSemUpperOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchUpperOffsetPower(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchUpperOffsetPower(self: RFmxNRMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchUpperOffsetPowerArray(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchUpperOffsetPowerArray(self: RFmxNRMXSemResults, selectorString: str, timeout: float, totalAbsolutePower: Array[float], totalRelativePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], peakRelativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLowerOffsetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetLowerOffsetAbsoluteIntegratedPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetAbsolutePeakPower(self, selectorString, value):
        """ GetLowerOffsetAbsolutePeakPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMargin(self, selectorString, value):
        """ GetLowerOffsetMargin(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetMarginAbsolutePower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginFrequency(self, selectorString, value):
        """ GetLowerOffsetMarginFrequency(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginRelativePower(self, selectorString, value):
        """ GetLowerOffsetMarginRelativePower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMeasurementStatus(self, selectorString, value):
        """ GetLowerOffsetMeasurementStatus(self: RFmxNRMXSemResults, selectorString: str) -> (int, RFmxNRMXSemLowerOffsetMeasurementStatus) """
        pass

    def GetLowerOffsetPeakFrequency(self, selectorString, value):
        """ GetLowerOffsetPeakFrequency(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativeIntegratedPower(self, selectorString, value):
        """ GetLowerOffsetRelativeIntegratedPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativePeakPower(self, selectorString, value):
        """ GetLowerOffsetRelativePeakPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementStatus(self, selectorString, value):
        """ GetMeasurementStatus(self: RFmxNRMXSemResults, selectorString: str) -> (int, RFmxNRMXSemMeasurementStatus) """
        pass

    def GetSubblockPower(self, selectorString, value):
        """ GetSubblockPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalAggregatedPower(self, selectorString, value):
        """ GetTotalAggregatedPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetUpperOffsetAbsoluteIntegratedPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsolutePeakPower(self, selectorString, value):
        """ GetUpperOffsetAbsolutePeakPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMargin(self, selectorString, value):
        """ GetUpperOffsetMargin(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetMarginAbsolutePower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginFrequency(self, selectorString, value):
        """ GetUpperOffsetMarginFrequency(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginRelativePower(self, selectorString, value):
        """ GetUpperOffsetMarginRelativePower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMeasurementStatus(self, selectorString, value):
        """ GetUpperOffsetMeasurementStatus(self: RFmxNRMXSemResults, selectorString: str) -> (int, RFmxNRMXSemUpperOffsetMeasurementStatus) """
        pass

    def GetUpperOffsetPeakFrequency(self, selectorString, value):
        """ GetUpperOffsetPeakFrequency(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativeIntegratedPower(self, selectorString, value):
        """ GetUpperOffsetRelativeIntegratedPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativePeakPower(self, selectorString, value):
        """ GetUpperOffsetRelativePeakPower(self: RFmxNRMXSemResults, selectorString: str) -> (int, float) """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxNRMXSemResults) -> RFmxNRMXSemComponentCarrierResults

"""



class RFmxNRMXSemSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemSweepTimeAuto, values: False (0), True (1) """
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


class RFmxNRMXSemUplinkMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemUplinkMaskType, values: Custom (2), General (0), NS03 (3), NS04 (4), NS06 (5), NS35 (1) """
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
    General = None
    NS03 = None
    NS04 = None
    NS06 = None
    NS35 = None
    value__ = None


class RFmxNRMXSemUpperOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSemUpperOffsetMeasurementStatus, values: Fail (0), Pass (1) """
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


class RFmxNRMXSsbEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSsbEnabled, values: False (0), True (1) """
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


class RFmxNRMXSsbPattern(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSsbPattern, values: CaseA3GHzTo6GHz (1), CaseAUpTo3GHz (0), CaseB3GHzTo6GHz (3), CaseBUpTo3GHz (2), CaseC3GHzTo6GHz (5), CaseCUpTo3GHz (4), CaseD (6), CaseE (7) """
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

    CaseA3GHzTo6GHz = None
    CaseAUpTo3GHz = None
    CaseB3GHzTo6GHz = None
    CaseBUpTo3GHz = None
    CaseC3GHzTo6GHz = None
    CaseCUpTo3GHz = None
    CaseD = None
    CaseE = None
    value__ = None


class RFmxNRMXSubblockFrequencyDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXSubblockFrequencyDefinition, values: Absolute (1), Relative (0) """
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


class RFmxNRMXTransmitterArchitecture(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXTransmitterArchitecture, values: LOPerComponentCarrier (0), LOPerSubblock (1) """
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

    LOPerComponentCarrier = None
    LOPerSubblock = None
    value__ = None


class RFmxNRMXTriggerMinimumQuietTimeMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXTriggerMinimumQuietTimeMode, values: Auto (1), Manual (0) """
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


class RFmxNRMXTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxNRMXTriggerType, values: DigitalEdge (1), IQPowerEdge (2), None (0), Software (3) """
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


