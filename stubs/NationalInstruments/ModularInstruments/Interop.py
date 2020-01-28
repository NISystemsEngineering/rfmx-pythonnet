# encoding: utf-8
# module NationalInstruments.ModularInstruments.Interop calls itself Interop
# from NationalInstruments.ModularInstruments.Interop.Fx40, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class niComplexF32(object):
    # no doc
    Imaginary = None
    Real = None


class niComplexI16(object):
    # no doc
    Imaginary = None
    Real = None


class niComplexNumber(object):
    # no doc
    Imaginary = None
    Real = None


class niComplexNumberF32(object):
    # no doc
    Imaginary = None
    Real = None


class niRFSA(object, IDisposable):
    """
    niRFSA(instrumentHandle: IntPtr)
    niRFSA(Resource_Name: str, ID_Query: bool, Reset: bool)
    niRFSA(Resource_Name: str, ID_Query: bool, Reset: bool, Option_String: str)
    """
    def Abort(self):
        """ Abort(self: niRFSA) -> int """
        pass

    def CalAdjustCalTonePower(self, Channel_List, Measurement):
        """ CalAdjustCalTonePower(self: niRFSA, Channel_List: str, Measurement: float) -> int """
        pass

    def CalAdjustDeviceGain(self, Channel_List, Frequency, Gain):
        """ CalAdjustDeviceGain(self: niRFSA, Channel_List: str, Frequency: float, Gain: float) -> int """
        pass

    def CalAdjustDownconverterGain(self, channelList, frequency, gain):
        """ CalAdjustDownconverterGain(self: niRFSA, channelList: str, frequency: float, gain: float) -> int """
        pass

    def CalAdjustIFAttenuationCalibration(self, channelList, iFFilter, numberofAttenuators, attenuatorSettings, measurement):
        """ CalAdjustIFAttenuationCalibration(self: niRFSA, channelList: str, iFFilter: int, numberofAttenuators: int, attenuatorSettings: Array[float], measurement: float) -> int """
        pass

    def CalAdjustIFResponseCalibration(self, channelList, iFFilter, rFFrequency, bandwidth, numberofMeasurements, measurements):
        """ CalAdjustIFResponseCalibration(self: niRFSA, channelList: str, iFFilter: int, rFFrequency: float, bandwidth: float, numberofMeasurements: int, measurements: Array[float]) -> int """
        pass

    def CalAdjustLOExportCalibration(self, channelList, LONumber, numberOfFrequencyPoints, frequencies, LOAttenuations):
        """ CalAdjustLOExportCalibration(self: niRFSA, channelList: str, LONumber: int, numberOfFrequencyPoints: int, frequencies: Array[float], LOAttenuations: Array[float]) -> int """
        pass

    def CalAdjustRefLevelCalibration(self, channelList, referenceLevelCalDataType, rFBand, attenuatorTableNumber, frequency, measurement):
        """ CalAdjustRefLevelCalibration(self: niRFSA, channelList: str, referenceLevelCalDataType: int, rFBand: int, attenuatorTableNumber: int, frequency: float, measurement: float) -> int """
        pass

    def CalSetTemperature(self, temperaturedegreesC):
        """ CalSetTemperature(self: niRFSA, temperaturedegreesC: float) -> int """
        pass

    def ChangeExtCalPassword(self, oldpassword, newpassword):
        """ ChangeExtCalPassword(self: niRFSA, oldpassword: str, newpassword: str) -> int """
        pass

    def CheckAcquisitionStatus(self, Is_Done):
        """ CheckAcquisitionStatus(self: niRFSA) -> (int, bool) """
        pass

    def ClearError(self):
        """ ClearError(self: niRFSA) -> int """
        pass

    def Close(self):
        """ Close(self: niRFSA) """
        pass

    def CloseCalibrationStep(self):
        """ CloseCalibrationStep(self: niRFSA) -> int """
        pass

    def CloseExtCal(self, action):
        """ CloseExtCal(self: niRFSA, action: int) -> int """
        pass

    def CloseExternalAlignmentStep(self):
        """ CloseExternalAlignmentStep(self: niRFSA) -> int """
        pass

    def Commit(self):
        """ Commit(self: niRFSA) -> int """
        pass

    def ConfigureAcquisitionType(self, Acquisition_Type):
        """ ConfigureAcquisitionType(self: niRFSA, Acquisition_Type: int) -> int """
        pass

    def ConfigureDigitalEdgeAdvanceTrigger(self, Source, Edge):
        """ ConfigureDigitalEdgeAdvanceTrigger(self: niRFSA, Source: str, Edge: int) -> int """
        pass

    def ConfigureDigitalEdgeRefTrigger(self, Source, Edge, Pretrigger_Samples):
        """ ConfigureDigitalEdgeRefTrigger(self: niRFSA, Source: str, Edge: int, Pretrigger_Samples: Int64) -> int """
        pass

    def ConfigureDigitalEdgeStartTrigger(self, Source, Edge):
        """ ConfigureDigitalEdgeStartTrigger(self: niRFSA, Source: str, Edge: int) -> int """
        pass

    def ConfigureIQCarrierFrequency(self, Channel_List, Carrier_Frequency):
        """ ConfigureIQCarrierFrequency(self: niRFSA, Channel_List: str, Carrier_Frequency: float) -> int """
        pass

    def ConfigureIQPowerEdgeRefTrigger(self, Source, Level, Slope, Pretrigger_Samples):
        """ ConfigureIQPowerEdgeRefTrigger(self: niRFSA, Source: str, Level: float, Slope: int, Pretrigger_Samples: Int64) -> int """
        pass

    def ConfigureIQRate(self, Channel_List, IQ_Rate):
        """ ConfigureIQRate(self: niRFSA, Channel_List: str, IQ_Rate: float) -> int """
        pass

    def ConfigureNumberOfRecords(self, Channel_List, Number_of_Records_Is_Finite, Number_of_Records):
        """ ConfigureNumberOfRecords(self: niRFSA, Channel_List: str, Number_of_Records_Is_Finite: bool, Number_of_Records: Int64) -> int """
        pass

    def ConfigureNumberOfSamples(self, Channel_List, Number_of_Samples_Is_Finite, Samples_Per_Record):
        """ ConfigureNumberOfSamples(self: niRFSA, Channel_List: str, Number_of_Samples_Is_Finite: bool, Samples_Per_Record: Int64) -> int """
        pass

    def ConfigurePXIChassisClk10(self, PXI_Clk_10_Source):
        """ ConfigurePXIChassisClk10(self: niRFSA, PXI_Clk_10_Source: str) -> int """
        pass

    def ConfigureRefClock(self, Ref_Clock_Source, Ref_Clock_Rate):
        """ ConfigureRefClock(self: niRFSA, Ref_Clock_Source: str, Ref_Clock_Rate: float) -> int """
        pass

    def ConfigureReferenceLevel(self, Channel_List, Reference_Level):
        """ ConfigureReferenceLevel(self: niRFSA, Channel_List: str, Reference_Level: float) -> int """
        pass

    def ConfigureResolutionBandwidth(self, Channel_List, Resolution_Bandwidth):
        """ ConfigureResolutionBandwidth(self: niRFSA, Channel_List: str, Resolution_Bandwidth: float) -> int """
        pass

    def ConfigureSoftwareEdgeAdvanceTrigger(self):
        """ ConfigureSoftwareEdgeAdvanceTrigger(self: niRFSA) -> int """
        pass

    def ConfigureSoftwareEdgeRefTrigger(self, Pretrigger_Samples):
        """ ConfigureSoftwareEdgeRefTrigger(self: niRFSA, Pretrigger_Samples: Int64) -> int """
        pass

    def ConfigureSoftwareEdgeStartTrigger(self):
        """ ConfigureSoftwareEdgeStartTrigger(self: niRFSA) -> int """
        pass

    def ConfigureSpectrumFrequencyCenterSpan(self, Channel_List, Center_Frequency, Span):
        """ ConfigureSpectrumFrequencyCenterSpan(self: niRFSA, Channel_List: str, Center_Frequency: float, Span: float) -> int """
        pass

    def ConfigureSpectrumFrequencyStartStop(self, Channel_List, Start_Frequency, Stop_Frequency):
        """ ConfigureSpectrumFrequencyStartStop(self: niRFSA, Channel_List: str, Start_Frequency: float, Stop_Frequency: float) -> int """
        pass

    def CreateConfigurationList(self, listName, numberOfListAttributes, listAttributeIDs, setAsActiveList):
        """ CreateConfigurationList(self: niRFSA, listName: str, numberOfListAttributes: int, listAttributeIDs: Array[niRFSAProperties], setAsActiveList: bool) -> int """
        pass

    def CreateConfigurationListStep(self, setAsActiveStep):
        """ CreateConfigurationListStep(self: niRFSA, setAsActiveStep: bool) -> int """
        pass

    def DeleteConfigurationList(self, listName):
        """ DeleteConfigurationList(self: niRFSA, listName: str) -> int """
        pass

    def Disable(self):
        """ Disable(self: niRFSA) -> int """
        pass

    def DisableAdvanceTrigger(self):
        """ DisableAdvanceTrigger(self: niRFSA) -> int """
        pass

    def DisableRefTrigger(self):
        """ DisableRefTrigger(self: niRFSA) -> int """
        pass

    def DisableStartTrigger(self):
        """ DisableStartTrigger(self: niRFSA) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: niRFSA) """
        pass

    def EnableSessionAccess(self, *__args):
        """
        EnableSessionAccess(self: niRFSA, channelList: str, enable: bool) -> int
        EnableSessionAccess(self: niRFSA, enable: bool) -> int
        """
        pass

    @staticmethod
    def ErrorMessage(*__args):
        """
        ErrorMessage(handle: HandleRef, code: int, msg: StringBuilder) -> int
        ErrorMessage(self: niRFSA, code: int, msg: StringBuilder) -> int
        """
        pass

    def ExportSignal(self, Signal, Signal_Identifier, Output_Terminal):
        """ ExportSignal(self: niRFSA, Signal: int, Signal_Identifier: str, Output_Terminal: str) -> int """
        pass

    def ExtCalStoreBaselineForSelfCalibration(self, password, stepToRun):
        """ ExtCalStoreBaselineForSelfCalibration(self: niRFSA, password: str, stepToRun: Int64) -> int """
        pass

    def ExternalAlignmentAdjustPreselector(self, numberOfCoefficients, coefficients):
        """ ExternalAlignmentAdjustPreselector(self: niRFSA, numberOfCoefficients: int, coefficients: Array[float]) -> int """
        pass

    def FetchIQMultiRecordComplexF32(self, Channel_List, StartingRecord, NumberOfRecords, Number_of_Samples, Timeout, Data, Waveform_Info):
        """
        FetchIQMultiRecordComplexF32(self: niRFSA, Channel_List: str, StartingRecord: Int64, NumberOfRecords: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexF32]) -> (int, niRFSA_wfmInfo)
        FetchIQMultiRecordComplexF32(self: niRFSA, Channel_List: str, StartingRecord: Int64, NumberOfRecords: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexNumberF32]) -> (int, niRFSA_wfmInfo)
        """
        pass

    def FetchIQMultiRecordComplexF64(self, Channel_List, Starting_Record, Number_of_Records, Number_of_Samples, Timeout, Data, Waveform_Info):
        """ FetchIQMultiRecordComplexF64(self: niRFSA, Channel_List: str, Starting_Record: Int64, Number_of_Records: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexNumber], Waveform_Info: Array[niRFSA_wfmInfo]) -> int """
        pass

    def FetchIQMultiRecordComplexI16(self, Channel_List, Starting_Record, Number_of_Records, Number_of_Samples, Timeout, Data, Waveform_Info):
        """
        FetchIQMultiRecordComplexI16(self: niRFSA, Channel_List: str, Starting_Record: Int64, Number_of_Records: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[Int16], Waveform_Info: Array[niRFSA_wfmInfo]) -> int
        FetchIQMultiRecordComplexI16(self: niRFSA, Channel_List: str, Starting_Record: Int64, Number_of_Records: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexI16], Waveform_Info: Array[niRFSA_wfmInfo]) -> int
        """
        pass

    def FetchIQSingleRecordComplexF32(self, Channel_List, Record_Number, Number_of_Samples, Timeout, Data, Waveform_Info):
        """
        FetchIQSingleRecordComplexF32(self: niRFSA, Channel_List: str, Record_Number: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexF32]) -> (int, niRFSA_wfmInfo)
        FetchIQSingleRecordComplexF32(self: niRFSA, Channel_List: str, Record_Number: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexNumberF32]) -> (int, niRFSA_wfmInfo)
        """
        pass

    def FetchIQSingleRecordComplexF64(self, Channel_List, Record_Number, Number_of_Samples, Timeout, Data, Waveform_Info):
        """ FetchIQSingleRecordComplexF64(self: niRFSA, Channel_List: str, Record_Number: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexNumber]) -> (int, niRFSA_wfmInfo) """
        pass

    def FetchIQSingleRecordComplexI16(self, Channel_List, Record_Number, Number_of_Samples, Timeout, Data, Waveform_Info):
        """
        FetchIQSingleRecordComplexI16(self: niRFSA, Channel_List: str, Record_Number: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[Int16]) -> (int, niRFSA_wfmInfo)
        FetchIQSingleRecordComplexI16(self: niRFSA, Channel_List: str, Record_Number: Int64, Number_of_Samples: Int64, Timeout: float, Data: Array[niComplexI16]) -> (int, niRFSA_wfmInfo)
        """
        pass

    def GetAcquisitionType(self, channel, value):
        """ GetAcquisitionType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetActiveConfigurationList(self, channel, value):
        """ GetActiveConfigurationList(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetActiveConfigurationListStep(self, channel, value):
        """ GetActiveConfigurationListStep(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetAdvanceTriggerTerminalName(self, channel, value):
        """ GetAdvanceTriggerTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetAdvanceTriggerType(self, channel, value):
        """ GetAdvanceTriggerType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetAllowMoreRecordsThanMemory(self, channel, value):
        """ GetAllowMoreRecordsThanMemory(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetArmRefTriggerType(self, channel, value):
        """ GetArmRefTriggerType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetAttenuation(self, channel, value):
        """ GetAttenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetAttributeBoolean(self, channelName, attributeID, attributeValue):
        """ GetAttributeBoolean(self: niRFSA, channelName: str, attributeID: niRFSAProperties) -> (int, bool) """
        pass

    def GetAttributeInt32(self, channelName, attributeID, attributeValue):
        """ GetAttributeInt32(self: niRFSA, channelName: str, attributeID: niRFSAProperties) -> (int, int) """
        pass

    def GetAttributeInt64(self, channelName, attributeID, attributeValue):
        """ GetAttributeInt64(self: niRFSA, channelName: str, attributeID: niRFSAProperties) -> (int, Int64) """
        pass

    def GetAttributeReal64(self, channelName, attributeID, attributeValue):
        """ GetAttributeReal64(self: niRFSA, channelName: str, attributeID: niRFSAProperties) -> (int, float) """
        pass

    def GetAttributeSession(self, channelName, attributeID, attributeValue):
        """ GetAttributeSession(self: niRFSA, channelName: str, attributeID: niRFSAProperties) -> (int, IntPtr) """
        pass

    def GetAttributeString(self, channelName, attributeID, attributeValue):
        """ GetAttributeString(self: niRFSA, channelName: str, attributeID: niRFSAProperties) -> (int, str) """
        pass

    def GetBoolean(self, propertyId, *__args):
        """
        GetBoolean(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> bool
        GetBoolean(self: niRFSA, propertyId: niRFSAProperties) -> bool
        GetBoolean(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> (int, bool)
        GetBoolean(self: niRFSA, propertyId: niRFSAProperties) -> (int, bool)
        """
        pass

    def GetCache(self, channel, value):
        """ GetCache(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetCalDigitizerId(self, channel, value):
        """ GetCalDigitizerId(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetCalibrationCorrection100mhzFilter(self, channel, value):
        """ GetCalibrationCorrection100mhzFilter(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalibrationCorrection300KhzFilter(self, channel, value):
        """ GetCalibrationCorrection300KhzFilter(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalibrationCorrection320mhzFilter(self, channel, value):
        """ GetCalibrationCorrection320mhzFilter(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalibrationCorrection5MhzFilter(self, channel, value):
        """ GetCalibrationCorrection5MhzFilter(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalibrationCorrection765mhzFilter(self, channel, value):
        """ GetCalibrationCorrection765mhzFilter(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalibrationCorrectionThroughFilter(self, channel, value):
        """ GetCalibrationCorrectionThroughFilter(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalIfAttenuationIndex(self, channel, value):
        """ GetCalIfAttenuationIndex(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalIfAttenuationTableSelection(self, channel, value):
        """ GetCalIfAttenuationTableSelection(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalIfAttenuationTableSize(self, channel, value):
        """ GetCalIfAttenuationTableSize(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalIfFilterSelection(self, channel, value):
        """ GetCalIfFilterSelection(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalLo1Attenuation(self, channel, value):
        """ GetCalLo1Attenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalLo2Attenuation(self, channel, value):
        """ GetCalLo2Attenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalLo3Attenuation(self, channel, value):
        """ GetCalLo3Attenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalLoPathSelection(self, channel, value):
        """ GetCalLoPathSelection(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalRfElectronicAttenuationIndex(self, channel, value):
        """ GetCalRfElectronicAttenuationIndex(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalRfLowbandSignalConditioningPathSelection(self, channel, value):
        """ GetCalRfLowbandSignalConditioningPathSelection(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalRfMechanicalAttenuationIndex(self, channel, value):
        """ GetCalRfMechanicalAttenuationIndex(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalRfPathSelection(self, channel, value):
        """ GetCalRfPathSelection(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalToneFrequency(self, channel, value):
        """ GetCalToneFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalToneMode(self, channel, value):
        """ GetCalToneMode(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetCalTonePowerReferredToRfIn(self, channel, value):
        """ GetCalTonePowerReferredToRfIn(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalToneStepAttenuation(self, channel, value):
        """ GetCalToneStepAttenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetCalUserDefinedInfo(self, userdefinedinfo):
        """ GetCalUserDefinedInfo(self: niRFSA, userdefinedinfo: StringBuilder) -> int """
        pass

    def GetCalUserDefinedInfoMaxSize(self, infoSize):
        """ GetCalUserDefinedInfoMaxSize(self: niRFSA) -> (int, int) """
        pass

    def GetCenterFrequency(self, channel, value):
        """ GetCenterFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetChannelCount(self, channel, value):
        """ GetChannelCount(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetChannelCoupling(self, channel, value):
        """ GetChannelCoupling(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetConfigurationListStepInProgress(self, channel, value):
        """ GetConfigurationListStepInProgress(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetConfigurationListStepTriggerSource(self, channel, value):
        """ GetConfigurationListStepTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetContiguousMultiRecord(self, channel, value):
        """ GetContiguousMultiRecord(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDataTransferBlockSize(self, channel, value):
        """ GetDataTransferBlockSize(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDataTransferMaximumBandwidth(self, channel, value):
        """ GetDataTransferMaximumBandwidth(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDdcRefTriggerOverride(self, channel, value):
        """ GetDdcRefTriggerOverride(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetDecimationDelay(self, channel, value):
        """ GetDecimationDelay(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDeviceConfigurationTemperature(self, channel, value):
        """ GetDeviceConfigurationTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDeviceInstantaneousBandwidth(self, channel, value):
        """ GetDeviceInstantaneousBandwidth(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDeviceResponse(self, channelList, responseType, bufferSize, frequencies, magnitudeResponse, phaseResponse, numberofFrequencies):
        """ GetDeviceResponse(self: niRFSA, channelList: str, responseType: int, bufferSize: int, frequencies: Array[float], magnitudeResponse: Array[float], phaseResponse: Array[float]) -> (int, int) """
        pass

    def GetDeviceTemperature(self, channel, value):
        """ GetDeviceTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDigitalEdgeAdvanceTriggerSource(self, channel, value):
        """ GetDigitalEdgeAdvanceTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetDigitalEdgeArmRefTriggerSource(self, channel, value):
        """ GetDigitalEdgeArmRefTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetDigitalEdgeRefTriggerEdge(self, channel, value):
        """ GetDigitalEdgeRefTriggerEdge(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDigitalEdgeRefTriggerSource(self, channel, value):
        """ GetDigitalEdgeRefTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetDigitalEdgeStartTriggerEdge(self, channel, value):
        """ GetDigitalEdgeStartTriggerEdge(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDigitalEdgeStartTriggerSource(self, channel, value):
        """ GetDigitalEdgeStartTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetDigitalIfEqualizationEnabled(self, channel, value):
        """ GetDigitalIfEqualizationEnabled(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetDigitizerDitherEnabled(self, channel, value):
        """ GetDigitizerDitherEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDigitizerSampleClockRate(self, channel, value):
        """ GetDigitizerSampleClockRate(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDigitizerSampleClockTimebaseRate(self, channel, value):
        """ GetDigitizerSampleClockTimebaseRate(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDigitizerSampleClockTimebaseSource(self, channel, value):
        """ GetDigitizerSampleClockTimebaseSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetDigitizerTemperature(self, channel, value):
        """ GetDigitizerTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDigitizerVerticalRange(self, channel, value):
        """ GetDigitizerVerticalRange(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDoneEventTerminalName(self, channel, value):
        """ GetDoneEventTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetDouble(self, propertyId, *__args):
        """
        GetDouble(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> float
        GetDouble(self: niRFSA, propertyId: niRFSAProperties) -> float
        GetDouble(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> (int, float)
        GetDouble(self: niRFSA, propertyId: niRFSAProperties) -> (int, float)
        """
        pass

    def GetDownconverterCenterFrequency(self, channel, value):
        """ GetDownconverterCenterFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDownconverterGain(self, channel, value):
        """ GetDownconverterGain(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDownconverterLoopBandwidth(self, channel, value):
        """ GetDownconverterLoopBandwidth(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDownconvertorCalToneFrequency(self, channel, value):
        """ GetDownconvertorCalToneFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDownconvertorCalToneMode(self, channel, value):
        """ GetDownconvertorCalToneMode(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDownconvertorFrequencyOffset(self, channel, value):
        """ GetDownconvertorFrequencyOffset(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetDownconvertorPreselectorEnabled(self, channel, value):
        """ GetDownconvertorPreselectorEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetDriverSetup(self, channel, value):
        """ GetDriverSetup(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetEnableFractionalResampling(self, channel, value):
        """ GetEnableFractionalResampling(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetEndOfRecordEventTerminalName(self, channel, value):
        """ GetEndOfRecordEventTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    @staticmethod
    def GetError(*__args):
        """
        GetError(handle: HandleRef, code: int, msg: StringBuilder) -> int
        GetError(self: niRFSA, code: int, msg: StringBuilder) -> int
        """
        pass

    def GetExportedAdvanceTriggerOutputTerminal(self, channel, value):
        """ GetExportedAdvanceTriggerOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedDigitizerSampleClockOutputTerminal(self, channel, value):
        """ GetExportedDigitizerSampleClockOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedDoneEventOutputTerminal(self, channel, value):
        """ GetExportedDoneEventOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedEndOfRecordEventOutputTerminal(self, channel, value):
        """ GetExportedEndOfRecordEventOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedReadyForAdvanceEventOutputTerminal(self, channel, value):
        """ GetExportedReadyForAdvanceEventOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedReadyForRefEventOutputTerminal(self, channel, value):
        """ GetExportedReadyForRefEventOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedReadyForStartEventOutputTerminal(self, channel, value):
        """ GetExportedReadyForStartEventOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedRefClockOutputTerminal(self, channel, value):
        """ GetExportedRefClockOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedRefTriggerOutputTerminal(self, channel, value):
        """ GetExportedRefTriggerOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExportedStartTriggerOutputTerminal(self, channel, value):
        """ GetExportedStartTriggerOutputTerminal(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetExtCalLastDateAndTime(self, year, month, day, hour, minute):
        """ GetExtCalLastDateAndTime(self: niRFSA) -> (int, int, int, int, int, int) """
        pass

    def GetExtCalLastTemp(self, temperature):
        """ GetExtCalLastTemp(self: niRFSA) -> (int, float) """
        pass

    def GetExtCalRecommendedInterval(self, months):
        """ GetExtCalRecommendedInterval(self: niRFSA) -> (int, int) """
        pass

    def GetExternalGain(self, channel, value):
        """ GetExternalGain(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetFetchBacklog(self, Channel_List, Record_Number, Backlog):
        """ GetFetchBacklog(self: niRFSA, Channel_List: str, Record_Number: Int64) -> (int, Int64) """
        pass

    def GetFetchOffset(self, channel, value):
        """ GetFetchOffset(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetFetchRelativeTo(self, channel, value):
        """ GetFetchRelativeTo(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetFftSize(self, channel, value):
        """ GetFftSize(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetFftWidth(self, channel, value):
        """ GetFftWidth(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetFftWindowShapeFactor(self, channel, value):
        """ GetFftWindowShapeFactor(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetFftWindowSize(self, channel, value):
        """ GetFftWindowSize(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetFftWindowType(self, channel, value):
        """ GetFftWindowType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetFpgaBitFilePath(self, channel, value):
        """ GetFpgaBitFilePath(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetFpgaTargetName(self, channel, value):
        """ GetFpgaTargetName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetFrequencyResponse(self, Channel_List, Buffer_Size, Frequencies, Magnitude_Response, Phase_Response, Number_of_Frequencies):
        """ GetFrequencyResponse(self: niRFSA, Channel_List: str, Buffer_Size: int, Frequencies: Array[float], Magnitude_Response: Array[float], Phase_Response: Array[float]) -> (int, int) """
        pass

    def GetFrequencySettling(self, channel, value):
        """ GetFrequencySettling(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetFrequencySettlingUnits(self, channel, value):
        """ GetFrequencySettlingUnits(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetGainReferenceCalBaseline(self, bufferSize, gainReferenceCalConstants, numberofRefCalConstants):
        """ GetGainReferenceCalBaseline(self: niRFSA, bufferSize: int, gainReferenceCalConstants: Array[float]) -> (int, int) """
        pass

    def GetGroupCapabilities(self, channel, value):
        """ GetGroupCapabilities(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIf1AttenValue(self, channel, value):
        """ GetIf1AttenValue(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIf2AttenValue(self, channel, value):
        """ GetIf2AttenValue(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIfAttenuation(self, channel, value):
        """ GetIfAttenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIfConditioningDownConversionEnabled(self, channel, value):
        """ GetIfConditioningDownConversionEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetIfConditioningTemperature(self, channel, value):
        """ GetIfConditioningTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIfFilter(self, channel, value):
        """ GetIfFilter(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetIfFilterBandwidth(self, channel, value):
        """ GetIfFilterBandwidth(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIfOutputFrequency(self, channel, value):
        """ GetIfOutputFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIfOutputPowerLevel(self, channel, value):
        """ GetIfOutputPowerLevel(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIfOutputPowerLevelOffset(self, channel, value):
        """ GetIfOutputPowerLevelOffset(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetInputIsolationEnabled(self, channel, value):
        """ GetInputIsolationEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetInputPort(self, channel, value):
        """ GetInputPort(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetInstrumentFirmwareRevision(self, channel, value):
        """ GetInstrumentFirmwareRevision(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetInstrumentManufacturer(self, channel, value):
        """ GetInstrumentManufacturer(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetInstrumentModel(self, channel, value):
        """ GetInstrumentModel(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetInt32(self, propertyId, *__args):
        """
        GetInt32(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> int
        GetInt32(self: niRFSA, propertyId: niRFSAProperties) -> int
        GetInt32(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> (int, int)
        GetInt32(self: niRFSA, propertyId: niRFSAProperties) -> (int, int)
        """
        pass

    def GetInt64(self, *__args):
        """
        GetInt64(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> (int, Int64)
        GetInt64(self: niRFSA, propertyId: niRFSAProperties) -> (int, Int64)
        GetInt64(self: niRFSA, repeatedCapabilityOrChannel: str, propertyId: niRFSAProperties) -> (int, Int64)
        """
        pass

    def GetInterchangeCheck(self, channel, value):
        """ GetInterchangeCheck(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetIoResourceDescriptor(self, channel, value):
        """ GetIoResourceDescriptor(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetIqAnalogEdgeRefTrigger(self, channel, value):
        """ GetIqAnalogEdgeRefTrigger(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetIqAnalogEdgeRefTriggerHysteresis(self, channel, value):
        """ GetIqAnalogEdgeRefTriggerHysteresis(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqAnalogEdgeRefTriggerLevel(self, channel, value):
        """ GetIqAnalogEdgeRefTriggerLevel(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqAnalogEdgeRefTriggerSlope(self, channel, value):
        """ GetIqAnalogEdgeRefTriggerSlope(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetIqAnalogEdgeRefTriggerSource(self, channel, value):
        """ GetIqAnalogEdgeRefTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetIqCarrierFrequency(self, channel, value):
        """ GetIqCarrierFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqInPortCarrierFrequency(self, channel, value):
        """ GetIqInPortCarrierFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqInPortTemperature(self, channel, value):
        """ GetIqInPortTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqInportTerminalConfiguration(self, channel, value):
        """ GetIqInportTerminalConfiguration(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetIqInPortVerticalRange(self, channel, value):
        """ GetIqInPortVerticalRange(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqPowerEdgeRefTriggerLevel(self, channel, value):
        """ GetIqPowerEdgeRefTriggerLevel(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetIqPowerEdgeRefTriggerSlope(self, channel, value):
        """ GetIqPowerEdgeRefTriggerSlope(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetIqPowerEdgeRefTriggerSource(self, channel, value):
        """ GetIqPowerEdgeRefTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetIqRate(self, channel, value):
        """ GetIqRate(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetLo2ExportEnabled(self, channel, value):
        """ GetLo2ExportEnabled(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetLoExportEnabled(self, channel, value):
        """ GetLoExportEnabled(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetLoFrequency(self, channel, value):
        """ GetLoFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetLoFrequencyStepSize(self, channel, value):
        """ GetLoFrequencyStepSize(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetLogicalName(self, channel, value):
        """ GetLogicalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetLoInjectionSide(self, channel, value):
        """ GetLoInjectionSide(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetLoInPower(self, channel, value):
        """ GetLoInPower(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetLoPllFractionalModeEnabled(self, channel, value):
        """ GetLoPllFractionalModeEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetLoSource(self, channel, value):
        """ GetLoSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetLoTemperature(self, channel, value):
        """ GetLoTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetLowFrequencyByPassEnabled(self, channel, value):
        """ GetLowFrequencyByPassEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetLoYigMainCoilDrive(self, channel, value):
        """ GetLoYigMainCoilDrive(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetMaxDeviceInstantaneousBandwidth(self, channel, value):
        """ GetMaxDeviceInstantaneousBandwidth(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetMaxIQRate(self, channel, value):
        """ GetMaxIQRate(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetMechanicalAttenuation(self, channel, value):
        """ GetMechanicalAttenuation(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetMechanicalAttenuatorEnabled(self, channel, value):
        """ GetMechanicalAttenuatorEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetMemorySize(self, channel, value):
        """ GetMemorySize(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetMinimumAcpr(self, channel, value):
        """ GetMinimumAcpr(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetMinimumReconfigTime(self, channel, value):
        """ GetMinimumReconfigTime(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetMixerLevel(self, channel, value):
        """ GetMixerLevel(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetMixerLevelOffset(self, channel, value):
        """ GetMixerLevelOffset(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetModuleRevision(self, channel, value):
        """ GetModuleRevision(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetNoiseSourcePowerEnabled(self, channel, value):
        """ GetNoiseSourcePowerEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetNormalizationCoefficients(self, channelList, bufferSize, coefficientInfo, numberofCoefficientSets):
        """ GetNormalizationCoefficients(self: niRFSA, channelList: str, bufferSize: int) -> (int, niRFSA_coefficientInfo, int) """
        pass

    def GetNotchFilterEnabled(self, channel, value):
        """ GetNotchFilterEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetNumberOfRecords(self, channel, value):
        """ GetNumberOfRecords(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetNumberOfRecordsIsFinite(self, channel, value):
        """ GetNumberOfRecordsIsFinite(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetNumberOfSamples(self, channel, value):
        """ GetNumberOfSamples(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetNumberOfSamplesIsFinite(self, channel, value):
        """ GetNumberOfSamplesIsFinite(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetNumberOfSpectralLines(self, Channel_List, Number_of_Spectral_Lines):
        """ GetNumberOfSpectralLines(self: niRFSA, Channel_List: str) -> (int, int) """
        pass

    def GetNumberOfSpectralLinesAttribute(self, channel, value):
        """ GetNumberOfSpectralLinesAttribute(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetOspDataScalingFactor(self, channel, value):
        """ GetOspDataScalingFactor(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetP2pEnabled(self, channel, value):
        """ GetP2pEnabled(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetP2pEndpointOverflow(self, channel, value):
        """ GetP2pEndpointOverflow(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetP2pEndpointSize(self, channel, value):
        """ GetP2pEndpointSize(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetP2pFifoEndpointCount(self, channel, value):
        """ GetP2pFifoEndpointCount(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetP2pMostSamplesAvailableInEndpoint(self, channel, value):
        """ GetP2pMostSamplesAvailableInEndpoint(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetP2pOnboardMemoryEnabled(self, channel, value):
        """ GetP2pOnboardMemoryEnabled(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetP2pSamplesAvailableInEndpoint(self, channel, value):
        """ GetP2pSamplesAvailableInEndpoint(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetP2pSamplesTransferred(self, channel, value):
        """ GetP2pSamplesTransferred(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetPhaseOffset(self, channel, value):
        """ GetPhaseOffset(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetPowerSpectrumUnits(self, channel, value):
        """ GetPowerSpectrumUnits(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetPreselectorEnabled(self, channel, value):
        """ GetPreselectorEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetPreselectorPresent(self, channel, value):
        """ GetPreselectorPresent(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetPreselectorTuningDacValue5665(self, channel, value):
        """ GetPreselectorTuningDacValue5665(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetPxiChassisClk10Source(self, channel, value):
        """ GetPxiChassisClk10Source(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetQueryInstrumentStatus(self, channel, value):
        """ GetQueryInstrumentStatus(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetRangeCheck(self, channel, value):
        """ GetRangeCheck(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetReadyForAdvanceEventTerminalName(self, channel, value):
        """ GetReadyForAdvanceEventTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetReadyForRefEventTerminalName(self, channel, value):
        """ GetReadyForRefEventTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetReadyForStartEventTerminalName(self, channel, value):
        """ GetReadyForStartEventTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetReconfigurationTriggerSource(self, channel, value):
        """ GetReconfigurationTriggerSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetRecordCoercions(self, channel, value):
        """ GetRecordCoercions(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetRecordsDone(self, channel, value):
        """ GetRecordsDone(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRefClockRate(self, channel, value):
        """ GetRefClockRate(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRefClockSource(self, channel, value):
        """ GetRefClockSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetReferenceLevel(self, channel, value):
        """ GetReferenceLevel(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRefToRefTriggerHoldoff(self, channel, value):
        """ GetRefToRefTriggerHoldoff(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRefTriggerDelay(self, channel, value):
        """ GetRefTriggerDelay(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRefTriggerMinimumQuietTime(self, channel, value):
        """ GetRefTriggerMinimumQuietTime(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRefTriggerOspDelayEnabled(self, channel, value):
        """ GetRefTriggerOspDelayEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRefTriggerPretriggerSamples(self, channel, value):
        """ GetRefTriggerPretriggerSamples(self: niRFSA, channel: str) -> (int, Int64) """
        pass

    def GetRefTriggerTerminalName(self, channel, value):
        """ GetRefTriggerTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetRefTriggerType(self, channel, value):
        """ GetRefTriggerType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRelayName(self, channelList, indexofRelay, name, bufferSize):
        """ GetRelayName(self: niRFSA, channelList: str, indexofRelay: int, name: StringBuilder) -> (int, int) """
        pass

    def GetRelayOperationsCount(self, channelList, operationsCountArray, bufferSize):
        """ GetRelayOperationsCount(self: niRFSA, channelList: str, operationsCountArray: Array[int]) -> (int, int) """
        pass

    def GetResolutionBandwidth(self, channel, value):
        """ GetResolutionBandwidth(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetResolutionBandwidthType(self, channel, value):
        """ GetResolutionBandwidthType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRfAttenuationIndex(self, channel, value):
        """ GetRfAttenuationIndex(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRfAttenuationStepSize(self, channel, value):
        """ GetRfAttenuationStepSize(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRfAttenuationTable(self, channel, value):
        """ GetRfAttenuationTable(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRfConditioningTemperature(self, channel, value):
        """ GetRfConditioningTemperature(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRfHighPassFilteringe(self, channel, value):
        """ GetRfHighPassFilteringe(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRfPreampEnabled(self, channel, value):
        """ GetRfPreampEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRfPreampPresent(self, channel, value):
        """ GetRfPreampPresent(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetRfPreselectorCalToneFrequency(self, channel, value):
        """ GetRfPreselectorCalToneFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetRfPreselectorCalToneMode(self, channel, value):
        """ GetRfPreselectorCalToneMode(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetRfPreselectorFilter(self, channel, value):
        """ GetRfPreselectorFilter(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetScalingCoefficients(self, channelList, arraySize, coefficientInfo, numberOfCoefficientSets):
        """ GetScalingCoefficients(self: niRFSA, channelList: str, arraySize: int) -> (int, niRFSA_coefficientInfo, int) """
        pass

    def GetSelfCalLastDateAndTime(self, selfCalibrationStep, year, month, day, hour, minute):
        """ GetSelfCalLastDateAndTime(self: niRFSA, selfCalibrationStep: Int64) -> (int, int, int, int, int, int) """
        pass

    def GetSelfCalLastTemp(self, selfCalibrationStep, temperature):
        """ GetSelfCalLastTemp(self: niRFSA, selfCalibrationStep: Int64) -> (int, float) """
        pass

    def GetSerialNumber(self, channel, value):
        """ GetSerialNumber(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSession(self, propertyId, *__args):
        """
        GetSession(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> (int, IntPtr)
        GetSession(self: niRFSA, propertyId: niRFSAProperties) -> (int, IntPtr)
        """
        pass

    def GetSignalConditioningEnabled(self, channel, value):
        """ GetSignalConditioningEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSimulate(self, channel, value):
        """ GetSimulate(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetSmoothSpectrumEnabled(self, channel, value):
        """ GetSmoothSpectrumEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSpecificDriverClassSpecMajorVersion(self, channel, value):
        """ GetSpecificDriverClassSpecMajorVersion(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSpecificDriverClassSpecMinorVersion(self, channel, value):
        """ GetSpecificDriverClassSpecMinorVersion(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSpecificDriverDescription(self, channel, value):
        """ GetSpecificDriverDescription(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSpecificDriverPrefix(self, channel, value):
        """ GetSpecificDriverPrefix(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSpecificDriverRevision(self, channel, value):
        """ GetSpecificDriverRevision(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSpecificDriverVendor(self, channel, value):
        """ GetSpecificDriverVendor(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSpectralInfoForSMT(self, Spectrum_Info):
        """ GetSpectralInfoForSMT(self: niRFSA) -> (int, SmtSpectrumInfo) """
        pass

    def GetSpectrumAveragingMode(self, channel, value):
        """ GetSpectrumAveragingMode(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSpectrumCenterFrequency(self, channel, value):
        """ GetSpectrumCenterFrequency(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetSpectrumNumberOfAverages(self, channel, value):
        """ GetSpectrumNumberOfAverages(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSpectrumOspSamplingRatio(self, channel, value):
        """ GetSpectrumOspSamplingRatio(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetSpectrumSpan(self, channel, value):
        """ GetSpectrumSpan(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetStartToRefTriggerHoldoff(self, channel, value):
        """ GetStartToRefTriggerHoldoff(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetStartTriggerDelay(self, channel, value):
        """ GetStartTriggerDelay(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetStartTriggerTerminalName(self, channel, value):
        """ GetStartTriggerTerminalName(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetStartTriggerType(self, channel, value):
        """ GetStartTriggerType(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetStepGainEnabled(self, channel, value):
        """ GetStepGainEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetStreamEndpointHandle(self, streamEndpoint, writerHandle):
        """ GetStreamEndpointHandle(self: niRFSA, streamEndpoint: str) -> (int, UInt32) """
        pass

    def GetString(self, propertyId, *__args):
        """
        GetString(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> str
        GetString(self: niRFSA, propertyId: niRFSAProperties) -> str
        GetString(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str) -> (int, str)
        GetString(self: niRFSA, propertyId: niRFSAProperties) -> (int, str)
        """
        pass

    def GetSubspanOverlap(self, channel, value):
        """ GetSubspanOverlap(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetSupportedInstrumentModels(self, channel, value):
        """ GetSupportedInstrumentModels(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSyncAdvanceTriggerDistLine(self, channel, value):
        """ GetSyncAdvanceTriggerDistLine(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSyncAdvanceTriggerMaster(self, channel, value):
        """ GetSyncAdvanceTriggerMaster(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetSyncRefTriggerDelayEnabled(self, channel, value):
        """ GetSyncRefTriggerDelayEnabled(self: niRFSA, channel: str) -> (int, int) """
        pass

    def GetSyncRefTriggerDistLine(self, channel, value):
        """ GetSyncRefTriggerDistLine(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSyncRefTriggerMaster(self, channel, value):
        """ GetSyncRefTriggerMaster(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetSyncSampleClockDistLine(self, channel, value):
        """ GetSyncSampleClockDistLine(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSyncSampleClockMaster(self, channel, value):
        """ GetSyncSampleClockMaster(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetSyncStartTriggerDistLine(self, channel, value):
        """ GetSyncStartTriggerDistLine(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetSyncStartTriggerMaster(self, channel, value):
        """ GetSyncStartTriggerMaster(self: niRFSA, channel: str) -> (int, bool) """
        pass

    def GetTemperatureReadInterval(self, channel, value):
        """ GetTemperatureReadInterval(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetTerminalName(self, signal, signalIdentifier, bufferSize, terminalName):
        """ GetTerminalName(self: niRFSA, signal: int, signalIdentifier: str, bufferSize: int, terminalName: StringBuilder) -> int """
        pass

    def GetTimerEventInterval(self, channel, value):
        """ GetTimerEventInterval(self: niRFSA, channel: str) -> (int, float) """
        pass

    def GetTimerStartSource(self, channel, value):
        """ GetTimerStartSource(self: niRFSA, channel: str) -> (int, str) """
        pass

    def GetUserData(self, identifier, bufferSize, data, actualDataSize):
        """ GetUserData(self: niRFSA, identifier: str, bufferSize: int, data: Array[Byte], actualDataSize: int) -> (int, int) """
        pass

    def InitExtCal(self, resourceName, password, optionstring, instrumentHandle):
        """ InitExtCal(self: niRFSA, resourceName: str, password: str, optionstring: str) -> (int, HandleRef) """
        pass

    def InitializeCalibrationStep(self, calibrationstep):
        """ InitializeCalibrationStep(self: niRFSA, calibrationstep: int) -> int """
        pass

    def InitializeExternalAlignment(self, resourceName, optionstring, instrumentHandle):
        """ InitializeExternalAlignment(self: niRFSA, resourceName: str, optionstring: str) -> (int, HandleRef) """
        pass

    def InitializeExternalAlignmentStep(self, externalAlignmentStep):
        """ InitializeExternalAlignmentStep(self: niRFSA, externalAlignmentStep: int) -> int """
        pass

    def Initiate(self):
        """ Initiate(self: niRFSA) -> int """
        pass

    def InvalidateAllAttributes(self):
        """ InvalidateAllAttributes(self: niRFSA) -> int """
        pass

    def IsSelfCalValid(self, selfCalValid, validSteps):
        """ IsSelfCalValid(self: niRFSA) -> (int, bool, Int64) """
        pass

    def LockSession(self, callerHasLock):
        """ LockSession(self: niRFSA, callerHasLock: bool) -> (int, bool) """
        pass

    def PerformThermalCorrection(self):
        """ PerformThermalCorrection(self: niRFSA) -> int """
        pass

    def ReadIQSingleRecordComplexF64(self, Channel_List, Timeout, Data, Data_Array_Size, Waveform_Info):
        """ ReadIQSingleRecordComplexF64(self: niRFSA, Channel_List: str, Timeout: float, Data: Array[niComplexNumber], Data_Array_Size: Int64) -> (int, niRFSA_wfmInfo) """
        pass

    def ReadPowerSpectrumF64(self, Channel_List, Timeout, Power_Spectrum_Data, Data_Array_Size, Spectrum_Info):
        """ ReadPowerSpectrumF64(self: niRFSA, Channel_List: str, Timeout: float, Power_Spectrum_Data: Array[float], Data_Array_Size: int) -> (int, niRFSA_spectrumInfo) """
        pass

    def reset(self):
        """ reset(self: niRFSA) -> int """
        pass

    def ResetAttribute(self, Channel_Name, Attribute_ID):
        """ ResetAttribute(self: niRFSA, Channel_Name: str, Attribute_ID: int) -> int """
        pass

    def ResetDevice(self):
        """ ResetDevice(self: niRFSA) -> int """
        pass

    def ResetWithDefaults(self):
        """ ResetWithDefaults(self: niRFSA) -> int """
        pass

    def ResetWithOptions(self, stepsToOmit):
        """ ResetWithOptions(self: niRFSA, stepsToOmit: UInt64) -> int """
        pass

    def revision_query(self, Instrument_Driver_Revision, Firmware_Revision):
        """ revision_query(self: niRFSA, Instrument_Driver_Revision: StringBuilder, Firmware_Revision: StringBuilder) -> int """
        pass

    def SelfCal(self):
        """ SelfCal(self: niRFSA) -> int """
        pass

    def SelfCalibrate(self, stepsToOmit):
        """ SelfCalibrate(self: niRFSA, stepsToOmit: Int64) -> int """
        pass

    def SelfCalibrateRange(self, stepsToOmit, minFrequency, maxFrequency, minReferenceLevel, maxReferenceLevel):
        """ SelfCalibrateRange(self: niRFSA, stepsToOmit: Int64, minFrequency: float, maxFrequency: float, minReferenceLevel: float, maxReferenceLevel: float) -> int """
        pass

    def self_test(self, testResult, testMessage):
        """ self_test(self: niRFSA, testMessage: StringBuilder) -> (int, Int16) """
        pass

    def SendSoftwareEdgeTrigger(self, Trigger, Trigger_Identifier):
        """ SendSoftwareEdgeTrigger(self: niRFSA, Trigger: int, Trigger_Identifier: str) -> int """
        pass

    def SetAcquisitionType(self, channel, value):
        """ SetAcquisitionType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetActiveConfigurationList(self, channel, value):
        """ SetActiveConfigurationList(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetActiveConfigurationListStep(self, channel, value):
        """ SetActiveConfigurationListStep(self: niRFSA, channel: str, value: Int64) -> int """
        pass

    def SetAdvanceTriggerType(self, channel, value):
        """ SetAdvanceTriggerType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetAllowMoreRecordsThanMemory(self, channel, value):
        """ SetAllowMoreRecordsThanMemory(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetArmRefTriggerType(self, channel, value):
        """ SetArmRefTriggerType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetAttenuation(self, channel, value):
        """ SetAttenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetAttributeBoolean(self, channelName, attributeID, attributeValue):
        """ SetAttributeBoolean(self: niRFSA, channelName: str, attributeID: niRFSAProperties, attributeValue: bool) -> int """
        pass

    def SetAttributeInt32(self, channelName, attributeID, attributeValue):
        """ SetAttributeInt32(self: niRFSA, channelName: str, attributeID: niRFSAProperties, attributeValue: int) -> int """
        pass

    def SetAttributeInt64(self, channelName, attributeID, attributeValue):
        """ SetAttributeInt64(self: niRFSA, channelName: str, attributeID: niRFSAProperties, attributeValue: Int64) -> int """
        pass

    def SetAttributeReal64(self, channelName, attributeID, attributeValue):
        """ SetAttributeReal64(self: niRFSA, channelName: str, attributeID: niRFSAProperties, attributeValue: float) -> int """
        pass

    def SetAttributeSession(self, channelName, attributeID, attributeValue):
        """ SetAttributeSession(self: niRFSA, channelName: str, attributeID: niRFSAProperties, attributeValue: IntPtr) -> int """
        pass

    def SetAttributeString(self, channelName, attributeID, attributeValue):
        """ SetAttributeString(self: niRFSA, channelName: str, attributeID: niRFSAProperties, attributeValue: str) -> int """
        pass

    def SetBoolean(self, propertyId, *__args):
        """
        SetBoolean(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str, val: bool) -> int
        SetBoolean(self: niRFSA, propertyId: niRFSAProperties, val: bool) -> int
        """
        pass

    def SetCache(self, channel, value):
        """ SetCache(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetCalDigitizerId(self, channel, value):
        """ SetCalDigitizerId(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetCalibrationCorrection100mhzFilter(self, channel, value):
        """ SetCalibrationCorrection100mhzFilter(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalibrationCorrection300KhzFilter(self, channel, value):
        """ SetCalibrationCorrection300KhzFilter(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalibrationCorrection320mhzFilter(self, channel, value):
        """ SetCalibrationCorrection320mhzFilter(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalibrationCorrection5MhzFilter(self, channel, value):
        """ SetCalibrationCorrection5MhzFilter(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalibrationCorrection765mhzFilter(self, channel, value):
        """ SetCalibrationCorrection765mhzFilter(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalibrationCorrectionThroughFilter(self, channel, value):
        """ SetCalibrationCorrectionThroughFilter(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalIfAttenuationIndex(self, channel, value):
        """ SetCalIfAttenuationIndex(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalIfAttenuationTableSelection(self, channel, value):
        """ SetCalIfAttenuationTableSelection(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalIfAttenuationTableSize(self, channel, value):
        """ SetCalIfAttenuationTableSize(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalIfFilterSelection(self, channel, value):
        """ SetCalIfFilterSelection(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalLo1Attenuation(self, channel, value):
        """ SetCalLo1Attenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalLo2Attenuation(self, channel, value):
        """ SetCalLo2Attenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalLo3Attenuation(self, channel, value):
        """ SetCalLo3Attenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalLoPathSelection(self, channel, value):
        """ SetCalLoPathSelection(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalRfElectronicAttenuationIndex(self, channel, value):
        """ SetCalRfElectronicAttenuationIndex(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalRfLowbandSignalConditioningPathSelection(self, channel, value):
        """ SetCalRfLowbandSignalConditioningPathSelection(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalRfMechanicalAttenuationIndex(self, channel, value):
        """ SetCalRfMechanicalAttenuationIndex(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalRfPathSelection(self, channel, value):
        """ SetCalRfPathSelection(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalToneFrequency(self, channel, value):
        """ SetCalToneFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalToneMode(self, channel, value):
        """ SetCalToneMode(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetCalTonePowerReferredToRfIn(self, channel, value):
        """ SetCalTonePowerReferredToRfIn(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalToneStepAttenuation(self, channel, value):
        """ SetCalToneStepAttenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetCalUserDefinedInfo(self, userdefinedinfo):
        """ SetCalUserDefinedInfo(self: niRFSA, userdefinedinfo: str) -> int """
        pass

    def SetCenterFrequency(self, channel, value):
        """ SetCenterFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetChannelCoupling(self, channel, value):
        """ SetChannelCoupling(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetConfigurationListStepTriggerSource(self, channel, value):
        """ SetConfigurationListStepTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetContiguousMultiRecord(self, channel, value):
        """ SetContiguousMultiRecord(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDataTransferBlockSize(self, channel, value):
        """ SetDataTransferBlockSize(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDataTransferMaximumBandwidth(self, channel, value):
        """ SetDataTransferMaximumBandwidth(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDdcRefTriggerOverride(self, channel, value):
        """ SetDdcRefTriggerOverride(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetDecimationDelay(self, channel, value):
        """ SetDecimationDelay(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDeviceConfigurationTemperature(self, channel, value):
        """ SetDeviceConfigurationTemperature(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDeviceInstantaneousBandwidth(self, channel, value):
        """ SetDeviceInstantaneousBandwidth(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDigitalEdgeAdvanceTriggerSource(self, channel, value):
        """ SetDigitalEdgeAdvanceTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetDigitalEdgeArmRefTriggerSource(self, channel, value):
        """ SetDigitalEdgeArmRefTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetDigitalEdgeRefTriggerEdge(self, channel, value):
        """ SetDigitalEdgeRefTriggerEdge(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDigitalEdgeRefTriggerSource(self, channel, value):
        """ SetDigitalEdgeRefTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetDigitalEdgeStartTriggerEdge(self, channel, value):
        """ SetDigitalEdgeStartTriggerEdge(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDigitalEdgeStartTriggerSource(self, channel, value):
        """ SetDigitalEdgeStartTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetDigitalIfEqualizationEnabled(self, channel, value):
        """ SetDigitalIfEqualizationEnabled(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetDigitizerDitherEnabled(self, channel, value):
        """ SetDigitizerDitherEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDigitizerSampleClockRate(self, channel, value):
        """ SetDigitizerSampleClockRate(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDigitizerSampleClockTimebaseRate(self, channel, value):
        """ SetDigitizerSampleClockTimebaseRate(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDigitizerSampleClockTimebaseSource(self, channel, value):
        """ SetDigitizerSampleClockTimebaseSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetDigitizerVerticalRange(self, channel, value):
        """ SetDigitizerVerticalRange(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDouble(self, propertyId, *__args):
        """
        SetDouble(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str, val: float) -> int
        SetDouble(self: niRFSA, propertyId: niRFSAProperties, val: float) -> int
        """
        pass

    def SetDownconverterCenterFrequency(self, channel, value):
        """ SetDownconverterCenterFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDownconverterGain(self, channel, value):
        """ SetDownconverterGain(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDownconverterLoopBandwidth(self, channel, value):
        """ SetDownconverterLoopBandwidth(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDownconvertorCalToneFrequency(self, channel, value):
        """ SetDownconvertorCalToneFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDownconvertorCalToneMode(self, channel, value):
        """ SetDownconvertorCalToneMode(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetDownconvertorFrequencyOffset(self, channel, value):
        """ SetDownconvertorFrequencyOffset(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetDownconvertorPreselectorEnabled(self, channel, value):
        """ SetDownconvertorPreselectorEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetEnableFractionalResampling(self, channel, value):
        """ SetEnableFractionalResampling(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetExportedAdvanceTriggerOutputTerminal(self, channel, value):
        """ SetExportedAdvanceTriggerOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedDigitizerSampleClockOutputTerminal(self, channel, value):
        """ SetExportedDigitizerSampleClockOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedDoneEventOutputTerminal(self, channel, value):
        """ SetExportedDoneEventOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedEndOfRecordEventOutputTerminal(self, channel, value):
        """ SetExportedEndOfRecordEventOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedReadyForAdvanceEventOutputTerminal(self, channel, value):
        """ SetExportedReadyForAdvanceEventOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedReadyForRefEventOutputTerminal(self, channel, value):
        """ SetExportedReadyForRefEventOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedReadyForStartEventOutputTerminal(self, channel, value):
        """ SetExportedReadyForStartEventOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedRefClockOutputTerminal(self, channel, value):
        """ SetExportedRefClockOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedRefTriggerOutputTerminal(self, channel, value):
        """ SetExportedRefTriggerOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExportedStartTriggerOutputTerminal(self, channel, value):
        """ SetExportedStartTriggerOutputTerminal(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetExternalGain(self, channel, value):
        """ SetExternalGain(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetFetchOffset(self, channel, value):
        """ SetFetchOffset(self: niRFSA, channel: str, value: Int64) -> int """
        pass

    def SetFetchRelativeTo(self, channel, value):
        """ SetFetchRelativeTo(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetFftWidth(self, channel, value):
        """ SetFftWidth(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetFftWindowType(self, channel, value):
        """ SetFftWindowType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetFpgaTargetName(self, channel, value):
        """ SetFpgaTargetName(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetFrequencySettling(self, channel, value):
        """ SetFrequencySettling(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetFrequencySettlingUnits(self, channel, value):
        """ SetFrequencySettlingUnits(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetIf1AttenValue(self, channel, value):
        """ SetIf1AttenValue(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIf2AttenValue(self, channel, value):
        """ SetIf2AttenValue(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIfAttenuation(self, channel, value):
        """ SetIfAttenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIfConditioningDownConversionEnabled(self, channel, value):
        """ SetIfConditioningDownConversionEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetIfFilter(self, channel, value):
        """ SetIfFilter(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetIfFilterBandwidth(self, channel, value):
        """ SetIfFilterBandwidth(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIfOutputPowerLevel(self, channel, value):
        """ SetIfOutputPowerLevel(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIfOutputPowerLevelOffset(self, channel, value):
        """ SetIfOutputPowerLevelOffset(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetInputIsolationEnabled(self, channel, value):
        """ SetInputIsolationEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetInputPort(self, channel, value):
        """ SetInputPort(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetInt32(self, propertyId, *__args):
        """
        SetInt32(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str, val: int) -> int
        SetInt32(self: niRFSA, propertyId: niRFSAProperties, val: int) -> int
        """
        pass

    def SetInt64(self, propertyId, *__args):
        """
        SetInt64(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str, val: Int64) -> int
        SetInt64(self: niRFSA, propertyId: niRFSAProperties, val: Int64) -> int
        """
        pass

    def SetInterchangeCheck(self, channel, value):
        """ SetInterchangeCheck(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetIqAnalogEdgeRefTrigger(self, channel, value):
        """ SetIqAnalogEdgeRefTrigger(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetIqAnalogEdgeRefTriggerHysteresis(self, channel, value):
        """ SetIqAnalogEdgeRefTriggerHysteresis(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqAnalogEdgeRefTriggerLevel(self, channel, value):
        """ SetIqAnalogEdgeRefTriggerLevel(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqAnalogEdgeRefTriggerSlope(self, channel, value):
        """ SetIqAnalogEdgeRefTriggerSlope(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetIqAnalogEdgeRefTriggerSource(self, channel, value):
        """ SetIqAnalogEdgeRefTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetIqCarrierFrequency(self, channel, value):
        """ SetIqCarrierFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqInPortCarrierFrequency(self, channel, value):
        """ SetIqInPortCarrierFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqInPortTemperature(self, channel, value):
        """ SetIqInPortTemperature(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqInportTerminalConfiguration(self, channel, value):
        """ SetIqInportTerminalConfiguration(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetIqInPortVerticalRange(self, channel, value):
        """ SetIqInPortVerticalRange(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqPowerEdgeRefTriggerLevel(self, channel, value):
        """ SetIqPowerEdgeRefTriggerLevel(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetIqPowerEdgeRefTriggerSlope(self, channel, value):
        """ SetIqPowerEdgeRefTriggerSlope(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetIqPowerEdgeRefTriggerSource(self, channel, value):
        """ SetIqPowerEdgeRefTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetIqRate(self, channel, value):
        """ SetIqRate(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetLo2ExportEnabled(self, channel, value):
        """ SetLo2ExportEnabled(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetLoExportEnabled(self, channel, value):
        """ SetLoExportEnabled(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetLoFrequency(self, channel, value):
        """ SetLoFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetLoFrequencyStepSize(self, channel, value):
        """ SetLoFrequencyStepSize(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetLoInjectionSide(self, channel, value):
        """ SetLoInjectionSide(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetLoInPower(self, channel, value):
        """ SetLoInPower(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetLoPllFractionalModeEnabled(self, channel, value):
        """ SetLoPllFractionalModeEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetLoSource(self, channel, value):
        """ SetLoSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetLowFrequencyByPassEnabled(self, channel, value):
        """ SetLowFrequencyByPassEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetLoYigMainCoilDrive(self, channel, value):
        """ SetLoYigMainCoilDrive(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetMaxDeviceInstantaneousBandwidth(self, channel, value):
        """ SetMaxDeviceInstantaneousBandwidth(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetMaxIQRate(self, channel, value):
        """ SetMaxIQRate(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetMechanicalAttenuation(self, channel, value):
        """ SetMechanicalAttenuation(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetMechanicalAttenuatorEnabled(self, channel, value):
        """ SetMechanicalAttenuatorEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetMinimumAcpr(self, channel, value):
        """ SetMinimumAcpr(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetMinimumReconfigTime(self, channel, value):
        """ SetMinimumReconfigTime(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetMixerLevel(self, channel, value):
        """ SetMixerLevel(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetMixerLevelOffset(self, channel, value):
        """ SetMixerLevelOffset(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetNoiseSourcePowerEnabled(self, channel, value):
        """ SetNoiseSourcePowerEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetNotchFilterEnabled(self, channel, value):
        """ SetNotchFilterEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetNumberOfRecords(self, channel, value):
        """ SetNumberOfRecords(self: niRFSA, channel: str, value: Int64) -> int """
        pass

    def SetNumberOfRecordsIsFinite(self, channel, value):
        """ SetNumberOfRecordsIsFinite(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetNumberOfSamples(self, channel, value):
        """ SetNumberOfSamples(self: niRFSA, channel: str, value: Int64) -> int """
        pass

    def SetNumberOfSamplesIsFinite(self, channel, value):
        """ SetNumberOfSamplesIsFinite(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetNumberOfSpectralLines(self, channel, value):
        """ SetNumberOfSpectralLines(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetOspDataScalingFactor(self, channel, value):
        """ SetOspDataScalingFactor(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetP2pEnabled(self, channel, value):
        """ SetP2pEnabled(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetP2pOnboardMemoryEnabled(self, channel, value):
        """ SetP2pOnboardMemoryEnabled(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetPhaseOffset(self, channel, value):
        """ SetPhaseOffset(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetPowerSpectrumUnits(self, channel, value):
        """ SetPowerSpectrumUnits(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetPreselectorEnabled(self, channel, value):
        """ SetPreselectorEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetPreselectorTuningDacValue5665(self, channel, value):
        """ SetPreselectorTuningDacValue5665(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetPxiChassisClk10Source(self, channel, value):
        """ SetPxiChassisClk10Source(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetQueryInstrumentStatus(self, channel, value):
        """ SetQueryInstrumentStatus(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetRangeCheck(self, channel, value):
        """ SetRangeCheck(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetReconfigurationTriggerSource(self, channel, value):
        """ SetReconfigurationTriggerSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetRecordCoercions(self, channel, value):
        """ SetRecordCoercions(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetRefClockRate(self, channel, value):
        """ SetRefClockRate(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRefClockSource(self, channel, value):
        """ SetRefClockSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetReferenceLevel(self, channel, value):
        """ SetReferenceLevel(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRefToRefTriggerHoldoff(self, channel, value):
        """ SetRefToRefTriggerHoldoff(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRefTriggerDelay(self, channel, value):
        """ SetRefTriggerDelay(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRefTriggerMinimumQuietTime(self, channel, value):
        """ SetRefTriggerMinimumQuietTime(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRefTriggerOspDelayEnabled(self, channel, value):
        """ SetRefTriggerOspDelayEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetRefTriggerPretriggerSamples(self, channel, value):
        """ SetRefTriggerPretriggerSamples(self: niRFSA, channel: str, value: Int64) -> int """
        pass

    def SetRefTriggerType(self, channel, value):
        """ SetRefTriggerType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetResolutionBandwidth(self, channel, value):
        """ SetResolutionBandwidth(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetResolutionBandwidthType(self, channel, value):
        """ SetResolutionBandwidthType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetRfAttenuationIndex(self, channel, value):
        """ SetRfAttenuationIndex(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetRfAttenuationStepSize(self, channel, value):
        """ SetRfAttenuationStepSize(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRfAttenuationTable(self, channel, value):
        """ SetRfAttenuationTable(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetRfHighPassFiltering(self, channel, value):
        """ SetRfHighPassFiltering(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRfPreampEnabled(self, channel, value):
        """ SetRfPreampEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetRfPreselectorCalToneFrequency(self, channel, value):
        """ SetRfPreselectorCalToneFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetRfPreselectorCalToneMode(self, channel, value):
        """ SetRfPreselectorCalToneMode(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetRfPreselectorFilter(self, channel, value):
        """ SetRfPreselectorFilter(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetSession(self, propertyId, *__args):
        """
        SetSession(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str, val: IntPtr) -> int
        SetSession(self: niRFSA, propertyId: niRFSAProperties, val: IntPtr) -> int
        """
        pass

    def SetSignalConditioningEnabled(self, channel, value):
        """ SetSignalConditioningEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetSmoothSpectrumEnabled(self, channel, value):
        """ SetSmoothSpectrumEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetSpectrumAveragingMode(self, channel, value):
        """ SetSpectrumAveragingMode(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetSpectrumCenterFrequency(self, channel, value):
        """ SetSpectrumCenterFrequency(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetSpectrumNumberOfAverages(self, channel, value):
        """ SetSpectrumNumberOfAverages(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetSpectrumOspSamplingRatio(self, channel, value):
        """ SetSpectrumOspSamplingRatio(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetSpectrumSpan(self, channel, value):
        """ SetSpectrumSpan(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetStartToRefTriggerHoldoff(self, channel, value):
        """ SetStartToRefTriggerHoldoff(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetStartTriggerDelay(self, channel, value):
        """ SetStartTriggerDelay(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetStartTriggerType(self, channel, value):
        """ SetStartTriggerType(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetStepGainEnabled(self, channel, value):
        """ SetStepGainEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetString(self, propertyId, *__args):
        """
        SetString(self: niRFSA, propertyId: niRFSAProperties, repeatedCapabilityOrChannel: str, val: str) -> int
        SetString(self: niRFSA, propertyId: niRFSAProperties, val: str) -> int
        """
        pass

    def SetSubspanOverlap(self, channel, value):
        """ SetSubspanOverlap(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetSyncAdvanceTriggerDistLine(self, channel, value):
        """ SetSyncAdvanceTriggerDistLine(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetSyncAdvanceTriggerMaster(self, channel, value):
        """ SetSyncAdvanceTriggerMaster(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetSyncRefTriggerDelayEnabled(self, channel, value):
        """ SetSyncRefTriggerDelayEnabled(self: niRFSA, channel: str, value: int) -> int """
        pass

    def SetSyncRefTriggerDistLine(self, channel, value):
        """ SetSyncRefTriggerDistLine(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetSyncRefTriggerMaster(self, channel, value):
        """ SetSyncRefTriggerMaster(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetSyncSampleClockDistLine(self, channel, value):
        """ SetSyncSampleClockDistLine(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetSyncSampleClockMaster(self, channel, value):
        """ SetSyncSampleClockMaster(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetSyncStartTriggerDistLine(self, channel, value):
        """ SetSyncStartTriggerDistLine(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetSyncStartTriggerMaster(self, channel, value):
        """ SetSyncStartTriggerMaster(self: niRFSA, channel: str, value: bool) -> int """
        pass

    def SetTemperatureReadInterval(self, channel, value):
        """ SetTemperatureReadInterval(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetTimerEventInterval(self, channel, value):
        """ SetTimerEventInterval(self: niRFSA, channel: str, value: float) -> int """
        pass

    def SetTimerStartSource(self, channel, value):
        """ SetTimerStartSource(self: niRFSA, channel: str, value: str) -> int """
        pass

    def SetUserData(self, identifier, bufferSize, data):
        """ SetUserData(self: niRFSA, identifier: str, bufferSize: int, data: Array[Byte]) -> int """
        pass

    def UnlockSession(self, callerHasLock):
        """ UnlockSession(self: niRFSA, callerHasLock: bool) -> (int, bool) """
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
        __new__(cls: type, Resource_Name: str, ID_Query: bool, Reset: bool)
        __new__(cls: type, Resource_Name: str, ID_Query: bool, Reset: bool, Option_String: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: niRFSA) -> HandleRef

"""



class niRFSAConstants(object):
    """ niRFSAConstants() """
    AC = 3001
    AdvanceTrigger = 1102
    ArmRefTrigger = 1103
    Blackman = 505
    BlackmanHarris = 503
    Bypass = 1403
    CalClkOutStr = 'ClkOut'
    CalIn = 2002
    CalToneCombGenerator = 2705
    CalToneDisabled = 2700
    CalToneHighbandIf = 2703
    CalToneHighbandRf = 2702
    CalToneLowbandRf = 2701
    CalToneLowbandRfWithoutAlc = 2704
    ClkInStr = 'ClkIn'
    ClkOutStr = 'ClkOut'
    CurrentReadPosition = 704
    Dbm = 200
    Dbmv = 202
    Dbuv = 203
    DC = 3002
    Differential = 2100
    DigitalEdge = 601
    DigitalLevel = 602
    Disabled = 1900
    DoneEvent = 1204
    DoNotExportStr = ''
    DownconverterCombinedResponse = 2802
    DownconverterIfResponse = 2800
    DownconverterLo2OutStr = 'downconverterlo2out'
    DownconverterRfResponse = 2801
    Enabled = 1901
    EndOfRecordEvent = 1203
    EndOfRecordEventStr = 'EndOfRecordEvent'
    EndOrRecordEventStr = 'EndOfRecordEvent'
    ExactBlackman = 504
    ExtAlignmentAbort = 3100
    ExtAlignmentCommit = 3101
    ExtAllignmentPreselector = 1
    ExtCalAbort = 1500
    ExtCalCommit = 1501
    ExtCalDefault = 1800
    ExtCalGainReferenceCalibration = 1604
    ExtCalIfAttenuationCalibration = 1600
    ExtCalIfAttenuationTableAcpr = 2901
    ExtCalIfAttenuationTableStandard = 2900
    ExtCalIfFilterPath1 = 2100
    ExtCalIfFilterPath10 = 2109
    ExtCalIfFilterPath11 = 2110
    ExtCalIfFilterPath2 = 2101
    ExtCalIfFilterPath3 = 2102
    ExtCalIfFilterPath4 = 2103
    ExtCalIfFilterPath5 = 2104
    ExtCalIfFilterPath6 = 2105
    ExtCalIfFilterPath7 = 2106
    ExtCalIfFilterPath8 = 2107
    ExtCalIfFilterPath9 = 2108
    ExtCalIfResponseCalibration = 1601
    ExtCalLo1 = 2200
    ExtCalLo2 = 2201
    ExtCalLo3 = 2202
    ExtCalLoExportCalibration = 1603
    ExtCalLoPath1 = 2300
    ExtCalLoPath2 = 2301
    ExtCalLoPath3 = 2302
    ExtCalLoPath4 = 2303
    ExtCalLoPath5 = 2304
    ExtCalMechanicalAttenuatorDisabled = 1801
    ExtCalRefLevelCalibration = 1602
    ExtCalRfBand1 = 1700
    ExtCalRfBand2 = 1701
    ExtCalRfBand3 = 1702
    ExtCalRfBand4 = 1703
    ExtCalRfLowbandSignalConditioningPath1 = 3700
    ExtCalRfLowbandSignalConditioningPath2 = 3701
    ExtCalRfLowbandSignalConditioningPath3 = 3702
    ExtCalRfLowbandSignalConditioningPath4 = 3703
    ExtCalRfLowbandSignalConditioningPath5 = 3704
    FallingEdge = 901
    FallingSlope = 1001
    FirstPretriggerSample = 703
    FirstSample = 701
    FlatTop = 506
    FsuPpm = 2000
    FsuSecondsAfterIo = 2002
    FsuSecondsAfterLock = 2001
    Gaussian = 510
    Hamming = 502
    Hanning = 501
    High = 802
    IfCondOutStr = 'IFCondRefOut'
    IOnly = 2003
    Iq = 100
    IqAnalogEdge = 605
    IqIn = 2001
    IqPowerEdge = 603
    KaiserBessel = 511
    LogAveraging = 406
    LoInjectionHighSide = 1300
    LoInjectionLowSide = 1301
    LoInStr = 'LO_In'
    LoRefClkStr = 'LORefClk'
    Low = 800
    LowSideLobe = 509
    LOYigMainCoilDriveFast = 2401
    LOYigMainCoilDriveNormal = 2400
    Medium = 801
    MinHoldAveraging = 404
    MostRecentSample = 700
    Narrow = 800
    NiextCalIfAttenuationTableAcpr = 2901
    NiextCalIfAttenuationTableStandard = 2900
    NoAveraging = 400
    None = 600
    NoneStr = 'None'
    NotchFilterDisabled = 3400
    NotchFilterEnabled = 3402
    NotchFilterEnabledWhenInSignal = 3401
    OnboardClockStr = 'OnboardClock'
    OnBoardStr = 'Onboard'
    PeakHoldAveraging = 403
    Pfi0Str = 'PFI0'
    Pfi1Str = 'PFI1'
    PreselectorDisabled = 2600
    PreselectorEnabled = 2602
    PreselectorEnabledWhenInSignalPath = 2601
    PxiClk10Str = 'PXI_Clk10'
    PxiClkStr = 'PXI_Clk'
    PxiStarStr = 'PXI_STAR'
    PxiTrig0Str = 'PXI_Trig0'
    PxiTrig1Str = 'PXI_Trig1'
    PxiTrig2Str = 'PXI_Trig2'
    PxiTrig3Str = 'PXI_Trig3'
    PxiTrig4Str = 'PXI_Trig4'
    PxiTrig5Str = 'PXI_Trig5'
    PxiTrig6Str = 'PXI_Trig6'
    PxiTrig7Str = 'PXI_Trig7'
    Rbw3db = 300
    Rbw6db = 301
    RbwBinWidth = 302
    RbwEnbw = 303
    ReadyForAdvanceEvent = 1202
    ReadyForRefEvent = 1201
    ReadyForStartEvent = 1200
    RefClock = 1205
    ReferenceTriggerStr = 'ReferenceTrigger'
    RefInStr = 'RefIn'
    RefOut2Str = 'RefOut2'
    RefOutStr = 'RefOut'
    RefTrigger = 702
    RfIn = 2000
    RFPreampAutomatic = 2503
    RFPreampDisabled = 2500
    RFPreampEnabled = 2502
    RFPreampEnabledWhenInSignalPath = 2501
    RfPreselectorPath1 = 3301
    RfPreselectorPath10 = 3310
    RfPreselectorPath11 = 3311
    RfPreselectorPath12 = 3312
    RfPreselectorPath13 = 3313
    RfPreselectorPath14 = 3314
    RfPreselectorPath15 = 3315
    RfPreselectorPath16 = 3316
    RfPreselectorPath2 = 3302
    RfPreselectorPath3 = 3303
    RfPreselectorPath4 = 3304
    RfPreselectorPath5 = 3305
    RfPreselectorPath6 = 3306
    RfPreselectorPath7 = 3307
    RfPreselectorPath8 = 3308
    RfPreselectorPath9 = 3309
    RfPreselectorPathExternalFilter = 3317
    RfPreselectorPathNone = 3300
    RisingEdge = 900
    RisingSlope = 1000
    RmsAveraging = 401
    Rtsi0Str = 'PXI_Trig0'
    Rtsi1Str = 'PXI_Trig1'
    Rtsi2Str = 'PXI_Trig2'
    Rtsi3Str = 'PXI_Trig3'
    Rtsi4Str = 'PXI_Trig4'
    Rtsi5Str = 'PXI_Trig5'
    Rtsi6Str = 'PXI_Trig6'
    Rtsi7Str = 'PXI_Trig7'
    ScalarAveraging = 405
    SelfCalAmplitudeAccuracy = 32
    SelfCalDigitizerSelfCal = 8
    SelfCalGainReference = 2
    SelfCalIfFlatness = 4
    SelfCalImageSuppresion = 128
    SelfCalLoSelfCal = 16
    SelfCalOmitNone = 0
    SelfCalPreselectorAlignment = 1
    SelfCalPreselectorAllignment = 1
    SelfCalResidualLoPower = 64
    SignalCondioningBypassed = 3601
    SignalCondioningEnabled = 3600
    SingleEnded = 2101
    SoftwareEdge = 604
    Spectrum = 101
    StartTrigger = 1100
    StartTriggerStr = 'StartTrigger'
    StepGainDisabled = 3200
    StepGainEnabled = 3201
    SyncAdvanceTriggerStr = 'Sync_Advance'
    SyncRefTriggerStr = 'Sync_Ref'
    SyncStartTriggerStr = 'Sync_Start'
    TimerEventStr = 'TimerEvent'
    Uniform = 500
    User = 1206
    VectorAveraging = 402
    Volts = 204
    VoltsSquared = 201
    VsaCombinedResponse = 2804
    VsaIfResponse = 2803
    Watts = 205
    Wide = 802
    _1875MhzNarrow = 1401
    _1875MhzWide = 1400
    _4TermBlackmanHarris = 507
    _53Mhz = 1402
    _7TermBlackmanHarris = 508


class niRFSAProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum niRFSAProperties, values: AcquisitionType (1150001), ActiveConfigurationList (1150092), ActiveConfigurationListStep (1150093), AdvanceTriggerTerminalName (1150124), AdvanceTriggerType (1150036), AllowMoreRecordsThanMemory (1150154), ArmRefTriggerType (1150039), Attenuation (1150005), Cache (1050004), CalDigitizerId (1150226), CalibrationCorrection100mhzFilter (1150223), CalibrationCorrection300KhzFilter (1150147), CalibrationCorrection320mhzFilter (1150224), CalibrationCorrection5MhzFilter (1150148), CalibrationCorrection765mhzFilter (1150225), CalibrationCorrectionThroughFilter (1150146), CalIfAttenuationIndex (1150109), CalIfAttenuationTableSelection (1150141), CalIfAttenuationTableSize (1150216), CalIfFilterSelection (1150112), CalLo1Attenuation (1150114), CalLo2Attenuation (1150115), CalLo3Attenuation (1150116), CalLoPathSelection (1150113), CalRfElectronicAttenuationIndex (1150110), CalRfLowbandSignalConditioningPathSelection (1150215), CalRfMechanicalAttenuationIndex (1150111), CalRfPathSelection (1150083), CalToneFrequency (1150140), CalToneMode (1150139), CalTonePowerReferredToRfIn (1150174), CalToneStepAttenuation (1150168), CenterFrequency (1150002), ChannelCount (1050203), ChannelCoupling (1150149), ConfigurationListStepInProgress (1150126), ConfigurationListStepTriggerSource (1150095), ContiguousMultiRecord (1150172), DataTransferBlockSize (1150105), DataTransferMaximumBandwidth (1150104), DdcRefTriggerOverride (1150164), DecimationDelay (1150191), DeviceConfigurationTemperature (1150159), DeviceInstantaneousBandwidth (1150125), DeviceTemperature (1150051), DigitalEdgeAdvanceTriggerSource (1150037), DigitalEdgeArmRefTriggerSource (1150040), DigitalEdgeRefTriggerEdge (1150030), DigitalEdgeRefTriggerSource (1150029), DigitalEdgeStartTriggerEdge (1150026), DigitalEdgeStartTriggerSource (1150025), DigitalIfEqualizationEnabled (1150048), DigitizerDitherEnabled (1150080), DigitizerSampleClockRate (1150228), DigitizerSampleClockTimebaseRate (1150022), DigitizerSampleClockTimebaseSource (1150021), DigitizerTemperature (1150090), DigitizerVerticalRange (1150070), DoneEventTerminalName (1150121), DownconverterCenterFrequency (1150082), DownconverterGain (1150065), DownconverterLoopBandwidth (1150067), DownconvertorCalToneFrequency (1150140), DownconvertorCalToneMode (1150139), DownconvertorFrequencyOffset (1150203), DownconvertorPreselectorEnabled (1150132), DriverSetup (1050007), EnableFractionalResampling (1150071), EndOfRecordEventTerminalName (1150120), ExportedAdvanceTriggerOutputTerminal (1150038), ExportedDigitizerSampleClockOutputTerminal (1150229), ExportedDoneEventOutputTerminal (1150054), ExportedEndOfRecordEventOutputTerminal (1150044), ExportedReadyForAdvanceEventOutputTerminal (1150042), ExportedReadyForRefEventOutputTerminal (1150043), ExportedReadyForStartEventOutputTerminal (1150041), ExportedRefClockOutputTerminal (1150072), ExportedRefTriggerOutputTerminal (1150032), ExportedStartTriggerOutputTerminal (1150027), ExternalGain (1150094), FetchOffset (1150046), FetchRelativeTo (1150045), FftSize (1150050), FftWidth (1150169), FftWindowShapeFactor (1150206), FftWindowSize (1150049), FftWindowType (1150017), FpgaBitFilePath (1150221), FpgaTargetName (1150233), FrequencySettling (1150088), FrequencySettlingUnits (1150087), GroupCapabilities (1050401), If1AttenValue (1150078), If2AttenValue (1150079), IfAttenuation (1150074), IfConditioningDownConversionEnabled (1150161), IfConditioningTemperature (1150210), IfFilter (1150075), IfFilterBandwidth (1150205), IfOutputFrequency (1150086), IfOutputPowerLevel (1150130), IfOutputPowerLevelOffset (1150131), InputIsolationEnabled (1150170), InputPort (1150180), InstrumentFirmwareRevision (1050510), InstrumentManufacturer (1050511), InstrumentModel (1050512), InterchangeCheck (1050021), IoResourceDescriptor (1050304), IqAnalogEdgeRefTrigger (1150092), IqAnalogEdgeRefTriggerHysteresis (1150195), IqAnalogEdgeRefTriggerLevel (1150194), IqAnalogEdgeRefTriggerSlope (1150193), IqAnalogEdgeRefTriggerSource (1150192), IqCarrierFrequency (1150059), IqInPortCarrierrFrequency (1150181), IqInPortTemperature (1150204), IqInportTerminalConfiguration (1150182), IqInPortVerticalRange (1150183), IqPowerEdgeRefTriggerLevel (1150056), IqPowerEdgeRefTriggerSlope (1150057), IqPowerEdgeRefTriggerSource (1150055), IqRate (1150007), Lo2ExportEnabled (1150235), LoExportEnabled (1150134), LoFrequency (1150068), LoFrequencyStepSize (1150188), LogicalName (1050305), LoInjectionSide (1150069), LoInPower (1150186), LoPllFractionalModeEnabled (1150187), LoSource (1150162), LoTemperature (1150089), LowFrequencyByPassEnabled (1150207), LoYigMainCoilDrive (1150135), MaxDeviceInstantaneousBandwidth (1150236), MaxIQRate (1150237), MechanicalAttenuation (1150128), MechanicalAttenuatorEnabled (1150081), MemorySize (1150085), MinimumAcpr (1150142), MinimumReconfigTime (1150165), MixerLevel (1150006), MixerLevelOffset (1150127), ModuleRevision (1150091), NoiseSourcePowerEnabled (1150222), NotchFilterEnabled (1150167), NumberOfRecords (1150011), NumberOfRecordsIsFinite (1150010), NumberOfSamples (1150009), NumberOfSamplesIsFinite (1150008), NumberOfSpectralLines (1150018), OspDataScalingFactor (1150151), P2pEnabled (1150097), P2pEndpointOverflow (1150103), P2pEndpointSize (1150102), P2pFifoEndpointCount (1150098), P2pMostSamplesAvailableInEndpoint (1150101), P2pOnboardMemoryEnabled (1150107), P2pSamplesAvailableInEndpoint (1150100), P2pSamplesTransferred (1150099), PhaseOffset (1150106), PowerSpectrumUnits (1150012), PreselectorEnabled (1150132), PreselectorPresent (1150136), PreselectorTuningDacValue5665 (1150158), PxiChassisClk10Source (1150023), QueryInstrumentStatus (1050003), RangeCheck (1050002), ReadyForAdvanceEventTerminalName (1150118), ReadyForRefEventTerminalName (1150119), ReadyForStartEventTerminalName (1150117), ReconfigurationTriggerSource (1150095), RecordCoercions (1050006), RecordsDone (1150047), RefClockRate (1150020), RefClockSource (1150019), ReferenceLevel (1150004), RefToRefTriggerHoldoff (1150034), RefTriggerDelay (1150060), RefTriggerMinimumQuietTime (1150058), RefTriggerOspDelayEnabled (1150196), RefTriggerPretriggerSamples (1150035), RefTriggerTerminalName (1150123), RefTriggerType (1150028), ResolutionBandwidth (1150013), ResolutionBandwidthType (1150014), RfAttenuationIndex (1150076), RfAttenuationStepSize (1150155), RfAttenuationTable (1150077), RfConditioningTemperature (1150211), RfHighPassFiltering (1150220), RfPreampEnabled (1150129), RfPreampPresent (1150137), RfPreselectorCalToneFrequency (1150209), RfPreselectorCalToneMode (1150208), RfPreselectorFilter (1150166), SerialNumber (1150053), SignalConditioningEnabled (1150160), Simulate (1050005), SmoothSpectrumEnabled (1150219), SpecificDriverClassSpecMajorVersion (1050515), SpecificDriverClassSpecMinorVersion (1050516), SpecificDriverDescription (1050514), SpecificDriverPrefix (1050302), SpecificDriverRevision (1050551), SpecificDriverVendor (1050513), SpectrumAveragingMode (1150016), SpectrumCenterFrequency (1150002), SpectrumNumberOfAverages (1150015), SpectrumOspSamplingRatio (1150144), SpectrumSpan (1150003), StartToRefTriggerHoldoff (1150033), StartTriggerDelay (1150175), StartTriggerTerminalName (1150122), StartTriggerType (1150024), StepGainEnabled (1150157), SubspanOverlap (1150234), SupportedInstrumentModels (1050327), SyncAdvanceTriggerDistLine (1150185), SyncAdvanceTriggerMaster (1150184), SyncRefTriggerDelayEnabled (1150189), SyncRefTriggerDistLine (1150179), SyncRefTriggerMaster (1150178), SyncSampleClockDistLine (1150218), SyncSampleClockMaster (1150217), SyncStartTriggerDistLine (1150177), SyncStartTriggerMaster (1150176), TemperatureReadInterval (1150061), TimerEventInterval (1150096), TimerStartSource (1150173) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AcquisitionType = None
    ActiveConfigurationList = None
    ActiveConfigurationListStep = None
    AdvanceTriggerTerminalName = None
    AdvanceTriggerType = None
    AllowMoreRecordsThanMemory = None
    ArmRefTriggerType = None
    Attenuation = None
    Cache = None
    CalDigitizerId = None
    CalibrationCorrection100mhzFilter = None
    CalibrationCorrection300KhzFilter = None
    CalibrationCorrection320mhzFilter = None
    CalibrationCorrection5MhzFilter = None
    CalibrationCorrection765mhzFilter = None
    CalibrationCorrectionThroughFilter = None
    CalIfAttenuationIndex = None
    CalIfAttenuationTableSelection = None
    CalIfAttenuationTableSize = None
    CalIfFilterSelection = None
    CalLo1Attenuation = None
    CalLo2Attenuation = None
    CalLo3Attenuation = None
    CalLoPathSelection = None
    CalRfElectronicAttenuationIndex = None
    CalRfLowbandSignalConditioningPathSelection = None
    CalRfMechanicalAttenuationIndex = None
    CalRfPathSelection = None
    CalToneFrequency = None
    CalToneMode = None
    CalTonePowerReferredToRfIn = None
    CalToneStepAttenuation = None
    CenterFrequency = None
    ChannelCount = None
    ChannelCoupling = None
    ConfigurationListStepInProgress = None
    ConfigurationListStepTriggerSource = None
    ContiguousMultiRecord = None
    DataTransferBlockSize = None
    DataTransferMaximumBandwidth = None
    DdcRefTriggerOverride = None
    DecimationDelay = None
    DeviceConfigurationTemperature = None
    DeviceInstantaneousBandwidth = None
    DeviceTemperature = None
    DigitalEdgeAdvanceTriggerSource = None
    DigitalEdgeArmRefTriggerSource = None
    DigitalEdgeRefTriggerEdge = None
    DigitalEdgeRefTriggerSource = None
    DigitalEdgeStartTriggerEdge = None
    DigitalEdgeStartTriggerSource = None
    DigitalIfEqualizationEnabled = None
    DigitizerDitherEnabled = None
    DigitizerSampleClockRate = None
    DigitizerSampleClockTimebaseRate = None
    DigitizerSampleClockTimebaseSource = None
    DigitizerTemperature = None
    DigitizerVerticalRange = None
    DoneEventTerminalName = None
    DownconverterCenterFrequency = None
    DownconverterGain = None
    DownconverterLoopBandwidth = None
    DownconvertorCalToneFrequency = None
    DownconvertorCalToneMode = None
    DownconvertorFrequencyOffset = None
    DownconvertorPreselectorEnabled = None
    DriverSetup = None
    EnableFractionalResampling = None
    EndOfRecordEventTerminalName = None
    ExportedAdvanceTriggerOutputTerminal = None
    ExportedDigitizerSampleClockOutputTerminal = None
    ExportedDoneEventOutputTerminal = None
    ExportedEndOfRecordEventOutputTerminal = None
    ExportedReadyForAdvanceEventOutputTerminal = None
    ExportedReadyForRefEventOutputTerminal = None
    ExportedReadyForStartEventOutputTerminal = None
    ExportedRefClockOutputTerminal = None
    ExportedRefTriggerOutputTerminal = None
    ExportedStartTriggerOutputTerminal = None
    ExternalGain = None
    FetchOffset = None
    FetchRelativeTo = None
    FftSize = None
    FftWidth = None
    FftWindowShapeFactor = None
    FftWindowSize = None
    FftWindowType = None
    FpgaBitFilePath = None
    FpgaTargetName = None
    FrequencySettling = None
    FrequencySettlingUnits = None
    GroupCapabilities = None
    If1AttenValue = None
    If2AttenValue = None
    IfAttenuation = None
    IfConditioningDownConversionEnabled = None
    IfConditioningTemperature = None
    IfFilter = None
    IfFilterBandwidth = None
    IfOutputFrequency = None
    IfOutputPowerLevel = None
    IfOutputPowerLevelOffset = None
    InputIsolationEnabled = None
    InputPort = None
    InstrumentFirmwareRevision = None
    InstrumentManufacturer = None
    InstrumentModel = None
    InterchangeCheck = None
    IoResourceDescriptor = None
    IqAnalogEdgeRefTrigger = None
    IqAnalogEdgeRefTriggerHysteresis = None
    IqAnalogEdgeRefTriggerLevel = None
    IqAnalogEdgeRefTriggerSlope = None
    IqAnalogEdgeRefTriggerSource = None
    IqCarrierFrequency = None
    IqInPortCarrierrFrequency = None
    IqInPortTemperature = None
    IqInportTerminalConfiguration = None
    IqInPortVerticalRange = None
    IqPowerEdgeRefTriggerLevel = None
    IqPowerEdgeRefTriggerSlope = None
    IqPowerEdgeRefTriggerSource = None
    IqRate = None
    Lo2ExportEnabled = None
    LoExportEnabled = None
    LoFrequency = None
    LoFrequencyStepSize = None
    LogicalName = None
    LoInjectionSide = None
    LoInPower = None
    LoPllFractionalModeEnabled = None
    LoSource = None
    LoTemperature = None
    LowFrequencyByPassEnabled = None
    LoYigMainCoilDrive = None
    MaxDeviceInstantaneousBandwidth = None
    MaxIQRate = None
    MechanicalAttenuation = None
    MechanicalAttenuatorEnabled = None
    MemorySize = None
    MinimumAcpr = None
    MinimumReconfigTime = None
    MixerLevel = None
    MixerLevelOffset = None
    ModuleRevision = None
    NoiseSourcePowerEnabled = None
    NotchFilterEnabled = None
    NumberOfRecords = None
    NumberOfRecordsIsFinite = None
    NumberOfSamples = None
    NumberOfSamplesIsFinite = None
    NumberOfSpectralLines = None
    OspDataScalingFactor = None
    P2pEnabled = None
    P2pEndpointOverflow = None
    P2pEndpointSize = None
    P2pFifoEndpointCount = None
    P2pMostSamplesAvailableInEndpoint = None
    P2pOnboardMemoryEnabled = None
    P2pSamplesAvailableInEndpoint = None
    P2pSamplesTransferred = None
    PhaseOffset = None
    PowerSpectrumUnits = None
    PreselectorEnabled = None
    PreselectorPresent = None
    PreselectorTuningDacValue5665 = None
    PxiChassisClk10Source = None
    QueryInstrumentStatus = None
    RangeCheck = None
    ReadyForAdvanceEventTerminalName = None
    ReadyForRefEventTerminalName = None
    ReadyForStartEventTerminalName = None
    ReconfigurationTriggerSource = None
    RecordCoercions = None
    RecordsDone = None
    RefClockRate = None
    RefClockSource = None
    ReferenceLevel = None
    RefToRefTriggerHoldoff = None
    RefTriggerDelay = None
    RefTriggerMinimumQuietTime = None
    RefTriggerOspDelayEnabled = None
    RefTriggerPretriggerSamples = None
    RefTriggerTerminalName = None
    RefTriggerType = None
    ResolutionBandwidth = None
    ResolutionBandwidthType = None
    RfAttenuationIndex = None
    RfAttenuationStepSize = None
    RfAttenuationTable = None
    RfConditioningTemperature = None
    RfHighPassFiltering = None
    RfPreampEnabled = None
    RfPreampPresent = None
    RfPreselectorCalToneFrequency = None
    RfPreselectorCalToneMode = None
    RfPreselectorFilter = None
    SerialNumber = None
    SignalConditioningEnabled = None
    Simulate = None
    SmoothSpectrumEnabled = None
    SpecificDriverClassSpecMajorVersion = None
    SpecificDriverClassSpecMinorVersion = None
    SpecificDriverDescription = None
    SpecificDriverPrefix = None
    SpecificDriverRevision = None
    SpecificDriverVendor = None
    SpectrumAveragingMode = None
    SpectrumCenterFrequency = None
    SpectrumNumberOfAverages = None
    SpectrumOspSamplingRatio = None
    SpectrumSpan = None
    StartToRefTriggerHoldoff = None
    StartTriggerDelay = None
    StartTriggerTerminalName = None
    StartTriggerType = None
    StepGainEnabled = None
    SubspanOverlap = None
    SupportedInstrumentModels = None
    SyncAdvanceTriggerDistLine = None
    SyncAdvanceTriggerMaster = None
    SyncRefTriggerDelayEnabled = None
    SyncRefTriggerDistLine = None
    SyncRefTriggerMaster = None
    SyncSampleClockDistLine = None
    SyncSampleClockMaster = None
    SyncStartTriggerDistLine = None
    SyncStartTriggerMaster = None
    TemperatureReadInterval = None
    TimerEventInterval = None
    TimerStartSource = None
    value__ = None


class niRFSA_coefficientInfo(object):
    # no doc
    gain = None
    offset = None
    reserved1 = None
    reserved2 = None


class niRFSA_spectrumInfo(object):
    # no doc
    frequencyIncrement = None
    initialFrequency = None
    numberOfSpectralLines = None
    reserved1 = None
    reserved2 = None
    reserved3 = None
    reserved4 = None
    reserved5 = None


class niRFSA_wfmInfo(object):
    # no doc
    absoluteInitialX = None
    actualSamples = None
    gain = None
    offset = None
    relativeInitialX = None
    reserved1 = None
    reserved2 = None
    xIncrement = None


class niRFSG(object, IDisposable):
    """
    niRFSG(Resource_Name: str, ID_Query: bool, Reset: bool)
    niRFSG(Resource_Name: str, ID_Query: bool, Reset: bool, Option_String: str)
    """
    def Abort(self):
        """ Abort(self: niRFSG) -> int """
        pass

    def AllocateArbWaveform(self, Name, Size_In_Samples):
        """ AllocateArbWaveform(self: niRFSG, Name: str, Size_In_Samples: int) -> int """
        pass

    def ChangeExternalCalibrationPassword(self, Old_Password, New_Password):
        """ ChangeExternalCalibrationPassword(self: niRFSG, Old_Password: str, New_Password: str) -> int """
        pass

    def CheckGenerationStatus(self, Is_Done):
        """ CheckGenerationStatus(self: niRFSG) -> (int, bool) """
        pass

    def CheckIfConfigurationListExists(self, listName, listExists):
        """ CheckIfConfigurationListExists(self: niRFSG, listName: str) -> (int, bool) """
        pass

    def CheckIfScriptExists(self, scriptName, scriptExists):
        """ CheckIfScriptExists(self: niRFSG, scriptName: str) -> (int, bool) """
        pass

    def CheckIfWaveformExists(self, waveformName, waveformExists):
        """ CheckIfWaveformExists(self: niRFSG, waveformName: str) -> (int, bool) """
        pass

    def ClearAllArbWaveforms(self):
        """ ClearAllArbWaveforms(self: niRFSG) -> int """
        pass

    def ClearArbWaveform(self, Name):
        """ ClearArbWaveform(self: niRFSG, Name: str) -> int """
        pass

    def close(self):
        """ close(self: niRFSG) -> int """
        pass

    def Commit(self):
        """ Commit(self: niRFSG) -> int """
        pass

    def ConfigureDigitalEdgeConfigurationListStepTrigger(self, Source, Edge):
        """ ConfigureDigitalEdgeConfigurationListStepTrigger(self: niRFSG, Source: str, Edge: int) -> int """
        pass

    def ConfigureDigitalEdgeScriptTrigger(self, Trigger_Identifier, Source, Edge):
        """ ConfigureDigitalEdgeScriptTrigger(self: niRFSG, Trigger_Identifier: str, Source: str, Edge: int) -> int """
        pass

    def ConfigureDigitalEdgeStartTrigger(self, Source, Edge):
        """ ConfigureDigitalEdgeStartTrigger(self: niRFSG, Source: str, Edge: int) -> int """
        pass

    def ConfigureDigitalLevelScriptTrigger(self, Trigger_Identifier, Source, Level):
        """ ConfigureDigitalLevelScriptTrigger(self: niRFSG, Trigger_Identifier: str, Source: str, Level: int) -> int """
        pass

    def ConfigureDigitalModulationUserDefinedWaveform(self, Number_Of_Samples, User_Defined_Waveform):
        """ ConfigureDigitalModulationUserDefinedWaveform(self: niRFSG, Number_Of_Samples: int, User_Defined_Waveform: Array[SByte]) -> int """
        pass

    def ConfigureGenerationMode(self, Generation_Mode):
        """ ConfigureGenerationMode(self: niRFSG, Generation_Mode: int) -> int """
        pass

    def ConfigureIQEnabled(self, IQ_Enabled):
        """ ConfigureIQEnabled(self: niRFSG, IQ_Enabled: bool) -> int """
        pass

    def ConfigureOutputEnabled(self, Output_Enabled):
        """ ConfigureOutputEnabled(self: niRFSG, Output_Enabled: bool) -> int """
        pass

    def ConfigureP2PEndpointFullnessStartTrigger(self, P2P_Endpoint_Fullness_Level):
        """ ConfigureP2PEndpointFullnessStartTrigger(self: niRFSG, P2P_Endpoint_Fullness_Level: Int64) -> int """
        pass

    def ConfigurePowerLevelType(self, Power_Level_Type):
        """ ConfigurePowerLevelType(self: niRFSG, Power_Level_Type: int) -> int """
        pass

    def ConfigurePXIChassisClk10(self, PXI_Clk_10_Source):
        """ ConfigurePXIChassisClk10(self: niRFSG, PXI_Clk_10_Source: str) -> int """
        pass

    def ConfigureRefClock(self, Ref_Clock_Source, Ref_Clock_Rate):
        """ ConfigureRefClock(self: niRFSG, Ref_Clock_Source: str, Ref_Clock_Rate: float) -> int """
        pass

    def ConfigureRF(self, Frequency, Power_Level):
        """ ConfigureRF(self: niRFSG, Frequency: float, Power_Level: float) -> int """
        pass

    def ConfigureSignalBandwidth(self, Signal_Bandwidth):
        """ ConfigureSignalBandwidth(self: niRFSG, Signal_Bandwidth: float) -> int """
        pass

    def ConfigureSoftwareScriptTrigger(self, Trigger_Identifier):
        """ ConfigureSoftwareScriptTrigger(self: niRFSG, Trigger_Identifier: str) -> int """
        pass

    def ConfigureSoftwareStartTrigger(self):
        """ ConfigureSoftwareStartTrigger(self: niRFSG) -> int """
        pass

    def CreateConfigurationList(self, List_Name, Number_Of_Attributes, Configuration_List_Attributes, Set_As_Active_List):
        """ CreateConfigurationList(self: niRFSG, List_Name: str, Number_Of_Attributes: int, Configuration_List_Attributes: Array[niRFSGProperties], Set_As_Active_List: bool) -> int """
        pass

    def CreateConfigurationListStep(self, Set_As_Active_Step):
        """ CreateConfigurationListStep(self: niRFSG, Set_As_Active_Step: bool) -> int """
        pass

    def DeleteConfigurationList(self, List_Name):
        """ DeleteConfigurationList(self: niRFSG, List_Name: str) -> int """
        pass

    def Disable(self):
        """ Disable(self: niRFSG) -> int """
        pass

    def DisableConfigurationListStepTrigger(self):
        """ DisableConfigurationListStepTrigger(self: niRFSG) -> int """
        pass

    def DisableScriptTrigger(self, Trigger_Identifier):
        """ DisableScriptTrigger(self: niRFSG, Trigger_Identifier: str) -> int """
        pass

    def DisableStartTrigger(self):
        """ DisableStartTrigger(self: niRFSG) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: niRFSG) """
        pass

    @staticmethod
    def ErrorMessage(*__args):
        """
        ErrorMessage(handle: HandleRef, code: int, msg: StringBuilder) -> int
        ErrorMessage(self: niRFSG, code: int, msg: StringBuilder) -> int
        """
        pass

    def error_query(self, Error_Code, Error_Message):
        """ error_query(self: niRFSG, Error_Message: StringBuilder) -> (int, int) """
        pass

    def ExportSignal(self, Signal, Signal_Identifier, Output_Terminal):
        """ ExportSignal(self: niRFSG, Signal: int, Signal_Identifier: str, Output_Terminal: str) -> int """
        pass

    def GetActiveConfigurationList(self, channel, value):
        """ GetActiveConfigurationList(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetActiveConfigurationListStep(self, channel, value):
        """ GetActiveConfigurationListStep(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetAllowOutOfSpecificationUserSettings(self, channel, value):
        """ GetAllowOutOfSpecificationUserSettings(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetAnalogModulationFmDeviation(self, channel, value):
        """ GetAnalogModulationFmDeviation(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetAnalogModulationPmDeviation(self, channel, value):
        """ GetAnalogModulationPmDeviation(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetAnalogModulationType(self, channel, value):
        """ GetAnalogModulationType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetAnalogModulationWaveformFrequency(self, channel, value):
        """ GetAnalogModulationWaveformFrequency(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetAnalogModulationWaveformType(self, channel, value):
        """ GetAnalogModulationWaveformType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbCarrierFrequency(self, channel, value):
        """ GetArbCarrierFrequency(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbFilterRaisedCosineAlpha(self, channel, value):
        """ GetArbFilterRaisedCosineAlpha(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbFilterRootRaisedCosineAlpha(self, channel, value):
        """ GetArbFilterRootRaisedCosineAlpha(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbFilterType(self, channel, value):
        """ GetArbFilterType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbMaxNumberWaveforms(self, channel, value):
        """ GetArbMaxNumberWaveforms(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbOnboardSampleClockMode(self, channel, value):
        """ GetArbOnboardSampleClockMode(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbOscillatorPhaseDacValue(self, channel, value):
        """ GetArbOscillatorPhaseDacValue(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbPower(self, channel, value):
        """ GetArbPower(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbPreFilterGain(self, channel, value):
        """ GetArbPreFilterGain(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbSampleClockRate(self, channel, value):
        """ GetArbSampleClockRate(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbSampleClockSource(self, channel, value):
        """ GetArbSampleClockSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetArbTemperature(self, channel, value):
        """ GetArbTemperature(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetArbWaveformQuantum(self, channel, value):
        """ GetArbWaveformQuantum(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbWaveformRepeatCount(self, channel, value):
        """ GetArbWaveformRepeatCount(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbWaveformSizeMax(self, channel, value):
        """ GetArbWaveformSizeMax(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbWaveformSizeMin(self, channel, value):
        """ GetArbWaveformSizeMin(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetArbWaveformSoftwareScalingFactor(self, channel, value):
        """ GetArbWaveformSoftwareScalingFactor(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetAttenuatorHoldEnabled(self, channel, value):
        """ GetAttenuatorHoldEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetAttenuatorHoldMaxPower(self, channel, value):
        """ GetAttenuatorHoldMaxPower(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetAttrArbWaveformRepeatCountIsFinite(self, channel, value):
        """ GetAttrArbWaveformRepeatCountIsFinite(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetAutomaticThermalCorrection(self, channel, value):
        """ GetAutomaticThermalCorrection(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetBoolean(self, propertyId, *__args):
        """
        GetBoolean(self: niRFSG, propertyId: niRFSGProperties) -> (int, bool)
        GetBoolean(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> bool
        GetBoolean(self: niRFSG, propertyId: niRFSGProperties) -> bool
        GetBoolean(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> (int, bool)
        """
        pass

    def GetCache(self, channel, value):
        """ GetCache(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetChannelName(self, Index, BufferSize, Channel_Name):
        """ GetChannelName(self: niRFSG, Index: int, BufferSize: int, Channel_Name: StringBuilder) -> int """
        pass

    def GetCompensateForFilterGroupDelay(self, channel, value):
        """ GetCompensateForFilterGroupDelay(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetConfigurationListStepInProgress(self, channel, value):
        """ GetConfigurationListStepInProgress(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetConfigurationListStepTriggerTerminalName(self, channel, value):
        """ GetConfigurationListStepTriggerTerminalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetConfigurationListStepTriggerType(self, channel, value):
        """ GetConfigurationListStepTriggerType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDataTransferBlockSize(self, channel, value):
        """ GetDataTransferBlockSize(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDataTransferMaximumBandwidth(self, channel, value):
        """ GetDataTransferMaximumBandwidth(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetDataTransferMaximumInFlightReads(self, channel, value):
        """ GetDataTransferMaximumInFlightReads(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDataTransferPreferredPacketSize(self, channel, value):
        """ GetDataTransferPreferredPacketSize(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDeviceTemperature(self, channel, value):
        """ GetDeviceTemperature(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetDigitalEdgeConfigurationListStepTriggerEdge(self, channel, value):
        """ GetDigitalEdgeConfigurationListStepTriggerEdge(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalEdgeConfigurationListStepTriggerSource(self, channel, value):
        """ GetDigitalEdgeConfigurationListStepTriggerSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetDigitalEdgeScriptTriggerEdge(self, channel, value):
        """ GetDigitalEdgeScriptTriggerEdge(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalEdgeScriptTriggerSource(self, channel, value):
        """ GetDigitalEdgeScriptTriggerSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetDigitalEdgeStartTriggerEdge(self, channel, value):
        """ GetDigitalEdgeStartTriggerEdge(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalEdgeStartTriggerSource(self, channel, value):
        """ GetDigitalEdgeStartTriggerSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetDigitalEqualizationEnabled(self, channel, value):
        """ GetDigitalEqualizationEnabled(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalLevelScriptTriggerActiveLevel(self, channel, value):
        """ GetDigitalLevelScriptTriggerActiveLevel(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalLevelScriptTriggerSource(self, channel, value):
        """ GetDigitalLevelScriptTriggerSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetDigitalModulationFskDeviation(self, channel, value):
        """ GetDigitalModulationFskDeviation(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetDigitalModulationPrbsOrder(self, channel, value):
        """ GetDigitalModulationPrbsOrder(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalModulationPrbsSeed(self, channel, value):
        """ GetDigitalModulationPrbsSeed(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalModulationSymbolRate(self, channel, value):
        """ GetDigitalModulationSymbolRate(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetDigitalModulationType(self, channel, value):
        """ GetDigitalModulationType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalModulationWaveformType(self, channel, value):
        """ GetDigitalModulationWaveformType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDigitalPattern(self, channel, value):
        """ GetDigitalPattern(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetDirectDmaEnabled(self, channel, value):
        """ GetDirectDmaEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetDirectDmaWindowAddress(self, channel, value):
        """ GetDirectDmaWindowAddress(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDirectDmaWindowSize(self, channel, value):
        """ GetDirectDmaWindowSize(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDirectDownload(self, channel, value):
        """ GetDirectDownload(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetDoneEventTerminalName(self, channel, value):
        """ GetDoneEventTerminalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetDouble(self, propertyId, *__args):
        """
        GetDouble(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> float
        GetDouble(self: niRFSG, propertyId: niRFSGProperties) -> float
        GetDouble(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> (int, float)
        GetDouble(self: niRFSG, propertyId: niRFSGProperties) -> (int, float)
        """
        pass

    def GetDriverSetup(self, channel, value):
        """ GetDriverSetup(self: niRFSG, channel: str) -> (int, str) """
        pass

    @staticmethod
    def GetError(*__args):
        """
        GetError(handle: HandleRef, code: int, msg: StringBuilder) -> int
        GetError(self: niRFSG, code: int, msg: StringBuilder) -> int
        """
        pass

    def GetEventsDelay(self, channel, value):
        """ GetEventsDelay(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetExportedConfigurationListStepTriggerOutputTerminal(self, channel, value):
        """ GetExportedConfigurationListStepTriggerOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExportedDoneEventOutputTerminal(self, channel, value):
        """ GetExportedDoneEventOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExportedMarkerEventOutputTerminal(self, channel, value):
        """ GetExportedMarkerEventOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExportedRefClockOutputTerminal(self, channel, value):
        """ GetExportedRefClockOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExportedScriptTriggerOutputTerminal(self, channel, value):
        """ GetExportedScriptTriggerOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExportedStartedEventOutputTerminal(self, channel, value):
        """ GetExportedStartedEventOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExportedStartTriggerOutputTerminal(self, channel, value):
        """ GetExportedStartTriggerOutputTerminal(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExternalCalibrationLastDateAndTime(self, Year, Month, Day, Hour, Minute, Second):
        """ GetExternalCalibrationLastDateAndTime(self: niRFSG) -> (int, int, int, int, int, int, int) """
        pass

    def GetExternalCalibrationRecommendedInterval(self, channel, value):
        """ GetExternalCalibrationRecommendedInterval(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetExternalCalibrationTemperature(self, channel, value):
        """ GetExternalCalibrationTemperature(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetExternalCalibrationUserDefinedInfo(self, channel, value):
        """ GetExternalCalibrationUserDefinedInfo(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetExternalCalibrationUserDefinedInfoMaxSize(self, channel, value):
        """ GetExternalCalibrationUserDefinedInfoMaxSize(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetExternalGain(self, channel, value):
        """ GetExternalGain(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetFpgaBitfilePath(self, channel, value):
        """ GetFpgaBitfilePath(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetFrequency(self, channel, value):
        """ GetFrequency(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetFrequencySettling(self, channel, value):
        """ GetFrequencySettling(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetFrequencySettlingUnits(self, channel, value):
        """ GetFrequencySettlingUnits(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetFrequencyTolerance(self, channel, value):
        """ GetFrequencyTolerance(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetGenerationMode(self, channel, value):
        """ GetGenerationMode(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetGroupCapabilities(self, channel, value):
        """ GetGroupCapabilities(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetInstrumentFirmwareRevision(self, channel, value):
        """ GetInstrumentFirmwareRevision(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetInstrumentManufacturer(self, channel, value):
        """ GetInstrumentManufacturer(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetInstrumentModel(self, channel, value):
        """ GetInstrumentModel(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetInt32(self, propertyId, *__args):
        """
        GetInt32(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> int
        GetInt32(self: niRFSG, propertyId: niRFSGProperties) -> int
        GetInt32(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> (int, int)
        GetInt32(self: niRFSG, propertyId: niRFSGProperties) -> (int, int)
        """
        pass

    def GetInterchangeCheck(self, channel, value):
        """ GetInterchangeCheck(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetInterpolationDelay(self, channel, value):
        """ GetInterpolationDelay(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqGainImbalance(self, channel, value):
        """ GetIqGainImbalance(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqImpairmentEnabled(self, channel, value):
        """ GetIqImpairmentEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetIqIOffset(self, channel, value):
        """ GetIqIOffset(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOffsetUnits(self, channel, value):
        """ GetIqOffsetUnits(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetIqOutPortCarrierFrequency(self, channel, value):
        """ GetIqOutPortCarrierFrequency(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOutPortCommonModeOffset(self, channel, value):
        """ GetIqOutPortCommonModeOffset(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOutPortLevel(self, channel, value):
        """ GetIqOutPortLevel(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOutPortLoadImpedance(self, channel, value):
        """ GetIqOutPortLoadImpedance(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOutPortOffset(self, channel, value):
        """ GetIqOutPortOffset(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOutPortTemperature(self, channel, value):
        """ GetIqOutPortTemperature(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqOutPortTerminalConfiguration(self, channel, value):
        """ GetIqOutPortTerminalConfiguration(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetIqQOffset(self, channel, value):
        """ GetIqQOffset(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqRate(self, channel, value):
        """ GetIqRate(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqSkew(self, channel, value):
        """ GetIqSkew(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetIqSwapEnabled(self, channel, value):
        """ GetIqSwapEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetLoFrequencyStepSize(self, channel, value):
        """ GetLoFrequencyStepSize(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetLogicalName(self, channel, value):
        """ GetLogicalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetLoInPower(self, channel, value):
        """ GetLoInPower(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetLong(self, propertyId, *__args):
        """
        GetLong(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> Int64
        GetLong(self: niRFSG, propertyId: niRFSGProperties) -> Int64
        GetLong(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> (int, Int64)
        GetLong(self: niRFSG, propertyId: niRFSGProperties) -> (int, Int64)
        """
        pass

    def GetLoopBandwidth(self, channel, value):
        """ GetLoopBandwidth(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetLoOutEnabled(self, channel, value):
        """ GetLoOutEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetLoOutPower(self, channel, value):
        """ GetLoOutPower(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetLoPllFractionalModeEnabled(self, channel, value):
        """ GetLoPllFractionalModeEnabled(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetLoSource(self, channel, value):
        """ GetLoSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetLoTemperature(self, channel, value):
        """ GetLoTemperature(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetMarkerEventTerminalName(self, channel, value):
        """ GetMarkerEventTerminalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetMemorySize(self, channel, value):
        """ GetMemorySize(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetModuleRevision(self, channel, value):
        """ GetModuleRevision(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetOutputEnabled(self, channel, value):
        """ GetOutputEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetOutputPort(self, channel, value):
        """ GetOutputPort(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetP2pDataTransferPermissionInterval(self, channel, value):
        """ GetP2pDataTransferPermissionInterval(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetP2pDataTransferPermissionitialCredits(self, channel, value):
        """ GetP2pDataTransferPermissionitialCredits(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetP2pEnabled(self, channel, value):
        """ GetP2pEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetP2pEndpointCount(self, channel, value):
        """ GetP2pEndpointCount(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetP2pEndpointFullnessStartTriggerLevel(self, channel, value):
        """ GetP2pEndpointFullnessStartTriggerLevel(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetP2pEndpointSize(self, channel, value):
        """ GetP2pEndpointSize(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetP2pMostSpaceAvailableInEndpoint(self, channel, value):
        """ GetP2pMostSpaceAvailableInEndpoint(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetP2pSpaceAvailableInEndpoint(self, channel, value):
        """ GetP2pSpaceAvailableInEndpoint(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetPeakEnvelopePower(self, channel, value):
        """ GetPeakEnvelopePower(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetPeakPowerAdjsutmentInheritance(self, channel, value):
        """ GetPeakPowerAdjsutmentInheritance(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetPeakPowerAdjustment(self, channel, value):
        """ GetPeakPowerAdjustment(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetPhaseContinuityEnabled(self, channel, value):
        """ GetPhaseContinuityEnabled(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetPhaseOffset(self, channel, value):
        """ GetPhaseOffset(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetPowerLevel(self, channel, value):
        """ GetPowerLevel(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetPowerLevelType(self, channel, value):
        """ GetPowerLevelType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetPulseModulationEnabled(self, channel, value):
        """ GetPulseModulationEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetPxiChassisClk10Source(self, channel, value):
        """ GetPxiChassisClk10Source(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetQueryInstrumentStatus(self, channel, value):
        """ GetQueryInstrumentStatus(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetRangeCheck(self, channel, value):
        """ GetRangeCheck(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetRecordCoercions(self, channel, value):
        """ GetRecordCoercions(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetRefClockRate(self, channel, value):
        """ GetRefClockRate(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetRefClockSource(self, channel, value):
        """ GetRefClockSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetRefPllBandwidth(self, channel, value):
        """ GetRefPllBandwidth(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetRfBlankingSource(self, channel, value):
        """ GetRfBlankingSource(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetScriptTriggerTerminalName(self, channel, value):
        """ GetScriptTriggerTerminalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetScriptTriggerType(self, channel, value):
        """ GetScriptTriggerType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetSelectedScript(self, channel, value):
        """ GetSelectedScript(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSelfCalibrationDateAndTime(self, Module, Year, Month, Day, Hour, Minute, Second):
        """ GetSelfCalibrationDateAndTime(self: niRFSG, Module: int) -> (int, int, int, int, int, int, int) """
        pass

    def GetSelfCalibrationTemperature(self, *__args):
        """
        GetSelfCalibrationTemperature(self: niRFSG, module: int) -> (int, float)
        GetSelfCalibrationTemperature(self: niRFSG, channel: str) -> (int, float)
        """
        pass

    def GetSerialNumber(self, channel, value):
        """ GetSerialNumber(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSignalBandwidth(self, channel, value):
        """ GetSignalBandwidth(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetSimulate(self, channel, value):
        """ GetSimulate(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetSpecificDriverClassSpecMajorVersion(self, channel, value):
        """ GetSpecificDriverClassSpecMajorVersion(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetSpecificDriverClassSpecMinorVersion(self, channel, value):
        """ GetSpecificDriverClassSpecMinorVersion(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetSpecificDriverDescription(self, channel, value):
        """ GetSpecificDriverDescription(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSpecificDriverPrefix(self, channel, value):
        """ GetSpecificDriverPrefix(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSpecificDriverRevision(self, channel, value):
        """ GetSpecificDriverRevision(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSpecificDriverVendor(self, channel, value):
        """ GetSpecificDriverVendor(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetStartedEventTerminalName(self, channel, value):
        """ GetStartedEventTerminalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetStartTriggerTerminalName(self, channel, value):
        """ GetStartTriggerTerminalName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetStartTriggerType(self, channel, value):
        """ GetStartTriggerType(self: niRFSG, channel: str) -> (int, int) """
        pass

    def GetStreamEndpointHandle(self, Stream_Endpoint, Reader_Handle):
        """ GetStreamEndpointHandle(self: niRFSG, Stream_Endpoint: str) -> (int, UInt32) """
        pass

    def GetStreamingEnabled(self, channel, value):
        """ GetStreamingEnabled(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetStreamingSpaceAvailableInWaveform(self, channel, value):
        """ GetStreamingSpaceAvailableInWaveform(self: niRFSG, channel: str) -> (int, Int64) """
        pass

    def GetStreamingWaveformName(self, channel, value):
        """ GetStreamingWaveformName(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetStreamingWriteTimeout(self, channel, value):
        """ GetStreamingWriteTimeout(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetString(self, propertyId, *__args):
        """
        GetString(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> str
        GetString(self: niRFSG, propertyId: niRFSGProperties) -> str
        GetString(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str) -> (int, str)
        GetString(self: niRFSG, propertyId: niRFSGProperties) -> (int, str)
        """
        pass

    def GetSupportedInstrumentModels(self, channel, value):
        """ GetSupportedInstrumentModels(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSyncSampleClockDistLine(self, channel, value):
        """ GetSyncSampleClockDistLine(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSyncSampleClockMaster(self, channel, value):
        """ GetSyncSampleClockMaster(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetSyncScriptTriggerDistLine(self, channel, value):
        """ GetSyncScriptTriggerDistLine(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSyncScriptTriggerMaster(self, channel, value):
        """ GetSyncScriptTriggerMaster(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetSyncStartTriggerDistLine(self, channel, value):
        """ GetSyncStartTriggerDistLine(self: niRFSG, channel: str) -> (int, str) """
        pass

    def GetSyncStartTriggerMaster(self, channel, value):
        """ GetSyncStartTriggerMaster(self: niRFSG, channel: str) -> (int, bool) """
        pass

    def GetTerminalName(self, Signal, Signal_Identifier, Buffer_Size, Terminal_Name):
        """ GetTerminalName(self: niRFSG, Signal: int, Signal_Identifier: str, Buffer_Size: int, Terminal_Name: StringBuilder) -> int """
        pass

    def GetTimerEventInterval(self, channel, value):
        """ GetTimerEventInterval(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetUpconverterCenterFrequency(self, channel, value):
        """ GetUpconverterCenterFrequency(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetUpconverterCenterFrequencyIncrement(self, channel, value):
        """ GetUpconverterCenterFrequencyIncrement(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetUpconverterCenterFrequencyIncrementAnchor(self, channel, value):
        """ GetUpconverterCenterFrequencyIncrementAnchor(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetUpconverterFrequencyOffset(self, channel, value):
        """ GetUpconverterFrequencyOffset(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetUpconverterGain(self, channel, value):
        """ GetUpconverterGain(self: niRFSG, channel: str) -> (int, float) """
        pass

    def GetUserData(self, Channel_Name, bufferSize, data, actualDataSize):
        """ GetUserData(self: niRFSG, Channel_Name: str, bufferSize: int) -> (int, Array[Char], int) """
        pass

    def GetYigMainCoilDrive(self, channel, value):
        """ GetYigMainCoilDrive(self: niRFSG, channel: str) -> (int, int) """
        pass

    def Initiate(self):
        """ Initiate(self: niRFSG) -> int """
        pass

    def PerformPowerSearch(self):
        """ PerformPowerSearch(self: niRFSG) -> int """
        pass

    def PerformThermalCorrection(self):
        """ PerformThermalCorrection(self: niRFSG) -> int """
        pass

    def QueryArbWaveformCapabilities(self, Max_Number_Waveforms, Waveform_Quantum, Min_Waveform_Size, Max_Waveform_Size):
        """ QueryArbWaveformCapabilities(self: niRFSG) -> (int, int, int, int, int) """
        pass

    def reset(self):
        """ reset(self: niRFSG) -> int """
        pass

    def ResetAttribute(self, Channel_Name, Attribute_ID):
        """ ResetAttribute(self: niRFSG, Channel_Name: str, Attribute_ID: int) -> int """
        pass

    def ResetDevice(self):
        """ ResetDevice(self: niRFSG) -> int """
        pass

    def ResetWithDefaults(self):
        """ ResetWithDefaults(self: niRFSG) -> int """
        pass

    def revision_query(self, Instrument_Driver_Revision, Firmware_Revision):
        """ revision_query(self: niRFSG, Instrument_Driver_Revision: StringBuilder, Firmware_Revision: StringBuilder) -> int """
        pass

    def SelectArbWaveform(self, Name):
        """ SelectArbWaveform(self: niRFSG, Name: str) -> int """
        pass

    def SelfCal(self):
        """ SelfCal(self: niRFSG) -> int """
        pass

    def SelfCalibrateRange(self, stepsToOmit, minFrequency, maxFrequency, minPowerLevel, maxPowerLevel):
        """ SelfCalibrateRange(self: niRFSG, stepsToOmit: Int64, minFrequency: float, maxFrequency: float, minPowerLevel: float, maxPowerLevel: float) -> int """
        pass

    def self_test(self, Self_Test_Result, Self_Test_Message):
        """ self_test(self: niRFSG, Self_Test_Message: StringBuilder) -> (int, Int16) """
        pass

    def SendSoftwareEdgeTrigger(self, Trigger, Trigger_Identifier):
        """ SendSoftwareEdgeTrigger(self: niRFSG, Trigger: int, Trigger_Identifier: str) -> int """
        pass

    def SetActiveConfigurationList(self, channel, value):
        """ SetActiveConfigurationList(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetActiveConfigurationListStep(self, channel, value):
        """ SetActiveConfigurationListStep(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetAllowOutOfSpecificationUserSettings(self, channel, value):
        """ SetAllowOutOfSpecificationUserSettings(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetAnalogModulationFmDeviation(self, channel, value):
        """ SetAnalogModulationFmDeviation(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetAnalogModulationPmDeviation(self, channel, value):
        """ SetAnalogModulationPmDeviation(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetAnalogModulationType(self, channel, value):
        """ SetAnalogModulationType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetAnalogModulationWaveformFrequency(self, channel, value):
        """ SetAnalogModulationWaveformFrequency(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetAnalogModulationWaveformType(self, channel, value):
        """ SetAnalogModulationWaveformType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetArbCarrierFrequency(self, channel, value):
        """ SetArbCarrierFrequency(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetArbFilterRaisedCosineAlpha(self, channel, value):
        """ SetArbFilterRaisedCosineAlpha(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetArbFilterRootRaisedCosineAlpha(self, channel, value):
        """ SetArbFilterRootRaisedCosineAlpha(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetArbFilterType(self, channel, value):
        """ SetArbFilterType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetArbOnboardSampleClockMode(self, channel, value):
        """ SetArbOnboardSampleClockMode(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetArbOscillatorPhaseDacValue(self, channel, value):
        """ SetArbOscillatorPhaseDacValue(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetArbPreFilterGain(self, channel, value):
        """ SetArbPreFilterGain(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetArbSampleClockSource(self, channel, value):
        """ SetArbSampleClockSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetArbWaveformRepeatCount(self, channel, value):
        """ SetArbWaveformRepeatCount(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetArbWaveformRepeatCountIsFinite(self, channel, value):
        """ SetArbWaveformRepeatCountIsFinite(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetArbWaveformSoftwareScalingFactor(self, channel, value):
        """ SetArbWaveformSoftwareScalingFactor(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetAttenuatorHoldEnabled(self, channel, value):
        """ SetAttenuatorHoldEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetAttenuatorHoldMaxPower(self, channel, value):
        """ SetAttenuatorHoldMaxPower(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetBoolean(self, propertyId, *__args):
        """
        SetBoolean(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str, val: bool) -> int
        SetBoolean(self: niRFSG, propertyId: niRFSGProperties, val: bool) -> int
        """
        pass

    def SetCache(self, channel, value):
        """ SetCache(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetCompensateForFilterGroupDelay(self, channel, value):
        """ SetCompensateForFilterGroupDelay(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetConfigurationListStepTriggerType(self, channel, value):
        """ SetConfigurationListStepTriggerType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDataTransferBlockSize(self, channel, value):
        """ SetDataTransferBlockSize(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDataTransferMaximumBandwidth(self, channel, value):
        """ SetDataTransferMaximumBandwidth(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetDataTransferMaximumInFlightReads(self, channel, value):
        """ SetDataTransferMaximumInFlightReads(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDataTransferPreferredPacketSize(self, channel, value):
        """ SetDataTransferPreferredPacketSize(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalEdgeConfigurationListStepTriggerEdge(self, channel, value):
        """ SetDigitalEdgeConfigurationListStepTriggerEdge(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalEdgeConfigurationListStepTriggerSource(self, channel, value):
        """ SetDigitalEdgeConfigurationListStepTriggerSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetDigitalEdgeScriptTriggerEdge(self, channel, value):
        """ SetDigitalEdgeScriptTriggerEdge(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalEdgeScriptTriggerSource(self, channel, value):
        """ SetDigitalEdgeScriptTriggerSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetDigitalEdgeStartTriggerEdge(self, channel, value):
        """ SetDigitalEdgeStartTriggerEdge(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalEdgeStartTriggerSource(self, channel, value):
        """ SetDigitalEdgeStartTriggerSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetDigitalEqualizationEnabled(self, channel, value):
        """ SetDigitalEqualizationEnabled(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalLevelScriptTriggerActiveLevel(self, channel, value):
        """ SetDigitalLevelScriptTriggerActiveLevel(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalLevelScriptTriggerSource(self, channel, value):
        """ SetDigitalLevelScriptTriggerSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetDigitalModulationFskDeviation(self, channel, value):
        """ SetDigitalModulationFskDeviation(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetDigitalModulationPrbsOrder(self, channel, value):
        """ SetDigitalModulationPrbsOrder(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalModulationPrbsSeed(self, channel, value):
        """ SetDigitalModulationPrbsSeed(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalModulationSymbolRate(self, channel, value):
        """ SetDigitalModulationSymbolRate(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetDigitalModulationType(self, channel, value):
        """ SetDigitalModulationType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalModulationWaveformType(self, channel, value):
        """ SetDigitalModulationWaveformType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDigitalPattern(self, channel, value):
        """ SetDigitalPattern(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetDirectDmaEnabled(self, channel, value):
        """ SetDirectDmaEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetDirectDmaWindowAddress(self, channel, value):
        """ SetDirectDmaWindowAddress(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDirectDmaWindowSize(self, channel, value):
        """ SetDirectDmaWindowSize(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDirectDownload(self, channel, value):
        """ SetDirectDownload(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetDouble(self, propertyId, *__args):
        """
        SetDouble(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str, val: float) -> int
        SetDouble(self: niRFSG, propertyId: niRFSGProperties, val: float) -> int
        """
        pass

    def SetEventsDelay(self, channel, value):
        """ SetEventsDelay(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetExportedConfigurationListStepTriggerOutputTerminal(self, channel, value):
        """ SetExportedConfigurationListStepTriggerOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExportedDoneEventOutputTerminal(self, channel, value):
        """ SetExportedDoneEventOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExportedMarkerEventOutputTerminal(self, channel, value):
        """ SetExportedMarkerEventOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExportedRefClockOutputTerminal(self, channel, value):
        """ SetExportedRefClockOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExportedScriptTriggerOutputTerminal(self, channel, value):
        """ SetExportedScriptTriggerOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExportedStartedEventOutputTerminal(self, channel, value):
        """ SetExportedStartedEventOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExportedStartTriggerOutputTerminal(self, channel, value):
        """ SetExportedStartTriggerOutputTerminal(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetExternalGain(self, channel, value):
        """ SetExternalGain(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetFrequency(self, channel, value):
        """ SetFrequency(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetFrequencySettling(self, channel, value):
        """ SetFrequencySettling(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetFrequencySettlingUnits(self, channel, value):
        """ SetFrequencySettlingUnits(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetFrequencyTolerance(self, channel, value):
        """ SetFrequencyTolerance(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetGenerationMode(self, channel, value):
        """ SetGenerationMode(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetInt32(self, propertyId, *__args):
        """
        SetInt32(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str, val: int) -> int
        SetInt32(self: niRFSG, propertyId: niRFSGProperties, val: int) -> int
        """
        pass

    def SetInterchangeCheck(self, channel, value):
        """ SetInterchangeCheck(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetInterpolationDelay(self, channel, value):
        """ SetInterpolationDelay(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqGainImbalance(self, channel, value):
        """ SetIqGainImbalance(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqImpairmentEnabled(self, channel, value):
        """ SetIqImpairmentEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetIqIOffset(self, channel, value):
        """ SetIqIOffset(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqOffsetUnits(self, channel, value):
        """ SetIqOffsetUnits(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetIqOutPortCarrierFrequency(self, channel, value):
        """ SetIqOutPortCarrierFrequency(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqOutPortCommonModeOffset(self, channel, value):
        """ SetIqOutPortCommonModeOffset(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqOutPortLevel(self, channel, value):
        """ SetIqOutPortLevel(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqOutPortLoadImpedance(self, channel, value):
        """ SetIqOutPortLoadImpedance(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqOutPortOffset(self, channel, value):
        """ SetIqOutPortOffset(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqOutPortTerminalConfiguration(self, channel, value):
        """ SetIqOutPortTerminalConfiguration(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetIqQOffset(self, channel, value):
        """ SetIqQOffset(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqRate(self, channel, value):
        """ SetIqRate(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqSkew(self, channel, value):
        """ SetIqSkew(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetIqSwapEnabled(self, channel, value):
        """ SetIqSwapEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetLoFrequencyStepSize(self, channel, value):
        """ SetLoFrequencyStepSize(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetLoInPower(self, channel, value):
        """ SetLoInPower(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetLong(self, propertyId, *__args):
        """
        SetLong(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str, val: Int64) -> int
        SetLong(self: niRFSG, propertyId: niRFSGProperties, val: Int64) -> int
        """
        pass

    def SetLoopBandwidth(self, channel, value):
        """ SetLoopBandwidth(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetLoOutEnabled(self, channel, value):
        """ SetLoOutEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetLoPllFractionalModeEnabled(self, channel, value):
        """ SetLoPllFractionalModeEnabled(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetLoSource(self, channel, value):
        """ SetLoSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetOutputEnabled(self, channel, value):
        """ SetOutputEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetOutputPort(self, channel, value):
        """ SetOutputPort(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetP2pDataTransferPermissionInterval(self, channel, value):
        """ SetP2pDataTransferPermissionInterval(self: niRFSG, channel: str, value: Int64) -> int """
        pass

    def SetP2pDataTransferPermissionitialCredits(self, channel, value):
        """ SetP2pDataTransferPermissionitialCredits(self: niRFSG, channel: str, value: Int64) -> int """
        pass

    def SetP2pEnabled(self, channel, value):
        """ SetP2pEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetP2pEndpointFullnessStartTriggerLevel(self, channel, value):
        """ SetP2pEndpointFullnessStartTriggerLevel(self: niRFSG, channel: str, value: Int64) -> int """
        pass

    def SetPeakPowerAdjsutmentInheritance(self, channel, value):
        """ SetPeakPowerAdjsutmentInheritance(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetPeakPowerAdjustment(self, channel, value):
        """ SetPeakPowerAdjustment(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetPhaseContinuityEnabled(self, channel, value):
        """ SetPhaseContinuityEnabled(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetPhaseOffset(self, channel, value):
        """ SetPhaseOffset(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetPowerLevel(self, channel, value):
        """ SetPowerLevel(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetPowerLevelType(self, channel, value):
        """ SetPowerLevelType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetPulseModulationEnabled(self, channel, value):
        """ SetPulseModulationEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetPxiChassisClk10Source(self, channel, value):
        """ SetPxiChassisClk10Source(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetQueryInstrumentStatus(self, channel, value):
        """ SetQueryInstrumentStatus(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetRangeCheck(self, channel, value):
        """ SetRangeCheck(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetRecordCoercions(self, channel, value):
        """ SetRecordCoercions(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetRefClockRate(self, channel, value):
        """ SetRefClockRate(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetRefClockSource(self, channel, value):
        """ SetRefClockSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetRefPllBandwidth(self, channel, value):
        """ SetRefPllBandwidth(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetRfBlankingSource(self, channel, value):
        """ SetRfBlankingSource(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetScriptTriggerType(self, channel, value):
        """ SetScriptTriggerType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetSelectedScript(self, channel, value):
        """ SetSelectedScript(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetSignalBandwidth(self, channel, value):
        """ SetSignalBandwidth(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetStartTriggerType(self, channel, value):
        """ SetStartTriggerType(self: niRFSG, channel: str, value: int) -> int """
        pass

    def SetStreamingEnabled(self, channel, value):
        """ SetStreamingEnabled(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetStreamingWaveformName(self, channel, value):
        """ SetStreamingWaveformName(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetStreamingWriteTimeout(self, channel, value):
        """ SetStreamingWriteTimeout(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetString(self, propertyId, *__args):
        """
        SetString(self: niRFSG, propertyId: niRFSGProperties, repeatedCapabilityOrChannel: str, val: str) -> int
        SetString(self: niRFSG, propertyId: niRFSGProperties, val: str) -> int
        """
        pass

    def SetSyncSampleClockDistLine(self, channel, value):
        """ SetSyncSampleClockDistLine(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetSyncSampleClockMaster(self, channel, value):
        """ SetSyncSampleClockMaster(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetSyncScriptTriggerDistLine(self, channel, value):
        """ SetSyncScriptTriggerDistLine(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetSyncScriptTriggerMaster(self, channel, value):
        """ SetSyncScriptTriggerMaster(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetSyncStartTriggerDistLine(self, channel, value):
        """ SetSyncStartTriggerDistLine(self: niRFSG, channel: str, value: str) -> int """
        pass

    def SetSyncStartTriggerMaster(self, channel, value):
        """ SetSyncStartTriggerMaster(self: niRFSG, channel: str, value: bool) -> int """
        pass

    def SetTimerEventInterval(self, channel, value):
        """ SetTimerEventInterval(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetUpconverterCenterFrequency(self, channel, value):
        """ SetUpconverterCenterFrequency(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetUpconverterCenterFrequencyIncrement(self, channel, value):
        """ SetUpconverterCenterFrequencyIncrement(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetUpconverterCenterFrequencyIncrementAnchor(self, channel, value):
        """ SetUpconverterCenterFrequencyIncrementAnchor(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetUpconverterFrequencyOffset(self, channel, value):
        """ SetUpconverterFrequencyOffset(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetUpconverterGain(self, channel, value):
        """ SetUpconverterGain(self: niRFSG, channel: str, value: float) -> int """
        pass

    def SetUserData(self, Channel_Name, bufferSize, data):
        """ SetUserData(self: niRFSG, Channel_Name: str, bufferSize: int, data: Array[Char]) -> int """
        pass

    def SetYigMainCoilDrive(self, channel, value):
        """ SetYigMainCoilDrive(self: niRFSG, channel: str, value: int) -> int """
        pass

    def WaitUntilSettled(self, Max_Time_Milliseconds):
        """ WaitUntilSettled(self: niRFSG, Max_Time_Milliseconds: int) -> int """
        pass

    def WriteArbWaveform(self, Name, Number_Of_Samples, IData, QData, More_Data_Pending):
        """ WriteArbWaveform(self: niRFSG, Name: str, Number_Of_Samples: int, IData: Array[float], QData: Array[float], More_Data_Pending: bool) -> int """
        pass

    def WriteArbWaveformComplexF32(self, Name, Number_Of_Samples, Data, More_Data_Pending):
        """ WriteArbWaveformComplexF32(self: niRFSG, Name: str, Number_Of_Samples: int, Data: Array[niComplexNumberF32], More_Data_Pending: bool) -> int """
        pass

    def WriteArbWaveformComplexF64(self, Name, Number_Of_Samples, Data, More_Data_Pending):
        """ WriteArbWaveformComplexF64(self: niRFSG, Name: str, Number_Of_Samples: int, Data: Array[niComplexNumber], More_Data_Pending: bool) -> int """
        pass

    def WriteArbWaveformComplexI16(self, Name, Number_Of_Samples, Data):
        """
        WriteArbWaveformComplexI16(self: niRFSG, Name: str, Number_Of_Samples: int, Data: Array[niComplexI16]) -> int
        WriteArbWaveformComplexI16(self: niRFSG, Name: str, Number_Of_Samples: int, Data: Array[RfsgNIComplexI16]) -> int
        """
        pass

    def WriteArbWaveformF32(self, Name, Number_Of_Samples, iData, qData, More_Data_Pending):
        """ WriteArbWaveformF32(self: niRFSG, Name: str, Number_Of_Samples: int, iData: Array[Single], qData: Array[Single], More_Data_Pending: bool) -> int """
        pass

    def WriteP2PEndpointI16(self, Stream_Endpoint, Number_Of_Samples, Endpoint_Data):
        """ WriteP2PEndpointI16(self: niRFSG, Stream_Endpoint: str, Number_Of_Samples: int, Endpoint_Data: Array[Int16]) -> int """
        pass

    def WriteScript(self, Script):
        """ WriteScript(self: niRFSG, Script: str) -> int """
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
    def __new__(self, Resource_Name, ID_Query, Reset, Option_String=None):
        """
        __new__(cls: type, Resource_Name: str, ID_Query: bool, Reset: bool)
        __new__(cls: type, Resource_Name: str, ID_Query: bool, Reset: bool, Option_String: str)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: niRFSG) -> HandleRef

"""



class niRFSGConstants(object):
    """ niRFSGConstants() """
    ActiveHigh = 9000
    ActiveLow = 9001
    Am = 2002
    ArbExternalTriggerSlopeNegative = 1
    ArbExternalTriggerSlopePositive = 0
    ArbFilterTypeNone = 10000
    ArbFilterTypeRaisedCosine = 10002
    ArbFilterTypeRootRaisedCosine = 10001
    ArbTriggerSourceExternal = 1
    ArbTriggerSourceImmediate = 0
    ArbTriggerSourceSoftware = 2
    ArbWaveform = 1001
    Auto = -1
    AveragePower = 7000
    CalOut = 14002
    ClkInStr = 'ClkIn'
    ClkOutStr = 'ClkOut'
    ConfigurationListRepeatContinuous = 0
    ConfigurationListRepeatSingle = 1
    ConfigurationListStepTrigger = 6
    ConfigurationSettledEvent = 7
    Cw = 1000
    Differential = 15000
    DigitalEdge = 1
    DigitalLevel = 8000
    Disable = 0
    DivideDown = 6001
    DoneEvent = 5
    DoNotExportStr = ''
    DucNone = 10000
    DucRaisedCosine = 10002
    DucRootRaisedCosine = 10001
    Enable = 1
    ExactMatch = 0
    FallingEdge = 1
    Fast = 1
    Fm = 2000
    FmBanded = 14001
    FmContinuous = 14000
    Fsk = 4000
    HighDeviation = 19000
    HighIsolation = 20001
    HighPower = 16000
    HighResolution = 6000
    IOnly = 14003
    IqOut = 14001
    LoSourceLoInStr = 'LO_In'
    LoSourceOnboardStr = 'Onboard'
    Low = 0
    LowHarmonic = 16001
    LowPhaseNoise = 19001
    Marker0EventStr = 'Marker0Event'
    Marker1EventStr = 'Marker1Event'
    Marker2EventStr = 'Marker2Event'
    Marker3EventStr = 'Marker3Event'
    MarkerEvent = 2
    MarkerEvent0 = 'marker0'
    MarkerEvent1 = 'marker1'
    MarkerEvent2 = 'marker2'
    MarkerEvent3 = 'marker3'
    MaxTimeImmediate = 0
    MaxTimeInfinite = None
    Medium = 1
    Minimum = 1
    Narrow = 0
    Narrowband = 17000
    None = 0
    NoneStr = 'None'
    OnBoardClockStr = 'OnBoardClock'
    OnboardClockStr = 'OnboardClock'
    onboardClockStr = 'OnboardClock'
    Ook = 4001
    OptimalMatch = 20000
    P2pEndpointFullness = 3
    PeakPower = 7001
    Percent = 11000
    Pfi0Str = 'PFI0'
    Pfi1Str = 'PFI1'
    Pfi2Str = 'PFI2'
    Pfi3Str = 'PFI3'
    Pfi4Str = 'PFI4'
    Pfi5Str = 'PFI5'
    Pm = 2001
    Ppm = 12002
    Prbs = 5000
    Psk = 4002
    PxiClk10Str = 'PXI_CLK10'
    PxiClkStr = 'PXI_CLK'
    PxiStarStr = 'PXI_STAR'
    PxiTrig0Str = 'PXI_Trig0'
    PxiTrig1Str = 'PXI_Trig1'
    PxiTrig2Str = 'PXI_Trig2'
    PxiTrig3Str = 'PXI_Trig3'
    PxiTrig4Str = 'PXI_Trig4'
    PxiTrig5Str = 'PXI_Trig5'
    PxiTrig6Str = 'PXI_Trig6'
    PxiTrig7Str = 'PXI_Trig7'
    RefClock = 3
    RefClockSourcePxiClk = 1001
    ReferenceOscillatorSourceExternal = 1
    ReferenceOscillatorSourceInternal = 0
    RefInStr = 'RefIn'
    RefOut2Str = 'RefOut2'
    RefOutStr = 'RefOut'
    RfOut = 14000
    RisingEdge = 0
    Rtsi0Str = 'RTSI0'
    Rtsi1Str = 'RTSI1'
    Rtsi2Str = 'RTSI2'
    Rtsi3Str = 'RTSI3'
    Rtsi4Str = 'RTSI4'
    Rtsi5Str = 'RTSI5'
    Rtsi6Str = 'RTSI6'
    Rtsi7Str = 'RTSI7'
    Script = 1002
    ScriptTrigger = 1
    ScriptTrigger0 = 'scriptTrigger0'
    ScriptTrigger1 = 'scriptTrigger1'
    ScriptTrigger2 = 'scriptTrigger2'
    ScriptTrigger3 = 'scriptTrigger3'
    SelfCalImageSuppression = 8
    SelfCalLoSelfCal = 1
    SelfCalOmitNone = 0
    SelfCalPowerLevelAccuracy = 2
    SelfCalResidualLoPower = 4
    Sine = 3000
    SingleEnded = 15001
    Slow = 0
    Software = 2
    Square = 3001
    StartedEvent = 4
    StartTrigger = 0
    SyncScriptTriggerStr = 'Sync_Script'
    SyncStartTriggerStr = 'Sync_Start'
    TimeAfterIo = 12001
    TimeAfterLock = 12000
    TimerEventStr = 'TimerEvent'
    Triangle = 3002
    TrigInStr = 'TrigIn'
    TrigOutStr = 'TrigOut'
    UserDefined = 5001
    Volts = 11001
    Wide = 2
    Wideband = 17001
    _100hzTo1khz = 18000
    _10khzTo100khz = 18002
    _10mhz = 10000000
    _1khzTo10khz = 18001


class niRFSGProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum niRFSGProperties, values: ActiveConfigurationList (1150096), ActiveConfigurationListStep (1150097), AeSession (1150183), AeTemperature (1150182), AlcControl (1150195), AlcEnabled (1250003), AllowOutOfSpecificationUserSettings (1150014), AmplitudeSettling (1150137), AmpPath (1150185), AnalogModulationAmSensitivity (1150167), AnalogModulationFmBand (1150191), AnalogModulationFmDeviation (1150035), AnalogModulationFmNarrowbandIntegrator (1150165), AnalogModulationFmSensitivity (1150166), AnalogModulationPmDeviation (1150062), AnalogModulationPmMode (1150192), AnalogModulationPmSensitivity (1150168), AnalogModulationType (1150032), AnalogModulationWaveformFrequency (1150034), AnalogModulationWaveformType (1150033), ArbCarrierFrequency (1150015), ArbFilterFrequency (1250453), ArbFilterRaisedCosineAlpha (1150060), ArbFilterRootRaisedCosineAlpha (1150057), ArbFilterType (1150056), ArbMaxNumberWaveforms (1250454), ArbOnboardSampleClockMode (1150029), ArbOscillatorPhaseDacValue (1150089), ArbPower (1150016), ArbPreFilterGain (1150025), ArbSampleClockRate (1150031), ArbSampleClockSource (1150030), ArbTemperature (1150068), ArbTriggerSource (1250458), ArbWaveformQuantum (1250455), ArbWaveformRepeatCount (1150158), ArbWaveformRepeatCountIsFinite (1150157), ArbWaveformSizeMax (1250457), ArbWaveformSizeMin (1250456), ArbWaveformSoftwareScalingFactor (1150052), AttenuatorHoldEnabled (1150009), AttenuatorHoldMaxPower (1150010), AttenuatorSetting (1150173), AutomaticThermalCorrection (1150008), AutoPowerSearch (1150196), Cache (1050004), ChannelCount (1050203), CompensateForFilterGroupDelay (119740), ConfigurationListIsDone (1150175), ConfigurationListRepeat (1150102), ConfigurationListStepInProgress (1150122), ConfigurationListStepTriggerTerminalName (1150117), ConfigurationListStepTriggerType (1150098), ConfigurationSettledEventTerminalName (1150194), CorrectionTemperature (1150104), DataTransferBlockSize (1150048), DataTransferMaximumBandwidth (1150086), DataTransferMaximumInFlightReads (1150088), DataTransferPreferredPacketSize (1150087), DeviceTemperature (1150017), DigitalEdgeConfigurationListStepTriggerEdge (1150103), DigitalEdgeConfigurationListStepTriggerSource (1150099), DigitalEdgeScriptTriggerEdge (1150021), DigitalEdgeScriptTriggerSource (1150020), DigitalEdgeStartTriggerEdge (1250459), DigitalEdgeStartTriggerSource (1150002), DigitalEqualizationEnabled (1150012), DigitalIfEqualizationEnabled (1150012), DigitalLevelScriptTriggerActiveLevel (1150055), DigitalLevelScriptTriggerSource (1150054), DigitalModulationFskDeviation (1150041), DigitalModulationPrbsOrder (1150039), DigitalModulationPrbsSeed (1150040), DigitalModulationSymbolRate (1150037), DigitalModulationType (1150036), DigitalModulationWaveformType (1150038), DigitalPattern (1150044), DirectDmaEnabled (1150049), DirectDmaWindowAddress (1150050), DirectDmaWindowSize (1150051), DirectDownload (1150042), DoneEventTerminalName (1150113), DriverSetup (1050007), DucFirFilterRaisedCosineAlpha (1150060), DucFirFilterRootRaisedCosineAlpha (1150057), DucFirFilterType (1150056), DucPreFilterGain (1150025), EventsDelay (1150154), ExportedConfigurationListStepTriggerOutputTerminal (1150105), ExportedConfigurationSettledEventOutputTerminal (1150129), ExportedDoneEventOutputTerminal (1150063), ExportedMarkerEventOutputTerminal (1150064), ExportedRefClockOutputTerminal (1150053), ExportedScriptTriggerOutputTerminal (1150022), ExportedStartedEventOutputTerminal (1150065), ExportedStartTriggerOutputTerminal (1150003), ExternalCalibrationRecommendedInterval (1150076), ExternalCalibrationTemperature (1150077), ExternalCalibrationUserDefinedInfo (1150078), ExternalCalibrationUserDefinedInfoMaxSize (1150079), ExternalGain (1150085), FastTuningOption (1150188), FgenSession (1150028), FpgaBitfilePath (1150186), Frequency (1250001), FrequencySettling (1150083), FrequencySettlingUnits (1150082), FrequencyTolerance (1150006), FunctionCapabilities (1050402), GenerationMode (1150018), GroupCapabilities (1050401), IfCarrierFrequency (1150015), IfPower (1150016), InstrumentFirmwareRevision (1050510), InstrumentManufacturer (1050511), InstrumentModel (1050512), InterchangeCheck (1050021), InterpolationDelay (1150153), IOResourceDescriptor (1050304), IqEnabled (1250401), IqGainImbalance (1150072), IqImpairmentEnabled (1150069), IqIOffset (1150070), IqNominalVoltage (1250402), IqOffsetUnits (1150081), IqOutPortCarrierFrequency (1150145), IqOutPortCommonModeOffset (1150148), IqOutPortLevel (1150147), IqOutPortLoadImpedance (1150163), IqOutPortOffset (1150149), IqOutPortTemperature (1150161), IqOutPortTerminalConfiguration (1150146), IqQOffset (1150071), IqRate (1250452), IqSkew (1150073), IqSwapEnabled (1250404), LocalOscillatorOut0Enabled (1150013), LoFrequencyStepSize (1150151), LogicalName (1050305), LoInPower (1150067), LoopBandwidth (1150027), LoOutEnabled (1150013), LoOutPower (1150066), LoPllFractionalModeEnabled (1150152), LoSession (1150074), LoSource (1150150), LoTemperature (1150075), MarkerEventTerminalName (1150115), MemorySize (1150061), ModuleRevision (1150084), OutputEnabled (1250004), OutputPort (1150144), P2pDataTransferPermissionInterval (1150134), P2pDataTransferPermissionitialCredits (1150135), P2pEnabled (1150123), P2pEndpointCount (1150127), P2pEndpointFullnessStartTriggerLevel (1150128), P2pEndpointSize (1150124), P2pMostSpaceAvailableInEndpoint (1150126), P2pSpaceAvailableInEndpoint (1150125), PeakEnvelopePower (1150011), PeakPowerAdjsutmentInheritance (1150141), PeakPowerAdjustment (1150132), PhaseContinuityEnabled (1150005), PhaseOffset (1150024), PowerLevel (1250002), PowerLevelType (1150043), PulseModulationEnabled (1250051), PulseModulationMode (1150190), PxiChassisClk10Source (1150004), QueryInstrumentStatus (1050003), RangeCheck (1050002), RecordCoercions (1050006), RefClockRate (1250322), RefClockSource (1150001), ReferenceOscillatorExternalFrequency (1250322), ReferenceOscillatorSource (1250321), RefPllBandwidth (1150133), RfBlankingSource (1150162), SampleClockRate (1250452), ScriptTriggerTerminalName (1150116), ScriptTriggerType (1150019), SelectedScript (1150023), SelfCalibrationTemperature (1150136), SerialNumber (1150026), SignalBandwidth (1150007), Simulate (1050005), SpecificDriverClassSpecMajorVersion (1050515), SpecificDriverClassSpecMinorVersion (1050516), SpecificDriverDescription (1050514), SpecificDriverPrefix (1050302), SpecificDriverRevision (1050551), SpecificDriverVendor (1050513), Spy (1050022), StartedEventTerminalName (1150112), StartTriggerTerminalName (1150114), StartTriggerType (1250458), StreamingEnabled (1150045), StreamingSpaceAvailableInWaveform (1150047), StreamingWaveformName (1150046), StreamingWriteTimeout (1150140), SupportedInstrumentModels (1050327), SyncSampleClockDistLine (1150181), SyncSampleClockMaster (1150180), SyncScriptTriggerDistLine (1150143), SyncScriptTriggerMaster (1150142), SyncStartTriggerDistLine (1150156), SyncStartTriggerMaster (1150155), ThermalCorrectionEnabled (1150008), TimerEventInterval (1150100), UpconverterCenterFrequency (1154098), UpconverterCenterFrequencyIncrement (1150058), UpconverterCenterFrequencyIncrementAnchor (1150059), UpconverterFrequencyOffset (1150160), UpconverterGain (1154097), UpconverterLoopBandwidth (1150027), UpconverterTemperature (1150017), UseSpecificSimulation (1050023), YigMainCoilDrive (1150118) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveConfigurationList = None
    ActiveConfigurationListStep = None
    AeSession = None
    AeTemperature = None
    AlcControl = None
    AlcEnabled = None
    AllowOutOfSpecificationUserSettings = None
    AmplitudeSettling = None
    AmpPath = None
    AnalogModulationAmSensitivity = None
    AnalogModulationFmBand = None
    AnalogModulationFmDeviation = None
    AnalogModulationFmNarrowbandIntegrator = None
    AnalogModulationFmSensitivity = None
    AnalogModulationPmDeviation = None
    AnalogModulationPmMode = None
    AnalogModulationPmSensitivity = None
    AnalogModulationType = None
    AnalogModulationWaveformFrequency = None
    AnalogModulationWaveformType = None
    ArbCarrierFrequency = None
    ArbFilterFrequency = None
    ArbFilterRaisedCosineAlpha = None
    ArbFilterRootRaisedCosineAlpha = None
    ArbFilterType = None
    ArbMaxNumberWaveforms = None
    ArbOnboardSampleClockMode = None
    ArbOscillatorPhaseDacValue = None
    ArbPower = None
    ArbPreFilterGain = None
    ArbSampleClockRate = None
    ArbSampleClockSource = None
    ArbTemperature = None
    ArbTriggerSource = None
    ArbWaveformQuantum = None
    ArbWaveformRepeatCount = None
    ArbWaveformRepeatCountIsFinite = None
    ArbWaveformSizeMax = None
    ArbWaveformSizeMin = None
    ArbWaveformSoftwareScalingFactor = None
    AttenuatorHoldEnabled = None
    AttenuatorHoldMaxPower = None
    AttenuatorSetting = None
    AutomaticThermalCorrection = None
    AutoPowerSearch = None
    Cache = None
    ChannelCount = None
    CompensateForFilterGroupDelay = None
    ConfigurationListIsDone = None
    ConfigurationListRepeat = None
    ConfigurationListStepInProgress = None
    ConfigurationListStepTriggerTerminalName = None
    ConfigurationListStepTriggerType = None
    ConfigurationSettledEventTerminalName = None
    CorrectionTemperature = None
    DataTransferBlockSize = None
    DataTransferMaximumBandwidth = None
    DataTransferMaximumInFlightReads = None
    DataTransferPreferredPacketSize = None
    DeviceTemperature = None
    DigitalEdgeConfigurationListStepTriggerEdge = None
    DigitalEdgeConfigurationListStepTriggerSource = None
    DigitalEdgeScriptTriggerEdge = None
    DigitalEdgeScriptTriggerSource = None
    DigitalEdgeStartTriggerEdge = None
    DigitalEdgeStartTriggerSource = None
    DigitalEqualizationEnabled = None
    DigitalIfEqualizationEnabled = None
    DigitalLevelScriptTriggerActiveLevel = None
    DigitalLevelScriptTriggerSource = None
    DigitalModulationFskDeviation = None
    DigitalModulationPrbsOrder = None
    DigitalModulationPrbsSeed = None
    DigitalModulationSymbolRate = None
    DigitalModulationType = None
    DigitalModulationWaveformType = None
    DigitalPattern = None
    DirectDmaEnabled = None
    DirectDmaWindowAddress = None
    DirectDmaWindowSize = None
    DirectDownload = None
    DoneEventTerminalName = None
    DriverSetup = None
    DucFirFilterRaisedCosineAlpha = None
    DucFirFilterRootRaisedCosineAlpha = None
    DucFirFilterType = None
    DucPreFilterGain = None
    EventsDelay = None
    ExportedConfigurationListStepTriggerOutputTerminal = None
    ExportedConfigurationSettledEventOutputTerminal = None
    ExportedDoneEventOutputTerminal = None
    ExportedMarkerEventOutputTerminal = None
    ExportedRefClockOutputTerminal = None
    ExportedScriptTriggerOutputTerminal = None
    ExportedStartedEventOutputTerminal = None
    ExportedStartTriggerOutputTerminal = None
    ExternalCalibrationRecommendedInterval = None
    ExternalCalibrationTemperature = None
    ExternalCalibrationUserDefinedInfo = None
    ExternalCalibrationUserDefinedInfoMaxSize = None
    ExternalGain = None
    FastTuningOption = None
    FgenSession = None
    FpgaBitfilePath = None
    Frequency = None
    FrequencySettling = None
    FrequencySettlingUnits = None
    FrequencyTolerance = None
    FunctionCapabilities = None
    GenerationMode = None
    GroupCapabilities = None
    IfCarrierFrequency = None
    IfPower = None
    InstrumentFirmwareRevision = None
    InstrumentManufacturer = None
    InstrumentModel = None
    InterchangeCheck = None
    InterpolationDelay = None
    IOResourceDescriptor = None
    IqEnabled = None
    IqGainImbalance = None
    IqImpairmentEnabled = None
    IqIOffset = None
    IqNominalVoltage = None
    IqOffsetUnits = None
    IqOutPortCarrierFrequency = None
    IqOutPortCommonModeOffset = None
    IqOutPortLevel = None
    IqOutPortLoadImpedance = None
    IqOutPortOffset = None
    IqOutPortTemperature = None
    IqOutPortTerminalConfiguration = None
    IqQOffset = None
    IqRate = None
    IqSkew = None
    IqSwapEnabled = None
    LocalOscillatorOut0Enabled = None
    LoFrequencyStepSize = None
    LogicalName = None
    LoInPower = None
    LoopBandwidth = None
    LoOutEnabled = None
    LoOutPower = None
    LoPllFractionalModeEnabled = None
    LoSession = None
    LoSource = None
    LoTemperature = None
    MarkerEventTerminalName = None
    MemorySize = None
    ModuleRevision = None
    OutputEnabled = None
    OutputPort = None
    P2pDataTransferPermissionInterval = None
    P2pDataTransferPermissionitialCredits = None
    P2pEnabled = None
    P2pEndpointCount = None
    P2pEndpointFullnessStartTriggerLevel = None
    P2pEndpointSize = None
    P2pMostSpaceAvailableInEndpoint = None
    P2pSpaceAvailableInEndpoint = None
    PeakEnvelopePower = None
    PeakPowerAdjsutmentInheritance = None
    PeakPowerAdjustment = None
    PhaseContinuityEnabled = None
    PhaseOffset = None
    PowerLevel = None
    PowerLevelType = None
    PulseModulationEnabled = None
    PulseModulationMode = None
    PxiChassisClk10Source = None
    QueryInstrumentStatus = None
    RangeCheck = None
    RecordCoercions = None
    RefClockRate = None
    RefClockSource = None
    ReferenceOscillatorExternalFrequency = None
    ReferenceOscillatorSource = None
    RefPllBandwidth = None
    RfBlankingSource = None
    SampleClockRate = None
    ScriptTriggerTerminalName = None
    ScriptTriggerType = None
    SelectedScript = None
    SelfCalibrationTemperature = None
    SerialNumber = None
    SignalBandwidth = None
    Simulate = None
    SpecificDriverClassSpecMajorVersion = None
    SpecificDriverClassSpecMinorVersion = None
    SpecificDriverDescription = None
    SpecificDriverPrefix = None
    SpecificDriverRevision = None
    SpecificDriverVendor = None
    Spy = None
    StartedEventTerminalName = None
    StartTriggerTerminalName = None
    StartTriggerType = None
    StreamingEnabled = None
    StreamingSpaceAvailableInWaveform = None
    StreamingWaveformName = None
    StreamingWriteTimeout = None
    SupportedInstrumentModels = None
    SyncSampleClockDistLine = None
    SyncSampleClockMaster = None
    SyncScriptTriggerDistLine = None
    SyncScriptTriggerMaster = None
    SyncStartTriggerDistLine = None
    SyncStartTriggerMaster = None
    ThermalCorrectionEnabled = None
    TimerEventInterval = None
    UpconverterCenterFrequency = None
    UpconverterCenterFrequencyIncrement = None
    UpconverterCenterFrequencyIncrementAnchor = None
    UpconverterFrequencyOffset = None
    UpconverterGain = None
    UpconverterLoopBandwidth = None
    UpconverterTemperature = None
    UseSpecificSimulation = None
    value__ = None
    YigMainCoilDrive = None


class RfsgNIComplexI16(object):
    """ RfsgNIComplexI16(Real: Int16, Imaginary: Int16) """
    @staticmethod # known case of __new__
    def __new__(self, Real, Imaginary):
        """
        __new__[RfsgNIComplexI16]() -> RfsgNIComplexI16
        
        __new__(cls: type, Real: Int16, Imaginary: Int16)
        """
        pass

    Imaginary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Imaginary(self: RfsgNIComplexI16) -> Int16

"""

    Real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Real(self: RfsgNIComplexI16) -> Int16

"""



class RfsgNIComplexNumberF32(object):
    """ RfsgNIComplexNumberF32(Real: Single, Imaginary: Single) """
    @staticmethod # known case of __new__
    def __new__(self, Real, Imaginary):
        """
        __new__[RfsgNIComplexNumberF32]() -> RfsgNIComplexNumberF32
        
        __new__(cls: type, Real: Single, Imaginary: Single)
        """
        pass

    Imaginary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Imaginary(self: RfsgNIComplexNumberF32) -> Single

"""

    Real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Real(self: RfsgNIComplexNumberF32) -> Single

"""



class SmtSpectrumInfo(object):
    # no doc
    FFTSize = None
    linearDB = None
    spectrumType = None
    window = None
    windowSize = None


