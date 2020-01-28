# encoding: utf-8
# module NationalInstruments.RFmx.WlanMX calls itself WlanMX
# from NationalInstruments.RFmx.WlanMX.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RFmxWlanMX(object, ISignalConfiguration, IDisposable):
    # no doc
    def AbortMeasurements(self, selectorString):
        """ AbortMeasurements(self: RFmxWlanMX, selectorString: str) -> int """
        pass

    def AnalyzeIQ(self, selectorString, resultName, iq, reset, averagingDone):
        """ AnalyzeIQ(self: RFmxWlanMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool) -> (int, bool) """
        pass

    def AnalyzeIQ1Waveform(self, selectorString, resultName, iq, reset, reserved):
        """ AnalyzeIQ1Waveform(self: RFmxWlanMX, selectorString: str, resultName: str, iq: ComplexWaveform[ComplexSingle], reset: bool, reserved: Int64) -> int """
        pass

    def AnalyzeNWaveformsIQ(self, selectorString, resultName, iq, reset):
        """ AnalyzeNWaveformsIQ(self: RFmxWlanMX, selectorString: str, resultName: str, iq: Array[ComplexWaveform[ComplexSingle]], reset: bool) -> int """
        pass

    def AnalyzeNWaveformsSpectrum(self, selectorString, resultName, spectrum, reset):
        """ AnalyzeNWaveformsSpectrum(self: RFmxWlanMX, selectorString: str, resultName: str, spectrum: Array[Spectrum[Single]], reset: bool) -> int """
        pass

    def AnalyzeSpectrum(self, selectorString, resultName, spectrum, reset, averagingDone):
        """ AnalyzeSpectrum(self: RFmxWlanMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool) -> (int, bool) """
        pass

    def AnalyzeSpectrum1Waveform(self, selectorString, resultName, spectrum, reset, reserved):
        """ AnalyzeSpectrum1Waveform(self: RFmxWlanMX, selectorString: str, resultName: str, spectrum: Spectrum[Single], reset: bool, reserved: Int64) -> int """
        pass

    def AutoDetectSignal(self, selectorString, timeout):
        """ AutoDetectSignal(self: RFmxWlanMX, selectorString: str, timeout: float) -> int """
        pass

    def AutoLevel(self, selectorString, measurementInterval):
        """ AutoLevel(self: RFmxWlanMX, selectorString: str, measurementInterval: float) -> int """
        pass

    @staticmethod
    def BuildChainString(selectorString, chainNumber):
        """ BuildChainString(selectorString: str, chainNumber: int) -> str """
        pass

    @staticmethod
    def BuildGateString(selectorString, gateNumber):
        """ BuildGateString(selectorString: str, gateNumber: int) -> str """
        pass

    @staticmethod
    def BuildOffsetString(selectorString, offsetNumber):
        """ BuildOffsetString(selectorString: str, offsetNumber: int) -> str """
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
    def BuildStreamString(selectorString, streamNumber):
        """ BuildStreamString(selectorString: str, streamNumber: int) -> str """
        pass

    @staticmethod
    def BuildUserString(selectorString, userNumber):
        """ BuildUserString(selectorString: str, userNumber: int) -> str """
        pass

    def CheckMeasurementStatus(self, selectorString, isDone):
        """ CheckMeasurementStatus(self: RFmxWlanMX, selectorString: str) -> (int, bool) """
        pass

    def ClearAllNamedResults(self, selectorString):
        """ ClearAllNamedResults(self: RFmxWlanMX, selectorString: str) -> int """
        pass

    def ClearNamedResult(self, selectorString):
        """ ClearNamedResult(self: RFmxWlanMX, selectorString: str) -> int """
        pass

    def CloneSignalConfiguration(self, newSignalName, signalConfiguration):
        """ CloneSignalConfiguration(self: RFmxWlanMX, newSignalName: str) -> (int, RFmxWlanMX) """
        pass

    def Commit(self, selectorString):
        """ Commit(self: RFmxWlanMX, selectorString: str) -> int """
        pass

    def ConfigureChannelBandwidth(self, selectorString, channelBandwidth):
        """ ConfigureChannelBandwidth(self: RFmxWlanMX, selectorString: str, channelBandwidth: float) -> int """
        pass

    def ConfigureDigitalEdgeTrigger(self, selectorString, digitalEdgeTriggerSource, digitalEdgeTriggerEdge, triggerDelay, enableTrigger):
        """ ConfigureDigitalEdgeTrigger(self: RFmxWlanMX, selectorString: str, digitalEdgeTriggerSource: str, digitalEdgeTriggerEdge: RFmxWlanMXDigitalEdgeTriggerEdge, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def ConfigureExternalAttenuation(self, selectorString, externalAttenuation):
        """ ConfigureExternalAttenuation(self: RFmxWlanMX, selectorString: str, externalAttenuation: float) -> int """
        pass

    def ConfigureExternalAttenuationArray(self, selectorString, externalAttenuation):
        """ ConfigureExternalAttenuationArray(self: RFmxWlanMX, selectorString: str, externalAttenuation: Array[float]) -> int """
        pass

    def ConfigureFrequency(self, selectorString, centerFrequency):
        """ ConfigureFrequency(self: RFmxWlanMX, selectorString: str, centerFrequency: float) -> int """
        pass

    def ConfigureFrequencyArray(self, selectorString, centerFrequency):
        """ ConfigureFrequencyArray(self: RFmxWlanMX, selectorString: str, centerFrequency: Array[float]) -> int """
        pass

    def ConfigureIQPowerEdgeTrigger(self, selectorString, iqPowerEdgeTriggerSource, iqPowerEdgeTriggerSlope, iqPowerEdgeTriggerLevel, triggerDelay, minimumQuietTimeMode, minimumQuietTimeDuration, iqPowerEdgeTriggerLevelType, enableTrigger):
        """ ConfigureIQPowerEdgeTrigger(self: RFmxWlanMX, selectorString: str, iqPowerEdgeTriggerSource: str, iqPowerEdgeTriggerSlope: RFmxWlanMXIQPowerEdgeTriggerSlope, iqPowerEdgeTriggerLevel: float, triggerDelay: float, minimumQuietTimeMode: RFmxWlanMXTriggerMinimumQuietTimeMode, minimumQuietTimeDuration: float, iqPowerEdgeTriggerLevelType: RFmxWlanMXIQPowerEdgeTriggerLevelType, enableTrigger: bool) -> int """
        pass

    def ConfigureNumberOfFrequencySegmentsAndReceiveChains(self, selectorString, numberOfFrequencySegments, numberOfReceiveChains):
        """ ConfigureNumberOfFrequencySegmentsAndReceiveChains(self: RFmxWlanMX, selectorString: str, numberOfFrequencySegments: int, numberOfReceiveChains: int) -> int """
        pass

    def ConfigureReferenceLevel(self, selectorString, referenceLevel):
        """ ConfigureReferenceLevel(self: RFmxWlanMX, selectorString: str, referenceLevel: float) -> int """
        pass

    def ConfigureReferenceLevelArray(self, selectorString, referenceLevel):
        """ ConfigureReferenceLevelArray(self: RFmxWlanMX, selectorString: str, referenceLevel: Array[float]) -> int """
        pass

    def ConfigureReferenceLevelUnits(self, selectorString, referenceLevelUnits):
        """ ConfigureReferenceLevelUnits(self: RFmxWlanMX, selectorString: str, referenceLevelUnits: RFmxWlanMXReferenceLevelUnits) -> int """
        pass

    def ConfigureSelectedPortsMultiple(self, selectorString, selectedPorts):
        """ ConfigureSelectedPortsMultiple(self: RFmxWlanMX, selectorString: str, selectedPorts: Array[str]) -> int """
        pass

    def ConfigureSoftwareEdgeTrigger(self, selectorString, triggerDelay, enableTrigger):
        """ ConfigureSoftwareEdgeTrigger(self: RFmxWlanMX, selectorString: str, triggerDelay: float, enableTrigger: bool) -> int """
        pass

    def ConfigureStandard(self, selectorString, standard):
        """ ConfigureStandard(self: RFmxWlanMX, selectorString: str, standard: RFmxWlanMXStandard) -> int """
        pass

    def DeleteSignalConfiguration(self):
        """ DeleteSignalConfiguration(self: RFmxWlanMX) -> int """
        pass

    def DisableTrigger(self, selectorString):
        """ DisableTrigger(self: RFmxWlanMX, selectorString: str) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: RFmxWlanMX) """
        pass

    def GetAllNamedResultNames(self, selectorString, resultNames, defaultResultExists):
        """ GetAllNamedResultNames(self: RFmxWlanMX, selectorString: str) -> (int, Array[str], bool) """
        pass

    def GetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ GetAttributeBool(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int) -> (int, bool) """
        pass

    def GetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ GetAttributeDouble(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int) -> (int, float) """
        pass

    def GetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ GetAttributeInt(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int) -> (int, int) """
        pass

    def GetAttributeLong(self, selectorString, attributeIdentifier, value):
        """ GetAttributeLong(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int) -> (int, Int64) """
        pass

    def GetAttributeString(self, selectorString, attributeIdentifier, value):
        """ GetAttributeString(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int) -> (int, str) """
        pass

    def GetAutoLevelInitialReferenceLevel(self, selectorString, value):
        """ GetAutoLevelInitialReferenceLevel(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetCenterFrequency(self, selectorString, value):
        """ GetCenterFrequency(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetChannelBandwidth(self, selectorString, value):
        """ GetChannelBandwidth(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetChannelList(self, selectorString, wlanBand, centerFrequencies, channelBandwidths):
        """ GetChannelList(self: RFmxWlanMX, selectorString: str, wlanBand: int, centerFrequencies: Array[float], channelBandwidths: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def GetDetectedBurstLength(self, selectorString, value):
        """ GetDetectedBurstLength(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetDetectedChannelBandwidth(self, selectorString, value):
        """ GetDetectedChannelBandwidth(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetDetectedStandard(self, selectorString, value):
        """ GetDetectedStandard(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ GetDigitalEdgeTriggerEdge(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXDigitalEdgeTriggerEdge) """
        pass

    def GetDigitalEdgeTriggerSource(self, selectorString, value):
        """ GetDigitalEdgeTriggerSource(self: RFmxWlanMX, selectorString: str) -> (int, str) """
        pass

    def GetError(self, errorCode, errorDescription):
        """ GetError(self: RFmxWlanMX) -> (int, int, str) """
        pass

    def GetErrorString(self, errorCode, errorDescription):
        """ GetErrorString(self: RFmxWlanMX, errorCode: int) -> (int, str) """
        pass

    def GetExternalAttenuation(self, selectorString, value):
        """ GetExternalAttenuation(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevel(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ GetIQPowerEdgeTriggerLevelType(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXIQPowerEdgeTriggerLevelType) """
        pass

    def GetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSlope(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXIQPowerEdgeTriggerSlope) """
        pass

    def GetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ GetIQPowerEdgeTriggerSource(self: RFmxWlanMX, selectorString: str) -> (int, str) """
        pass

    def GetLimitedConfigurationChange(self, selectorString, value):
        """ GetLimitedConfigurationChange(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXLimitedConfigurationChange) """
        pass

    def GetOfdmAutoPpduTypeDetectionEnabled(self, selectorString, value):
        """ GetOfdmAutoPpduTypeDetectionEnabled(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) """
        pass

    def GetOfdmDcmEnabled(self, selectorString, value):
        """ GetOfdmDcmEnabled(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmDcmEnabled) """
        pass

    def GetOfdmFrequencyBand(self, selectorString, value):
        """ GetOfdmFrequencyBand(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmFrequencyBand) """
        pass

    def GetOfdmGuardIntervalType(self, selectorString, value):
        """ GetOfdmGuardIntervalType(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmGuardIntervalType) """
        pass

    def GetOfdmHeaderDecodingEnabled(self, selectorString, value):
        """ GetOfdmHeaderDecodingEnabled(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmHeaderDecodingEnabled) """
        pass

    def GetOfdmHELtfSize(self, selectorString, value):
        """ GetOfdmHELtfSize(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmHELtfSize) """
        pass

    def GetOfdmMcsIndex(self, selectorString, value):
        """ GetOfdmMcsIndex(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmMUMimoLtfModeEnabled(self, selectorString, value):
        """ GetOfdmMUMimoLtfModeEnabled(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmMUMimoLtfModeEnabled) """
        pass

    def GetOfdmNumberHELtfSymbols(self, selectorString, value):
        """ GetOfdmNumberHELtfSymbols(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmNumberOfHESigBSymbols(self, selectorString, value):
        """ GetOfdmNumberOfHESigBSymbols(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmNumberOfUsers(self, selectorString, value):
        """ GetOfdmNumberOfUsers(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmPEDisambiguity(self, selectorString, value):
        """ GetOfdmPEDisambiguity(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmPpduType(self, selectorString, value):
        """ GetOfdmPpduType(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmPpduType) """
        pass

    def GetOfdmPreamblePuncturingBitmap(self, selectorString, value):
        """ GetOfdmPreamblePuncturingBitmap(self: RFmxWlanMX, selectorString: str) -> (int, Int64) """
        pass

    def GetOfdmPreamblePuncturingEnabled(self, selectorString, value):
        """ GetOfdmPreamblePuncturingEnabled(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmPreamblePuncturingEnabled) """
        pass

    def GetOfdmRUOffset(self, selectorString, value):
        """ GetOfdmRUOffset(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmRUSize(self, selectorString, value):
        """ GetOfdmRUSize(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmSpaceTimeStreamOffset(self, selectorString, value):
        """ GetOfdmSpaceTimeStreamOffset(self: RFmxWlanMX, selectorString: str) -> (int, int) """
        pass

    def GetOfdmTransmitPowerClass(self, selectorString, value):
        """ GetOfdmTransmitPowerClass(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXOfdmTransmitPowerClass) """
        pass

    def GetReferenceLevel(self, selectorString, value):
        """ GetReferenceLevel(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetReferenceLevelHeadroom(self, selectorString, value):
        """ GetReferenceLevelHeadroom(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetResultFetchTimeout(self, selectorString, value):
        """ GetResultFetchTimeout(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetSelectedPorts(self, selectorString, value):
        """ GetSelectedPorts(self: RFmxWlanMX, selectorString: str) -> (int, str) """
        pass

    def GetStandard(self, selectorString, value):
        """ GetStandard(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXStandard) """
        pass

    def GetTriggerDelay(self, selectorString, value):
        """ GetTriggerDelay(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerGateEnabled(self, selectorString, value):
        """ GetTriggerGateEnabled(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXTriggerGateEnabled) """
        pass

    def GetTriggerGateLength(self, selectorString, value):
        """ GetTriggerGateLength(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeDuration(self: RFmxWlanMX, selectorString: str) -> (int, float) """
        pass

    def GetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ GetTriggerMinimumQuietTimeMode(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXTriggerMinimumQuietTimeMode) """
        pass

    def GetTriggerType(self, selectorString, value):
        """ GetTriggerType(self: RFmxWlanMX, selectorString: str) -> (int, RFmxWlanMXTriggerType) """
        pass

    def GetWarning(self, warningCode, warningDescription):
        """ GetWarning(self: RFmxWlanMX) -> (int, int, str) """
        pass

    def Initiate(self, selectorString, resultName):
        """ Initiate(self: RFmxWlanMX, selectorString: str, resultName: str) -> int """
        pass

    def ResetAttribute(self, selectorString, attributeId):
        """ ResetAttribute(self: RFmxWlanMX, selectorString: str, attributeId: RFmxWlanMXPropertyId) -> int """
        pass

    def ResetToDefault(self, selectorString):
        """ ResetToDefault(self: RFmxWlanMX, selectorString: str) -> int """
        pass

    def SelectMeasurements(self, selectorString, measurement, enableAllTraces):
        """ SelectMeasurements(self: RFmxWlanMX, selectorString: str, measurement: RFmxWlanMXMeasurementTypes, enableAllTraces: bool) -> int """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RFmxWlanMX) -> int """
        pass

    def SetAttributeBool(self, selectorString, attributeIdentifier, value):
        """ SetAttributeBool(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int, value: bool) -> int """
        pass

    def SetAttributeDouble(self, selectorString, attributeIdentifier, value):
        """ SetAttributeDouble(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int, value: float) -> int """
        pass

    def SetAttributeInt(self, selectorString, attributeIdentifier, value):
        """ SetAttributeInt(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int, value: int) -> int """
        pass

    def SetAttributeLong(self, selectorString, attributeIdentifier, value):
        """ SetAttributeLong(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int, value: Int64) -> int """
        pass

    def SetAttributeString(self, selectorString, attributeIdentifier, value):
        """ SetAttributeString(self: RFmxWlanMX, selectorString: str, attributeIdentifier: int, value: str) -> int """
        pass

    def SetAutoLevelInitialReferenceLevel(self, selectorString, value):
        """ SetAutoLevelInitialReferenceLevel(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetCenterFrequency(self, selectorString, value):
        """ SetCenterFrequency(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetChannelBandwidth(self, selectorString, value):
        """ SetChannelBandwidth(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetDigitalEdgeTriggerEdge(self, selectorString, value):
        """ SetDigitalEdgeTriggerEdge(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXDigitalEdgeTriggerEdge) -> int """
        pass

    def SetDigitalEdgeTriggerSource(self, selectorString, value):
        """ SetDigitalEdgeTriggerSource(self: RFmxWlanMX, selectorString: str, value: str) -> int """
        pass

    def SetExternalAttenuation(self, selectorString, value):
        """ SetExternalAttenuation(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevel(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevel(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetIQPowerEdgeTriggerLevelType(self, selectorString, value):
        """ SetIQPowerEdgeTriggerLevelType(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXIQPowerEdgeTriggerLevelType) -> int """
        pass

    def SetIQPowerEdgeTriggerSlope(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSlope(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXIQPowerEdgeTriggerSlope) -> int """
        pass

    def SetIQPowerEdgeTriggerSource(self, selectorString, value):
        """ SetIQPowerEdgeTriggerSource(self: RFmxWlanMX, selectorString: str, value: str) -> int """
        pass

    def SetLimitedConfigurationChange(self, selectorString, value):
        """ SetLimitedConfigurationChange(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXLimitedConfigurationChange) -> int """
        pass

    def SetOfdmAutoPpduTypeDetectionEnabled(self, selectorString, value):
        """ SetOfdmAutoPpduTypeDetectionEnabled(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled) -> int """
        pass

    def SetOfdmDcmEnabled(self, selectorString, value):
        """ SetOfdmDcmEnabled(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmDcmEnabled) -> int """
        pass

    def SetOfdmFrequencyBand(self, selectorString, value):
        """ SetOfdmFrequencyBand(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmFrequencyBand) -> int """
        pass

    def SetOfdmGuardIntervalType(self, selectorString, value):
        """ SetOfdmGuardIntervalType(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmGuardIntervalType) -> int """
        pass

    def SetOfdmHeaderDecodingEnabled(self, selectorString, value):
        """ SetOfdmHeaderDecodingEnabled(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmHeaderDecodingEnabled) -> int """
        pass

    def SetOfdmHELtfSize(self, selectorString, value):
        """ SetOfdmHELtfSize(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmHELtfSize) -> int """
        pass

    def SetOfdmMcsIndex(self, selectorString, value):
        """ SetOfdmMcsIndex(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmMUMimoLtfModeEnabled(self, selectorString, value):
        """ SetOfdmMUMimoLtfModeEnabled(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmMUMimoLtfModeEnabled) -> int """
        pass

    def SetOfdmNumberHELtfSymbols(self, selectorString, value):
        """ SetOfdmNumberHELtfSymbols(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmNumberOfHESigBSymbols(self, selectorString, value):
        """ SetOfdmNumberOfHESigBSymbols(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmNumberOfUsers(self, selectorString, value):
        """ SetOfdmNumberOfUsers(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmPEDisambiguity(self, selectorString, value):
        """ SetOfdmPEDisambiguity(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmPpduType(self, selectorString, value):
        """ SetOfdmPpduType(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmPpduType) -> int """
        pass

    def SetOfdmPreamblePuncturingBitmap(self, selectorString, value):
        """ SetOfdmPreamblePuncturingBitmap(self: RFmxWlanMX, selectorString: str, value: Int64) -> int """
        pass

    def SetOfdmPreamblePuncturingEnabled(self, selectorString, value):
        """ SetOfdmPreamblePuncturingEnabled(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmPreamblePuncturingEnabled) -> int """
        pass

    def SetOfdmRUOffset(self, selectorString, value):
        """ SetOfdmRUOffset(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmRUSize(self, selectorString, value):
        """ SetOfdmRUSize(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmSpaceTimeStreamOffset(self, selectorString, value):
        """ SetOfdmSpaceTimeStreamOffset(self: RFmxWlanMX, selectorString: str, value: int) -> int """
        pass

    def SetOfdmTransmitPowerClass(self, selectorString, value):
        """ SetOfdmTransmitPowerClass(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXOfdmTransmitPowerClass) -> int """
        pass

    def SetReferenceLevel(self, selectorString, value):
        """ SetReferenceLevel(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetReferenceLevelHeadroom(self, selectorString, value):
        """ SetReferenceLevelHeadroom(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetResultFetchTimeout(self, selectorString, value):
        """ SetResultFetchTimeout(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetSelectedPorts(self, selectorString, value):
        """ SetSelectedPorts(self: RFmxWlanMX, selectorString: str, value: str) -> int """
        pass

    def SetStandard(self, selectorString, value):
        """ SetStandard(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXStandard) -> int """
        pass

    def SetTriggerDelay(self, selectorString, value):
        """ SetTriggerDelay(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerGateEnabled(self, selectorString, value):
        """ SetTriggerGateEnabled(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXTriggerGateEnabled) -> int """
        pass

    def SetTriggerGateLength(self, selectorString, value):
        """ SetTriggerGateLength(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeDuration(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeDuration(self: RFmxWlanMX, selectorString: str, value: float) -> int """
        pass

    def SetTriggerMinimumQuietTimeMode(self, selectorString, value):
        """ SetTriggerMinimumQuietTimeMode(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXTriggerMinimumQuietTimeMode) -> int """
        pass

    def SetTriggerType(self, selectorString, value):
        """ SetTriggerType(self: RFmxWlanMX, selectorString: str, value: RFmxWlanMXTriggerType) -> int """
        pass

    def WaitForMeasurementComplete(self, selectorString, timeout):
        """ WaitForMeasurementComplete(self: RFmxWlanMX, selectorString: str, timeout: float) -> int """
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

    DsssModAcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DsssModAcc(self: RFmxWlanMX) -> RFmxWlanMXDsssModAcc

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: RFmxWlanMX) -> bool

"""

    OfdmModAcc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OfdmModAcc(self: RFmxWlanMX) -> RFmxWlanMXOfdmModAcc

"""

    PowerRamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerRamp(self: RFmxWlanMX) -> RFmxWlanMXPowerRamp

"""

    Sem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sem(self: RFmxWlanMX) -> RFmxWlanMXSem

"""

    SignalConfigurationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationName(self: RFmxWlanMX) -> str

"""

    SignalConfigurationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConfigurationType(self: RFmxWlanMX) -> Type

"""

    Txp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Txp(self: RFmxWlanMX) -> RFmxWlanMXTxp

"""



class RFmxWlanMXConstants(object):
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


class RFmxWlanMXDigitalEdgeTriggerEdge(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDigitalEdgeTriggerEdge, values: Falling (1), Rising (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSubObject(object):
    # no doc

class RFmxWlanMXDsssModAcc(RFmxWlanMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxWlanMXDsssModAcc) -> RFmxWlanMXDsssModAccConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxWlanMXDsssModAcc) -> RFmxWlanMXDsssModAccResults

"""



class RFmxWlanMXDsssModAccAcquisitionLengthMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccAcquisitionLengthMode, values: Auto (1), Manual (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccBurstStartDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccBurstStartDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccConfiguration(RFmxWlanMXSubObject):
    # no doc
    def ConfigureAcquisitionLength(self, selectorString, acquisitionLengthMode, acquisitionLength):
        """ ConfigureAcquisitionLength(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, acquisitionLengthMode: RFmxWlanMXDsssModAccAcquisitionLengthMode, acquisitionLength: float) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, averagingEnabled: RFmxWlanMXDsssModAccAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureEvmUnit(self, selectorString, evmUnit):
        """ ConfigureEvmUnit(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, evmUnit: RFmxWlanMXDsssModAccEvmUnit) -> int """
        pass

    def ConfigureMeasurementLength(self, selectorString, measurementOffset, maximumMeasurementLength):
        """ ConfigureMeasurementLength(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, measurementOffset: int, maximumMeasurementLength: int) -> int """
        pass

    def ConfigurePowerMeasurementCustomGateArray(self, selectorString, startTime, stopTime):
        """ ConfigurePowerMeasurementCustomGateArray(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, startTime: Array[float], stopTime: Array[float]) -> int """
        pass

    def ConfigurePowerMeasurementEnabled(self, selectorString, powerMeasurementEnabled):
        """ ConfigurePowerMeasurementEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, powerMeasurementEnabled: RFmxWlanMXDsssModAccPowerMeasurementEnabled) -> int """
        pass

    def ConfigurePowerMeasurementNumberOfCustomGates(self, selectorString, numberOfCustomGates):
        """ ConfigurePowerMeasurementNumberOfCustomGates(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, numberOfCustomGates: int) -> int """
        pass

    def GetAcquisitionLength(self, selectorString, value):
        """ GetAcquisitionLength(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetAcquisitionLengthMode(self, selectorString, value):
        """ GetAcquisitionLengthMode(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccAcquisitionLengthMode) """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccAveragingEnabled) """
        pass

    def GetBurstStartDetectionEnabled(self, selectorString, value):
        """ GetBurstStartDetectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccBurstStartDetectionEnabled) """
        pass

    def GetChipClockErrorCorrectionEnabled(self, selectorString, value):
        """ GetChipClockErrorCorrectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled) """
        pass

    def GetEqualizationEnabled(self, selectorString, value):
        """ GetEqualizationEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccEqualizationEnabled) """
        pass

    def GetEvmUnit(self, selectorString, value):
        """ GetEvmUnit(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccEvmUnit) """
        pass

    def GetFrequencyErrorCorrectionEnabled(self, selectorString, value):
        """ GetFrequencyErrorCorrectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled) """
        pass

    def GetIQOriginOffsetCorrectionEnabled(self, selectorString, value):
        """ GetIQOriginOffsetCorrectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled) """
        pass

    def GetMaximumMeasurementLength(self, selectorString, value):
        """ GetMaximumMeasurementLength(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetPowerCustomGateStartTime(self, selectorString, value):
        """ GetPowerCustomGateStartTime(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPowerCustomGateStopTime(self, selectorString, value):
        """ GetPowerCustomGateStopTime(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPowerMeasurementEnabled(self, selectorString, value):
        """ GetPowerMeasurementEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccPowerMeasurementEnabled) """
        pass

    def GetPowerNumberOfCustomGates(self, selectorString, value):
        """ GetPowerNumberOfCustomGates(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetPulseShapingFilterParameter(self, selectorString, value):
        """ GetPulseShapingFilterParameter(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPulseShapingFilterType(self, selectorString, value):
        """ GetPulseShapingFilterType(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccPulseShapingFilterType) """
        pass

    def GetSpectrumInverted(self, selectorString, value):
        """ GetSpectrumInverted(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXDsssModAccSpectrumInverted) """
        pass

    def SetAcquisitionLength(self, selectorString, value):
        """ SetAcquisitionLength(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetAcquisitionLengthMode(self, selectorString, value):
        """ SetAcquisitionLengthMode(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccAcquisitionLengthMode) -> int """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccAveragingEnabled) -> int """
        pass

    def SetBurstStartDetectionEnabled(self, selectorString, value):
        """ SetBurstStartDetectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccBurstStartDetectionEnabled) -> int """
        pass

    def SetChipClockErrorCorrectionEnabled(self, selectorString, value):
        """ SetChipClockErrorCorrectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccChipClockErrorCorrectionEnabled) -> int """
        pass

    def SetEqualizationEnabled(self, selectorString, value):
        """ SetEqualizationEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccEqualizationEnabled) -> int """
        pass

    def SetEvmUnit(self, selectorString, value):
        """ SetEvmUnit(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccEvmUnit) -> int """
        pass

    def SetFrequencyErrorCorrectionEnabled(self, selectorString, value):
        """ SetFrequencyErrorCorrectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled) -> int """
        pass

    def SetIQOriginOffsetCorrectionEnabled(self, selectorString, value):
        """ SetIQOriginOffsetCorrectionEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled) -> int """
        pass

    def SetMaximumMeasurementLength(self, selectorString, value):
        """ SetMaximumMeasurementLength(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetPowerCustomGateStartTime(self, selectorString, value):
        """ SetPowerCustomGateStartTime(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPowerCustomGateStopTime(self, selectorString, value):
        """ SetPowerCustomGateStopTime(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPowerMeasurementEnabled(self, selectorString, value):
        """ SetPowerMeasurementEnabled(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccPowerMeasurementEnabled) -> int """
        pass

    def SetPowerNumberOfCustomGates(self, selectorString, value):
        """ SetPowerNumberOfCustomGates(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetPulseShapingFilterParameter(self, selectorString, value):
        """ SetPulseShapingFilterParameter(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPulseShapingFilterType(self, selectorString, value):
        """ SetPulseShapingFilterType(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccPulseShapingFilterType) -> int """
        pass

    def SetSpectrumInverted(self, selectorString, value):
        """ SetSpectrumInverted(self: RFmxWlanMXDsssModAccConfiguration, selectorString: str, value: RFmxWlanMXDsssModAccSpectrumInverted) -> int """
        pass


class RFmxWlanMXDsssModAccDataModulationFormat(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccDataModulationFormat, values: Cck11Mbps (3), Cck5_5Mbps (2), Dsss1Mbps (0), Dsss2Mbps (1), Pbcc11Mbps (5), Pbcc22Mbps (6), Pbcc33Mbps (7), Pbcc5_5Mbps (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Cck11Mbps = None
    Cck5_5Mbps = None
    Dsss1Mbps = None
    Dsss2Mbps = None
    Pbcc11Mbps = None
    Pbcc22Mbps = None
    Pbcc33Mbps = None
    Pbcc5_5Mbps = None
    value__ = None


class RFmxWlanMXDsssModAccEqualizationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccEqualizationEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccEvmUnit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccEvmUnit, values: dB (1), Percentage (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccFrequencyErrorCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccIQOriginOffsetCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccPayloadHeaderCrcStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccPayloadHeaderCrcStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccPowerMeasurementEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccPowerMeasurementEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXDsssModAccPreambleType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccPreambleType, values: Long (0), Short (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Long = None
    Short = None
    value__ = None


class RFmxWlanMXDsssModAccPulseShapingFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccPulseShapingFilterType, values: RaisedCosine (1), Rectangular (0), RootRaisedCosine (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    RaisedCosine = None
    Rectangular = None
    RootRaisedCosine = None
    value__ = None


class RFmxWlanMXDsssModAccResults(RFmxWlanMXSubObject):
    # no doc
    def FetchAveragePowers(self, selectorString, timeout, preambleAveragePowerMean, headerAveragePowerMean, dataAveragePowerMean, ppduAveragePowerMean):
        """ FetchAveragePowers(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchConstellationTrace(self, selectorString, timeout, constellation):
        """ FetchConstellationTrace(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float, constellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchCustomGatePowersArray(self, selectorString, timeout, averagePowerMean, peakPowerMaximum):
        """ FetchCustomGatePowersArray(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float, averagePowerMean: Array[float], peakPowerMaximum: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchEvm(self, selectorString, timeout, rmsEvmMean, peakEvm80211_2016Maximum, peakEvm80211_2007Maximum, peakEvm80211_1999Maximum, frequencyErrorMean, chipClockErrorMean, numberOfChipsUsed):
        """ FetchEvm(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float, float, int) """
        pass

    def FetchEvmPerChipMeanTrace(self, selectorString, timeout, evmPerChipMean):
        """ FetchEvmPerChipMeanTrace(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float, evmPerChipMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchIQImpairments(self, selectorString, timeout, iqOriginOffsetMean, iqGainImbalanceMean, iqQuadratureErrorMean):
        """ FetchIQImpairments(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchPeakPowers(self, selectorString, timeout, preamblePeakPowerMaximum, headerPeakPowerMaximum, dataPeakPowerMaximum, ppduPeakPowerMaximum):
        """ FetchPeakPowers(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPpduInformation(self, selectorString, timeout, dataModulationFormat, payloadLength, preambleType, lockedClocksBit, headerCrcStatus, psduCrcStatus):
        """ FetchPpduInformation(self: RFmxWlanMXDsssModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXDsssModAccDataModulationFormat, int, RFmxWlanMXDsssModAccPreambleType, int, int, int) """
        pass

    def GetChipClockErrorMean(self, selectorString, value):
        """ GetChipClockErrorMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCustomGateAveragePowerMean(self, selectorString, value):
        """ GetCustomGateAveragePowerMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCustomGatePeakPowerMaximum(self, selectorString, value):
        """ GetCustomGatePeakPowerMaximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetDataAveragePowerMean(self, selectorString, value):
        """ GetDataAveragePowerMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetDataModulationFormat(self, selectorString, value):
        """ GetDataModulationFormat(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, RFmxWlanMXDsssModAccDataModulationFormat) """
        pass

    def GetDataPeakPowerMaximum(self, selectorString, value):
        """ GetDataPeakPowerMaximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyErrorMean(self, selectorString, value):
        """ GetFrequencyErrorMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHeaderAveragePowerMean(self, selectorString, value):
        """ GetHeaderAveragePowerMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHeaderCrcStatus(self, selectorString, value):
        """ GetHeaderCrcStatus(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, RFmxWlanMXDsssModAccPayloadHeaderCrcStatus) """
        pass

    def GetHeaderPeakPowerMaximum(self, selectorString, value):
        """ GetHeaderPeakPowerMaximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetIQGainImbalanceMean(self, selectorString, value):
        """ GetIQGainImbalanceMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetIQOriginOffsetMean(self, selectorString, value):
        """ GetIQOriginOffsetMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetIQQuadratureErrorMean(self, selectorString, value):
        """ GetIQQuadratureErrorMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLockedClocksBit(self, selectorString, value):
        """ GetLockedClocksBit(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfChipsUsed(self, selectorString, value):
        """ GetNumberOfChipsUsed(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetPayloadLength(self, selectorString, value):
        """ GetPayloadLength(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetPeakEvm802_11_1999Maximum(self, selectorString, value):
        """ GetPeakEvm802_11_1999Maximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakEvm802_11_1999Mean(self, selectorString, value):
        """ GetPeakEvm802_11_1999Mean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakEvm802_11_2007Maximum(self, selectorString, value):
        """ GetPeakEvm802_11_2007Maximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakEvm802_11_2007Mean(self, selectorString, value):
        """ GetPeakEvm802_11_2007Mean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakEvm802_11_2016Maximum(self, selectorString, value):
        """ GetPeakEvm802_11_2016Maximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakEvm802_11_2016Mean(self, selectorString, value):
        """ GetPeakEvm802_11_2016Mean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPpduAveragePowerMean(self, selectorString, value):
        """ GetPpduAveragePowerMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPpduPeakPowerMaximum(self, selectorString, value):
        """ GetPpduPeakPowerMaximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPreambleAveragePowerMean(self, selectorString, value):
        """ GetPreambleAveragePowerMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPreamblePeakPowerMaximum(self, selectorString, value):
        """ GetPreamblePeakPowerMaximum(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPreambleType(self, selectorString, value):
        """ GetPreambleType(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, RFmxWlanMXDsssModAccPreambleType) """
        pass

    def GetRmsEvmMean(self, selectorString, value):
        """ GetRmsEvmMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRmsMagnitudeErrorMean(self, selectorString, value):
        """ GetRmsMagnitudeErrorMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRmsPhaseErrorMean(self, selectorString, value):
        """ GetRmsPhaseErrorMean(self: RFmxWlanMXDsssModAccResults, selectorString: str) -> (int, float) """
        pass


class RFmxWlanMXDsssModAccSpectrumInverted(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXDsssModAccSpectrumInverted, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXIQPowerEdgeTriggerLevelType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXIQPowerEdgeTriggerLevelType, values: Absolute (1), Relative (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXIQPowerEdgeTriggerSlope(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXIQPowerEdgeTriggerSlope, values: Falling (1), Rising (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXLimitedConfigurationChange(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXLimitedConfigurationChange, values: Disabled (0), Frequency (2), FrequencyAndReferenceLevel (4), NoChange (1), ReferenceLevel (3), SelectedPortsFrequencyAndReferenceLevel (5) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXMeasurementTypes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RFmxWlanMXMeasurementTypes, values: DsssModAcc (4), OfdmModAcc (8), PowerRamp (2), Sem (16), Txp (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DsssModAcc = None
    OfdmModAcc = None
    PowerRamp = None
    Sem = None
    Txp = None
    value__ = None


class RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmAutoPpduTypeDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmDcmEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmDcmEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmFrequencyBand(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmFrequencyBand, values: Band2_4GHz (0), Band5GHz (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Band2_4GHz = None
    Band5GHz = None
    value__ = None


class RFmxWlanMXOfdmGuardIntervalType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmGuardIntervalType, values: OneByEight (1), OneByFour (0), OneBySixteen (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    OneByEight = None
    OneByFour = None
    OneBySixteen = None
    value__ = None


class RFmxWlanMXOfdmHeaderDecodingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmHeaderDecodingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmHELtfSize(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmHELtfSize, values: HELtfSize1x (2), HELtfSize2x (1), HELtfSize4x (0), NotApplicable (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HELtfSize1x = None
    HELtfSize2x = None
    HELtfSize4x = None
    NotApplicable = None
    value__ = None


class RFmxWlanMXOfdmModAcc(RFmxWlanMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxWlanMXOfdmModAcc) -> RFmxWlanMXOfdmModAccConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxWlanMXOfdmModAcc) -> RFmxWlanMXOfdmModAccResults

"""



class RFmxWlanMXOfdmModAccAcquisitionLengthMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccAcquisitionLengthMode, values: Auto (1), Manual (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccBurstStartDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccBurstStartDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccCalibrationDataValid(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccCalibrationDataValid, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccChannelEstimationSmoothingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccChannelEstimationSmoothingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccChannelEstimationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccChannelEstimationType, values: ChannelEstimationReference (0), ChannelEstimationReferenceAndData (1), Reference (0), ReferenceAndData (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ChannelEstimationReference = None
    ChannelEstimationReferenceAndData = None
    Reference = None
    ReferenceAndData = None
    value__ = None


class RFmxWlanMXOfdmModAccCommonClockSourceEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccCommonClockSourceEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccConfiguration(RFmxWlanMXSubObject):
    # no doc
    def ConfigureAcquisitionLength(self, selectorString, acquisitionLengthMode, acquisitionLength):
        """ ConfigureAcquisitionLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, acquisitionLengthMode: RFmxWlanMXOfdmModAccAcquisitionLengthMode, acquisitionLength: float) -> int """
        pass

    def ConfigureAmplitudeTrackingEnabled(self, selectorString, amplitudeTrackingEnabled):
        """ ConfigureAmplitudeTrackingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, amplitudeTrackingEnabled: RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, averagingEnabled: RFmxWlanMXOfdmModAccAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureChannelEstimationType(self, selectorString, channelEstimationType):
        """ ConfigureChannelEstimationType(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, channelEstimationType: RFmxWlanMXOfdmModAccChannelEstimationType) -> int """
        pass

    def ConfigureCommonClockSourceEnabled(self, selectorString, commonClockSourceEnabled):
        """ ConfigureCommonClockSourceEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, commonClockSourceEnabled: RFmxWlanMXOfdmModAccCommonClockSourceEnabled) -> int """
        pass

    def ConfigureEvmUnit(self, selectorString, evmUnit):
        """ ConfigureEvmUnit(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, evmUnit: RFmxWlanMXOfdmModAccEvmUnit) -> int """
        pass

    def ConfigureFrequencyErrorEstimationMethod(self, selectorString, frequencyErrorEstimationMethod):
        """ ConfigureFrequencyErrorEstimationMethod(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, frequencyErrorEstimationMethod: RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod) -> int """
        pass

    def ConfigureMeasurementLength(self, selectorString, measurementOffset, maximumMeasurementLength):
        """ ConfigureMeasurementLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, measurementOffset: int, maximumMeasurementLength: int) -> int """
        pass

    def ConfigureMeasurementMode(self, selectorString, measurementMode):
        """ ConfigureMeasurementMode(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, measurementMode: RFmxWlanMXOfdmModAccMeasurementMode) -> int """
        pass

    def ConfigureNoiseCompensationEnabled(self, selectorString, noiseCompensationEnabled):
        """ ConfigureNoiseCompensationEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, noiseCompensationEnabled: RFmxWlanMXOfdmModAccNoiseCompensationEnabled) -> int """
        pass

    def ConfigureOptimizeDynamicRangeForEvm(self, selectorString, optimizeDynamicRangeForEvmEnabled, optimizeDynamicRangeForEvmMargin):
        """ ConfigureOptimizeDynamicRangeForEvm(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, optimizeDynamicRangeForEvmEnabled: RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled, optimizeDynamicRangeForEvmMargin: float) -> int """
        pass

    def ConfigurePhaseTrackingEnabled(self, selectorString, phaseTrackingEnabled):
        """ ConfigurePhaseTrackingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, phaseTrackingEnabled: RFmxWlanMXOfdmModAccPhaseTrackingEnabled) -> int """
        pass

    def ConfigureSymbolClockErrorCorrectionEnabled(self, selectorString, symbolClockErrorCorrectionEnabled):
        """ ConfigureSymbolClockErrorCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, symbolClockErrorCorrectionEnabled: RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled) -> int """
        pass

    def GetAcquisitionLength(self, selectorString, value):
        """ GetAcquisitionLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetAcquisitionLengthMode(self, selectorString, value):
        """ GetAcquisitionLengthMode(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccAcquisitionLengthMode) """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeTrackingEnabled(self, selectorString, value):
        """ GetAmplitudeTrackingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccAveragingEnabled) """
        pass

    def GetBurstStartDetectionEnabled(self, selectorString, value):
        """ GetBurstStartDetectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccBurstStartDetectionEnabled) """
        pass

    def GetChannelEstimationLLtfEnabled(self, selectorString, value):
        """ GetChannelEstimationLLtfEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled) """
        pass

    def GetChannelEstimationSmoothingEnabled(self, selectorString, value):
        """ GetChannelEstimationSmoothingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccChannelEstimationSmoothingEnabled) """
        pass

    def GetChannelEstimationSmoothingLength(self, selectorString, value):
        """ GetChannelEstimationSmoothingLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetChannelEstimationType(self, selectorString, value):
        """ GetChannelEstimationType(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccChannelEstimationType) """
        pass

    def GetCommonClockSourceEnabled(self, selectorString, value):
        """ GetCommonClockSourceEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccCommonClockSourceEnabled) """
        pass

    def GetEvmUnit(self, selectorString, value):
        """ GetEvmUnit(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccEvmUnit) """
        pass

    def GetFrequencyErrorEstimationMethod(self, selectorString, value):
        """ GetFrequencyErrorEstimationMethod(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod) """
        pass

    def GetIQGainImbalanceCorrectionEnabled(self, selectorString, value):
        """ GetIQGainImbalanceCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled) """
        pass

    def GetIQImpairmentsEstimationEnabled(self, selectorString, value):
        """ GetIQImpairmentsEstimationEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccIQImpairmentsEstimationEnabled) """
        pass

    def GetIQImpairmentsModel(self, selectorString, value):
        """ GetIQImpairmentsModel(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccIQImpairmentsModel) """
        pass

    def GetIQImpairmentsPerSubcarrierEnabled(self, selectorString, value):
        """ GetIQImpairmentsPerSubcarrierEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled) """
        pass

    def GetIQQuadratureErrorCorrectionEnabled(self, selectorString, value):
        """ GetIQQuadratureErrorCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled) """
        pass

    def GetIQTimingSkewCorrectionEnabled(self, selectorString, value):
        """ GetIQTimingSkewCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled) """
        pass

    def GetMaximumMeasurementLength(self, selectorString, value):
        """ GetMaximumMeasurementLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetMeasurementMode(self, selectorString, value):
        """ GetMeasurementMode(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccMeasurementMode) """
        pass

    def GetMeasurementOffset(self, selectorString, value):
        """ GetMeasurementOffset(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNoiseCompensationEnabled(self, selectorString, value):
        """ GetNoiseCompensationEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccNoiseCompensationEnabled) """
        pass

    def GetNoiseCompensationInputPowerCheckEnabled(self, selectorString, value):
        """ GetNoiseCompensationInputPowerCheckEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled) """
        pass

    def GetNoiseCompensationReferenceLevelCoercionLimit(self, selectorString, value):
        """ GetNoiseCompensationReferenceLevelCoercionLimit(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOptimizeDynamicRangeForEvmEnabled(self, selectorString, value):
        """ GetOptimizeDynamicRangeForEvmEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled) """
        pass

    def GetOptimizeDynamicRangeForEvmMargin(self, selectorString, value):
        """ GetOptimizeDynamicRangeForEvmMargin(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPhaseTrackingEnabled(self, selectorString, value):
        """ GetPhaseTrackingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccPhaseTrackingEnabled) """
        pass

    def GetPowerCustomGateStartTime(self, selectorString, value):
        """ GetPowerCustomGateStartTime(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPowerCustomGateStopTime(self, selectorString, value):
        """ GetPowerCustomGateStopTime(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetPowerMeasurementEnabled(self, selectorString, value):
        """ GetPowerMeasurementEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccPowerMeasurementEnabled) """
        pass

    def GetPowerNumberOfCustomGates(self, selectorString, value):
        """ GetPowerNumberOfCustomGates(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetSpectrumInverted(self, selectorString, value):
        """ GetSpectrumInverted(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccSpectrumInverted) """
        pass

    def GetSymbolClockErrorCorrectionEnabled(self, selectorString, value):
        """ GetSymbolClockErrorCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled) """
        pass

    def GetUnusedToneErrorMaskReference(self, selectorString, value):
        """ GetUnusedToneErrorMaskReference(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccUnusedToneErrorMaskReference) """
        pass

    def NoiseCalibrate(self, selectorString, sharedLOConnection):
        """ NoiseCalibrate(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, sharedLOConnection: bool) -> int """
        pass

    def SetAcquisitionLength(self, selectorString, value):
        """ SetAcquisitionLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetAcquisitionLengthMode(self, selectorString, value):
        """ SetAcquisitionLengthMode(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccAcquisitionLengthMode) -> int """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeTrackingEnabled(self, selectorString, value):
        """ SetAmplitudeTrackingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccAmplitudeTrackingEnabled) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccAveragingEnabled) -> int """
        pass

    def SetBurstStartDetectionEnabled(self, selectorString, value):
        """ SetBurstStartDetectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccBurstStartDetectionEnabled) -> int """
        pass

    def SetChannelEstimationLLtfEnabled(self, selectorString, value):
        """ SetChannelEstimationLLtfEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccChannelEstimationLLtfEnabled) -> int """
        pass

    def SetChannelEstimationSmoothingEnabled(self, selectorString, value):
        """ SetChannelEstimationSmoothingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccChannelEstimationSmoothingEnabled) -> int """
        pass

    def SetChannelEstimationSmoothingLength(self, selectorString, value):
        """ SetChannelEstimationSmoothingLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetChannelEstimationType(self, selectorString, value):
        """ SetChannelEstimationType(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccChannelEstimationType) -> int """
        pass

    def SetCommonClockSourceEnabled(self, selectorString, value):
        """ SetCommonClockSourceEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccCommonClockSourceEnabled) -> int """
        pass

    def SetEvmUnit(self, selectorString, value):
        """ SetEvmUnit(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccEvmUnit) -> int """
        pass

    def SetFrequencyErrorEstimationMethod(self, selectorString, value):
        """ SetFrequencyErrorEstimationMethod(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod) -> int """
        pass

    def SetIQGainImbalanceCorrectionEnabled(self, selectorString, value):
        """ SetIQGainImbalanceCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled) -> int """
        pass

    def SetIQImpairmentsEstimationEnabled(self, selectorString, value):
        """ SetIQImpairmentsEstimationEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccIQImpairmentsEstimationEnabled) -> int """
        pass

    def SetIQImpairmentsModel(self, selectorString, value):
        """ SetIQImpairmentsModel(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccIQImpairmentsModel) -> int """
        pass

    def SetIQImpairmentsPerSubcarrierEnabled(self, selectorString, value):
        """ SetIQImpairmentsPerSubcarrierEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled) -> int """
        pass

    def SetIQQuadratureErrorCorrectionEnabled(self, selectorString, value):
        """ SetIQQuadratureErrorCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled) -> int """
        pass

    def SetIQTimingSkewCorrectionEnabled(self, selectorString, value):
        """ SetIQTimingSkewCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled) -> int """
        pass

    def SetMaximumMeasurementLength(self, selectorString, value):
        """ SetMaximumMeasurementLength(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetMeasurementMode(self, selectorString, value):
        """ SetMeasurementMode(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccMeasurementMode) -> int """
        pass

    def SetMeasurementOffset(self, selectorString, value):
        """ SetMeasurementOffset(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNoiseCompensationEnabled(self, selectorString, value):
        """ SetNoiseCompensationEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccNoiseCompensationEnabled) -> int """
        pass

    def SetNoiseCompensationInputPowerCheckEnabled(self, selectorString, value):
        """ SetNoiseCompensationInputPowerCheckEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled) -> int """
        pass

    def SetNoiseCompensationReferenceLevelCoercionLimit(self, selectorString, value):
        """ SetNoiseCompensationReferenceLevelCoercionLimit(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOptimizeDynamicRangeForEvmEnabled(self, selectorString, value):
        """ SetOptimizeDynamicRangeForEvmEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled) -> int """
        pass

    def SetOptimizeDynamicRangeForEvmMargin(self, selectorString, value):
        """ SetOptimizeDynamicRangeForEvmMargin(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPhaseTrackingEnabled(self, selectorString, value):
        """ SetPhaseTrackingEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccPhaseTrackingEnabled) -> int """
        pass

    def SetPowerCustomGateStartTime(self, selectorString, value):
        """ SetPowerCustomGateStartTime(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPowerCustomGateStopTime(self, selectorString, value):
        """ SetPowerCustomGateStopTime(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetPowerMeasurementEnabled(self, selectorString, value):
        """ SetPowerMeasurementEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccPowerMeasurementEnabled) -> int """
        pass

    def SetPowerNumberOfCustomGates(self, selectorString, value):
        """ SetPowerNumberOfCustomGates(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetSpectrumInverted(self, selectorString, value):
        """ SetSpectrumInverted(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccSpectrumInverted) -> int """
        pass

    def SetSymbolClockErrorCorrectionEnabled(self, selectorString, value):
        """ SetSymbolClockErrorCorrectionEnabled(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled) -> int """
        pass

    def SetUnusedToneErrorMaskReference(self, selectorString, value):
        """ SetUnusedToneErrorMaskReference(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str, value: RFmxWlanMXOfdmModAccUnusedToneErrorMaskReference) -> int """
        pass

    def ValidateCalibrationData(self, selectorString, calibrationDataValid):
        """ ValidateCalibrationData(self: RFmxWlanMXOfdmModAccConfiguration, selectorString: str) -> (int, RFmxWlanMXOfdmModAccCalibrationDataValid) """
        pass


class RFmxWlanMXOfdmModAccEvmUnit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccEvmUnit, values: dB (1), Percentage (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccFrequencyErrorEstimationMethod, values: Disabled (0), InitialPreamble (1), Preamble (2), PreambleAndPilots (3), PreamblePilotsAndData (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    InitialPreamble = None
    Preamble = None
    PreambleAndPilots = None
    PreamblePilotsAndData = None
    value__ = None


class RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccIQGainImbalanceCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccIQImpairmentsEstimationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccIQImpairmentsEstimationEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccIQImpairmentsModel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccIQImpairmentsModel, values: RX (1), TX (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    RX = None
    TX = None
    value__ = None


class RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccIQImpairmentsPerSubcarrierEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccIQQuadratureErrorCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccIQTimingSkewCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccLSigParityCheckStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccLSigParityCheckStatus, values: Fail (0), NotApplicable (-1), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    NotApplicable = None
    Pass = None
    value__ = None


class RFmxWlanMXOfdmModAccMeasurementMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccMeasurementMode, values: CalibrateNoiseFloor (1), Measure (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CalibrateNoiseFloor = None
    Measure = None
    value__ = None


class RFmxWlanMXOfdmModAccNoiseCompensationApplied(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccNoiseCompensationApplied, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccNoiseCompensationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccNoiseCompensationEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccNoiseCompensationInputPowerCheckEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccOptimizeDynamicRangeForEvmEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccPhaseTrackingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccPhaseTrackingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccPowerMeasurementEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccPowerMeasurementEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccResults(RFmxWlanMXSubObject):
    # no doc
    def FetchChainDataRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, chainDataRmsEvmPerSymbolMean):
        """ FetchChainDataRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, chainDataRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchChainPilotRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, chainPilotRmsEvmPerSymbolMean):
        """ FetchChainPilotRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, chainPilotRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchChainRmsEvm(self, selectorString, timeout, chainRmsEvmMean, chainDataRmsEvmMean, chainPilotRmsEvmMean):
        """ FetchChainRmsEvm(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchChainRmsEvmPerSubcarrierMeanTrace(self, selectorString, timeout, chainRmsEvmPerSubcarrierMean):
        """ FetchChainRmsEvmPerSubcarrierMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, chainRmsEvmPerSubcarrierMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchChainRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, chainRmsEvmPerSymbolMean):
        """ FetchChainRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, chainRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchChannelFrequencyResponseMeanTrace(self, selectorString, timeout, channelFrequencyResponseMeanMagnitude, channelFrequencyResponseMeanPhase):
        """ FetchChannelFrequencyResponseMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, channelFrequencyResponseMeanMagnitude: AnalogWaveform[Single], channelFrequencyResponseMeanPhase: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchCommonPilotErrorTrace(self, selectorString, timeout, commonPilotErrorMagnitude, commonPilotErrorPhase):
        """ FetchCommonPilotErrorTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, commonPilotErrorMagnitude: AnalogWaveform[Single], commonPilotErrorPhase: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchCompositeRmsEvm(self, selectorString, timeout, compositeRmsEvmMean, compositeDataRmsEvmMean, compositePilotRmsEvmMean):
        """ FetchCompositeRmsEvm(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchCustomGatePowersArray(self, selectorString, timeout, averagePowerMean, peakPowerMaximum):
        """ FetchCustomGatePowersArray(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, averagePowerMean: Array[float], peakPowerMaximum: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchDataAveragePower(self, selectorString, timeout, dataAveragePowerMean):
        """ FetchDataAveragePower(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchDataConstellationTrace(self, selectorString, timeout, dataConstellation):
        """ FetchDataConstellationTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, dataConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchDataPeakPower(self, selectorString, timeout, dataPeakPowerMaximum):
        """ FetchDataPeakPower(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchEvmSubcarrierIndices(self, selectorString, timeout, subcarrierIndices):
        """ FetchEvmSubcarrierIndices(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, subcarrierIndices: Array[int]) -> (int, Array[int]) """
        pass

    def FetchFrequencyErrorCcdf10Percent(self, selectorString, timeout, frequencyErrorCcdf10Percent):
        """ FetchFrequencyErrorCcdf10Percent(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchFrequencyErrorMean(self, selectorString, timeout, frequencyErrorMean):
        """ FetchFrequencyErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchGuardIntervalType(self, selectorString, timeout, guardIntervalType):
        """ FetchGuardIntervalType(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXOfdmGuardIntervalType) """
        pass

    def FetchHELtfSize(self, selectorString, timeout, heLtfSize):
        """ FetchHELtfSize(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXOfdmHELtfSize) """
        pass

    def FetchHESigABits(self, selectorString, timeout, heSigABits):
        """ FetchHESigABits(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, heSigABits: Array[int]) -> (int, Array[int]) """
        pass

    def FetchHESigBBits(self, selectorString, timeout, heSigBBits):
        """ FetchHESigBBits(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, heSigBBits: Array[int]) -> (int, Array[int]) """
        pass

    def FetchHTSigBits(self, selectorString, timeout, htSigBits):
        """ FetchHTSigBits(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, htSigBits: Array[int]) -> (int, Array[int]) """
        pass

    def FetchIQGainImbalancePerSubcarrierMeanTrace(self, selectorString, timeout, iqGainImbalancePerSubcarrierMean):
        """ FetchIQGainImbalancePerSubcarrierMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, iqGainImbalancePerSubcarrierMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchIQImpairments(self, selectorString, timeout, relativeIQOriginOffsetMean, iqGainImbalanceMean, iqQuadratureErrorMean, absoluteIQOriginOffsetMean, iqTimingSkewMean):
        """ FetchIQImpairments(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchIQQuadratureErrorPerSubcarrierMeanTrace(self, selectorString, timeout, iqQuadratureErrorPerSubcarrierMean):
        """ FetchIQQuadratureErrorPerSubcarrierMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, iqQuadratureErrorPerSubcarrierMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchLSigBits(self, selectorString, timeout, lSigBits):
        """ FetchLSigBits(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, lSigBits: Array[int]) -> (int, Array[int]) """
        pass

    def FetchLSigParityCheckStatus(self, selectorString, timeout, lSigParityCheckStatus):
        """ FetchLSigParityCheckStatus(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXOfdmModAccLSigParityCheckStatus) """
        pass

    def FetchMcsIndex(self, selectorString, timeout, mcsIndex):
        """ FetchMcsIndex(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, int) """
        pass

    def FetchNumberOfHESigBSymbols(self, selectorString, timeout, numberOfHESigBSymbols):
        """ FetchNumberOfHESigBSymbols(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, int) """
        pass

    def FetchNumberOfSpaceTimeStreams(self, selectorString, timeout, numberOfSpaceTimeStreams):
        """ FetchNumberOfSpaceTimeStreams(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, int) """
        pass

    def FetchNumberOfSymbolsUsed(self, selectorString, timeout, numberOfSymbolsUsed):
        """ FetchNumberOfSymbolsUsed(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, int) """
        pass

    def FetchNumberOfUsers(self, selectorString, timeout, numberOfUsers):
        """ FetchNumberOfUsers(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, int) """
        pass

    def FetchPEAveragePower(self, selectorString, timeout, peAveragePowerMean):
        """ FetchPEAveragePower(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchPEPeakPower(self, selectorString, timeout, pePeakPowerMaximum):
        """ FetchPEPeakPower(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchPilotConstellationTrace(self, selectorString, timeout, pilotConstellation):
        """ FetchPilotConstellationTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, pilotConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchPpduAveragePower(self, selectorString, timeout, ppduAveragePowerMean):
        """ FetchPpduAveragePower(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchPpduPeakPower(self, selectorString, timeout, ppduPeakPowerMaximum):
        """ FetchPpduPeakPower(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchPpduType(self, selectorString, timeout, ppduType):
        """ FetchPpduType(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXOfdmPpduType) """
        pass

    def FetchPreambleAveragePowers802_11ac(self, selectorString, timeout, vhtSigAAveragePowerMean, vhtStfAveragePowerMean, vhtLtfAveragePowerMean, vhtSigBAveragePowerMean):
        """ FetchPreambleAveragePowers802_11ac(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPreambleAveragePowers802_11ax(self, selectorString, timeout, rlSigAveragePowerMean, heSigAAveragePowerMean, heSigBAveragePowerMean, heStfAveragePowerMean, heLtfAveragePowerMean):
        """ FetchPreambleAveragePowers802_11ax(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchPreambleAveragePowers802_11n(self, selectorString, timeout, htSigAveragePowerMean, htStfAveragePowerMean, htDltfAveragePowerMean, htEltfAveragePowerMean):
        """ FetchPreambleAveragePowers802_11n(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPreambleAveragePowersCommon(self, selectorString, timeout, lStfAveragePowerMean, lLtfAveragePowerMean, lSigAveragePowerMean):
        """ FetchPreambleAveragePowersCommon(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchPreambleFrequencyErrorTrace(self, selectorString, timeout, preambleFrequencyError):
        """ FetchPreambleFrequencyErrorTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, preambleFrequencyError: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchPreamblePeakPowers802_11ac(self, selectorString, timeout, vhtSigAPeakPowerMaximum, vhtStfPeakPowerMaximum, vhtLtfPeakPowerMaximum, vhtSigBPeakPowerMaximum):
        """ FetchPreamblePeakPowers802_11ac(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPreamblePeakPowers802_11ax(self, selectorString, timeout, rlSigPeakPowerMaximum, heSigAPeakPowerMaximum, heSigBPeakPowerMaximum, heStfPeakPowerMaximum, heLtfPeakPowerMaximum):
        """ FetchPreamblePeakPowers802_11ax(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchPreamblePeakPowers802_11n(self, selectorString, timeout, htSigPeakPowerMaximum, htStfPeakPowerMaximum, htDltfPeakPowerMaximum, htEltfPeakPowerMaximum):
        """ FetchPreamblePeakPowers802_11n(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float, float) """
        pass

    def FetchPreamblePeakPowersCommon(self, selectorString, timeout, lStfPeakPowerMaximum, lLtfPeakPowerMaximum, lSigPeakPowerMaximum):
        """ FetchPreamblePeakPowersCommon(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchRUOffsetAndSize(self, selectorString, timeout, ruOffset, ruSize):
        """ FetchRUOffsetAndSize(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, int, int) """
        pass

    def FetchSigBCrcStatus(self, selectorString, timeout, sigBCrcStatus):
        """ FetchSigBCrcStatus(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXOfdmModAccSigBCrcStatus) """
        pass

    def FetchSigCrcStatus(self, selectorString, timeout, sigCrcStatus):
        """ FetchSigCrcStatus(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXOfdmModAccSigCrcStatus) """
        pass

    def FetchSpectralFlatness(self, selectorString, timeout, spectralFlatnessMargin, spectralFlatnessMarginSubcarrierIndex):
        """ FetchSpectralFlatness(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, int) """
        pass

    def FetchSpectralFlatnessMeanTrace(self, selectorString, timeout, spectralFlatnessMean, spectralFlatnessLowerMask, spectralFlatnessUpperMask):
        """ FetchSpectralFlatnessMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, spectralFlatnessMean: AnalogWaveform[Single], spectralFlatnessLowerMask: AnalogWaveform[Single], spectralFlatnessUpperMask: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchStreamDataRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, streamDataRmsEvmPerSymbolMean):
        """ FetchStreamDataRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, streamDataRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchStreamPilotRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, streamPilotRmsEvmPerSymbolMean):
        """ FetchStreamPilotRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, streamPilotRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchStreamRmsEvm(self, selectorString, timeout, streamRmsEvmMean, streamDataRmsEvmMean, streamPilotRmsEvmMean):
        """ FetchStreamRmsEvm(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchStreamRmsEvmPerSubcarrierMeanTrace(self, selectorString, timeout, streamRmsEvmPerSubcarrierMean):
        """ FetchStreamRmsEvmPerSubcarrierMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, streamRmsEvmPerSubcarrierMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchStreamRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, streamRmsEvmPerSymbolMean):
        """ FetchStreamRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, streamRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSubcarrierChainEvmPerSymbolTrace(self, selectorString, timeout, subcarrierIndex, subcarrierChainEvmPerSymbol):
        """ FetchSubcarrierChainEvmPerSymbolTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, subcarrierIndex: int, subcarrierChainEvmPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSubcarrierStreamEvmPerSymbolTrace(self, selectorString, timeout, subcarrierIndex, subcarrierStreamEVMPerSymbol):
        """ FetchSubcarrierStreamEvmPerSymbolTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, subcarrierIndex: int, subcarrierStreamEVMPerSymbol: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSymbolChainEvmPerSubcarrierTrace(self, selectorString, timeout, symbolIndex, symbolChainEvmPerSubcarrier):
        """ FetchSymbolChainEvmPerSubcarrierTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, symbolIndex: int, symbolChainEvmPerSubcarrier: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchSymbolClockErrorMean(self, selectorString, timeout, symbolClockErrorMean):
        """ FetchSymbolClockErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchSymbolStreamEvmPerSubcarrierTrace(self, selectorString, timeout, symbolIndex, symbolStreamEvmPerSubcarrier):
        """ FetchSymbolStreamEvmPerSubcarrierTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, symbolIndex: int, symbolStreamEvmPerSubcarrier: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchUnusedToneError(self, selectorString, timeout, unusedToneErrorMargin, unusedToneErrorMarginRUIndex):
        """ FetchUnusedToneError(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, int) """
        pass

    def FetchUnusedToneErrorMarginPerRU(self, selectorString, timeout, unusedToneErrorMarginPerRU):
        """ FetchUnusedToneErrorMarginPerRU(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, unusedToneErrorMarginPerRU: Array[float]) -> (int, Array[float]) """
        pass

    def FetchUnusedToneErrorMeanTrace(self, selectorString, timeout, unusedToneError, unusedToneErrorMask):
        """ FetchUnusedToneErrorMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, unusedToneError: AnalogWaveform[Single], unusedToneErrorMask: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchUserDataConstellationTrace(self, selectorString, timeout, userDataConstellation):
        """ FetchUserDataConstellationTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, userDataConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchUserPilotConstellationTrace(self, selectorString, timeout, userPilotConstellation):
        """ FetchUserPilotConstellationTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, userPilotConstellation: Array[ComplexSingle]) -> (int, Array[ComplexSingle]) """
        pass

    def FetchUserStreamDataRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, userStreamDataRmsEvmPerSymbolMean):
        """ FetchUserStreamDataRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, userStreamDataRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchUserStreamPilotRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, userStreamPilotRmsEvmPerSymbolMean):
        """ FetchUserStreamPilotRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, userStreamPilotRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchUserStreamRmsEvm(self, selectorString, timeout, userStreamRmsEvmMean, userStreamDataRmsEvmMean, userStreamPilotRmsEvmMean):
        """ FetchUserStreamRmsEvm(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float) -> (int, float, float, float) """
        pass

    def FetchUserStreamRmsEvmPerSubcarrierMeanTrace(self, selectorString, timeout, userStreamRmsEvmPerSubcarrierMean):
        """ FetchUserStreamRmsEvmPerSubcarrierMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, userStreamRmsEvmPerSubcarrierMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchUserStreamRmsEvmPerSymbolMeanTrace(self, selectorString, timeout, userStreamRmsEvmPerSymbolMean):
        """ FetchUserStreamRmsEvmPerSymbolMeanTrace(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, userStreamRmsEvmPerSymbolMean: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def FetchVhtSigABits(self, selectorString, timeout, vhtSigABits):
        """ FetchVhtSigABits(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, vhtSigABits: Array[int]) -> (int, Array[int]) """
        pass

    def FetchVhtSigBBits(self, selectorString, timeout, vhtSigBBits):
        """ FetchVhtSigBBits(self: RFmxWlanMXOfdmModAccResults, selectorString: str, timeout: float, vhtSigBBits: Array[int]) -> (int, Array[int]) """
        pass

    def GetAbsoluteIQOriginOffsetMean(self, selectorString, value):
        """ GetAbsoluteIQOriginOffsetMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositeDataRmsEvmMean(self, selectorString, value):
        """ GetCompositeDataRmsEvmMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositePilotRmsEvmMean(self, selectorString, value):
        """ GetCompositePilotRmsEvmMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCompositeRmsEvmMean(self, selectorString, value):
        """ GetCompositeRmsEvmMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCustomGateAveragePowerMean(self, selectorString, value):
        """ GetCustomGateAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetCustomGatePeakPowerMaximum(self, selectorString, value):
        """ GetCustomGatePeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetDataAveragePowerMean(self, selectorString, value):
        """ GetDataAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetDataPeakPowerMaximum(self, selectorString, value):
        """ GetDataPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyErrorCcdf10Percent(self, selectorString, value):
        """ GetFrequencyErrorCcdf10Percent(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetFrequencyErrorMean(self, selectorString, value):
        """ GetFrequencyErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetGuardIntervalType(self, selectorString, value):
        """ GetGuardIntervalType(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmGuardIntervalType) """
        pass

    def GetHELtfAveragePowerMean(self, selectorString, value):
        """ GetHELtfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHELtfPeakPowerMaximum(self, selectorString, value):
        """ GetHELtfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHELtfSize(self, selectorString, value):
        """ GetHELtfSize(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmHELtfSize) """
        pass

    def GetHESigAAveragePowerMean(self, selectorString, value):
        """ GetHESigAAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHESigAPeakPowerMaximum(self, selectorString, value):
        """ GetHESigAPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHESigBAveragePowerMean(self, selectorString, value):
        """ GetHESigBAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHESigBPeakPowerMaximum(self, selectorString, value):
        """ GetHESigBPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHEStfAveragePowerMean(self, selectorString, value):
        """ GetHEStfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHEStfPeakPowerMaximum(self, selectorString, value):
        """ GetHEStfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTDltfAveragePowerMean(self, selectorString, value):
        """ GetHTDltfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTDltfPeakPowerMaximum(self, selectorString, value):
        """ GetHTDltfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTEltfAveragePowerMean(self, selectorString, value):
        """ GetHTEltfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTEltfPeakPowerMaximum(self, selectorString, value):
        """ GetHTEltfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTGFStfAveragePowerMean(self, selectorString, value):
        """ GetHTGFStfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTGFStfPeakPowerMaximum(self, selectorString, value):
        """ GetHTGFStfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTSigAveragePowerMean(self, selectorString, value):
        """ GetHTSigAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTSigPeakPowerMaximum(self, selectorString, value):
        """ GetHTSigPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTStfAveragePowerMean(self, selectorString, value):
        """ GetHTStfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetHTStfPeakPowerMaximum(self, selectorString, value):
        """ GetHTStfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetIQGainImbalanceMean(self, selectorString, value):
        """ GetIQGainImbalanceMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetIQQuadratureErrorMean(self, selectorString, value):
        """ GetIQQuadratureErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetIQTimingSkewMean(self, selectorString, value):
        """ GetIQTimingSkewMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLLtfAveragePowerMean(self, selectorString, value):
        """ GetLLtfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLLtfPeakPowerMaximum(self, selectorString, value):
        """ GetLLtfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLSigAveragePowerMean(self, selectorString, value):
        """ GetLSigAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLSigParityCheckStatus(self, selectorString, value):
        """ GetLSigParityCheckStatus(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmModAccLSigParityCheckStatus) """
        pass

    def GetLSigPeakPowerMaximum(self, selectorString, value):
        """ GetLSigPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLStfAveragePowerMean(self, selectorString, value):
        """ GetLStfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetLStfPeakPowerMaximum(self, selectorString, value):
        """ GetLStfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetMcsIndex(self, selectorString, value):
        """ GetMcsIndex(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetNoiseCompensationApplied(self, selectorString, value):
        """ GetNoiseCompensationApplied(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmModAccNoiseCompensationApplied) """
        pass

    def GetNumberOfHESigBSymbols(self, selectorString, value):
        """ GetNumberOfHESigBSymbols(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfSpaceTimeStreams(self, selectorString, value):
        """ GetNumberOfSpaceTimeStreams(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfSymbolsUsed(self, selectorString, value):
        """ GetNumberOfSymbolsUsed(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfUsers(self, selectorString, value):
        """ GetNumberOfUsers(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetPEAveragePowerMean(self, selectorString, value):
        """ GetPEAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPEPeakPowerMaximum(self, selectorString, value):
        """ GetPEPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPpduAveragePowerMean(self, selectorString, value):
        """ GetPpduAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPpduPeakPowerMaximum(self, selectorString, value):
        """ GetPpduPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetPpduType(self, selectorString, value):
        """ GetPpduType(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmPpduType) """
        pass

    def GetRelativeIQOriginOffsetMean(self, selectorString, value):
        """ GetRelativeIQOriginOffsetMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRLSigAveragePowerMean(self, selectorString, value):
        """ GetRLSigAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRLSigPeakPowerMaximum(self, selectorString, value):
        """ GetRLSigPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRmsCommonPhaseErrorMean(self, selectorString, value):
        """ GetRmsCommonPhaseErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRmsCommonPilotErrorMean(self, selectorString, value):
        """ GetRmsCommonPilotErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetRUOffset(self, selectorString, value):
        """ GetRUOffset(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetRUSize(self, selectorString, value):
        """ GetRUSize(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetSigBCrcStatus(self, selectorString, value):
        """ GetSigBCrcStatus(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmModAccSigBCrcStatus) """
        pass

    def GetSigCrcStatus(self, selectorString, value):
        """ GetSigCrcStatus(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, RFmxWlanMXOfdmModAccSigCrcStatus) """
        pass

    def GetSpectralFlatnessMargin(self, selectorString, value):
        """ GetSpectralFlatnessMargin(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetSpectralFlatnessMarginSubcarrierIndex(self, selectorString, value):
        """ GetSpectralFlatnessMarginSubcarrierIndex(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetSymbolClockErrorMean(self, selectorString, value):
        """ GetSymbolClockErrorMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetUnusedToneErrorMargin(self, selectorString, value):
        """ GetUnusedToneErrorMargin(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetUnusedToneErrorMarginRUIndex(self, selectorString, value):
        """ GetUnusedToneErrorMarginRUIndex(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, int) """
        pass

    def GetUserStreamDataRmsEvmMean(self, selectorString, value):
        """ GetUserStreamDataRmsEvmMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetUserStreamPilotRmsEvmMean(self, selectorString, value):
        """ GetUserStreamPilotRmsEvmMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetUserStreamRmsEvmMean(self, selectorString, value):
        """ GetUserStreamRmsEvmMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtLtfAveragePowerMean(self, selectorString, value):
        """ GetVhtLtfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtLtfPeakPowerMaximum(self, selectorString, value):
        """ GetVhtLtfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtSigAAveragePowerMean(self, selectorString, value):
        """ GetVhtSigAAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtSigAPeakPowerMaximum(self, selectorString, value):
        """ GetVhtSigAPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtSigBAveragePowerMean(self, selectorString, value):
        """ GetVhtSigBAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtSigBPeakPowerMaximum(self, selectorString, value):
        """ GetVhtSigBPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtStfAveragePowerMean(self, selectorString, value):
        """ GetVhtStfAveragePowerMean(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass

    def GetVhtStfPeakPowerMaximum(self, selectorString, value):
        """ GetVhtStfPeakPowerMaximum(self: RFmxWlanMXOfdmModAccResults, selectorString: str) -> (int, float) """
        pass


class RFmxWlanMXOfdmModAccSigBCrcStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccSigBCrcStatus, values: Fail (0), NotApplicable (-1), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    NotApplicable = None
    Pass = None
    value__ = None


class RFmxWlanMXOfdmModAccSigCrcStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccSigCrcStatus, values: Fail (0), NotApplicable (-1), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    NotApplicable = None
    Pass = None
    value__ = None


class RFmxWlanMXOfdmModAccSpectrumInverted(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccSpectrumInverted, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccSymbolClockErrorCorrectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmModAccUnusedToneErrorMaskReference(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmModAccUnusedToneErrorMaskReference, values: Limit1 (0), Limit2 (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Limit1 = None
    Limit2 = None
    value__ = None


class RFmxWlanMXOfdmMUMimoLtfModeEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmMUMimoLtfModeEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmPpduType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmPpduType, values: ExtendedRangeSU (5), Greenfield (2), Mixed (1), MU (4), NonHT (0), SU (3), TriggerBased (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ExtendedRangeSU = None
    Greenfield = None
    Mixed = None
    MU = None
    NonHT = None
    SU = None
    TriggerBased = None
    value__ = None


class RFmxWlanMXOfdmPreamblePuncturingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmPreamblePuncturingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXOfdmTransmitPowerClass(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXOfdmTransmitPowerClass, values: A (0), B (1), C (2), D (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    A = None
    B = None
    C = None
    D = None
    value__ = None


class RFmxWlanMXPowerRamp(RFmxWlanMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxWlanMXPowerRamp) -> RFmxWlanMXPowerRampConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxWlanMXPowerRamp) -> RFmxWlanMXPowerRampResults

"""



class RFmxWlanMXPowerRampAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXPowerRampAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXPowerRampConfiguration(RFmxWlanMXSubObject):
    # no doc
    def ConfigureAcquisitionLength(self, selectorString, acquisitionLength):
        """ ConfigureAcquisitionLength(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, acquisitionLength: float) -> int """
        pass

    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, averagingEnabled: RFmxWlanMXPowerRampAveragingEnabled, averagingCount: int) -> int """
        pass

    def GetAcquisitionLength(self, selectorString, value):
        """ GetAcquisitionLength(self: RFmxWlanMXPowerRampConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxWlanMXPowerRampConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxWlanMXPowerRampConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxWlanMXPowerRampConfiguration, selectorString: str) -> (int, RFmxWlanMXPowerRampAveragingEnabled) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxWlanMXPowerRampConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxWlanMXPowerRampConfiguration, selectorString: str) -> (int, int) """
        pass

    def SetAcquisitionLength(self, selectorString, value):
        """ SetAcquisitionLength(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, value: RFmxWlanMXPowerRampAveragingEnabled) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxWlanMXPowerRampConfiguration, selectorString: str, value: int) -> int """
        pass


class RFmxWlanMXPowerRampResults(RFmxWlanMXSubObject):
    # no doc
    def FetchFallTrace(self, selectorString, timeout, rawWaveform, processedWaveform, threshold, powerReference):
        """ FetchFallTrace(self: RFmxWlanMXPowerRampResults, selectorString: str, timeout: float, rawWaveform: AnalogWaveform[Single], processedWaveform: AnalogWaveform[Single], threshold: AnalogWaveform[Single], powerReference: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single], AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def FetchMeasurement(self, selectorString, timeout, riseTimeMean, fallTimeMean):
        """ FetchMeasurement(self: RFmxWlanMXPowerRampResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchRiseTrace(self, selectorString, timeout, rawWaveform, processedWaveform, threshold, powerReference):
        """ FetchRiseTrace(self: RFmxWlanMXPowerRampResults, selectorString: str, timeout: float, rawWaveform: AnalogWaveform[Single], processedWaveform: AnalogWaveform[Single], threshold: AnalogWaveform[Single], powerReference: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single], AnalogWaveform[Single], AnalogWaveform[Single], AnalogWaveform[Single]) """
        pass

    def GetFallTimeMean(self, selectorString, value):
        """ GetFallTimeMean(self: RFmxWlanMXPowerRampResults, selectorString: str) -> (int, float) """
        pass

    def GetRiseTimeMean(self, selectorString, value):
        """ GetRiseTimeMean(self: RFmxWlanMXPowerRampResults, selectorString: str) -> (int, float) """
        pass


class RFmxWlanMXPropertyId(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXPropertyId, values: AutoLevelInitialReferenceLevel (10485796), CenterFrequency (10485761), ChannelBandwidth (10485774), DetectedBurstLength (10485779), DetectedChannelBandwidth (10485778), DetectedStandard (10485777), DigitalEdgeTriggerEdge (10485766), DigitalEdgeTriggerSource (10485765), DsssModAccAcquisitionLength (10498060), DsssModAccAcquisitionLengthMode (10498059), DsssModAccAllTracesEnabled (10498097), DsssModAccAveragingCount (10498096), DsssModAccAveragingEnabled (10498095), DsssModAccBurstStartDetectionEnabled (10498170), DsssModAccChipClockErrorCorrectionEnabled (10498093), DsssModAccEqualizationEnabled (10498065), DsssModAccEvmUnit (10498066), DsssModAccFrequencyErrorCorrectionEnabled (10498092), DsssModAccIQOriginOffsetCorrectionEnabled (10498094), DsssModAccMaximumMeasurementLength (10498062), DsssModAccMeasurementEnabled (10498058), DsssModAccMeasurementOffset (10498061), DsssModAccNumberOfAnalysisThreads (10498161), DsssModAccPowerCustomGateStartTime (10498069), DsssModAccPowerCustomGateStopTime (10498070), DsssModAccPowerMeasurementEnabled (10498067), DsssModAccPowerNumberOfCustomGates (10498068), DsssModAccPulseShapingFilterParameter (10498064), DsssModAccPulseShapingFilterType (10498063), DsssModAccResultsChipClockErrorMean (10498130), DsssModAccResultsCustomGateAveragePowerMean (10498110), DsssModAccResultsCustomGatePeakPowerMaximum (10498111), DsssModAccResultsDataAveragePowerMean (10498166), DsssModAccResultsDataModulationFormat (10498152), DsssModAccResultsDataPeakPowerMaximum (10498167), DsssModAccResultsFrequencyErrorMean (10498126), DsssModAccResultsHeaderAveragePowerMean (10498164), DsssModAccResultsHeaderCrcStatus (10498157), DsssModAccResultsHeaderPeakPowerMaximum (10498165), DsssModAccResultsIQGainImbalanceMean (10498131), DsssModAccResultsIQOriginOffsetMean (10498139), DsssModAccResultsIQQuadratureErrorMean (10498135), DsssModAccResultsLockedClocksBit (10498156), DsssModAccResultsNumberOfChipsUsed (10498125), DsssModAccResultsPayloadLength (10498153), DsssModAccResultsPeakEvm802_11_1999Maximum (10498100), DsssModAccResultsPeakEvm802_11_1999Mean (10498099), DsssModAccResultsPeakEvm802_11_2007Maximum (10498102), DsssModAccResultsPeakEvm802_11_2007Mean (10498101), DsssModAccResultsPeakEvm802_11_2016Maximum (10498109), DsssModAccResultsPeakEvm802_11_2016Mean (10498108), DsssModAccResultsPpduAveragePowerMean (10498168), DsssModAccResultsPpduPeakPowerMaximum (10498169), DsssModAccResultsPreambleAveragePowerMean (10498162), DsssModAccResultsPreamblePeakPowerMaximum (10498163), DsssModAccResultsPreambleType (10498154), DsssModAccResultsRmsEvmMean (10498098), DsssModAccResultsRmsMagnitudeErrorMean (10498146), DsssModAccResultsRmsPhaseErrorMean (10498147), DsssModAccSpectrumInverted (10498171), ExternalAttenuation (10485763), IQPowerEdgeTriggerLevel (10485768), IQPowerEdgeTriggerLevelType (10489855), IQPowerEdgeTriggerSlope (10485769), IQPowerEdgeTriggerSource (10485767), LimitedConfigurationChange (10485797), OfdmAutoPpduTypeDetectionEnabled (10485799), OfdmDcmEnabled (10485793), OfdmFrequencyBand (10485782), OfdmGuardIntervalType (10485788), OfdmHeaderDecodingEnabled (10485800), OfdmHELtfSize (10485789), OfdmMcsIndex (10485785), OfdmModAccAcquisitionLength (10502154), OfdmModAccAcquisitionLengthMode (10502153), OfdmModAccAllTracesEnabled (10502149), OfdmModAccAmplitudeTrackingEnabled (10502158), OfdmModAccAveragingCount (10502147), OfdmModAccAveragingEnabled (10502146), OfdmModAccBurstStartDetectionEnabled (10502277), OfdmModAccChannelEstimationLLtfEnabled (10502279), OfdmModAccChannelEstimationSmoothingEnabled (10502250), OfdmModAccChannelEstimationSmoothingLength (10502251), OfdmModAccChannelEstimationType (10502161), OfdmModAccCommonClockSourceEnabled (10502157), OfdmModAccEvmUnit (10502152), OfdmModAccFrequencyErrorEstimationMethod (10502270), OfdmModAccIQGainImbalanceCorrectionEnabled (10502172), OfdmModAccIQImpairmentsEstimationEnabled (10502267), OfdmModAccIQImpairmentsModel (10502171), OfdmModAccIQImpairmentsPerSubcarrierEnabled (10502271), OfdmModAccIQQuadratureErrorCorrectionEnabled (10502173), OfdmModAccIQTimingSkewCorrectionEnabled (10502174), OfdmModAccMaximumMeasurementLength (10502156), OfdmModAccMeasurementEnabled (10502144), OfdmModAccMeasurementMode (10502246), OfdmModAccMeasurementOffset (10502155), OfdmModAccNoiseCompensationEnabled (10502247), OfdmModAccNoiseCompensationInputPowerCheckEnabled (10502248), OfdmModAccNoiseCompensationReferenceLevelCoercionLimit (10502249), OfdmModAccNumberOfAnalysisThreads (10502148), OfdmModAccOptimizeDynamicRangeForEvmEnabled (10502268), OfdmModAccOptimizeDynamicRangeForEvmMargin (10502269), OfdmModAccPhaseTrackingEnabled (10502159), OfdmModAccPowerCustomGateStartTime (10502169), OfdmModAccPowerCustomGateStopTime (10502170), OfdmModAccPowerMeasurementEnabled (10502167), OfdmModAccPowerNumberOfCustomGates (10502168), OfdmModAccResultsAbsoluteIQOriginOffsetMean (10502188), OfdmModAccResultsCompositeDataRmsEvmMean (10502255), OfdmModAccResultsCompositePilotRmsEvmMean (10502256), OfdmModAccResultsCompositeRmsEvmMean (10502254), OfdmModAccResultsCustomGateAveragePowerMean (10502242), OfdmModAccResultsCustomGatePeakPowerMaximum (10502243), OfdmModAccResultsDataAveragePowerMean (10502236), OfdmModAccResultsDataPeakPowerMaximum (10502237), OfdmModAccResultsFrequencyErrorCcdf10Percent (10502185), OfdmModAccResultsFrequencyErrorMean (10502184), OfdmModAccResultsGuardIntervalType (10502199), OfdmModAccResultsHELtfAveragePowerMean (10502234), OfdmModAccResultsHELtfPeakPowerMaximum (10502235), OfdmModAccResultsHELtfSize (10502200), OfdmModAccResultsHESigAAveragePowerMean (10502214), OfdmModAccResultsHESigAPeakPowerMaximum (10502215), OfdmModAccResultsHESigBAveragePowerMean (10502218), OfdmModAccResultsHESigBPeakPowerMaximum (10502219), OfdmModAccResultsHEStfAveragePowerMean (10502226), OfdmModAccResultsHEStfPeakPowerMaximum (10502227), OfdmModAccResultsHTDltfAveragePowerMean (10502228), OfdmModAccResultsHTDltfPeakPowerMaximum (10502229), OfdmModAccResultsHTEltfAveragePowerMean (10502230), OfdmModAccResultsHTEltfPeakPowerMaximum (10502231), OfdmModAccResultsHTGFStfAveragePowerMean (10502222), OfdmModAccResultsHTGFStfPeakPowerMaximum (10502223), OfdmModAccResultsHTSigAveragePowerMean (10502210), OfdmModAccResultsHTSigPeakPowerMaximum (10502211), OfdmModAccResultsHTStfAveragePowerMean (10502220), OfdmModAccResultsHTStfPeakPowerMaximum (10502221), OfdmModAccResultsIQGainImbalanceMean (10502189), OfdmModAccResultsIQQuadratureErrorMean (10502190), OfdmModAccResultsIQTimingSkewMean (10502191), OfdmModAccResultsLLtfAveragePowerMean (10502204), OfdmModAccResultsLLtfPeakPowerMaximum (10502205), OfdmModAccResultsLSigAveragePowerMean (10502206), OfdmModAccResultsLSigParityCheckStatus (10502280), OfdmModAccResultsLSigPeakPowerMaximum (10502207), OfdmModAccResultsLStfAveragePowerMean (10502202), OfdmModAccResultsLStfPeakPowerMaximum (10502203), OfdmModAccResultsMcsIndex (10502194), OfdmModAccResultsNoiseCompensationApplied (10502183), OfdmModAccResultsNumberOfHESigBSymbols (10502198), OfdmModAccResultsNumberOfSpaceTimeStreams (10502201), OfdmModAccResultsNumberOfSymbolsUsed (10502166), OfdmModAccResultsNumberOfUsers (10502197), OfdmModAccResultsPEAveragePowerMean (10502238), OfdmModAccResultsPEPeakPowerMaximum (10502239), OfdmModAccResultsPpduAveragePowerMean (10502240), OfdmModAccResultsPpduPeakPowerMaximum (10502241), OfdmModAccResultsPpduType (10502193), OfdmModAccResultsRelativeIQOriginOffsetMean (10502187), OfdmModAccResultsRLSigAveragePowerMean (10502208), OfdmModAccResultsRLSigPeakPowerMaximum (10502209), OfdmModAccResultsRmsCommonPhaseErrorMean (10502192), OfdmModAccResultsRmsCommonPilotErrorMean (10502253), OfdmModAccResultsRUOffset (10502196), OfdmModAccResultsRUSize (10502195), OfdmModAccResultsSigBCrcStatus (10502282), OfdmModAccResultsSigCrcStatus (10502281), OfdmModAccResultsSpectralFlatnessMargin (10502179), OfdmModAccResultsSpectralFlatnessMarginSubcarrierIndex (10502180), OfdmModAccResultsSymbolClockErrorMean (10502186), OfdmModAccResultsUnusedToneErrorMargin (10502181), OfdmModAccResultsUnusedToneErrorMarginRUIndex (10502182), OfdmModAccResultsUserStreamDataRmsEvmMean (10502264), OfdmModAccResultsUserStreamPilotRmsEvmMean (10502265), OfdmModAccResultsUserStreamRmsEvmMean (10502263), OfdmModAccResultsVhtLtfAveragePowerMean (10502232), OfdmModAccResultsVhtLtfPeakPowerMaximum (10502233), OfdmModAccResultsVhtSigAAveragePowerMean (10502212), OfdmModAccResultsVhtSigAPeakPowerMaximum (10502213), OfdmModAccResultsVhtSigBAveragePowerMean (10502216), OfdmModAccResultsVhtSigBPeakPowerMaximum (10502217), OfdmModAccResultsVhtStfAveragePowerMean (10502224), OfdmModAccResultsVhtStfPeakPowerMaximum (10502225), OfdmModAccSpectrumInverted (10502266), OfdmModAccSymbolClockErrorCorrectionEnabled (10502160), OfdmModAccUnusedToneErrorMaskReference (10502252), OfdmMUMimoLtfModeEnabled (10485801), OfdmNumberHELtfSymbols (10485794), OfdmNumberOfHESigBSymbols (10485792), OfdmNumberOfUsers (10485784), OfdmPEDisambiguity (10485809), OfdmPpduType (10485783), OfdmPreamblePuncturingBitmap (10485808), OfdmPreamblePuncturingEnabled (10485807), OfdmRUOffset (10485787), OfdmRUSize (10485786), OfdmSpaceTimeStreamOffset (10485791), OfdmTransmitPowerClass (10485781), PowerRampAcquisitionLength (10493964), PowerRampAllTracesEnabled (10493974), PowerRampAveragingCount (10493973), PowerRampAveragingEnabled (10493972), PowerRampMeasurementEnabled (10493962), PowerRampNumberOfAnalysisThreads (10493975), PowerRampResultsFallTimeMean (10493977), PowerRampResultsRiseTimeMean (10493976), ReferenceLevel (10485762), ReferenceLevelHeadroom (10489852), ResultFetchTimeout (10534912), SelectedPorts (10489853), SemAllTracesEnabled (10506263), SemAmplitudeCorrectionType (10506262), SemAveragingCount (10506260), SemAveragingEnabled (10506259), SemAveragingType (10506261), SemCarrierIntegrationBandwidth (10506245), SemMaskType (10506242), SemMeasurementEnabled (10506240), SemNumberOfAnalysisThreads (10506264), SemNumberOfOffsets (10506246), SemOffsetRelativeLimitStart (10506250), SemOffsetRelativeLimitStop (10506251), SemOffsetSideband (10506249), SemOffsetStartFrequency (10506247), SemOffsetStopFrequency (10506248), SemResultsCarrierAbsoluteIntegratedPower (10506268), SemResultsCarrierAbsolutePeakPower (10506270), SemResultsCarrierPeakFrequency (10506271), SemResultsLowerOffsetAbsoluteIntegratedPower (10506274), SemResultsLowerOffsetAbsolutePeakPower (10506276), SemResultsLowerOffsetMargin (10506279), SemResultsLowerOffsetMarginAbsolutePower (10506280), SemResultsLowerOffsetMarginFrequency (10506282), SemResultsLowerOffsetMarginRelativePower (10506281), SemResultsLowerOffsetMeasurementStatus (10506273), SemResultsLowerOffsetPeakFrequency (10506278), SemResultsLowerOffsetRelativeIntegratedPower (10506275), SemResultsLowerOffsetRelativePeakPower (10506277), SemResultsMeasurementStatus (10506267), SemResultsUpperOffsetAbsoluteIntegratedPower (10506284), SemResultsUpperOffsetAbsolutePeakPower (10506286), SemResultsUpperOffsetMargin (10506289), SemResultsUpperOffsetMarginAbsolutePower (10506290), SemResultsUpperOffsetMarginFrequency (10506292), SemResultsUpperOffsetMarginRelativePower (10506291), SemResultsUpperOffsetMeasurementStatus (10506283), SemResultsUpperOffsetPeakFrequency (10506288), SemResultsUpperOffsetRelativeIntegratedPower (10506285), SemResultsUpperOffsetRelativePeakPower (10506287), SemSpan (10506253), SemSpanAuto (10506252), SemSweepTimeAuto (10506257), SemSweepTimeInterval (10506258), Standard (10485773), TriggerDelay (10485770), TriggerGateEnabled (10485802), TriggerGateLength (10485803), TriggerMinimumQuietTimeDuration (10485772), TriggerMinimumQuietTimeMode (10485771), TriggerType (10485764), TxpAllTracesEnabled (10489862), TxpAveragingCount (10489861), TxpAveragingEnabled (10489860), TxpBurstDetectionEnabled (10489859), TxpMaximumMeasurementInterval (10489858), TxpMeasurementEnabled (10489856), TxpNumberOfAnalysisThreads (10489863), TxpResultsAveragePowerMean (10489865), TxpResultsPeakPowerMaximum (10489873) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoLevelInitialReferenceLevel = None
    CenterFrequency = None
    ChannelBandwidth = None
    DetectedBurstLength = None
    DetectedChannelBandwidth = None
    DetectedStandard = None
    DigitalEdgeTriggerEdge = None
    DigitalEdgeTriggerSource = None
    DsssModAccAcquisitionLength = None
    DsssModAccAcquisitionLengthMode = None
    DsssModAccAllTracesEnabled = None
    DsssModAccAveragingCount = None
    DsssModAccAveragingEnabled = None
    DsssModAccBurstStartDetectionEnabled = None
    DsssModAccChipClockErrorCorrectionEnabled = None
    DsssModAccEqualizationEnabled = None
    DsssModAccEvmUnit = None
    DsssModAccFrequencyErrorCorrectionEnabled = None
    DsssModAccIQOriginOffsetCorrectionEnabled = None
    DsssModAccMaximumMeasurementLength = None
    DsssModAccMeasurementEnabled = None
    DsssModAccMeasurementOffset = None
    DsssModAccNumberOfAnalysisThreads = None
    DsssModAccPowerCustomGateStartTime = None
    DsssModAccPowerCustomGateStopTime = None
    DsssModAccPowerMeasurementEnabled = None
    DsssModAccPowerNumberOfCustomGates = None
    DsssModAccPulseShapingFilterParameter = None
    DsssModAccPulseShapingFilterType = None
    DsssModAccResultsChipClockErrorMean = None
    DsssModAccResultsCustomGateAveragePowerMean = None
    DsssModAccResultsCustomGatePeakPowerMaximum = None
    DsssModAccResultsDataAveragePowerMean = None
    DsssModAccResultsDataModulationFormat = None
    DsssModAccResultsDataPeakPowerMaximum = None
    DsssModAccResultsFrequencyErrorMean = None
    DsssModAccResultsHeaderAveragePowerMean = None
    DsssModAccResultsHeaderCrcStatus = None
    DsssModAccResultsHeaderPeakPowerMaximum = None
    DsssModAccResultsIQGainImbalanceMean = None
    DsssModAccResultsIQOriginOffsetMean = None
    DsssModAccResultsIQQuadratureErrorMean = None
    DsssModAccResultsLockedClocksBit = None
    DsssModAccResultsNumberOfChipsUsed = None
    DsssModAccResultsPayloadLength = None
    DsssModAccResultsPeakEvm802_11_1999Maximum = None
    DsssModAccResultsPeakEvm802_11_1999Mean = None
    DsssModAccResultsPeakEvm802_11_2007Maximum = None
    DsssModAccResultsPeakEvm802_11_2007Mean = None
    DsssModAccResultsPeakEvm802_11_2016Maximum = None
    DsssModAccResultsPeakEvm802_11_2016Mean = None
    DsssModAccResultsPpduAveragePowerMean = None
    DsssModAccResultsPpduPeakPowerMaximum = None
    DsssModAccResultsPreambleAveragePowerMean = None
    DsssModAccResultsPreamblePeakPowerMaximum = None
    DsssModAccResultsPreambleType = None
    DsssModAccResultsRmsEvmMean = None
    DsssModAccResultsRmsMagnitudeErrorMean = None
    DsssModAccResultsRmsPhaseErrorMean = None
    DsssModAccSpectrumInverted = None
    ExternalAttenuation = None
    IQPowerEdgeTriggerLevel = None
    IQPowerEdgeTriggerLevelType = None
    IQPowerEdgeTriggerSlope = None
    IQPowerEdgeTriggerSource = None
    LimitedConfigurationChange = None
    OfdmAutoPpduTypeDetectionEnabled = None
    OfdmDcmEnabled = None
    OfdmFrequencyBand = None
    OfdmGuardIntervalType = None
    OfdmHeaderDecodingEnabled = None
    OfdmHELtfSize = None
    OfdmMcsIndex = None
    OfdmModAccAcquisitionLength = None
    OfdmModAccAcquisitionLengthMode = None
    OfdmModAccAllTracesEnabled = None
    OfdmModAccAmplitudeTrackingEnabled = None
    OfdmModAccAveragingCount = None
    OfdmModAccAveragingEnabled = None
    OfdmModAccBurstStartDetectionEnabled = None
    OfdmModAccChannelEstimationLLtfEnabled = None
    OfdmModAccChannelEstimationSmoothingEnabled = None
    OfdmModAccChannelEstimationSmoothingLength = None
    OfdmModAccChannelEstimationType = None
    OfdmModAccCommonClockSourceEnabled = None
    OfdmModAccEvmUnit = None
    OfdmModAccFrequencyErrorEstimationMethod = None
    OfdmModAccIQGainImbalanceCorrectionEnabled = None
    OfdmModAccIQImpairmentsEstimationEnabled = None
    OfdmModAccIQImpairmentsModel = None
    OfdmModAccIQImpairmentsPerSubcarrierEnabled = None
    OfdmModAccIQQuadratureErrorCorrectionEnabled = None
    OfdmModAccIQTimingSkewCorrectionEnabled = None
    OfdmModAccMaximumMeasurementLength = None
    OfdmModAccMeasurementEnabled = None
    OfdmModAccMeasurementMode = None
    OfdmModAccMeasurementOffset = None
    OfdmModAccNoiseCompensationEnabled = None
    OfdmModAccNoiseCompensationInputPowerCheckEnabled = None
    OfdmModAccNoiseCompensationReferenceLevelCoercionLimit = None
    OfdmModAccNumberOfAnalysisThreads = None
    OfdmModAccOptimizeDynamicRangeForEvmEnabled = None
    OfdmModAccOptimizeDynamicRangeForEvmMargin = None
    OfdmModAccPhaseTrackingEnabled = None
    OfdmModAccPowerCustomGateStartTime = None
    OfdmModAccPowerCustomGateStopTime = None
    OfdmModAccPowerMeasurementEnabled = None
    OfdmModAccPowerNumberOfCustomGates = None
    OfdmModAccResultsAbsoluteIQOriginOffsetMean = None
    OfdmModAccResultsCompositeDataRmsEvmMean = None
    OfdmModAccResultsCompositePilotRmsEvmMean = None
    OfdmModAccResultsCompositeRmsEvmMean = None
    OfdmModAccResultsCustomGateAveragePowerMean = None
    OfdmModAccResultsCustomGatePeakPowerMaximum = None
    OfdmModAccResultsDataAveragePowerMean = None
    OfdmModAccResultsDataPeakPowerMaximum = None
    OfdmModAccResultsFrequencyErrorCcdf10Percent = None
    OfdmModAccResultsFrequencyErrorMean = None
    OfdmModAccResultsGuardIntervalType = None
    OfdmModAccResultsHELtfAveragePowerMean = None
    OfdmModAccResultsHELtfPeakPowerMaximum = None
    OfdmModAccResultsHELtfSize = None
    OfdmModAccResultsHESigAAveragePowerMean = None
    OfdmModAccResultsHESigAPeakPowerMaximum = None
    OfdmModAccResultsHESigBAveragePowerMean = None
    OfdmModAccResultsHESigBPeakPowerMaximum = None
    OfdmModAccResultsHEStfAveragePowerMean = None
    OfdmModAccResultsHEStfPeakPowerMaximum = None
    OfdmModAccResultsHTDltfAveragePowerMean = None
    OfdmModAccResultsHTDltfPeakPowerMaximum = None
    OfdmModAccResultsHTEltfAveragePowerMean = None
    OfdmModAccResultsHTEltfPeakPowerMaximum = None
    OfdmModAccResultsHTGFStfAveragePowerMean = None
    OfdmModAccResultsHTGFStfPeakPowerMaximum = None
    OfdmModAccResultsHTSigAveragePowerMean = None
    OfdmModAccResultsHTSigPeakPowerMaximum = None
    OfdmModAccResultsHTStfAveragePowerMean = None
    OfdmModAccResultsHTStfPeakPowerMaximum = None
    OfdmModAccResultsIQGainImbalanceMean = None
    OfdmModAccResultsIQQuadratureErrorMean = None
    OfdmModAccResultsIQTimingSkewMean = None
    OfdmModAccResultsLLtfAveragePowerMean = None
    OfdmModAccResultsLLtfPeakPowerMaximum = None
    OfdmModAccResultsLSigAveragePowerMean = None
    OfdmModAccResultsLSigParityCheckStatus = None
    OfdmModAccResultsLSigPeakPowerMaximum = None
    OfdmModAccResultsLStfAveragePowerMean = None
    OfdmModAccResultsLStfPeakPowerMaximum = None
    OfdmModAccResultsMcsIndex = None
    OfdmModAccResultsNoiseCompensationApplied = None
    OfdmModAccResultsNumberOfHESigBSymbols = None
    OfdmModAccResultsNumberOfSpaceTimeStreams = None
    OfdmModAccResultsNumberOfSymbolsUsed = None
    OfdmModAccResultsNumberOfUsers = None
    OfdmModAccResultsPEAveragePowerMean = None
    OfdmModAccResultsPEPeakPowerMaximum = None
    OfdmModAccResultsPpduAveragePowerMean = None
    OfdmModAccResultsPpduPeakPowerMaximum = None
    OfdmModAccResultsPpduType = None
    OfdmModAccResultsRelativeIQOriginOffsetMean = None
    OfdmModAccResultsRLSigAveragePowerMean = None
    OfdmModAccResultsRLSigPeakPowerMaximum = None
    OfdmModAccResultsRmsCommonPhaseErrorMean = None
    OfdmModAccResultsRmsCommonPilotErrorMean = None
    OfdmModAccResultsRUOffset = None
    OfdmModAccResultsRUSize = None
    OfdmModAccResultsSigBCrcStatus = None
    OfdmModAccResultsSigCrcStatus = None
    OfdmModAccResultsSpectralFlatnessMargin = None
    OfdmModAccResultsSpectralFlatnessMarginSubcarrierIndex = None
    OfdmModAccResultsSymbolClockErrorMean = None
    OfdmModAccResultsUnusedToneErrorMargin = None
    OfdmModAccResultsUnusedToneErrorMarginRUIndex = None
    OfdmModAccResultsUserStreamDataRmsEvmMean = None
    OfdmModAccResultsUserStreamPilotRmsEvmMean = None
    OfdmModAccResultsUserStreamRmsEvmMean = None
    OfdmModAccResultsVhtLtfAveragePowerMean = None
    OfdmModAccResultsVhtLtfPeakPowerMaximum = None
    OfdmModAccResultsVhtSigAAveragePowerMean = None
    OfdmModAccResultsVhtSigAPeakPowerMaximum = None
    OfdmModAccResultsVhtSigBAveragePowerMean = None
    OfdmModAccResultsVhtSigBPeakPowerMaximum = None
    OfdmModAccResultsVhtStfAveragePowerMean = None
    OfdmModAccResultsVhtStfPeakPowerMaximum = None
    OfdmModAccSpectrumInverted = None
    OfdmModAccSymbolClockErrorCorrectionEnabled = None
    OfdmModAccUnusedToneErrorMaskReference = None
    OfdmMUMimoLtfModeEnabled = None
    OfdmNumberHELtfSymbols = None
    OfdmNumberOfHESigBSymbols = None
    OfdmNumberOfUsers = None
    OfdmPEDisambiguity = None
    OfdmPpduType = None
    OfdmPreamblePuncturingBitmap = None
    OfdmPreamblePuncturingEnabled = None
    OfdmRUOffset = None
    OfdmRUSize = None
    OfdmSpaceTimeStreamOffset = None
    OfdmTransmitPowerClass = None
    PowerRampAcquisitionLength = None
    PowerRampAllTracesEnabled = None
    PowerRampAveragingCount = None
    PowerRampAveragingEnabled = None
    PowerRampMeasurementEnabled = None
    PowerRampNumberOfAnalysisThreads = None
    PowerRampResultsFallTimeMean = None
    PowerRampResultsRiseTimeMean = None
    ReferenceLevel = None
    ReferenceLevelHeadroom = None
    ResultFetchTimeout = None
    SelectedPorts = None
    SemAllTracesEnabled = None
    SemAmplitudeCorrectionType = None
    SemAveragingCount = None
    SemAveragingEnabled = None
    SemAveragingType = None
    SemCarrierIntegrationBandwidth = None
    SemMaskType = None
    SemMeasurementEnabled = None
    SemNumberOfAnalysisThreads = None
    SemNumberOfOffsets = None
    SemOffsetRelativeLimitStart = None
    SemOffsetRelativeLimitStop = None
    SemOffsetSideband = None
    SemOffsetStartFrequency = None
    SemOffsetStopFrequency = None
    SemResultsCarrierAbsoluteIntegratedPower = None
    SemResultsCarrierAbsolutePeakPower = None
    SemResultsCarrierPeakFrequency = None
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
    SemSpan = None
    SemSpanAuto = None
    SemSweepTimeAuto = None
    SemSweepTimeInterval = None
    Standard = None
    TriggerDelay = None
    TriggerGateEnabled = None
    TriggerGateLength = None
    TriggerMinimumQuietTimeDuration = None
    TriggerMinimumQuietTimeMode = None
    TriggerType = None
    TxpAllTracesEnabled = None
    TxpAveragingCount = None
    TxpAveragingEnabled = None
    TxpBurstDetectionEnabled = None
    TxpMaximumMeasurementInterval = None
    TxpMeasurementEnabled = None
    TxpNumberOfAnalysisThreads = None
    TxpResultsAveragePowerMean = None
    TxpResultsPeakPowerMaximum = None
    value__ = None


class RFmxWlanMXReferenceLevelUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXReferenceLevelUnits, values: dBm (0), dBmV (4), dBuV (5), dBV (3), dBW (2), Volts (7), VoltsSquared (8), Watts (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSem(RFmxWlanMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxWlanMXSem) -> RFmxWlanMXSemConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxWlanMXSem) -> RFmxWlanMXSemResults

"""



class RFmxWlanMXSemAmplitudeCorrectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemAmplitudeCorrectionType, values: RFCenterFrequency (0), SpectrumFrequencyBin (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemAveragingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemAveragingType, values: Log (1), Maximum (3), Minimum (4), Rms (0), Scalar (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemConfiguration(RFmxWlanMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount, averagingType):
        """ ConfigureAveraging(self: RFmxWlanMXSemConfiguration, selectorString: str, averagingEnabled: RFmxWlanMXSemAveragingEnabled, averagingCount: int, averagingType: RFmxWlanMXSemAveragingType) -> int """
        pass

    def ConfigureMaskType(self, selectorString, maskType):
        """ ConfigureMaskType(self: RFmxWlanMXSemConfiguration, selectorString: str, maskType: RFmxWlanMXSemMaskType) -> int """
        pass

    def ConfigureNumberOfOffsets(self, selectorString, numberOfOffsets):
        """ ConfigureNumberOfOffsets(self: RFmxWlanMXSemConfiguration, selectorString: str, numberOfOffsets: int) -> int """
        pass

    def ConfigureOffsetFrequencyArray(self, selectorString, offsetStartFrequency, offsetStopFrequency, offsetSideband):
        """ ConfigureOffsetFrequencyArray(self: RFmxWlanMXSemConfiguration, selectorString: str, offsetStartFrequency: Array[float], offsetStopFrequency: Array[float], offsetSideband: Array[RFmxWlanMXSemOffsetSideband]) -> int """
        pass

    def ConfigureOffsetRelativeLimitArray(self, selectorString, relativeLimitStart, relativeLimitStop):
        """ ConfigureOffsetRelativeLimitArray(self: RFmxWlanMXSemConfiguration, selectorString: str, relativeLimitStart: Array[float], relativeLimitStop: Array[float]) -> int """
        pass

    def ConfigureSpan(self, selectorString, spanAuto, span):
        """ ConfigureSpan(self: RFmxWlanMXSemConfiguration, selectorString: str, spanAuto: RFmxWlanMXSemSpanAuto, span: float) -> int """
        pass

    def ConfigureSweepTime(self, selectorString, sweepTimeAuto, sweepTimeInterval):
        """ ConfigureSweepTime(self: RFmxWlanMXSemConfiguration, selectorString: str, sweepTimeAuto: RFmxWlanMXSemSweepTimeAuto, sweepTimeInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAmplitudeCorrectionType(self, selectorString, value):
        """ GetAmplitudeCorrectionType(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemAmplitudeCorrectionType) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemAveragingEnabled) """
        pass

    def GetAveragingType(self, selectorString, value):
        """ GetAveragingType(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemAveragingType) """
        pass

    def GetCarrierIntegrationBandwidth(self, selectorString, value):
        """ GetCarrierIntegrationBandwidth(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMaskType(self, selectorString, value):
        """ GetMaskType(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemMaskType) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetNumberOfOffsets(self, selectorString, value):
        """ GetNumberOfOffsets(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetOffsetRelativeLimitStart(self, selectorString, value):
        """ GetOffsetRelativeLimitStart(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetRelativeLimitStop(self, selectorString, value):
        """ GetOffsetRelativeLimitStop(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetSideband(self, selectorString, value):
        """ GetOffsetSideband(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemOffsetSideband) """
        pass

    def GetOffsetStartFrequency(self, selectorString, value):
        """ GetOffsetStartFrequency(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetOffsetStopFrequency(self, selectorString, value):
        """ GetOffsetStopFrequency(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSpan(self, selectorString, value):
        """ GetSpan(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetSpanAuto(self, selectorString, value):
        """ GetSpanAuto(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemSpanAuto) """
        pass

    def GetSweepTimeAuto(self, selectorString, value):
        """ GetSweepTimeAuto(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, RFmxWlanMXSemSweepTimeAuto) """
        pass

    def GetSweepTimeInterval(self, selectorString, value):
        """ GetSweepTimeInterval(self: RFmxWlanMXSemConfiguration, selectorString: str) -> (int, float) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxWlanMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAmplitudeCorrectionType(self, selectorString, value):
        """ SetAmplitudeCorrectionType(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemAmplitudeCorrectionType) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxWlanMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemAveragingEnabled) -> int """
        pass

    def SetAveragingType(self, selectorString, value):
        """ SetAveragingType(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemAveragingType) -> int """
        pass

    def SetMaskType(self, selectorString, value):
        """ SetMaskType(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemMaskType) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxWlanMXSemConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxWlanMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetNumberOfOffsets(self, selectorString, value):
        """ SetNumberOfOffsets(self: RFmxWlanMXSemConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetOffsetRelativeLimitStart(self, selectorString, value):
        """ SetOffsetRelativeLimitStart(self: RFmxWlanMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetRelativeLimitStop(self, selectorString, value):
        """ SetOffsetRelativeLimitStop(self: RFmxWlanMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetSideband(self, selectorString, value):
        """ SetOffsetSideband(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemOffsetSideband) -> int """
        pass

    def SetOffsetStartFrequency(self, selectorString, value):
        """ SetOffsetStartFrequency(self: RFmxWlanMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetOffsetStopFrequency(self, selectorString, value):
        """ SetOffsetStopFrequency(self: RFmxWlanMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSpan(self, selectorString, value):
        """ SetSpan(self: RFmxWlanMXSemConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetSpanAuto(self, selectorString, value):
        """ SetSpanAuto(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemSpanAuto) -> int """
        pass

    def SetSweepTimeAuto(self, selectorString, value):
        """ SetSweepTimeAuto(self: RFmxWlanMXSemConfiguration, selectorString: str, value: RFmxWlanMXSemSweepTimeAuto) -> int """
        pass

    def SetSweepTimeInterval(self, selectorString, value):
        """ SetSweepTimeInterval(self: RFmxWlanMXSemConfiguration, selectorString: str, value: float) -> int """
        pass


class RFmxWlanMXSemLowerOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemLowerOffsetMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemMaskType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemMaskType, values: Custom (1), Standard (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemOffsetSideband(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemOffsetSideband, values: Both (2), Negative (0), Positive (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemResults(RFmxWlanMXSubObject):
    # no doc
    def FetchCarrierMeasurement(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchCarrierMeasurement(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchCarrierMeasurementArray(self, selectorString, timeout, absolutePower, relativePower):
        """ FetchCarrierMeasurementArray(self: RFmxWlanMXSemResults, selectorString: str, timeout: float, absolutePower: Array[float], relativePower: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchLowerOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMargin(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXSemLowerOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchLowerOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchLowerOffsetMarginArray(self: RFmxWlanMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxWlanMXSemLowerOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxWlanMXSemLowerOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchLowerOffsetPower(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchLowerOffsetPower(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchLowerOffsetPowerArray(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchLowerOffsetPowerArray(self: RFmxWlanMXSemResults, selectorString: str, timeout: float, totalAbsolutePower: Array[float], totalRelativePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], peakRelativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchMeasurementStatus(self, selectorString, timeout, measurementStatus):
        """ FetchMeasurementStatus(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXSemMeasurementStatus) """
        pass

    def FetchSpectrum(self, selectorString, timeout, spectrum, compositeMask):
        """ FetchSpectrum(self: RFmxWlanMXSemResults, selectorString: str, timeout: float, spectrum: Spectrum[Single], compositeMask: Spectrum[Single]) -> (int, Spectrum[Single], Spectrum[Single]) """
        pass

    def FetchTotalAggregatedPower(self, selectorString, timeout, totalAggregatedPower):
        """ FetchTotalAggregatedPower(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, float) """
        pass

    def FetchUpperOffsetMargin(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMargin(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, RFmxWlanMXSemUpperOffsetMeasurementStatus, float, float, float, float) """
        pass

    def FetchUpperOffsetMarginArray(self, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower):
        """ FetchUpperOffsetMarginArray(self: RFmxWlanMXSemResults, selectorString: str, timeout: float, measurementStatus: Array[RFmxWlanMXSemUpperOffsetMeasurementStatus], margin: Array[float], marginFrequency: Array[float], marginAbsolutePower: Array[float], marginRelativePower: Array[float]) -> (int, Array[RFmxWlanMXSemUpperOffsetMeasurementStatus], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def FetchUpperOffsetPower(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchUpperOffsetPower(self: RFmxWlanMXSemResults, selectorString: str, timeout: float) -> (int, float, float, float, float, float) """
        pass

    def FetchUpperOffsetPowerArray(self, selectorString, timeout, totalAbsolutePower, totalRelativePower, peakAbsolutePower, peakFrequency, peakRelativePower):
        """ FetchUpperOffsetPowerArray(self: RFmxWlanMXSemResults, selectorString: str, timeout: float, totalAbsolutePower: Array[float], totalRelativePower: Array[float], peakAbsolutePower: Array[float], peakFrequency: Array[float], peakRelativePower: Array[float]) -> (int, Array[float], Array[float], Array[float], Array[float], Array[float]) """
        pass

    def GetCarrierAbsoluteIntegratedPower(self, selectorString, value):
        """ GetCarrierAbsoluteIntegratedPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierAbsolutePeakPower(self, selectorString, value):
        """ GetCarrierAbsolutePeakPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetCarrierPeakFrequency(self, selectorString, value):
        """ GetCarrierPeakFrequency(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetLowerOffsetAbsoluteIntegratedPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetAbsolutePeakPower(self, selectorString, value):
        """ GetLowerOffsetAbsolutePeakPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMargin(self, selectorString, value):
        """ GetLowerOffsetMargin(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetLowerOffsetMarginAbsolutePower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginFrequency(self, selectorString, value):
        """ GetLowerOffsetMarginFrequency(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMarginRelativePower(self, selectorString, value):
        """ GetLowerOffsetMarginRelativePower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetMeasurementStatus(self, selectorString, value):
        """ GetLowerOffsetMeasurementStatus(self: RFmxWlanMXSemResults, selectorString: str) -> (int, RFmxWlanMXSemLowerOffsetMeasurementStatus) """
        pass

    def GetLowerOffsetPeakFrequency(self, selectorString, value):
        """ GetLowerOffsetPeakFrequency(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativeIntegratedPower(self, selectorString, value):
        """ GetLowerOffsetRelativeIntegratedPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetLowerOffsetRelativePeakPower(self, selectorString, value):
        """ GetLowerOffsetRelativePeakPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementStatus(self, selectorString, value):
        """ GetMeasurementStatus(self: RFmxWlanMXSemResults, selectorString: str) -> (int, RFmxWlanMXSemMeasurementStatus) """
        pass

    def GetUpperOffsetAbsoluteIntegratedPower(self, selectorString, value):
        """ GetUpperOffsetAbsoluteIntegratedPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetAbsolutePeakPower(self, selectorString, value):
        """ GetUpperOffsetAbsolutePeakPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMargin(self, selectorString, value):
        """ GetUpperOffsetMargin(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginAbsolutePower(self, selectorString, value):
        """ GetUpperOffsetMarginAbsolutePower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginFrequency(self, selectorString, value):
        """ GetUpperOffsetMarginFrequency(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMarginRelativePower(self, selectorString, value):
        """ GetUpperOffsetMarginRelativePower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetMeasurementStatus(self, selectorString, value):
        """ GetUpperOffsetMeasurementStatus(self: RFmxWlanMXSemResults, selectorString: str) -> (int, RFmxWlanMXSemUpperOffsetMeasurementStatus) """
        pass

    def GetUpperOffsetPeakFrequency(self, selectorString, value):
        """ GetUpperOffsetPeakFrequency(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativeIntegratedPower(self, selectorString, value):
        """ GetUpperOffsetRelativeIntegratedPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass

    def GetUpperOffsetRelativePeakPower(self, selectorString, value):
        """ GetUpperOffsetRelativePeakPower(self: RFmxWlanMXSemResults, selectorString: str) -> (int, float) """
        pass


class RFmxWlanMXSemSpanAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemSpanAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemSweepTimeAuto(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemSweepTimeAuto, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXSemUpperOffsetMeasurementStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXSemUpperOffsetMeasurementStatus, values: Fail (0), Pass (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXStandard(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXStandard, values: Standard802_11ac (5), Standard802_11ag (0), Standard802_11ax (6), Standard802_11b (1), Standard802_11j (2), Standard802_11n (4), Standard802_11p (3), Unknown (-1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Standard802_11ac = None
    Standard802_11ag = None
    Standard802_11ax = None
    Standard802_11b = None
    Standard802_11j = None
    Standard802_11n = None
    Standard802_11p = None
    Unknown = None
    value__ = None


class RFmxWlanMXTriggerGateEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXTriggerGateEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXTriggerMinimumQuietTimeMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXTriggerMinimumQuietTimeMode, values: Auto (1), Manual (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXTriggerType, values: DigitalEdge (1), IQPowerEdge (2), None (0), Software (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXTxp(RFmxWlanMXSubObject):
    # no doc
    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: RFmxWlanMXTxp) -> RFmxWlanMXTxpConfiguration

"""

    Results = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Results(self: RFmxWlanMXTxp) -> RFmxWlanMXTxpResults

"""



class RFmxWlanMXTxpAveragingEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXTxpAveragingEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXTxpBurstDetectionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RFmxWlanMXTxpBurstDetectionEnabled, values: False (0), True (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RFmxWlanMXTxpConfiguration(RFmxWlanMXSubObject):
    # no doc
    def ConfigureAveraging(self, selectorString, averagingEnabled, averagingCount):
        """ ConfigureAveraging(self: RFmxWlanMXTxpConfiguration, selectorString: str, averagingEnabled: RFmxWlanMXTxpAveragingEnabled, averagingCount: int) -> int """
        pass

    def ConfigureBurstDetectionEnabled(self, selectorString, burstDetectionEnabled):
        """ ConfigureBurstDetectionEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str, burstDetectionEnabled: RFmxWlanMXTxpBurstDetectionEnabled) -> int """
        pass

    def ConfigureMaximumMeasurementInterval(self, selectorString, maximumMeasurementInterval):
        """ ConfigureMaximumMeasurementInterval(self: RFmxWlanMXTxpConfiguration, selectorString: str, maximumMeasurementInterval: float) -> int """
        pass

    def GetAllTracesEnabled(self, selectorString, value):
        """ GetAllTracesEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetAveragingCount(self, selectorString, value):
        """ GetAveragingCount(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, int) """
        pass

    def GetAveragingEnabled(self, selectorString, value):
        """ GetAveragingEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, RFmxWlanMXTxpAveragingEnabled) """
        pass

    def GetBurstDetectionEnabled(self, selectorString, value):
        """ GetBurstDetectionEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, RFmxWlanMXTxpBurstDetectionEnabled) """
        pass

    def GetMaximumMeasurementInterval(self, selectorString, value):
        """ GetMaximumMeasurementInterval(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, float) """
        pass

    def GetMeasurementEnabled(self, selectorString, value):
        """ GetMeasurementEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, bool) """
        pass

    def GetNumberOfAnalysisThreads(self, selectorString, value):
        """ GetNumberOfAnalysisThreads(self: RFmxWlanMXTxpConfiguration, selectorString: str) -> (int, int) """
        pass

    def SetAllTracesEnabled(self, selectorString, value):
        """ SetAllTracesEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetAveragingCount(self, selectorString, value):
        """ SetAveragingCount(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: int) -> int """
        pass

    def SetAveragingEnabled(self, selectorString, value):
        """ SetAveragingEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: RFmxWlanMXTxpAveragingEnabled) -> int """
        pass

    def SetBurstDetectionEnabled(self, selectorString, value):
        """ SetBurstDetectionEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: RFmxWlanMXTxpBurstDetectionEnabled) -> int """
        pass

    def SetMaximumMeasurementInterval(self, selectorString, value):
        """ SetMaximumMeasurementInterval(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: float) -> int """
        pass

    def SetMeasurementEnabled(self, selectorString, value):
        """ SetMeasurementEnabled(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: bool) -> int """
        pass

    def SetNumberOfAnalysisThreads(self, selectorString, value):
        """ SetNumberOfAnalysisThreads(self: RFmxWlanMXTxpConfiguration, selectorString: str, value: int) -> int """
        pass


class RFmxWlanMXTxpResults(RFmxWlanMXSubObject):
    # no doc
    def FetchMeasurement(self, selectorString, timeout, averagePowerMean, peakPowerMaximum):
        """ FetchMeasurement(self: RFmxWlanMXTxpResults, selectorString: str, timeout: float) -> (int, float, float) """
        pass

    def FetchMeasurementArray(self, selectorString, timeout, averagePowerMean, peakPowerMaximum):
        """ FetchMeasurementArray(self: RFmxWlanMXTxpResults, selectorString: str, timeout: float, averagePowerMean: Array[float], peakPowerMaximum: Array[float]) -> (int, Array[float], Array[float]) """
        pass

    def FetchPowerTrace(self, selectorString, timeout, power):
        """ FetchPowerTrace(self: RFmxWlanMXTxpResults, selectorString: str, timeout: float, power: AnalogWaveform[Single]) -> (int, AnalogWaveform[Single]) """
        pass

    def GetAveragePowerMean(self, selectorString, value):
        """ GetAveragePowerMean(self: RFmxWlanMXTxpResults, selectorString: str) -> (int, float) """
        pass

    def GetPeakPowerMaximum(self, selectorString, value):
        """ GetPeakPowerMaximum(self: RFmxWlanMXTxpResults, selectorString: str) -> (int, float) """
        pass


