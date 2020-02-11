# encoding: utf-8
# module NationalInstruments.RFmx.LteMX calls itself LteMX
# from NationalInstruments.RFmx.LteMX.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RFmxLteMX(object, IDisposable, ISignalConfiguration):
    # no doc
    def AbortMeasurements(self, selectorString):
        """ AbortMeasurements(self: RFmxLteMX, selectorString: str) -> int """
        pass

    def AnalyzeIQ(self, selectorString, resultName, iq, reset, averagingDone):
        """ AnalyzeIQ(self: RFmxLteMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool) -> (int, bool) """
        pass

    def AnalyzeIQ1Waveform(self, selectorString, resultName, iq, reset, reserved):
        """ AnalyzeIQ1Waveform(self: RFmxLteMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool, reserved: Int64) -> int """
        pass

    def AnalyzeSpectrum(self, selectorString, resultName, spectrum, reset, averagingDone):
        """ AnalyzeSpectrum(self: RFmxLteMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool) -> (int, bool) """
        pass

    def AnalyzeSpectrum1Waveform(self, selectorString, resultName, spectrum, reset, reserved):
        """ AnalyzeSpectrum1Waveform(self: RFmxLteMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool, reserved: Int64) -> int """
        pass

    def AutoLevel(self, selectorString, measurementInterval, referenceLevel):
        """ AutoLevel(self: RFmxLteMX, selectorString: str, measurementInterval: float) -> (int, float) """
        pass

    @staticmethod
    def BuildCarrierString(selectorString, carrierNumber):
        """ BuildCarrierString(selectorString: str, carrierNumber: int) -> str """
        pass

    @staticmethod
    def BuildClusterString(selectorString, clusterNumber):
        """ BuildClusterString(selectorString: str, clusterNumber: int) -> str """
        pass

    @staticmethod
    def BuildOffsetString(selectorString, offsetNumber):
        """ BuildOffsetString(selectorString: str, offsetNumber: int) -> str """
        pass

    @staticmethod
    def BuildPdschString(selectorString, pdschNumber):
        """ BuildPdschString(selectorString: str, pdschNumber: int) -> str """
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
    def BuildSubframeString(selectorString, subframeNumber):
        """ BuildSubframeString(selectorString: str, subframeNumber: int) -> str """
        pass

    @staticmethod
    def CalculateFrequencyFromEarfcn(linkDirection, band, earfcn, centerFrequency):
        """ CalculateFrequencyFromEarfcn(linkDirection: RFmxLteMXLinkDirection, band: int, earfcn: int) -> (int, float) """
        pass

    def CheckMeasurementStatus(self, selectorString, done):
        """ CheckMeasurementStatus(self: RFmxLteMX, selectorString: str) -> (int, bool) """
        pass

    def ClearAllNamedResults(self, selectorString):
        """ ClearAllNamedResults(self: RFmxLteMX, selectorString: str) -> int """
        pass

    def ClearNamedResult(self, selectorString):
        """ ClearNamedResult(self: RFmxLteMX, selectorString: str) -> int """
        pass

    def CloneSignalConfiguration(self, newSignalName, signalConfiguration):
        """ CloneSignalConfiguration(self: RFmxLteMX, newSignalName: str) -> (int, RFmxLteMX) """
        pass

    def Commit(self, selectorString):
        """ Commit(self: RFmxLteMX, selectorString: str) -> int """
        pass

    def ConfigureAutoDmrsDetectionEnabled(self, selectorString, autoDmrsDetectionEnabled):
        """ ConfigureAutoDmrsDetectionEnabled(self: RFmxLteMX, selectorString: str, autoDmrsDetectionEnabled: RFmxLteMXAutoDmrsDetectionEnabled) -> int """
        pass

    def ConfigureBand(self, selectorString, band):
        """ ConfigureBand(self: RFmxLteMX, selectorString: str, band: int) -> int """
        pass

    def ConfigureDigitalEdgeTrigger(self, selectorString, digitalEdgeTriggerSource, digitalEdgeTriggerEdge, triggerDelay, enableTrigger):
        """ ConfigureDigitalEdgeTrigger(self: RFmxLteMX, selectorString: str, digitalEdgeTriggerSource: str, digitalEdgeTriggerEdge: RFmxLteMXDigitalEdgeTriggerEdge, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def ConfigureDuplexScheme(self, selectorString, duplexScheme, uplinkDownlinkConfiguration):
        """ ConfigureDuplexScheme(self: RFmxLteMX, selectorString: str, duplexScheme: RFmxLteMXDuplexScheme, uplinkDownlinkConfiguration: RFmxLteMXUplinkDownlinkConfiguration) -> int """
        pass

    def ConfigureeNodeBCategory(self, selectorString, eNodeBCategory):
        """ ConfigureeNodeBCategory(self: RFmxLteMX, selectorString: str, eNodeBCategory: RFmxLteMXeNodeBCategory) -> int """
        pass

    def ConfigureExternalAttenuation(self, selectorString, externalAttenuation):
        """ ConfigureExternalAttenuation(self: RFmxLteMX, selectorString: str, externalAttenuation: float) -> int """
        pass

    def ConfigureFrequency(self, selectorString, centerFrequency):
        """ ConfigureFrequency(self: RFmxLteMX, selectorString: str, centerFrequency: float) -> int """
        pass

    def ConfigureFrequencyEarfcn(self, selectorString, linkDirection, band, earfcn):
        """ ConfigureFrequencyEarfcn(self: RFmxLteMX, selectorString: str, linkDirection: RFmxLteMXLinkDirection, band: int, earfcn: int) -> int """
        pass

    def ConfigureIQPowerEdgeTrigger(self, selectorString, iqPowerEdgeTriggerSource, iqPowerEdgeTriggerSlope, iqPowerEdgeTriggerLevel, triggerDelay, minimumQuietTimeMode, minimumQuietTimeDuration, iqPowerEdgeTriggerLevelType, enableTrigger):
        """ ConfigureIQPowerEdgeTrigger(self: RFmxLteMX, selectorString: str, iqPowerEdgeTriggerSource: str, iqPowerEdgeTriggerSlope: RFmxLteMXIQPowerEdgeTriggerSlope, iqPowerEdgeTriggerLevel: float, triggerDelay: float, minimumQuietTimeMode: RFmxLteMXTriggerMinimumQuietTimeMode, minimumQuietTimeDuration: float, iqPowerEdgeTriggerLevelType: RFmxLteMXIQPowerEdgeTriggerLevelType, enableTrigger: bool) -> int """
        pass

    def ConfigureLinkDirection(self, selectorString, linkDirection):
        """ ConfigureLinkDirection(self: RFmxLteMX, selectorString: str, linkDirection: RFmxLteMXLinkDirection) -> int """
        pass

    def ConfigureNumberOfComponentCarriers(self, selectorString, numberOfComponentCarriers):
        """ ConfigureNumberOfComponentCarriers(self: RFmxLteMX, selectorString: str, numberOfComponentCarriers: int) -> int """
        pass

    def ConfigureNumberOfDutAntennas(self, selectorString, numberOfDutAntennas):
        """ ConfigureNumberOfDutAntennas(self: RFmxLteMX, selectorString: str, numberOfDutAntennas: int) -> int """
        pass

    def ConfigureNumberOfSubblocks(self, selectorString, numberOfSubblocks):
        """ ConfigureNumberOfSubblocks(self: RFmxLteMX, selectorString: str, numberOfSubblocks: int) -> int """
        pass

    def ConfigureReferenceLevel(self, selectorString, referenceLevel):
        """ ConfigureReferenceLevel(self: RFmxLteMX, selectorString: str, referenceLevel: float) -> int """
        pass

    def ConfigureReferenceLevelUnits(self, selectorString, referenceLevelUnits):
        """ ConfigureReferenceLevelUnits(self: RFmxLteMX, selectorString: str, referenceLevelUnits: RFmxLteMXReferenceLevelUnits) -> int """
        pass

    def ConfigureRF(self, selectorString, centerFrequency, referenceLevel, externalAttenuation):
        """ ConfigureRF(self: RFmxLteMX, selectorString: str, centerFrequency: float, referenceLevel: float, externalAttenuation: float) -> int """
        pass

    def ConfigureSoftwareEdgeTrigger(self, selectorString, triggerDelay, enableTrigger):
        """ ConfigureSoftwareEdgeTrigger(self: RFmxLteMX, selectorString: str, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def ConfigureSubblockFrequencyDefinition(self, selectorString, subblockFrequencyDefinition):
        """ ConfigureSubblockFrequencyDefinition(self: RFmxLteMX, selectorString: str, subblockFrequencyDefinition: RFmxLteMXSubblockFrequencyDefinition) -> int """
        pass

    def ConfigureTransmitAntennaToAnalyze(self, selectorString, transmitAntennaToAnalyze):
        """ ConfigureTransmitAntennaToAnalyze(self: RFmxLteMX, selectorString: str, transmitAntennaToAnalyze: int) -> int """
        pass

    def DeleteSignalConfiguration(self):
        """ DeleteSignalConfiguration(self: RFmxLteMX) -> int """
        pass

    def DisableTrigger(self, selectorString):
        """ DisableTrigger(self: RFmxLteMX, selectorString: str) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: RFmxLteMX) """
        pass

    def GetAcquisitionBandwidthOptimizationEnabled(self, selectorString, value):
        """ GetAcquisitionBandwidthOptimizationEnabled(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXAcquisitionBandwidthOptimizationEnabled) """
        pass

    def GetAllNamedResultNames(self, selectorString, resultNames, defaultResultExists):
        """ GetAllNamedResultNames(self: RFmxLteMX, selectorString: str) -> (int, Array[str], bool) """
        pass

    def GetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ GetAttributeBool(self: RFmxLteMX, selectorString: str, attributeIdentifier: int) -> (int, bool) """
        pass

    def GetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ GetAttributeDouble(self: RFmxLteMX, selectorString: str, attributeIdentifier: int) -> (int, float) """
        pass

    def GetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ GetAttributeInt(self: RFmxLteMX, selectorString: str, attributeIdentifier: int) -> (int, int) """
        pass

    def GetAttributeString(self, selectorString, attributeIdentifier, value):
        """ GetAttributeString(self: RFmxLteMX, selectorString: str, attributeIdentifier: int) -> (int, str) """
        pass

    def GetAutoDmrsDetectionEnabled(self, selectorString, value):
        """ GetAutoDmrsDetectionEnabled(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXAutoDmrsDetectionEnabled) """
        pass

    def GetAutoLevelInitialReferenceLevel(self, selectorString, value):
        """ GetAutoLevelInitialReferenceLevel(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetBand(self, selectorString, value):
        """ GetBand(self: RFmxLteMX, selectorString: str) -> (int, int) """
        pass

    def GetCenterFrequency(self, selectorString, value):
        """ GetCenterFrequency(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetCenterFrequencyForLimits(self, selectorString, value):
        """ GetCenterFrequencyForLimits(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ GetDigitalEdgeTriggerEdge(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXDigitalEdgeTriggerEdge) """
        pass

    def GetDigitalEdgeTriggerSource(self, selectorString, value):
        """ GetDigitalEdgeTriggerSource(self: RFmxLteMX, selectorString: str) -> (int, str) """
        pass

    def GetDuplexScheme(self, selectorString, value):
        """ GetDuplexScheme(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXDuplexScheme) """
        pass

    def GeteNodeBCategory(self, selectorString, value):
        """ GeteNodeBCategory(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXeNodeBCategory) """
        pass

    def GetError(self, errorCode, errorDescription):
        """ GetError(self: RFmxLteMX) -> (int, int, str) """
        pass

    def GetErrorString(self, errorCode, errorDescription):
        """ GetErrorString(self: RFmxLteMX, errorCode: int) -> (int, str) """
        pass

    def GetExternalAttenuation(self, selectorString, value):
        """ GetExternalAttenuation(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevel(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevelType(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXIQPowerEdgeTriggerLevelType) """
        pass

    def GetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSlope(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXIQPowerEdgeTriggerSlope) """
        pass

    def GetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSource(self: RFmxLteMX, selectorString: str) -> (int, str) """
        pass

    def GetLimitedConfigurationChange(self, selectorString, value):
        """ GetLimitedConfigurationChange(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXLimitedConfigurationChange) """
        pass

    def GetLinkDirection(self, selectorString, value):
        """ GetLinkDirection(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXLinkDirection) """
        pass

    def GetMiConfiguration(self, selectorString, value):
        """ GetMiConfiguration(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXMiConfiguration) """
        pass

    def GetNumberOfDutAntennas(self, selectorString, value):
        """ GetNumberOfDutAntennas(self: RFmxLteMX, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfSubblocks(self, selectorString, value):
        """ GetNumberOfSubblocks(self: RFmxLteMX, selectorString: str) -> (int, int) """
        pass

    def GetPuschPower(self, selectorString, value):
        """ GetPuschPower(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetReferenceLevel(self, selectorString, value):
        """ GetReferenceLevel(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetReferenceLevelHeadroom(self, selectorString, value):
        """ GetReferenceLevelHeadroom(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetResultFetchTimeout(self, selectorString, value):
        """ GetResultFetchTimeout(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetSelectedPorts(self, selectorString, value):
        """ GetSelectedPorts(self: RFmxLteMX, selectorString: str) -> (int, str) """
        pass

    def GetSpecialSubframeConfiguration(self, selectorString, value):
        """ GetSpecialSubframeConfiguration(self: RFmxLteMX, selectorString: str) -> (int, int) """
        pass

    def GetSubblockFrequencyDefinition(self, selectorString, value):
        """ GetSubblockFrequencyDefinition(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXSubblockFrequencyDefinition) """
        pass

    def GetTransmitAntennaToAnalyze(self, selectorString, value):
        """ GetTransmitAntennaToAnalyze(self: RFmxLteMX, selectorString: str) -> (int, int) """
        pass

    def GetTransmitterArchitecture(self, selectorString, value):
        """ GetTransmitterArchitecture(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXTransmitterArchitecture) """
        pass

    def GetTriggerDelay(self, selectorString, value):
        """ GetTriggerDelay(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeDuration(self: RFmxLteMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeMode(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXTriggerMinimumQuietTimeMode) """
        pass

    def GetTriggerType(self, selectorString, value):
        """ GetTriggerType(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXTriggerType) """
        pass

    def GetUplinkDownlinkConfiguration(self, selectorString, value):
        """ GetUplinkDownlinkConfiguration(self: RFmxLteMX, selectorString: str) -> (int, RFmxLteMXUplinkDownlinkConfiguration) """
        pass

    def GetWarning(self, warningCode, warningDescription):
        """ GetWarning(self: RFmxLteMX) -> (int, int, str) """
        pass

    def Initiate(self, selectorString, resultName):
        """ Initiate(self: RFmxLteMX, selectorString: str, resultName: str) -> int """
        pass

    def ResetAttribute(self, selectorString, attributeId):
        """ ResetAttribute(self: RFmxLteMX, selectorString: str, attributeId: RFmxLteMXPropertyId) -> int """
        pass

    def ResetToDefault(self, selectorString):
        """ ResetToDefault(self: RFmxLteMX, selectorString: str) -> int """
        pass

    def SelectMeasurements(self, selectorString, measurement, enableAllTraces):
        """ SelectMeasurements(self: RFmxLteMX, selectorString: str, measurement: RFmxLteMXMeasurementTypes, enableAllTraces: bool) -> int """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RFmxLteMX) -> int """
        pass

    def SetAcquisitionBandwidthOptimizationEnabled(self, selectorString, value):
        """ SetAcquisitionBandwidthOptimizationEnabled(self: RFmxLteMX, selectorString: str, value: RFmxLteMXAcquisitionBandwidthOptimizationEnabled) -> int """
        pass

    def SetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ SetAttributeBool(self: RFmxLteMX, selectorString: str, attributeIdentifier: int, value: bool) -> int """
        pass

    def SetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ SetAttributeDouble(self: RFmxLteMX, selectorString: str, attributeIdentifier: int, value: float) -> int """
        pass

    def SetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ SetAttributeInt(self: RFmxLteMX, selectorString: str, attributeIdentifier: int, value: int) -> int """
        pass

    def SetAttributeString(self, selectorString, attributeIdentifier, value):
        """ SetAttributeString(self: RFmxLteMX, selectorString: str, attributeIdentifier: int, value: str) -> int """
        pass

    def SetAutoDmrsDetectionEnabled(self, selectorString, value):
        """ SetAutoDmrsDetectionEnabled(self: RFmxLteMX, selectorString: str, value: RFmxLteMXAutoDmrsDetectionEnabled) -> int """
        pass

    def SetAutoLevelInitialReferenceLevel(self, selectorString, value):
        """ SetAutoLevelInitialReferenceLevel(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetBand(self, selectorString, value):
        """ SetBand(self: RFmxLteMX, selectorString: str, value: int) -> int """
        pass

    def SetCenterFrequency(self, selectorString, value):
        """ SetCenterFrequency(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetCenterFrequencyForLimits(self, selectorString, value):
        """ SetCenterFrequencyForLimits(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ SetDigitalEdgeTriggerEdge(self: RFmxLteMX, selectorString: str, value: RFmxLteMXDigitalEdgeTriggerEdge) -> int """
        pass

    def SetDigitalEdgeTriggerSource(self, selectorString, value):
        """ SetDigitalEdgeTriggerSource(self: RFmxLteMX, selectorString: str, value: str) -> int """
        pass

    def SetDuplexScheme(self, selectorString, value):
        """ SetDuplexScheme(self: RFmxLteMX, selectorString: str, value: RFmxLteMXDuplexScheme) -> int """
        pass

    def SeteNodeBCategory(self, selectorString, value):
        """ SeteNodeBCategory(self: RFmxLteMX, selectorString: str, value: RFmxLteMXeNodeBCategory) -> int """
        pass

    def SetExternalAttenuation(self, selectorString, value):
        """ SetExternalAttenuation(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevel(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevelType(self: RFmxLteMX, selectorString: str, value: RFmxLteMXIQPowerEdgeTriggerLevelType) -> int """
        pass

    def SetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSlope(self: RFmxLteMX, selectorString: str, value: RFmxLteMXIQPowerEdgeTriggerSlope) -> int """
        pass

    def SetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSource(self: RFmxLteMX, selectorString: str, value: str) -> int """
        pass

    def SetLimitedConfigurationChange(self, selectorString, value):
        """ SetLimitedConfigurationChange(self: RFmxLteMX, selectorString: str, value: RFmxLteMXLimitedConfigurationChange) -> int """
        pass

    def SetLinkDirection(self, selectorString, value):
        """ SetLinkDirection(self: RFmxLteMX, selectorString: str, value: RFmxLteMXLinkDirection) -> int """
        pass

    def SetMiConfiguration(self, selectorString, value):
        """ SetMiConfiguration(self: RFmxLteMX, selectorString: str, value: RFmxLteMXMiConfiguration) -> int """
        pass

    def SetNumberOfDutAntennas(self, selectorString, value):
        """ SetNumberOfDutAntennas(self: RFmxLteMX, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfSubblocks(self, selectorString, value):
        """ SetNumberOfSubblocks(self: RFmxLteMX, selectorString: str, value: int) -> int """
        pass

    def SetPuschPower(self, selectorString, value):
        """ SetPuschPower(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetReferenceLevel(self, selectorString, value):
        """ SetReferenceLevel(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetReferenceLevelHeadroom(self, selectorString, value):
        """ SetReferenceLevelHeadroom(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetResultFetchTimeout(self, selectorString, value):
        """ SetResultFetchTimeout(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetSelectedPorts(self, selectorString, value):
        """ SetSelectedPorts(self: RFmxLteMX, selectorString: str, value: str) -> int """
        pass

    def SetSpecialSubframeConfiguration(self, selectorString, value):
        """ SetSpecialSubframeConfiguration(self: RFmxLteMX, selectorString: str, value: int) -> int """
        pass

    def SetSubblockFrequencyDefinition(self, selectorString, value):
        """ SetSubblockFrequencyDefinition(self: RFmxLteMX, selectorString: str, value: RFmxLteMXSubblockFrequencyDefinition) -> int """
        pass

    def SetTransmitAntennaToAnalyze(self, selectorString, value):
        """ SetTransmitAntennaToAnalyze(self: RFmxLteMX, selectorString: str, value: int) -> int """
        pass

    def SetTransmitterArchitecture(self, selectorString, value):
        """ SetTransmitterArchitecture(self: RFmxLteMX, selectorString: str, value: RFmxLteMXTransmitterArchitecture) -> int """
        pass

    def SetTriggerDelay(self, selectorString, value):
        """ SetTriggerDelay(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeDuration(self: RFmxLteMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeMode(self: RFmxLteMX, selectorString: str, value: RFmxLteMXTriggerMinimumQuietTimeMode) -> int """
        pass

    def SetTriggerType(self, selectorString, value):
        """ SetTriggerType(self: RFmxLteMX, selectorString: str, value: RFmxLteMXTriggerType) -> int """
        pass

    def SetUplinkDownlinkConfiguration(self, selectorString, value):
        """ SetUplinkDownlinkConfiguration(self: RFmxLteMX, selectorString: str, value: RFmxLteMXUplinkDownlinkConfiguration) -> int """
        pass

    def WaitForMeasurementComplete(self, selectorString, timeout):
        """ WaitForMeasurementComplete(self: RFmxLteMX, selectorString: str, timeout: float) -> int """
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
    """Get: Acp(self: RFmxLteMX) -> RFmxLteMXAcp

"""

    Chp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chp(self: RFmxLteMX) -> RFmxLteMXChp

"""

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxLteMX) -> RFmxLteMXComponentCarrier

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: RFmxLteMX) -> bool

"""

    ModAcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModAcc(self: RFmxLteMX) -> RFmxLteMXModAcc

"""

    Obw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Obw(self: RFmxLteMX) -> RFmxLteMXObw

"""

    Pvt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pvt(self: RFmxLteMX) -> RFmxLteMXPvt

"""

    Sem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sem(self: RFmxLteMX) -> RFmxLteMXSem

"""

    SignalConfigurationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationName(self: RFmxLteMX) -> str

"""

    SignalConfigurationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationType(self: RFmxLteMX) -> Type

"""

    SlotPhase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlotPhase(self: RFmxLteMX) -> RFmxLteMXSlotPhase

"""

    SlotPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlotPower(self: RFmxLteMX) -> RFmxLteMXSlotPower

"""



class RFmxLteMXSubObject(object):
    # no doc

class RFmxLteMXAcp(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXAcp) -> RFmxLteMXAcpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXAcp) -> RFmxLteMXAcpResults

"""



class RFmxLteMXAcpAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpComponentCarrierResults(RFmxLteMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurement(self: RFmxLteMXAcpComponentCarrierResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurementArray(self: RFmxLteMXAcpComponentCarrierResults, selectorString: str, timeout: float, absolutePower: Array[float], relativePower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetAbsolutePower(self, selectorString, value):
        """ GetAbsolutePower(self: RFmxLteMXAcpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetRelativePower(self, selectorString, value):
        """ GetRelativePower(self: RFmxLteMXAcpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass


class RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxLteMXAcpConfiguration, selectorString: str, averagingEnabled: RFmxLteMXAcpAveragingEnabled, averagingCount: int, averagingType: RFmxLteMXAcpAveragingType) -> int """
        pass

    def ConfigureConfigurableNumberOfOffsetsEnabled(self, selectorString, configurableNumberOfOffsetsEnabled):
        """ ConfigureConfigurableNumberOfOffsetsEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, configurableNumberOfOffsetsEnabled: RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxLteMXAcpConfiguration, selectorString: str, measurementMethod: RFmxLteMXAcpMeasurementMethod) -> int """
        pass

    def ConfigureNoiseCompensationEnabled(self, selectorString, noiseCompensationEnabled):
        """ ConfigureNoiseCompensationEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, noiseCompensationEnabled: RFmxLteMXAcpNoiseCompensationEnabled) -> int """
        pass

    def ConfigureNumberOfEutraOffsets(self, selectorString, numberOfEutraOffsets):
        """ ConfigureNumberOfEutraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, numberOfEutraOffsets: int) -> int """
        pass

    def ConfigureNumberOfGsmOffsets(self, selectorString, numberOfGsmOffsets):
        """ ConfigureNumberOfGsmOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, numberOfGsmOffsets: int) -> int """
        pass

    def ConfigureNumberOfUtraOffsets(self, selectorString, numberOfUtraOffsets):
        """ ConfigureNumberOfUtraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, numberOfUtraOffsets: int) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxLteMXAcpConfiguration, selectorString: str, rbwAuto: RFmxLteMXAcpRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxLteMXAcpRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxLteMXAcpConfiguration, selectorString: str, sweepTimeAuto: RFmxLteMXAcpSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def ConfigureUtraAndEutraOffsets(self, selectorString, numberOfUtraOffsets, numberOfEutraOffsets):
        """ ConfigureUtraAndEutraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, numberOfUtraOffsets: int, numberOfEutraOffsets: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpAveragingType) """
        pass

    def GetComponentCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetComponentCarrierIntegrationBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetConfigurableNumberOfOffsetsEnabled(self, selectorString, value):
        """ GetConfigurableNumberOfOffsetsEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled) """
        pass

    def GetEutraOffsetDefinition(self, selectorString, value):
        """ GetEutraOffsetDefinition(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpEutraOffsetDefinition) """
        pass

    def GetFarIFOutputPowerOffset(self, selectorString, value):
        """ GetFarIFOutputPowerOffset(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ GetIFOutputPowerOffsetAuto(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpIFOutputPowerOffsetAuto) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpMeasurementMethod) """
        pass

    def GetNearIFOutputPowerOffset(self, selectorString, value):
        """ GetNearIFOutputPowerOffset(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNoiseCompensationEnabled(self, selectorString, value):
        """ GetNoiseCompensationEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpNoiseCompensationEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfEutraOffsets(self, selectorString, value):
        """ GetNumberOfEutraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfGsmOffsets(self, selectorString, value):
        """ GetNumberOfGsmOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfUtraOffsets(self, selectorString, value):
        """ GetNumberOfUtraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetFrequency(self, selectorString, value):
        """ GetOffsetFrequency(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetIntegrationBandwidth(self, selectorString, value):
        """ GetOffsetIntegrationBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpRbwFilterType) """
        pass

    def GetSequentialFftSize(self, selectorString, value):
        """ GetSequentialFftSize(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, RFmxLteMXAcpSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxLteMXAcpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxLteMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpAveragingType) -> int """
        pass

    def SetConfigurableNumberOfOffsetsEnabled(self, selectorString, value):
        """ SetConfigurableNumberOfOffsetsEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpConfigurableNumberOfOffsetsEnabled) -> int """
        pass

    def SetEutraOffsetDefinition(self, selectorString, value):
        """ SetEutraOffsetDefinition(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpEutraOffsetDefinition) -> int """
        pass

    def SetFarIFOutputPowerOffset(self, selectorString, value):
        """ SetFarIFOutputPowerOffset(self: RFmxLteMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetIFOutputPowerOffsetAuto(self, selectorString, value):
        """ SetIFOutputPowerOffsetAuto(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpIFOutputPowerOffsetAuto) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpMeasurementMethod) -> int """
        pass

    def SetNearIFOutputPowerOffset(self, selectorString, value):
        """ SetNearIFOutputPowerOffset(self: RFmxLteMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNoiseCompensationEnabled(self, selectorString, value):
        """ SetNoiseCompensationEnabled(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpNoiseCompensationEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxLteMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfEutraOffsets(self, selectorString, value):
        """ SetNumberOfEutraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfGsmOffsets(self, selectorString, value):
        """ SetNumberOfGsmOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfUtraOffsets(self, selectorString, value):
        """ SetNumberOfUtraOffsets(self: RFmxLteMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxLteMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpRbwFilterType) -> int """
        pass

    def SetSequentialFftSize(self, selectorString, value):
        """ SetSequentialFftSize(self: RFmxLteMXAcpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxLteMXAcpConfiguration, selectorString: str, value: RFmxLteMXAcpSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxLteMXAcpConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxLteMXAcpEutraOffsetDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpEutraOffsetDefinition, values: Auto (0), Closest (1), Composite (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Closest = None
    Composite = None
    value__ = None


class RFmxLteMXAcpIFOutputPowerOffsetAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpIFOutputPowerOffsetAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpMeasurementMethod, values: DynamicRange (1), Normal (0), SequentialFft (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpNoiseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpNoiseCompensationEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpRbwAutoBandwidth, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcpResults(RFmxLteMXSubObject):
    # no doc
    def FetchAbsolutePowersTrace(self, selectorString, timeout, traceIndex, absolutePowersTrace):
        """ FetchAbsolutePowersTrace(self: RFmxLteMXAcpResults, selectorString: str, timeout: float, traceIndex: int, absolutePowersTrace: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchOffsetMeasurement(self, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower):
        """ FetchOffsetMeasurement(self: RFmxLteMXAcpResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchOffsetMeasurementArray(self, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower):
        """ FetchOffsetMeasurementArray(self: RFmxLteMXAcpResults, selectorString: str, timeout: float, lowerRelativePower: Array[float], upperRelativePower: Array[float], lowerAbsolutePower: Array[float], upperAbsolutePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchRelativePowersTrace(self, selectorString, timeout, traceIndex, relativePowersTrace):
        """ FetchRelativePowersTrace(self: RFmxLteMXAcpResults, selectorString: str, timeout: float, traceIndex: int, relativePowersTrace: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxLteMXAcpResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSubblockMeasurement(self, selectorString, timeout, subblockPower, integrationBandwidth, frequency):
        """ FetchSubblockMeasurement(self: RFmxLteMXAcpResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxLteMXAcpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def GetLowerOffsetAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetAbsolutePower(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativePower(self, selectorString, value):
        """ GetLowerOffsetRelativePower(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockCenterFrequency(self, selectorString, value):
        """ GetSubblockCenterFrequency(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockPower(self, selectorString, value):
        """ GetSubblockPower(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalAggregatedPower(self, selectorString, value):
        """ GetTotalAggregatedPower(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetAbsolutePower(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativePower(self, selectorString, value):
        """ GetUpperOffsetRelativePower(self: RFmxLteMXAcpResults, selectorString: str) -> (int, float) """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxLteMXAcpResults) -> RFmxLteMXAcpComponentCarrierResults

"""



class RFmxLteMXAcpSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcpSweepTimeAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAcquisitionBandwidthOptimizationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAcquisitionBandwidthOptimizationEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAutoControlChannelPowerDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAutoControlChannelPowerDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAutoDmrsDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAutoDmrsDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAutoNPuschChannelDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAutoNPuschChannelDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAutoPcfichCfiDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAutoPcfichCfiDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAutoPdschChannelDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAutoPdschChannelDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXAutoResourceBlockDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXAutoResourceBlockDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXChp(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXChp) -> RFmxLteMXChpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXChp) -> RFmxLteMXChpResults

"""



class RFmxLteMXChpAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXChpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXChpAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXChpComponentCarrierResults(RFmxLteMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurement(self: RFmxLteMXChpComponentCarrierResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchMeasurementArray(self: RFmxLteMXChpComponentCarrierResults, selectorString: str, timeout: float, absolutePower: Array[float], relativePower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetAbsolutePower(self, selectorString, value):
        """ GetAbsolutePower(self: RFmxLteMXChpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetRelativePower(self, selectorString, value):
        """ GetRelativePower(self: RFmxLteMXChpComponentCarrierResults, selectorString: str) -> (int, float) """
        pass


class RFmxLteMXChpConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxLteMXChpConfiguration, selectorString: str, averagingEnabled: RFmxLteMXChpAveragingEnabled, averagingCount: int, averagingType: RFmxLteMXChpAveragingType) -> int """
        pass

    def ConfigureIntegrationBandwidthType(self, selectorString, integrationBandwidthType):
        """ ConfigureIntegrationBandwidthType(self: RFmxLteMXChpConfiguration, selectorString: str, integrationBandwidthType: RFmxLteMXChpIntegrationBandwidthType) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxLteMXChpConfiguration, selectorString: str, rbwAuto: RFmxLteMXChpRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxLteMXChpRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxLteMXChpConfiguration, selectorString: str, sweepTimeAuto: RFmxLteMXChpSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpAveragingType) """
        pass

    def GetComponentCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetComponentCarrierIntegrationBandwidth(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetIntegrationBandwidthType(self, selectorString, value):
        """ GetIntegrationBandwidthType(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpIntegrationBandwidthType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpRbwFilterType) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, RFmxLteMXChpSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxLteMXChpConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXChpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxLteMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpAveragingType) -> int """
        pass

    def SetIntegrationBandwidthType(self, selectorString, value):
        """ SetIntegrationBandwidthType(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpIntegrationBandwidthType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXChpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxLteMXChpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxLteMXChpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpRbwFilterType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxLteMXChpConfiguration, selectorString: str, value: RFmxLteMXChpSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxLteMXChpConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxLteMXChpIntegrationBandwidthType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpIntegrationBandwidthType, values: ChannelBandwidth (1), SignalBandwidth (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ChannelBandwidth = None
    SignalBandwidth = None
    value__ = None


class RFmxLteMXChpRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpRbwAutoBandwidth, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXChpRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXChpResults(RFmxLteMXSubObject):
    # no doc
    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxLteMXChpResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def FetchSubblockMeasurement(self, selectorString, timeout, subblockPower, integrationBandwidth, frequency):
        """ FetchSubblockMeasurement(self: RFmxLteMXChpResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxLteMXChpResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def GetSubblockFrequency(self, selectorString, value):
        """ GetSubblockFrequency(self: RFmxLteMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxLteMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockPower(self, selectorString, value):
        """ GetSubblockPower(self: RFmxLteMXChpResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalAggregatedPower(self, selectorString, value):
        """ GetTotalAggregatedPower(self: RFmxLteMXChpResults, selectorString: str) -> (int, float) """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxLteMXChpResults) -> RFmxLteMXChpComponentCarrierResults

"""



class RFmxLteMXChpSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXChpSweepTimeAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXComponentCarrier(RFmxLteMXSubObject):
    # no doc
    def Configure(self, selectorString, componentCarrierBandwidth, componentCarrierFrequency, cellId):
        """ Configure(self: RFmxLteMXComponentCarrier, selectorString: str, componentCarrierBandwidth: float, componentCarrierFrequency: float, cellId: int) -> int """
        pass

    def ConfigureArray(self, selectorString, componentCarrierBandwidth, componentCarrierFrequency, cellId):
        """ ConfigureArray(self: RFmxLteMXComponentCarrier, selectorString: str, componentCarrierBandwidth: Array[float], componentCarrierFrequency: Array[float], cellId: Array[int]) -> int """
        pass

    def ConfigureAutoNPuschChannelDetectionEnabled(self, selectorString, autoNPuschChannelDetectionEnabled):
        """ ConfigureAutoNPuschChannelDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, autoNPuschChannelDetectionEnabled: RFmxLteMXAutoNPuschChannelDetectionEnabled) -> int """
        pass

    def ConfigureAutoResourceBlockDetectionEnabled(self, selectorString, autoResourceBlockDetectionEnabled):
        """ ConfigureAutoResourceBlockDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, autoResourceBlockDetectionEnabled: RFmxLteMXAutoResourceBlockDetectionEnabled) -> int """
        pass

    def ConfigureCellSpecificRatio(self, selectorString, cellSpecificRatio):
        """ ConfigureCellSpecificRatio(self: RFmxLteMXComponentCarrier, selectorString: str, cellSpecificRatio: RFmxLteMXDownlinkUserDefinedRatio) -> int """
        pass

    def ConfigureDownlinkAutoCellIDDetectionEnabled(self, selectorString, autoCellIDDetectionEnabled):
        """ ConfigureDownlinkAutoCellIDDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, autoCellIDDetectionEnabled: RFmxLteMXDownlinkAutoCellIDDetectionEnabled) -> int """
        pass

    def ConfigureDownlinkAutoChannelDetection(self, selectorString, autoPdschChannelDetectionEnabled, autoControlChannelPowerDetectionEnabled, autoPcfichCfiDetectionEnabled):
        """ ConfigureDownlinkAutoChannelDetection(self: RFmxLteMXComponentCarrier, selectorString: str, autoPdschChannelDetectionEnabled: RFmxLteMXAutoPdschChannelDetectionEnabled, autoControlChannelPowerDetectionEnabled: RFmxLteMXAutoControlChannelPowerDetectionEnabled, autoPcfichCfiDetectionEnabled: RFmxLteMXAutoPcfichCfiDetectionEnabled) -> int """
        pass

    def ConfigureDownlinkChannelConfigurationMode(self, selectorString, channelConfigurationMode):
        """ ConfigureDownlinkChannelConfigurationMode(self: RFmxLteMXComponentCarrier, selectorString: str, channelConfigurationMode: RFmxLteMXDownlinkChannelConfigurationMode) -> int """
        pass

    def ConfigureDownlinkNumberOfSubframes(self, selectorString, numberOfSubframes):
        """ ConfigureDownlinkNumberOfSubframes(self: RFmxLteMXComponentCarrier, selectorString: str, numberOfSubframes: int) -> int """
        pass

    def ConfigureDownlinkSynchronizationSignal(self, selectorString, pssPower, sssPower):
        """ ConfigureDownlinkSynchronizationSignal(self: RFmxLteMXComponentCarrier, selectorString: str, pssPower: float, sssPower: float) -> int """
        pass

    def ConfigureDownlinkTestModel(self, selectorString, downlinkTestModel):
        """ ConfigureDownlinkTestModel(self: RFmxLteMXComponentCarrier, selectorString: str, downlinkTestModel: RFmxLteMXDownlinkTestModel) -> int """
        pass

    def ConfigureDownlinkTestModelArray(self, selectorString, downlinkTestModel):
        """ ConfigureDownlinkTestModelArray(self: RFmxLteMXComponentCarrier, selectorString: str, downlinkTestModel: Array[RFmxLteMXDownlinkTestModel]) -> int """
        pass

    def ConfigureEmtcAnalysisEnabled(self, selectorString, emtcAnalysisEnabled):
        """ ConfigureEmtcAnalysisEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, emtcAnalysisEnabled: RFmxLteMXEmtcAnalysisEnabled) -> int """
        pass

    def ConfigureNBIoTComponentCarrier(self, selectorString, nCellID, uplinkSubcarrierSpacing):
        """ ConfigureNBIoTComponentCarrier(self: RFmxLteMXComponentCarrier, selectorString: str, nCellID: int, uplinkSubcarrierSpacing: RFmxLteMXNBIoTUplinkSubcarrierSpacing) -> int """
        pass

    def ConfigureNPuschDmrs(self, selectorString, nPuschDmrsBaseSequenceMode, nPuschDmrsBaseSequenceIndex, nPuschDmrsCyclicShift, nPuschDmrsGroupHoppingEnabled, nPuschDmrsDeltaSS):
        """ ConfigureNPuschDmrs(self: RFmxLteMXComponentCarrier, selectorString: str, nPuschDmrsBaseSequenceMode: RFmxLteMXNPuschDmrsBaseSequenceMode, nPuschDmrsBaseSequenceIndex: int, nPuschDmrsCyclicShift: int, nPuschDmrsGroupHoppingEnabled: RFmxLteMXNPuschDmrsGroupHoppingEnabled, nPuschDmrsDeltaSS: int) -> int """
        pass

    def ConfigureNPuschFormat(self, selectorString, format):
        """ ConfigureNPuschFormat(self: RFmxLteMXComponentCarrier, selectorString: str, format: int) -> int """
        pass

    def ConfigureNPuschStartingSlot(self, selectorString, startingSlot):
        """ ConfigureNPuschStartingSlot(self: RFmxLteMXComponentCarrier, selectorString: str, startingSlot: int) -> int """
        pass

    def ConfigureNPuschTones(self, selectorString, toneOffset, numberOfTones, modulationType):
        """ ConfigureNPuschTones(self: RFmxLteMXComponentCarrier, selectorString: str, toneOffset: int, numberOfTones: int, modulationType: RFmxLteMXNPuschModulationType) -> int """
        pass

    def ConfigureNumberOfPdschChannels(self, selectorString, numberOfPdschChannels):
        """ ConfigureNumberOfPdschChannels(self: RFmxLteMXComponentCarrier, selectorString: str, numberOfPdschChannels: int) -> int """
        pass

    def ConfigureNumberOfPuschResourceBlockClusters(self, selectorString, numberOfResourceBlockClusters):
        """ ConfigureNumberOfPuschResourceBlockClusters(self: RFmxLteMXComponentCarrier, selectorString: str, numberOfResourceBlockClusters: int) -> int """
        pass

    def ConfigurePbch(self, selectorString, pbchPower):
        """ ConfigurePbch(self: RFmxLteMXComponentCarrier, selectorString: str, pbchPower: float) -> int """
        pass

    def ConfigurePcfich(self, selectorString, cfi, power):
        """ ConfigurePcfich(self: RFmxLteMXComponentCarrier, selectorString: str, cfi: int, power: float) -> int """
        pass

    def ConfigurePdcch(self, selectorString, pdcchPower):
        """ ConfigurePdcch(self: RFmxLteMXComponentCarrier, selectorString: str, pdcchPower: float) -> int """
        pass

    def ConfigurePdsch(self, selectorString, cw0ModulationType, recourceBlockAllocation, power):
        """ ConfigurePdsch(self: RFmxLteMXComponentCarrier, selectorString: str, cw0ModulationType: RFmxLteMXUserDefinedPdschCW0ModulationType, recourceBlockAllocation: str, power: float) -> int """
        pass

    def ConfigurePhich(self, selectorString, resource, duration, power):
        """ ConfigurePhich(self: RFmxLteMXComponentCarrier, selectorString: str, resource: RFmxLteMXDownlinkUserDefinedPhichResource, duration: RFmxLteMXDownlinkUserDefinedPhichDuration, power: float) -> int """
        pass

    def ConfigurePsschModulationType(self, selectorString, modulationType):
        """ ConfigurePsschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str, modulationType: RFmxLteMXPsschModulationType) -> int """
        pass

    def ConfigurePsschResourceBlocks(self, selectorString, resourceBlockOffset, numberOfResourceBlocks):
        """ ConfigurePsschResourceBlocks(self: RFmxLteMXComponentCarrier, selectorString: str, resourceBlockOffset: int, numberOfResourceBlocks: int) -> int """
        pass

    def ConfigurePuschModulationType(self, selectorString, modulationType):
        """ ConfigurePuschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str, modulationType: RFmxLteMXPuschModulationType) -> int """
        pass

    def ConfigurePuschResourceBlocks(self, selectorString, resourceBlockOffset, numberOfResourceBlocks):
        """ ConfigurePuschResourceBlocks(self: RFmxLteMXComponentCarrier, selectorString: str, resourceBlockOffset: int, numberOfResourceBlocks: int) -> int """
        pass

    def ConfigureSpacing(self, selectorString, componentCarrierSpacingType, componentCarrierAtCenterFrequency):
        """ ConfigureSpacing(self: RFmxLteMXComponentCarrier, selectorString: str, componentCarrierSpacingType: RFmxLteMXComponentCarrierSpacingType, componentCarrierAtCenterFrequency: int) -> int """
        pass

    def GetAutoControlChannelPowerDetectionEnabled(self, selectorString, value):
        """ GetAutoControlChannelPowerDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXAutoControlChannelPowerDetectionEnabled) """
        pass

    def GetAutoNPuschChannelDetectionEnabled(self, selectorString, value):
        """ GetAutoNPuschChannelDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXAutoNPuschChannelDetectionEnabled) """
        pass

    def GetAutoPcfichCfiDetectionEnabled(self, selectorString, value):
        """ GetAutoPcfichCfiDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXAutoPcfichCfiDetectionEnabled) """
        pass

    def GetAutoPdschChannelDetectionEnabled(self, selectorString, value):
        """ GetAutoPdschChannelDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXAutoPdschChannelDetectionEnabled) """
        pass

    def GetAutoResourceBlockDetectionEnabled(self, selectorString, value):
        """ GetAutoResourceBlockDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXAutoResourceBlockDetectionEnabled) """
        pass

    def GetBandwidth(self, selectorString, value):
        """ GetBandwidth(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetCellId(self, selectorString, value):
        """ GetCellId(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetComponentCarrierAtCenterFrequency(self, selectorString, value):
        """ GetComponentCarrierAtCenterFrequency(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetCyclicPrefixMode(self, selectorString, value):
        """ GetCyclicPrefixMode(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXCyclicPrefixMode) """
        pass

    def GetDmrsOccEnabled(self, selectorString, value):
        """ GetDmrsOccEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDmrsOccEnabled) """
        pass

    def GetDownlinkAutoCellIDDetectionEnabled(self, selectorString, value):
        """ GetDownlinkAutoCellIDDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDownlinkAutoCellIDDetectionEnabled) """
        pass

    def GetDownlinkChannelConfigurationMode(self, selectorString, value):
        """ GetDownlinkChannelConfigurationMode(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDownlinkChannelConfigurationMode) """
        pass

    def GetDownlinkNumberOfSubframes(self, selectorString, value):
        """ GetDownlinkNumberOfSubframes(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetDownlinkTestModel(self, selectorString, value):
        """ GetDownlinkTestModel(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDownlinkTestModel) """
        pass

    def GetDownlinkUserDefinedCellSpecificRatio(self, selectorString, value):
        """ GetDownlinkUserDefinedCellSpecificRatio(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDownlinkUserDefinedRatio) """
        pass

    def GetEmtcAnalysisEnabled(self, selectorString, value):
        """ GetEmtcAnalysisEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXEmtcAnalysisEnabled) """
        pass

    def GetFrequency(self, selectorString, value):
        """ GetFrequency(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetLaaDownlinkNumberOfEndingSymbols(self, selectorString, value):
        """ GetLaaDownlinkNumberOfEndingSymbols(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXLaaDownlinkNumberOfEndingSymbols) """
        pass

    def GetLaaDownlinkStartingSymbol(self, selectorString, value):
        """ GetLaaDownlinkStartingSymbol(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXLaaDownlinkStartingSymbol) """
        pass

    def GetLaaNumberOfSubframes(self, selectorString, value):
        """ GetLaaNumberOfSubframes(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetLaaStartingSubframe(self, selectorString, value):
        """ GetLaaStartingSubframe(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetLaaUplinkEndingSymbol(self, selectorString, value):
        """ GetLaaUplinkEndingSymbol(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXLaaUplinkEndingSymbol) """
        pass

    def GetLaaUplinkStartPosition(self, selectorString, value):
        """ GetLaaUplinkStartPosition(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXLaaUplinkStartPosition) """
        pass

    def GetNBIoTUplinkSubcarrierSpacing(self, selectorString, value):
        """ GetNBIoTUplinkSubcarrierSpacing(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXNBIoTUplinkSubcarrierSpacing) """
        pass

    def GetNCellId(self, selectorString, value):
        """ GetNCellId(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschDmrsBaseSequenceIndex(self, selectorString, value):
        """ GetNPuschDmrsBaseSequenceIndex(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschDmrsBaseSequenceMode(self, selectorString, value):
        """ GetNPuschDmrsBaseSequenceMode(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXNPuschDmrsBaseSequenceMode) """
        pass

    def GetNPuschDmrsCyclicShift(self, selectorString, value):
        """ GetNPuschDmrsCyclicShift(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschDmrsDeltaSequenceShift(self, selectorString, value):
        """ GetNPuschDmrsDeltaSequenceShift(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschDmrsGroupHoppingEnabled(self, selectorString, value):
        """ GetNPuschDmrsGroupHoppingEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXNPuschDmrsGroupHoppingEnabled) """
        pass

    def GetNPuschFormat(self, selectorString, value):
        """ GetNPuschFormat(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschModulationType(self, selectorString, value):
        """ GetNPuschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXNPuschModulationType) """
        pass

    def GetNPuschNumberOfTones(self, selectorString, value):
        """ GetNPuschNumberOfTones(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschStartingSlot(self, selectorString, value):
        """ GetNPuschStartingSlot(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNPuschToneOffset(self, selectorString, value):
        """ GetNPuschToneOffset(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfComponentCarriers(self, selectorString, value):
        """ GetNumberOfComponentCarriers(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfPdschChannels(self, selectorString, value):
        """ GetNumberOfPdschChannels(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPbchPower(self, selectorString, value):
        """ GetPbchPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPcfichCfi(self, selectorString, value):
        """ GetPcfichCfi(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPcfichPower(self, selectorString, value):
        """ GetPcfichPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPdcchPower(self, selectorString, value):
        """ GetPdcchPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPdschCW0ModulationType(self, selectorString, value):
        """ GetPdschCW0ModulationType(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXUserDefinedPdschCW0ModulationType) """
        pass

    def GetPdschPower(self, selectorString, value):
        """ GetPdschPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPdschResourceBlockAllocation(self, selectorString, value):
        """ GetPdschResourceBlockAllocation(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, str) """
        pass

    def GetPhichDuration(self, selectorString, value):
        """ GetPhichDuration(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDownlinkUserDefinedPhichDuration) """
        pass

    def GetPhichPower(self, selectorString, value):
        """ GetPhichPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPhichResource(self, selectorString, value):
        """ GetPhichResource(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXDownlinkUserDefinedPhichResource) """
        pass

    def GetPsschModulationType(self, selectorString, value):
        """ GetPsschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXPsschModulationType) """
        pass

    def GetPsschNumberOfResourceBlocks(self, selectorString, value):
        """ GetPsschNumberOfResourceBlocks(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPsschPower(self, selectorString, value):
        """ GetPsschPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPsschResourceBlockOffset(self, selectorString, value):
        """ GetPsschResourceBlockOffset(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPssPower(self, selectorString, value):
        """ GetPssPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPuschCyclicShiftField(self, selectorString, value):
        """ GetPuschCyclicShiftField(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschDeltaSequenceShift(self, selectorString, value):
        """ GetPuschDeltaSequenceShift(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschModulationType(self, selectorString, value):
        """ GetPuschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXPuschModulationType) """
        pass

    def GetPuschNDmrs1(self, selectorString, value):
        """ GetPuschNDmrs1(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschNDmrs2(self, selectorString, value):
        """ GetPuschNDmrs2(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschNumberOfResourceBlockClusters(self, selectorString, value):
        """ GetPuschNumberOfResourceBlockClusters(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschNumberOfResourceBlocks(self, selectorString, value):
        """ GetPuschNumberOfResourceBlocks(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetPuschPower(self, selectorString, value):
        """ GetPuschPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetPuschResourceBlockOffset(self, selectorString, value):
        """ GetPuschResourceBlockOffset(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSpacingType(self, selectorString, value):
        """ GetSpacingType(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXComponentCarrierSpacingType) """
        pass

    def GetSrsbHop(self, selectorString, value):
        """ GetSrsbHop(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsBSrs(self, selectorString, value):
        """ GetSrsBSrs(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsCSrs(self, selectorString, value):
        """ GetSrsCSrs(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsEnabled(self, selectorString, value):
        """ GetSrsEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXSrsEnabled) """
        pass

    def GetSrsISrs(self, selectorString, value):
        """ GetSrsISrs(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrskTC(self, selectorString, value):
        """ GetSrskTC(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsMaximumUpPtsEnabled(self, selectorString, value):
        """ GetSrsMaximumUpPtsEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXSrsMaximumUpPtsEnabled) """
        pass

    def GetSrsnRrc(self, selectorString, value):
        """ GetSrsnRrc(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsnSrsCS(self, selectorString, value):
        """ GetSrsnSrsCS(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsPower(self, selectorString, value):
        """ GetSrsPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetSrsSubframe1NRA(self, selectorString, value):
        """ GetSrsSubframe1NRA(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsSubframe6NRA(self, selectorString, value):
        """ GetSrsSubframe6NRA(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSrsSubframeConfiguration(self, selectorString, value):
        """ GetSrsSubframeConfiguration(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, int) """
        pass

    def GetSssPower(self, selectorString, value):
        """ GetSssPower(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, float) """
        pass

    def GetUplinkGroupHoppingEnabled(self, selectorString, value):
        """ GetUplinkGroupHoppingEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXUplinkGroupHoppingEnabled) """
        pass

    def GetUplinkSequenceHoppingEnabled(self, selectorString, value):
        """ GetUplinkSequenceHoppingEnabled(self: RFmxLteMXComponentCarrier, selectorString: str) -> (int, RFmxLteMXUplinkSequenceHoppingEnabled) """
        pass

    def SetAutoControlChannelPowerDetectionEnabled(self, selectorString, value):
        """ SetAutoControlChannelPowerDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXAutoControlChannelPowerDetectionEnabled) -> int """
        pass

    def SetAutoNPuschChannelDetectionEnabled(self, selectorString, value):
        """ SetAutoNPuschChannelDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXAutoNPuschChannelDetectionEnabled) -> int """
        pass

    def SetAutoPcfichCfiDetectionEnabled(self, selectorString, value):
        """ SetAutoPcfichCfiDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXAutoPcfichCfiDetectionEnabled) -> int """
        pass

    def SetAutoPdschChannelDetectionEnabled(self, selectorString, value):
        """ SetAutoPdschChannelDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXAutoPdschChannelDetectionEnabled) -> int """
        pass

    def SetAutoResourceBlockDetectionEnabled(self, selectorString, value):
        """ SetAutoResourceBlockDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXAutoResourceBlockDetectionEnabled) -> int """
        pass

    def SetBandwidth(self, selectorString, value):
        """ SetBandwidth(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetCellId(self, selectorString, value):
        """ SetCellId(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetComponentCarrierAtCenterFrequency(self, selectorString, value):
        """ SetComponentCarrierAtCenterFrequency(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetCyclicPrefixMode(self, selectorString, value):
        """ SetCyclicPrefixMode(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXCyclicPrefixMode) -> int """
        pass

    def SetDmrsOccEnabled(self, selectorString, value):
        """ SetDmrsOccEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDmrsOccEnabled) -> int """
        pass

    def SetDownlinkAutoCellIDDetectionEnabled(self, selectorString, value):
        """ SetDownlinkAutoCellIDDetectionEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDownlinkAutoCellIDDetectionEnabled) -> int """
        pass

    def SetDownlinkChannelConfigurationMode(self, selectorString, value):
        """ SetDownlinkChannelConfigurationMode(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDownlinkChannelConfigurationMode) -> int """
        pass

    def SetDownlinkNumberOfSubframes(self, selectorString, value):
        """ SetDownlinkNumberOfSubframes(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetDownlinkTestModel(self, selectorString, value):
        """ SetDownlinkTestModel(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDownlinkTestModel) -> int """
        pass

    def SetDownlinkUserDefinedCellSpecificRatio(self, selectorString, value):
        """ SetDownlinkUserDefinedCellSpecificRatio(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDownlinkUserDefinedRatio) -> int """
        pass

    def SetEmtcAnalysisEnabled(self, selectorString, value):
        """ SetEmtcAnalysisEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXEmtcAnalysisEnabled) -> int """
        pass

    def SetFrequency(self, selectorString, value):
        """ SetFrequency(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetLaaDownlinkNumberOfEndingSymbols(self, selectorString, value):
        """ SetLaaDownlinkNumberOfEndingSymbols(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXLaaDownlinkNumberOfEndingSymbols) -> int """
        pass

    def SetLaaDownlinkStartingSymbol(self, selectorString, value):
        """ SetLaaDownlinkStartingSymbol(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXLaaDownlinkStartingSymbol) -> int """
        pass

    def SetLaaNumberOfSubframes(self, selectorString, value):
        """ SetLaaNumberOfSubframes(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetLaaStartingSubframe(self, selectorString, value):
        """ SetLaaStartingSubframe(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetLaaUplinkEndingSymbol(self, selectorString, value):
        """ SetLaaUplinkEndingSymbol(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXLaaUplinkEndingSymbol) -> int """
        pass

    def SetLaaUplinkStartPosition(self, selectorString, value):
        """ SetLaaUplinkStartPosition(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXLaaUplinkStartPosition) -> int """
        pass

    def SetNBIoTUplinkSubcarrierSpacing(self, selectorString, value):
        """ SetNBIoTUplinkSubcarrierSpacing(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXNBIoTUplinkSubcarrierSpacing) -> int """
        pass

    def SetNCellId(self, selectorString, value):
        """ SetNCellId(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschDmrsBaseSequenceIndex(self, selectorString, value):
        """ SetNPuschDmrsBaseSequenceIndex(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschDmrsBaseSequenceMode(self, selectorString, value):
        """ SetNPuschDmrsBaseSequenceMode(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXNPuschDmrsBaseSequenceMode) -> int """
        pass

    def SetNPuschDmrsCyclicShift(self, selectorString, value):
        """ SetNPuschDmrsCyclicShift(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschDmrsDeltaSequenceShift(self, selectorString, value):
        """ SetNPuschDmrsDeltaSequenceShift(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschDmrsGroupHoppingEnabled(self, selectorString, value):
        """ SetNPuschDmrsGroupHoppingEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXNPuschDmrsGroupHoppingEnabled) -> int """
        pass

    def SetNPuschFormat(self, selectorString, value):
        """ SetNPuschFormat(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschModulationType(self, selectorString, value):
        """ SetNPuschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXNPuschModulationType) -> int """
        pass

    def SetNPuschNumberOfTones(self, selectorString, value):
        """ SetNPuschNumberOfTones(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschStartingSlot(self, selectorString, value):
        """ SetNPuschStartingSlot(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNPuschToneOffset(self, selectorString, value):
        """ SetNPuschToneOffset(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfComponentCarriers(self, selectorString, value):
        """ SetNumberOfComponentCarriers(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfPdschChannels(self, selectorString, value):
        """ SetNumberOfPdschChannels(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPbchPower(self, selectorString, value):
        """ SetPbchPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPcfichCfi(self, selectorString, value):
        """ SetPcfichCfi(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPcfichPower(self, selectorString, value):
        """ SetPcfichPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPdcchPower(self, selectorString, value):
        """ SetPdcchPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPdschCW0ModulationType(self, selectorString, value):
        """ SetPdschCW0ModulationType(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXUserDefinedPdschCW0ModulationType) -> int """
        pass

    def SetPdschPower(self, selectorString, value):
        """ SetPdschPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPdschResourceBlockAllocation(self, selectorString, value):
        """ SetPdschResourceBlockAllocation(self: RFmxLteMXComponentCarrier, selectorString: str, value: str) -> int """
        pass

    def SetPhichDuration(self, selectorString, value):
        """ SetPhichDuration(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDownlinkUserDefinedPhichDuration) -> int """
        pass

    def SetPhichPower(self, selectorString, value):
        """ SetPhichPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPhichResource(self, selectorString, value):
        """ SetPhichResource(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXDownlinkUserDefinedPhichResource) -> int """
        pass

    def SetPsschModulationType(self, selectorString, value):
        """ SetPsschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXPsschModulationType) -> int """
        pass

    def SetPsschNumberOfResourceBlocks(self, selectorString, value):
        """ SetPsschNumberOfResourceBlocks(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPsschPower(self, selectorString, value):
        """ SetPsschPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPsschResourceBlockOffset(self, selectorString, value):
        """ SetPsschResourceBlockOffset(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPssPower(self, selectorString, value):
        """ SetPssPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPuschCyclicShiftField(self, selectorString, value):
        """ SetPuschCyclicShiftField(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschDeltaSequenceShift(self, selectorString, value):
        """ SetPuschDeltaSequenceShift(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschModulationType(self, selectorString, value):
        """ SetPuschModulationType(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXPuschModulationType) -> int """
        pass

    def SetPuschNDmrs1(self, selectorString, value):
        """ SetPuschNDmrs1(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschNDmrs2(self, selectorString, value):
        """ SetPuschNDmrs2(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschNumberOfResourceBlockClusters(self, selectorString, value):
        """ SetPuschNumberOfResourceBlockClusters(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschNumberOfResourceBlocks(self, selectorString, value):
        """ SetPuschNumberOfResourceBlocks(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetPuschPower(self, selectorString, value):
        """ SetPuschPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetPuschResourceBlockOffset(self, selectorString, value):
        """ SetPuschResourceBlockOffset(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSpacingType(self, selectorString, value):
        """ SetSpacingType(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXComponentCarrierSpacingType) -> int """
        pass

    def SetSrsbHop(self, selectorString, value):
        """ SetSrsbHop(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsBSrs(self, selectorString, value):
        """ SetSrsBSrs(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsCSrs(self, selectorString, value):
        """ SetSrsCSrs(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsEnabled(self, selectorString, value):
        """ SetSrsEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXSrsEnabled) -> int """
        pass

    def SetSrsISrs(self, selectorString, value):
        """ SetSrsISrs(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrskTC(self, selectorString, value):
        """ SetSrskTC(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsMaximumUpPtsEnabled(self, selectorString, value):
        """ SetSrsMaximumUpPtsEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXSrsMaximumUpPtsEnabled) -> int """
        pass

    def SetSrsnRrc(self, selectorString, value):
        """ SetSrsnRrc(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsnSrsCS(self, selectorString, value):
        """ SetSrsnSrsCS(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsPower(self, selectorString, value):
        """ SetSrsPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetSrsSubframe1NRA(self, selectorString, value):
        """ SetSrsSubframe1NRA(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsSubframe6NRA(self, selectorString, value):
        """ SetSrsSubframe6NRA(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSrsSubframeConfiguration(self, selectorString, value):
        """ SetSrsSubframeConfiguration(self: RFmxLteMXComponentCarrier, selectorString: str, value: int) -> int """
        pass

    def SetSssPower(self, selectorString, value):
        """ SetSssPower(self: RFmxLteMXComponentCarrier, selectorString: str, value: float) -> int """
        pass

    def SetUplinkGroupHoppingEnabled(self, selectorString, value):
        """ SetUplinkGroupHoppingEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXUplinkGroupHoppingEnabled) -> int """
        pass

    def SetUplinkSequenceHoppingEnabled(self, selectorString, value):
        """ SetUplinkSequenceHoppingEnabled(self: RFmxLteMXComponentCarrier, selectorString: str, value: RFmxLteMXUplinkSequenceHoppingEnabled) -> int """
        pass


class RFmxLteMXComponentCarrierSpacingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXComponentCarrierSpacingType, values: Minimum (1), Nominal (0), User (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Minimum = None
    Nominal = None
    User = None
    value__ = None


class RFmxLteMXConstants(object):
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


class RFmxLteMXCyclicPrefixMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXCyclicPrefixMode, values: Extended (1), Normal (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXDigitalEdgeTriggerEdge(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDigitalEdgeTriggerEdge, values: Falling (1), Rising (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXDmrsOccEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDmrsOccEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXDownlinkAutoCellIDDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDownlinkAutoCellIDDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXDownlinkChannelConfigurationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDownlinkChannelConfigurationMode, values: TestModel (2), UserDefined (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXDownlinkTestModel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDownlinkTestModel, values: TM1_1 (0), TM1_2 (1), TM2 (2), TM2A (3), TM3_1 (4), TM3_1A (7), TM3_2 (5), TM3_3 (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    TM2A = None
    TM3_1 = None
    TM3_1A = None
    TM3_2 = None
    TM3_3 = None
    value__ = None


class RFmxLteMXDownlinkUserDefinedPhichDuration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDownlinkUserDefinedPhichDuration, values: Normal (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXDownlinkUserDefinedPhichResource(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDownlinkUserDefinedPhichResource, values: Half (1), One (2), OneSixth (0), Two (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Half = None
    One = None
    OneSixth = None
    Two = None
    value__ = None


class RFmxLteMXDownlinkUserDefinedRatio(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDownlinkUserDefinedRatio, values: PB0 (0), PB1 (1), PB2 (2), PB3 (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PB0 = None
    PB1 = None
    PB2 = None
    PB3 = None
    value__ = None


class RFmxLteMXDuplexScheme(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXDuplexScheme, values: Fdd (0), Laa (2), Tdd (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Laa = None
    Tdd = None
    value__ = None


class RFmxLteMXEmtcAnalysisEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXEmtcAnalysisEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXeNodeBCategory(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXeNodeBCategory, values: HomeBaseStation (4), LocalAreaBaseStation (3), MediumRangeBaseStation (5), WideAreaBaseStationCategoryA (0), WideAreaBaseStationCategoryBOption1 (1), WideAreaBaseStationCategoryBOption2 (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HomeBaseStation = None
    LocalAreaBaseStation = None
    MediumRangeBaseStation = None
    value__ = None
    WideAreaBaseStationCategoryA = None
    WideAreaBaseStationCategoryBOption1 = None
    WideAreaBaseStationCategoryBOption2 = None


class RFmxLteMXIQPowerEdgeTriggerLevelType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXIQPowerEdgeTriggerLevelType, values: Absolute (1), Relative (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXIQPowerEdgeTriggerSlope(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXIQPowerEdgeTriggerSlope, values: Falling (1), Rising (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXLaaDownlinkNumberOfEndingSymbols(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXLaaDownlinkNumberOfEndingSymbols, values: EndingSymbols10 (10), EndingSymbols11 (11), EndingSymbols12 (12), EndingSymbols14 (14), EndingSymbols3 (3), EndingSymbols6 (6), EndingSymbols9 (9) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EndingSymbols10 = None
    EndingSymbols11 = None
    EndingSymbols12 = None
    EndingSymbols14 = None
    EndingSymbols3 = None
    EndingSymbols6 = None
    EndingSymbols9 = None
    value__ = None


class RFmxLteMXLaaDownlinkStartingSymbol(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXLaaDownlinkStartingSymbol, values: StartingSymbol0 (0), StartingSymbol7 (7) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    StartingSymbol0 = None
    StartingSymbol7 = None
    value__ = None


class RFmxLteMXLaaUplinkEndingSymbol(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXLaaUplinkEndingSymbol, values: EndingSymbol12 (12), EndingSymbol13 (13) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    EndingSymbol12 = None
    EndingSymbol13 = None
    value__ = None


class RFmxLteMXLaaUplinkStartPosition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXLaaUplinkStartPosition, values: StartPosition00 (0), StartPosition01 (1), StartPosition10 (2), StartPosition11 (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    StartPosition00 = None
    StartPosition01 = None
    StartPosition10 = None
    StartPosition11 = None
    value__ = None


class RFmxLteMXLimitedConfigurationChange(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXLimitedConfigurationChange, values: Disabled (0), Frequency (2), FrequencyAndReferenceLevel (4), NoChange (1), ReferenceLevel (3), SelectedPortsFrequencyAndReferenceLevel (5) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXLinkDirection(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXLinkDirection, values: Downlink (0), Sidelink (2), Uplink (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Sidelink = None
    Uplink = None
    value__ = None


class RFmxLteMXMeasurementTypes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RFmxLteMXMeasurementTypes, values: Acp (1), Chp (2), ModAcc (4), Obw (8), Pvt (32), Sem (16), SlotPhase (64), SlotPower (128) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    SlotPhase = None
    SlotPower = None
    value__ = None


class RFmxLteMXMiConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXMiConfiguration, values: Standard (1), TestModel (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    TestModel = None
    value__ = None


class RFmxLteMXModAcc(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXModAcc) -> RFmxLteMXModAccConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXModAcc) -> RFmxLteMXModAccResults

"""



class RFmxLteMXModAccAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccChannelEstimationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccChannelEstimationType, values: Reference (0), ReferenceAndData (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccCommonClockSourceEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccCommonClockSourceEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxLteMXModAccConfiguration, selectorString: str, averagingEnabled: RFmxLteMXModAccAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureCommonClockSourceEnabled(self, selectorString, commonClockSourceEnabled):
        """ ConfigureCommonClockSourceEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, commonClockSourceEnabled: RFmxLteMXModAccCommonClockSourceEnabled) -> int """
        pass

    def ConfigureEvmUnit(self, selectorString, evmUnit):
        """ ConfigureEvmUnit(self: RFmxLteMXModAccConfiguration, selectorString: str, evmUnit: RFmxLteMXModAccEvmUnit) -> int """
        pass

    def ConfigureFftWindowOffset(self, selectorString, fftWindowOffset):
        """ ConfigureFftWindowOffset(self: RFmxLteMXModAccConfiguration, selectorString: str, fftWindowOffset: float) -> int """
        pass

    def ConfigureFftWindowPosition(self, selectorString, fftWindowType, fftWindowOffset, fftWindowLength):
        """ ConfigureFftWindowPosition(self: RFmxLteMXModAccConfiguration, selectorString: str, fftWindowType: RFmxLteMXModAccFftWindowType, fftWindowOffset: float, fftWindowLength: float) -> int """
        pass

    def ConfigureInBandEmissionMaskType(self, selectorString, inBandEmissionMaskType):
        """ ConfigureInBandEmissionMaskType(self: RFmxLteMXModAccConfiguration, selectorString: str, inBandEmissionMaskType: RFmxLteMXModAccInBandEmissionMaskType) -> int """
        pass

    def ConfigureSynchronizationModeAndInterval(self, selectorString, synchronizationMode, measurementOffset, measurementLength):
        """ ConfigureSynchronizationModeAndInterval(self: RFmxLteMXModAccConfiguration, selectorString: str, synchronizationMode: RFmxLteMXModAccSynchronizationMode, measurementOffset: int, measurementLength: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccAveragingEnabled) """
        pass

    def GetChannelEstimationType(self, selectorString, value):
        """ GetChannelEstimationType(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccChannelEstimationType) """
        pass

    def GetCommonClockSourceEnabled(self, selectorString, value):
        """ GetCommonClockSourceEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccCommonClockSourceEnabled) """
        pass

    def GetEvmUnit(self, selectorString, value):
        """ GetEvmUnit(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccEvmUnit) """
        pass

    def GetEvmWithExclusionPeriodEnabled(self, selectorString, value):
        """ GetEvmWithExclusionPeriodEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccEvmWithExclusionPeriodEnabled) """
        pass

    def GetFftWindowLength(self, selectorString, value):
        """ GetFftWindowLength(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindowOffset(self, selectorString, value):
        """ GetFftWindowOffset(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetFftWindowType(self, selectorString, value):
        """ GetFftWindowType(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccFftWindowType) """
        pass

    def GetInBandEmissionMaskType(self, selectorString, value):
        """ GetInBandEmissionMaskType(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccInBandEmissionMaskType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementLength(self, selectorString, value):
        """ GetMeasurementLength(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMulticarrierFilterEnabled(self, selectorString, value):
        """ GetMulticarrierFilterEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccMulticarrierFilterEnabled) """
        pass

    def GetMultiCarrierFilterEnabled(self, selectorString, value):
        """ GetMultiCarrierFilterEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccMulticarrierFilterEnabled) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSpectralFlatnessCondition(self, selectorString, value):
        """ GetSpectralFlatnessCondition(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccSpectralFlatnessCondition) """
        pass

    def GetSpectrumInverted(self, selectorString, value):
        """ GetSpectrumInverted(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccSpectrumInverted) """
        pass

    def GetSynchronizationMode(self, selectorString, value):
        """ GetSynchronizationMode(self: RFmxLteMXModAccConfiguration, selectorString: str) -> (int, RFmxLteMXModAccSynchronizationMode) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxLteMXModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccAveragingEnabled) -> int """
        pass

    def SetChannelEstimationType(self, selectorString, value):
        """ SetChannelEstimationType(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccChannelEstimationType) -> int """
        pass

    def SetCommonClockSourceEnabled(self, selectorString, value):
        """ SetCommonClockSourceEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccCommonClockSourceEnabled) -> int """
        pass

    def SetEvmUnit(self, selectorString, value):
        """ SetEvmUnit(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccEvmUnit) -> int """
        pass

    def SetEvmWithExclusionPeriodEnabled(self, selectorString, value):
        """ SetEvmWithExclusionPeriodEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccEvmWithExclusionPeriodEnabled) -> int """
        pass

    def SetFftWindowLength(self, selectorString, value):
        """ SetFftWindowLength(self: RFmxLteMXModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindowOffset(self, selectorString, value):
        """ SetFftWindowOffset(self: RFmxLteMXModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetFftWindowType(self, selectorString, value):
        """ SetFftWindowType(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccFftWindowType) -> int """
        pass

    def SetInBandEmissionMaskType(self, selectorString, value):
        """ SetInBandEmissionMaskType(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccInBandEmissionMaskType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementLength(self, selectorString, value):
        """ SetMeasurementLength(self: RFmxLteMXModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxLteMXModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMulticarrierFilterEnabled(self, selectorString, value):
        """ SetMulticarrierFilterEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccMulticarrierFilterEnabled) -> int """
        pass

    def SetMultiCarrierFilterEnabled(self, selectorString, value):
        """ SetMultiCarrierFilterEnabled(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccMulticarrierFilterEnabled) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxLteMXModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSpectralFlatnessCondition(self, selectorString, value):
        """ SetSpectralFlatnessCondition(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccSpectralFlatnessCondition) -> int """
        pass

    def SetSpectrumInverted(self, selectorString, value):
        """ SetSpectrumInverted(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccSpectrumInverted) -> int """
        pass

    def SetSynchronizationMode(self, selectorString, value):
        """ SetSynchronizationMode(self: RFmxLteMXModAccConfiguration, selectorString: str, value: RFmxLteMXModAccSynchronizationMode) -> int """
        pass


class RFmxLteMXModAccEvmUnit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccEvmUnit, values: dB (1), Percentage (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccEvmWithExclusionPeriodEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccEvmWithExclusionPeriodEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccFftWindowType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccFftWindowType, values: Type3GPP (0), TypeCustom (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccInBandEmissionMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccInBandEmissionMaskType, values: Release11Onwards (1), Release8_10 (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Release11Onwards = None
    Release8_10 = None
    value__ = None


class RFmxLteMXModAccMulticarrierFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccMulticarrierFilterEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccResults(RFmxLteMXSubObject):
    # no doc
    def FetchCompositeEvm(self, selectorString, timeout, meanRmsCompositeEvm, maximumPeakCompositeEvm, meanFrequencyError, peakCompositeEvmSymbolIndex, peakCompositeEvmSubcarrierIndex, peakCompositeEvmSlotIndex):
        """ FetchCompositeEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, int, int, int) """
        pass

    def FetchCompositeEvmArray(self, selectorString, timeout, meanRmsCompositeEvm, maximumPeakCompositeEvm, meanFrequencyError, peakCompositeEvmSymbolIndex, peakCompositeEvmSubcarrierIndex, peakCompositeEvmSlotIndex):
        """ FetchCompositeEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsCompositeEvm: Array[float], maximumPeakCompositeEvm: Array[float], meanFrequencyError: Array[float], peakCompositeEvmSymbolIndex: Array[int], peakCompositeEvmSubcarrierIndex: Array[int], peakCompositeEvmSlotIndex: Array[int]) -> (int, Array[float], Array[float], Array[float], Array[int], Array[int], Array[int]) """
        pass

    def FetchCompositeMagnitudeAndPhaseError(self, selectorString, timeout, meanRmsCompositeMagnitudeError, maximumPeakCompositeMagnitudeError, meanRmsCompositePhaseError, maximumPeakCompositePhaseError):
        """ FetchCompositeMagnitudeAndPhaseError(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchCompositeMagnitudeAndPhaseErrorArray(self, selectorString, timeout, meanRmsCompositeMagnitudeError, maximumPeakCompositeMagnitudeError, meanRmsCompositePhaseError, maximumPeakCompositePhaseError):
        """ FetchCompositeMagnitudeAndPhaseErrorArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsCompositeMagnitudeError: Array[float], maximumPeakCompositeMagnitudeError: Array[float], meanRmsCompositePhaseError: Array[float], maximumPeakCompositePhaseError: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchCsrsConstellation(self, selectorString, timeout, csrsConstellation):
        """ FetchCsrsConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, csrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchCsrsEvm(self, selectorString, timeout, meanRmsCsrsEvm):
        """ FetchCsrsEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchCsrsEvmArray(self, selectorString, timeout, meanRmsCsrsEvm):
        """ FetchCsrsEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsCsrsEvm: Array[float]) -> (int, Array[float]) """
        pass

    def FetchDownlinkDetectedCellID(self, selectorString, timeout, detectedCellID):
        """ FetchDownlinkDetectedCellID(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, int) """
        pass

    def FetchDownlinkDetectedCellIDArray(self, selectorString, timeout, detectedCellID):
        """ FetchDownlinkDetectedCellIDArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, detectedCellID: Array[int]) -> (int, Array[int]) """
        pass

    def FetchDownlinkPbchConstellation(self, selectorString, timeout, pbchConstellation):
        """ FetchDownlinkPbchConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, pbchConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchDownlinkPcfichConstellation(self, selectorString, timeout, pcfichConstellation):
        """ FetchDownlinkPcfichConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, pcfichConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchDownlinkPdcchConstellation(self, selectorString, timeout, pdcchConstellation):
        """ FetchDownlinkPdcchConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, pdcchConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchDownlinkPhichConstellation(self, selectorString, timeout, phichConstellation):
        """ FetchDownlinkPhichConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, phichConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchDownlinkTransmitPower(self, selectorString, timeout, RSTransmitPower, ofdmSymbolTransmitPower, reserved1, reserved2):
        """ FetchDownlinkTransmitPower(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchDownlinkTransmitPowerArray(self, selectorString, timeout, RSTransmitPower, ofdmSymbolTransmitPower, reserved1, reserved2):
        """ FetchDownlinkTransmitPowerArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, RSTransmitPower: Array[float], ofdmSymbolTransmitPower: Array[float], reserved1: Array[float], reserved2: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchEvmHighPerSymbolTrace(self, selectorString, timeout, evmHighPerSymbol):
        """ FetchEvmHighPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, evmHighPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchEvmLowPerSymbolTrace(self, selectorString, timeout, evmLowPerSymbol):
        """ FetchEvmLowPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, evmLowPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchEvmPerSlotTrace(self, selectorString, timeout, rmsEvmPerSlot):
        """ FetchEvmPerSlotTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, rmsEvmPerSlot: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchEvmPerSubcarrierTrace(self, selectorString, timeout, meanRmsEvmPerSubcarrier):
        """ FetchEvmPerSubcarrierTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsEvmPerSubcarrier: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchEvmPerSymbolTrace(self, selectorString, timeout, rmsEvmPerSymbol):
        """ FetchEvmPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, rmsEvmPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchInBandEmissionMargin(self, selectorString, timeout, inBandEmissionMargin):
        """ FetchInBandEmissionMargin(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchInBandEmissionMarginArray(self, selectorString, timeout, inBandEmissionMargin):
        """ FetchInBandEmissionMarginArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, inBandEmissionMargin: Array[float]) -> (int, Array[float]) """
        pass

    def FetchInBandEmissionTrace(self, selectorString, timeout, inBandEmission, inBandEmissionMask):
        """ FetchInBandEmissionTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, inBandEmission: AnalogWaveform[Single], inBandEmissionMask: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchIQImpairments(self, selectorString, timeout, meanIQOriginOffset, meanIQGainImbalance, meanIQQuadratureError):
        """ FetchIQImpairments(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchIQImpairmentsArray(self, selectorString, timeout, meanIQOriginOffset, meanIQGainImbalance, meanIQQuadratureError):
        """ FetchIQImpairmentsArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanIQOriginOffset: Array[float], meanIQGainImbalance: Array[float], meanIQQuadratureError: Array[float]) -> (int, Array[float], Array[float], Array[float]) """
        pass

    def FetchMaximumEvmPerSlotTrace(self, selectorString, timeout, maximumEvmPerSlot):
        """ FetchMaximumEvmPerSlotTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, maximumEvmPerSlot: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchMaximumEvmPerSubcarrierTrace(self, selectorString, timeout, maximumEvmPerSubcarrier):
        """ FetchMaximumEvmPerSubcarrierTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, maximumEvmPerSubcarrier: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchMaximumEvmPerSymbolTrace(self, selectorString, timeout, maximumEvmPerSymbol):
        """ FetchMaximumEvmPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, maximumEvmPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchMaximumMagnitudeErrorPerSymbolTrace(self, selectorString, timeout, maximumMagnitudeErrorPerSymbol):
        """ FetchMaximumMagnitudeErrorPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, maximumMagnitudeErrorPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchMaximumPhaseErrorPerSymbolTrace(self, selectorString, timeout, maximumPhaseErrorPerSymbol):
        """ FetchMaximumPhaseErrorPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, maximumPhaseErrorPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchNPuschConstellationTrace(self, selectorString, timeout, dataConstellation, DmrsConstellation):
        """ FetchNPuschConstellationTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, dataConstellation: Array[ComplexSingle], DmrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle], Array[ComplexSingle]) """
        pass

    def FetchNPuschDataEvm(self, selectorString, timeout, nPuschMeanRmsDataEvm, nPuschMaximumPeakDataEvm):
        """ FetchNPuschDataEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchNPuschDmrsEvm(self, selectorString, timeout, nPuschMeanRMSDmrsEvm, nPuschMaximumPeakDmrsEvm):
        """ FetchNPuschDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchNPuschSymbolPower(self, selectorString, timeout, nPuschMeanDataPower, nPuschMeanDmrsPower):
        """ FetchNPuschSymbolPower(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPdsch1024QamConstellation(self, selectorString, timeout, qam1024Constellation):
        """ FetchPdsch1024QamConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, qam1024Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdsch1024QamEvm(self, selectorString, timeout, meanRms1024QamEvm):
        """ FetchPdsch1024QamEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchPdsch1024QamEvmArray(self, selectorString, timeout, meanRms1024QamEvm):
        """ FetchPdsch1024QamEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRms1024QamEvm: Array[float]) -> (int, Array[float]) """
        pass

    def FetchPdsch16QamConstellation(self, selectorString, timeout, qam16Constellation):
        """ FetchPdsch16QamConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, qam16Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdsch256QamConstellation(self, selectorString, timeout, qam256Constellation):
        """ FetchPdsch256QamConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, qam256Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdsch64QamConstellation(self, selectorString, timeout, qam64Constellation):
        """ FetchPdsch64QamConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, qam64Constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPdschEvm(self, selectorString, timeout, meanRmsEvm, meanRmsQpskEvm, meanRms16QamEvm, meanRms64QamEvm, meanRms256QamEvm):
        """ FetchPdschEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchPdschEvmArray(self, selectorString, timeout, meanRmsEvm, meanRmsQpskEvm, meanRms16QamEvm, meanRms64QamEvm, meanRms256QamEvm):
        """ FetchPdschEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsEvm: Array[float], meanRmsQpskEvm: Array[float], meanRms16QamEvm: Array[float], meanRms64QamEvm: Array[float], meanRms256QamEvm: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchPdschQpskConstellation(self, selectorString, timeout, qpskConstellation):
        """ FetchPdschQpskConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, qpskConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPsschConstellationTrace(self, selectorString, timeout, dataConstellation, dmrsConstellation):
        """ FetchPsschConstellationTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, dataConstellation: Array[ComplexSingle], dmrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle], Array[ComplexSingle]) """
        pass

    def FetchPsschDataEvm(self, selectorString, timeout, psschMeanRmsDataEvm, psschMaximumPeakDataEvm):
        """ FetchPsschDataEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPsschDataEvmArray(self, selectorString, timeout, psschMeanRmsDataEvm, psschMaximumPeakDataEvm):
        """ FetchPsschDataEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, psschMeanRmsDataEvm: Array[float], psschMaximumPeakDataEvm: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPsschDmrsEvm(self, selectorString, timeout, psschMeanRmsDmrsEvm, psschMaximumPeakDmrsEvm):
        """ FetchPsschDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPsschDmrsEvmArray(self, selectorString, timeout, psschMeanRmsDmrsEvm, psschMaximumPeakDmrsEvm):
        """ FetchPsschDmrsEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, psschMeanRmsDmrsEvm: Array[float], psschMaximumPeakDmrsEvm: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPsschSymbolPower(self, selectorString, timeout, psschMeanDataPower, psschMeanDmrsPower):
        """ FetchPsschSymbolPower(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPsschSymbolPowerArray(self, selectorString, timeout, psschMeanDataPower, psschMeanDmrsPower):
        """ FetchPsschSymbolPowerArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, psschMeanDataPower: Array[float], psschMeanDmrsPower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPuschConstellationTrace(self, selectorString, timeout, dataConstellation, dmrsConstellation):
        """ FetchPuschConstellationTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, dataConstellation: Array[ComplexSingle], dmrsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle], Array[ComplexSingle]) """
        pass

    def FetchPuschDataEvm(self, selectorString, timeout, meanRmsDataEvm, maximumPeakDataEvm):
        """ FetchPuschDataEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPuschDataEvmArray(self, selectorString, timeout, meanRmsDataEvm, maximumPeakDataEvm):
        """ FetchPuschDataEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsDataEvm: Array[float], maximumPeakDataEvm: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPuschDemodulatedBits(self, selectorString, timeout, bits):
        """ FetchPuschDemodulatedBits(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, bits: Array[SByte]) -> (int, Array[SByte]) """
        pass

    def FetchPuschDmrsEvm(self, selectorString, timeout, meanRmsDmrsEvm, maximumPeakDmrsEvm):
        """ FetchPuschDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPuschDmrsEvmArray(self, selectorString, timeout, meanRmsDmrsEvm, maximumPeakDmrsEvm):
        """ FetchPuschDmrsEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsDmrsEvm: Array[float], maximumPeakDmrsEvm: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPuschSymbolPower(self, selectorString, timeout, puschMeanDataPower, puschMeanDmrsPower):
        """ FetchPuschSymbolPower(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchPuschSymbolPowerArray(self, selectorString, timeout, puschMeanDataPower, puschMeanDmrsPower):
        """ FetchPuschSymbolPowerArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, puschMeanDataPower: Array[float], puschMeanDmrsPower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchRmsMagnitudeErrorPerSymbolTrace(self, selectorString, timeout, rmsMagnitudeErrorPerSymbol):
        """ FetchRmsMagnitudeErrorPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, rmsMagnitudeErrorPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchRmsPhaseErrorPerSymbolTrace(self, selectorString, timeout, rmsPhaseErrorPerSymbol):
        """ FetchRmsPhaseErrorPerSymbolTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, rmsPhaseErrorPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSpectralFlatness(self, selectorString, timeout, range1MaximumToRange1Minimum, range2MaximumToRange2Minimum, range1MaximumToRange2Minimum, range2MaximumToRange1Minimum):
        """ FetchSpectralFlatness(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchSpectralFlatnessArray(self, selectorString, timeout, range1MaximumToRange1Minimum, range2MaximumToRange2Minimum, range1MaximumToRange2Minimum, range2MaximumToRange1Minimum):
        """ FetchSpectralFlatnessArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, range1MaximumToRange1Minimum: Array[float], range2MaximumToRange2Minimum: Array[float], range1MaximumToRange2Minimum: Array[float], range2MaximumToRange1Minimum: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchSpectralFlatnessTrace(self, selectorString, timeout, spectralFlatness, spectralFlatnessLowerMask, spectralFlatnessUpperMask):
        """ FetchSpectralFlatnessTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, spectralFlatness: Spectrum[Single], spectralFlatnessLowerMask: Spectrum[Single], spectralFlatnessUpperMask: Spectrum[Single]) -> (int, Spectrum[Single], Spectrum[Single], Spectrum[Single]) """
        pass

    def FetchSrsConstellation(self, selectorString, timeout, srsConstellation):
        """ FetchSrsConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, srsConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchSrsEvm(self, selectorString, timeout, meanRmsSrsEvm, meanSrsPower):
        """ FetchSrsEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchSrsEvmArray(self, selectorString, timeout, meanRmsSrsEvm, meanSrsPower):
        """ FetchSrsEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsSrsEvm: Array[float], meanSrsPower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchSubblockInBandEmissionMargin(self, selectorString, timeout, subblockInBandEmissionMargin):
        """ FetchSubblockInBandEmissionMargin(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchSubblockInBandEmissionTrace(self, selectorString, timeout, subblockInBandEmission, subblockInBandEmissionMask, subblockInBandEmissionRBIndices):
        """ FetchSubblockInBandEmissionTrace(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, subblockInBandEmission: Array[float], subblockInBandEmissionMask: Array[float], subblockInBandEmissionRBIndices: Array[float]) -> (int, Array[float], Array[float], Array[float]) """
        pass

    def FetchSubblockIQImpairments(self, selectorString, timeout, subblockMeanIQOriginOffset, subblockMeanIQGainImbalance, subblockMeanIQQuadratureError):
        """ FetchSubblockIQImpairments(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchSynchronizationSignalConstellation(self, selectorString, timeout, sssConstellation, pssConstellation):
        """ FetchSynchronizationSignalConstellation(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, sssConstellation: Array[ComplexSingle], pssConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle], Array[ComplexSingle]) """
        pass

    def FetchSynchronizationSignalEvm(self, selectorString, timeout, meanRmsPssEvm, meanRmsSssEvm):
        """ FetchSynchronizationSignalEvm(self: RFmxLteMXModAccResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchSynchronizationSignalEvmArray(self, selectorString, timeout, meanRmsPssEvm, meanRmsSssEvm):
        """ FetchSynchronizationSignalEvmArray(self: RFmxLteMXModAccResults, selectorString: str, timeout: float, meanRmsPssEvm: Array[float], meanRmsSssEvm: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetDownlinkDetectedCellID(self, selectorString, value):
        """ GetDownlinkDetectedCellID(self: RFmxLteMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetDownlinkOfdmSymbolTransmitPower(self, selectorString, value):
        """ GetDownlinkOfdmSymbolTransmitPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetDownlinkRSTransmitPower(self, selectorString, value):
        """ GetDownlinkRSTransmitPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetInBandEmissionMargin(self, selectorString, value):
        """ GetInBandEmissionMargin(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMaximumPeakCompositeEvm(self, selectorString, value):
        """ GetMaximumPeakCompositeEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMaximumPeakCompositeMagnitudeError(self, selectorString, value):
        """ GetMaximumPeakCompositeMagnitudeError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMaximumPeakCompositePhaseError(self, selectorString, value):
        """ GetMaximumPeakCompositePhaseError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanFrequencyError(self, selectorString, value):
        """ GetMeanFrequencyError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanIQGainImbalance(self, selectorString, value):
        """ GetMeanIQGainImbalance(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanIQOriginOffset(self, selectorString, value):
        """ GetMeanIQOriginOffset(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanQuadratureError(self, selectorString, value):
        """ GetMeanQuadratureError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsCompositeEvm(self, selectorString, value):
        """ GetMeanRmsCompositeEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsCompositeMagnitudeError(self, selectorString, value):
        """ GetMeanRmsCompositeMagnitudeError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsCompositePhaseError(self, selectorString, value):
        """ GetMeanRmsCompositePhaseError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsCsrsEvm(self, selectorString, value):
        """ GetMeanRmsCsrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsPbchEvm(self, selectorString, value):
        """ GetMeanRmsPbchEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsPcfichEvm(self, selectorString, value):
        """ GetMeanRmsPcfichEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsPdcchEvm(self, selectorString, value):
        """ GetMeanRmsPdcchEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsPhichEvm(self, selectorString, value):
        """ GetMeanRmsPhichEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsPssEvm(self, selectorString, value):
        """ GetMeanRmsPssEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsSrsEvm(self, selectorString, value):
        """ GetMeanRmsSrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanRmsSssEvm(self, selectorString, value):
        """ GetMeanRmsSssEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanSrsPower(self, selectorString, value):
        """ GetMeanSrsPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanSymbolClockError(self, selectorString, value):
        """ GetMeanSymbolClockError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetNPuschMaximumPeakDataEvm(self, selectorString, value):
        """ GetNPuschMaximumPeakDataEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetNPuschMaximumPeakDmrsEvm(self, selectorString, value):
        """ GetNPuschMaximumPeakDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetNPuschMeanDataPower(self, selectorString, value):
        """ GetNPuschMeanDataPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetNPuschMeanDmrsPower(self, selectorString, value):
        """ GetNPuschMeanDmrsPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetNPuschMeanRmsDataEvm(self, selectorString, value):
        """ GetNPuschMeanRmsDataEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetNPuschMeanRmsDmrsEvm(self, selectorString, value):
        """ GetNPuschMeanRmsDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschMeanRms1024QamEvm(self, selectorString, value):
        """ GetPdschMeanRms1024QamEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschMeanRms16QamEvm(self, selectorString, value):
        """ GetPdschMeanRms16QamEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschMeanRms256QamEvm(self, selectorString, value):
        """ GetPdschMeanRms256QamEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschMeanRms64QamEvm(self, selectorString, value):
        """ GetPdschMeanRms64QamEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschMeanRmsEvm(self, selectorString, value):
        """ GetPdschMeanRmsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPdschMeanRmsQpskEvm(self, selectorString, value):
        """ GetPdschMeanRmsQpskEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakCompositeEvmSlotIndex(self, selectorString, value):
        """ GetPeakCompositeEvmSlotIndex(self: RFmxLteMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetPeakCompositeEvmSubcarrierIndex(self, selectorString, value):
        """ GetPeakCompositeEvmSubcarrierIndex(self: RFmxLteMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetPeakCompositeEvmSymbolIndex(self, selectorString, value):
        """ GetPeakCompositeEvmSymbolIndex(self: RFmxLteMXModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetPsschMaximumPeakDataEvm(self, selectorString, value):
        """ GetPsschMaximumPeakDataEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPsschMaximumPeakDmrsEvm(self, selectorString, value):
        """ GetPsschMaximumPeakDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPsschMeanDataPower(self, selectorString, value):
        """ GetPsschMeanDataPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPsschMeanDmrsPower(self, selectorString, value):
        """ GetPsschMeanDmrsPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPsschMeanRmsDataEvm(self, selectorString, value):
        """ GetPsschMeanRmsDataEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPsschMeanRmsDmrsEvm(self, selectorString, value):
        """ GetPsschMeanRmsDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschMaximumPeakDataEvm(self, selectorString, value):
        """ GetPuschMaximumPeakDataEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschMaximumPeakDmrsEvm(self, selectorString, value):
        """ GetPuschMaximumPeakDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschMeanDataPower(self, selectorString, value):
        """ GetPuschMeanDataPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschMeanDmrsPower(self, selectorString, value):
        """ GetPuschMeanDmrsPower(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschMeanRmsDataEvm(self, selectorString, value):
        """ GetPuschMeanRmsDataEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPuschMeanRmsDmrsEvm(self, selectorString, value):
        """ GetPuschMeanRmsDmrsEvm(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange1MaximumToRange1Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange1MaximumToRange1Minimum(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange1MaximumToRange2Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange1MaximumToRange2Minimum(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange2MaximumToRange1Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange2MaximumToRange1Minimum(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessRange2MaximumToRange2Minimum(self, selectorString, value):
        """ GetSpectralFlatnessRange2MaximumToRange2Minimum(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockInBandEmissionMargin(self, selectorString, value):
        """ GetSubblockInBandEmissionMargin(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockMeanIQGainImbalance(self, selectorString, value):
        """ GetSubblockMeanIQGainImbalance(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockMeanIQOriginOffset(self, selectorString, value):
        """ GetSubblockMeanIQOriginOffset(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockMeanQuadratureError(self, selectorString, value):
        """ GetSubblockMeanQuadratureError(self: RFmxLteMXModAccResults, selectorString: str) -> (int, float) """
        pass


class RFmxLteMXModAccSpectralFlatnessCondition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccSpectralFlatnessCondition, values: Extreme (1), Normal (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccSpectrumInverted(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccSpectrumInverted, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXModAccSynchronizationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXModAccSynchronizationMode, values: Frame (0), Marker (2), Slot (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Marker = None
    Slot = None
    value__ = None


class RFmxLteMXNBIoTUplinkSubcarrierSpacing(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXNBIoTUplinkSubcarrierSpacing, values: SubcarrierSpacing15kHz (0), SubcarrierSpacing3_75kHz (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SubcarrierSpacing15kHz = None
    SubcarrierSpacing3_75kHz = None
    value__ = None


class RFmxLteMXNPuschDmrsBaseSequenceMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXNPuschDmrsBaseSequenceMode, values: Auto (1), Manual (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXNPuschDmrsGroupHoppingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXNPuschDmrsGroupHoppingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXNPuschModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXNPuschModulationType, values: Bpsk (0), Qpsk (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bpsk = None
    Qpsk = None
    value__ = None


class RFmxLteMXObw(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXObw) -> RFmxLteMXObwConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXObw) -> RFmxLteMXObwResults

"""



class RFmxLteMXObwAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXObwAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXObwAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXObwAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXObwAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXObwAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXObwConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxLteMXObwConfiguration, selectorString: str, averagingEnabled: RFmxLteMXObwAveragingEnabled, averagingCount: int, averagingType: RFmxLteMXObwAveragingType) -> int """
        pass

    def ConfigureRbwFilter(self, selectorString, rbwAuto, rbw, rbwFilterType):
        """ ConfigureRbwFilter(self: RFmxLteMXObwConfiguration, selectorString: str, rbwAuto: RFmxLteMXObwRbwAutoBandwidth, rbw: float, rbwFilterType: RFmxLteMXObwRbwFilterType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxLteMXObwConfiguration, selectorString: str, sweepTimeAuto: RFmxLteMXObwSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, RFmxLteMXObwAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, RFmxLteMXObwAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, RFmxLteMXObwAveragingType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetRbwFilterAutoBandwidth(self, selectorString, value):
        """ GetRbwFilterAutoBandwidth(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, RFmxLteMXObwRbwAutoBandwidth) """
        pass

    def GetRbwFilterBandwidth(self, selectorString, value):
        """ GetRbwFilterBandwidth(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetRbwFilterType(self, selectorString, value):
        """ GetRbwFilterType(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, RFmxLteMXObwRbwFilterType) """
        pass

    def GetSpan(self, selectorString, value):
        """ GetSpan(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, RFmxLteMXObwSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxLteMXObwConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXObwConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxLteMXObwConfiguration, selectorString: str, value: RFmxLteMXObwAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxLteMXObwConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxLteMXObwConfiguration, selectorString: str, value: RFmxLteMXObwAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxLteMXObwConfiguration, selectorString: str, value: RFmxLteMXObwAveragingType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXObwConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxLteMXObwConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetRbwFilterAutoBandwidth(self, selectorString, value):
        """ SetRbwFilterAutoBandwidth(self: RFmxLteMXObwConfiguration, selectorString: str, value: RFmxLteMXObwRbwAutoBandwidth) -> int """
        pass

    def SetRbwFilterBandwidth(self, selectorString, value):
        """ SetRbwFilterBandwidth(self: RFmxLteMXObwConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetRbwFilterType(self, selectorString, value):
        """ SetRbwFilterType(self: RFmxLteMXObwConfiguration, selectorString: str, value: RFmxLteMXObwRbwFilterType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxLteMXObwConfiguration, selectorString: str, value: RFmxLteMXObwSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxLteMXObwConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxLteMXObwRbwAutoBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXObwRbwAutoBandwidth, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXObwRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXObwRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXObwResults(RFmxLteMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, occupiedBandwidth, absolutePower, startFrequency, stopFrequency):
        """ FetchMeasurement(self: RFmxLteMXObwResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum):
        """ FetchSpectrum(self: RFmxLteMXObwResults, selectorString: str, timeout: float, spectrum: Spectrum[Single]) -> (int, Spectrum[Single]) """
        pass

    def GetAbsolutePower(self, selectorString, value):
        """ GetAbsolutePower(self: RFmxLteMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetOccupiedBandwidth(self, selectorString, value):
        """ GetOccupiedBandwidth(self: RFmxLteMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetStartFrequency(self, selectorString, value):
        """ GetStartFrequency(self: RFmxLteMXObwResults, selectorString: str) -> (int, float) """
        pass

    def GetStopFrequency(self, selectorString, value):
        """ GetStopFrequency(self: RFmxLteMXObwResults, selectorString: str) -> (int, float) """
        pass


class RFmxLteMXObwSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXObwSweepTimeAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXPropertyId(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPropertyId, values: AcpAllTracesEnabled (3149857), AcpAmplitudeCorrectionType (3149888), AcpAveragingCount (3149845), AcpAveragingEnabled (3149846), AcpAveragingType (3149848), AcpComponentCarrierIntegrationBandwidth (3149829), AcpConfigurableNumberOfOffsetsEnabled (3149892), AcpEutraOffsetDefinition (3149891), AcpFarIFOutputPowerOffset (3149878), AcpIFOutputPowerOffsetAuto (3149876), AcpMeasurementEnabled (3149824), AcpMeasurementMethod (3149842), AcpNearIFOutputPowerOffset (3149877), AcpNoiseCompensationEnabled (3149856), AcpNumberOfAnalysisThreads (3149844), AcpNumberOfEutraOffsets (3149883), AcpNumberOfGsmOffsets (3149890), AcpNumberOfUtraOffsets (3149882), AcpOffsetFrequency (3149834), AcpOffsetIntegrationBandwidth (3149838), AcpRbwFilterAutoBandwidth (3149851), AcpRbwFilterBandwidth (3149852), AcpRbwFilterType (3149853), AcpResultsComponentCarrierAbsolutePower (3149862), AcpResultsComponentCarrierRelativePower (3149863), AcpResultsLowerOffsetAbsolutePower (3149868), AcpResultsLowerOffsetRelativePower (3149869), AcpResultsSubblockCenterFrequency (3149881), AcpResultsSubblockIntegrationBandwidth (3149879), AcpResultsSubblockPower (3149880), AcpResultsTotalAggregatedPower (3149858), AcpResultsUpperOffsetAbsolutePower (3149874), AcpResultsUpperOffsetRelativePower (3149875), AcpSequentialFftSize (3149889), AcpSubblockIntegrationBandwidth (3149887), AcpSweepTimeAuto (3149854), AcpSweepTimeInterval (3149855), AcquisitionBandwidthOptimizationEnabled (3198977), AutoControlChannelPowerDetectionEnabled (3162197), AutoDmrsDetectionEnabled (3145768), AutoLevelInitialReferenceLevel (3198976), AutoNPuschChannelDetectionEnabled (3162208), AutoPcfichCfiDetectionEnabled (3162198), AutoPdschChannelDetectionEnabled (3162196), AutoResourceBlockDetectionEnabled (3145766), Band (3145751), CellId (3145746), CenterFrequency (3145729), CenterFrequencyForLimits (3198980), ChpAllTracesEnabled (3158036), ChpAmplitudeCorrectionType (3158051), ChpAveragingCount (3158022), ChpAveragingEnabled (3158023), ChpAveragingType (3158025), ChpComponentCarrierIntegrationBandwidth (3158018), ChpIntegrationBandwidthType (3158040), ChpMeasurementEnabled (3158016), ChpNumberOfAnalysisThreads (3158019), ChpRbwFilterAutoBandwidth (3158028), ChpRbwFilterBandwidth (3158029), ChpRbwFilterType (3158030), ChpResultsComponentCarrierAbsolutePower (3158037), ChpResultsComponentCarrierRelativePower (3158048), ChpResultsSubblockFrequency (3158043), ChpResultsSubblockIntegrationBandwidth (3158044), ChpResultsSubblockPower (3158045), ChpResultsTotalAggregatedPower (3158041), ChpSubblockIntegrationBandwidth (3158050), ChpSweepTimeAuto (3158033), ChpSweepTimeInterval (3158034), ComponentCarrierAtCenterFrequency (3145748), ComponentCarrierBandwidth (3145744), ComponentCarrierFrequency (3145745), ComponentCarrierSpacingType (3145747), CyclicPrefixMode (3145749), DigitalEdgeTriggerEdge (3145734), DigitalEdgeTriggerSource (3145733), DmrsOccEnabled (3145809), DownlinkAutoCellIDDetectionEnabled (3145788), DownlinkChannelConfigurationMode (3145789), DownlinkNumberOfSubframes (3145795), DownlinkTestModel (3145805), DownlinkUserDefinedCellSpecificRatio (3145790), DuplexScheme (3145741), EmtcAnalysisEnabled (3162224), eNodeBCategory (3145808), ExternalAttenuation (3145731), IQPowerEdgeTriggerLevel (3145736), IQPowerEdgeTriggerLevelType (3149823), IQPowerEdgeTriggerSlope (3145737), IQPowerEdgeTriggerSource (3145735), LaaDownlinkNumberOfEndingSymbols (3162204), LaaDownlinkStartingSymbol (3162203), LaaNumberOfSubframes (3162200), LaaStartingSubframe (3162199), LaaUplinkEndingSymbol (3162202), LaaUplinkStartPosition (3162201), LimitedConfigurationChange (3198979), LinkDirection (3145769), MiConfiguration (3145811), ModAccAllTracesEnabled (3162125), ModAccAveragingCount (3162123), ModAccAveragingEnabled (3162122), ModAccChannelEstimationType (3162167), ModAccCommonClockSourceEnabled (3162121), ModAccEvmUnit (3162118), ModAccEvmWithExclusionPeriodEnabled (3162162), ModAccFftWindowLength (3162169), ModAccFftWindowOffset (3162119), ModAccFftWindowType (3162168), ModAccInBandEmissionMaskType (3162225), ModAccMeasurementEnabled (3162112), ModAccMeasurementLength (3162117), ModAccMeasurementOffset (3162116), ModAccMulticarrierFilterEnabled (3162114), ModAccMultiCarrierFilterEnabled (3162114), ModAccNumberOfAnalysisThreads (3162126), ModAccResultsDownlinkDetectedCellID (3162195), ModAccResultsDownlinkOfdmSymbolTransmitPower (3162194), ModAccResultsDownlinkRSTransmitPower (3162193), ModAccResultsInBandEmissionMargin (3162155), ModAccResultsMaximumPeakCompositeEvm (3162128), ModAccResultsMaximumPeakCompositeMagnitudeError (3162171), ModAccResultsMaximumPeakCompositePhaseError (3162173), ModAccResultsMeanFrequencyError (3162146), ModAccResultsMeanIQGainImbalance (3162148), ModAccResultsMeanIQOriginOffset (3162147), ModAccResultsMeanQuadratureError (3162149), ModAccResultsMeanRmsCompositeEvm (3162127), ModAccResultsMeanRmsCompositeMagnitudeError (3162170), ModAccResultsMeanRmsCompositePhaseError (3162172), ModAccResultsMeanRmsCsrsEvm (3162185), ModAccResultsMeanRmsPbchEvm (3162188), ModAccResultsMeanRmsPcfichEvm (3162189), ModAccResultsMeanRmsPdcchEvm (3162190), ModAccResultsMeanRmsPhichEvm (3162191), ModAccResultsMeanRmsPssEvm (3162186), ModAccResultsMeanRmsSrsEvm (3162178), ModAccResultsMeanRmsSssEvm (3162187), ModAccResultsMeanSrsPower (3162179), ModAccResultsMeanSymbolClockError (3162152), ModAccResultsNPuschMaximumPeakDataEvm (3162219), ModAccResultsNPuschMaximumPeakDmrsEvm (3162221), ModAccResultsNPuschMeanDataPower (3162222), ModAccResultsNPuschMeanDmrsPower (3162223), ModAccResultsNPuschMeanRmsDataEvm (3162218), ModAccResultsNPuschMeanRmsDmrsEvm (3162220), ModAccResultsPdschMeanRms1024QamEvm (3162205), ModAccResultsPdschMeanRms16QamEvm (3162182), ModAccResultsPdschMeanRms256QamEvm (3162184), ModAccResultsPdschMeanRms64QamEvm (3162183), ModAccResultsPdschMeanRmsEvm (3162180), ModAccResultsPdschMeanRmsQpskEvm (3162181), ModAccResultsPeakCompositeEvmSlotIndex (3162131), ModAccResultsPeakCompositeEvmSubcarrierIndex (3162133), ModAccResultsPeakCompositeEvmSymbolIndex (3162132), ModAccResultsPsschMaximumPeakDataEvm (3162228), ModAccResultsPsschMaximumPeakDmrsEvm (3162230), ModAccResultsPsschMeanDataPower (3162231), ModAccResultsPsschMeanDmrsPower (3162232), ModAccResultsPsschMeanRmsDataEvm (3162227), ModAccResultsPsschMeanRmsDmrsEvm (3162229), ModAccResultsPuschMaximumPeakDataEvm (3162135), ModAccResultsPuschMaximumPeakDmrsEvm (3162137), ModAccResultsPuschMeanDataPower (3162138), ModAccResultsPuschMeanDmrsPower (3162139), ModAccResultsPuschMeanRmsDataEvm (3162134), ModAccResultsPuschMeanRmsDmrsEvm (3162136), ModAccResultsSpectralFlatnessRange1MaximumToRange1Minimum (3162156), ModAccResultsSpectralFlatnessRange1MaximumToRange2Minimum (3162158), ModAccResultsSpectralFlatnessRange2MaximumToRange1Minimum (3162159), ModAccResultsSpectralFlatnessRange2MaximumToRange2Minimum (3162157), ModAccResultsSubblockInBandEmissionMargin (3162174), ModAccResultsSubblockMeanIQGainImbalance (3162176), ModAccResultsSubblockMeanIQOriginOffset (3162175), ModAccResultsSubblockMeanQuadratureError (3162177), ModAccSpectralFlatnessCondition (3162120), ModAccSpectrumInverted (3162166), ModAccSynchronizationMode (3162115), NBIoTUplinkSubcarrierSpacing (3162207), NCellId (3162206), NPuschDmrsBaseSequenceIndex (3162214), NPuschDmrsBaseSequenceMode (3162213), NPuschDmrsCyclicShift (3162215), NPuschDmrsDeltaSequenceShift (3162216), NPuschDmrsGroupHoppingEnabled (3162217), NPuschFormat (3162209), NPuschModulationType (3162212), NPuschNumberOfTones (3162211), NPuschStartingSlot (3162226), NPuschToneOffset (3162210), NumberOfComponentCarriers (3145743), NumberOfDutAntennas (3145771), NumberOfPdschChannels (3145801), NumberOfSubblocks (3145763), ObwAllTracesEnabled (3170322), ObwAmplitudeCorrectionType (3170331), ObwAveragingCount (3170310), ObwAveragingEnabled (3170311), ObwAveragingType (3170313), ObwMeasurementEnabled (3170304), ObwNumberOfAnalysisThreads (3170307), ObwRbwFilterAutoBandwidth (3170316), ObwRbwFilterBandwidth (3170317), ObwRbwFilterType (3170318), ObwResultsAbsolutePower (3170324), ObwResultsOccupiedBandwidth (3170323), ObwResultsStartFrequency (3170325), ObwResultsStopFrequency (3170326), ObwSpan (3170308), ObwSweepTimeAuto (3170319), ObwSweepTimeInterval (3170320), PbchPower (3145793), PcfichCfi (3145796), PcfichPower (3145797), PdcchPower (3145794), PdschCW0ModulationType (3145802), PdschPower (3145804), PdschResourceBlockAllocation (3145803), PhichDuration (3145799), PhichPower (3145800), PhichResource (3145798), PsschModulationType (3145813), PsschNumberOfResourceBlocks (3145815), PsschPower (3145816), PsschResourceBlockOffset (3145814), PssPower (3145791), PuschCyclicShiftField (3145810), PuschDeltaSequenceShift (3145761), PuschModulationType (3145755), PuschNDmrs1 (3145759), PuschNDmrs2 (3145760), PuschNumberOfResourceBlockClusters (3145756), PuschNumberOfResourceBlocks (3145762), PuschPower (3145767), PuschResourceBlockOffset (3145758), PvtAllTracesEnabled (3182603), PvtAveragingCount (3182601), PvtAveragingEnabled (3182599), PvtAveragingType (3182602), PvtMeasurementEnabled (3182592), PvtMeasurementMethod (3182594), PvtNumberOfAnalysisThreads (3182604), PvtOffPowerExclusionAfter (3182614), PvtOffPowerExclusionBefore (3182613), PvtResultsBurstWidth (3182612), PvtResultsMeanAbsoluteOffPowerAfter (3182609), PvtResultsMeanAbsoluteOffPowerBefore (3182608), PvtResultsMeanAbsoluteOnPower (3182610), PvtResultsMeasurementStatus (3182606), ReferenceLevel (3145730), ReferenceLevelHeadroom (3149820), ResultFetchTimeout (3194880), SelectedPorts (3149821), SemAggregatedMaximumPower (3178581), SemAllTracesEnabled (3178535), SemAmplitudeCorrectionType (3178583), SemAveragingCount (3178526), SemAveragingEnabled (3178527), SemAveragingType (3178529), SemComponentCarrierIntegrationBandwidth (3178501), SemComponentCarrierMaximumOutputPower (3178582), SemDeltaFMaximum (3178580), SemDownlinkMaskType (3178579), SemMeasurementEnabled (3178496), SemNumberOfAnalysisThreads (3178525), SemNumberOfOffsets (3178507), SemOffsetAbsoluteLimitStart (3178512), SemOffsetAbsoluteLimitStop (3178513), SemOffsetBandwidthIntegral (3178508), SemOffsetLimitFailMask (3178509), SemOffsetRbwFilterBandwidth (3178519), SemOffsetRbwFilterType (3178520), SemOffsetRelativeLimitStart (3178522), SemOffsetRelativeLimitStop (3178523), SemOffsetSideband (3178515), SemOffsetStartFrequency (3178516), SemOffsetStopFrequency (3178517), SemResultsComponentCarrierAbsoluteIntegratedPower (3178541), SemResultsComponentCarrierAbsolutePeakPower (3178543), SemResultsComponentCarrierPeakFrequency (3178544), SemResultsComponentCarrierRelativeIntegratedPower (3178542), SemResultsLowerOffsetAbsoluteIntegratedPower (3178548), SemResultsLowerOffsetAbsolutePeakPower (3178550), SemResultsLowerOffsetMargin (3178553), SemResultsLowerOffsetMarginAbsolutePower (3178554), SemResultsLowerOffsetMarginFrequency (3178556), SemResultsLowerOffsetMarginRelativePower (3178555), SemResultsLowerOffsetMeasurementStatus (3178557), SemResultsLowerOffsetPeakFrequency (3178552), SemResultsLowerOffsetRelativeIntegratedPower (3178549), SemResultsLowerOffsetRelativePeakPower (3178551), SemResultsMeasurementStatus (3178537), SemResultsSubblockCenterFrequency (3178573), SemResultsSubblockIntegrationBandwidth (3178574), SemResultsSubblockPower (3178575), SemResultsTotalAggregatedPower (3178536), SemResultsUpperOffsetAbsoluteIntegratedPower (3178561), SemResultsUpperOffsetAbsolutePeakPower (3178563), SemResultsUpperOffsetMargin (3178566), SemResultsUpperOffsetMarginAbsolutePower (3178567), SemResultsUpperOffsetMarginFrequency (3178569), SemResultsUpperOffsetMarginRelativePower (3178568), SemResultsUpperOffsetMeasurementStatus (3178570), SemResultsUpperOffsetPeakFrequency (3178565), SemResultsUpperOffsetRelativeIntegratedPower (3178562), SemResultsUpperOffsetRelativePeakPower (3178564), SemSidelinkMaskType (3178584), SemStandardMaskType (3178572), SemSubblockAggregatedChannelBandwidth (3178578), SemSubblockIntegrationBandwidth (3178577), SemSweepTimeAuto (3178533), SemSweepTimeInterval (3178534), SemUplinkMaskType (3178572), SlotPhaseAllTracesEnabled (3186699), SlotPhaseCommonClockSourceEnabled (3186696), SlotPhaseExclusionPeriodEnabled (3186695), SlotPhaseMeasurementEnabled (3186688), SlotPhaseMeasurementLength (3186691), SlotPhaseMeasurementOffset (3186690), SlotPhaseResultsMaximumPhaseDiscontinuity (3186708), SlotPhaseSpectrumInverted (3186697), SlotPhaseSynchronizationMode (3186694), SlotPowerAllTracesEnabled (3190794), SlotPowerCommonClockSourceEnabled (3190789), SlotPowerMeasurementEnabled (3190784), SlotPowerMeasurementLength (3190787), SlotPowerMeasurementOffset (3190786), SlotPowerSpectrumInverted (3190790), SpecialSubframeConfiguration (3145770), SrsbHop (3145780), SrsBSrs (3145776), SrsCSrs (3145775), SrsEnabled (3145773), SrsISrs (3145777), SrskTC (3145781), SrsMaximumUpPtsEnabled (3145782), SrsnRrc (3145778), SrsnSrsCS (3145779), SrsPower (3145785), SrsSubframe1NRA (3145783), SrsSubframe6NRA (3145784), SrsSubframeConfiguration (3145774), SssPower (3145792), SubblockFrequencyDefinition (3145764), TransmitAntennaToAnalyze (3145772), TransmitterArchitecture (3198978), TriggerDelay (3145738), TriggerMinimumQuietTimeDuration (3145740), TriggerMinimumQuietTimeMode (3145739), TriggerType (3145732), UplinkDownlinkConfiguration (3145742), UplinkGroupHoppingEnabled (3145753), UplinkSequenceHoppingEnabled (3145754) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    AcpConfigurableNumberOfOffsetsEnabled = None
    AcpEutraOffsetDefinition = None
    AcpFarIFOutputPowerOffset = None
    AcpIFOutputPowerOffsetAuto = None
    AcpMeasurementEnabled = None
    AcpMeasurementMethod = None
    AcpNearIFOutputPowerOffset = None
    AcpNoiseCompensationEnabled = None
    AcpNumberOfAnalysisThreads = None
    AcpNumberOfEutraOffsets = None
    AcpNumberOfGsmOffsets = None
    AcpNumberOfUtraOffsets = None
    AcpOffsetFrequency = None
    AcpOffsetIntegrationBandwidth = None
    AcpRbwFilterAutoBandwidth = None
    AcpRbwFilterBandwidth = None
    AcpRbwFilterType = None
    AcpResultsComponentCarrierAbsolutePower = None
    AcpResultsComponentCarrierRelativePower = None
    AcpResultsLowerOffsetAbsolutePower = None
    AcpResultsLowerOffsetRelativePower = None
    AcpResultsSubblockCenterFrequency = None
    AcpResultsSubblockIntegrationBandwidth = None
    AcpResultsSubblockPower = None
    AcpResultsTotalAggregatedPower = None
    AcpResultsUpperOffsetAbsolutePower = None
    AcpResultsUpperOffsetRelativePower = None
    AcpSequentialFftSize = None
    AcpSubblockIntegrationBandwidth = None
    AcpSweepTimeAuto = None
    AcpSweepTimeInterval = None
    AcquisitionBandwidthOptimizationEnabled = None
    AutoControlChannelPowerDetectionEnabled = None
    AutoDmrsDetectionEnabled = None
    AutoLevelInitialReferenceLevel = None
    AutoNPuschChannelDetectionEnabled = None
    AutoPcfichCfiDetectionEnabled = None
    AutoPdschChannelDetectionEnabled = None
    AutoResourceBlockDetectionEnabled = None
    Band = None
    CellId = None
    CenterFrequency = None
    CenterFrequencyForLimits = None
    ChpAllTracesEnabled = None
    ChpAmplitudeCorrectionType = None
    ChpAveragingCount = None
    ChpAveragingEnabled = None
    ChpAveragingType = None
    ChpComponentCarrierIntegrationBandwidth = None
    ChpIntegrationBandwidthType = None
    ChpMeasurementEnabled = None
    ChpNumberOfAnalysisThreads = None
    ChpRbwFilterAutoBandwidth = None
    ChpRbwFilterBandwidth = None
    ChpRbwFilterType = None
    ChpResultsComponentCarrierAbsolutePower = None
    ChpResultsComponentCarrierRelativePower = None
    ChpResultsSubblockFrequency = None
    ChpResultsSubblockIntegrationBandwidth = None
    ChpResultsSubblockPower = None
    ChpResultsTotalAggregatedPower = None
    ChpSubblockIntegrationBandwidth = None
    ChpSweepTimeAuto = None
    ChpSweepTimeInterval = None
    ComponentCarrierAtCenterFrequency = None
    ComponentCarrierBandwidth = None
    ComponentCarrierFrequency = None
    ComponentCarrierSpacingType = None
    CyclicPrefixMode = None
    DigitalEdgeTriggerEdge = None
    DigitalEdgeTriggerSource = None
    DmrsOccEnabled = None
    DownlinkAutoCellIDDetectionEnabled = None
    DownlinkChannelConfigurationMode = None
    DownlinkNumberOfSubframes = None
    DownlinkTestModel = None
    DownlinkUserDefinedCellSpecificRatio = None
    DuplexScheme = None
    EmtcAnalysisEnabled = None
    eNodeBCategory = None
    ExternalAttenuation = None
    IQPowerEdgeTriggerLevel = None
    IQPowerEdgeTriggerLevelType = None
    IQPowerEdgeTriggerSlope = None
    IQPowerEdgeTriggerSource = None
    LaaDownlinkNumberOfEndingSymbols = None
    LaaDownlinkStartingSymbol = None
    LaaNumberOfSubframes = None
    LaaStartingSubframe = None
    LaaUplinkEndingSymbol = None
    LaaUplinkStartPosition = None
    LimitedConfigurationChange = None
    LinkDirection = None
    MiConfiguration = None
    ModAccAllTracesEnabled = None
    ModAccAveragingCount = None
    ModAccAveragingEnabled = None
    ModAccChannelEstimationType = None
    ModAccCommonClockSourceEnabled = None
    ModAccEvmUnit = None
    ModAccEvmWithExclusionPeriodEnabled = None
    ModAccFftWindowLength = None
    ModAccFftWindowOffset = None
    ModAccFftWindowType = None
    ModAccInBandEmissionMaskType = None
    ModAccMeasurementEnabled = None
    ModAccMeasurementLength = None
    ModAccMeasurementOffset = None
    ModAccMultiCarrierFilterEnabled = None
    ModAccMulticarrierFilterEnabled = None
    ModAccNumberOfAnalysisThreads = None
    ModAccResultsDownlinkDetectedCellID = None
    ModAccResultsDownlinkOfdmSymbolTransmitPower = None
    ModAccResultsDownlinkRSTransmitPower = None
    ModAccResultsInBandEmissionMargin = None
    ModAccResultsMaximumPeakCompositeEvm = None
    ModAccResultsMaximumPeakCompositeMagnitudeError = None
    ModAccResultsMaximumPeakCompositePhaseError = None
    ModAccResultsMeanFrequencyError = None
    ModAccResultsMeanIQGainImbalance = None
    ModAccResultsMeanIQOriginOffset = None
    ModAccResultsMeanQuadratureError = None
    ModAccResultsMeanRmsCompositeEvm = None
    ModAccResultsMeanRmsCompositeMagnitudeError = None
    ModAccResultsMeanRmsCompositePhaseError = None
    ModAccResultsMeanRmsCsrsEvm = None
    ModAccResultsMeanRmsPbchEvm = None
    ModAccResultsMeanRmsPcfichEvm = None
    ModAccResultsMeanRmsPdcchEvm = None
    ModAccResultsMeanRmsPhichEvm = None
    ModAccResultsMeanRmsPssEvm = None
    ModAccResultsMeanRmsSrsEvm = None
    ModAccResultsMeanRmsSssEvm = None
    ModAccResultsMeanSrsPower = None
    ModAccResultsMeanSymbolClockError = None
    ModAccResultsNPuschMaximumPeakDataEvm = None
    ModAccResultsNPuschMaximumPeakDmrsEvm = None
    ModAccResultsNPuschMeanDataPower = None
    ModAccResultsNPuschMeanDmrsPower = None
    ModAccResultsNPuschMeanRmsDataEvm = None
    ModAccResultsNPuschMeanRmsDmrsEvm = None
    ModAccResultsPdschMeanRms1024QamEvm = None
    ModAccResultsPdschMeanRms16QamEvm = None
    ModAccResultsPdschMeanRms256QamEvm = None
    ModAccResultsPdschMeanRms64QamEvm = None
    ModAccResultsPdschMeanRmsEvm = None
    ModAccResultsPdschMeanRmsQpskEvm = None
    ModAccResultsPeakCompositeEvmSlotIndex = None
    ModAccResultsPeakCompositeEvmSubcarrierIndex = None
    ModAccResultsPeakCompositeEvmSymbolIndex = None
    ModAccResultsPsschMaximumPeakDataEvm = None
    ModAccResultsPsschMaximumPeakDmrsEvm = None
    ModAccResultsPsschMeanDataPower = None
    ModAccResultsPsschMeanDmrsPower = None
    ModAccResultsPsschMeanRmsDataEvm = None
    ModAccResultsPsschMeanRmsDmrsEvm = None
    ModAccResultsPuschMaximumPeakDataEvm = None
    ModAccResultsPuschMaximumPeakDmrsEvm = None
    ModAccResultsPuschMeanDataPower = None
    ModAccResultsPuschMeanDmrsPower = None
    ModAccResultsPuschMeanRmsDataEvm = None
    ModAccResultsPuschMeanRmsDmrsEvm = None
    ModAccResultsSpectralFlatnessRange1MaximumToRange1Minimum = None
    ModAccResultsSpectralFlatnessRange1MaximumToRange2Minimum = None
    ModAccResultsSpectralFlatnessRange2MaximumToRange1Minimum = None
    ModAccResultsSpectralFlatnessRange2MaximumToRange2Minimum = None
    ModAccResultsSubblockInBandEmissionMargin = None
    ModAccResultsSubblockMeanIQGainImbalance = None
    ModAccResultsSubblockMeanIQOriginOffset = None
    ModAccResultsSubblockMeanQuadratureError = None
    ModAccSpectralFlatnessCondition = None
    ModAccSpectrumInverted = None
    ModAccSynchronizationMode = None
    NBIoTUplinkSubcarrierSpacing = None
    NCellId = None
    NPuschDmrsBaseSequenceIndex = None
    NPuschDmrsBaseSequenceMode = None
    NPuschDmrsCyclicShift = None
    NPuschDmrsDeltaSequenceShift = None
    NPuschDmrsGroupHoppingEnabled = None
    NPuschFormat = None
    NPuschModulationType = None
    NPuschNumberOfTones = None
    NPuschStartingSlot = None
    NPuschToneOffset = None
    NumberOfComponentCarriers = None
    NumberOfDutAntennas = None
    NumberOfPdschChannels = None
    NumberOfSubblocks = None
    ObwAllTracesEnabled = None
    ObwAmplitudeCorrectionType = None
    ObwAveragingCount = None
    ObwAveragingEnabled = None
    ObwAveragingType = None
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
    PbchPower = None
    PcfichCfi = None
    PcfichPower = None
    PdcchPower = None
    PdschCW0ModulationType = None
    PdschPower = None
    PdschResourceBlockAllocation = None
    PhichDuration = None
    PhichPower = None
    PhichResource = None
    PsschModulationType = None
    PsschNumberOfResourceBlocks = None
    PsschPower = None
    PsschResourceBlockOffset = None
    PssPower = None
    PuschCyclicShiftField = None
    PuschDeltaSequenceShift = None
    PuschModulationType = None
    PuschNDmrs1 = None
    PuschNDmrs2 = None
    PuschNumberOfResourceBlockClusters = None
    PuschNumberOfResourceBlocks = None
    PuschPower = None
    PuschResourceBlockOffset = None
    PvtAllTracesEnabled = None
    PvtAveragingCount = None
    PvtAveragingEnabled = None
    PvtAveragingType = None
    PvtMeasurementEnabled = None
    PvtMeasurementMethod = None
    PvtNumberOfAnalysisThreads = None
    PvtOffPowerExclusionAfter = None
    PvtOffPowerExclusionBefore = None
    PvtResultsBurstWidth = None
    PvtResultsMeanAbsoluteOffPowerAfter = None
    PvtResultsMeanAbsoluteOffPowerBefore = None
    PvtResultsMeanAbsoluteOnPower = None
    PvtResultsMeasurementStatus = None
    ReferenceLevel = None
    ReferenceLevelHeadroom = None
    ResultFetchTimeout = None
    SelectedPorts = None
    SemAggregatedMaximumPower = None
    SemAllTracesEnabled = None
    SemAmplitudeCorrectionType = None
    SemAveragingCount = None
    SemAveragingEnabled = None
    SemAveragingType = None
    SemComponentCarrierIntegrationBandwidth = None
    SemComponentCarrierMaximumOutputPower = None
    SemDeltaFMaximum = None
    SemDownlinkMaskType = None
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
    SemResultsSubblockCenterFrequency = None
    SemResultsSubblockIntegrationBandwidth = None
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
    SemSidelinkMaskType = None
    SemStandardMaskType = None
    SemSubblockAggregatedChannelBandwidth = None
    SemSubblockIntegrationBandwidth = None
    SemSweepTimeAuto = None
    SemSweepTimeInterval = None
    SemUplinkMaskType = None
    SlotPhaseAllTracesEnabled = None
    SlotPhaseCommonClockSourceEnabled = None
    SlotPhaseExclusionPeriodEnabled = None
    SlotPhaseMeasurementEnabled = None
    SlotPhaseMeasurementLength = None
    SlotPhaseMeasurementOffset = None
    SlotPhaseResultsMaximumPhaseDiscontinuity = None
    SlotPhaseSpectrumInverted = None
    SlotPhaseSynchronizationMode = None
    SlotPowerAllTracesEnabled = None
    SlotPowerCommonClockSourceEnabled = None
    SlotPowerMeasurementEnabled = None
    SlotPowerMeasurementLength = None
    SlotPowerMeasurementOffset = None
    SlotPowerSpectrumInverted = None
    SpecialSubframeConfiguration = None
    SrsbHop = None
    SrsBSrs = None
    SrsCSrs = None
    SrsEnabled = None
    SrsISrs = None
    SrskTC = None
    SrsMaximumUpPtsEnabled = None
    SrsnRrc = None
    SrsnSrsCS = None
    SrsPower = None
    SrsSubframe1NRA = None
    SrsSubframe6NRA = None
    SrsSubframeConfiguration = None
    SssPower = None
    SubblockFrequencyDefinition = None
    TransmitAntennaToAnalyze = None
    TransmitterArchitecture = None
    TriggerDelay = None
    TriggerMinimumQuietTimeDuration = None
    TriggerMinimumQuietTimeMode = None
    TriggerType = None
    UplinkDownlinkConfiguration = None
    UplinkGroupHoppingEnabled = None
    UplinkSequenceHoppingEnabled = None
    value__ = None


class RFmxLteMXPsschModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPsschModulationType, values: Qam16 (1), Qam64 (2), Qpsk (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Qam64 = None
    Qpsk = None
    value__ = None


class RFmxLteMXPuschModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPuschModulationType, values: ModulationType1024Qam (4), ModulationType16Qam (1), ModulationType256Qam (3), ModulationType64Qam (2), ModulationTypeQpsk (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ModulationType1024Qam = None
    ModulationType16Qam = None
    ModulationType256Qam = None
    ModulationType64Qam = None
    ModulationTypeQpsk = None
    value__ = None


class RFmxLteMXPvt(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXPvt) -> RFmxLteMXPvtConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXPvt) -> RFmxLteMXPvtResults

"""



class RFmxLteMXPvtAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPvtAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXPvtAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPvtAveragingType, values: Log (1), Rms (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXPvtConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxLteMXPvtConfiguration, selectorString: str, averagingEnabled: RFmxLteMXPvtAveragingEnabled, averagingCount: int, averagingType: RFmxLteMXPvtAveragingType) -> int """
        pass

    def ConfigureMeasurementMethod(self, selectorString, measurementMethod):
        """ ConfigureMeasurementMethod(self: RFmxLteMXPvtConfiguration, selectorString: str, measurementMethod: RFmxLteMXPvtMeasurementMethod) -> int """
        pass

    def ConfigureOffPowerExclusionPeriods(self, selectorString, offPowerExclusionBefore, offPowerExclusionAfter):
        """ ConfigureOffPowerExclusionPeriods(self: RFmxLteMXPvtConfiguration, selectorString: str, offPowerExclusionBefore: float, offPowerExclusionAfter: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, RFmxLteMXPvtAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, RFmxLteMXPvtAveragingType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMethod(self, selectorString, value):
        """ GetMeasurementMethod(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, RFmxLteMXPvtMeasurementMethod) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffPowerExclusionAfter(self, selectorString, value):
        """ GetOffPowerExclusionAfter(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffPowerExclusionBefore(self, selectorString, value):
        """ GetOffPowerExclusionBefore(self: RFmxLteMXPvtConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXPvtConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxLteMXPvtConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxLteMXPvtConfiguration, selectorString: str, value: RFmxLteMXPvtAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxLteMXPvtConfiguration, selectorString: str, value: RFmxLteMXPvtAveragingType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXPvtConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMethod(self, selectorString, value):
        """ SetMeasurementMethod(self: RFmxLteMXPvtConfiguration, selectorString: str, value: RFmxLteMXPvtMeasurementMethod) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxLteMXPvtConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffPowerExclusionAfter(self, selectorString, value):
        """ SetOffPowerExclusionAfter(self: RFmxLteMXPvtConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffPowerExclusionBefore(self, selectorString, value):
        """ SetOffPowerExclusionBefore(self: RFmxLteMXPvtConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxLteMXPvtMeasurementMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPvtMeasurementMethod, values: DynamicRange (1), Normal (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXPvtMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXPvtMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXPvtResults(RFmxLteMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, measurementStatus, meanAbsoluteOffPowerBefore, meanAbsoluteOffPowerAfter, meanAbsoluteOnPower, burstWidth):
        """ FetchMeasurement(self: RFmxLteMXPvtResults, selectorString: str, timeout: float) -> (int, RFmxLteMXPvtMeasurementStatus, float, float, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, measurementStatus, meanAbsoluteOffPowerBefore, meanAbsoluteOffPowerAfter, meanAbsoluteOnPower, burstWidth):
        """ FetchMeasurementArray(self: RFmxLteMXPvtResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxLteMXPvtMeasurementStatus], meanAbsoluteOffPowerBefore: Array[float], meanAbsoluteOffPowerAfter: Array[float], meanAbsoluteOnPower: Array[float], burstWidth: Array[float]) -> (int, Array[RFmxLteMXPvtMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchSignalPowerTrace(self, selectorString, timeout, signalPower, absoluteLimit):
        """ FetchSignalPowerTrace(self: RFmxLteMXPvtResults, selectorString: str, timeout: float, signalPower: AnalogWaveform[Single], absoluteLimit: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def GetBurstWidth(self, selectorString, value):
        """ GetBurstWidth(self: RFmxLteMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanAbsoluteOffPowerAfter(self, selectorString, value):
        """ GetMeanAbsoluteOffPowerAfter(self: RFmxLteMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanAbsoluteOffPowerBefore(self, selectorString, value):
        """ GetMeanAbsoluteOffPowerBefore(self: RFmxLteMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeanAbsoluteOnPower(self, selectorString, value):
        """ GetMeanAbsoluteOnPower(self: RFmxLteMXPvtResults, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementStatus(self, selectorString, value):
        """ GetMeasurementStatus(self: RFmxLteMXPvtResults, selectorString: str) -> (int, RFmxLteMXPvtMeasurementStatus) """
        pass


class RFmxLteMXReferenceLevelUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXReferenceLevelUnits, values: dBm (0), Volts (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Volts = None


class RFmxLteMXSem(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXSem) -> RFmxLteMXSemConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXSem) -> RFmxLteMXSemResults

"""



class RFmxLteMXSemAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemComponentCarrierConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureMaximumOutputPower(self, selectorString, maximumOutputPower):
        """ ConfigureMaximumOutputPower(self: RFmxLteMXSemComponentCarrierConfiguration, selectorString: str, maximumOutputPower: float) -> int """
        pass

    def ConfigureMaximumOutputPowerArray(self, selectorString, maximumOutputPower):
        """ ConfigureMaximumOutputPowerArray(self: RFmxLteMXSemComponentCarrierConfiguration, selectorString: str, maximumOutputPower: Array[float]) -> int """
        pass

    def GetIntegrationBandwidth(self, selectorString, value):
        """ GetIntegrationBandwidth(self: RFmxLteMXSemComponentCarrierConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMaximumOutputPower(self, selectorString, value):
        """ GetMaximumOutputPower(self: RFmxLteMXSemComponentCarrierConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetMaximumOutputPower(self, selectorString, value):
        """ SetMaximumOutputPower(self: RFmxLteMXSemComponentCarrierConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxLteMXSemComponentCarrierResults(RFmxLteMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower):
        """ FetchMeasurement(self: RFmxLteMXSemComponentCarrierResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower):
        """ FetchMeasurementArray(self: RFmxLteMXSemComponentCarrierResults, selectorString: str, timeout: float, absoluteIntegratedPower: Array[float], relativeIntegratedPower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetAbsoluteIntegratedPower(self: RFmxLteMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetAbsolutePeakPower(self, selectorString, value):
        """ GetAbsolutePeakPower(self: RFmxLteMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakFrequency(self, selectorString, value):
        """ GetPeakFrequency(self: RFmxLteMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass

    def GetRelativeIntegratedPower(self, selectorString, value):
        """ GetRelativeIntegratedPower(self: RFmxLteMXSemComponentCarrierResults, selectorString: str) -> (int, float) """
        pass


class RFmxLteMXSemConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxLteMXSemConfiguration, selectorString: str, averagingEnabled: RFmxLteMXSemAveragingEnabled, averagingCount: int, averagingType: RFmxLteMXSemAveragingType) -> int """
        pass

    def ConfigureDownlinkMask(self, selectorString, downlinkMaskType, deltaFMaximum, aggregatedMaximumPower):
        """ ConfigureDownlinkMask(self: RFmxLteMXSemConfiguration, selectorString: str, downlinkMaskType: RFmxLteMXSemDownlinkMaskType, deltaFMaximum: float, aggregatedMaximumPower: float) -> int """
        pass

    def ConfigureNumberOfOffsets(self, selectorString, numberOfOffsets):
        """ ConfigureNumberOfOffsets(self: RFmxLteMXSemConfiguration, selectorString: str, numberOfOffsets: int) -> int """
        pass

    def ConfigureOffsetAbsoluteLimit(self, selectorString, offsetAbsoluteLimitStart, offsetAbsoluteLimitStop):
        """ ConfigureOffsetAbsoluteLimit(self: RFmxLteMXSemConfiguration, selectorString: str, offsetAbsoluteLimitStart: float, offsetAbsoluteLimitStop: float) -> int """
        pass

    def ConfigureOffsetAbsoluteLimitArray(self, selectorString, offsetAbsoluteLimitStart, offsetAbsoluteLimitStop):
        """ ConfigureOffsetAbsoluteLimitArray(self: RFmxLteMXSemConfiguration, selectorString: str, offsetAbsoluteLimitStart: Array[float], offsetAbsoluteLimitStop: Array[float]) -> int """
        pass

    def ConfigureOffsetBandwidthIntegral(self, selectorString, offsetBandwidthIntegral):
        """ ConfigureOffsetBandwidthIntegral(self: RFmxLteMXSemConfiguration, selectorString: str, offsetBandwidthIntegral: int) -> int """
        pass

    def ConfigureOffsetBandwidthIntegralArray(self, selectorString, offsetBandwidthIntegral):
        """ ConfigureOffsetBandwidthIntegralArray(self: RFmxLteMXSemConfiguration, selectorString: str, offsetBandwidthIntegral: Array[int]) -> int """
        pass

    def ConfigureOffsetFrequency(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband):
        """ ConfigureOffsetFrequency(self: RFmxLteMXSemConfiguration, selectorString: str, offsetStartFrequency: float, offsetStopFrequency: float, offsetSideband: RFmxLteMXSemOffsetSideband) -> int """
        pass

    def ConfigureOffsetFrequencyArray(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband):
        """ ConfigureOffsetFrequencyArray(self: RFmxLteMXSemConfiguration, selectorString: str, offsetStartFrequency: Array[float], offsetStopFrequency: Array[float], offsetSideband: Array[RFmxLteMXSemOffsetSideband]) -> int """
        pass

    def ConfigureOffsetLimitFailMask(self, selectorString, limitFailMask):
        """ ConfigureOffsetLimitFailMask(self: RFmxLteMXSemConfiguration, selectorString: str, limitFailMask: RFmxLteMXSemOffsetLimitFailMask) -> int """
        pass

    def ConfigureOffsetLimitFailMaskArray(self, selectorString, limitFailMask):
        """ ConfigureOffsetLimitFailMaskArray(self: RFmxLteMXSemConfiguration, selectorString: str, limitFailMask: Array[RFmxLteMXSemOffsetLimitFailMask]) -> int """
        pass

    def ConfigureOffsetRbwFilter(self, selectorString, offsetRbw, offsetRbwFilterType):
        """ ConfigureOffsetRbwFilter(self: RFmxLteMXSemConfiguration, selectorString: str, offsetRbw: float, offsetRbwFilterType: RFmxLteMXSemOffsetRbwFilterType) -> int """
        pass

    def ConfigureOffsetRbwFilterArray(self, selectorString, offsetRbw, offsetRbwFilterType):
        """ ConfigureOffsetRbwFilterArray(self: RFmxLteMXSemConfiguration, selectorString: str, offsetRbw: Array[float], offsetRbwFilterType: Array[RFmxLteMXSemOffsetRbwFilterType]) -> int """
        pass

    def ConfigureOffsetRelativeLimit(self, selectorString, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimit(self: RFmxLteMXSemConfiguration, selectorString: str, relativeLimitStart: float, relativeLimitStop: float) -> int """
        pass

    def ConfigureOffsetRelativeLimitArray(self, selectorString, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimitArray(self: RFmxLteMXSemConfiguration, selectorString: str, relativeLimitStart: Array[float], relativeLimitStop: Array[float]) -> int """
        pass

    def ConfigureStandardMaskType(self, selectorString, standardMaskType):
        """ ConfigureStandardMaskType(self: RFmxLteMXSemConfiguration, selectorString: str, standardMaskType: RFmxLteMXSemStandardMaskType) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxLteMXSemConfiguration, selectorString: str, sweepTimeAuto: RFmxLteMXSemSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def ConfigureUplinkMaskType(self, selectorString, uplinkMaskType):
        """ ConfigureUplinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str, uplinkMaskType: RFmxLteMXSemUplinkMaskType) -> int """
        pass

    def GetAggregatedMaximumPower(self, selectorString, value):
        """ GetAggregatedMaximumPower(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemAveragingType) """
        pass

    def GetComponentCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetComponentCarrierIntegrationBandwidth(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDeltaFMaximum(self, selectorString, value):
        """ GetDeltaFMaximum(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetDownlinkMaskType(self, selectorString, value):
        """ GetDownlinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemDownlinkMaskType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfOffsets(self, selectorString, value):
        """ GetNumberOfOffsets(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetAbsoluteLimitStart(self, selectorString, value):
        """ GetOffsetAbsoluteLimitStart(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetAbsoluteLimitStop(self, selectorString, value):
        """ GetOffsetAbsoluteLimitStop(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetBandwidthIntegral(self, selectorString, value):
        """ GetOffsetBandwidthIntegral(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetLimitFailMask(self, selectorString, value):
        """ GetOffsetLimitFailMask(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemOffsetLimitFailMask) """
        pass

    def GetOffsetRbwFilterBandwidth(self, selectorString, value):
        """ GetOffsetRbwFilterBandwidth(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRbwFilterType(self, selectorString, value):
        """ GetOffsetRbwFilterType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemOffsetRbwFilterType) """
        pass

    def GetOffsetRelativeLimitStart(self, selectorString, value):
        """ GetOffsetRelativeLimitStart(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRelativeLimitStop(self, selectorString, value):
        """ GetOffsetRelativeLimitStop(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetSideband(self, selectorString, value):
        """ GetOffsetSideband(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemOffsetSideband) """
        pass

    def GetOffsetStartFrequency(self, selectorString, value):
        """ GetOffsetStartFrequency(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetStopFrequency(self, selectorString, value):
        """ GetOffsetStopFrequency(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSidelinkMaskType(self, selectorString, value):
        """ GetSidelinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemSidelinkMaskType) """
        pass

    def GetStandardMaskType(self, selectorString, value):
        """ GetStandardMaskType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemStandardMaskType) """
        pass

    def GetSubblockAggregatedChannelBandwidth(self, selectorString, value):
        """ GetSubblockAggregatedChannelBandwidth(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetUplinkMaskType(self, selectorString, value):
        """ GetUplinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str) -> (int, RFmxLteMXSemUplinkMaskType) """
        pass

    def SetAggregatedMaximumPower(self, selectorString, value):
        """ SetAggregatedMaximumPower(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxLteMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemAveragingType) -> int """
        pass

    def SetDeltaFMaximum(self, selectorString, value):
        """ SetDeltaFMaximum(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetDownlinkMaskType(self, selectorString, value):
        """ SetDownlinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemDownlinkMaskType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxLteMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfOffsets(self, selectorString, value):
        """ SetNumberOfOffsets(self: RFmxLteMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetAbsoluteLimitStart(self, selectorString, value):
        """ SetOffsetAbsoluteLimitStart(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetAbsoluteLimitStop(self, selectorString, value):
        """ SetOffsetAbsoluteLimitStop(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetBandwidthIntegral(self, selectorString, value):
        """ SetOffsetBandwidthIntegral(self: RFmxLteMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetLimitFailMask(self, selectorString, value):
        """ SetOffsetLimitFailMask(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemOffsetLimitFailMask) -> int """
        pass

    def SetOffsetRbwFilterBandwidth(self, selectorString, value):
        """ SetOffsetRbwFilterBandwidth(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRbwFilterType(self, selectorString, value):
        """ SetOffsetRbwFilterType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemOffsetRbwFilterType) -> int """
        pass

    def SetOffsetRelativeLimitStart(self, selectorString, value):
        """ SetOffsetRelativeLimitStart(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRelativeLimitStop(self, selectorString, value):
        """ SetOffsetRelativeLimitStop(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetSideband(self, selectorString, value):
        """ SetOffsetSideband(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemOffsetSideband) -> int """
        pass

    def SetOffsetStartFrequency(self, selectorString, value):
        """ SetOffsetStartFrequency(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetStopFrequency(self, selectorString, value):
        """ SetOffsetStopFrequency(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSidelinkMaskType(self, selectorString, value):
        """ SetSidelinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemSidelinkMaskType) -> int """
        pass

    def SetStandardMaskType(self, selectorString, value):
        """ SetStandardMaskType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemStandardMaskType) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxLteMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetUplinkMaskType(self, selectorString, value):
        """ SetUplinkMaskType(self: RFmxLteMXSemConfiguration, selectorString: str, value: RFmxLteMXSemUplinkMaskType) -> int """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxLteMXSemConfiguration) -> RFmxLteMXSemComponentCarrierConfiguration

"""



class RFmxLteMXSemDownlinkMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemDownlinkMaskType, values: Band46 (1), Custom (5), ENodeBCategoryBased (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Band46 = None
    Custom = None
    ENodeBCategoryBased = None
    value__ = None


class RFmxLteMXSemLowerOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemLowerOffsetMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemOffsetLimitFailMask(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemOffsetLimitFailMask, values: AbsAndRel (0), Absolute (2), AbsOrRel (1), Relative (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemOffsetRbwFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemOffsetRbwFilterType, values: FftBased (0), Flat (2), Gaussian (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemOffsetSideband(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemOffsetSideband, values: Both (2), Negative (0), Positive (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemResults(RFmxLteMXSubObject):
    # no doc
    def FetchLowerOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMargin(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, RFmxLteMXSemLowerOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchLowerOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMarginArray(self: RFmxLteMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxLteMXSemLowerOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxLteMXSemLowerOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchLowerOffsetPower(self, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower):
        """ FetchLowerOffsetPower(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchLowerOffsetPowerArray(self, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower):
        """ FetchLowerOffsetPowerArray(self: RFmxLteMXSemResults, selectorString: str, timeout: float, absoluteIntegratedPower: Array[float], relativeIntegratedPower: Array[float], absolutePeakPower: Array[float], peakFrequency: Array[float], relativePeakPower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchMeasurementStatus(self, selectorString, timeout, measurementStatus):
        """ FetchMeasurementStatus(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, RFmxLteMXSemMeasurementStatus) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum, compositeMask):
        """ FetchSpectrum(self: RFmxLteMXSemResults, selectorString: str, timeout: float, spectrum: Spectrum[Single], compositeMask: Spectrum[Single]) -> (int, Spectrum[Single], Spectrum[Single]) """
        pass

    def FetchSubblockMeasurement(self, selectorString, timeout, subblockPower, integrationBandwidth, frequency):
        """ FetchSubblockMeasurement(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchUpperOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMargin(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, RFmxLteMXSemUpperOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchUpperOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMarginArray(self: RFmxLteMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxLteMXSemUpperOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxLteMXSemUpperOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchUpperOffsetPower(self, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower):
        """ FetchUpperOffsetPower(self: RFmxLteMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchUpperOffsetPowerArray(self, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower):
        """ FetchUpperOffsetPowerArray(self: RFmxLteMXSemResults, selectorString: str, timeout: float, absoluteIntegratedPower: Array[float], relativeIntegratedPower: Array[float], absolutePeakPower: Array[float], peakFrequency: Array[float], relativePeakPower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetLowerOffsetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetLowerOffsetAbsoluteIntegratedPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetAbsolutePeakPower(self, selectorString, value):
        """ GetLowerOffsetAbsolutePeakPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMargin(self, selectorString, value):
        """ GetLowerOffsetMargin(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetMarginAbsolutePower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginFrequency(self, selectorString, value):
        """ GetLowerOffsetMarginFrequency(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginRelativePower(self, selectorString, value):
        """ GetLowerOffsetMarginRelativePower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMeasurementStatus(self, selectorString, value):
        """ GetLowerOffsetMeasurementStatus(self: RFmxLteMXSemResults, selectorString: str) -> (int, RFmxLteMXSemLowerOffsetMeasurementStatus) """
        pass

    def GetLowerOffsetPeakFrequency(self, selectorString, value):
        """ GetLowerOffsetPeakFrequency(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativeIntegratedPower(self, selectorString, value):
        """ GetLowerOffsetRelativeIntegratedPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativePeakPower(self, selectorString, value):
        """ GetLowerOffsetRelativePeakPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementStatus(self, selectorString, value):
        """ GetMeasurementStatus(self: RFmxLteMXSemResults, selectorString: str) -> (int, RFmxLteMXSemMeasurementStatus) """
        pass

    def GetSubblockCenterFrequency(self, selectorString, value):
        """ GetSubblockCenterFrequency(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockIntegrationBandwidth(self, selectorString, value):
        """ GetSubblockIntegrationBandwidth(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetSubblockPower(self, selectorString, value):
        """ GetSubblockPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetTotalAggregatedPower(self, selectorString, value):
        """ GetTotalAggregatedPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetUpperOffsetAbsoluteIntegratedPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsolutePeakPower(self, selectorString, value):
        """ GetUpperOffsetAbsolutePeakPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMargin(self, selectorString, value):
        """ GetUpperOffsetMargin(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetMarginAbsolutePower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginFrequency(self, selectorString, value):
        """ GetUpperOffsetMarginFrequency(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginRelativePower(self, selectorString, value):
        """ GetUpperOffsetMarginRelativePower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMeasurementStatus(self, selectorString, value):
        """ GetUpperOffsetMeasurementStatus(self: RFmxLteMXSemResults, selectorString: str) -> (int, RFmxLteMXSemUpperOffsetMeasurementStatus) """
        pass

    def GetUpperOffsetPeakFrequency(self, selectorString, value):
        """ GetUpperOffsetPeakFrequency(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativeIntegratedPower(self, selectorString, value):
        """ GetUpperOffsetRelativeIntegratedPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativePeakPower(self, selectorString, value):
        """ GetUpperOffsetRelativePeakPower(self: RFmxLteMXSemResults, selectorString: str) -> (int, float) """
        pass

    ComponentCarrier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentCarrier(self: RFmxLteMXSemResults) -> RFmxLteMXSemComponentCarrierResults

"""



class RFmxLteMXSemSidelinkMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemSidelinkMaskType, values: Custom (5), General_NS01 (0), NS33_Or_NS34 (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    General_NS01 = None
    NS33_Or_NS34 = None
    value__ = None


class RFmxLteMXSemStandardMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemStandardMaskType, values: CANS04 (4), Custom (5), General_NS01 (0), NS03_Or_NS11_Or_NS20 (1), NS04 (2), NS06_Or_NS07 (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CANS04 = None
    Custom = None
    General_NS01 = None
    NS03_Or_NS11_Or_NS20 = None
    NS04 = None
    NS06_Or_NS07 = None
    value__ = None


class RFmxLteMXSemSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemSweepTimeAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSemUplinkMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemUplinkMaskType, values: CANCNS01 (7), CANS04 (4), Custom (5), General_CAClassB (6), General_NS01 (0), NS03_Or_NS11_Or_NS20 (1), NS03_Or_NS11_Or_NS20_Or_NS21 (1), NS04 (2), NS06_Or_NS07 (3), NS27 (8), NS35 (9) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CANCNS01 = None
    CANS04 = None
    Custom = None
    General_CAClassB = None
    General_NS01 = None
    NS03_Or_NS11_Or_NS20 = None
    NS03_Or_NS11_Or_NS20_Or_NS21 = None
    NS04 = None
    NS06_Or_NS07 = None
    NS27 = None
    NS35 = None
    value__ = None


class RFmxLteMXSemUpperOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSemUpperOffsetMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSlotPhase(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXSlotPhase) -> RFmxLteMXSlotPhaseConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXSlotPhase) -> RFmxLteMXSlotPhaseResults

"""



class RFmxLteMXSlotPhaseCommonClockSourceEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSlotPhaseCommonClockSourceEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSlotPhaseConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureSynchronizationModeAndInterval(self, selectorString, synchronizationMode, measurementOffset, measurementLength):
        """ ConfigureSynchronizationModeAndInterval(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, synchronizationMode: RFmxLteMXSlotPhaseSynchronizationMode, measurementOffset: int, measurementLength: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetCommonClockSourceEnabled(self, selectorString, value):
        """ GetCommonClockSourceEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, RFmxLteMXSlotPhaseCommonClockSourceEnabled) """
        pass

    def GetExclusionPeriodEnabled(self, selectorString, value):
        """ GetExclusionPeriodEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, RFmxLteMXSlotPhaseExclusionPeriodEnabled) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementLength(self, selectorString, value):
        """ GetMeasurementLength(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSpectrumInverted(self, selectorString, value):
        """ GetSpectrumInverted(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, RFmxLteMXSlotPhaseSpectrumInverted) """
        pass

    def GetSynchronizationMode(self, selectorString, value):
        """ GetSynchronizationMode(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str) -> (int, RFmxLteMXSlotPhaseSynchronizationMode) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetCommonClockSourceEnabled(self, selectorString, value):
        """ SetCommonClockSourceEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: RFmxLteMXSlotPhaseCommonClockSourceEnabled) -> int """
        pass

    def SetExclusionPeriodEnabled(self, selectorString, value):
        """ SetExclusionPeriodEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: RFmxLteMXSlotPhaseExclusionPeriodEnabled) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementLength(self, selectorString, value):
        """ SetMeasurementLength(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSpectrumInverted(self, selectorString, value):
        """ SetSpectrumInverted(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: RFmxLteMXSlotPhaseSpectrumInverted) -> int """
        pass

    def SetSynchronizationMode(self, selectorString, value):
        """ SetSynchronizationMode(self: RFmxLteMXSlotPhaseConfiguration, selectorString: str, value: RFmxLteMXSlotPhaseSynchronizationMode) -> int """
        pass


class RFmxLteMXSlotPhaseExclusionPeriodEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSlotPhaseExclusionPeriodEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSlotPhaseResults(RFmxLteMXSubObject):
    # no doc
    def FetchMaximumPhaseDiscontinuity(self, selectorString, timeout, maximumPhaseDiscontinuity):
        """ FetchMaximumPhaseDiscontinuity(self: RFmxLteMXSlotPhaseResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchMaximumPhaseDiscontinuityArray(self, selectorString, timeout, maximumPhaseDiscontinuity):
        """ FetchMaximumPhaseDiscontinuityArray(self: RFmxLteMXSlotPhaseResults, selectorString: str, timeout: float, maximumPhaseDiscontinuity: Array[float]) -> (int, Array[float]) """
        pass

    def FetchPhaseDiscontinuities(self, selectorString, timeout, slotPhaseDiscontinuity):
        """ FetchPhaseDiscontinuities(self: RFmxLteMXSlotPhaseResults, selectorString: str, timeout: float, slotPhaseDiscontinuity: Array[float]) -> (int, Array[float]) """
        pass

    def FetchSamplePhaseError(self, selectorString, timeout, samplePhaseError):
        """ FetchSamplePhaseError(self: RFmxLteMXSlotPhaseResults, selectorString: str, timeout: float, samplePhaseError: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSamplePhaseErrorLinearFitTrace(self, selectorString, timeout, samplePhaseErrorLinearFit):
        """ FetchSamplePhaseErrorLinearFitTrace(self: RFmxLteMXSlotPhaseResults, selectorString: str, timeout: float, samplePhaseErrorLinearFit: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def GetMaximumPhaseDiscontinuity(self, selectorString, value):
        """ GetMaximumPhaseDiscontinuity(self: RFmxLteMXSlotPhaseResults, selectorString: str) -> (int, float) """
        pass


class RFmxLteMXSlotPhaseSpectrumInverted(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSlotPhaseSpectrumInverted, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSlotPhaseSynchronizationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSlotPhaseSynchronizationMode, values: Frame (0), Slot (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSlotPower(RFmxLteMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxLteMXSlotPower) -> RFmxLteMXSlotPowerConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxLteMXSlotPower) -> RFmxLteMXSlotPowerResults

"""



class RFmxLteMXSlotPowerCommonClockSourceEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSlotPowerCommonClockSourceEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSlotPowerConfiguration(RFmxLteMXSubObject):
    # no doc
    def ConfigureMeasurementInterval(self, selectorString, measurementOffset, measurementLength):
        """ ConfigureMeasurementInterval(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, measurementOffset: int, measurementLength: int) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxLteMXSlotPowerConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetCommonClockSourceEnabled(self, selectorString, value):
        """ GetCommonClockSourceEnabled(self: RFmxLteMXSlotPowerConfiguration, selectorString: str) -> (int, RFmxLteMXSlotPowerCommonClockSourceEnabled) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxLteMXSlotPowerConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementLength(self, selectorString, value):
        """ GetMeasurementLength(self: RFmxLteMXSlotPowerConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxLteMXSlotPowerConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSpectrumInverted(self, selectorString, value):
        """ GetSpectrumInverted(self: RFmxLteMXSlotPowerConfiguration, selectorString: str) -> (int, RFmxLteMXSlotPowerSpectrumInverted) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetCommonClockSourceEnabled(self, selectorString, value):
        """ SetCommonClockSourceEnabled(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, value: RFmxLteMXSlotPowerCommonClockSourceEnabled) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementLength(self, selectorString, value):
        """ SetMeasurementLength(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSpectrumInverted(self, selectorString, value):
        """ SetSpectrumInverted(self: RFmxLteMXSlotPowerConfiguration, selectorString: str, value: RFmxLteMXSlotPowerSpectrumInverted) -> int """
        pass


class RFmxLteMXSlotPowerResults(RFmxLteMXSubObject):
    # no doc
    def FetchPowers(self, selectorString, timeout, subframePower, subframePowerDelta):
        """ FetchPowers(self: RFmxLteMXSlotPowerResults, selectorString: str, timeout: float, subframePower: Array[float], subframePowerDelta: Array[float]) -> (int, Array[float], Array[float]) """
        pass


class RFmxLteMXSlotPowerSpectrumInverted(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSlotPowerSpectrumInverted, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSrsEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSrsEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSrsMaximumUpPtsEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSrsMaximumUpPtsEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXSubblockFrequencyDefinition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXSubblockFrequencyDefinition, values: Absolute (1), Relative (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXTransmitterArchitecture(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXTransmitterArchitecture, values: LOPerComponentCarrier (0), LOPerSubblock (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXTriggerMinimumQuietTimeMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXTriggerMinimumQuietTimeMode, values: Auto (1), Manual (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXTriggerType, values: DigitalEdge (1), IQPowerEdge (2), None (0), Software (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXUplinkDownlinkConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXUplinkDownlinkConfiguration, values: Configuration0 (0), Configuration1 (1), Configuration2 (2), Configuration3 (3), Configuration4 (4), Configuration5 (5), Configuration6 (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Configuration0 = None
    Configuration1 = None
    Configuration2 = None
    Configuration3 = None
    Configuration4 = None
    Configuration5 = None
    Configuration6 = None
    value__ = None


class RFmxLteMXUplinkGroupHoppingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXUplinkGroupHoppingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXUplinkSequenceHoppingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXUplinkSequenceHoppingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxLteMXUserDefinedPdschCW0ModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxLteMXUserDefinedPdschCW0ModulationType, values: Qam1024 (4), Qam16 (1), Qam256 (3), Qam64 (2), Qpsk (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Qam1024 = None
    Qam16 = None
    Qam256 = None
    Qam64 = None
    Qpsk = None
    value__ = None


