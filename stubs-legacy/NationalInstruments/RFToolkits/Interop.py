# encoding: utf-8
# module NationalInstruments.RFToolkits.Interop calls itself Interop
# from NationalInstruments.RFToolkits.Interop.Fx40, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class niWLANA(object, IDisposable):
    """
    niWLANA(toolkitCompatibilityVersion: int)
    niWLANA(sessionName: str, toolkitCompatibilityVersion: int) -> int
    """
    def AnalyzeIQComplexF64(self, t0, dt, data, numberofSamples, reset, averagingDone):
        """ AnalyzeIQComplexF64(self: niWLANA, t0: float, dt: float, data: Array[niComplexNumber], numberofSamples: int, reset: int) -> (int, int) """
        pass

    def AnalyzeMIMOIQComplexF64(self, t0, dt, waveforms, numberofRxChains, numberofSamplesInEachWfm, reset, averagingDone):
        """ AnalyzeMIMOIQComplexF64(self: niWLANA, t0: Array[float], dt: Array[float], waveforms: Array[niComplexNumber], numberofRxChains: int, numberofSamplesInEachWfm: int, reset: int) -> (int, int) """
        pass

    def AnalyzeMIMOPowerSpectrum(self, f0, df, powerSpectra, numberofRxChains, numofSamplesInEachSpectrum):
        """ AnalyzeMIMOPowerSpectrum(self: niWLANA, f0: Array[float], df: Array[float], powerSpectra: Array[float], numberofRxChains: int, numofSamplesInEachSpectrum: int) -> int """
        pass

    def AnalyzePowerSpectrum(self, f0, df, powerSpectrumData, dataArraySize):
        """ AnalyzePowerSpectrum(self: niWLANA, f0: float, df: float, powerSpectrumData: Array[float], dataArraySize: int) -> int """
        pass

    def AutoDetectionOfStandard(self, rfsaSession, hwChannelString):
        """ AutoDetectionOfStandard(self: niWLANA, rfsaSession: HandleRef, hwChannelString: str) -> int """
        pass

    def ChannelNumberToCarrierFrequency(self, frequencyBand, channelBandwidth, channelNumber, secondaryFactor, channelStartingFactor, carrierFrequency):
        """ ChannelNumberToCarrierFrequency(self: niWLANA, frequencyBand: int, channelBandwidth: float, channelNumber: int, secondaryFactor: int, channelStartingFactor: float) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211abgjpn(self, channelStartingFrequency, channelBandwidth, channelNumber, secondaryFactor, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211abgjpn(self: niWLANA, channelStartingFrequency: float, channelBandwidth: float, channelNumber: int, secondaryFactor: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211ac(self, channelStartingFrequencyHz, channelNumber, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211ac(self: niWLANA, channelStartingFrequencyHz: float, channelNumber: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211af(self, channelStartingFrequency, channelBandwidth, channelNumber, TVHTMode, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211af(self: niWLANA, channelStartingFrequency: float, channelBandwidth: float, channelNumber: int, TVHTMode: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211ah(self, channelStartingFrequencyHz, channelNumber, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211ah(self: niWLANA, channelStartingFrequencyHz: float, channelNumber: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211ax(self, channelStartingFrequency, channelBandwidth, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211ax(self: niWLANA, channelStartingFrequency: float, channelBandwidth: float) -> (int, float) """
        pass

    def Close(self):
        """ Close(self: niWLANA) """
        pass

    def ConfigureFastEVM(self, standard, channelBandwidth):
        """ ConfigureFastEVM(self: niWLANA, standard: int, channelBandwidth: float) -> int """
        pass

    def DeallocateMemory(self):
        """ DeallocateMemory(self: niWLANA) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: niWLANA) """
        pass

    def Get80211AcAmpduEnabled(self, channelString, value):
        """ Get80211AcAmpduEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAcpEnabled(self, channel, value):
        """ GetAcpEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetAcpLowerAbsolutePower(self, channelString, dataArray, dataArraySize, actualArraySize):
        """ GetAcpLowerAbsolutePower(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAcpLowerRelativePower(self, channelString, dataArray, dataArraySize, actualArraySize):
        """ GetAcpLowerRelativePower(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAcpNumberOfAverages(self, channel, value):
        """ GetAcpNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetAcpNumberOfOffsets(self, channel, value):
        """ GetAcpNumberOfOffsets(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetAcpReferenceChannelPower(self, channel, value):
        """ GetAcpReferenceChannelPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetACPTrace(self, channelString, f0, df, y, dataArraySize, actualArraySize):
        """ GetACPTrace(self: niWLANA, channelString: str, y: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetAcpTraceEnabled(self, channel, value):
        """ GetAcpTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetAcpUpperAbsolutePower(self, channelString, dataArray, dataArraySize, actualArraySize):
        """ GetAcpUpperAbsolutePower(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAcpUpperRelativePower(self, channelString, dataArray, dataArraySize, actualArraySize):
        """ GetAcpUpperRelativePower(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAcquisitionLength(self, channel, value):
        """ GetAcquisitionLength(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetAggregationBit(self, channelString, value):
        """ GetAggregationBit(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMAMPolynomialCoefficients(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetAMAMPolynomialCoefficients(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAmplitudeCorrectionEnabled(self, channelString, value):
        """ GetAmplitudeCorrectionEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAmplitudeCorrectionTable(self, channelString, index, isTableIndex, amplitudeCorrection, frequency, dataArraySize, actualArraySize):
        """ GetAmplitudeCorrectionTable(self: niWLANA, channelString: str, index: int, isTableIndex: int, amplitudeCorrection: Array[float], frequency: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAMPMMeasurements1dbCompressionPoint(self, channelString, value):
        """ GetAMPMMeasurements1dbCompressionPoint(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsAllTracesEnabled(self, channelString, value):
        """ GetAMPMMeasurementsAllTracesEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsAMAMCurveFitTraceEnabled(self, channelString, value):
        """ GetAMPMMeasurementsAMAMCurveFitTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsAMAMResidual(self, channelString, value):
        """ GetAMPMMeasurementsAMAMResidual(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsAMAMTraceEnabled(self, channelString, value):
        """ GetAMPMMeasurementsAMAMTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsAMPMCurveFitTraceEnabled(self, channelString, value):
        """ GetAMPMMeasurementsAMPMCurveFitTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsAMPMResidual(self, channelString, value):
        """ GetAMPMMeasurementsAMPMResidual(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsAMPMTraceEnabled(self, channelString, value):
        """ GetAMPMMeasurementsAMPMTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsAverageGain(self, channelString, value):
        """ GetAMPMMeasurementsAverageGain(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsAveragePhaseError(self, channelString, value):
        """ GetAMPMMeasurementsAveragePhaseError(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsAveragingMode(self, channelString, value):
        """ GetAMPMMeasurementsAveragingMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsDUTInputPowerLevel(self, channelString, value):
        """ GetAMPMMeasurementsDUTInputPowerLevel(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsEnabled(self, channelString, value):
        """ GetAMPMMeasurementsEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsGainErrorRange(self, channelString, value):
        """ GetAMPMMeasurementsGainErrorRange(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsMaximumInputPower(self, channelString, value):
        """ GetAMPMMeasurementsMaximumInputPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsMeanAcquiredWaveformTraceEnabled(self, channelString, value):
        """ GetAMPMMeasurementsMeanAcquiredWaveformTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAmpmMeasurementsMeasurementInterval(self, channelString, value):
        """ GetAmpmMeasurementsMeasurementInterval(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsMeasurementLength(self, channelString, value):
        """ GetAMPMMeasurementsMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsMinimumInputPower(self, channelString, value):
        """ GetAMPMMeasurementsMinimumInputPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsNumberOfAverages(self, channelString, value):
        """ GetAMPMMeasurementsNumberOfAverages(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMMeasurementsPhaseErrorRange(self, channelString, value):
        """ GetAMPMMeasurementsPhaseErrorRange(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAMPMMeasurementsProcessedReferenceWaveformTraceEnabled(self, channelString, value):
        """ GetAMPMMeasurementsProcessedReferenceWaveformTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetAMPMPolynomialCoefficients(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetAMPMPolynomialCoefficients(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetAttributeString(self, channelString, attributeID, attributeValue, bufferSize, actualStringSize):
        """ GetAttributeString(self: niWLANA, channelString: str, attributeID: niWLANAProperties, attributeValue: str, bufferSize: int) -> (int, int) """
        pass

    def GetAutoDetectionOfStandardMode(self, channel, value):
        """ GetAutoDetectionOfStandardMode(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetAutoRangeAcquisitionLength(self, channelString, value):
        """ GetAutoRangeAcquisitionLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAutorangeMaxAcquisitionLength(self, channel, value):
        """ GetAutorangeMaxAcquisitionLength(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetAutorangeMaxIdleTime(self, channel, value):
        """ GetAutorangeMaxIdleTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetAutoRangeMaxInputPower(self, channelString, value):
        """ GetAutoRangeMaxInputPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAutoRangeMaxInputRange(self, channelString, value):
        """ GetAutoRangeMaxInputRange(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetAutoSpanEnabled(self, channel, value):
        """ GetAutoSpanEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetCarrierFrequency(self, channel, value):
        """ GetCarrierFrequency(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetCCDF10PercentPower(self, channelString, value):
        """ GetCCDF10PercentPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDF1By10000PercentPower(self, channelString, value):
        """ GetCCDF1By10000PercentPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDF1By1000PercentPower(self, channelString, value):
        """ GetCCDF1By1000PercentPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDF1By100PercentPower(self, channelString, value):
        """ GetCCDF1By100PercentPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDF1By10PercentPower(self, channelString, value):
        """ GetCCDF1By10PercentPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDF1PercentPower(self, channelString, value):
        """ GetCCDF1PercentPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDFAveragePower(self, channelString, value):
        """ GetCCDFAveragePower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDFAveragePowerPercentile(self, channelString, value):
        """ GetCCDFAveragePowerPercentile(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDFEnabled(self, channelString, value):
        """ GetCCDFEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetCCDFMeasurementLength(self, channelString, value):
        """ GetCCDFMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDFNumberOfRecords(self, channelString, value):
        """ GetCCDFNumberOfRecords(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetCCDFPeakToAveragePowerRatio(self, channelString, value):
        """ GetCCDFPeakToAveragePowerRatio(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDFRemoveDeadTime(self, channelString, value):
        """ GetCCDFRemoveDeadTime(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetCCDFResultantCount(self, channelString, value):
        """ GetCCDFResultantCount(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetCCDFTrace(self, channelString, signalCcdfMinBin, signalCcdfBinSize, signalCcdf, signalCcdfDataArraySize, signalCcdfActualArraySize, guassianCcdfBinSize, guassianCcdfMinSize, gaussianCcdf, gaussianCcdfDataArraySize, gaussianCcdfActualArraySize):
        """ GetCCDFTrace(self: niWLANA, channelString: str, signalCcdf: Array[float], signalCcdfDataArraySize: int, gaussianCcdf: Array[float], gaussianCcdfDataArraySize: int) -> (int, float, float, int, float, float, int) """
        pass

    def GetCCDFTraceEnabled(self, channelString, value):
        """ GetCCDFTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetChannelBandwidth(self, channel, value):
        """ GetChannelBandwidth(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetCompatibilityVersion(self, channel, value):
        """ GetCompatibilityVersion(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetCurrentIterationConstellation(self, channelString, iData, qData, dataArraySize, actualNumDataArrayElements):
        """ GetCurrentIterationConstellation(self: niWLANA, channelString: str, iData: Array[float], qData: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationConstellationTrace(self, channelString, iData, qData, dataArraySize, actualArraySize):
        """ GetCurrentIterationConstellationTrace(self: niWLANA, channelString: str, iData: Array[float], qData: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationDecodedBitsTrace(self, decodedbits, dataArraySize, actualArraySize):
        """ GetCurrentIterationDecodedBitsTrace(self: niWLANA, decodedbits: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationDecodedHeaderBitsTrace80211ac(self, channelString, decodedLSIGBitsTrace, actualDecodedLSIGBitsTraceSize, decodedVHTSIGABitsTrace, actualDecodedVHTSIGABitsTraceSize, decodedVHTSIGBBitsTrace, actualDecodedVHTSIGBBitsTraceSize):
        """ GetCurrentIterationDecodedHeaderBitsTrace80211ac(self: niWLANA, channelString: str, decodedLSIGBitsTrace: Array[int], decodedVHTSIGABitsTrace: Array[int], decodedVHTSIGBBitsTrace: Array[int]) -> (int, int, int, int) """
        pass

    def GetCurrentIterationDecodedHeaderBitsTrace80211agjp(self, channelString, decodedSignalBitsTrace, actualdecodedSignalBitsTrace):
        """ GetCurrentIterationDecodedHeaderBitsTrace80211agjp(self: niWLANA, channelString: str, decodedSignalBitsTrace: Array[int]) -> (int, int) """
        pass

    def GetCurrentIterationDecodedHeaderBitsTrace80211ax(self, channelString, decodedHESIGABitsTrace, actualDecodedHESIGABitsTraceSize, decodedHESIGBBitsTrace, actualdecodedHESIGBBitsTraceSize, decodedLSIGBitsTrace, actualDecodedLSIGBitsTraceSize):
        """ GetCurrentIterationDecodedHeaderBitsTrace80211ax(self: niWLANA, channelString: str, decodedHESIGABitsTrace: Array[int], decodedHESIGBBitsTrace: Array[int], decodedLSIGBitsTrace: Array[int]) -> (int, int, int, int) """
        pass

    def GetCurrentIterationDecodedHeaderBitsTrace80211n(self, channelString, decodedHTSIGBitsTrace, actualDecodedHTSIGBitsTraceSize, decodedLSIGBitsTrace, actualdecodedLSIGBitsTrace):
        """ GetCurrentIterationDecodedHeaderBitsTrace80211n(self: niWLANA, channelString: str, decodedHTSIGBitsTrace: Array[int], decodedLSIGBitsTrace: Array[int]) -> (int, int, int) """
        pass

    def GetCurrentIterationEVMPerSymbol(self, channelString, eVMperSymbol, eVMperSymbolArraySize, actualArraySize):
        """ GetCurrentIterationEVMPerSymbol(self: niWLANA, channelString: str, eVMperSymbol: Array[float], eVMperSymbolArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationEVMPerSymbolTrace(self, channelString, index, eVMperSymbol, dataArraySize, actualArraySize):
        """ GetCurrentIterationEVMPerSymbolTrace(self: niWLANA, channelString: str, index: Array[int], eVMperSymbol: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodChannelFrequencyResponseTrace(self, channelString, index, magnitude, phase, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodChannelFrequencyResponseTrace(self: niWLANA, channelString: str, index: Array[int], magnitude: Array[float], phase: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodCommonPilotErrorTrace(self, channelString, index, CPEMagnitude, CPEPhase, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodCommonPilotErrorTrace(self: niWLANA, channelString: str, index: Array[int], CPEMagnitude: Array[float], CPEPhase: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodDataEVMPerSymbolTrace(self, channelString, index, dataEVMperSymbol, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodDataEVMPerSymbolTrace(self: niWLANA, channelString: str, index: Array[int], dataEVMperSymbol: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodEVMPerSubcarrierTrace(self, channelString, index, eVMperSubcarrier, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodEVMPerSubcarrierTrace(self: niWLANA, channelString: str, index: Array[int], eVMperSubcarrier: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodEVMPerSymbolPerSubcarrierTrace(self, channelString, index, eVMTrace, numRows, numColumns, actualNumRows, actualNumColumns):
        """ GetCurrentIterationOFDMDemodEVMPerSymbolPerSubcarrierTrace(self: niWLANA, channelString: str, index: Array[int], numRows: int, numColumns: int) -> (int, float, int, int) """
        pass

    def GetCurrentIterationOfdmDemodIQGainImbalancePerSubcarrierTrace(self, channelString, IQGainImbalance, subcarrierIndices, dataArraySize, actualArraySize):
        """ GetCurrentIterationOfdmDemodIQGainImbalancePerSubcarrierTrace(self: niWLANA, channelString: str, IQGainImbalance: Array[float], subcarrierIndices: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodNumberOfSpaceTimeStreams(self, channelString, numStreams):
        """ GetCurrentIterationOFDMDemodNumberOfSpaceTimeStreams(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodNumberOfSpatialStreams(self, channelString, numStreams):
        """ GetCurrentIterationOFDMDemodNumberOfSpatialStreams(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodPhaseNoisePSDTrace(self, channelString, f0, df, phaseNoisePSD, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodPhaseNoisePSDTrace(self: niWLANA, channelString: str, phaseNoisePSD: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetCurrentIterationOFDMDemodPilotEVMPerSymbolTrace(self, channelString, index, pilotEVMperSymbol, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodPilotEVMPerSymbolTrace(self: niWLANA, channelString: str, index: Array[int], pilotEVMperSymbol: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMDemodPreambleFrequencyErrorTrace(self, channelString, time, preambleFrequencyError, dataArraySize, actualArraySize):
        """ GetCurrentIterationOFDMDemodPreambleFrequencyErrorTrace(self: niWLANA, channelString: str, time: Array[float], preambleFrequencyError: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOfdmDemodQuadratureSkewPerSubcarrierTrace(self, channelString, quadratureSkew, subcarrierIndices, dataArraySize, actualArraySize):
        """ GetCurrentIterationOfdmDemodQuadratureSkewPerSubcarrierTrace(self: niWLANA, channelString: str, quadratureSkew: Array[float], subcarrierIndices: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMEVMPerSubcarrier(self, channelString, eVMperSubcarrier, eVMperSubcarrierArraySize, actualArraySize):
        """ GetCurrentIterationOFDMEVMPerSubcarrier(self: niWLANA, channelString: str, eVMperSubcarrier: Array[float], eVMperSubcarrierArraySize: int) -> (int, int) """
        pass

    def GetCurrentIterationOFDMEVMPerSymbolPerSubcarrier(self, channelString, eVMTrace, numRows, numColumns, actualNumRows, actualNumColumns):
        """ GetCurrentIterationOFDMEVMPerSymbolPerSubcarrier(self: niWLANA, channelString: str, numRows: int, numColumns: int) -> (int, float, int, int) """
        pass

    def GetCurrentIterationPvT(self, channelString, t0, dt, data, dataArraySize, actualNumDataArrayElements):
        """ GetCurrentIterationPvT(self: niWLANA, channelString: str, data: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetCurrentIterationPvTTrace(self, channelString, t0, dt, pvT, dataArraySize, actualArraySize):
        """ GetCurrentIterationPvTTrace(self: niWLANA, channelString: str, pvT: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetCurrentIterationReferenceConstellationTrace(self, channelString, I, Q, dataArraySize, actualArraySize):
        """ GetCurrentIterationReferenceConstellationTrace(self: niWLANA, channelString: str, I: Array[float], Q: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetDetectedChannelBandwidth(self, channel, value):
        """ GetDetectedChannelBandwidth(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDetectedStandard(self, channel, value):
        """ GetDetectedStandard(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDeviceInstantaneousBandwidth(self, channel, value):
        """ GetDeviceInstantaneousBandwidth(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssDataRate(self, channel, value):
        """ GetDsssDataRate(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodAllTracesEnabled(self, channel, value):
        """ GetDsssDemodAllTracesEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodAutoComputeAcquisitionLengthEnabled(self, channel, value):
        """ GetDSSSDemodAutoComputeAcquisitionLengthEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodAutoComputeMeasurementLengthEnabled(self, channelString, value):
        """ GetDSSSDemodAutoComputeMeasurementLengthEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetDSSSDemodBurstStartDetectionEnabled(self, channel, value):
        """ GetDSSSDemodBurstStartDetectionEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodBurstStartTime(self, channelString, value):
        """ GetDSSSDemodBurstStartTime(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetDSSSDemodCarrierFrequencyOffset(self, channelString, carrierFrequencyOffset):
        """ GetDSSSDemodCarrierFrequencyOffset(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetDSSSDemodCarrierFrequencyOffsetEstimationEnabled(self, channel, value):
        """ GetDSSSDemodCarrierFrequencyOffsetEstimationEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodCarrierSuppressionEstimationEnabled(self, channel, value):
        """ GetDSSSDemodCarrierSuppressionEstimationEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodConstellationTraceEnabled(self, channel, value):
        """ GetDsssDemodConstellationTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodDecodedBitsTraceEnabled(self, channel, value):
        """ GetDsssDemodDecodedBitsTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodEnabled(self, channel, value):
        """ GetDsssDemodEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodEqualizationEnabled(self, channel, value):
        """ GetDsssDemodEqualizationEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodEvmPerChipTraceEnabled(self, channel, value):
        """ GetDsssDemodEvmPerChipTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodEvmPerSymbolTraceEnabled(self, channel, value):
        """ GetDsssDemodEvmPerSymbolTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodGatedPowerDataPowerEnabled(self, channel, value):
        """ GetDsssDemodGatedPowerDataPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodGatedPowerEnabled(self, channel, value):
        """ GetDsssDemodGatedPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodGatedPowerPreambleAndHeaderPowerEnabled(self, channel, value):
        """ GetDsssDemodGatedPowerPreambleAndHeaderPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodGatedPowerStartTime(self, channel, value):
        """ GetDsssDemodGatedPowerStartTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssDemodGatedPowerStopTime(self, channel, value):
        """ GetDsssDemodGatedPowerStopTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssDemodGatedPowerTotalPacketPowerEnabled(self, channel, value):
        """ GetDsssDemodGatedPowerTotalPacketPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodHeaderDetectionEnabled(self, channel, value):
        """ GetDsssDemodHeaderDetectionEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodIQGainImbalanceEstimationEnabled(self, channel, value):
        """ GetDSSSDemodIQGainImbalanceEstimationEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodLowpassFilteringEnabled(self, channel, value):
        """ GetDsssDemodLowpassFilteringEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodMacFrameCheckSequenceCheckEnabled(self, channel, value):
        """ GetDsssDemodMacFrameCheckSequenceCheckEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodMaximumChipsUsed(self, channel, value):
        """ GetDsssDemodMaximumChipsUsed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodMeasurementLength(self, channelString, value):
        """ GetDSSSDemodMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetDsssDemodMeasurementStartLocation(self, channel, value):
        """ GetDsssDemodMeasurementStartLocation(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodNumberOfAverages(self, channel, value):
        """ GetDsssDemodNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodPhaseTracking(self, channel, value):
        """ GetDsssDemodPhaseTracking(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodQuadratureSkewEstimationEnabled(self, channel, value):
        """ GetDSSSDemodQuadratureSkewEstimationEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodReferencePulseShapingFilterCoefficient(self, channel, value):
        """ GetDsssDemodReferencePulseShapingFilterCoefficient(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssDemodReferencePulseShapingFilterType(self, channel, value):
        """ GetDsssDemodReferencePulseShapingFilterType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSDemodSampleClockOffsetEstimationEnabled(self, channel, value):
        """ GetDSSSDemodSampleClockOffsetEstimationEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodUserDefinedGatePowerEnabled(self, channel, value):
        """ GetDsssDemodUserDefinedGatePowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssDemodUserDefinedGateStartTime(self, channel, value):
        """ GetDsssDemodUserDefinedGateStartTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssDemodUserDefinedGateStopTime(self, channel, value):
        """ GetDsssDemodUserDefinedGateStopTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssPayloadLength(self, channel, value):
        """ GetDsssPayloadLength(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssPowerRampDownHighThreshold(self, channel, value):
        """ GetDsssPowerRampDownHighThreshold(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssPowerRampDownLowThreshold(self, channel, value):
        """ GetDsssPowerRampDownLowThreshold(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssPowerRampMeasurementEnabled(self, channel, value):
        """ GetDsssPowerRampMeasurementEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDSSSPowerRampMeasurementLength(self, channelString, value):
        """ GetDSSSPowerRampMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetDsssPowerRampMeasurementNumberOfAverages(self, channel, value):
        """ GetDsssPowerRampMeasurementNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetDsssPowerRampUpHighThreshold(self, channel, value):
        """ GetDsssPowerRampUpHighThreshold(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDsssPowerRampUpLowThreshold(self, channel, value):
        """ GetDsssPowerRampUpLowThreshold(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetDualCarrierModulationEnabled(self, channelString, value):
        """ GetDualCarrierModulationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetErrorString(self, status, msg):
        """ GetErrorString(self: niWLANA, status: int, msg: StringBuilder) -> int """
        pass

    def GetETSIIBEDeltaACLR(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetETSIIBEDeltaACLR(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetETSIIBEDeltaACLRMarginFrequencyVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetETSIIBEDeltaACLRMarginFrequencyVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetETSIIBEDeltaACLRMarginVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetETSIIBEDeltaACLRMarginVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetETSIIBEDeviceEmissionClass(self, channelString, value):
        """ GetETSIIBEDeviceEmissionClass(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetETSIIBEDUTAverageOutputPower(self, channelString, value):
        """ GetETSIIBEDUTAverageOutputPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetETSIIBEEnabled(self, channelString, value):
        """ GetETSIIBEEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetETSIIBEMargin(self, channelString, value):
        """ GetETSIIBEMargin(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetETSIIBEMarginFrequencyVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetETSIIBEMarginFrequencyVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetETSIIBEMarginVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetETSIIBEMarginVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetETSIIBENumberOfAverages(self, channelString, value):
        """ GetETSIIBENumberOfAverages(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetETSIIBENumberOfOffsets(self, channelString, value):
        """ GetETSIIBENumberOfOffsets(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetETSIIBETrace(self, f0, df, relativeLimits, absoluteLimits, PSD, dataArraySize, actualDataArraySize):
        """ GetETSIIBETrace(self: niWLANA, relativeLimits: Array[float], absoluteLimits: Array[float], PSD: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetETSIIBETraceEnabled(self, channelString, value):
        """ GetETSIIBETraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetETSIIBETransmitChannelPSDLimit(self, channelString, value):
        """ GetETSIIBETransmitChannelPSDLimit(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetETSIIBEViolation(self, channelString, value):
        """ GetETSIIBEViolation(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetFecCodingType(self, channel, value):
        """ GetFecCodingType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetFftSize(self, channel, value):
        """ GetFftSize(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetFftWindowSize(self, channel, value):
        """ GetFftWindowSize(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetFftWindowType(self, channel, value):
        """ GetFftWindowType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetGatedSpectrumAveragingType(self, channelString, value):
        """ GetGatedSpectrumAveragingType(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetGatedSpectrumEnabled(self, channel, value):
        """ GetGatedSpectrumEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetGatedSpectrumMeasurementLength(self, channelString, value):
        """ GetGatedSpectrumMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetGatedSpectrumMode(self, channel, value):
        """ GetGatedSpectrumMode(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetGuardInterval(self, channel, value):
        """ GetGuardInterval(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetGuardIntervalType(self, channel, value):
        """ GetGuardIntervalType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetHELTFSize(self, channelString, value):
        """ GetHELTFSize(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetHESIGBDCMEnabled(self, channelString, value):
        """ GetHESIGBDCMEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetHESIGBMCSIndex(self, channelString, value):
        """ GetHESIGBMCSIndex(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetIqPowerEdgeReferenceTriggerEnabled(self, channel, value):
        """ GetIqPowerEdgeReferenceTriggerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetIQPowerEdgeReferenceTriggerEnabled(self, channelString, value):
        """ GetIQPowerEdgeReferenceTriggerEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetLDPCExtraSymbolUsed(self, channelString, value):
        """ GetLDPCExtraSymbolUsed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetLOFrequencyOffset(self, channelString, value):
        """ GetLOFrequencyOffset(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetLOOffsetMode(self, channelString, value):
        """ GetLOOffsetMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetLOSharingEnabled(self, channelString, value):
        """ GetLOSharingEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetMaxInputPower(self, channel, value):
        """ GetMaxInputPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetMaxSpectralDensityEnabled(self, channel, value):
        """ GetMaxSpectralDensityEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetMaxSpectralDensityNumberOfAverages(self, channel, value):
        """ GetMaxSpectralDensityNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetMcsIndex(self, channel, value):
        """ GetMcsIndex(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetMidamblePeriodicity(self, channelString, value):
        """ GetMidamblePeriodicity(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetMultiSegmentMeasurementMode(self, channelString, value):
        """ GetMultiSegmentMeasurementMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetMUMimoLtfModeEnabled(self, channelString, value):
        """ GetMUMimoLtfModeEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetNoiseCompensationCarrierFrequencies(self, channelString, dataArray, actualNumDataArrayElements):
        """ GetNoiseCompensationCarrierFrequencies(self: niWLANA, channelString: str, dataArray: Array[float]) -> (int, int) """
        pass

    def GetNoiseCompensationEnabled(self, channelString, value):
        """ GetNoiseCompensationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetNoiseCompensationMaxChannelBandwidths(self, channelString, dataArray, actualNumDataArrayElements):
        """ GetNoiseCompensationMaxChannelBandwidths(self: niWLANA, channelString: str, dataArray: Array[float]) -> (int, int) """
        pass

    def GetNoiseCompensationMaximumReferenceLevel(self, channelString, value):
        """ GetNoiseCompensationMaximumReferenceLevel(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetNoiseCompensationMinimumReferenceLevel(self, channelString, value):
        """ GetNoiseCompensationMinimumReferenceLevel(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetNoiseCompensationReferenceLevelStepSize(self, channelString, value):
        """ GetNoiseCompensationReferenceLevelStepSize(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetNonHTModulationMode(self, channelString, value):
        """ GetNonHTModulationMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetNumberOfExtensionSpatialStreams(self, channel, value):
        """ GetNumberOfExtensionSpatialStreams(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetNumberOfHELTFSymbols(self, channelString, value):
        """ GetNumberOfHELTFSymbols(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetNumberOfHESIGBSymbols(self, channelString, value):
        """ GetNumberOfHESIGBSymbols(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetNumberOfIterations(self, channel, value):
        """ GetNumberOfIterations(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetNumberOfReceiveChannels(self, channel, value):
        """ GetNumberOfReceiveChannels(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetNumberOfSegments(self, channelString, value):
        """ GetNumberOfSegments(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetNumberOfSpaceTimeStreams(self, channelString, value):
        """ GetNumberOfSpaceTimeStreams(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetObw(self, channelString, value):
        """ GetObw(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetObwEnabled(self, channel, value):
        """ GetObwEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetObwNumberOfAverages(self, channel, value):
        """ GetObwNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMChannelEstimationOnLLTFEnabled(self, channelString, value):
        """ GetOFDMChannelEstimationOnLLTFEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDataRate(self, channel, value):
        """ GetOfdmDataRate(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemod80211ahPreambleDetectionEnabled(self, channel, value):
        """ GetOfdmDemod80211ahPreambleDetectionEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemod80211ahPreambleType(self, channel, value):
        """ GetOfdmDemod80211ahPreambleType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemod80211nPlcpFrameDetectionEnabled(self, channel, value):
        """ GetOfdmDemod80211nPlcpFrameDetectionEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemod80Plus80FilterBeforeSyncEnabled(self, channel, value):
        """ GetOfdmDemod80Plus80FilterBeforeSyncEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemod80Plus80OversamplingFactor(self, channel, value):
        """ GetOfdmDemod80Plus80OversamplingFactor(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetOFDMDemod80Plus80SegmentIndex(self, channelString, value):
        """ GetOFDMDemod80Plus80SegmentIndex(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodAbsoluteCarrierFrequencyLeakageAverage(self, channelString, value):
        """ GetOFDMDemodAbsoluteCarrierFrequencyLeakageAverage(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodAbsoluteCarrierFrequencyLeakageMaximum(self, channelString, value):
        """ GetOFDMDemodAbsoluteCarrierFrequencyLeakageMaximum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodAbsoluteCarrierFrequencyLeakageMinimum(self, channelString, value):
        """ GetOFDMDemodAbsoluteCarrierFrequencyLeakageMinimum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodAbsoluteCarrierFrequencyLeakageStandardDeviation(self, channelString, value):
        """ GetOFDMDemodAbsoluteCarrierFrequencyLeakageStandardDeviation(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodAggregation(self, channelString, value):
        """ GetOFDMDemodAggregation(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodAllTracesEnabled(self, channel, value):
        """ GetOfdmDemodAllTracesEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodAmplitudeTrackingEnabled(self, channel, value):
        """ GetOfdmDemodAmplitudeTrackingEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodAutoComputeAcquisitionLengthEnabled(self, channel, value):
        """ GetOfdmDemodAutoComputeAcquisitionLengthEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodAutoComputeMeasurementLengthEnabled(self, channelString, value):
        """ GetOFDMDemodAutoComputeMeasurementLengthEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodBurstStartDetectionEnabled(self, channelString, value):
        """ GetOfdmDemodBurstStartDetectionEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodBurstStartTime(self, channelString, value):
        """ GetOFDMDemodBurstStartTime(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodCarrierFrequencyLeakageEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodCarrierFrequencyLeakageEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodCarrierFrequencyOffsetCCDFTenPercent(self, channelString, value):
        """ GetOFDMDemodCarrierFrequencyOffsetCCDFTenPercent(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodCarrierFrequencyOffsetCCDFTrace(self, channelString, minBin, binSize, CCDF, actualCCDFArraySize):
        """ GetOFDMDemodCarrierFrequencyOffsetCCDFTrace(self: niWLANA, channelString: str, CCDF: Array[float]) -> (int, float, float, int) """
        pass

    def GetOFDMDemodCarrierFrequencyOffsetCCDFTraceEnabled(self, channelString, value):
        """ GetOFDMDemodCarrierFrequencyOffsetCCDFTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodCarrierFrequencyOffsetEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodCarrierFrequencyOffsetEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodCfoEstimationMethod(self, channel, value):
        """ GetOfdmDemodCfoEstimationMethod(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodChannelEstimationMethod(self, channelString, value):
        """ GetOFDMDemodChannelEstimationMethod(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodChannelEVMEnabled(self, channelString, value):
        """ GetOFDMDemodChannelEVMEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodChannelFrequencyResponseTraceEnabled(self, channel, value):
        """ GetOfdmDemodChannelFrequencyResponseTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodChannelFrequencyResponseTraceMode(self, channel, value):
        """ GetOfdmDemodChannelFrequencyResponseTraceMode(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodChannelMatrixPowerEnabled(self, channelString, value):
        """ GetOFDMDemodChannelMatrixPowerEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodChannelTrackingEnabled(self, channel, value):
        """ GetOfdmDemodChannelTrackingEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodCombinedSignalDemodulationEnabled(self, channelString, value):
        """ GetOfdmDemodCombinedSignalDemodulationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodCommonClockSourceEnabled(self, channel, value):
        """ GetOFDMDemodCommonClockSourceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodCommonPhaseErrorEstimationEnabled(self, channelString, value):
        """ GetOfdmDemodCommonPhaseErrorEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodCommonPilotErrorEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodCommonPilotErrorEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodCommonPilotErrorRMS(self, channelString, value):
        """ GetOFDMDemodCommonPilotErrorRMS(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodCommonPilotErrorTraceEnabled(self, channelString, value):
        """ GetOFDMDemodCommonPilotErrorTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodConstellationTraceEnabled(self, channel, value):
        """ GetOfdmDemodConstellationTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodDataEvmPerSymbolTraceEnabled(self, channel, value):
        """ GetOfdmDemodDataEvmPerSymbolTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodDCMEnabled(self, channelString, value):
        """ GetOFDMDemodDCMEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodDecodedBitsTraceEnabled(self, channel, value):
        """ GetOfdmDemodDecodedBitsTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodDecodedHeaderTraceEnabled(self, channelString, value):
        """ GetOFDMDemodDecodedHeaderTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodEnabled(self, channel, value):
        """ GetOfdmDemodEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodEvmPerSubcarrierPerSymbolTraceEnabled(self, channel, value):
        """ GetOfdmDemodEvmPerSubcarrierPerSymbolTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodEvmPerSubcarrierTraceEnabled(self, channel, value):
        """ GetOfdmDemodEvmPerSubcarrierTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodEvmPerSymbolPerSubcarrierTraceEnabled(self, channel, value):
        """ GetOfdmDemodEvmPerSymbolPerSubcarrierTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodEvmPerSymbolTraceEnabled(self, channel, value):
        """ GetOfdmDemodEvmPerSymbolTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodFECCodingType(self, channelString, value):
        """ GetOFDMDemodFECCodingType(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodGatedPowerDataPowerEnabled(self, channel, value):
        """ GetOfdmDemodGatedPowerDataPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodGatedPowerEnabled(self, channel, value):
        """ GetOfdmDemodGatedPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodGatedPowerPreambleAndHeaderPowerEnabled(self, channel, value):
        """ GetOfdmDemodGatedPowerPreambleAndHeaderPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodGatedPowerStartTime(self, channel, value):
        """ GetOfdmDemodGatedPowerStartTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetOfdmDemodGatedPowerStopTime(self, channel, value):
        """ GetOfdmDemodGatedPowerStopTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetOfdmDemodGatedPowerTotalPacketPowerEnabled(self, channel, value):
        """ GetOfdmDemodGatedPowerTotalPacketPowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodGroupDelayTraceEnabled(self, channel, value):
        """ GetOfdmDemodGroupDelayTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodGroupDelayTraceMode(self, channel, value):
        """ GetOfdmDemodGroupDelayTraceMode(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodGuardIntervalType(self, channel, value):
        """ GetOfdmDemodGuardIntervalType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodHeaderDetectionEnabled(self, channel, value):
        """ GetOfdmDemodHeaderDetectionEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodHELTFSize(self, channelString, value):
        """ GetOFDMDemodHELTFSize(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodHESIGACRCPassed(self, channelString, value):
        """ GetOFDMDemodHESIGACRCPassed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodHESIGBCRCPassed(self, channelString, value):
        """ GetOFDMDemodHESIGBCRCPassed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodHESIGBDualCarrierModulationEnabled(self, channelString, value):
        """ GetOFDMDemodHESIGBDualCarrierModulationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodHESIGBMCSIndex(self, channelString, value):
        """ GetOFDMDemodHESIGBMCSIndex(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodIQGainImbalance(self, channelString, value):
        """ GetOfdmDemodIQGainImbalance(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodIQGainImbalanceCompensationEnabled(self, channelString, value):
        """ GetOFDMDemodIQGainImbalanceCompensationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodIQGainImbalanceEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodIQGainImbalanceEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodIQGainImbalancePerSubcarrierTraceEnabled(self, channelString, value):
        """ GetOFDMDemodIQGainImbalancePerSubcarrierTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodIQImpairmentsCompensationEnabled(self, channelString, value):
        """ GetOfdmDemodIQImpairmentsCompensationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodIQImpairmentsPerSubcarrierEnabled(self, channelString, value):
        """ GetOfdmDemodIQImpairmentsPerSubcarrierEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodIQMismatchSignalModel(self, channelString, value):
        """ GetOFDMDemodIQMismatchSignalModel(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodLDPCExtraSymbol(self, channelString, value):
        """ GetOFDMDemodLDPCExtraSymbol(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodLowpassFilteringEnabled(self, channel, value):
        """ GetOfdmDemodLowpassFilteringEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodLSIGPayloadLength(self, channelString, value):
        """ GetOFDMDemodLSIGPayloadLength(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodMacFrameCheckSequenceCheckEnabled(self, channel, value):
        """ GetOfdmDemodMacFrameCheckSequenceCheckEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodMaximumSymbolsUsed(self, channel, value):
        """ GetOfdmDemodMaximumSymbolsUsed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodMCSIndex(self, channelString, value):
        """ GetOFDMDemodMCSIndex(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodMeasurementLength(self, channelString, value):
        """ GetOFDMDemodMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOfdmDemodMeasurementStartLocation(self, channel, value):
        """ GetOfdmDemodMeasurementStartLocation(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodNonHTModulationDetectionEnabled(self, channelString, value):
        """ GetOFDMDemodNonHTModulationDetectionEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodNonHTModulationMode(self, channelString, value):
        """ GetOFDMDemodNonHTModulationMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodNumberOfAverages(self, channel, value):
        """ GetOfdmDemodNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodNumberOfHESIGBSymbols(self, channelString, value):
        """ GetOFDMDemodNumberOfHESIGBSymbols(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodNumberOfOFDMSymbols(self, channelString, value):
        """ GetOFDMDemodNumberOfOFDMSymbols(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodNumberOfSpaceTimeStreams(self, channelString, value):
        """ GetOfdmDemodNumberOfSpaceTimeStreams(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodNumberOfSymbolsUsed(self, channelString, value):
        """ GetOFDMDemodNumberOfSymbolsUsed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodNumberOfUsers(self, channelString, value):
        """ GetOFDMDemodNumberOfUsers(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodPacketExtensionDisambiguity(self, channelString, value):
        """ GetOFDMDemodPacketExtensionDisambiguity(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodPhaseNoisePSDTraceEnabled(self, channelString, value):
        """ GetOFDMDemodPhaseNoisePSDTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodPhaseTracking(self, channel, value):
        """ GetOfdmDemodPhaseTracking(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodPilotEvmPerSymbolTraceEnabled(self, channel, value):
        """ GetOfdmDemodPilotEvmPerSymbolTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodPPDUType(self, channelString, value):
        """ GetOFDMDemodPPDUType(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodPreambleFrequencyErrorTraceEnabled(self, channelString, value):
        """ GetOFDMDemodPreambleFrequencyErrorTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodPreFECPaddingFactor(self, channelString, value):
        """ GetOFDMDemodPreFECPaddingFactor(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodPSDULength(self, channelString, value):
        """ GetOFDMDemodPSDULength(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodQuadratureSkew(self, channelString, value):
        """ GetOfdmDemodQuadratureSkew(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodQuadratureSkewCompensationEnabled(self, channelString, value):
        """ GetOFDMDemodQuadratureSkewCompensationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodQuadratureSkewEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodQuadratureSkewEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodQuadratureSkewPerSubcarrierTraceEnabled(self, channelString, value):
        """ GetOfdmDemodQuadratureSkewPerSubcarrierTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodRefDataConstellationIdentifier(self, channelString, arraySize, attrVal):
        """ GetOFDMDemodRefDataConstellationIdentifier(self: niWLANA, channelString: str, arraySize: int, attrVal: str) -> int """
        pass

    def GetOFDMDemodReferenceConstellationTraceEnabled(self, channel, value):
        """ GetOFDMDemodReferenceConstellationTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodReferenceDataConstellationEnabled(self, channelString, value):
        """ GetOFDMDemodReferenceDataConstellationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodRmsPhaseError(self, channelString, value):
        """ GetOfdmDemodRmsPhaseError(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodRUOffset(self, channelString, value):
        """ GetOFDMDemodRUOffset(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodRUSize(self, channelString, value):
        """ GetOFDMDemodRUSize(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodS1gSigCrcPassed(self, channel, value):
        """ GetOfdmDemodS1gSigCrcPassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodS1gSigLength(self, channel, value):
        """ GetOfdmDemodS1gSigLength(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodSampleClockOffsetEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodSampleClockOffsetEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodScramblerSeed(self, channelString, value):
        """ GetOFDMDemodScramblerSeed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodServiceBitsTraceEnabled(self, channelString, value):
        """ GetOfdmDemodServiceBitsTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodShortGuardIntervalB1Bit(self, channelString, value):
        """ GetOFDMDemodShortGuardIntervalB1Bit(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodSpaceTimeStreamOffset(self, channelString, value):
        """ GetOFDMDemodSpaceTimeStreamOffset(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodSpectralFlatnessMarginEnabled(self, channelString, value):
        """ GetOFDMDemodSpectralFlatnessMarginEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodSpectralFlatnessMarginSubcarrierIndex(self, channelString, value):
        """ GetOFDMDemodSpectralFlatnessMarginSubcarrierIndex(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodSpectralFlatnessTraceEnabled(self, channel, value):
        """ GetOfdmDemodSpectralFlatnessTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodSTAID(self, channelString, value):
        """ GetOFDMDemodSTAID(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodSTBCAllStreamsEnabled(self, channelString, value):
        """ GetOFDMDemodSTBCAllStreamsEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodStreamPowerEnabled(self, channelString, value):
        """ GetOfdmDemodStreamPowerEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodSymbolTimingAdjustment(self, channel, value):
        """ GetOfdmDemodSymbolTimingAdjustment(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetOfdmDemodTimeTrackingEnabled(self, channel, value):
        """ GetOfdmDemodTimeTrackingEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodTimingSkew(self, channelString, value):
        """ GetOfdmDemodTimingSkew(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodTimingSkew(self, channelString, value):
        """ GetOFDMDemodTimingSkew(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodTimingSkewCompensationEnabled(self, channelString, value):
        """ GetOFDMDemodTimingSkewCompensationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodTimingSkewEstimationEnabled(self, channelString, value):
        """ GetOFDMDemodTimingSkewEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodTransmissionMode(self, channelString, value):
        """ GetOFDMDemodTransmissionMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodTVHTMode(self, channelString, value):
        """ GetOFDMDemodTVHTMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodTVHTSIGACRCPassed(self, channelString, value):
        """ GetOFDMDemodTVHTSIGACRCPassed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodUnusedToneErrorEnabled(self, channelString, value):
        """ GetOFDMDemodUnusedToneErrorEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodUnusedToneErrorMargin(self, channelString, value):
        """ GetOFDMDemodUnusedToneErrorMargin(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetOFDMDemodUnusedToneErrorMarginRUIndex(self, channelString, value):
        """ GetOFDMDemodUnusedToneErrorMarginRUIndex(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodUnusedToneErrorMarginVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetOFDMDemodUnusedToneErrorMarginVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetOFDMDemodUnusedToneErrorMaskReference(self, channelString, value):
        """ GetOFDMDemodUnusedToneErrorMaskReference(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMDemodUnusedToneErrorTrace(self, channelString, RUIndex, UnusedToneErrorMask, UnusedToneError, actualDataArraySize):
        """ GetOFDMDemodUnusedToneErrorTrace(self: niWLANA, channelString: str, RUIndex: Array[int], UnusedToneErrorMask: Array[float], UnusedToneError: Array[float]) -> (int, int) """
        pass

    def GetOFDMDemodUnusedToneErrorTraceEnabled(self, channelString, value):
        """ GetOFDMDemodUnusedToneErrorTraceEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodUserDefinedGatePowerEnabled(self, channel, value):
        """ GetOfdmDemodUserDefinedGatePowerEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOfdmDemodUserDefinedGateStartTime(self, channel, value):
        """ GetOfdmDemodUserDefinedGateStartTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetOfdmDemodUserDefinedGateStopTime(self, channel, value):
        """ GetOfdmDemodUserDefinedGateStopTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetOFDMDemodVHTSIGACRCPassed(self, channelString, value):
        """ GetOFDMDemodVHTSIGACRCPassed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmDemodVhtSigBCrcCheckEnabled(self, channel, value):
        """ GetOfdmDemodVhtSigBCrcCheckEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMDemodVHTSIGBCRCPassed(self, channelString, value):
        """ GetOFDMDemodVHTSIGBCRCPassed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMLSIGPayloadLength(self, channelString, value):
        """ GetOFDMLSIGPayloadLength(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmMidamblePeriodicity(self, channelString, value):
        """ GetOfdmMidamblePeriodicity(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMNoiseCompensationApplied(self, channelString, value):
        """ GetOFDMNoiseCompensationApplied(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMNumberOfUsers(self, channelString, value):
        """ GetOFDMNumberOfUsers(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMPacketExtensionDisambiguity(self, channelString, value):
        """ GetOFDMPacketExtensionDisambiguity(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOfdmPayloadLength(self, channel, value):
        """ GetOfdmPayloadLength(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetOFDMPhaseErrorEstimationEnabled(self, channelString, value):
        """ GetOFDMPhaseErrorEstimationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMPPDUType(self, channelString, value):
        """ GetOFDMPPDUType(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMPreFECPaddingFactor(self, channelString, value):
        """ GetOFDMPreFECPaddingFactor(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMRUOffset(self, channelString, value):
        """ GetOFDMRUOffset(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOFDMRUSize(self, channelString, value):
        """ GetOFDMRUSize(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOptimizeReferenceLevelForEVMEnabled(self, channelString, value):
        """ GetOptimizeReferenceLevelForEVMEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetOptimizeReferenceLevelForEVMMargin(self, channelString, value):
        """ GetOptimizeReferenceLevelForEVMMargin(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetPackeExtensionDuration(self, channelString, value):
        """ GetPackeExtensionDuration(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetRbw(self, channel, value):
        """ GetRbw(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRbwDefinition(self, channel, value):
        """ GetRbwDefinition(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetRecommendedAcquisitionLength(self, channel, value):
        """ GetRecommendedAcquisitionLength(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedAcquisitionType(self, channel, value):
        """ GetRecommendedAcquisitionType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetRecommendedIqPostTriggerDelay(self, channel, value):
        """ GetRecommendedIqPostTriggerDelay(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedIqPreTriggerDelay(self, channel, value):
        """ GetRecommendedIqPreTriggerDelay(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedIqSamplingRate(self, channel, value):
        """ GetRecommendedIqSamplingRate(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedMinimumQuietTime(self, channel, value):
        """ GetRecommendedMinimumQuietTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedNumberOfRecords(self, channel, value):
        """ GetRecommendedNumberOfRecords(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetRecommendedSpectrumFftWindowType(self, channel, value):
        """ GetRecommendedSpectrumFftWindowType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetRecommendedSpectrumRbw(self, channel, value):
        """ GetRecommendedSpectrumRbw(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedSpectrumRbwDefinition(self, channel, value):
        """ GetRecommendedSpectrumRbwDefinition(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetRecommendedSpectrumSpan(self, channel, value):
        """ GetRecommendedSpectrumSpan(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetRecommendedSpectrumVbw(self, channel, value):
        """ GetRecommendedSpectrumVbw(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultAmpmMeasurementsAmamPolynomialCoefficients(self, channelString, value, dataSize, actualNumDataArrayElements):
        """ GetResultAmpmMeasurementsAmamPolynomialCoefficients(self: niWLANA, channelString: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultAmpmMeasurementsAmamResidual(self, channel, value):
        """ GetResultAmpmMeasurementsAmamResidual(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultAmpmMeasurementsAmpmPolynomialCoefficients(self, channelString, value, dataSize, actualNumDataArrayElements):
        """ GetResultAmpmMeasurementsAmpmPolynomialCoefficients(self: niWLANA, channelString: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultAutorangeAcquisitionLength(self, channel, value):
        """ GetResultAutorangeAcquisitionLength(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultAutorangeMaxInputPower(self, channel, value):
        """ GetResultAutorangeMaxInputPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemod80211bPeakEvm(self, channel, value):
        """ GetResultDsssDemod80211bPeakEvm(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemod80211bPeakEvm2007(self, channel, value):
        """ GetResultDsssDemod80211bPeakEvm2007(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemod80211bPeakEvm2007Maximum(self, channel, value):
        """ GetResultDsssDemod80211bPeakEvm2007Maximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemod80211bPeakEvm2007Minimum(self, channel, value):
        """ GetResultDsssDemod80211bPeakEvm2007Minimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemod80211bPeakEvmMaximum(self, channel, value):
        """ GetResultDsssDemod80211bPeakEvmMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemod80211bPeakEvmMinimum(self, channel, value):
        """ GetResultDsssDemod80211bPeakEvmMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodAverageGatedPower(self, channel, value):
        """ GetResultDsssDemodAverageGatedPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodAverageGatedPowerAverage(self, channel, value):
        """ GetResultDsssDemodAverageGatedPowerAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodAverageGatedPowerMaximum(self, channel, value):
        """ GetResultDsssDemodAverageGatedPowerMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodAverageGatedPowerMinimum(self, channel, value):
        """ GetResultDsssDemodAverageGatedPowerMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodAverageGatedPowerStandardDeviation(self, channel, value):
        """ GetResultDsssDemodAverageGatedPowerStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodBurstStartTime(self, channel, value):
        """ GetResultDsssDemodBurstStartTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierFrequencyOffset(self, channel, value):
        """ GetResultDsssDemodCarrierFrequencyOffset(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierFrequencyOffsetAverage(self, channel, value):
        """ GetResultDsssDemodCarrierFrequencyOffsetAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierFrequencyOffsetMaximum(self, channel, value):
        """ GetResultDsssDemodCarrierFrequencyOffsetMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierFrequencyOffsetMinimum(self, channel, value):
        """ GetResultDsssDemodCarrierFrequencyOffsetMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierFrequencyOffsetStandardDeviation(self, channel, value):
        """ GetResultDsssDemodCarrierFrequencyOffsetStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierSuppression(self, channel, value):
        """ GetResultDsssDemodCarrierSuppression(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierSuppressionAverage(self, channel, value):
        """ GetResultDsssDemodCarrierSuppressionAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierSuppressionMaximum(self, channel, value):
        """ GetResultDsssDemodCarrierSuppressionMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierSuppressionMinimum(self, channel, value):
        """ GetResultDsssDemodCarrierSuppressionMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodCarrierSuppressionStandardDeviation(self, channel, value):
        """ GetResultDsssDemodCarrierSuppressionStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodDataRate(self, channel, value):
        """ GetResultDsssDemodDataRate(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerMeanPowerAverage(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerMeanPowerAverage(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerMeanPowerMaximum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerMeanPowerMaximum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerMeanPowerMinimum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerMeanPowerMinimum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerMeanPowerStandardDeviation(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerMeanPowerStandardDeviation(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerPeakPowerAverage(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerPeakPowerAverage(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerPeakPowerMaximum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerPeakPowerMaximum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerPeakPowerMinimum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerPeakPowerMinimum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodGatedPowerPeakPowerStandardDeviation(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultDsssDemodGatedPowerPeakPowerStandardDeviation(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultDsssDemodHeaderChecksumPassed(self, channel, value):
        """ GetResultDsssDemodHeaderChecksumPassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultDsssDemodIqGainImbalance(self, channel, value):
        """ GetResultDsssDemodIqGainImbalance(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodIqGainImbalanceAverage(self, channel, value):
        """ GetResultDsssDemodIqGainImbalanceAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodIqGainImbalanceMaximum(self, channel, value):
        """ GetResultDsssDemodIqGainImbalanceMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodIqGainImbalanceMinimum(self, channel, value):
        """ GetResultDsssDemodIqGainImbalanceMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodIqGainImbalanceStandardDeviation(self, channel, value):
        """ GetResultDsssDemodIqGainImbalanceStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodMacFrameCheckSequencePassed(self, channel, value):
        """ GetResultDsssDemodMacFrameCheckSequencePassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultDsssDemodPayloadLength(self, channel, value):
        """ GetResultDsssDemodPayloadLength(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultDsssDemodPeakEvm(self, channel, value):
        """ GetResultDsssDemodPeakEvm(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodPeakEvmMaximum(self, channel, value):
        """ GetResultDsssDemodPeakEvmMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodPeakEvmMinimum(self, channel, value):
        """ GetResultDsssDemodPeakEvmMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodPhaseErrorRmsAverage(self, channelString, value):
        """ GetResultDsssDemodPhaseErrorRmsAverage(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultDsssDemodPhaseErrorRmsMaximum(self, channelString, value):
        """ GetResultDsssDemodPhaseErrorRmsMaximum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultDsssDemodPhaseErrorRmsMinimum(self, channelString, value):
        """ GetResultDsssDemodPhaseErrorRmsMinimum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultDsssDemodPhaseErrorRmsStandardDeviation(self, channelString, value):
        """ GetResultDsssDemodPhaseErrorRmsStandardDeviation(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultDsssDemodPreambleType(self, channel, value):
        """ GetResultDsssDemodPreambleType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultDsssDemodQuadratureSkew(self, channel, value):
        """ GetResultDsssDemodQuadratureSkew(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodQuadratureSkewAverage(self, channel, value):
        """ GetResultDsssDemodQuadratureSkewAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodQuadratureSkewMaximum(self, channel, value):
        """ GetResultDsssDemodQuadratureSkewMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodQuadratureSkewMinimum(self, channel, value):
        """ GetResultDsssDemodQuadratureSkewMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodQuadratureSkewStandardDeviation(self, channel, value):
        """ GetResultDsssDemodQuadratureSkewStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodRmsEvm(self, channel, value):
        """ GetResultDsssDemodRmsEvm(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodRmsEvmAverage(self, channel, value):
        """ GetResultDsssDemodRmsEvmAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodRmsEvmMaximum(self, channel, value):
        """ GetResultDsssDemodRmsEvmMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodRmsEvmMinimum(self, channel, value):
        """ GetResultDsssDemodRmsEvmMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodRmsEvmStandardDeviation(self, channel, value):
        """ GetResultDsssDemodRmsEvmStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodSampleClockOffset(self, channel, value):
        """ GetResultDsssDemodSampleClockOffset(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodSampleClockOffsetAverage(self, channel, value):
        """ GetResultDsssDemodSampleClockOffsetAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodSampleClockOffsetMaximum(self, channel, value):
        """ GetResultDsssDemodSampleClockOffsetMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodSampleClockOffsetMinimum(self, channel, value):
        """ GetResultDsssDemodSampleClockOffsetMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodSampleClockOffsetStandardDeviation(self, channel, value):
        """ GetResultDsssDemodSampleClockOffsetStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssDemodSfdFound(self, channel, value):
        """ GetResultDsssDemodSfdFound(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultDsssPowerRampDownTime(self, channel, value):
        """ GetResultDsssPowerRampDownTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultDsssPowerRampUpTime(self, channel, value):
        """ GetResultDsssPowerRampUpTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultMaxSpectralDensity(self, channel, value):
        """ GetResultMaxSpectralDensity(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultObw(self, channel, value):
        """ GetResultObw(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultObwHighFrequency(self, channel, value):
        """ GetResultObwHighFrequency(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultObwLowFrequency(self, channel, value):
        """ GetResultObwLowFrequency(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemod80211nPlcpFrameFormat(self, channel, value):
        """ GetResultOfdmDemod80211nPlcpFrameFormat(self: niWLANA, channel: str) -> (int, str) """
        pass

    def GetResultOfdmDemodAggregation(self, channel, value):
        """ GetResultOfdmDemodAggregation(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodAverageGatedPower(self, channel, value):
        """ GetResultOfdmDemodAverageGatedPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodAverageGatedPowerAverage(self, channel, value):
        """ GetResultOfdmDemodAverageGatedPowerAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodAverageGatedPowerMaximum(self, channel, value):
        """ GetResultOfdmDemodAverageGatedPowerMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodAverageGatedPowerMinimum(self, channel, value):
        """ GetResultOfdmDemodAverageGatedPowerMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodAverageGatedPowerStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodAverageGatedPowerStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodBurstStartTime(self, channel, value):
        """ GetResultOfdmDemodBurstStartTime(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyLeakage(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyLeakage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyLeakageAverage(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyLeakageAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyLeakageMaximum(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyLeakageMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyLeakageMinimum(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyLeakageMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyLeakageStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyLeakageStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyOffset(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyOffset(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyOffsetAverage(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyOffsetAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyOffsetMaximum(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyOffsetMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyOffsetMinimum(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyOffsetMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCarrierFrequencyOffsetStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodCarrierFrequencyOffsetStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixAbsolutePowerAverage(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixAbsolutePowerAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixAbsolutePowerMaximum(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixAbsolutePowerMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixAbsolutePowerMinimum(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixAbsolutePowerMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixAbsolutePowerStdDev(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixAbsolutePowerStdDev(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixCrossPowerMaximum(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixCrossPowerMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixCrossPowerMinimum(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixCrossPowerMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodChannelMatrixCrossPowerStdDev(self, channel, value):
        """ GetResultOfdmDemodChannelMatrixCrossPowerStdDev(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommmonPhaseErrorAverage(self, channel, value):
        """ GetResultOfdmDemodCommmonPhaseErrorAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommmonPhaseErrorMaximum(self, channel, value):
        """ GetResultOfdmDemodCommmonPhaseErrorMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommmonPhaseErrorMinimum(self, channel, value):
        """ GetResultOfdmDemodCommmonPhaseErrorMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommmonPhaseErrorStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodCommmonPhaseErrorStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPhaseErrorAverage(self, channel, value):
        """ GetResultOfdmDemodCommonPhaseErrorAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPhaseErrorMaximum(self, channel, value):
        """ GetResultOfdmDemodCommonPhaseErrorMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPhaseErrorMinimum(self, channel, value):
        """ GetResultOfdmDemodCommonPhaseErrorMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPhaseErrorStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodCommonPhaseErrorStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPilotErrorRms(self, channel, value):
        """ GetResultOfdmDemodCommonPilotErrorRms(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPilotErrorRmsAverage(self, channel, value):
        """ GetResultOfdmDemodCommonPilotErrorRmsAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPilotErrorRmsMaximum(self, channel, value):
        """ GetResultOfdmDemodCommonPilotErrorRmsMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPilotErrorRmsMinimum(self, channel, value):
        """ GetResultOfdmDemodCommonPilotErrorRmsMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCommonPilotErrorRmsStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodCommonPilotErrorRmsStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCrossPower(self, channel, value):
        """ GetResultOfdmDemodCrossPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodCrossPowerAverage(self, channel, value):
        """ GetResultOfdmDemodCrossPowerAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodDataRate(self, channel, value):
        """ GetResultOfdmDemodDataRate(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodDataRmsEvm(self, channel, value):
        """ GetResultOfdmDemodDataRmsEvm(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodDataRmsEvmAverage(self, channel, value):
        """ GetResultOfdmDemodDataRmsEvmAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodDataRmsEvmMaximum(self, channel, value):
        """ GetResultOfdmDemodDataRmsEvmMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodDataRmsEvmMinimum(self, channel, value):
        """ GetResultOfdmDemodDataRmsEvmMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodDataRmsEvmStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodDataRmsEvmStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodDsssofdmHeaderCrcPassed(self, channel, value):
        """ GetResultOfdmDemodDsssofdmHeaderCrcPassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodEffectiveDataRate(self, channel, value):
        """ GetResultOfdmDemodEffectiveDataRate(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodFecCodingType(self, channel, value):
        """ GetResultOfdmDemodFecCodingType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerMeanPowerAverage(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerMeanPowerAverage(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerMeanPowerMaximum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerMeanPowerMaximum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerMeanPowerMinimum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerMeanPowerMinimum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerMeanPowerStandardDeviation(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerMeanPowerStandardDeviation(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerPeakPowerAverage(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerPeakPowerAverage(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerPeakPowerMaximum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerPeakPowerMaximum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerPeakPowerMinimum(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerPeakPowerMinimum(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGatedPowerPeakPowerStandardDeviation(self, channel, value, dataSize, actualNumDataArrayElements):
        """ GetResultOfdmDemodGatedPowerPeakPowerStandardDeviation(self: niWLANA, channel: str, value: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetResultOfdmDemodGuardInterval(self, channel, value):
        """ GetResultOfdmDemodGuardInterval(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodHeaderParityPassed(self, channel, value):
        """ GetResultOfdmDemodHeaderParityPassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodHtSigCrcPassed(self, channel, value):
        """ GetResultOfdmDemodHtSigCrcPassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodIqGainImbalance(self, channel, value):
        """ GetResultOfdmDemodIqGainImbalance(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodIqGainImbalanceAverage(self, channel, value):
        """ GetResultOfdmDemodIqGainImbalanceAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodIqGainImbalanceMaximum(self, channel, value):
        """ GetResultOfdmDemodIqGainImbalanceMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodIqGainImbalanceMinimum(self, channel, value):
        """ GetResultOfdmDemodIqGainImbalanceMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodIqGainImbalanceStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodIqGainImbalanceStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodMacFrameCheckSequencePassed(self, channel, value):
        """ GetResultOfdmDemodMacFrameCheckSequencePassed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodMcsIndex(self, channel, value):
        """ GetResultOfdmDemodMcsIndex(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodNotSoundingBit(self, channel, value):
        """ GetResultOfdmDemodNotSoundingBit(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodNumberOfExtensionSpatialStreams(self, channel, value):
        """ GetResultOfdmDemodNumberOfExtensionSpatialStreams(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodNumberOfOfdmSymbols(self, channel, value):
        """ GetResultOfdmDemodNumberOfOfdmSymbols(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodNumberOfSpaceTimeStreams(self, channelString, value):
        """ GetResultOfdmDemodNumberOfSpaceTimeStreams(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetResultOfdmDemodNumberOfSymbolsUsed(self, channel, value):
        """ GetResultOfdmDemodNumberOfSymbolsUsed(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodPayloadLength(self, channel, value):
        """ GetResultOfdmDemodPayloadLength(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodPilotRmsEvm(self, channel, value):
        """ GetResultOfdmDemodPilotRmsEvm(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodPilotRmsEvmAverage(self, channel, value):
        """ GetResultOfdmDemodPilotRmsEvmAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodPilotRmsEvmMaximum(self, channel, value):
        """ GetResultOfdmDemodPilotRmsEvmMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodPilotRmsEvmMinimum(self, channel, value):
        """ GetResultOfdmDemodPilotRmsEvmMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodPilotRmsEvmStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodPilotRmsEvmStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodQuadratureSkew(self, channel, value):
        """ GetResultOfdmDemodQuadratureSkew(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodQuadratureSkewAverage(self, channel, value):
        """ GetResultOfdmDemodQuadratureSkewAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodQuadratureSkewMaximum(self, channel, value):
        """ GetResultOfdmDemodQuadratureSkewMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodQuadratureSkewMinimum(self, channel, value):
        """ GetResultOfdmDemodQuadratureSkewMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodQuadratureSkewStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodQuadratureSkewStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodRmsEvm(self, channel, value):
        """ GetResultOfdmDemodRmsEvm(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodRmsEvmAverage(self, channel, value):
        """ GetResultOfdmDemodRmsEvmAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodRmsEvmMaximum(self, channel, value):
        """ GetResultOfdmDemodRmsEvmMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodRmsEvmMinimum(self, channel, value):
        """ GetResultOfdmDemodRmsEvmMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodRmsEvmStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodRmsEvmStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodRmsPhaseError(self, channelString, value):
        """ GetResultOfdmDemodRmsPhaseError(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSampleClockOffset(self, channel, value):
        """ GetResultOfdmDemodSampleClockOffset(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSampleClockOffsetAverage(self, channel, value):
        """ GetResultOfdmDemodSampleClockOffsetAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSampleClockOffsetMaximum(self, channel, value):
        """ GetResultOfdmDemodSampleClockOffsetMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSampleClockOffsetMinimum(self, channel, value):
        """ GetResultOfdmDemodSampleClockOffsetMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSampleClockOffsetStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodSampleClockOffsetStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSpectralFlatnessMargin(self, channel, value):
        """ GetResultOfdmDemodSpectralFlatnessMargin(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSpectralFlatnessMarginAverage(self, channel, value):
        """ GetResultOfdmDemodSpectralFlatnessMarginAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSpectralFlatnessMarginMaximum(self, channel, value):
        """ GetResultOfdmDemodSpectralFlatnessMarginMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSpectralFlatnessMarginMinimum(self, channel, value):
        """ GetResultOfdmDemodSpectralFlatnessMarginMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSpectralFlatnessMarginStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodSpectralFlatnessMarginStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodSpectralFlatnessMarginSubcarrierIndex(self, channel, value):
        """ GetResultOfdmDemodSpectralFlatnessMarginSubcarrierIndex(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodStbcIndex(self, channel, value):
        """ GetResultOfdmDemodStbcIndex(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetResultOfdmDemodStreamPowerAverage(self, channelString, value):
        """ GetResultOfdmDemodStreamPowerAverage(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultOfdmDemodStreamPowerMaximum(self, channelString, value):
        """ GetResultOfdmDemodStreamPowerMaximum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultOfdmDemodStreamPowerMinimum(self, channelString, value):
        """ GetResultOfdmDemodStreamPowerMinimum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultOfdmDemodStreamPowerStandardDeviation(self, channelString, value):
        """ GetResultOfdmDemodStreamPowerStandardDeviation(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultOfdmDemodTimingSkewAverage(self, channel, value):
        """ GetResultOfdmDemodTimingSkewAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodTimingSkewMaximum(self, channel, value):
        """ GetResultOfdmDemodTimingSkewMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodTimingSkewMinimum(self, channel, value):
        """ GetResultOfdmDemodTimingSkewMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultOfdmDemodTimingSkewStandardDeviation(self, channel, value):
        """ GetResultOfdmDemodTimingSkewStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultSpectralMaskMargin(self, channel, value):
        """ GetResultSpectralMaskMargin(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultSpectralMaskMarginVector(self, channel, *__args):
        """
        GetResultSpectralMaskMarginVector(self: niWLANA, channel: str, data: Array[float], dataSize: int) -> (int, int)
        GetResultSpectralMaskMarginVector(self: niWLANA, channel: str) -> (int, float)
        """
        pass

    def GetResultSpectralMaskReferenceLevel(self, channel, value):
        """ GetResultSpectralMaskReferenceLevel(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultSpectralMaskViolation(self, channelString, value):
        """ GetResultSpectralMaskViolation(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultSpectralMeasurementsChannelPower(self, channelString, value):
        """ GetResultSpectralMeasurementsChannelPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerAverage(self, channel, value):
        """ GetResultTxpAveragePowerAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerMaximum(self, channel, value):
        """ GetResultTxpAveragePowerMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerMinimum(self, channelString, value):
        """ GetResultTxpAveragePowerMinimum(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerStandardDeviation(self, channel, value):
        """ GetResultTxpAveragePowerStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerWithIdleTimeAverage(self, channel, value):
        """ GetResultTxpAveragePowerWithIdleTimeAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerWithIdleTimeMaximum(self, channel, value):
        """ GetResultTxpAveragePowerWithIdleTimeMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerWithIdleTimeMinimum(self, channel, value):
        """ GetResultTxpAveragePowerWithIdleTimeMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpAveragePowerWithIdleTimeStandardDeviation(self, channel, value):
        """ GetResultTxpAveragePowerWithIdleTimeStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpowerMeasurementsAveragePower(self, channel, value):
        """ GetResultTxpowerMeasurementsAveragePower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpowerMeasurementsPeakPower(self, channel, value):
        """ GetResultTxpowerMeasurementsPeakPower(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpPeakPowerAverage(self, channel, value):
        """ GetResultTxpPeakPowerAverage(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpPeakPowerMaximum(self, channel, value):
        """ GetResultTxpPeakPowerMaximum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpPeakPowerMinimum(self, channel, value):
        """ GetResultTxpPeakPowerMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetResultTxpPeakPowerStandardDeviation(self, channel, value):
        """ GetResultTxpPeakPowerStandardDeviation(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetSampleClockRateFactor(self, channelString, value):
        """ GetSampleClockRateFactor(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetScalarAttributeF64(self, channelString, attributeID, attributeValue):
        """ GetScalarAttributeF64(self: niWLANA, channelString: str, attributeID: niWLANAProperties) -> (int, float) """
        pass

    def GetScalarAttributeI32(self, channelString, attributeID, attributeValue):
        """ GetScalarAttributeI32(self: niWLANA, channelString: str, attributeID: niWLANAProperties) -> (int, int) """
        pass

    def GetScramblerSeed(self, channelString, value):
        """ GetScramblerSeed(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetShortGuardIntervalB1Bit(self, channelString, value):
        """ GetShortGuardIntervalB1Bit(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetSpaceTimeStreamOffset(self, channelString, value):
        """ GetSpaceTimeStreamOffset(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetSpan(self, channel, value):
        """ GetSpan(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetSpectralMask(self, channelString, f0, df, spectralMask, spectrum, dataArraySize, actualNumDataArrayElements):
        """ GetSpectralMask(self: niWLANA, channelString: str, spectralMask: Array[float], spectrum: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetSpectralMaskCenterFrequency(self, channel, value):
        """ GetSpectralMaskCenterFrequency(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetSpectralMaskCombinedMaskEnabled(self, channel, value):
        """ GetSpectralMaskCombinedMaskEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMaskEnabled(self, channel, value):
        """ GetSpectralMaskEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMaskFrequencyOffsets(self, channel, data, dataSize, actualNumDataArrayElements):
        """ GetSpectralMaskFrequencyOffsets(self: niWLANA, channel: str, data: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetSpectralMaskFrequencyOffsetsUsed(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetSpectralMaskFrequencyOffsetsUsed(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetSpectralMaskMargin(self, channelString, value):
        """ GetSpectralMaskMargin(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetSpectralMaskMarginFrequencyVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetSpectralMaskMarginFrequencyVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetSpectralMaskMarginPowerSpectralDensityVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetSpectralMaskMarginPowerSpectralDensityVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetSpectralMaskMarginVector(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetSpectralMaskMarginVector(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetSpectralMaskNumberOfAverages(self, channel, value):
        """ GetSpectralMaskNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMaskPowerOffsets(self, channel, data, dataSize, actualNumDataArrayElements):
        """ GetSpectralMaskPowerOffsets(self: niWLANA, channel: str, data: Array[float], dataSize: int) -> (int, int) """
        pass

    def GetSpectralMaskPowerOffsetsUsed(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetSpectralMaskPowerOffsetsUsed(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetSpectralMaskReferenceLevel(self, channel, value):
        """ GetSpectralMaskReferenceLevel(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetSpectralMaskReferenceLevelType(self, channel, value):
        """ GetSpectralMaskReferenceLevelType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMaskTrace(self, channelString, f0, df, spectralMask, spectrum, dataArraySize, actualArraySize):
        """ GetSpectralMaskTrace(self: niWLANA, channelString: str, spectralMask: Array[float], spectrum: Array[float], dataArraySize: int) -> (int, float, float, int) """
        pass

    def GetSpectralMaskTraceEnabled(self, channel, value):
        """ GetSpectralMaskTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMaskTransmitPowerClass(self, channelString, value):
        """ GetSpectralMaskTransmitPowerClass(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetSpectralMaskType(self, channel, value):
        """ GetSpectralMaskType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMeasurementChannelPower(self, channelString, value):
        """ GetSpectralMeasurementChannelPower(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetSpectralMeasurementChannelPowerMeasuremntBW(self, channelString, value):
        """ GetSpectralMeasurementChannelPowerMeasuremntBW(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetSpectralMeasurementsAllEnabled(self, channel, value):
        """ GetSpectralMeasurementsAllEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSpectralMeasurementsChannelPowerAutoMeasureBwEnabled(self, channelString, value):
        """ GetSpectralMeasurementsChannelPowerAutoMeasureBwEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetSpectralMeasurementsChannelPowerEnabled(self, channelString, value):
        """ GetSpectralMeasurementsChannelPowerEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetSpectralMeasurementsChannelPowerMeasurementBandwidth(self, channelString, value):
        """ GetSpectralMeasurementsChannelPowerMeasurementBandwidth(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetSpectralMeasurementsChannelPowerNumberOfAverages(self, channelString, value):
        """ GetSpectralMeasurementsChannelPowerNumberOfAverages(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetSpectralMeasurementsChPowerAutoMeasureBWEnabled(self, channelString, value):
        """ GetSpectralMeasurementsChPowerAutoMeasureBWEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetStandard(self, channel, value):
        """ GetStandard(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSTBCAllStreamsEnabled(self, channelString, value):
        """ GetSTBCAllStreamsEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetStbcIndex(self, channel, value):
        """ GetStbcIndex(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetSwapIAndQEnabled(self, channelString, value):
        """ GetSwapIAndQEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetTClkSynchronizationEnabled(self, channelString, value):
        """ GetTClkSynchronizationEnabled(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetToolkitCompatibilityVersion(self, channelString, value):
        """ GetToolkitCompatibilityVersion(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetTransmissionMode(self, channelString, value):
        """ GetTransmissionMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetTriggerDelay(self, channel, value):
        """ GetTriggerDelay(self: niWLANA, channel: str) -> (int, float) """
        pass

    def GetTxPowerBurstDetectionEnabled(self, channel, value):
        """ GetTxPowerBurstDetectionEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetTxPowerMeasurementLength(self, channelString, value):
        """ GetTxPowerMeasurementLength(self: niWLANA, channelString: str) -> (int, float) """
        pass

    def GetTxPowerMeasurementMode(self, channelString, value):
        """ GetTxPowerMeasurementMode(self: niWLANA, channelString: str) -> (int, int) """
        pass

    def GetTxpowerMeasurementsEnabled(self, channel, value):
        """ GetTxpowerMeasurementsEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetTxpowerMeasurementsMode(self, channel, value):
        """ GetTxpowerMeasurementsMode(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetTxpowerMeasurementsNumberOfAverages(self, channel, value):
        """ GetTxpowerMeasurementsNumberOfAverages(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetTxpowerMeasurementsPvtTraceEnabled(self, channel, value):
        """ GetTxpowerMeasurementsPvtTraceEnabled(self: niWLANA, channel: str) -> (int, int) """
        pass

    def GetVectorAttributeF64(self, channelString, attributeID, data, dataArraySize, actualNumDataArrayElements):
        """ GetVectorAttributeF64(self: niWLANA, channelString: str, attributeID: niWLANAProperties, data: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def Get_80211ahPreambleType(self, channel, value):
        """ Get_80211ahPreambleType(self: niWLANA, channel: str) -> (int, int) """
        pass

    def Get_80211nPlcpFrameFormat(self, channel, value):
        """ Get_80211nPlcpFrameFormat(self: niWLANA, channel: str) -> (int, int) """
        pass

    def LoadConfigurationFromFile(self, filePath, reset):
        """ LoadConfigurationFromFile(self: niWLANA, filePath: str, reset: int) -> int """
        pass

    def niWLANA_GetCurrentIterationOFDMDemodSpectralFlatnessTrace(self, channelString, index, upperMask, spectralFlatness, lowerMask, dataArraySize, actualArraySize):
        """ niWLANA_GetCurrentIterationOFDMDemodSpectralFlatnessTrace(self: niWLANA, channelString: str, index: Array[int], upperMask: Array[float], spectralFlatness: Array[float], lowerMask: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def ReadWaveformFromFile(self, filePath, waveformName, offset, count, t0, dt, waveform, waveformSize, actualSize, eOF):
        """ ReadWaveformFromFile(self: niWLANA, filePath: str, waveformName: str, offset: int, count: int, waveformSize: int) -> (int, float, float, niComplexNumber, int, int) """
        pass

    def ResetSession(self):
        """ ResetSession(self: niWLANA) -> int """
        pass

    def ResultTxpAveragePowerMinimum(self, channel, value):
        """ ResultTxpAveragePowerMinimum(self: niWLANA, channel: str) -> (int, float) """
        pass

    def RFSAAutoLevel(self, rFSASession, hardwareChannelString, *__args):
        """
        RFSAAutoLevel(self: niWLANA, rFSASession: HandleRef, hardwareChannelString: str, carrierFrequency: float, bandwidth: float, measurementInterval: float, maxNumberofIterations: int) -> (int, float)
        RFSAAutoLevel(self: niWLANA, rFSASession: HandleRef, hardwareChannelString: str, bandwidth: float, measurementInterval: float, maxNumberofIterations: int) -> (int, float)
        """
        pass

    def RFSAAutoLevelv2(self, rFSASession, channelString, measurementInterval, maximumNumberOfIterations, resultantReferenceLevel):
        """ RFSAAutoLevelv2(self: niWLANA, rFSASession: HandleRef, channelString: str, measurementInterval: float, maximumNumberOfIterations: int) -> (int, float) """
        pass

    def RFSAAutoRange(self, wLANChannelString, rFSASession, hardwareChannelString):
        """ RFSAAutoRange(self: niWLANA, wLANChannelString: str, rFSASession: HandleRef, hardwareChannelString: str) -> int """
        pass

    def RFSAConfigure(self, wLANChannelString, rFSASession, hardwareChannelString, resetHardware, samplesPerRecord):
        """ RFSAConfigure(self: niWLANA, wLANChannelString: str, rFSASession: HandleRef, hardwareChannelString: str, resetHardware: int) -> (int, Int64) """
        pass

    def RFSAConfigureFrequencyMultipleLO(self, rfsaHandles, LOSource, externalLOHandles, carrierFrequencies, dataArraySize, rfsaLODaisyChainEnabled, LOExportToExternalDevicesEnabled):
        """ RFSAConfigureFrequencyMultipleLO(self: niWLANA, rfsaHandles: Array[HandleRef], LOSource: int, externalLOHandles: Array[HandleRef], carrierFrequencies: Array[float], dataArraySize: int, rfsaLODaisyChainEnabled: int, LOExportToExternalDevicesEnabled: int) -> int """
        pass

    def RFSAConfigureFrequencySingleLO(self, rfsaHandles, LOSource, externalLOHandle, carrierFrequency, rfsaLODaisyChainEnabled, LOExportToExternalDevicesEnabled):
        """ RFSAConfigureFrequencySingleLO(self: niWLANA, rfsaHandles: Array[HandleRef], LOSource: int, externalLOHandle: HandleRef, carrierFrequency: float, rfsaLODaisyChainEnabled: int, LOExportToExternalDevicesEnabled: int) -> int """
        pass

    def RFSAConfigureHardware(self, rFSASession, hardwareChannelString, samplesPerRecord):
        """ RFSAConfigureHardware(self: niWLANA, rFSASession: HandleRef, hardwareChannelString: str) -> (int, Int64) """
        pass

    def RFSAConfigureMultipleDeviceSynchronization(self, rFSASessions, noOfChannels, MasterReferenceClockSource, TriggerLines, noOfTriggerLines):
        """ RFSAConfigureMultipleDeviceSynchronization(self: niWLANA, rFSASessions: Array[HandleRef], noOfChannels: int, MasterReferenceClockSource: str, TriggerLines: Array[int], noOfTriggerLines: int) -> int """
        pass

    def RFSAConfigureOptimalEVMReferenceLevel(self, rFSASession, channelString, peakPower, referenceLevel):
        """ RFSAConfigureOptimalEVMReferenceLevel(self: niWLANA, rFSASession: HandleRef, channelString: str, peakPower: float) -> (int, float) """
        pass

    def RFSAForceTClkSynchronization(self, rfsaHandles, forceSync):
        """ RFSAForceTClkSynchronization(self: niWLANA, rfsaHandles: Array[HandleRef], forceSync: int) -> int """
        pass

    def RFSALoadNoiseCompensationData(self, rFSASession, forceLoad):
        """ RFSALoadNoiseCompensationData(self: niWLANA, rFSASession: HandleRef, forceLoad: int) -> int """
        pass

    def RFSAMeasure(self, rFSASession, hardwareChannelString, timeout):
        """ RFSAMeasure(self: niWLANA, rFSASession: HandleRef, hardwareChannelString: str, timeout: float) -> int """
        pass

    def RFSAMeasureNoiseFloor(self, instrHandle, externalLOHandle, LOSource, PortType):
        """ RFSAMeasureNoiseFloor(self: niWLANA, instrHandle: Array[HandleRef], externalLOHandle: HandleRef, LOSource: Array[int], PortType: Array[int]) -> int """
        pass

    def RFSAMIMOMeasure(self, rFSASessions, hardwareChannelStrings, numberofRxChains, timeout):
        """ RFSAMIMOMeasure(self: niWLANA, rFSASessions: Array[HandleRef], hardwareChannelStrings: Array[str], numberofRxChains: int, timeout: float) -> int """
        pass

    def RFSAMultipleDeviceInitiate(self, rFSASessions, numberofChannels):
        """ RFSAMultipleDeviceInitiate(self: niWLANA, rFSASessions: Array[HandleRef], numberofChannels: int) -> int """
        pass

    def RFSAReadGatedPowerSpectrum(self, wLANChannelString, rFSASession, hardwareChannelString, timeout, f0, df, powerSpectrum, powerSpectrumArraySize, actualNumPowerSpectrumElement):
        """ RFSAReadGatedPowerSpectrum(self: niWLANA, wLANChannelString: str, rFSASession: HandleRef, hardwareChannelString: str, timeout: float, powerSpectrum: Array[float], powerSpectrumArraySize: int) -> (int, float, float, int) """
        pass

    def RFSAReadMIMOGatedPowerSpectrum(self, wLANChannelStrings, rFSASessions, hwChannelStrings, timeout, f0, df, powerSpectra, numberofRxChains, individualSpectrumSize, actualNumSamplesInEachSpec):
        """ RFSAReadMIMOGatedPowerSpectrum(self: niWLANA, wLANChannelStrings: str, rFSASessions: Array[HandleRef], hwChannelStrings: str, timeout: float, f0: Array[float], df: Array[float], powerSpectra: Array[float], numberofRxChains: int, individualSpectrumSize: int) -> (int, int) """
        pass

    def SaveConfigurationToFile(self, filePath, operation):
        """ SaveConfigurationToFile(self: niWLANA, filePath: str, operation: int) -> int """
        pass

    def SelectAmplitudeCorrectionTable(self, channelString, analyzerIndex, tableIndex):
        """ SelectAmplitudeCorrectionTable(self: niWLANA, channelString: str, analyzerIndex: int, tableIndex: int) -> int """
        pass

    def SelectMeasurements(self, measurement):
        """ SelectMeasurements(self: niWLANA, measurement: UInt32) -> int """
        pass

    def SelectMeasurementsWithTraces(self, measurement, enableTraces):
        """ SelectMeasurementsWithTraces(self: niWLANA, measurement: int, enableTraces: int) -> int """
        pass

    def Set80211AcAmpduEnabled(self, channelString, value):
        """ Set80211AcAmpduEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAcpEnabled(self, channel, value):
        """ SetAcpEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetAcpNumberOfAverages(self, channel, value):
        """ SetAcpNumberOfAverages(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetAcpNumberOfOffsets(self, channel, value):
        """ SetAcpNumberOfOffsets(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetAcpTraceEnabled(self, channel, value):
        """ SetAcpTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetAcquisitionLength(self, channelString, acquisitionLength):
        """ SetAcquisitionLength(self: niWLANA, channelString: str, acquisitionLength: float) -> int """
        pass

    def SetAggregationBit(self, channelString, value):
        """ SetAggregationBit(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAmplitudeCorrectionEnabled(self, channelString, value):
        """ SetAmplitudeCorrectionEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAmplitudeCorrectionTable(self, channelString, tableIndex, amplitudeCorrection, frequency, arraySize):
        """ SetAmplitudeCorrectionTable(self: niWLANA, channelString: str, tableIndex: int, amplitudeCorrection: Array[float], frequency: Array[float], arraySize: int) -> int """
        pass

    def SetAMPMMeasurementsAllTracesEnabled(self, channelString, value):
        """ SetAMPMMeasurementsAllTracesEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsAMAMCurveFitTraceEnabled(self, channelString, value):
        """ SetAMPMMeasurementsAMAMCurveFitTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsAMAMTraceEnabled(self, channelString, value):
        """ SetAMPMMeasurementsAMAMTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsAMPMCurveFitTraceEnabled(self, channelString, value):
        """ SetAMPMMeasurementsAMPMCurveFitTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsAMPMTraceEnabled(self, channelString, value):
        """ SetAMPMMeasurementsAMPMTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsAveragingMode(self, channelString, value):
        """ SetAMPMMeasurementsAveragingMode(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsDUTInputPowerLevel(self, channelString, value):
        """ SetAMPMMeasurementsDUTInputPowerLevel(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetAMPMMeasurementsEnabled(self, channelString, value):
        """ SetAMPMMeasurementsEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsMeanAcquiredWaveformTraceEnabled(self, channelString, value):
        """ SetAMPMMeasurementsMeanAcquiredWaveformTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAmpmMeasurementsMeasurementInterval(self, channelString, value):
        """ SetAmpmMeasurementsMeasurementInterval(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetAMPMMeasurementsMeasurementLength(self, channelString, value):
        """ SetAMPMMeasurementsMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetAMPMMeasurementsNumberOfAverages(self, channelString, value):
        """ SetAMPMMeasurementsNumberOfAverages(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMMeasurementsProcessedReferenceWaveformTraceEnabled(self, channelString, value):
        """ SetAMPMMeasurementsProcessedReferenceWaveformTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetAMPMReferenceWaveform(self, t0, dt, data, lenOfY):
        """ SetAMPMReferenceWaveform(self: niWLANA, t0: float, dt: float, data: Array[niComplexNumber], lenOfY: int) -> int """
        pass

    def SetAttributeString(self, channelString, attributeID, attributeValue):
        """ SetAttributeString(self: niWLANA, channelString: str, attributeID: niWLANAProperties, attributeValue: str) -> int """
        pass

    def SetAutoDetectionOfStandardMode(self, channel, value):
        """ SetAutoDetectionOfStandardMode(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetAutorangeMaxAcquisitionLength(self, channel, value):
        """ SetAutorangeMaxAcquisitionLength(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetAutorangeMaxIdleTime(self, channel, value):
        """ SetAutorangeMaxIdleTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetAutoSpanEnabled(self, channel, value):
        """ SetAutoSpanEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetCarrierFrequency(self, channelString, carrierFrequency):
        """ SetCarrierFrequency(self: niWLANA, channelString: str, carrierFrequency: float) -> int """
        pass

    def SetCCDFEnabled(self, channelString, value):
        """ SetCCDFEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetCCDFMeasurementLength(self, channelString, value):
        """ SetCCDFMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetCCDFNumberOfRecords(self, channelString, value):
        """ SetCCDFNumberOfRecords(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetCCDFRemoveDeadTime(self, channelString, value):
        """ SetCCDFRemoveDeadTime(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetCCDFTraceEnabled(self, channelString, value):
        """ SetCCDFTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetChannelBandwidth(self, channelString, channelBandwidth):
        """ SetChannelBandwidth(self: niWLANA, channelString: str, channelBandwidth: float) -> int """
        pass

    def SetCompatibilityVersion(self, channel, value):
        """ SetCompatibilityVersion(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDeviceInstantaneousBandwidth(self, channel, value):
        """ SetDeviceInstantaneousBandwidth(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssDataRate(self, channel, value):
        """ SetDsssDataRate(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodAllTracesEnabled(self, channel, value):
        """ SetDsssDemodAllTracesEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodAutoComputeAcquisitionLengthEnabled(self, channel, value):
        """ SetDSSSDemodAutoComputeAcquisitionLengthEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodAutoComputeMeasurementLengthEnabled(self, channelString, value):
        """ SetDSSSDemodAutoComputeMeasurementLengthEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetDSSSDemodBurstStartDetectionEnabled(self, channel, value):
        """ SetDSSSDemodBurstStartDetectionEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodCarrierFrequencyOffsetEstimationEnabled(self, channel, value):
        """ SetDSSSDemodCarrierFrequencyOffsetEstimationEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodCarrierSuppressionEstimationEnabled(self, channel, value):
        """ SetDSSSDemodCarrierSuppressionEstimationEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodConstellationTraceEnabled(self, channel, value):
        """ SetDsssDemodConstellationTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodDecodedBitsTraceEnabled(self, channel, value):
        """ SetDsssDemodDecodedBitsTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodEnabled(self, channelString, enabled):
        """ SetDSSSDemodEnabled(self: niWLANA, channelString: str, enabled: int) -> int """
        pass

    def SetDsssDemodEqualizationEnabled(self, channel, value):
        """ SetDsssDemodEqualizationEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodEvmPerChipTraceEnabled(self, channel, value):
        """ SetDsssDemodEvmPerChipTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodEvmPerSymbolTraceEnabled(self, channel, value):
        """ SetDsssDemodEvmPerSymbolTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodGatedPowerDataPowerEnabled(self, channel, value):
        """ SetDsssDemodGatedPowerDataPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodGatedPowerEnabled(self, channel, value):
        """ SetDsssDemodGatedPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodGatedPowerPreambleAndHeaderPowerEnabled(self, channel, value):
        """ SetDsssDemodGatedPowerPreambleAndHeaderPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodGatedPowerStartTime(self, channel, value):
        """ SetDsssDemodGatedPowerStartTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssDemodGatedPowerStopTime(self, channel, value):
        """ SetDsssDemodGatedPowerStopTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssDemodGatedPowerTotalPacketPowerEnabled(self, channel, value):
        """ SetDsssDemodGatedPowerTotalPacketPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodHeaderDetectionEnabled(self, channel, value):
        """ SetDsssDemodHeaderDetectionEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodIQGainImbalanceEstimationEnabled(self, channel, value):
        """ SetDSSSDemodIQGainImbalanceEstimationEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodLowpassFilteringEnabled(self, channel, value):
        """ SetDsssDemodLowpassFilteringEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodMacFrameCheckSequenceCheckEnabled(self, channel, value):
        """ SetDsssDemodMacFrameCheckSequenceCheckEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodMaximumChipsUsed(self, channel, value):
        """ SetDsssDemodMaximumChipsUsed(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodMeasurementLength(self, channelString, value):
        """ SetDSSSDemodMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetDsssDemodMeasurementStartLocation(self, channel, value):
        """ SetDsssDemodMeasurementStartLocation(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodNumberOfAverages(self, channelString, numberofAverages):
        """ SetDSSSDemodNumberOfAverages(self: niWLANA, channelString: str, numberofAverages: int) -> int """
        pass

    def SetDsssDemodPhaseTracking(self, channel, value):
        """ SetDsssDemodPhaseTracking(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodQuadratureSkewEstimationEnabled(self, channel, value):
        """ SetDSSSDemodQuadratureSkewEstimationEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodReferencePulseShapingFilterCoefficient(self, channel, value):
        """ SetDsssDemodReferencePulseShapingFilterCoefficient(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssDemodReferencePulseShapingFilterType(self, channel, value):
        """ SetDsssDemodReferencePulseShapingFilterType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDSSSDemodSampleClockOffsetEstimationEnabled(self, channel, value):
        """ SetDSSSDemodSampleClockOffsetEstimationEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodUserDefinedGatePowerEnabled(self, channel, value):
        """ SetDsssDemodUserDefinedGatePowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssDemodUserDefinedGateStartTime(self, channel, value):
        """ SetDsssDemodUserDefinedGateStartTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssDemodUserDefinedGateStopTime(self, channel, value):
        """ SetDsssDemodUserDefinedGateStopTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssPayloadLength(self, channel, value):
        """ SetDsssPayloadLength(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetDsssPowerRampDownHighThreshold(self, channel, value):
        """ SetDsssPowerRampDownHighThreshold(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssPowerRampDownLowThreshold(self, channel, value):
        """ SetDsssPowerRampDownLowThreshold(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDSSSPowerRampMeasurementEnabled(self, channelString, enabled):
        """ SetDSSSPowerRampMeasurementEnabled(self: niWLANA, channelString: str, enabled: int) -> int """
        pass

    def SetDSSSPowerRampMeasurementLength(self, channelString, value):
        """ SetDSSSPowerRampMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetDSSSPowerRampMeasurementNumberOfAverages(self, channelString, numberofAverages):
        """ SetDSSSPowerRampMeasurementNumberOfAverages(self: niWLANA, channelString: str, numberofAverages: int) -> int """
        pass

    def SetDsssPowerRampUpHighThreshold(self, channel, value):
        """ SetDsssPowerRampUpHighThreshold(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDsssPowerRampUpLowThreshold(self, channel, value):
        """ SetDsssPowerRampUpLowThreshold(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetDualCarrierModulationEnabled(self, channelString, value):
        """ SetDualCarrierModulationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetETSIIBEDeltaACLR(self, channelString, dataArray, dataArraySize):
        """ SetETSIIBEDeltaACLR(self: niWLANA, channelString: str, dataArray: Array[float], dataArraySize: int) -> int """
        pass

    def SetETSIIBEDeviceEmissionClass(self, channelString, value):
        """ SetETSIIBEDeviceEmissionClass(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetETSIIBEDUTAverageOutputPower(self, channelString, value):
        """ SetETSIIBEDUTAverageOutputPower(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetETSIIBEEnabled(self, channelString, value):
        """ SetETSIIBEEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetETSIIBENumberOfAverages(self, channelString, value):
        """ SetETSIIBENumberOfAverages(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetETSIIBENumberOfOffsets(self, channelString, value):
        """ SetETSIIBENumberOfOffsets(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetETSIIBETraceEnabled(self, channelString, value):
        """ SetETSIIBETraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetETSIIBETransmitChannelPSDLimit(self, channelString, value):
        """ SetETSIIBETransmitChannelPSDLimit(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetFecCodingType(self, channel, value):
        """ SetFecCodingType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetFftSize(self, channel, value):
        """ SetFftSize(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetFftWindowSize(self, channel, value):
        """ SetFftWindowSize(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetFftWindowType(self, channel, value):
        """ SetFftWindowType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetGatedSpectrumAveragingType(self, channelString, value):
        """ SetGatedSpectrumAveragingType(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetGatedSpectrumEnabled(self, channel, value):
        """ SetGatedSpectrumEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetGatedSpectrumMeasurementLength(self, channelString, value):
        """ SetGatedSpectrumMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetGatedSpectrumMode(self, channel, value):
        """ SetGatedSpectrumMode(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetGuardInterval(self, channel, value):
        """ SetGuardInterval(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetGuardIntervalType(self, channel, value):
        """ SetGuardIntervalType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetHELTFSize(self, channelString, value):
        """ SetHELTFSize(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetHESIGBDCMEnabled(self, channelString, value):
        """ SetHESIGBDCMEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetHESIGBMCSIndex(self, channelString, value):
        """ SetHESIGBMCSIndex(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetIqPowerEdgeReferenceTriggerEnabled(self, channel, value):
        """ SetIqPowerEdgeReferenceTriggerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetIQPowerEdgeReferenceTriggerEnabled(self, channelString, value):
        """ SetIQPowerEdgeReferenceTriggerEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetLDPCExtraSymbolUsed(self, channelString, value):
        """ SetLDPCExtraSymbolUsed(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetLOFrequencyOffset(self, channelString, value):
        """ SetLOFrequencyOffset(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetLOOffsetMode(self, channelString, value):
        """ SetLOOffsetMode(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetLOSharingEnabled(self, channelString, value):
        """ SetLOSharingEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetMaxInputPower(self, channel, value):
        """ SetMaxInputPower(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetMaxSpectralDensityEnabled(self, channel, value):
        """ SetMaxSpectralDensityEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetMaxSpectralDensityNumberOfAverages(self, channel, value):
        """ SetMaxSpectralDensityNumberOfAverages(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetMcsIndex(self, channel, value):
        """ SetMcsIndex(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetMidamblePeriodicity(self, channelString, value):
        """ SetMidamblePeriodicity(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetMultiSegmentMeasurementMode(self, channelString, value):
        """ SetMultiSegmentMeasurementMode(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetMUMimoLtfModeEnabled(self, channelString, value):
        """ SetMUMimoLtfModeEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetNoiseCompensationCarrierFrequencies(self, channelString, dataArray):
        """ SetNoiseCompensationCarrierFrequencies(self: niWLANA, channelString: str, dataArray: Array[float]) -> int """
        pass

    def SetNoiseCompensationEnabled(self, channelString, value):
        """ SetNoiseCompensationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetNoiseCompensationMaxChannelBandwidths(self, channelString, dataArray):
        """ SetNoiseCompensationMaxChannelBandwidths(self: niWLANA, channelString: str, dataArray: Array[float]) -> int """
        pass

    def SetNoiseCompensationMaximumReferenceLevel(self, channelString, value):
        """ SetNoiseCompensationMaximumReferenceLevel(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetNoiseCompensationMinimumReferenceLevel(self, channelString, value):
        """ SetNoiseCompensationMinimumReferenceLevel(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetNoiseCompensationReferenceLevelStepSize(self, channelString, value):
        """ SetNoiseCompensationReferenceLevelStepSize(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetNonHTModulationMode(self, channelString, value):
        """ SetNonHTModulationMode(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetNumberOfExtensionSpatialStreams(self, channel, value):
        """ SetNumberOfExtensionSpatialStreams(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetNumberOfHELTFSymbols(self, channelString, value):
        """ SetNumberOfHELTFSymbols(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetNumberOfHESIGBSymbols(self, channelString, value):
        """ SetNumberOfHESIGBSymbols(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetNumberOfReceiveChannels(self, channelString, numberofReceiveChannels):
        """ SetNumberOfReceiveChannels(self: niWLANA, channelString: str, numberofReceiveChannels: int) -> int """
        pass

    def SetNumberOfSegments(self, channelString, value):
        """ SetNumberOfSegments(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetNumberOfSpaceTimeStreams(self, channelString, value):
        """ SetNumberOfSpaceTimeStreams(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetObwEnabled(self, channel, value):
        """ SetObwEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetObwNumberOfAverages(self, channel, value):
        """ SetObwNumberOfAverages(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMChannelEstimationOnLLTFEnabled(self, channelString, value):
        """ SetOFDMChannelEstimationOnLLTFEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDataRate(self, channel, value):
        """ SetOfdmDataRate(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemod80211ahPreambleDetectionEnabled(self, channel, value):
        """ SetOfdmDemod80211ahPreambleDetectionEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemod80211nPlcpFrameDetectionEnabled(self, channel, value):
        """ SetOfdmDemod80211nPlcpFrameDetectionEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemod80Plus80FilterBeforeSyncEnabled(self, channel, value):
        """ SetOfdmDemod80Plus80FilterBeforeSyncEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemod80Plus80OversamplingFactor(self, channel, value):
        """ SetOfdmDemod80Plus80OversamplingFactor(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetOFDMDemod80Plus80SegmentIndex(self, channelString, value):
        """ SetOFDMDemod80Plus80SegmentIndex(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodAllTracesEnabled(self, channel, value):
        """ SetOfdmDemodAllTracesEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodAmplitudeTrackingEnabled(self, channel, value):
        """ SetOfdmDemodAmplitudeTrackingEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodAutoComputeAcquisitionLengthEnabled(self, channel, value):
        """ SetOfdmDemodAutoComputeAcquisitionLengthEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodAutoComputeMeasurementLengthEnabled(self, channelString, value):
        """ SetOFDMDemodAutoComputeMeasurementLengthEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodBurstStartDetectionEnabled(self, channelString, value):
        """ SetOfdmDemodBurstStartDetectionEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodCarrierFrequencyLeakageEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodCarrierFrequencyLeakageEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodCarrierFrequencyOffsetCCDFTraceEnabled(self, channelString, value):
        """ SetOFDMDemodCarrierFrequencyOffsetCCDFTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodCarrierFrequencyOffsetEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodCarrierFrequencyOffsetEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodCfoEstimationMethod(self, channel, value):
        """ SetOfdmDemodCfoEstimationMethod(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodChannelEstimationMethod(self, channelString, value):
        """ SetOFDMDemodChannelEstimationMethod(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodChannelEVMEnabled(self, channelString, value):
        """ SetOFDMDemodChannelEVMEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodChannelFrequencyResponseTraceEnabled(self, channel, value):
        """ SetOfdmDemodChannelFrequencyResponseTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodChannelFrequencyResponseTraceMode(self, channel, value):
        """ SetOfdmDemodChannelFrequencyResponseTraceMode(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodChannelMatrixPowerEnabled(self, channelString, value):
        """ SetOFDMDemodChannelMatrixPowerEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodChannelTrackingEnabled(self, channel, value):
        """ SetOfdmDemodChannelTrackingEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodCombinedSignalDemodulationEnabled(self, channelString, value):
        """ SetOfdmDemodCombinedSignalDemodulationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodCommonClockSourceEnabled(self, channel, value):
        """ SetOFDMDemodCommonClockSourceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodCommonPhaseErrorEstimationEnabled(self, channelString, value):
        """ SetOfdmDemodCommonPhaseErrorEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodCommonPilotErrorEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodCommonPilotErrorEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodCommonPilotErrorTraceEnabled(self, channelString, value):
        """ SetOFDMDemodCommonPilotErrorTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodConstellationTraceEnabled(self, channel, value):
        """ SetOfdmDemodConstellationTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodDataEvmPerSymbolTraceEnabled(self, channel, value):
        """ SetOfdmDemodDataEvmPerSymbolTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodDecodedBitsTraceEnabled(self, channel, value):
        """ SetOfdmDemodDecodedBitsTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodDecodedHeaderTraceEnabled(self, channelString, value):
        """ SetOFDMDemodDecodedHeaderTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodEnabled(self, channel, value):
        """ SetOfdmDemodEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodEvmPerSubcarrierPerSymbolTraceEnabled(self, channel, value):
        """ SetOfdmDemodEvmPerSubcarrierPerSymbolTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodEvmPerSubcarrierTraceEnabled(self, channel, value):
        """ SetOfdmDemodEvmPerSubcarrierTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodEvmPerSymbolPerSubcarrierTraceEnabled(self, channel, value):
        """ SetOfdmDemodEvmPerSymbolPerSubcarrierTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodEvmPerSymbolTraceEnabled(self, channel, value):
        """ SetOfdmDemodEvmPerSymbolTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodGatedPowerDataPowerEnabled(self, channel, value):
        """ SetOfdmDemodGatedPowerDataPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodGatedPowerEnabled(self, channel, value):
        """ SetOfdmDemodGatedPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodGatedPowerPreambleAndHeaderPowerEnabled(self, channel, value):
        """ SetOfdmDemodGatedPowerPreambleAndHeaderPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodGatedPowerStartTime(self, channel, value):
        """ SetOfdmDemodGatedPowerStartTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetOfdmDemodGatedPowerStopTime(self, channel, value):
        """ SetOfdmDemodGatedPowerStopTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetOfdmDemodGatedPowerTotalPacketPowerEnabled(self, channel, value):
        """ SetOfdmDemodGatedPowerTotalPacketPowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodGroupDelayTraceEnabled(self, channel, value):
        """ SetOfdmDemodGroupDelayTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodGroupDelayTraceMode(self, channel, value):
        """ SetOfdmDemodGroupDelayTraceMode(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodHeaderDetectionEnabled(self, channel, value):
        """ SetOfdmDemodHeaderDetectionEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodIQGainImbalance(self, channelString, value):
        """ SetOfdmDemodIQGainImbalance(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetOFDMDemodIQGainImbalanceCompensationEnabled(self, channelString, value):
        """ SetOFDMDemodIQGainImbalanceCompensationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodIQGainImbalanceEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodIQGainImbalanceEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodIQGainImbalancePerSubcarrierTraceEnabled(self, channelString, value):
        """ SetOFDMDemodIQGainImbalancePerSubcarrierTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodIQImpairmentsCompensationEnabled(self, channelString, value):
        """ SetOfdmDemodIQImpairmentsCompensationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodIQImpairmentsPerSubcarrierEnabled(self, channelString, value):
        """ SetOfdmDemodIQImpairmentsPerSubcarrierEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodIQMismatchSignalModel(self, channelString, value):
        """ SetOFDMDemodIQMismatchSignalModel(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodLowpassFilteringEnabled(self, channel, value):
        """ SetOfdmDemodLowpassFilteringEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodMacFrameCheckSequenceCheckEnabled(self, channel, value):
        """ SetOfdmDemodMacFrameCheckSequenceCheckEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodMaximumSymbolsUsed(self, channel, value):
        """ SetOfdmDemodMaximumSymbolsUsed(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodMeasurementLength(self, channelString, value):
        """ SetOFDMDemodMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetOfdmDemodMeasurementStartLocation(self, channel, value):
        """ SetOfdmDemodMeasurementStartLocation(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodNonHTModulationDetectionEnabled(self, channelString, value):
        """ SetOFDMDemodNonHTModulationDetectionEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodNumberOfAverages(self, channelString, numberofAverages):
        """ SetOFDMDemodNumberOfAverages(self: niWLANA, channelString: str, numberofAverages: int) -> int """
        pass

    def SetOfdmDemodNumberOfAverages(self, channel, value):
        """ SetOfdmDemodNumberOfAverages(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodPhaseNoisePSDTraceEnabled(self, channelString, value):
        """ SetOFDMDemodPhaseNoisePSDTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodPhaseTracking(self, channel, value):
        """ SetOfdmDemodPhaseTracking(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodPilotEvmPerSymbolTraceEnabled(self, channel, value):
        """ SetOfdmDemodPilotEvmPerSymbolTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodPreambleFrequencyErrorTraceEnabled(self, channelString, value):
        """ SetOFDMDemodPreambleFrequencyErrorTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodQuadratureSkew(self, channelString, value):
        """ SetOfdmDemodQuadratureSkew(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetOFDMDemodQuadratureSkewCompensationEnabled(self, channelString, value):
        """ SetOFDMDemodQuadratureSkewCompensationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodQuadratureSkewEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodQuadratureSkewEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodQuadratureSkewPerSubcarrierTraceEnabled(self, channelString, value):
        """ SetOfdmDemodQuadratureSkewPerSubcarrierTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodRefDataConstellationIdentifier(self, channelString, attrVal):
        """ SetOFDMDemodRefDataConstellationIdentifier(self: niWLANA, channelString: str, attrVal: str) -> int """
        pass

    def SetOFDMDemodReferenceConstellationTraceEnabled(self, channel, value):
        """ SetOFDMDemodReferenceConstellationTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMDemodReferenceDataConstellationEnabled(self, channelString, value):
        """ SetOFDMDemodReferenceDataConstellationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodSampleClockOffsetEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodSampleClockOffsetEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodServiceBitsTraceEnabled(self, channelString, value):
        """ SetOfdmDemodServiceBitsTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodSpectralFlatnessMarginEnabled(self, channelString, value):
        """ SetOFDMDemodSpectralFlatnessMarginEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodSpectralFlatnessTraceEnabled(self, channel, value):
        """ SetOfdmDemodSpectralFlatnessTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodStreamPowerEnabled(self, channelString, value):
        """ SetOfdmDemodStreamPowerEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodSymbolTimingAdjustment(self, channel, value):
        """ SetOfdmDemodSymbolTimingAdjustment(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetOfdmDemodTimeTrackingEnabled(self, channel, value):
        """ SetOfdmDemodTimeTrackingEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodTimingSkew(self, channelString, value):
        """ SetOfdmDemodTimingSkew(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetOFDMDemodTimingSkewCompensationEnabled(self, channelString, value):
        """ SetOFDMDemodTimingSkewCompensationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodTimingSkewEstimationEnabled(self, channelString, value):
        """ SetOFDMDemodTimingSkewEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodUnusedToneErrorEnabled(self, channelString, value):
        """ SetOFDMDemodUnusedToneErrorEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodUnusedToneErrorMaskReference(self, channelString, value):
        """ SetOFDMDemodUnusedToneErrorMaskReference(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMDemodUnusedToneErrorTraceEnabled(self, channelString, value):
        """ SetOFDMDemodUnusedToneErrorTraceEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmDemodUserDefinedGatePowerEnabled(self, channel, value):
        """ SetOfdmDemodUserDefinedGatePowerEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOfdmDemodUserDefinedGateStartTime(self, channel, value):
        """ SetOfdmDemodUserDefinedGateStartTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetOfdmDemodUserDefinedGateStopTime(self, channel, value):
        """ SetOfdmDemodUserDefinedGateStopTime(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetOfdmDemodVhtSigBCrcCheckEnabled(self, channel, value):
        """ SetOfdmDemodVhtSigBCrcCheckEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMLSIGPayloadLength(self, channelString, value):
        """ SetOFDMLSIGPayloadLength(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMNumberOfUsers(self, channelString, value):
        """ SetOFDMNumberOfUsers(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMPacketExtensionDisambiguity(self, channelString, value):
        """ SetOFDMPacketExtensionDisambiguity(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOfdmPayloadLength(self, channel, value):
        """ SetOfdmPayloadLength(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetOFDMPhaseErrorEstimationEnabled(self, channelString, value):
        """ SetOFDMPhaseErrorEstimationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMPPDUType(self, channelString, value):
        """ SetOFDMPPDUType(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMPreFECPaddingFactor(self, channelString, value):
        """ SetOFDMPreFECPaddingFactor(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMRUOffset(self, channelString, value):
        """ SetOFDMRUOffset(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMRUSize(self, channelString, value):
        """ SetOFDMRUSize(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOFDMStreamPowerEnabled(self, channelString, value):
        """ SetOFDMStreamPowerEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOptimizeReferenceLevelForEVMEnabled(self, channelString, value):
        """ SetOptimizeReferenceLevelForEVMEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetOptimizeReferenceLevelForEVMMargin(self, channelString, value):
        """ SetOptimizeReferenceLevelForEVMMargin(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetPowerLevel(self, channelString, maxInputPower):
        """ SetPowerLevel(self: niWLANA, channelString: str, maxInputPower: float) -> int """
        pass

    def SetRbw(self, channel, value):
        """ SetRbw(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetRbwDefinition(self, channel, value):
        """ SetRbwDefinition(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetReferenceDataConstellation(self, channelString, I, Q, dataArraySize):
        """ SetReferenceDataConstellation(self: niWLANA, channelString: str, I: Array[float], Q: Array[float], dataArraySize: int) -> int """
        pass

    def SetSampleClockRateFactor(self, channelString, value):
        """ SetSampleClockRateFactor(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetScalarAttributeF64(self, channelString, attributeID, attributeValue):
        """ SetScalarAttributeF64(self: niWLANA, channelString: str, attributeID: niWLANAProperties, attributeValue: float) -> int """
        pass

    def SetScalarAttributeI32(self, channelString, attributeID, attributeValue):
        """ SetScalarAttributeI32(self: niWLANA, channelString: str, attributeID: niWLANAProperties, attributeValue: int) -> int """
        pass

    def SetScramblerSeed(self, channelString, value):
        """ SetScramblerSeed(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetShortGuardIntervalB1Bit(self, channelString, value):
        """ SetShortGuardIntervalB1Bit(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetSpaceTimeStreamOffset(self, channelString, value):
        """ SetSpaceTimeStreamOffset(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetSpan(self, channel, value):
        """ SetSpan(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetSpectralMaskCenterFrequency(self, channel, value):
        """ SetSpectralMaskCenterFrequency(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetSpectralMaskCombinedMaskEnabled(self, channel, value):
        """ SetSpectralMaskCombinedMaskEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetSpectralMaskEnabled(self, channelString, enabled):
        """ SetSpectralMaskEnabled(self: niWLANA, channelString: str, enabled: int) -> int """
        pass

    def SetSpectralMaskFrequencyOffsets(self, channel, data, dataSize):
        """ SetSpectralMaskFrequencyOffsets(self: niWLANA, channel: str, data: Array[float], dataSize: int) -> int """
        pass

    def SetSpectralMaskNumberOfAverages(self, channelString, numberofAverages):
        """ SetSpectralMaskNumberOfAverages(self: niWLANA, channelString: str, numberofAverages: int) -> int """
        pass

    def SetSpectralMaskPowerOffsets(self, channel, data, dataSize):
        """ SetSpectralMaskPowerOffsets(self: niWLANA, channel: str, data: Array[float], dataSize: int) -> int """
        pass

    def SetSpectralMaskReferenceLevel(self, channel, value):
        """ SetSpectralMaskReferenceLevel(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetSpectralMaskReferenceLevelType(self, channel, value):
        """ SetSpectralMaskReferenceLevelType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetSpectralMaskTraceEnabled(self, channel, value):
        """ SetSpectralMaskTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetSpectralMaskTransmitPowerClass(self, channelString, value):
        """ SetSpectralMaskTransmitPowerClass(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetSpectralMaskType(self, channel, value):
        """ SetSpectralMaskType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetSpectralMeasurementChannelPowerMeasuremntBW(self, channelString, value):
        """ SetSpectralMeasurementChannelPowerMeasuremntBW(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetSpectralMeasurementsAllEnabled(self, channel, value):
        """ SetSpectralMeasurementsAllEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetSpectralMeasurementsChannelPowerAutoMeasureBwEnabled(self, channelString, value):
        """ SetSpectralMeasurementsChannelPowerAutoMeasureBwEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetSpectralMeasurementsChannelPowerEnabled(self, channelString, value):
        """ SetSpectralMeasurementsChannelPowerEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetSpectralMeasurementsChannelPowerMeasurementBandwidth(self, channelString, value):
        """ SetSpectralMeasurementsChannelPowerMeasurementBandwidth(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetSpectralMeasurementsChannelPowerNumberOfAverages(self, channelString, value):
        """ SetSpectralMeasurementsChannelPowerNumberOfAverages(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetSpectralMeasurementsChPowerAutoMeasureBWEnabled(self, channelString, value):
        """ SetSpectralMeasurementsChPowerAutoMeasureBWEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetStandard(self, channelString, standard):
        """ SetStandard(self: niWLANA, channelString: str, standard: int) -> int """
        pass

    def SetSTBCAllStreamsEnabled(self, channelString, value):
        """ SetSTBCAllStreamsEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetStbcIndex(self, channel, value):
        """ SetStbcIndex(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetSwapIAndQEnabled(self, channelString, value):
        """ SetSwapIAndQEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetTClkSynchronizationEnabled(self, channelString, value):
        """ SetTClkSynchronizationEnabled(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetTransmissionMode(self, channelString, value):
        """ SetTransmissionMode(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetTriggerDelay(self, channel, value):
        """ SetTriggerDelay(self: niWLANA, channel: str, value: float) -> int """
        pass

    def SetTxPowerBurstDetectionEnabled(self, channel, value):
        """ SetTxPowerBurstDetectionEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetTxPowerMeasurementEnabled(self, channelString, enabled):
        """ SetTxPowerMeasurementEnabled(self: niWLANA, channelString: str, enabled: int) -> int """
        pass

    def SetTxPowerMeasurementLength(self, channelString, value):
        """ SetTxPowerMeasurementLength(self: niWLANA, channelString: str, value: float) -> int """
        pass

    def SetTxPowerMeasurementMode(self, channelString, value):
        """ SetTxPowerMeasurementMode(self: niWLANA, channelString: str, value: int) -> int """
        pass

    def SetTxPowerMeasurementNumberOfAverages(self, channelString, numberofAverages):
        """ SetTxPowerMeasurementNumberOfAverages(self: niWLANA, channelString: str, numberofAverages: int) -> int """
        pass

    def SetTxpowerMeasurementsEnabled(self, channel, value):
        """ SetTxpowerMeasurementsEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetTxpowerMeasurementsMode(self, channel, value):
        """ SetTxpowerMeasurementsMode(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetTxpowerMeasurementsNumberOfAverages(self, channel, value):
        """ SetTxpowerMeasurementsNumberOfAverages(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetTxpowerMeasurementsPvtTraceEnabled(self, channel, value):
        """ SetTxpowerMeasurementsPvtTraceEnabled(self: niWLANA, channel: str, value: int) -> int """
        pass

    def SetVectorAttributeF64(self, channelString, attributeID, data, dataArraySize):
        """ SetVectorAttributeF64(self: niWLANA, channelString: str, attributeID: niWLANAProperties, data: Array[float], dataArraySize: int) -> int """
        pass

    def Set_80211ahPreambleType(self, channel, value):
        """ Set_80211ahPreambleType(self: niWLANA, channel: str, value: int) -> int """
        pass

    def Set_80211nPlcpFrameFormat(self, channel, value):
        """ Set_80211nPlcpFrameFormat(self: niWLANA, channel: str, value: int) -> int """
        pass

    def TestForError(self, status):
        """ TestForError(self: niWLANA, status: int) -> int """
        pass

    @staticmethod
    def WLANA_RFSAAutoLevel(rFSASession, hardwareChannelString, carrierFrequency, bandwidth, measurementInterval, maxNumberofIterations, resultantReferenceLevel):
        """ WLANA_RFSAAutoLevel(rFSASession: HandleRef, hardwareChannelString: str, carrierFrequency: float, bandwidth: float, measurementInterval: float, maxNumberofIterations: int) -> (int, float) """
        pass

    @staticmethod
    def WLANA_RFSAAutoTriggerRoute(rFSASession, noOfChannels, triggerLine0, lenOfTrig0, triggerLine1, lenOfTrig1, reference, lenOfReference, isInSameBus, busNumber, sizeOfBusNo, isDefaultLineSelected):
        """ WLANA_RFSAAutoTriggerRoute(rFSASession: HandleRef, noOfChannels: int, triggerLine0: str, lenOfTrig0: int, triggerLine1: str, lenOfTrig1: int, reference: str, lenOfReference: int, busNumber: Array[int], sizeOfBusNo: int) -> (int, int, int) """
        pass

    @staticmethod
    def WLANA_RFSATriggerUnroute(triggerLine0, triggerLine1, reference, isInSameBus, busNumber, sizeOfBusNo, isDefaultLineSelected):
        """ WLANA_RFSATriggerUnroute(triggerLine0: str, triggerLine1: str, reference: str, isInSameBus: int, busNumber: Array[int], sizeOfBusNo: int, isDefaultLineSelected: int) -> int """
        pass

    @staticmethod
    def WLANSA_RFSAAutoLevel(rFSASession, hardwareChannelString, bandwidth, measurementInterval, maxNumberofIterations, resultantReferenceLevel):
        """ WLANSA_RFSAAutoLevel(rFSASession: HandleRef, hardwareChannelString: str, bandwidth: float, measurementInterval: float, maxNumberofIterations: int) -> (int, float) """
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
        __new__(cls: type, toolkitCompatibilityVersion: int)
        __new__(cls: type, sessionName: str, toolkitCompatibilityVersion: int) -> int
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: niWLANA) -> HandleRef

"""



class niWLANAConstants(object):
    """ niWLANAConstants() """
    AcpMeasurement = 4096
    AcquisitionTypeIq = 0
    AcquisitionTypeSpectrum = 1
    AmpmMeasurementsAveragingModeExponential = 0
    AmpmMeasurementsAveragingModeRepeat = 1
    AutoDetectionStandardModeOff = 0
    AutoDetectionStandardModePacketFilter = 2
    CcdfMeasurement = 1024
    CfoEstimationMethodFullPreamble = 3
    CfoEstimationMethodInitialPreamble = 0
    CfoEstimationMethodPreambleAndData = 1
    CfoEstimationMethodPreambleAndPilots = 1
    CfoEstimationMethodPreambleAndPilotsAndData = 2
    CfoEstimationMethodPreambleOnly = 0
    ChannelEstimationMethodPreamble = 0
    ChannelEstimationMethodPreambleAndData = 1
    ChannelPowerMeasurement = 512
    CompatibilityVersion010000 = 10000
    CompatibilityVersion020000 = 20000
    CompatibilityVersion030000 = 30000
    CompatibilityVersion040000 = 40000
    CompatibilityVersion050000 = 50000
    DsssDataRate1 = 0
    DsssDataRate11Cck = 4
    DsssDataRate11Pbcc = 5
    DsssDataRate2 = 1
    DsssDataRate22 = 6
    DsssDataRate33 = 7
    DsssDataRate5p5Cck = 2
    DsssDataRate5p5Pbcc = 3
    DsssDemodHeaderChecksumPassedFalse = 0
    DsssDemodHeaderChecksumPassedTrue = 1
    DsssDemodHeaderChecksumPassedVarious = 2
    DsssDemodMeasurement = 4
    DsssDemodSfdFoundFalse = 0
    DsssDemodSfdFoundTrue = 1
    DsssDemodSfdFoundVarious = 2
    DsssDemodWithGatedPowerMeasurement = 8
    DsssPhaseTrackingInstantaneous = 1
    DsssPhaseTrackingStandard = 0
    DsssPowerRampMeasurement = 16
    EtsiDeviceEmissionClass1 = 0
    EtsiDeviceEmissionClass2 = 1
    EtsiDeviceEmissionClass3 = 2
    EtsiDeviceEmissionClass4 = 3
    EtsiDeviceEmissionClass5 = 4
    EtsiIbeMeasurement = 8192
    False = 0
    FecCodingTypeBcc = 0
    FecCodingTypeLdpc = 1
    FileOperationModeCreate = 3
    FileOperationModeCreateOrReplace = 2
    FileOperationModeOpen = 0
    FileOperationModeOpenOrCreate = 1
    FilterGaussian = 3
    FilterRaisedCosine = 1
    FilterRectangular = 0
    FilterRootRaisedCosine = 2
    ForceSyncDisabled = 0
    ForceSyncEnabled = 1
    FrequencyBand2p4Ghz = 0
    FrequencyBand5Ghz = 1
    GatedSpectrumAveragingTypeLog = 1
    GatedSpectrumAveragingTypePeakHold = 2
    GatedSpectrumAveragingTypeRms = 0
    GatedSpectrumModeAcquisitionLength = 1
    GatedSpectrumModeMeasurementLength = 1
    GatedSpectrumModeRbw = 0
    GatedSpectrumModeRbwAndAcquisitionLength = 2
    GatedSpectrumModeRbwAndMeasurementLength = 2
    GuardIntervalTypeLong = 0
    GuardIntervalTypeOneByEight = 1
    GuardIntervalTypeOneByFour = 0
    GuardIntervalTypeOneBySixteen = 2
    GuardIntervalTypeShort = 1
    HeLtfSize1X = 2
    HeLtfSize2X = 1
    HeLtfSize4X = 0
    HeLtfSizeAuto = -1
    LOFrequencyOffsetModeAuto = 0
    LOFrequencyOffsetModeDisabled = 2
    LOFrequencyOffsetModeUserDefined = 1
    LoSharingEnabledFalse = 0
    LoSharingEnabledTrue = 1
    LOSourceExternal = 0
    LOSourceOnboard = 2
    LOSourcePreviousDevice = 1
    LOSourceSgSaShared = 3
    MaxSpectralDensityMeasurement = 256
    MidamblePeriodicity10Symbols = 1
    MidamblePeriodicity20Symbols = 2
    MidamblePeriodicityNone = 0
    MultipleAnalyzers = 1
    NoiseCompensationAppliedFull = 2
    NoiseCompensationAppliedNone = 0
    NoiseCompensationAppliedPartial = 1
    NotApplicable = -3
    ObwMeasurement = 128
    OfdmDataRate12 = 2
    OfdmDataRate18 = 3
    OfdmDataRate24 = 4
    OfdmDataRate36 = 5
    OfdmDataRate48 = 6
    OfdmDataRate54 = 7
    OfdmDataRate6 = 0
    OfdmDataRate9 = 1
    OfdmDemodCfrTraceModeDeviationFromLinearPhase = 1
    OfdmDemodCfrTraceModeWithLinearPhase = 0
    OfdmDemodExtendedRangeSuPpdu = 2
    OfdmDemodGroupDelayTraceModeDeviationFromAverageGroupDelay = 1
    OfdmDemodGroupDelayTraceModeWithAverageGroupDelay = 0
    OfdmDemodMeasurement = 1
    OfdmDemodPpduTypeMuPpdu = 1
    OfdmDemodPpduTypeSuPpdu = 0
    OfdmDemodRuSize106 = 106
    OfdmDemodRuSize242 = 242
    OfdmDemodRuSize26 = 26
    OfdmDemodRuSize2x996 = 1992
    OfdmDemodRuSize484 = 484
    OfdmDemodRuSize52 = 52
    OfdmDemodRuSize996 = 996
    OfdmDemodRuSizeAuto = -1
    OfdmDemodTriggerBasedPpdu = 3
    OfdmDemodWithGatedPowerMeasurement = 2
    OfdmIqMismatchCorrectionSignalModelRx = 1
    OfdmIqMismatchCorrectionSignalModelTx = 0
    OfdmNonHtModulationModeOff = 0
    OfdmNonHtModulationModeOn = 1
    OfdmPhaseTrackingInstantaneous = 1
    OfdmPhaseTrackingNone = 2
    OfdmPhaseTrackingStandard = 0
    OfdmPhaseTrackingStandardWithCubicSplineFit = 3
    OfdmUnusedToneErrorMaskReferenceHighPower = 1
    OfdmUnusedToneErrorMaskReferenceLowPower = 0
    PortTypeRFIn = 0
    PortTypeRFOut = 1
    PreambleTypeLongPreamble = 1
    PreambleTypeShortPreamble = 0
    PreambleTypeVarious = 2
    RbwDefinition3db = 0
    RbwDefinition6db = 1
    RbwDefinitionBinWidth = 3
    RbwDefinitionEnbw = 2
    ResultGuardIntervalTypeUnknown = -2
    ResultGuardIntervalTypeVarious = -1
    Results80211ahPreambleTypeNotApplicable = -3
    Results80211ahPreambleTypeUnknown = -2
    Results80211ahPreambleTypeVarious = -1
    Results80211nPlcpFrameFormatGreenfield = 1
    Results80211nPlcpFrameFormatMixed = 0
    Results80211nPlcpFrameFormatUnknown = -2
    Results80211nPlcpFrameFormatVarious = -1
    ResultsDsssDataRateVarious = 8
    ResultsFecCodingTypeVarious = 2
    ResultsOfdmDataRateVarious = 8
    SingleAnalyzer = 0
    SpectralMaskMeasurement = 64
    SpectralMaskReferenceLevelTypePeakSignalPower = 0
    SpectralMaskReferenceLevelTypeUserDefined = 1
    SpectralMaskTransmitPowerClassA = 0
    SpectralMaskTransmitPowerClassB = 1
    SpectralMaskTransmitPowerClassC = 2
    SpectralMaskTransmitPowerClassD = 3
    SpectralMaskTypeStandard = 0
    SpectralMaskTypeStandardAt5Ghz = 2
    SpectralMaskTypeUserDefined = 1
    Standard80211acMimoOfdm = 4
    Standard80211afMimoOfdm = 6
    Standard80211agjpOfdm = 0
    Standard80211agOfdm = 0
    Standard80211ahMimoOfdm = 5
    Standard80211axMimoOfdm = 9
    Standard80211bgDsss = 1
    Standard80211gDsssOfdm = 2
    Standard80211jOfdm = 7
    Standard80211nMimoOfdm = 3
    Standard80211pOfdm = 8
    StandardUnknown = -2
    TclkSynchronisationEnabledFalse = 0
    TclkSynchronisationEnabledTrue = 1
    TransmissionModeDownlink = 0
    TransmissionModeUplink = 1
    True = 1
    TvhtMode1 = 0
    TvhtMode2C = 1
    TvhtMode2N = 2
    TvhtMode4C = 3
    TvhtMode4N = 4
    TxPowerMeasurementsModeEntireAcquisition = 1
    TxPowerMeasurementsModeFirstPacket = 0
    TxpPowerMeasurement = 32
    Various = -1
    Window4TermBlackmanHarris = 7
    Window7TermBlackmanHarris = 8
    WindowBlackman = 5
    WindowBlackmanHarris = 3
    WindowExactBlackman = 4
    WindowFlatTop = 6
    WindowHamming = 2
    WindowHanning = 1
    WindowLowSideLobe = 9
    WindowUniform = 0
    _80211ahPreambleTypeLong = 1
    _80211ahPreambleTypeShort = 0


class niWLANAProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum niWLANAProperties, values: _80211ahPreambleType (797), _80211nPlcpFrameFormat (280), AcpEnabled (798), AcpLowerAbsolutePower (804), AcpLowerRelativePower (803), AcpNumberOfAverages (799), AcpNumberOfOffsets (801), AcpTraceEnabled (800), AcpUpperAbsolutePower (806), AcpUpperRelativePower (805), AcquisitionLength (2), AggregationBit (235), AmplitudeCorrectionEnabled (869), AmpmMeasurementsAllTracesEnabled (785), AmpmMeasurementsAmamCurveFitTraceEnabled (661), AmpmMeasurementsAmamTraceEnabled (659), AmpmMeasurementsAmpmCurveFitTraceEnabled (662), AmpmMeasurementsAmpmTraceEnabled (660), AmpmMeasurementsAveragingMode (621), AmpmMeasurementsDutInputPowerLevel (623), AmpmMeasurementsEnabled (620), AmpmMeasurementsMeanAcquiredWaveformTraceEnabled (783), AmpmMeasurementsMeasurementInterval (624), AmpmMeasurementsMeasurementLength (624), AmpmMeasurementsNumberOfAverages (622), AmpmMeasurementsProcessedReferenceWaveformTraceEnabled (784), AutoDetectionStandardMode (789), AutorangeMaxAcquisitionLength (270), AutorangeMaxIdleTime (274), AutoSpanEnabled (184), CarrierFrequency (0), CcdfEnabled (579), CcdfMeasurementLength (412), CcdfNumberOfRecords (596), CcdfRemoveDeadTime (595), CcdfTraceEnabled (580), ChannelBandwidth (276), CompatibilityVersion (309), DetectedChannelBandwidth (336), DetectedStandard (335), DeviceInstantaneousBandwidth (170), DsssDataRate (74), DsssDemodAllTracesEnabled (188), DsssDemodAutoComputeAcquisitionLengthEnabled (518), DsssDemodAutoComputeMeasurementLengthEnabled (518), DsssDemodBurstStartDetectionEnabled (517), DsssDemodCarrierFrequencyOffsetEstimationEnabled (543), DsssDemodCarrierSuppressionEstimationEnabled (547), DsssDemodConstellationTraceEnabled (267), DsssDemodDecodedBitsTraceEnabled (185), DsssDemodEnabled (67), DsssDemodEqualizationEnabled (69), DsssDemodEvmPerChipTraceEnabled (311), DsssDemodEvmPerSymbolTraceEnabled (311), DsssDemodGatedPowerDataPowerEnabled (555), DsssDemodGatedPowerEnabled (113), DsssDemodGatedPowerPreambleAndHeaderPowerEnabled (553), DsssDemodGatedPowerStartTime (75), DsssDemodGatedPowerStopTime (76), DsssDemodGatedPowerTotalPacketPowerEnabled (552), DsssDemodHeaderDetectionEnabled (72), DsssDemodIqGainImbalanceEstimationEnabled (545), DsssDemodLowpassFilteringEnabled (313), DsssDemodMacFrameCheckSequenceCheckEnabled (175), DsssDemodMaximumChipsUsed (143), DsssDemodMeasurementLength (418), DsssDemodMeasurementStartLocation (77), DsssDemodNumberOfAverages (68), DsssDemodPhaseTracking (145), DsssDemodQuadratureSkewEstimationEnabled (546), DsssDemodReferencePulseShapingFilterCoefficient (71), DsssDemodReferencePulseShapingFilterType (70), DsssDemodSampleClockOffsetEstimationEnabled (544), DsssDemodUserDefinedGatePowerEnabled (113), DsssDemodUserDefinedGateStartTime (75), DsssDemodUserDefinedGateStopTime (76), DsssPayloadLength (73), DsssPowerRampDownHighThreshold (138), DsssPowerRampDownLowThreshold (137), DsssPowerRampMeasurementEnabled (31), DsssPowerRampMeasurementLength (416), DsssPowerRampMeasurementNumberOfAverages (32), DsssPowerRampUpHighThreshold (136), DsssPowerRampUpLowThreshold (135), ETSIIBEDeltaACLR (837), ETSIIBEDeviceEmissionClass (836), ETSIIBEDUTAverageOutputPower (833), ETSIIBEEnabled (829), ETSIIBENumberOfAverages (830), ETSIIBENumberOfOffset (832), ETSIIBETraceEnabled (831), ETSIIBETransmitChannelPSDLimit (835), FecCodingType (162), FftSize (118), FftWindowSize (117), FftWindowType (9), GatedSpectrumAveragingType (384), GatedSpectrumEnabled (304), GatedSpectrumMeasurementLength (212), GatedSpectrumMode (295), GuardInterval (299), GuardIntervalType (814), HeLtfSize (874), HeSigBDualCarrierModulationEnabled (919), HeSigBMcsIndex (918), IqPowerEdgeReferenceTriggerEnabled (3), LdpcExtraSymbolUsed (898), LOFrequencyOffset (1035), LOFrequencyOffsetMode (1034), LoSharingEnabled (421), MaxInputPower (316), MaxSpectralDensityEnabled (19), MaxSpectralDensityNumberOfAverages (20), McsIndex (298), MidamblePeriodicity (1059), MultiSegmentMeasurementMode (858), MuMimoLtfModeEnabled (1044), NoiseCompensationCarrierFrequencies (916), NoiseCompensationEnabled (907), NoiseCompensationMaximumChannelBandwidths (917), NoiseCompensationMaximumReferenceLevel (911), NoiseCompensationMinimumReferenceLevel (910), NumberOfExtensionSpatialStreams (300), NumberOfHeLtfSymbols (896), NumberOfHeSigBSymbols (920), NumberOfIterations (154), NumberOfReceiveChannels (275), NumberOfSegments (209), NumberOfSpaceTimeStreams (210), ObwEnabled (16), ObwNumberOfAverages (18), OFDMChannelEstimationOnLLTFEnabled (1061), OfdmDataRate (49), OfdmDemod80211ahPreambleDetectionEnabled (817), OfdmDemod80211nPlcpFrameDetectionEnabled (279), OfdmDemod80Plus80FilterBeforeSyncEnabled (538), OfdmDemod80Plus80OversamplingFactor (539), OfdmDemod80Plus80SegmentIndex (1030), OfdmDemodAggregation (234), OfdmDemodAllTracesEnabled (187), OfdmDemodAmplitudeTrackingEnabled (52), OfdmDemodAutoComputeMeasurementLengthEnabled (515), OfdmDemodBurstStartDetectionEnabled (389), OfdmDemodCarrierFrequencyLeakageEstimationEnabled (397), OfdmDemodCarrierFrequencyOffsetEstimationEnabled (392), OfdmDemodCfoEstimationMethod (323), OfdmDemodChannelEstimationMethod (55), OfdmDemodChannelEvmEnabled (602), OfdmDemodChannelFrequencyResponseTraceEnabled (281), OfdmDemodChannelFrequencyResponseTraceMode (414), OfdmDemodChannelMatrixPowerEnabled (603), OfdmDemodChannelTrackingEnabled (55), OfdmDemodCombinedSignalDemodulationEnabled (408), OfdmDemodCommonClockSourceEnabled (540), OfdmDemodCommonPhaseErrorEstimationEnabled (778), OfdmDemodCommonPilotErrorEstimationEnabled (398), OfdmDemodCommonPilotErrorTraceEnabled (388), OfdmDemodConstellationTraceEnabled (266), OfdmDemodDataEvmPerSymbolTraceEnabled (331), OfdmDemodDecodedBitsTraceEnabled (164), OfdmDemodDecodedHeaderBitsTraceEnabled (1031), OfdmDemodEnabled (43), OfdmDemodEvmPerSubcarrierPerSymbolTraceEnabled (522), OfdmDemodEvmPerSubcarrierTraceEnabled (310), OfdmDemodEvmPerSymbolPerSubcarrierTraceEnabled (314), OfdmDemodEvmPerSymbolTraceEnabled (308), OfdmDemodGatedPowerDataPowerEnabled (551), OfdmDemodGatedPowerEnabled (112), OfdmDemodGatedPowerPreambleAndHeaderPowerEnabled (550), OfdmDemodGatedPowerStartTime (46), OfdmDemodGatedPowerStopTime (47), OfdmDemodGatedPowerTotalPacketPowerEnabled (549), OfdmDemodGroupDelayTraceEnabled (413), OfdmDemodGroupDelayTraceMode (415), OfdmDemodHeaderDetectionEnabled (45), OfdmDemodIqGainImbalanceCompensationEnabled (403), OfdmDemodIqGainImbalanceEstimationEnabled (394), OfdmDemodIQGainImbalancePerSubcarrierTraceEnabled (1053), OfdmDemodIQImpairmentsPerSubcarrierEnabled (1052), OfdmDemodIqMismatchSignalModel (233), OfdmDemodLowpassFilteringEnabled (312), OfdmDemodMacFrameCheckSequenceCheckEnabled (324), OfdmDemodMaximumSymbolsUsed (142), OfdmDemodMeasurementLength (417), OfdmDemodMeasurementStartLocation (50), OfdmDemodNumberOfAverages (44), OfdmDemodNumberOfOfdmSymbols (230), OfdmDemodNumberOfSpaceTimeStreams (217), OfdmDemodPhaseNoisePsdTraceEnabled (391), OfdmDemodPhaseTracking (53), OfdmDemodPilotEvmPerSymbolTraceEnabled (330), OfdmDemodPreambleFrequencyErrorTraceEnabled (213), OfdmDemodQuadratureSkewCompensationEnabled (404), OfdmDemodQuadratureSkewEstimationEnabled (395), OfdmDemodQuadratureSkewPerSubcarrierTraceEnabled (1054), OfdmDemodReferenceConstellationTraceEnabled (411), OfdmDemodReferenceDataConstellationEnabled (605), OfdmDemodReferenceDataConstellationIdentifier (853), OfdmDemodRmsPhaseError (224), OfdmDemodSampleClockOffsetEstimationEnabled (393), OfdmDemodServiceBitsTraceEnabled (771), OfdmDemodSpectralFlatnessMarginEnabled (604), OfdmDemodSpectralFlatnessMarginSubcarrierIndex (381), OfdmDemodSpectralFlatnessTraceEnabled (301), OfdmDemodStreamPowerEnabled (668), OfdmDemodSymbolTimingAdjustment (321), OfdmDemodTimeTrackingEnabled (54), OfdmDemodTimingSkewCompensationEnabled (400), OfdmDemodTimingSkewEstimationEnabled (396), OfdmDemodTraceSettingCarrierFrequencyOffsetCcdfTraceEnabled (1038), OfdmDemodUnusedToneErrorEnabled (922), OfdmDemodUnusedToneErrorMaskReference (923), OfdmDemodUnusedToneErrorTraceEnabled (859), OfdmDemodUserDefinedGatePowerEnabled (112), OfdmDemodUserDefinedGateStartTime (46), OfdmDemodUserDefinedGateStopTime (47), OfdmDemodUserDefinedIQGainImbalance (1046), OfdmDemodUserDefinedIQImpairmentsCompensationEnabled (1045), OfdmDemodUserDefinedQuadratureSkew (1047), OfdmDemodUserDefinedTimingSkew (1048), OfdmDemodVhtSigBCrcCheckEnabled (572), OfdmDualCarrierModulationEnabled (873), OfdmGuardIntervalType (821), OfdmLSigPayloadLength (215), OfdmNonHTModulationDetectionEnabled (846), OfdmNonHTModulationMode (827), OfdmNumberOfUsers (644), OfdmPacketExtensionDisambiguity (876), OfdmPayloadLength (48), OfdmPpduType (643), OptimizeReferenceLevelForEvmEnabled (915), OptimizeReferenceLevelForEvmMargin (914), PreFecPaddingFactor (875), Property80211acAmpduEnabled (399), Rbw (6), RbwDefinition (296), RecommendedAcquisitionLength (173), RecommendedAcquisitionType (172), RecommendedIqPostTriggerDelay (178), RecommendedIqPreTriggerDelay (177), RecommendedIqSamplingRate (176), RecommendedMinimumQuietTime (174), RecommendedNumberOfRecords (154), RecommendedSpectrumFftWindowType (183), RecommendedSpectrumRbw (181), RecommendedSpectrumRbwDefinition (180), RecommendedSpectrumSpan (179), RecommendedSpectrumVbw (182), ReferenceLevelStepSize (912), ResultAcpReferenceChannelPower (802), ResultAmpmMeasurements1DbCompressionPoint (629), ResultAmpmMeasurementsAmamPolynomialCoefficients (628), ResultAmpmMeasurementsAmamResidual (633), ResultAmpmMeasurementsAmpmPolynomialCoefficients (627), ResultAmpmMeasurementsAmpmResidual (632), ResultAmpmMeasurementsAverageGain (636), ResultAmpmMeasurementsAveragePhaseError (635), ResultAmpmMeasurementsGainErrorRange (631), ResultAmpmMeasurementsMaximumInputPower (651), ResultAmpmMeasurementsMinimumInputPower (650), ResultAmpmMeasurementsPhaseErrorRange (630), ResultAutorangeAcquisitionLength (318), ResultAutorangeMaxInputPower (317), ResultAutorangeMaxInputRange (317), ResultCcdf10PercentPower (584), ResultCcdf1By10000PercentPower (589), ResultCcdf1By1000PercentPower (588), ResultCcdf1By100PercentPower (587), ResultCcdf1By10PercentPower (586), ResultCcdf1PercentPower (585), ResultCcdfAveragePower (582), ResultCcdfAveragePowerPercentile (583), ResultCcdfPeakToAveragePowerRatio (590), ResultCcdfResultantCount (591), ResultDsssDemod80211bPeakEvm (140), ResultDsssDemod80211bPeakEvm2007 (205), ResultDsssDemod80211bPeakEvm2007Maximum (205), ResultDsssDemod80211bPeakEvm2007Minimum (373), ResultDsssDemod80211bPeakEvmMaximum (140), ResultDsssDemod80211bPeakEvmMinimum (372), ResultDsssDemodAverageGatedPower (258), ResultDsssDemodAverageGatedPowerAverage (258), ResultDsssDemodAverageGatedPowerMaximum (375), ResultDsssDemodAverageGatedPowerMinimum (374), ResultDsssDemodAverageGatedPowerStandardDeviation (376), ResultDsssDemodBurstStartTime (516), ResultDsssDemodCarrierFrequencyOffset (81), ResultDsssDemodCarrierFrequencyOffsetAverage (81), ResultDsssDemodCarrierFrequencyOffsetMaximum (354), ResultDsssDemodCarrierFrequencyOffsetMinimum (353), ResultDsssDemodCarrierFrequencyOffsetStandardDeviation (355), ResultDsssDemodCarrierSuppression (84), ResultDsssDemodCarrierSuppressionAverage (84), ResultDsssDemodCarrierSuppressionMaximum (363), ResultDsssDemodCarrierSuppressionMinimum (362), ResultDsssDemodCarrierSuppressionStandardDeviation (364), ResultDsssDemodDataRate (87), ResultDsssDemodGatedPowerMeanPowerAverage (564), ResultDsssDemodGatedPowerMeanPowerMaximum (566), ResultDsssDemodGatedPowerMeanPowerMinimum (565), ResultDsssDemodGatedPowerMeanPowerStandardDeviation (567), ResultDsssDemodGatedPowerPeakPowerAverage (568), ResultDsssDemodGatedPowerPeakPowerMaximum (570), ResultDsssDemodGatedPowerPeakPowerMinimum (569), ResultDsssDemodGatedPowerPeakPowerStandardDeviation (571), ResultDsssDemodHeaderChecksumPassed (90), ResultDsssDemodIqGainImbalance (82), ResultDsssDemodIqGainImbalanceAverage (82), ResultDsssDemodIqGainImbalanceMaximum (357), ResultDsssDemodIqGainImbalanceMinimum (356), ResultDsssDemodIqGainImbalanceStandardDeviation (358), ResultDsssDemodMacFrameCheckSequencePassed (189), ResultDsssDemodPayloadLength (85), ResultDsssDemodPeakEvm (80), ResultDsssDemodPeakEvmMaximum (80), ResultDsssDemodPeakEvmMinimum (371), ResultDsssDemodPhaseErrorRmsAverage (611), ResultDsssDemodPhaseErrorRmsMaximum (613), ResultDsssDemodPhaseErrorRmsMinimum (612), ResultDsssDemodPhaseErrorRmsStandardDeviation (614), ResultDsssDemodPreambleType (88), ResultDsssDemodQuadratureSkew (83), ResultDsssDemodQuadratureSkewAverage (83), ResultDsssDemodQuadratureSkewMaximum (360), ResultDsssDemodQuadratureSkewMinimum (359), ResultDsssDemodQuadratureSkewStandardDeviation (361), ResultDsssDemodRmsEvm (79), ResultDsssDemodRmsEvmAverage (79), ResultDsssDemodRmsEvmMaximum (369), ResultDsssDemodRmsEvmMinimum (368), ResultDsssDemodRmsEvmStandardDeviation (370), ResultDsssDemodSampleClockOffset (158), ResultDsssDemodSampleClockOffsetAverage (158), ResultDsssDemodSampleClockOffsetMaximum (366), ResultDsssDemodSampleClockOffsetMinimum (365), ResultDsssDemodSampleClockOffsetStandardDeviation (367), ResultDsssDemodSfdFound (89), ResultDsssPowerRampDownTime (42), ResultDsssPowerRampUpTime (41), ResultETSIIBEDeltaACLRFrequencyVector (843), ResultETSIIBEDeltaACLRMarginVector (842), ResultETSIIBEMargin (838), ResultETSIIBEMarginFrequencyVector (840), ResultETSIIBEMarginVector (839), ResultETSIIBEViolation (841), ResultMaxSpectralDensity (21), ResultObw (25), ResultObwHighFrequency (159), ResultObwLowFrequency (256), ResultOfdmDemod80211ahPreambleType (818), ResultOfdmDemod80211nPlcpFrameFormat (303), ResultOfdmDemodAggregation (234), ResultOfdmDemodAverageGatedPower (257), ResultOfdmDemodAverageGatedPowerAverage (257), ResultOfdmDemodAverageGatedPowerMaximum (351), ResultOfdmDemodAverageGatedPowerMinimum (350), ResultOfdmDemodAverageGatedPowerStandardDeviation (352), ResultOfdmDemodBurstStartTime (513), ResultOfdmDemodCarrierFrequencyLeakage (58), ResultOfdmDemodCarrierFrequencyLeakageAverage (58), ResultOfdmDemodCarrierFrequencyLeakageMaximum (240), ResultOfdmDemodCarrierFrequencyLeakageMinimum (239), ResultOfdmDemodCarrierFrequencyLeakageStandardDeviation (241), ResultOfdmDemodCarrierFrequencyOffset (57), ResultOfdmDemodCarrierFrequencyOffsetAverage (57), ResultOfdmDemodCarrierFrequencyOffsetCcdfTenPercent (1039), ResultOfdmDemodCarrierFrequencyOffsetMaximum (237), ResultOfdmDemodCarrierFrequencyOffsetMinimum (236), ResultOfdmDemodCarrierFrequencyOffsetStandardDeviation (238), ResultOfdmDemodChannelMatrixAbsolutePowerAverage (530), ResultOfdmDemodChannelMatrixAbsolutePowerMaximum (532), ResultOfdmDemodChannelMatrixAbsolutePowerMinimum (531), ResultOfdmDemodChannelMatrixAbsolutePowerStdDev (533), ResultOfdmDemodChannelMatrixCrossPowerMaximum (345), ResultOfdmDemodChannelMatrixCrossPowerMinimum (344), ResultOfdmDemodChannelMatrixCrossPowerStdDev (346), ResultOfdmDemodCommmonPhaseErrorAverage (774), ResultOfdmDemodCommmonPhaseErrorMaximum (776), ResultOfdmDemodCommmonPhaseErrorMinimum (775), ResultOfdmDemodCommmonPhaseErrorStandardDeviation (777), ResultOfdmDemodCommonPhaseErrorAverage (774), ResultOfdmDemodCommonPhaseErrorMaximum (776), ResultOfdmDemodCommonPhaseErrorMinimum (775), ResultOfdmDemodCommonPhaseErrorStandardDeviation (777), ResultOfdmDemodCommonPilotErrorRms (382), ResultOfdmDemodCommonPilotErrorRmsAverage (382), ResultOfdmDemodCommonPilotErrorRmsMaximum (406), ResultOfdmDemodCommonPilotErrorRmsMinimum (405), ResultOfdmDemodCommonPilotErrorRmsStandardDeviation (407), ResultOfdmDemodCrossPower (288), ResultOfdmDemodCrossPowerAverage (288), ResultOfdmDemodDataRate (66), ResultOfdmDemodDataRmsEvm (329), ResultOfdmDemodDataRmsEvmAverage (329), ResultOfdmDemodDataRmsEvmMaximum (342), ResultOfdmDemodDataRmsEvmMinimum (341), ResultOfdmDemodDataRmsEvmStandardDeviation (343), ResultOfdmDemodDcmEnabled (883), ResultOfdmDemodDetectedPsduLength (897), ResultOfdmDemodDetectedS1gSigLength (820), ResultOfdmDemodDsssofdmHeaderCrcPassed (334), ResultOfdmDemodEffectiveDataRate (168), ResultOfdmDemodFecCodingType (163), ResultOfdmDemodGatedPowerMeanPowerAverage (556), ResultOfdmDemodGatedPowerMeanPowerMaximum (558), ResultOfdmDemodGatedPowerMeanPowerMinimum (557), ResultOfdmDemodGatedPowerMeanPowerStandardDeviation (559), ResultOfdmDemodGatedPowerPeakPowerAverage (560), ResultOfdmDemodGatedPowerPeakPowerMaximum (562), ResultOfdmDemodGatedPowerPeakPowerMinimum (561), ResultOfdmDemodGatedPowerPeakPowerStandardDeviation (563), ResultOfdmDemodGuardInterval (293), ResultOfdmDemodHeaderParityPassed (325), ResultOfdmDemodHeLtfSize (1028), ResultOfdmDemodHeSigACrcPassed (872), ResultOfdmDemodHeSigBCrcPassed (892), ResultOfdmDemodHeSigBDualCarrierModulationEnabled (889), ResultOfdmDemodHeSigBMcsIndex (888), ResultOfdmDemodHtSigCrcPassed (326), ResultOfdmDemodIqGainImbalance (61), ResultOfdmDemodIqGainImbalanceAverage (61), ResultOfdmDemodIqGainImbalanceMaximum (246), ResultOfdmDemodIqGainImbalanceMinimum (245), ResultOfdmDemodIqGainImbalanceStandardDeviation (247), ResultOfdmDemodLSigPayloadLength (216), ResultOfdmDemodMacFrameCheckSequencePassed (327), ResultOfdmDemodMcsIndex (291), ResultOfdmDemodMidamblePeriodicity (1060), ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageAverage (1024), ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageMaximum (1026), ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageMinimum (1025), ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageStandardDeviation (1027), ResultOfdmDemodNoiseCompensationApplied (913), ResultOfdmDemodNotSoundingBit (169), ResultOfdmDemodNumberOfExtensionSpatialStreams (294), ResultOfdmDemodNumberofHeSigBSymbols (927), ResultOfdmDemodNumberOfOfdmSymbols (230), ResultOfdmDemodNumberOfSpaceTimeStreams (217), ResultOfdmDemodNumberOfSymbolsUsed (194), ResultOfdmDemodNumberOfUsers (647), ResultOfdmDemodPacketExtentionDisambiguity (881), ResultOfdmDemodPacketExtentionDuration (885), ResultOfdmDemodPayloadLength (64), ResultOfdmDemodPilotRmsEvm (328), ResultOfdmDemodPilotRmsEvmAverage (328), ResultOfdmDemodPilotRmsEvmMaximum (339), ResultOfdmDemodPilotRmsEvmMinimum (338), ResultOfdmDemodPilotRmsEvmStandardDeviation (340), ResultOfdmDemodPpduType (646), ResultOfdmDemodPreFecPaddingFactor (880), ResultOfdmDemodQuadratureSkew (62), ResultOfdmDemodQuadratureSkewAverage (62), ResultOfdmDemodQuadratureSkewMaximum (252), ResultOfdmDemodQuadratureSkewMinimum (251), ResultOfdmDemodQuadratureSkewStandardDeviation (253), ResultOfdmDemodRmsEvm (56), ResultOfdmDemodRmsEvmAverage (56), ResultOfdmDemodRmsEvmMaximum (255), ResultOfdmDemodRmsEvmMinimum (254), ResultOfdmDemodRmsEvmStandardDeviation (337), ResultOfdmDemodRmsPhaseError (224), ResultOfdmDemodRuOffset (894), ResultOfdmDemodRuSize (891), ResultOfdmDemodS1gSigCrcPassed (816), ResultOfdmDemodS1gSigLength (820), ResultOfdmDemodSampleClockOffset (60), ResultOfdmDemodSampleClockOffsetAverage (60), ResultOfdmDemodSampleClockOffsetMaximum (243), ResultOfdmDemodSampleClockOffsetMinimum (242), ResultOfdmDemodSampleClockOffsetStandardDeviation (244), ResultOfdmDemodScramblerSeed (649), ResultOfdmDemodShortGuardIntervalB1Bit (229), ResultOfdmDemodSpaceTimeStreamOffset (909), ResultOfdmDemodSpectralFlatnessMargin (59), ResultOfdmDemodSpectralFlatnessMarginAverage (59), ResultOfdmDemodSpectralFlatnessMarginMaximum (348), ResultOfdmDemodSpectralFlatnessMarginMinimum (347), ResultOfdmDemodSpectralFlatnessMarginStandardDeviation (349), ResultOfdmDemodSpectralFlatnessMarginSubcarrierIndex (381), ResultOfdmDemodStaId (890), ResultOfdmDemodStbcAllStreamsEnabled (218), ResultOfdmDemodStbcIndex (160), ResultOfdmDemodStreamPowerAverage (669), ResultOfdmDemodStreamPowerMaximum (671), ResultOfdmDemodStreamPowerMinimum (670), ResultOfdmDemodStreamPowerStandardDeviation (768), ResultOfdmDemodTimingSkew (221), ResultOfdmDemodTimingSkewAverage (221), ResultOfdmDemodTimingSkewMaximum (249), ResultOfdmDemodTimingSkewMinimum (248), ResultOfdmDemodTimingSkewStandardDeviation (250), ResultOfdmDemodTransmissionMode (882), ResultOfdmDemodUnusedToneErrorMargin (924), ResultOfdmDemodUnusedToneErrorMarginRuIndex (925), ResultOfdmDemodUnusedToneErrorMarginVector (926), ResultOfdmDemodVhtSigACrcPassed (219), ResultOfdmDemodVhtSigBCrcPassed (220), ResultOfdmLDPCExtraOfdmSymbol (825), ResultOfdmNonHTModulationMode (847), ResultOfdmTVHTMode (848), ResultOfdmTVHTSIGACRCPassed (823), ResultSpectralMaskFrequencyOffsetsUsed (192), ResultSpectralMaskMargin (22), ResultSpectralMaskMarginFrequencyVector (519), ResultSpectralMaskMarginPowerSpectralDensityVector (520), ResultSpectralMaskMarginVector (307), ResultSpectralMaskPowerOffsetsUsed (193), ResultSpectralMaskReferenceLevel (262), ResultSpectralMaskViolation (521), ResultSpectralMeasurementsChannelPower (782), ResultTxpAveragePowerAverage (36), ResultTxpAveragePowerMaximum (378), ResultTxpAveragePowerMinimum (377), ResultTxpAveragePowerStandardDeviation (379), ResultTxpAveragePowerWithIdleTimeAverage (204), ResultTxpAveragePowerWithIdleTimeMaximum (535), ResultTxpAveragePowerWithIdleTimeMinimum (534), ResultTxpAveragePowerWithIdleTimeStandardDeviation (536), ResultTxpowerMeasurementsAveragePower (36), ResultTxpowerMeasurementsPeakPower (35), ResultTxpPeakPowerAverage (541), ResultTxpPeakPowerMaximum (35), ResultTxpPeakPowerMinimum (380), ResultTxpPeakPowerStandardDeviation (542), RuOffset (852), RuSize (851), SampleClockRateFactor (383), ScramblerSeed (854), ShortGuardIntervalB1Bit (228), SpaceTimeStreamOffset (1043), Span (5), SpectralMaskCenterFrequency (527), SpectralMaskCombinedMaskEnabled (537), SpectralMaskEnabled (10), SpectralMaskFrequencyOffsets (305), SpectralMaskNumberOfAverages (11), SpectralMaskPowerOffsets (306), SpectralMaskReferenceLevel (156), SpectralMaskReferenceLevelType (155), SpectralMaskTraceEnabled (264), SpectralMaskTransmitPowerClass (419), SpectralMaskType (297), SpectralMeasurementsAllEnabled (8), SpectralMeasurementsChannelPowerAutoMeasureBWEnabled (780), SpectralMeasurementsChannelPowerEnabled (610), SpectralMeasurementsChannelPowerMeasurementBandwidth (781), SpectralMeasurementsChannelPowerNumberOfAverages (779), Standard (7), StbcAllStreamsEnabled (211), StbcIndex (141), SwapIAndQEnabled (214), TclkSynchronisationEnabled (420), TransmissionMode (850), TriggerDelay (171), TxPowerBurstDetectionEnabled (792), TxPowerMeasurementLength (387), TxpowerMeasurementsEnabled (33), TxpowerMeasurementsMode (529), TxpowerMeasurementsNumberOfAverages (34), TxpowerMeasurementsPvtTraceEnabled (265) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AcpEnabled = None
    AcpLowerAbsolutePower = None
    AcpLowerRelativePower = None
    AcpNumberOfAverages = None
    AcpNumberOfOffsets = None
    AcpTraceEnabled = None
    AcpUpperAbsolutePower = None
    AcpUpperRelativePower = None
    AcquisitionLength = None
    AggregationBit = None
    AmplitudeCorrectionEnabled = None
    AmpmMeasurementsAllTracesEnabled = None
    AmpmMeasurementsAmamCurveFitTraceEnabled = None
    AmpmMeasurementsAmamTraceEnabled = None
    AmpmMeasurementsAmpmCurveFitTraceEnabled = None
    AmpmMeasurementsAmpmTraceEnabled = None
    AmpmMeasurementsAveragingMode = None
    AmpmMeasurementsDutInputPowerLevel = None
    AmpmMeasurementsEnabled = None
    AmpmMeasurementsMeanAcquiredWaveformTraceEnabled = None
    AmpmMeasurementsMeasurementInterval = None
    AmpmMeasurementsMeasurementLength = None
    AmpmMeasurementsNumberOfAverages = None
    AmpmMeasurementsProcessedReferenceWaveformTraceEnabled = None
    AutoDetectionStandardMode = None
    AutorangeMaxAcquisitionLength = None
    AutorangeMaxIdleTime = None
    AutoSpanEnabled = None
    CarrierFrequency = None
    CcdfEnabled = None
    CcdfMeasurementLength = None
    CcdfNumberOfRecords = None
    CcdfRemoveDeadTime = None
    CcdfTraceEnabled = None
    ChannelBandwidth = None
    CompatibilityVersion = None
    DetectedChannelBandwidth = None
    DetectedStandard = None
    DeviceInstantaneousBandwidth = None
    DsssDataRate = None
    DsssDemodAllTracesEnabled = None
    DsssDemodAutoComputeAcquisitionLengthEnabled = None
    DsssDemodAutoComputeMeasurementLengthEnabled = None
    DsssDemodBurstStartDetectionEnabled = None
    DsssDemodCarrierFrequencyOffsetEstimationEnabled = None
    DsssDemodCarrierSuppressionEstimationEnabled = None
    DsssDemodConstellationTraceEnabled = None
    DsssDemodDecodedBitsTraceEnabled = None
    DsssDemodEnabled = None
    DsssDemodEqualizationEnabled = None
    DsssDemodEvmPerChipTraceEnabled = None
    DsssDemodEvmPerSymbolTraceEnabled = None
    DsssDemodGatedPowerDataPowerEnabled = None
    DsssDemodGatedPowerEnabled = None
    DsssDemodGatedPowerPreambleAndHeaderPowerEnabled = None
    DsssDemodGatedPowerStartTime = None
    DsssDemodGatedPowerStopTime = None
    DsssDemodGatedPowerTotalPacketPowerEnabled = None
    DsssDemodHeaderDetectionEnabled = None
    DsssDemodIqGainImbalanceEstimationEnabled = None
    DsssDemodLowpassFilteringEnabled = None
    DsssDemodMacFrameCheckSequenceCheckEnabled = None
    DsssDemodMaximumChipsUsed = None
    DsssDemodMeasurementLength = None
    DsssDemodMeasurementStartLocation = None
    DsssDemodNumberOfAverages = None
    DsssDemodPhaseTracking = None
    DsssDemodQuadratureSkewEstimationEnabled = None
    DsssDemodReferencePulseShapingFilterCoefficient = None
    DsssDemodReferencePulseShapingFilterType = None
    DsssDemodSampleClockOffsetEstimationEnabled = None
    DsssDemodUserDefinedGatePowerEnabled = None
    DsssDemodUserDefinedGateStartTime = None
    DsssDemodUserDefinedGateStopTime = None
    DsssPayloadLength = None
    DsssPowerRampDownHighThreshold = None
    DsssPowerRampDownLowThreshold = None
    DsssPowerRampMeasurementEnabled = None
    DsssPowerRampMeasurementLength = None
    DsssPowerRampMeasurementNumberOfAverages = None
    DsssPowerRampUpHighThreshold = None
    DsssPowerRampUpLowThreshold = None
    ETSIIBEDeltaACLR = None
    ETSIIBEDeviceEmissionClass = None
    ETSIIBEDUTAverageOutputPower = None
    ETSIIBEEnabled = None
    ETSIIBENumberOfAverages = None
    ETSIIBENumberOfOffset = None
    ETSIIBETraceEnabled = None
    ETSIIBETransmitChannelPSDLimit = None
    FecCodingType = None
    FftSize = None
    FftWindowSize = None
    FftWindowType = None
    GatedSpectrumAveragingType = None
    GatedSpectrumEnabled = None
    GatedSpectrumMeasurementLength = None
    GatedSpectrumMode = None
    GuardInterval = None
    GuardIntervalType = None
    HeLtfSize = None
    HeSigBDualCarrierModulationEnabled = None
    HeSigBMcsIndex = None
    IqPowerEdgeReferenceTriggerEnabled = None
    LdpcExtraSymbolUsed = None
    LOFrequencyOffset = None
    LOFrequencyOffsetMode = None
    LoSharingEnabled = None
    MaxInputPower = None
    MaxSpectralDensityEnabled = None
    MaxSpectralDensityNumberOfAverages = None
    McsIndex = None
    MidamblePeriodicity = None
    MultiSegmentMeasurementMode = None
    MuMimoLtfModeEnabled = None
    NoiseCompensationCarrierFrequencies = None
    NoiseCompensationEnabled = None
    NoiseCompensationMaximumChannelBandwidths = None
    NoiseCompensationMaximumReferenceLevel = None
    NoiseCompensationMinimumReferenceLevel = None
    NumberOfExtensionSpatialStreams = None
    NumberOfHeLtfSymbols = None
    NumberOfHeSigBSymbols = None
    NumberOfIterations = None
    NumberOfReceiveChannels = None
    NumberOfSegments = None
    NumberOfSpaceTimeStreams = None
    ObwEnabled = None
    ObwNumberOfAverages = None
    OFDMChannelEstimationOnLLTFEnabled = None
    OfdmDataRate = None
    OfdmDemod80211ahPreambleDetectionEnabled = None
    OfdmDemod80211nPlcpFrameDetectionEnabled = None
    OfdmDemod80Plus80FilterBeforeSyncEnabled = None
    OfdmDemod80Plus80OversamplingFactor = None
    OfdmDemod80Plus80SegmentIndex = None
    OfdmDemodAggregation = None
    OfdmDemodAllTracesEnabled = None
    OfdmDemodAmplitudeTrackingEnabled = None
    OfdmDemodAutoComputeMeasurementLengthEnabled = None
    OfdmDemodBurstStartDetectionEnabled = None
    OfdmDemodCarrierFrequencyLeakageEstimationEnabled = None
    OfdmDemodCarrierFrequencyOffsetEstimationEnabled = None
    OfdmDemodCfoEstimationMethod = None
    OfdmDemodChannelEstimationMethod = None
    OfdmDemodChannelEvmEnabled = None
    OfdmDemodChannelFrequencyResponseTraceEnabled = None
    OfdmDemodChannelFrequencyResponseTraceMode = None
    OfdmDemodChannelMatrixPowerEnabled = None
    OfdmDemodChannelTrackingEnabled = None
    OfdmDemodCombinedSignalDemodulationEnabled = None
    OfdmDemodCommonClockSourceEnabled = None
    OfdmDemodCommonPhaseErrorEstimationEnabled = None
    OfdmDemodCommonPilotErrorEstimationEnabled = None
    OfdmDemodCommonPilotErrorTraceEnabled = None
    OfdmDemodConstellationTraceEnabled = None
    OfdmDemodDataEvmPerSymbolTraceEnabled = None
    OfdmDemodDecodedBitsTraceEnabled = None
    OfdmDemodDecodedHeaderBitsTraceEnabled = None
    OfdmDemodEnabled = None
    OfdmDemodEvmPerSubcarrierPerSymbolTraceEnabled = None
    OfdmDemodEvmPerSubcarrierTraceEnabled = None
    OfdmDemodEvmPerSymbolPerSubcarrierTraceEnabled = None
    OfdmDemodEvmPerSymbolTraceEnabled = None
    OfdmDemodGatedPowerDataPowerEnabled = None
    OfdmDemodGatedPowerEnabled = None
    OfdmDemodGatedPowerPreambleAndHeaderPowerEnabled = None
    OfdmDemodGatedPowerStartTime = None
    OfdmDemodGatedPowerStopTime = None
    OfdmDemodGatedPowerTotalPacketPowerEnabled = None
    OfdmDemodGroupDelayTraceEnabled = None
    OfdmDemodGroupDelayTraceMode = None
    OfdmDemodHeaderDetectionEnabled = None
    OfdmDemodIqGainImbalanceCompensationEnabled = None
    OfdmDemodIqGainImbalanceEstimationEnabled = None
    OfdmDemodIQGainImbalancePerSubcarrierTraceEnabled = None
    OfdmDemodIQImpairmentsPerSubcarrierEnabled = None
    OfdmDemodIqMismatchSignalModel = None
    OfdmDemodLowpassFilteringEnabled = None
    OfdmDemodMacFrameCheckSequenceCheckEnabled = None
    OfdmDemodMaximumSymbolsUsed = None
    OfdmDemodMeasurementLength = None
    OfdmDemodMeasurementStartLocation = None
    OfdmDemodNumberOfAverages = None
    OfdmDemodNumberOfOfdmSymbols = None
    OfdmDemodNumberOfSpaceTimeStreams = None
    OfdmDemodPhaseNoisePsdTraceEnabled = None
    OfdmDemodPhaseTracking = None
    OfdmDemodPilotEvmPerSymbolTraceEnabled = None
    OfdmDemodPreambleFrequencyErrorTraceEnabled = None
    OfdmDemodQuadratureSkewCompensationEnabled = None
    OfdmDemodQuadratureSkewEstimationEnabled = None
    OfdmDemodQuadratureSkewPerSubcarrierTraceEnabled = None
    OfdmDemodReferenceConstellationTraceEnabled = None
    OfdmDemodReferenceDataConstellationEnabled = None
    OfdmDemodReferenceDataConstellationIdentifier = None
    OfdmDemodRmsPhaseError = None
    OfdmDemodSampleClockOffsetEstimationEnabled = None
    OfdmDemodServiceBitsTraceEnabled = None
    OfdmDemodSpectralFlatnessMarginEnabled = None
    OfdmDemodSpectralFlatnessMarginSubcarrierIndex = None
    OfdmDemodSpectralFlatnessTraceEnabled = None
    OfdmDemodStreamPowerEnabled = None
    OfdmDemodSymbolTimingAdjustment = None
    OfdmDemodTimeTrackingEnabled = None
    OfdmDemodTimingSkewCompensationEnabled = None
    OfdmDemodTimingSkewEstimationEnabled = None
    OfdmDemodTraceSettingCarrierFrequencyOffsetCcdfTraceEnabled = None
    OfdmDemodUnusedToneErrorEnabled = None
    OfdmDemodUnusedToneErrorMaskReference = None
    OfdmDemodUnusedToneErrorTraceEnabled = None
    OfdmDemodUserDefinedGatePowerEnabled = None
    OfdmDemodUserDefinedGateStartTime = None
    OfdmDemodUserDefinedGateStopTime = None
    OfdmDemodUserDefinedIQGainImbalance = None
    OfdmDemodUserDefinedIQImpairmentsCompensationEnabled = None
    OfdmDemodUserDefinedQuadratureSkew = None
    OfdmDemodUserDefinedTimingSkew = None
    OfdmDemodVhtSigBCrcCheckEnabled = None
    OfdmDualCarrierModulationEnabled = None
    OfdmGuardIntervalType = None
    OfdmLSigPayloadLength = None
    OfdmNonHTModulationDetectionEnabled = None
    OfdmNonHTModulationMode = None
    OfdmNumberOfUsers = None
    OfdmPacketExtensionDisambiguity = None
    OfdmPayloadLength = None
    OfdmPpduType = None
    OptimizeReferenceLevelForEvmEnabled = None
    OptimizeReferenceLevelForEvmMargin = None
    PreFecPaddingFactor = None
    Property80211acAmpduEnabled = None
    Rbw = None
    RbwDefinition = None
    RecommendedAcquisitionLength = None
    RecommendedAcquisitionType = None
    RecommendedIqPostTriggerDelay = None
    RecommendedIqPreTriggerDelay = None
    RecommendedIqSamplingRate = None
    RecommendedMinimumQuietTime = None
    RecommendedNumberOfRecords = None
    RecommendedSpectrumFftWindowType = None
    RecommendedSpectrumRbw = None
    RecommendedSpectrumRbwDefinition = None
    RecommendedSpectrumSpan = None
    RecommendedSpectrumVbw = None
    ReferenceLevelStepSize = None
    ResultAcpReferenceChannelPower = None
    ResultAmpmMeasurements1DbCompressionPoint = None
    ResultAmpmMeasurementsAmamPolynomialCoefficients = None
    ResultAmpmMeasurementsAmamResidual = None
    ResultAmpmMeasurementsAmpmPolynomialCoefficients = None
    ResultAmpmMeasurementsAmpmResidual = None
    ResultAmpmMeasurementsAverageGain = None
    ResultAmpmMeasurementsAveragePhaseError = None
    ResultAmpmMeasurementsGainErrorRange = None
    ResultAmpmMeasurementsMaximumInputPower = None
    ResultAmpmMeasurementsMinimumInputPower = None
    ResultAmpmMeasurementsPhaseErrorRange = None
    ResultAutorangeAcquisitionLength = None
    ResultAutorangeMaxInputPower = None
    ResultAutorangeMaxInputRange = None
    ResultCcdf10PercentPower = None
    ResultCcdf1By10000PercentPower = None
    ResultCcdf1By1000PercentPower = None
    ResultCcdf1By100PercentPower = None
    ResultCcdf1By10PercentPower = None
    ResultCcdf1PercentPower = None
    ResultCcdfAveragePower = None
    ResultCcdfAveragePowerPercentile = None
    ResultCcdfPeakToAveragePowerRatio = None
    ResultCcdfResultantCount = None
    ResultDsssDemod80211bPeakEvm = None
    ResultDsssDemod80211bPeakEvm2007 = None
    ResultDsssDemod80211bPeakEvm2007Maximum = None
    ResultDsssDemod80211bPeakEvm2007Minimum = None
    ResultDsssDemod80211bPeakEvmMaximum = None
    ResultDsssDemod80211bPeakEvmMinimum = None
    ResultDsssDemodAverageGatedPower = None
    ResultDsssDemodAverageGatedPowerAverage = None
    ResultDsssDemodAverageGatedPowerMaximum = None
    ResultDsssDemodAverageGatedPowerMinimum = None
    ResultDsssDemodAverageGatedPowerStandardDeviation = None
    ResultDsssDemodBurstStartTime = None
    ResultDsssDemodCarrierFrequencyOffset = None
    ResultDsssDemodCarrierFrequencyOffsetAverage = None
    ResultDsssDemodCarrierFrequencyOffsetMaximum = None
    ResultDsssDemodCarrierFrequencyOffsetMinimum = None
    ResultDsssDemodCarrierFrequencyOffsetStandardDeviation = None
    ResultDsssDemodCarrierSuppression = None
    ResultDsssDemodCarrierSuppressionAverage = None
    ResultDsssDemodCarrierSuppressionMaximum = None
    ResultDsssDemodCarrierSuppressionMinimum = None
    ResultDsssDemodCarrierSuppressionStandardDeviation = None
    ResultDsssDemodDataRate = None
    ResultDsssDemodGatedPowerMeanPowerAverage = None
    ResultDsssDemodGatedPowerMeanPowerMaximum = None
    ResultDsssDemodGatedPowerMeanPowerMinimum = None
    ResultDsssDemodGatedPowerMeanPowerStandardDeviation = None
    ResultDsssDemodGatedPowerPeakPowerAverage = None
    ResultDsssDemodGatedPowerPeakPowerMaximum = None
    ResultDsssDemodGatedPowerPeakPowerMinimum = None
    ResultDsssDemodGatedPowerPeakPowerStandardDeviation = None
    ResultDsssDemodHeaderChecksumPassed = None
    ResultDsssDemodIqGainImbalance = None
    ResultDsssDemodIqGainImbalanceAverage = None
    ResultDsssDemodIqGainImbalanceMaximum = None
    ResultDsssDemodIqGainImbalanceMinimum = None
    ResultDsssDemodIqGainImbalanceStandardDeviation = None
    ResultDsssDemodMacFrameCheckSequencePassed = None
    ResultDsssDemodPayloadLength = None
    ResultDsssDemodPeakEvm = None
    ResultDsssDemodPeakEvmMaximum = None
    ResultDsssDemodPeakEvmMinimum = None
    ResultDsssDemodPhaseErrorRmsAverage = None
    ResultDsssDemodPhaseErrorRmsMaximum = None
    ResultDsssDemodPhaseErrorRmsMinimum = None
    ResultDsssDemodPhaseErrorRmsStandardDeviation = None
    ResultDsssDemodPreambleType = None
    ResultDsssDemodQuadratureSkew = None
    ResultDsssDemodQuadratureSkewAverage = None
    ResultDsssDemodQuadratureSkewMaximum = None
    ResultDsssDemodQuadratureSkewMinimum = None
    ResultDsssDemodQuadratureSkewStandardDeviation = None
    ResultDsssDemodRmsEvm = None
    ResultDsssDemodRmsEvmAverage = None
    ResultDsssDemodRmsEvmMaximum = None
    ResultDsssDemodRmsEvmMinimum = None
    ResultDsssDemodRmsEvmStandardDeviation = None
    ResultDsssDemodSampleClockOffset = None
    ResultDsssDemodSampleClockOffsetAverage = None
    ResultDsssDemodSampleClockOffsetMaximum = None
    ResultDsssDemodSampleClockOffsetMinimum = None
    ResultDsssDemodSampleClockOffsetStandardDeviation = None
    ResultDsssDemodSfdFound = None
    ResultDsssPowerRampDownTime = None
    ResultDsssPowerRampUpTime = None
    ResultETSIIBEDeltaACLRFrequencyVector = None
    ResultETSIIBEDeltaACLRMarginVector = None
    ResultETSIIBEMargin = None
    ResultETSIIBEMarginFrequencyVector = None
    ResultETSIIBEMarginVector = None
    ResultETSIIBEViolation = None
    ResultMaxSpectralDensity = None
    ResultObw = None
    ResultObwHighFrequency = None
    ResultObwLowFrequency = None
    ResultOfdmDemod80211ahPreambleType = None
    ResultOfdmDemod80211nPlcpFrameFormat = None
    ResultOfdmDemodAggregation = None
    ResultOfdmDemodAverageGatedPower = None
    ResultOfdmDemodAverageGatedPowerAverage = None
    ResultOfdmDemodAverageGatedPowerMaximum = None
    ResultOfdmDemodAverageGatedPowerMinimum = None
    ResultOfdmDemodAverageGatedPowerStandardDeviation = None
    ResultOfdmDemodBurstStartTime = None
    ResultOfdmDemodCarrierFrequencyLeakage = None
    ResultOfdmDemodCarrierFrequencyLeakageAverage = None
    ResultOfdmDemodCarrierFrequencyLeakageMaximum = None
    ResultOfdmDemodCarrierFrequencyLeakageMinimum = None
    ResultOfdmDemodCarrierFrequencyLeakageStandardDeviation = None
    ResultOfdmDemodCarrierFrequencyOffset = None
    ResultOfdmDemodCarrierFrequencyOffsetAverage = None
    ResultOfdmDemodCarrierFrequencyOffsetCcdfTenPercent = None
    ResultOfdmDemodCarrierFrequencyOffsetMaximum = None
    ResultOfdmDemodCarrierFrequencyOffsetMinimum = None
    ResultOfdmDemodCarrierFrequencyOffsetStandardDeviation = None
    ResultOfdmDemodChannelMatrixAbsolutePowerAverage = None
    ResultOfdmDemodChannelMatrixAbsolutePowerMaximum = None
    ResultOfdmDemodChannelMatrixAbsolutePowerMinimum = None
    ResultOfdmDemodChannelMatrixAbsolutePowerStdDev = None
    ResultOfdmDemodChannelMatrixCrossPowerMaximum = None
    ResultOfdmDemodChannelMatrixCrossPowerMinimum = None
    ResultOfdmDemodChannelMatrixCrossPowerStdDev = None
    ResultOfdmDemodCommmonPhaseErrorAverage = None
    ResultOfdmDemodCommmonPhaseErrorMaximum = None
    ResultOfdmDemodCommmonPhaseErrorMinimum = None
    ResultOfdmDemodCommmonPhaseErrorStandardDeviation = None
    ResultOfdmDemodCommonPhaseErrorAverage = None
    ResultOfdmDemodCommonPhaseErrorMaximum = None
    ResultOfdmDemodCommonPhaseErrorMinimum = None
    ResultOfdmDemodCommonPhaseErrorStandardDeviation = None
    ResultOfdmDemodCommonPilotErrorRms = None
    ResultOfdmDemodCommonPilotErrorRmsAverage = None
    ResultOfdmDemodCommonPilotErrorRmsMaximum = None
    ResultOfdmDemodCommonPilotErrorRmsMinimum = None
    ResultOfdmDemodCommonPilotErrorRmsStandardDeviation = None
    ResultOfdmDemodCrossPower = None
    ResultOfdmDemodCrossPowerAverage = None
    ResultOfdmDemodDataRate = None
    ResultOfdmDemodDataRmsEvm = None
    ResultOfdmDemodDataRmsEvmAverage = None
    ResultOfdmDemodDataRmsEvmMaximum = None
    ResultOfdmDemodDataRmsEvmMinimum = None
    ResultOfdmDemodDataRmsEvmStandardDeviation = None
    ResultOfdmDemodDcmEnabled = None
    ResultOfdmDemodDetectedPsduLength = None
    ResultOfdmDemodDetectedS1gSigLength = None
    ResultOfdmDemodDsssofdmHeaderCrcPassed = None
    ResultOfdmDemodEffectiveDataRate = None
    ResultOfdmDemodFecCodingType = None
    ResultOfdmDemodGatedPowerMeanPowerAverage = None
    ResultOfdmDemodGatedPowerMeanPowerMaximum = None
    ResultOfdmDemodGatedPowerMeanPowerMinimum = None
    ResultOfdmDemodGatedPowerMeanPowerStandardDeviation = None
    ResultOfdmDemodGatedPowerPeakPowerAverage = None
    ResultOfdmDemodGatedPowerPeakPowerMaximum = None
    ResultOfdmDemodGatedPowerPeakPowerMinimum = None
    ResultOfdmDemodGatedPowerPeakPowerStandardDeviation = None
    ResultOfdmDemodGuardInterval = None
    ResultOfdmDemodHeaderParityPassed = None
    ResultOfdmDemodHeLtfSize = None
    ResultOfdmDemodHeSigACrcPassed = None
    ResultOfdmDemodHeSigBCrcPassed = None
    ResultOfdmDemodHeSigBDualCarrierModulationEnabled = None
    ResultOfdmDemodHeSigBMcsIndex = None
    ResultOfdmDemodHtSigCrcPassed = None
    ResultOfdmDemodIqGainImbalance = None
    ResultOfdmDemodIqGainImbalanceAverage = None
    ResultOfdmDemodIqGainImbalanceMaximum = None
    ResultOfdmDemodIqGainImbalanceMinimum = None
    ResultOfdmDemodIqGainImbalanceStandardDeviation = None
    ResultOfdmDemodLSigPayloadLength = None
    ResultOfdmDemodMacFrameCheckSequencePassed = None
    ResultOfdmDemodMcsIndex = None
    ResultOfdmDemodMidamblePeriodicity = None
    ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageAverage = None
    ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageMaximum = None
    ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageMinimum = None
    ResultOfdmDemodNoiseAbsoluteCarrierFrequencyLeakageStandardDeviation = None
    ResultOfdmDemodNoiseCompensationApplied = None
    ResultOfdmDemodNotSoundingBit = None
    ResultOfdmDemodNumberOfExtensionSpatialStreams = None
    ResultOfdmDemodNumberofHeSigBSymbols = None
    ResultOfdmDemodNumberOfOfdmSymbols = None
    ResultOfdmDemodNumberOfSpaceTimeStreams = None
    ResultOfdmDemodNumberOfSymbolsUsed = None
    ResultOfdmDemodNumberOfUsers = None
    ResultOfdmDemodPacketExtentionDisambiguity = None
    ResultOfdmDemodPacketExtentionDuration = None
    ResultOfdmDemodPayloadLength = None
    ResultOfdmDemodPilotRmsEvm = None
    ResultOfdmDemodPilotRmsEvmAverage = None
    ResultOfdmDemodPilotRmsEvmMaximum = None
    ResultOfdmDemodPilotRmsEvmMinimum = None
    ResultOfdmDemodPilotRmsEvmStandardDeviation = None
    ResultOfdmDemodPpduType = None
    ResultOfdmDemodPreFecPaddingFactor = None
    ResultOfdmDemodQuadratureSkew = None
    ResultOfdmDemodQuadratureSkewAverage = None
    ResultOfdmDemodQuadratureSkewMaximum = None
    ResultOfdmDemodQuadratureSkewMinimum = None
    ResultOfdmDemodQuadratureSkewStandardDeviation = None
    ResultOfdmDemodRmsEvm = None
    ResultOfdmDemodRmsEvmAverage = None
    ResultOfdmDemodRmsEvmMaximum = None
    ResultOfdmDemodRmsEvmMinimum = None
    ResultOfdmDemodRmsEvmStandardDeviation = None
    ResultOfdmDemodRmsPhaseError = None
    ResultOfdmDemodRuOffset = None
    ResultOfdmDemodRuSize = None
    ResultOfdmDemodS1gSigCrcPassed = None
    ResultOfdmDemodS1gSigLength = None
    ResultOfdmDemodSampleClockOffset = None
    ResultOfdmDemodSampleClockOffsetAverage = None
    ResultOfdmDemodSampleClockOffsetMaximum = None
    ResultOfdmDemodSampleClockOffsetMinimum = None
    ResultOfdmDemodSampleClockOffsetStandardDeviation = None
    ResultOfdmDemodScramblerSeed = None
    ResultOfdmDemodShortGuardIntervalB1Bit = None
    ResultOfdmDemodSpaceTimeStreamOffset = None
    ResultOfdmDemodSpectralFlatnessMargin = None
    ResultOfdmDemodSpectralFlatnessMarginAverage = None
    ResultOfdmDemodSpectralFlatnessMarginMaximum = None
    ResultOfdmDemodSpectralFlatnessMarginMinimum = None
    ResultOfdmDemodSpectralFlatnessMarginStandardDeviation = None
    ResultOfdmDemodSpectralFlatnessMarginSubcarrierIndex = None
    ResultOfdmDemodStaId = None
    ResultOfdmDemodStbcAllStreamsEnabled = None
    ResultOfdmDemodStbcIndex = None
    ResultOfdmDemodStreamPowerAverage = None
    ResultOfdmDemodStreamPowerMaximum = None
    ResultOfdmDemodStreamPowerMinimum = None
    ResultOfdmDemodStreamPowerStandardDeviation = None
    ResultOfdmDemodTimingSkew = None
    ResultOfdmDemodTimingSkewAverage = None
    ResultOfdmDemodTimingSkewMaximum = None
    ResultOfdmDemodTimingSkewMinimum = None
    ResultOfdmDemodTimingSkewStandardDeviation = None
    ResultOfdmDemodTransmissionMode = None
    ResultOfdmDemodUnusedToneErrorMargin = None
    ResultOfdmDemodUnusedToneErrorMarginRuIndex = None
    ResultOfdmDemodUnusedToneErrorMarginVector = None
    ResultOfdmDemodVhtSigACrcPassed = None
    ResultOfdmDemodVhtSigBCrcPassed = None
    ResultOfdmLDPCExtraOfdmSymbol = None
    ResultOfdmNonHTModulationMode = None
    ResultOfdmTVHTMode = None
    ResultOfdmTVHTSIGACRCPassed = None
    ResultSpectralMaskFrequencyOffsetsUsed = None
    ResultSpectralMaskMargin = None
    ResultSpectralMaskMarginFrequencyVector = None
    ResultSpectralMaskMarginPowerSpectralDensityVector = None
    ResultSpectralMaskMarginVector = None
    ResultSpectralMaskPowerOffsetsUsed = None
    ResultSpectralMaskReferenceLevel = None
    ResultSpectralMaskViolation = None
    ResultSpectralMeasurementsChannelPower = None
    ResultTxpAveragePowerAverage = None
    ResultTxpAveragePowerMaximum = None
    ResultTxpAveragePowerMinimum = None
    ResultTxpAveragePowerStandardDeviation = None
    ResultTxpAveragePowerWithIdleTimeAverage = None
    ResultTxpAveragePowerWithIdleTimeMaximum = None
    ResultTxpAveragePowerWithIdleTimeMinimum = None
    ResultTxpAveragePowerWithIdleTimeStandardDeviation = None
    ResultTxpowerMeasurementsAveragePower = None
    ResultTxpowerMeasurementsPeakPower = None
    ResultTxpPeakPowerAverage = None
    ResultTxpPeakPowerMaximum = None
    ResultTxpPeakPowerMinimum = None
    ResultTxpPeakPowerStandardDeviation = None
    RuOffset = None
    RuSize = None
    SampleClockRateFactor = None
    ScramblerSeed = None
    ShortGuardIntervalB1Bit = None
    SpaceTimeStreamOffset = None
    Span = None
    SpectralMaskCenterFrequency = None
    SpectralMaskCombinedMaskEnabled = None
    SpectralMaskEnabled = None
    SpectralMaskFrequencyOffsets = None
    SpectralMaskNumberOfAverages = None
    SpectralMaskPowerOffsets = None
    SpectralMaskReferenceLevel = None
    SpectralMaskReferenceLevelType = None
    SpectralMaskTraceEnabled = None
    SpectralMaskTransmitPowerClass = None
    SpectralMaskType = None
    SpectralMeasurementsAllEnabled = None
    SpectralMeasurementsChannelPowerAutoMeasureBWEnabled = None
    SpectralMeasurementsChannelPowerEnabled = None
    SpectralMeasurementsChannelPowerMeasurementBandwidth = None
    SpectralMeasurementsChannelPowerNumberOfAverages = None
    Standard = None
    StbcAllStreamsEnabled = None
    StbcIndex = None
    SwapIAndQEnabled = None
    TclkSynchronisationEnabled = None
    TransmissionMode = None
    TriggerDelay = None
    TxPowerBurstDetectionEnabled = None
    TxPowerMeasurementLength = None
    TxpowerMeasurementsEnabled = None
    TxpowerMeasurementsMode = None
    TxpowerMeasurementsNumberOfAverages = None
    TxpowerMeasurementsPvtTraceEnabled = None
    value__ = None
    _80211ahPreambleType = None
    _80211nPlcpFrameFormat = None


class niWLANG(object, IDisposable):
    """
    niWLANG(toolkitCompatibilityVersion: int)
    niWLANG(sessionName: str, toolkitCompatibilityVersion: int) -> int
    """
    def ChannelNumberToCarrierFrequency(self, frequencyBand, channelBandwidth, channelNumber, secondaryFactor, chStartingFactor, carrierFrequency):
        """ ChannelNumberToCarrierFrequency(self: niWLANG, frequencyBand: int, channelBandwidth: float, channelNumber: int, secondaryFactor: int, chStartingFactor: float) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211abgjpn(self, channelStartingFrequency, channelBandwidth, channelNumber, secondaryFactor, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211abgjpn(self: niWLANG, channelStartingFrequency: float, channelBandwidth: float, channelNumber: int, secondaryFactor: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211ac(self, channelStartingFrequencyHz, channelNumber, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211ac(self: niWLANG, channelStartingFrequencyHz: float, channelNumber: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211af(self, channelStartingFrequency, channelBandwidth, channelNumber, TVHTMode, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211af(self: niWLANG, channelStartingFrequency: float, channelBandwidth: float, channelNumber: int, TVHTMode: int) -> (int, float) """
        pass

    def ChannelNumberToCarrierFrequency80211ah(self, channelStartingFrequencyHz, channelNumber, carrierFrequency):
        """ ChannelNumberToCarrierFrequency80211ah(self: niWLANG, channelStartingFrequencyHz: float, channelNumber: int) -> (int, float) """
        pass

    def Close(self):
        """ Close(self: niWLANG) """
        pass

    def ConfigureMultipleDeviceSynchronization(self, rfsgHandles, numofChannels, masterReferenceClockSource, triggerLines, numofTriggerLines):
        """ ConfigureMultipleDeviceSynchronization(self: niWLANG, rfsgHandles: Array[HandleRef], numofChannels: int, masterReferenceClockSource: str, triggerLines: Array[int], numofTriggerLines: int) -> int """
        pass

    def CreateAndWriteWaveformsToFile(self, filePath, operation):
        """ CreateAndWriteWaveformsToFile(self: niWLANG, filePath: str, operation: int) -> int """
        pass

    def CreateMIMOWaveformsComplexF64(self, reset, t0, dt, waveforms, numberOfTxChains, individualWaveformSize, actualNumSamplesinEachWfm, done):
        """ CreateMIMOWaveformsComplexF64(self: niWLANG, reset: int, t0: Array[float], dt: Array[float], waveforms: Array[niComplexNumber], numberOfTxChains: int, individualWaveformSize: int) -> (int, int, int) """
        pass

    def CreateTriggerFrameMSDU(self, channelString, generationDone, triggerFrameMSDUBits, actualDataArraySize):
        """ CreateTriggerFrameMSDU(self: niWLANG, channelString: str, triggerFrameMSDUBits: Array[int]) -> (int, int, int) """
        pass

    def CreateWaveformComplexF64(self, reset, t0, dt, waveform, waveformSize, actualNumWaveformSamples, done):
        """ CreateWaveformComplexF64(self: niWLANG, reset: int, waveform: Array[niComplexNumber], waveformSize: int) -> (int, float, float, int, int) """
        pass

    def DeallocateMemory(self):
        """ DeallocateMemory(self: niWLANG) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: niWLANG) """
        pass

    def GetActualHeadroom(self, channel, value):
        """ GetActualHeadroom(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetActualOfdmDataRate(self, channel, value):
        """ GetActualOfdmDataRate(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetAllIqImpairmentsEnabled(self, channel, value):
        """ GetAllIqImpairmentsEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetAmpduEnabled(self, channel, value):
        """ GetAmpduEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetAPTXPower(self, channelString, value):
        """ GetAPTXPower(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetAutoHeadroomEnabled(self, channel, value):
        """ GetAutoHeadroomEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetAutoPayloadDataLengthMode(self, channelString, value):
        """ GetAutoPayloadDataLengthMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetAveragePowerReference(self, channelString, value):
        """ GetAveragePowerReference(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetAwgnEnabled(self, channel, value):
        """ GetAwgnEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetBSSColor(self, channelString, value):
        """ GetBSSColor(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetBurstStartLocations(self, channelString, dataArray, actualNumDataArrayElements):
        """ GetBurstStartLocations(self: niWLANG, channelString: str, dataArray: Array[int]) -> (int, int) """
        pass

    def GetBurstStopLocations(self, channelString, dataArray, actualNumDataArrayElements):
        """ GetBurstStopLocations(self: niWLANG, channelString: str, dataArray: Array[int]) -> (int, int) """
        pass

    def GetCarrierFrequency(self, channel, value):
        """ GetCarrierFrequency(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetCarrierFrequencyOffset(self, channel, value):
        """ GetCarrierFrequencyOffset(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetCarrierToNoiseRatio(self, channel, value):
        """ GetCarrierToNoiseRatio(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetChannelBandwidth(self, channel, value):
        """ GetChannelBandwidth(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetCompatibilityVersion(self, channel, value):
        """ GetCompatibilityVersion(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetDsssDataRate(self, channel, value):
        """ GetDsssDataRate(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetDsssPreambleType(self, channel, value):
        """ GetDsssPreambleType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetDsssWindowLength(self, channel, value):
        """ GetDsssWindowLength(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetDualCarrierModulationEnabled(self, channelString, value):
        """ GetDualCarrierModulationEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetErrorString(self, status, msg):
        """ GetErrorString(self: niWLANG, status: int, msg: StringBuilder) -> int """
        pass

    def GetFecCodingType(self, channel, value):
        """ GetFecCodingType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetFrameDuration(self, channel, value):
        """ GetFrameDuration(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetFullscaleBackoff(self, channelString, value):
        """ GetFullscaleBackoff(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetGuardInterval(self, channel, value):
        """ GetGuardInterval(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetHeaderEncoderEnabled(self, channel, value):
        """ GetHeaderEncoderEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetHeaderInterleaverEnabled(self, channel, value):
        """ GetHeaderInterleaverEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetHeadroom(self, channel, value):
        """ GetHeadroom(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetHESIGBDualCarrierModulationEnabled(self, channelString, value):
        """ GetHESIGBDualCarrierModulationEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetHESIGBMCSIndex(self, channelString, value):
        """ GetHESIGBMCSIndex(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetIDcOffset(self, channel, value):
        """ GetIDcOffset(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetIdleInterval(self, channel, value):
        """ GetIdleInterval(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetIdleIntervalMode(self, channelString, value):
        """ GetIdleIntervalMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetIqGainImbalance(self, channel, value):
        """ GetIqGainImbalance(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetIqRate(self, channel, value):
        """ GetIqRate(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetIqWaveformSize(self, channel, value):
        """ GetIqWaveformSize(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetLdpcExtraSymbolSegment(self, channelString, value):
        """ GetLdpcExtraSymbolSegment(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetLockedClockBitEnabled(self, channel, value):
        """ GetLockedClockBitEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetLOFrequencyOffset(self, channelString, value):
        """ GetLOFrequencyOffset(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetLOFrequencyOffsetMode(self, channelString, value):
        """ GetLOFrequencyOffsetMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetLOSharingEnabled(self, channelString, value):
        """ GetLOSharingEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetLSIGLength(self, channelString, value):
        """ GetLSIGLength(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetMacAddress1(self, channel, value):
        """ GetMacAddress1(self: niWLANG, channel: str) -> (int, Int64) """
        pass

    def GetMacAddress1Enabled(self, channel, value):
        """ GetMacAddress1Enabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacAddress1Length(self, channel, value):
        """ GetMacAddress1Length(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacAddress2(self, channel, value):
        """ GetMacAddress2(self: niWLANG, channel: str) -> (int, Int64) """
        pass

    def GetMacAddress2Enabled(self, channel, value):
        """ GetMacAddress2Enabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacAddress2Length(self, channel, value):
        """ GetMacAddress2Length(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacAddress3(self, channel, value):
        """ GetMacAddress3(self: niWLANG, channel: str) -> (int, Int64) """
        pass

    def GetMacAddress3Enabled(self, channel, value):
        """ GetMacAddress3Enabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacAddress4(self, channel, value):
        """ GetMacAddress4(self: niWLANG, channel: str) -> (int, Int64) """
        pass

    def GetMacAddress4Enabled(self, channel, value):
        """ GetMacAddress4Enabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMACCurrentSequenceControl(self, channelString, value):
        """ GetMACCurrentSequenceControl(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetMacDurationOrId(self, channel, value):
        """ GetMacDurationOrId(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacFcsEnabled(self, channel, value):
        """ GetMacFcsEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacFragmentNumberIncrementEnabled(self, channel, value):
        """ GetMacFragmentNumberIncrementEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacFrameControl(self, channel, value):
        """ GetMacFrameControl(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacFrameFormat(self, channel, value):
        """ GetMacFrameFormat(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacHeaderEnabled(self, channel, value):
        """ GetMacHeaderEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacHtControl(self, channel, value):
        """ GetMacHtControl(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacHtControlEnabled(self, channel, value):
        """ GetMacHtControlEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMACOverheadLength(self, channelString, value):
        """ GetMACOverheadLength(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetMacQosControl(self, channel, value):
        """ GetMacQosControl(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacQosControlEnabled(self, channel, value):
        """ GetMacQosControlEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacSequenceControl(self, channel, value):
        """ GetMacSequenceControl(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacSequenceControlEnabled(self, channel, value):
        """ GetMacSequenceControlEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacSequenceNumberIncrementEnabled(self, channel, value):
        """ GetMacSequenceNumberIncrementEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMacSequenceNumberIncrementInterval(self, channel, value):
        """ GetMacSequenceNumberIncrementInterval(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMappingMatrix(self, channelString, mappingMatrix, numMappingMatrixRows, numMappingMatrixColumns):
        """ GetMappingMatrix(self: niWLANG, channelString: str, mappingMatrix: Array[niComplexNumber], numMappingMatrixRows: int, numMappingMatrixColumns: int) -> int """
        pass

    def GetMappingMatrixType(self, channel, value):
        """ GetMappingMatrixType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMaxExpectedPapr(self, channel, value):
        """ GetMaxExpectedPapr(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetMaximumHardwareIqRate(self, channel, value):
        """ GetMaximumHardwareIqRate(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetMcsIndex(self, channel, value):
        """ GetMcsIndex(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMpduLength(self, channel, value):
        """ GetMpduLength(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetMultiSegmentGenerationMode(self, channelString, value):
        """ GetMultiSegmentGenerationMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetMUMimoLtfModeEnabled(self, channelString, value):
        """ GetMUMimoLtfModeEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetNominalPacketPadding(self, channelString, value):
        """ GetNominalPacketPadding(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetNonHTModulationMode(self, channel, value):
        """ GetNonHTModulationMode(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNonHtModulationMode(self, channel, value):
        """ GetNonHtModulationMode(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNotSoundingBit(self, channel, value):
        """ GetNotSoundingBit(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNumberOfDataSymbols(self, channelString, value):
        """ GetNumberOfDataSymbols(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetNumberOfExtensionSpatialStreams(self, channel, value):
        """ GetNumberOfExtensionSpatialStreams(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNumberOfFrames(self, channel, value):
        """ GetNumberOfFrames(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNumberOfHELTFSymbols(self, channelString, value):
        """ GetNumberOfHELTFSymbols(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetNumberOfMPDUs(self, channelString, value):
        """ GetNumberOfMPDUs(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetNumberOfSegments(self, channel, value):
        """ GetNumberOfSegments(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNumberOfSpaceTimeStreams(self, channel, value):
        """ GetNumberOfSpaceTimeStreams(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNumberOfTransmitChannels(self, channel, value):
        """ GetNumberOfTransmitChannels(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetNumberOfUsers(self, channelString, value):
        """ GetNumberOfUsers(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetNumberOfUsersFromRUAllocation(self, channelString, numberOfUsers):
        """ GetNumberOfUsersFromRUAllocation(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetOfdmDataRate(self, channel, value):
        """ GetOfdmDataRate(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetOFDMGuardIntervalType(self, channel, value):
        """ GetOFDMGuardIntervalType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetOFDMHELTFSize(self, channelString, value):
        """ GetOFDMHELTFSize(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetOfdmLegacyScalingEnabled(self, channel, value):
        """ GetOfdmLegacyScalingEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetOfdmMidamblePeriodicity(self, channelString, value):
        """ GetOfdmMidamblePeriodicity(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetOfdmWindowLength(self, channel, value):
        """ GetOfdmWindowLength(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetOversamplingFactor(self, channel, value):
        """ GetOversamplingFactor(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPacketExtensionDuration(self, channelString, value):
        """ GetPacketExtensionDuration(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetPayloadAutoDataLength(self, channelString, value):
        """ GetPayloadAutoDataLength(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPayloadAutoNumberOfMpdus(self, channelString, value):
        """ GetPayloadAutoNumberOfMpdus(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPayloadDataLength(self, channel, value):
        """ GetPayloadDataLength(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadDataType(self, channel, value):
        """ GetPayloadDataType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadEncoderEnabled(self, channel, value):
        """ GetPayloadEncoderEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadInterleaverEnabled(self, channel, value):
        """ GetPayloadInterleaverEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadMacFrameType(self, channelString, value):
        """ GetPayloadMacFrameType(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPayloadNumberOfMpdus(self, channel, value):
        """ GetPayloadNumberOfMpdus(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadPnOrder(self, channel, value):
        """ GetPayloadPnOrder(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadPnSeed(self, channel, value):
        """ GetPayloadPnSeed(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadScramblerEnabled(self, channel, value):
        """ GetPayloadScramblerEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadScramblerSeed(self, channel, value):
        """ GetPayloadScramblerSeed(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPayloadUserDefinedBits(self, channel, data, dataArraySize, actualNumDataElements):
        """ GetPayloadUserDefinedBits(self: niWLANG, channel: str, data: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetPEDisambiguity(self, channelString, value):
        """ GetPEDisambiguity(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPowerBoostFactor(self, channelString, value):
        """ GetPowerBoostFactor(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetPowerLevel(self, channel, value):
        """ GetPowerLevel(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetPPDUType(self, channelString, value):
        """ GetPPDUType(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPreamblePuncturingEnabled(self, channelString, value):
        """ GetPreamblePuncturingEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPreamblePuncturingMask(self, channelString, value):
        """ GetPreamblePuncturingMask(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPreFECPaddingFactor(self, channelString, value):
        """ GetPreFECPaddingFactor(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPrimary20MHzChannelIndex(self, channelString, value):
        """ GetPrimary20MHzChannelIndex(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetPulseShapingFilterEnabled(self, channel, value):
        """ GetPulseShapingFilterEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPulseShapingFilterLength(self, channel, value):
        """ GetPulseShapingFilterLength(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetPulseShapingFilterParameter(self, channel, value):
        """ GetPulseShapingFilterParameter(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetPulseShapingFilterType(self, channel, value):
        """ GetPulseShapingFilterType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetQDcOffset(self, channel, value):
        """ GetQDcOffset(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetQuadratureSkew(self, channel, value):
        """ GetQuadratureSkew(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetRelativePower(self, channelString, value):
        """ GetRelativePower(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetRFBlankingEnabled(self, channelString, value):
        """ GetRFBlankingEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetRFBlankingMarkerPositions(self, channelString, dataArray, dataArraySize, actualNumDataArrayElements):
        """ GetRFBlankingMarkerPositions(self: niWLANG, channelString: str, dataArray: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetRUAllocation(self, channel, data, dataArraySize, actualNumDataElements):
        """ GetRUAllocation(self: niWLANG, channel: str, data: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetRUAllocationMode(self, channelString, value):
        """ GetRUAllocationMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetRUOffset(self, channelString, value):
        """ GetRUOffset(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetRUSize(self, channelString, value):
        """ GetRUSize(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetSampleClockOffset(self, channel, value):
        """ GetSampleClockOffset(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetSampleClockRateFactor(self, channel, value):
        """ GetSampleClockRateFactor(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetScalarAttributeF64(self, channelString, attributeID, attributeValue):
        """ GetScalarAttributeF64(self: niWLANG, channelString: str, attributeID: niWLANGProperties) -> (int, float) """
        pass

    def GetScalarAttributeI32(self, channelString, attributeID, attributeValue):
        """ GetScalarAttributeI32(self: niWLANG, channelString: str, attributeID: niWLANGProperties) -> (int, int) """
        pass

    def GetScalarAttributeI64(self, channelString, attributeID, attributeValue):
        """
        GetScalarAttributeI64(self: niWLANG, channelString: str, attributeID: niWLANGProperties) -> (int, int)
        GetScalarAttributeI64(self: niWLANG, channelString: str, attributeID: niWLANGProperties) -> (int, Int64)
        """
        pass

    def GetSignalBandwidth(self, channelString, value):
        """ GetSignalBandwidth(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetSpaceTimeStreamOffset(self, channelString, value):
        """ GetSpaceTimeStreamOffset(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetSpatialMappingMode(self, channelString, value):
        """ GetSpatialMappingMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetSTAID(self, channelString, value):
        """ GetSTAID(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetStandard(self, channel, value):
        """ GetStandard(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetStbcAllStreamsEnabled(self, channel, value):
        """ GetStbcAllStreamsEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetStbcIndex(self, channel, value):
        """ GetStbcIndex(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetSubcarrierMask(self, channel, value):
        """ GetSubcarrierMask(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetSwapIAndQEnabled(self, channel, value):
        """ GetSwapIAndQEnabled(self: niWLANG, channel: str) -> (int, int) """
        pass

    def GetTargetRSSI(self, channelString, value):
        """ GetTargetRSSI(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetTimeDelay(self, channelString, value):
        """ GetTimeDelay(self: niWLANG, channelString: str) -> (int, float) """
        pass

    def GetTimingSkew(self, channel, value):
        """ GetTimingSkew(self: niWLANG, channel: str) -> (int, float) """
        pass

    def GetToolkitCompatibilityVersion(self, channelString, value):
        """ GetToolkitCompatibilityVersion(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetTransmissionMode(self, channelString, value):
        """ GetTransmissionMode(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetTriggerFrameAID12(self, channelString, value):
        """ GetTriggerFrameAID12(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetTriggerFrameCSRequired(self, channelString, value):
        """ GetTriggerFrameCSRequired(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetTriggerFrameMaximumMacPaddingDuration(self, channelString, value):
        """ GetTriggerFrameMaximumMacPaddingDuration(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetUserEnabled(self, channelString, value):
        """ GetUserEnabled(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetVectorAttributeF64(self, channelString, attributeID, data, dataArraySize, actualNumDataElements):
        """ GetVectorAttributeF64(self: niWLANG, channelString: str, attributeID: niWLANGProperties, data: Array[float], dataArraySize: int) -> (int, int) """
        pass

    def GetVectorAttributeI32(self, channelString, attributeID, data, dataArraySize, actualNumDataElements):
        """ GetVectorAttributeI32(self: niWLANG, channelString: str, attributeID: niWLANGProperties, data: Array[int], dataArraySize: int) -> (int, int) """
        pass

    def GetWindowingMethod(self, channelString, value):
        """ GetWindowingMethod(self: niWLANG, channelString: str) -> (int, int) """
        pass

    def GetWindowLength(self, channel, value):
        """ GetWindowLength(self: niWLANG, channel: str) -> (int, float) """
        pass

    def Get_80211ahPreambleType(self, channel, value):
        """ Get_80211ahPreambleType(self: niWLANG, channel: str) -> (int, int) """
        pass

    def Get_80211ahUplinkIndication(self, channel, value):
        """ Get_80211ahUplinkIndication(self: niWLANG, channel: str) -> (int, int) """
        pass

    def Get_80211nPlcpFrameFormat(self, channel, value):
        """ Get_80211nPlcpFrameFormat(self: niWLANG, channel: str) -> (int, int) """
        pass

    def LoadConfigurationFromFile(self, filePath, reset):
        """ LoadConfigurationFromFile(self: niWLANG, filePath: str, reset: int) -> int """
        pass

    def ReadBurstStartLocationsFromFile(self, filePath, waveformName, burstStartLocations, actualDataArraySize):
        """ ReadBurstStartLocationsFromFile(self: niWLANG, filePath: str, waveformName: str, burstStartLocations: Array[int]) -> (int, int) """
        pass

    def ReadBurstStopLocationsFromFile(self, filePath, waveformName, burstStopLocations, actualDataArraySize):
        """ ReadBurstStopLocationsFromFile(self: niWLANG, filePath: str, waveformName: str, burstStopLocations: Array[int]) -> (int, int) """
        pass

    def ReadWaveformFromFile(self, filePath, waveformName, offset, count, t0, dt, waveform, waveformSize, actualSize, iQRate, headroom, eOF):
        """ ReadWaveformFromFile(self: niWLANG, filePath: str, waveformName: str, offset: Int64, count: Int64, waveform: Array[niComplexNumber], waveformSize: int) -> (int, float, float, int, float, float, int) """
        pass

    def ResetSession(self):
        """ ResetSession(self: niWLANG) -> int """
        pass

    def RFSGClearDatabase(self, rFSGSession, channelString, waveformName):
        """ RFSGClearDatabase(self: niWLANG, rFSGSession: HandleRef, channelString: str, waveformName: str) -> int """
        pass

    def RFSGConfigure(self, wLANChannelString, rFSGSession, hardwareChannelString):
        """ RFSGConfigure(self: niWLANG, wLANChannelString: str, rFSGSession: HandleRef, hardwareChannelString: str) -> int """
        pass

    def RFSGConfigureFrequencyMultipleLO(self, rfsgHandles, LOSource, exteralLOHandles, carrierFrequency, dataArraySize, rfsgLODaisyChainEnabled, LOExportToExternalDevicesEnabled):
        """ RFSGConfigureFrequencyMultipleLO(self: niWLANG, rfsgHandles: Array[HandleRef], LOSource: int, exteralLOHandles: Array[HandleRef], carrierFrequency: Array[float], dataArraySize: int, rfsgLODaisyChainEnabled: int, LOExportToExternalDevicesEnabled: int) -> int """
        pass

    def RFSGConfigureFrequencySingleLO(self, rfsgHandles, LOSource, exteralLOHandle, carrierFrequencies, rfsgLODaisyChainEnabled, LOExportToExternalDevicesEnabled):
        """ RFSGConfigureFrequencySingleLO(self: niWLANG, rfsgHandles: Array[HandleRef], LOSource: int, exteralLOHandle: HandleRef, carrierFrequencies: float, rfsgLODaisyChainEnabled: int, LOExportToExternalDevicesEnabled: int) -> int """
        pass

    def RFSGConfigurePowerLevel(self, rFSGSession, channelString, script, powerLevel):
        """ RFSGConfigurePowerLevel(self: niWLANG, rFSGSession: HandleRef, channelString: str, script: str, powerLevel: float) -> int """
        pass

    def RFSGConfigureScript(self, rFSGSession, channelString, script, powerLevel):
        """ RFSGConfigureScript(self: niWLANG, rFSGSession: HandleRef, channelString: str, script: str, powerLevel: float) -> int """
        pass

    def RFSGConfigureWaveform(self, wLANChannelString, rFSGSession, hardwareChannelString, resetHardware, waveformSize):
        """ RFSGConfigureWaveform(self: niWLANG, wLANChannelString: str, rFSGSession: HandleRef, hardwareChannelString: str, resetHardware: int) -> (int, int) """
        pass

    def RFSGCreateAndDownloadMIMOWaveforms(self, rFSGSessions, hardwareChannelStrings, numberOfTxChains, waveformName):
        """ RFSGCreateAndDownloadMIMOWaveforms(self: niWLANG, rFSGSessions: Array[HandleRef], hardwareChannelStrings: Array[str], numberOfTxChains: int, waveformName: str) -> int """
        pass

    def RFSGCreateAndDownloadWaveform(self, rFSGSession, hardwareChannelString, waveformName):
        """ RFSGCreateAndDownloadWaveform(self: niWLANG, rFSGSession: HandleRef, hardwareChannelString: str, waveformName: str) -> int """
        pass

    def RFSGForceTClkSynchronization(self, rfsgHandles, forceSync):
        """ RFSGForceTClkSynchronization(self: niWLANG, rfsgHandles: Array[HandleRef], forceSync: int) -> int """
        pass

    def RFSGMultipleDeviceInitiate(self, rfsgHandles):
        """ RFSGMultipleDeviceInitiate(self: niWLANG, rfsgHandles: Array[HandleRef]) -> int """
        pass

    def RFSGRetrieveBurstStartLocations(self, channelString, rfsgHandle, waveformName, burstStartLocations, actualDataArraySize):
        """ RFSGRetrieveBurstStartLocations(self: niWLANG, channelString: str, rfsgHandle: HandleRef, waveformName: str, burstStartLocations: Array[int]) -> (int, int) """
        pass

    def RFSGRetrieveBurstStopLocations(self, channelString, rfsgHandle, waveformName, burstStopLocations, actualDataArraySize):
        """ RFSGRetrieveBurstStopLocations(self: niWLANG, channelString: str, rfsgHandle: HandleRef, waveformName: str, burstStopLocations: Array[int]) -> (int, int) """
        pass

    def RFSGRetrieveIQRate(self, rFSGSession, channelString, waveformName, iQRate):
        """ RFSGRetrieveIQRate(self: niWLANG, rFSGSession: HandleRef, channelString: str, waveformName: str) -> (int, float) """
        pass

    def RFSGRetrieveIQRateAllWaveforms(self, rFSGSession, channelString, script, iQRate):
        """ RFSGRetrieveIQRateAllWaveforms(self: niWLANG, rFSGSession: HandleRef, channelString: str, script: str) -> (int, float) """
        pass

    def RFSGRetrieveMinimumPAPRAllWaveforms(self, rFSGSession, channelString, script, pAPR):
        """ RFSGRetrieveMinimumPAPRAllWaveforms(self: niWLANG, rFSGSession: HandleRef, channelString: str, script: str) -> (int, float) """
        pass

    def RFSGRetrievePAPR(self, rFSGSession, channelString, waveformName, pAPR):
        """ RFSGRetrievePAPR(self: niWLANG, rFSGSession: HandleRef, channelString: str, waveformName: str) -> (int, float) """
        pass

    def RFSGRetrieveWaveformSize(self, channelString, rfsgHandle, waveformName, waveformSize):
        """ RFSGRetrieveWaveformSize(self: niWLANG, channelString: str, rfsgHandle: HandleRef, waveformName: str) -> (int, int) """
        pass

    def RFSGStoreBurstStartLocations(self, channelString, rfsgHandle, waveformName, burstStartLocations):
        """ RFSGStoreBurstStartLocations(self: niWLANG, channelString: str, rfsgHandle: HandleRef, waveformName: str, burstStartLocations: Array[int]) -> int """
        pass

    def RFSGStoreBurstStopLocations(self, channelString, rfsgHandle, waveformName, burstStopLocations):
        """ RFSGStoreBurstStopLocations(self: niWLANG, channelString: str, rfsgHandle: HandleRef, waveformName: str, burstStopLocations: Array[int]) -> int """
        pass

    def RFSGStoreIQRate(self, rFSGSession, channelString, waveformName, iQRate):
        """ RFSGStoreIQRate(self: niWLANG, rFSGSession: HandleRef, channelString: str, waveformName: str, iQRate: float) -> int """
        pass

    def RFSGStorePAPR(self, rFSGSession, channelString, waveformName, pAPR):
        """ RFSGStorePAPR(self: niWLANG, rFSGSession: HandleRef, channelString: str, waveformName: str, pAPR: float) -> int """
        pass

    def SaveConfigurationToFile(self, filePath, operation):
        """ SaveConfigurationToFile(self: niWLANG, filePath: str, operation: int) -> int """
        pass

    def Set80211nPLCPFrameFormat(self, channelString, frameFormat):
        """ Set80211nPLCPFrameFormat(self: niWLANG, channelString: str, frameFormat: int) -> int """
        pass

    def SetAllIqImpairmentsEnabled(self, channel, value):
        """ SetAllIqImpairmentsEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetAmpduEnabled(self, channel, value):
        """ SetAmpduEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetAPTXPower(self, channelString, value):
        """ SetAPTXPower(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetAutoHeadroomEnabled(self, channel, value):
        """ SetAutoHeadroomEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetAutoPayloadDataLengthMode(self, channelString, value):
        """ SetAutoPayloadDataLengthMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetAveragePowerReference(self, channelString, value):
        """ SetAveragePowerReference(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetAwgnEnabled(self, channel, value):
        """ SetAwgnEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetBSSColor(self, channelString, value):
        """ SetBSSColor(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetCarrierFrequency(self, channel, value):
        """ SetCarrierFrequency(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetCarrierFrequencyOffset(self, channel, value):
        """ SetCarrierFrequencyOffset(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetCarrierToNoiseRatio(self, channel, value):
        """ SetCarrierToNoiseRatio(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetChannelBandwidth(self, channel, value):
        """ SetChannelBandwidth(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetDsssDataRate(self, channel, value):
        """ SetDsssDataRate(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetDSSSDataRate(self, channelString, dSSSDataRate):
        """ SetDSSSDataRate(self: niWLANG, channelString: str, dSSSDataRate: int) -> int """
        pass

    def SetDsssPreambleType(self, channel, value):
        """ SetDsssPreambleType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetDSSSPreambleType(self, channelString, preambleType):
        """ SetDSSSPreambleType(self: niWLANG, channelString: str, preambleType: int) -> int """
        pass

    def SetDsssWindowLength(self, channel, value):
        """ SetDsssWindowLength(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetDualCarrierModulationEnabled(self, channelString, value):
        """ SetDualCarrierModulationEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetFecCodingType(self, channel, value):
        """ SetFecCodingType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetFrameDuration(self, channel, value):
        """ SetFrameDuration(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetFullscaleBackoff(self, channelString, value):
        """ SetFullscaleBackoff(self: niWLANG, channelString: str, value: float) -> int """
        pass

    def SetGuardInterval(self, channel, value):
        """ SetGuardInterval(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetHeaderEncoderEnabled(self, channel, value):
        """ SetHeaderEncoderEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetHeaderInterleaverEnabled(self, channel, value):
        """ SetHeaderInterleaverEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetHeadroom(self, channel, value):
        """ SetHeadroom(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetHESIGBDualCarrierModulationEnabled(self, channelString, value):
        """ SetHESIGBDualCarrierModulationEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetHESIGBMCSIndex(self, channelString, value):
        """ SetHESIGBMCSIndex(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetIDcOffset(self, channel, value):
        """ SetIDcOffset(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetIdleInterval(self, channel, value):
        """ SetIdleInterval(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetIdleIntervalMode(self, channelString, value):
        """ SetIdleIntervalMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetIqGainImbalance(self, channel, value):
        """ SetIqGainImbalance(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetLdpcExtraSymbolSegment(self, channelString, value):
        """ SetLdpcExtraSymbolSegment(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetLockedClockBitEnabled(self, channel, value):
        """ SetLockedClockBitEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetLOFrequencyOffset(self, channelString, value):
        """ SetLOFrequencyOffset(self: niWLANG, channelString: str, value: float) -> int """
        pass

    def SetLOFrequencyOffsetMode(self, channelString, value):
        """ SetLOFrequencyOffsetMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetLOSharingEnabled(self, channelString, value):
        """ SetLOSharingEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetLSIGLength(self, channelString, value):
        """ SetLSIGLength(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetMacAddress1(self, channel, value):
        """ SetMacAddress1(self: niWLANG, channel: str, value: Int64) -> int """
        pass

    def SetMacAddress1Enabled(self, channel, value):
        """ SetMacAddress1Enabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacAddress1Length(self, channel, value):
        """ SetMacAddress1Length(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacAddress2(self, channel, value):
        """ SetMacAddress2(self: niWLANG, channel: str, value: Int64) -> int """
        pass

    def SetMacAddress2Enabled(self, channel, value):
        """ SetMacAddress2Enabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacAddress2Length(self, channel, value):
        """ SetMacAddress2Length(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacAddress3(self, channel, value):
        """ SetMacAddress3(self: niWLANG, channel: str, value: Int64) -> int """
        pass

    def SetMacAddress3Enabled(self, channel, value):
        """ SetMacAddress3Enabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacAddress4(self, channel, value):
        """ SetMacAddress4(self: niWLANG, channel: str, value: Int64) -> int """
        pass

    def SetMacAddress4Enabled(self, channel, value):
        """ SetMacAddress4Enabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMACCurrentSequenceControl(self, channelString, value):
        """ SetMACCurrentSequenceControl(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetMacDurationOrId(self, channel, value):
        """ SetMacDurationOrId(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacFcsEnabled(self, channel, value):
        """ SetMacFcsEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacFragmentNumberIncrementEnabled(self, channel, value):
        """ SetMacFragmentNumberIncrementEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacFrameControl(self, channel, value):
        """ SetMacFrameControl(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacFrameFormat(self, channel, value):
        """ SetMacFrameFormat(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacHeaderEnabled(self, channel, value):
        """ SetMacHeaderEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacHtControl(self, channel, value):
        """ SetMacHtControl(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacHtControlEnabled(self, channel, value):
        """ SetMacHtControlEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacQosControl(self, channel, value):
        """ SetMacQosControl(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacQosControlEnabled(self, channel, value):
        """ SetMacQosControlEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacSequenceControl(self, channel, value):
        """ SetMacSequenceControl(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacSequenceControlEnabled(self, channel, value):
        """ SetMacSequenceControlEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacSequenceNumberIncrementEnabled(self, channel, value):
        """ SetMacSequenceNumberIncrementEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMacSequenceNumberIncrementInterval(self, channel, value):
        """ SetMacSequenceNumberIncrementInterval(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMappingMatrix(self, channelString, mappingMatrix, numMappingMatrixRows, numMappingMatrixColumns):
        """ SetMappingMatrix(self: niWLANG, channelString: str, mappingMatrix: Array[niComplexNumber], numMappingMatrixRows: int, numMappingMatrixColumns: int) -> int """
        pass

    def SetMappingMatrixType(self, channel, value):
        """ SetMappingMatrixType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMaxExpectedPapr(self, channel, value):
        """ SetMaxExpectedPapr(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetMaximumHardwareIqRate(self, channel, value):
        """ SetMaximumHardwareIqRate(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetMcsIndex(self, channel, value):
        """ SetMcsIndex(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetMCSIndex(self, channelString, mCSIndex):
        """ SetMCSIndex(self: niWLANG, channelString: str, mCSIndex: int) -> int """
        pass

    def SetMultiSegmentGenerationMode(self, channelString, value):
        """ SetMultiSegmentGenerationMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetMUMimoLtfModeEnabled(self, channelString, value):
        """ SetMUMimoLtfModeEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetNominalPacketPadding(self, channelString, value):
        """ SetNominalPacketPadding(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetNonHtModulationMode(self, channel, nonHTDuplicateModulationMode):
        """ SetNonHtModulationMode(self: niWLANG, channel: str, nonHTDuplicateModulationMode: int) -> int """
        pass

    def SetNonHTModulationMode(self, channel, nonHTDuplicateModulationMode):
        """ SetNonHTModulationMode(self: niWLANG, channel: str, nonHTDuplicateModulationMode: int) -> int """
        pass

    def SetNotSoundingBit(self, channel, value):
        """ SetNotSoundingBit(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetNumberOfDataSymbols(self, channelString, value):
        """ SetNumberOfDataSymbols(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetNumberOfExtensionSpatialStreams(self, channel, value):
        """ SetNumberOfExtensionSpatialStreams(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetNumberOfFrames(self, channel, value):
        """ SetNumberOfFrames(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetNumberOfHELTFSymbols(self, channelString, value):
        """ SetNumberOfHELTFSymbols(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetNumberOfMPDUs(self, channelString, value):
        """ SetNumberOfMPDUs(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetNumberOfSegments(self, channel, value):
        """ SetNumberOfSegments(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetNumberOfSpaceTimeStreams(self, channel, value):
        """ SetNumberOfSpaceTimeStreams(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetNumberOfTransmitChannels(self, channel, value):
        """ SetNumberOfTransmitChannels(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetNumberOfUsers(self, channelString, mappingMatrixType):
        """ SetNumberOfUsers(self: niWLANG, channelString: str, mappingMatrixType: int) -> int """
        pass

    def SetOFDMDataRate(self, channelString, oFDMDataRate):
        """ SetOFDMDataRate(self: niWLANG, channelString: str, oFDMDataRate: int) -> int """
        pass

    def SetOfdmDataRate(self, channel, value):
        """ SetOfdmDataRate(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetOFDMGuardIntervalType(self, channel, value):
        """ SetOFDMGuardIntervalType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetOFDMHELTFSize(self, channelString, value):
        """ SetOFDMHELTFSize(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetOfdmLegacyScalingEnabled(self, channel, value):
        """ SetOfdmLegacyScalingEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetOfdmMidamblePeriodicity(self, channelString, value):
        """ SetOfdmMidamblePeriodicity(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetOFDMPacketExtensionThresholds(self, channelString, PPET16, PPET8, numberOfSpaceTimeStreams, RUSize):
        """ SetOFDMPacketExtensionThresholds(self: niWLANG, channelString: str, PPET16: Array[int], PPET8: Array[int], numberOfSpaceTimeStreams: Array[int], RUSize: Array[int]) -> int """
        pass

    def SetOfdmWindowLength(self, channel, value):
        """ SetOfdmWindowLength(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetOversamplingFactor(self, channel, value):
        """ SetOversamplingFactor(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadAutoDataLength(self, channelString, value):
        """ SetPayloadAutoDataLength(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPayloadAutoNumberOfMpdus(self, channelString, value):
        """ SetPayloadAutoNumberOfMpdus(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPayloadDataLength(self, channel, value):
        """ SetPayloadDataLength(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadDataType(self, channel, value):
        """ SetPayloadDataType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadEncoderEnabled(self, channel, value):
        """ SetPayloadEncoderEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadInterleaverEnabled(self, channel, value):
        """ SetPayloadInterleaverEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadMacFrameType(self, channelString, value):
        """ SetPayloadMacFrameType(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPayloadNumberOfMpdus(self, channel, value):
        """ SetPayloadNumberOfMpdus(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadPnOrder(self, channel, value):
        """ SetPayloadPnOrder(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadPnSeed(self, channel, value):
        """ SetPayloadPnSeed(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadScramblerEnabled(self, channel, value):
        """ SetPayloadScramblerEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadScramblerSeed(self, channel, value):
        """ SetPayloadScramblerSeed(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPayloadUserDefinedBits(self, channel, data, dataArraySize):
        """ SetPayloadUserDefinedBits(self: niWLANG, channel: str, data: Array[int], dataArraySize: int) -> int """
        pass

    def SetPEDisambiguity(self, channelString, value):
        """ SetPEDisambiguity(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPowerBoostFactor(self, channelString, value):
        """ SetPowerBoostFactor(self: niWLANG, channelString: str, value: float) -> int """
        pass

    def SetPowerLevel(self, channel, value):
        """ SetPowerLevel(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetPPDUType(self, channelString, value):
        """ SetPPDUType(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPreamblePuncturingEnabled(self, channelString, value):
        """ SetPreamblePuncturingEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPreamblePuncturingMask(self, channelString, value):
        """ SetPreamblePuncturingMask(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPreFECPaddingFactor(self, channelString, value):
        """ SetPreFECPaddingFactor(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPrimary20MHzChannelIndex(self, channelString, value):
        """ SetPrimary20MHzChannelIndex(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetPulseShapingFilterEnabled(self, channel, value):
        """ SetPulseShapingFilterEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPulseShapingFilterLength(self, channel, value):
        """ SetPulseShapingFilterLength(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetPulseShapingFilterParameter(self, channel, value):
        """ SetPulseShapingFilterParameter(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetPulseShapingFilterType(self, channel, value):
        """ SetPulseShapingFilterType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetQDcOffset(self, channel, value):
        """ SetQDcOffset(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetQuadratureSkew(self, channel, value):
        """ SetQuadratureSkew(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetRelativePower(self, channelString, value):
        """ SetRelativePower(self: niWLANG, channelString: str, value: float) -> int """
        pass

    def SetRFBlankingEnabled(self, channelString, value):
        """ SetRFBlankingEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetRUAllocation(self, channel, data, dataArraySize):
        """ SetRUAllocation(self: niWLANG, channel: str, data: Array[int], dataArraySize: int) -> int """
        pass

    def SetRUAllocationMode(self, channelString, value):
        """ SetRUAllocationMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetRUOffset(self, channelString, value):
        """ SetRUOffset(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetRUSize(self, channelString, value):
        """ SetRUSize(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetSampleClockOffset(self, channel, value):
        """ SetSampleClockOffset(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetSampleClockRateFactor(self, channel, value):
        """ SetSampleClockRateFactor(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetScalarAttributeF64(self, channelString, attributeID, attributeValue):
        """ SetScalarAttributeF64(self: niWLANG, channelString: str, attributeID: niWLANGProperties, attributeValue: float) -> int """
        pass

    def SetScalarAttributeI32(self, channelString, attributeID, attributeValue):
        """ SetScalarAttributeI32(self: niWLANG, channelString: str, attributeID: niWLANGProperties, attributeValue: int) -> int """
        pass

    def SetScalarAttributeI64(self, channelString, attributeID, attributeValue):
        """
        SetScalarAttributeI64(self: niWLANG, channelString: str, attributeID: niWLANGProperties, attributeValue: int) -> int
        SetScalarAttributeI64(self: niWLANG, channelString: str, attributeID: niWLANGProperties, attributeValue: Int64) -> int
        """
        pass

    def SetSpaceTimeStreamOffset(self, channelString, value):
        """ SetSpaceTimeStreamOffset(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetSpatialMappingMode(self, channelString, value):
        """ SetSpatialMappingMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetSTAID(self, channelString, value):
        """ SetSTAID(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetStandard(self, channel, value):
        """ SetStandard(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetStbcAllStreamsEnabled(self, channel, value):
        """ SetStbcAllStreamsEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetStbcIndex(self, channel, value):
        """ SetStbcIndex(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetSTBCIndex(self, channelString, sTBCIndex):
        """ SetSTBCIndex(self: niWLANG, channelString: str, sTBCIndex: int) -> int """
        pass

    def SetSubcarrierMask(self, channel, value):
        """ SetSubcarrierMask(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetSwapIAndQEnabled(self, channel, value):
        """ SetSwapIAndQEnabled(self: niWLANG, channel: str, value: int) -> int """
        pass

    def SetTargetRSSI(self, channelString, value):
        """ SetTargetRSSI(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetTimeDelay(self, channelString, value):
        """ SetTimeDelay(self: niWLANG, channelString: str, value: float) -> int """
        pass

    def SetTimingSkew(self, channel, value):
        """ SetTimingSkew(self: niWLANG, channel: str, value: float) -> int """
        pass

    def SetTransmissionMode(self, channelString, value):
        """ SetTransmissionMode(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetTriggerFrameAID12(self, channelString, value):
        """ SetTriggerFrameAID12(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetTriggerFrameCSRequired(self, channelString, value):
        """ SetTriggerFrameCSRequired(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetTriggerFrameMaximumMacPaddingDuration(self, channelString, value):
        """ SetTriggerFrameMaximumMacPaddingDuration(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetUserEnabled(self, channelString, value):
        """ SetUserEnabled(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetVectorAttributeF64(self, channelString, attributeID, data, dataArraySize):
        """ SetVectorAttributeF64(self: niWLANG, channelString: str, attributeID: niWLANGProperties, data: Array[float], dataArraySize: int) -> int """
        pass

    def SetVectorAttributeI32(self, channelString, attributeID, data, dataArraySize):
        """ SetVectorAttributeI32(self: niWLANG, channelString: str, attributeID: niWLANGProperties, data: Array[int], dataArraySize: int) -> int """
        pass

    def SetWindowingMethod(self, channelString, value):
        """ SetWindowingMethod(self: niWLANG, channelString: str, value: int) -> int """
        pass

    def SetWindowLength(self, channel, value):
        """ SetWindowLength(self: niWLANG, channel: str, value: float) -> int """
        pass

    def Set_80211ahPreambleType(self, channel, value):
        """ Set_80211ahPreambleType(self: niWLANG, channel: str, value: int) -> int """
        pass

    def Set_80211ahUplinkIndication(self, channel, value):
        """ Set_80211ahUplinkIndication(self: niWLANG, channel: str, value: int) -> int """
        pass

    def Set_80211nPlcpFrameFormat(self, channel, value):
        """ Set_80211nPlcpFrameFormat(self: niWLANG, channel: str, value: int) -> int """
        pass

    @staticmethod
    def WLANG_RFSGClearDatabase(rFSGSession, channelString, waveformName):
        """ WLANG_RFSGClearDatabase(rFSGSession: HandleRef, channelString: str, waveformName: str) -> int """
        pass

    @staticmethod
    def WLANG_RFSGConfigurePowerLevel(rFSGSession, channelString, script, powerLevel):
        """ WLANG_RFSGConfigurePowerLevel(rFSGSession: HandleRef, channelString: str, script: str, powerLevel: float) -> int """
        pass

    @staticmethod
    def WLANG_RFSGConfigureScript(rFSGSession, channelString, script, powerLevel):
        """ WLANG_RFSGConfigureScript(rFSGSession: HandleRef, channelString: str, script: str, powerLevel: float) -> int """
        pass

    @staticmethod
    def WLANG_RFSGReadAndDownloadWaveformsFromFile(rfsgSessions, numberOfChannels, waveformName, filePath):
        """ WLANG_RFSGReadAndDownloadWaveformsFromFile(rfsgSessions: Array[HandleRef], numberOfChannels: int, waveformName: str, filePath: str) -> int """
        pass

    @staticmethod
    def WLANG_RFSGRetrieveIQRate(rFSGSession, channelString, waveformName, iQRate):
        """ WLANG_RFSGRetrieveIQRate(rFSGSession: HandleRef, channelString: str, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def WLANG_RFSGRetrieveIQRateAllWaveforms(rFSGSession, channelString, script, iQRate):
        """ WLANG_RFSGRetrieveIQRateAllWaveforms(rFSGSession: HandleRef, channelString: str, script: str) -> (int, float) """
        pass

    @staticmethod
    def WLANG_RFSGRetrieveMinimumPAPRAllWaveforms(rFSGSession, channelString, script, pAPR):
        """ WLANG_RFSGRetrieveMinimumPAPRAllWaveforms(rFSGSession: HandleRef, channelString: str, script: str) -> (int, float) """
        pass

    @staticmethod
    def WLANG_RFSGRetrievePAPR(rFSGSession, channelString, waveformName, pAPR):
        """ WLANG_RFSGRetrievePAPR(rFSGSession: HandleRef, channelString: str, waveformName: str) -> (int, float) """
        pass

    @staticmethod
    def WLANG_RFSGStoreIQRate(rFSGSession, channelString, waveformName, iQRate):
        """ WLANG_RFSGStoreIQRate(rFSGSession: HandleRef, channelString: str, waveformName: str, iQRate: float) -> int """
        pass

    @staticmethod
    def WLANG_RFSGStorePAPR(rFSGSession, channelString, waveformName, pAPR):
        """ WLANG_RFSGStorePAPR(rFSGSession: HandleRef, channelString: str, waveformName: str, pAPR: float) -> int """
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
        __new__(cls: type, toolkitCompatibilityVersion: int)
        __new__(cls: type, sessionName: str, toolkitCompatibilityVersion: int) -> int
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: niWLANG) -> HandleRef

"""



class niWLANGConstants(object):
    """ niWLANGConstants() """
    AutoPayloadDataLengthModeDisabled = 0
    AutoPayloadDataLengthModeFrameDuration = 2
    AutoPayloadDataLengthModeLSIGLength = 1
    CompatibilityVersion010000 = 10000
    CompatibilityVersion020000 = 20000
    CompatibilityVersion030000 = 30000
    CompatibilityVersion040000 = 40000
    CompatibilityVersion050000 = 50000
    DsssDataRate1 = 0
    DsssDataRate11Cck = 4
    DsssDataRate11Pbcc = 5
    DsssDataRate2 = 1
    DsssDataRate22 = 6
    DsssDataRate33 = 7
    DsssDataRate5p5Cck = 2
    DsssDataRate5p5Pbcc = 3
    False = 0
    FecCodingTypeBcc = 0
    FecCodingTypeLdpc = 1
    FileOperationModeCreate = 3
    FileOperationModeCreateOrReplace = 2
    FileOperationModeOpen = 0
    FileOperationModeOpenOrCreate = 1
    FilterGaussian = 3
    FilterRaisedCosine = 1
    FilterRectangular = 0
    FilterRootRaisedCosine = 2
    FrequencyBand2ghz = 0
    FrequencyBand2p4ghz = 0
    FrequencyBand5ghz = 1
    GuardIntervalTypeOneByEight = 1
    GuardIntervalTypeOneByFour = 0
    GuardIntervalTypeOneBySixteen = 2
    HeLtfSize4X = 0
    HeLtfSizeAuto = -1
    HeLtfSizeAuto1X = 2
    HeLtfSizeAuto2X = 1
    IdleIntervalModePostBurst = 1
    IdleIntervalModeSplit = 0
    LOFrequencyOffsetModeAuto = 0
    LOFrequencyOffsetModeDisabled = 2
    LOFrequencyOffsetModeUserDefined = 1
    LongPreambleType80211ah = 1
    LOSourceExternal = 0
    LOSourceOnboard = 2
    LOSourceSgSaShared = 3
    MacFrameFormatLong = 0
    MacFrameFormatShort = 1
    MappingMatrixTypeDirect = 0
    MappingMatrixTypeFourier = 2
    MappingMatrixTypeHadamard = 1
    MappingMatrixTypeUserDefined = 3
    MaximumPaddingDuration0us = 0
    MaximumPaddingDuration16us = 2
    MaximumPaddingDuration8us = 1
    MidamblePeriodicity10Symbols = 1
    MidamblePeriodicity20Symbols = 2
    MidamblePeriodicityNone = 0
    MultipleGenerators = 1
    NonHtModulationModeOff = 0
    NonHtModulationModeOn = 1
    OfdmDataRate12 = 2
    OfdmDataRate18 = 3
    OfdmDataRate24 = 4
    OfdmDataRate36 = 5
    OfdmDataRate48 = 6
    OfdmDataRate54 = 7
    OfdmDataRate6 = 0
    OfdmDataRate9 = 1
    OfdmGuardIntervalTypeLong = 0
    OfdmGuardIntervalTypeShort = 1
    PayloadFrameTypeDataFrame = 0
    PayloadFrameTypeTriggerFrame = 1
    PnSequence = 1
    PowerReferenceNonBoostedFields = 0
    PowerReferencePowerBoostedFields = 1
    PowerReferencePowerReferenceEntirePacket = 2
    PpduTypeExtendedRangeSuPpdu = 2
    PpduTypeMuPpdu = 1
    PpduTypeSuPpdu = 0
    PpduTypeTriggerBasedPpdu = 3
    PreambleTypeLongPreamble = 1
    PreambleTypeShortPreamble = 0
    RUAllocationModeGroup = 1
    RUAllocationModeIndividual = 0
    RuSize106 = 106
    RuSize242 = 242
    RuSize26 = 26
    RuSize2x996 = 1992
    RuSize484 = 484
    RuSize52 = 52
    RuSize996 = 996
    ShortPreambleType80211ah = 0
    SingleGenerator = 0
    SpatialMappingModeCommon = 0
    SpatialMappingModeUserSpecific = 1
    Standard80211AcMimoOfdm = 4
    Standard80211AfMimoOfdm = 6
    Standard80211agjpOfdm = 0
    Standard80211agOfdm = 0
    Standard80211AhMimoOfdm = 5
    Standard80211AxMimoOfdm = 9
    Standard80211bgDsss = 1
    Standard80211gDsssOfdm = 2
    Standard80211jOfdm = 7
    Standard80211nMimoOfdm = 3
    Standard80211pOfdm = 8
    TransmissionModeDownlinl = 0
    TransmissionModeUplink = 1
    True = 1
    TvhtMode1 = 0
    TvhtMode2c = 1
    TvhtMode2n = 2
    TvhtMode4c = 3
    TvhtMode4n = 4
    UserDefined = 0
    WinMethodCenteredAtSymbolBoundary = 0
    WinMethodStartingAtSymbolBoundary = 1
    _80211nPlcpFrameFormatGreenfield = 1
    _80211nPlcpFrameFormatMixed = 0


class niWLANGProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum niWLANGProperties, values: _80211ahPreambleType (119), _80211ahUplinkIndication (124), _80211nPlcpFrameFormat (43), ActualHeadroom (88), ActualOfdmDataRate (89), AllIqImpairmentsEnabled (96), AmpduEnabled (103), AutoHeadroomEnabled (87), AutoPayloadDataLengthMode (179), AveragePowerReference (170), AwgnEnabled (97), BSSColor (184), BurstStartLocation (174), BurstStopLocation (175), CarrierFrequency (0), CarrierFrequencyOffset (20), CarrierToNoiseRatio (98), ChannelBandwidth (42), CompatibilityVersion (56), DsssDataRate (33), DsssPreambleType (4), DsssWindowLength (29), DualCarrierModulationEnabled (154), FecCodingType (70), FrameDuration (209), FullscaleBackOff (168), GuardInterval (44), GuardIntervalType (123), HeaderEncoderEnabled (14), HeaderInterleaverEnabled (15), Headroom (40), HeLtfSize (144), HeSigBDualCarrierModulationEnabled (162), HeSigBMcsIndex (161), IDcOffset (22), IdleInterval (3), IdleIntervalMode (199), IqGainImbalance (21), IqRate (35), IqWaveformSize (37), LdpcExtraSymbolSegment (183), LockedClockBitEnabled (13), LOFrequencyOffset (177), LOFrequencyOffsetMode (176), LoSharingEnabled (118), LSIGLength (180), MacAddress1 (60), MacAddress1Enabled (59), MacAddress1Length (121), MacAddress2 (62), MacAddress2Enabled (61), MacAddress2Length (121), MacAddress3 (64), MacAddress3Enabled (63), MacAddress4 (68), MacAddress4Enabled (67), MacDurationOrId (58), MacFcsEnabled (100), MacFragmentNumberIncrementEnabled (82), MacFrameControl (57), MacFrameFormat (120), MacHeaderEnabled (11), MacHtControl (73), MacHtControlEnabled (72), MacQosControl (71), MacQosControlEnabled (53), MacSequenceControl (66), MacSequenceControlEnabled (65), MacSequenceNumberIncrementEnabled (80), MacSequenceNumberIncrementInterval (81), MappingMatrixType (55), MaxExpectedPapr (40), MaximumHardwareIqRate (102), McsIndex (41), MidamblePeriodicity (204), MpduLength (83), MultiSegmentGenerationMode (134), MuMimoLtfModeEnabled (186), NominalPacketPadding (195), NonHtModulationMode (127), NotSoundingBit (86), NumberOfDataSymbols (94), NumberOfExtensionSpatialStreams (46), NumberOfFrames (6), NumberOfHeLtfSymbols (165), NumberOfSegments (75), NumberOfSpaceTimeStreams (76), NumberOfTransmitChannels (47), NumberOfUsers (115), OfdmDataRate (32), OfdmLegacyScalingEnabled (101), OfdmWindowLength (125), OversamplingFactor (2), PacketExtensionDuration (159), PayloadAutoDataLength (179), PayloadAutoNumberOfMPDUs (178), PayloadDataLength (5), PayloadDataType (7), PayloadEncoderEnabled (18), PayloadInterleaverEnabled (19), PayloadMacFrameType (188), PayloadNumberOfMpdus (104), PayloadPnOrder (8), PayloadPnSeed (9), PayloadScramblerEnabled (16), PayloadScramblerSeed (17), PayloadUserDefinedBits (10), PEDisambiguity (182), PowerBoostFactor (164), PowerLevel (1), PpduType (95), PreamblePuncturingEnabled (191), PreamblePuncturingMask (193), PreFECPaddingFactor (181), Primary20MHzChannelIndex (192), PulseShapingFilterEnabled (54), PulseShapingFilterLength (112), PulseShapingFilterParameter (27), PulseShapingFilterType (26), QDcOffset (23), QuadratureSkew (24), RelativePower (136), RfBlankingEnabled (90), RfBlankingMarkerPositions (91), RUAllocation (206), RUAllocationMode (205), RuOffset (133), RuSize (132), SampleClockOffset (25), SampleClockRateFactor (107), SignalBandwidth (194), SpaceTimeStreamOffset (187), SpatialMappingMode (185), StaId (163), Standard (31), StbcAllStreamsEnabled (77), StbcIndex (49), SubcarrierMask (12), SwapIAndQEnabled (78), TimeDelay (135), TimingSkew (79), TransmissionMode (124), TriggerFrameAID12 (196), TriggerFrameApTxPower (172), TriggerFrameCSRequired (190), TriggerFrameMaximumMacPaddingDuration (189), TriggerFrameTargetRssi (173), UserEnabled (207), WindowingMethod (74), WindowLength (29) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActualHeadroom = None
    ActualOfdmDataRate = None
    AllIqImpairmentsEnabled = None
    AmpduEnabled = None
    AutoHeadroomEnabled = None
    AutoPayloadDataLengthMode = None
    AveragePowerReference = None
    AwgnEnabled = None
    BSSColor = None
    BurstStartLocation = None
    BurstStopLocation = None
    CarrierFrequency = None
    CarrierFrequencyOffset = None
    CarrierToNoiseRatio = None
    ChannelBandwidth = None
    CompatibilityVersion = None
    DsssDataRate = None
    DsssPreambleType = None
    DsssWindowLength = None
    DualCarrierModulationEnabled = None
    FecCodingType = None
    FrameDuration = None
    FullscaleBackOff = None
    GuardInterval = None
    GuardIntervalType = None
    HeaderEncoderEnabled = None
    HeaderInterleaverEnabled = None
    Headroom = None
    HeLtfSize = None
    HeSigBDualCarrierModulationEnabled = None
    HeSigBMcsIndex = None
    IDcOffset = None
    IdleInterval = None
    IdleIntervalMode = None
    IqGainImbalance = None
    IqRate = None
    IqWaveformSize = None
    LdpcExtraSymbolSegment = None
    LockedClockBitEnabled = None
    LOFrequencyOffset = None
    LOFrequencyOffsetMode = None
    LoSharingEnabled = None
    LSIGLength = None
    MacAddress1 = None
    MacAddress1Enabled = None
    MacAddress1Length = None
    MacAddress2 = None
    MacAddress2Enabled = None
    MacAddress2Length = None
    MacAddress3 = None
    MacAddress3Enabled = None
    MacAddress4 = None
    MacAddress4Enabled = None
    MacDurationOrId = None
    MacFcsEnabled = None
    MacFragmentNumberIncrementEnabled = None
    MacFrameControl = None
    MacFrameFormat = None
    MacHeaderEnabled = None
    MacHtControl = None
    MacHtControlEnabled = None
    MacQosControl = None
    MacQosControlEnabled = None
    MacSequenceControl = None
    MacSequenceControlEnabled = None
    MacSequenceNumberIncrementEnabled = None
    MacSequenceNumberIncrementInterval = None
    MappingMatrixType = None
    MaxExpectedPapr = None
    MaximumHardwareIqRate = None
    McsIndex = None
    MidamblePeriodicity = None
    MpduLength = None
    MultiSegmentGenerationMode = None
    MuMimoLtfModeEnabled = None
    NominalPacketPadding = None
    NonHtModulationMode = None
    NotSoundingBit = None
    NumberOfDataSymbols = None
    NumberOfExtensionSpatialStreams = None
    NumberOfFrames = None
    NumberOfHeLtfSymbols = None
    NumberOfSegments = None
    NumberOfSpaceTimeStreams = None
    NumberOfTransmitChannels = None
    NumberOfUsers = None
    OfdmDataRate = None
    OfdmLegacyScalingEnabled = None
    OfdmWindowLength = None
    OversamplingFactor = None
    PacketExtensionDuration = None
    PayloadAutoDataLength = None
    PayloadAutoNumberOfMPDUs = None
    PayloadDataLength = None
    PayloadDataType = None
    PayloadEncoderEnabled = None
    PayloadInterleaverEnabled = None
    PayloadMacFrameType = None
    PayloadNumberOfMpdus = None
    PayloadPnOrder = None
    PayloadPnSeed = None
    PayloadScramblerEnabled = None
    PayloadScramblerSeed = None
    PayloadUserDefinedBits = None
    PEDisambiguity = None
    PowerBoostFactor = None
    PowerLevel = None
    PpduType = None
    PreamblePuncturingEnabled = None
    PreamblePuncturingMask = None
    PreFECPaddingFactor = None
    Primary20MHzChannelIndex = None
    PulseShapingFilterEnabled = None
    PulseShapingFilterLength = None
    PulseShapingFilterParameter = None
    PulseShapingFilterType = None
    QDcOffset = None
    QuadratureSkew = None
    RelativePower = None
    RfBlankingEnabled = None
    RfBlankingMarkerPositions = None
    RUAllocation = None
    RUAllocationMode = None
    RuOffset = None
    RuSize = None
    SampleClockOffset = None
    SampleClockRateFactor = None
    SignalBandwidth = None
    SpaceTimeStreamOffset = None
    SpatialMappingMode = None
    StaId = None
    Standard = None
    StbcAllStreamsEnabled = None
    StbcIndex = None
    SubcarrierMask = None
    SwapIAndQEnabled = None
    TimeDelay = None
    TimingSkew = None
    TransmissionMode = None
    TriggerFrameAID12 = None
    TriggerFrameApTxPower = None
    TriggerFrameCSRequired = None
    TriggerFrameMaximumMacPaddingDuration = None
    TriggerFrameTargetRssi = None
    UserEnabled = None
    value__ = None
    WindowingMethod = None
    WindowLength = None
    _80211ahPreambleType = None
    _80211ahUplinkIndication = None
    _80211nPlcpFrameFormat = None


