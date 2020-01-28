# encoding: utf-8
# module NationalInstruments.ModularInstruments.NIRfsa calls itself NIRfsa
# from NationalInstruments.ModularInstruments.NIRfsa.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class MechanicalAttenuatorEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum MechanicalAttenuatorEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class NIRfsa(object, IDisposable, IServiceProvider, IIviDriver, ITClockSynchronizableDevice):
    """
    NIRfsa(resourceName: str, idQuery: bool, resetDevice: bool)
    NIRfsa(resourceName: str, idQuery: bool, resetDevice: bool, optionString: str)
    NIRfsa(instrumentHandle: IntPtr)
    """
    def Close(self):
        """ Close(self: NIRfsa) """
        pass

    def DangerousGetInstrumentHandle(self):
        """ DangerousGetInstrumentHandle(self: NIRfsa) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: NIRfsa) """
        pass

    def GetInstrumentHandle(self):
        """ GetInstrumentHandle(self: NIRfsa) -> SafeHandle """
        pass

    def GetService(self, serviceType):
        """ GetService(self: NIRfsa, serviceType: Type) -> object """
        pass

    @staticmethod
    def VstSelfCalibrate(resourceName):
        """ VstSelfCalibrate(resourceName: str) -> int """
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
        __new__(cls: type, resourceName: str, idQuery: bool, resetDevice: bool)
        __new__(cls: type, resourceName: str, idQuery: bool, resetDevice: bool, optionString: str)
        __new__(cls: type, instrumentHandle: IntPtr)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Acquisition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Acquisition(self: NIRfsa) -> RfsaAcquisition

"""

    Calibration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Calibration(self: NIRfsa) -> RfsaCalibration

"""

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: NIRfsa) -> RfsaConfiguration

"""

    DeviceCharacteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceCharacteristics(self: NIRfsa) -> RfsaDeviceCharacteristics

"""

    DriverIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverIdentity(self: NIRfsa) -> RfsaDriverIdentity

"""

    DriverOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverOperation(self: NIRfsa) -> RfsaDriverOperation

"""

    DriverUtility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverUtility(self: NIRfsa) -> RfsaDriverUtility

"""

    ErrorInfoUtility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorInfoUtility(self: NIRfsa) -> RfsaErrorInfoUtility

"""

    Identity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identity(self: NIRfsa) -> RfsaDriverIdentity

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: NIRfsa) -> bool

"""

    Utility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Utility(self: NIRfsa) -> RfsaDriverUtility

"""



class RfsaSubObject(object):
    # no doc

class RfsaAcquisition(RfsaSubObject):
    # no doc
    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaAcquisition) -> RfsaAdvancedAcquisition

"""

    IQ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQ(self: RfsaAcquisition) -> RfsaIQAcquisition

"""

    Spectrum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spectrum(self: RfsaAcquisition) -> RfsaSpectrumAcquisition

"""



class RfsaAcquisitionStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaAcquisitionStatus, values: Completed (1), InProgress (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Completed = None
    InProgress = None
    value__ = None


class RfsaAcquisitionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaAcquisitionType, values: IQ (100), Spectrum (101) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Spectrum = None
    value__ = None


class RfsaAdvancedAcquisition(RfsaSubObject):
    # no doc
    AllowOutOfSpecificationUserSettingsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowOutOfSpecificationUserSettingsEnabled(self: RfsaAdvancedAcquisition) -> RfsaAllowOutOfSpecificationUserSettingsEnabled

Set: AllowOutOfSpecificationUserSettingsEnabled(self: RfsaAdvancedAcquisition) = value
"""

    DataTransferBlockSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTransferBlockSize(self: RfsaAdvancedAcquisition) -> int

Set: DataTransferBlockSize(self: RfsaAdvancedAcquisition) = value
"""

    DataTransferMaximumBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTransferMaximumBandwidth(self: RfsaAdvancedAcquisition) -> float

Set: DataTransferMaximumBandwidth(self: RfsaAdvancedAcquisition) = value
"""

    DecimationDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecimationDelay(self: RfsaAdvancedAcquisition) -> float

Set: DecimationDelay(self: RfsaAdvancedAcquisition) = value
"""

    DeviceInstantaneousBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceInstantaneousBandwidth(self: RfsaAdvancedAcquisition) -> float

Set: DeviceInstantaneousBandwidth(self: RfsaAdvancedAcquisition) = value
"""

    DownconverterCenterFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterCenterFrequency(self: RfsaAdvancedAcquisition) -> float

Set: DownconverterCenterFrequency(self: RfsaAdvancedAcquisition) = value
"""

    DownconverterFrequencyOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterFrequencyOffset(self: RfsaAdvancedAcquisition) -> float

Set: DownconverterFrequencyOffset(self: RfsaAdvancedAcquisition) = value
"""

    DownconverterFrequencyOffsetMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterFrequencyOffsetMode(self: RfsaAdvancedAcquisition) -> RfsaDownconverterFrequencyOffsetMode

Set: DownconverterFrequencyOffsetMode(self: RfsaAdvancedAcquisition) = value
"""

    IFOutputFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFOutputFrequency(self: RfsaAdvancedAcquisition) -> float

"""



class RfsaAdvancedConfigurationList(RfsaSubObject):
    # no doc
    MinimumReconfigurationTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumReconfigurationTime(self: RfsaAdvancedConfigurationList) -> float

Set: MinimumReconfigurationTime(self: RfsaAdvancedConfigurationList) = value
"""

    TimerStartSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimerStartSource(self: RfsaAdvancedConfigurationList) -> RfsaTimerStartSource

Set: TimerStartSource(self: RfsaAdvancedConfigurationList) = value
"""



class RfsaAdvancedIQAcquisitionConfiguration(RfsaSubObject):
    # no doc
    ContiguousMultiRecordEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContiguousMultiRecordEnabled(self: RfsaAdvancedIQAcquisitionConfiguration) -> RfsaContiguousMultiRecordEnabled

Set: ContiguousMultiRecordEnabled(self: RfsaAdvancedIQAcquisitionConfiguration) = value
"""



class RfsaAdvancedReferenceTrigger(RfsaSubObject):
    # no doc
    OspDelayEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OspDelayEnabled(self: RfsaAdvancedReferenceTrigger) -> RfsaOspDelayEnabled

Set: OspDelayEnabled(self: RfsaAdvancedReferenceTrigger) = value
"""

    ReferenceToReferenceTriggerHoldOff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceToReferenceTriggerHoldOff(self: RfsaAdvancedReferenceTrigger) -> float

Set: ReferenceToReferenceTriggerHoldOff(self: RfsaAdvancedReferenceTrigger) = value
"""

    StartToReferenceTriggerHoldOff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartToReferenceTriggerHoldOff(self: RfsaAdvancedReferenceTrigger) -> float

Set: StartToReferenceTriggerHoldOff(self: RfsaAdvancedReferenceTrigger) = value
"""

    TriggerDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TriggerDelay(self: RfsaAdvancedReferenceTrigger) -> float

Set: TriggerDelay(self: RfsaAdvancedReferenceTrigger) = value
"""



class RfsaAdvancedSignalPath(RfsaSubObject):
    # no doc
    AbsoluteDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsoluteDelay(self: RfsaAdvancedSignalPath) -> float

Set: AbsoluteDelay(self: RfsaAdvancedSignalPath) = value
"""

    DownconverterLoopBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterLoopBandwidth(self: RfsaAdvancedSignalPath) -> RfsaDownconverterLoopBandwidth

Set: DownconverterLoopBandwidth(self: RfsaAdvancedSignalPath) = value
"""

    DownconverterPreselectorEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterPreselectorEnabled(self: RfsaAdvancedSignalPath) -> RfsaDownconverterPreselectorEnabled

Set: DownconverterPreselectorEnabled(self: RfsaAdvancedSignalPath) = value
"""

    FrequencySettlingTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencySettlingTime(self: RfsaAdvancedSignalPath) -> float

Set: FrequencySettlingTime(self: RfsaAdvancedSignalPath) = value
"""

    FrequencySettlingUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencySettlingUnits(self: RfsaAdvancedSignalPath) -> RfsaFrequencySettlingUnits

Set: FrequencySettlingUnits(self: RfsaAdvancedSignalPath) = value
"""

    IFConditioningDownconversionEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFConditioningDownconversionEnabled(self: RfsaAdvancedSignalPath) -> RfsaIFConditioningDownconversionEnabled

Set: IFConditioningDownconversionEnabled(self: RfsaAdvancedSignalPath) = value
"""

    InputIsolationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputIsolationEnabled(self: RfsaAdvancedSignalPath) -> RfsaInputIsolationEnabled

Set: InputIsolationEnabled(self: RfsaAdvancedSignalPath) = value
"""

    InputPort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputPort(self: RfsaAdvancedSignalPath) -> RfsaInputPort

Set: InputPort(self: RfsaAdvancedSignalPath) = value
"""

    LOFrequencyStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequencyStepSize(self: RfsaAdvancedSignalPath) -> float

Set: LOFrequencyStepSize(self: RfsaAdvancedSignalPath) = value
"""

    LOInjectionSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInjectionSide(self: RfsaAdvancedSignalPath) -> RfsaLOInjectionSide

Set: LOInjectionSide(self: RfsaAdvancedSignalPath) = value
"""

    LOInPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInPower(self: RfsaAdvancedSignalPath) -> float

"""

    LOOutPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutPower(self: RfsaAdvancedSignalPath) -> float

Set: LOOutPower(self: RfsaAdvancedSignalPath) = value
"""

    LOPllFractionalModeEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOPllFractionalModeEnabled(self: RfsaAdvancedSignalPath) -> RfsaLOPllFractionalModeEnabled

Set: LOPllFractionalModeEnabled(self: RfsaAdvancedSignalPath) = value
"""

    LowFrequencyBypassEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowFrequencyBypassEnabled(self: RfsaAdvancedSignalPath) -> RfsaLowFrequencyBypassEnabled

Set: LowFrequencyBypassEnabled(self: RfsaAdvancedSignalPath) = value
"""

    NotchFilterEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NotchFilterEnabled(self: RfsaAdvancedSignalPath) -> RfsaNotchFilterEnabled

Set: NotchFilterEnabled(self: RfsaAdvancedSignalPath) = value
"""

    RFHighPassFiltering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFHighPassFiltering(self: RfsaAdvancedSignalPath) -> float

Set: RFHighPassFiltering(self: RfsaAdvancedSignalPath) = value
"""

    RFPreselectorFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFPreselectorFilter(self: RfsaAdvancedSignalPath) -> RfsaRFPreselectorFilter

Set: RFPreselectorFilter(self: RfsaAdvancedSignalPath) = value
"""



class RfsaAdvancedTrigger(RfsaSubObject):
    # no doc
    DdcReferenceTriggerOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DdcReferenceTriggerOverride(self: RfsaAdvancedTrigger) -> bool

Set: DdcReferenceTriggerOverride(self: RfsaAdvancedTrigger) = value
"""

    StartTriggerDelay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartTriggerDelay(self: RfsaAdvancedTrigger) -> float

Set: StartTriggerDelay(self: RfsaAdvancedTrigger) = value
"""



class RfsaAdvancedVertical(RfsaSubObject):
    # no doc
    AmplitudeSettling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AmplitudeSettling(self: RfsaAdvancedVertical) -> float

Set: AmplitudeSettling(self: RfsaAdvancedVertical) = value
"""

    DeviceConfigurationTemperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceConfigurationTemperature(self: RfsaAdvancedVertical) -> float

Set: DeviceConfigurationTemperature(self: RfsaAdvancedVertical) = value
"""

    DigitalGain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalGain(self: RfsaAdvancedVertical) -> float

Set: DigitalGain(self: RfsaAdvancedVertical) = value
"""

    ExternalGain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalGain(self: RfsaAdvancedVertical) -> float

Set: ExternalGain(self: RfsaAdvancedVertical) = value
"""

    MechanicalAttenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MechanicalAttenuation(self: RfsaAdvancedVertical) -> float

Set: MechanicalAttenuation(self: RfsaAdvancedVertical) = value
"""

    MinimumAcpr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumAcpr(self: RfsaAdvancedVertical) -> float

Set: MinimumAcpr(self: RfsaAdvancedVertical) = value
"""

    NI5663 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5663(self: RfsaAdvancedVertical) -> RfsaNI5663AdvancedVertical

"""

    NI5665 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5665(self: RfsaAdvancedVertical) -> RfsaNI5665AdvancedVertical

"""

    NI5693 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5693(self: RfsaAdvancedVertical) -> RfsaNI5693AdvancedVertical

"""

    NI5694 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5694(self: RfsaAdvancedVertical) -> RfsaNI5694AdvancedVertical

"""

    OspDataScalingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OspDataScalingFactor(self: RfsaAdvancedVertical) -> float

Set: OspDataScalingFactor(self: RfsaAdvancedVertical) = value
"""

    OverflowErrorReporting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverflowErrorReporting(self: RfsaAdvancedVertical) -> RfsaOverflowErrorReporting

Set: OverflowErrorReporting(self: RfsaAdvancedVertical) = value
"""

    ReferenceLevelHeadroom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceLevelHeadroom(self: RfsaAdvancedVertical) -> float

Set: ReferenceLevelHeadroom(self: RfsaAdvancedVertical) = value
"""

    RFAttenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFAttenuation(self: RfsaAdvancedVertical) -> float

Set: RFAttenuation(self: RfsaAdvancedVertical) = value
"""

    RFAttenuationStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFAttenuationStepSize(self: RfsaAdvancedVertical) -> float

Set: RFAttenuationStepSize(self: RfsaAdvancedVertical) = value
"""

    RFPreampEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFPreampEnabled(self: RfsaAdvancedVertical) -> RfsaRFPreamplifierEnabled

Set: RFPreampEnabled(self: RfsaAdvancedVertical) = value
"""

    ThermalCorrectionHeadroomRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalCorrectionHeadroomRange(self: RfsaAdvancedVertical) -> float

Set: ThermalCorrectionHeadroomRange(self: RfsaAdvancedVertical) = value
"""

    ThermalCorrectionTemperatureResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalCorrectionTemperatureResolution(self: RfsaAdvancedVertical) -> float

Set: ThermalCorrectionTemperatureResolution(self: RfsaAdvancedVertical) = value
"""



class RfsaAdvanceTrigger(RfsaSubObject):
    # no doc
    def Disable(self):
        """ Disable(self: RfsaAdvanceTrigger) """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RfsaAdvanceTrigger) """
        pass

    DigitalEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsaAdvanceTrigger) -> RfsaDigitalEdgeAdvanceTrigger

"""

    Export = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Export(self: RfsaAdvanceTrigger) -> RfsaExportAdvanceTrigger

"""

    Synchronization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronization(self: RfsaAdvanceTrigger) -> RfsaAdvanceTriggerSynchronization

"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaAdvanceTrigger) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RfsaAdvanceTrigger) -> RfsaAdvanceTriggerType

Set: Type(self: RfsaAdvanceTrigger) = value
"""



class RfsaAdvanceTriggerSynchronization(RfsaSubObject):
    # no doc
    DistributionLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionLine(self: RfsaAdvanceTriggerSynchronization) -> RfsaAdvanceTriggerSynchronizationDistributionLine

Set: DistributionLine(self: RfsaAdvanceTriggerSynchronization) = value
"""

    IsMaster = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMaster(self: RfsaAdvanceTriggerSynchronization) -> bool

Set: IsMaster(self: RfsaAdvanceTriggerSynchronization) = value
"""



class RfsaAdvanceTriggerSynchronizationDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaAdvanceTriggerSynchronizationDistributionLine, obj: object) -> bool
        Equals(self: RfsaAdvanceTriggerSynchronizationDistributionLine, source: RfsaAdvanceTriggerSynchronizationDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaAdvanceTriggerSynchronizationDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaAdvanceTriggerSynchronizationDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaAdvanceTriggerSynchronizationDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    PxiTrig0 = None
    PxiTrig1 = None
    PxiTrig2 = None
    PxiTrig3 = None
    PxiTrig4 = None
    PxiTrig5 = None
    PxiTrig6 = None
    PxiTrig7 = None


class RfsaAdvanceTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaAdvanceTriggerType, values: DigitalEdge (601), None (600), SoftwareEdge (604) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    None = None
    SoftwareEdge = None
    value__ = None


class RfsaAllowOutOfSpecificationUserSettingsEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaAllowOutOfSpecificationUserSettingsEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaArmReferenceTrigger(RfsaSubObject):
    # no doc
    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RfsaArmReferenceTrigger) """
        pass

    DigitalEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsaArmReferenceTrigger) -> RfsaDigitalEdgeArmReferenceTrigger

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RfsaArmReferenceTrigger) -> RfsaArmReferenceTriggerType

Set: Type(self: RfsaArmReferenceTrigger) = value
"""



class RfsaArmReferenceTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaArmReferenceTriggerType, values: DigitalEdge (601), None (600), SoftwareEdge (604) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    None = None
    SoftwareEdge = None
    value__ = None


class RfsaBasicConfigurationList(RfsaSubObject):
    # no doc
    def CreateConfigurationList(self, listName, properties, setAsActiveList):
        """ CreateConfigurationList(self: RfsaBasicConfigurationList, listName: str, properties: Array[RfsaConfigurationListProperties], setAsActiveList: bool) """
        pass

    def CreateStep(self, setAsActiveStep):
        """ CreateStep(self: RfsaBasicConfigurationList, setAsActiveStep: bool) """
        pass

    def DeleteConfigurationList(self, listName):
        """ DeleteConfigurationList(self: RfsaBasicConfigurationList, listName: str) """
        pass

    ActiveList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveList(self: RfsaBasicConfigurationList) -> str

Set: ActiveList(self: RfsaBasicConfigurationList) = value
"""

    ActiveStep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveStep(self: RfsaBasicConfigurationList) -> Int64

Set: ActiveStep(self: RfsaBasicConfigurationList) = value
"""

    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaBasicConfigurationList) -> RfsaAdvancedConfigurationList

"""

    StepInProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StepInProgress(self: RfsaBasicConfigurationList) -> Int64

"""

    TimerEventInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimerEventInterval(self: RfsaBasicConfigurationList) -> float

Set: TimerEventInterval(self: RfsaBasicConfigurationList) = value
"""



class RfsaCalibration(RfsaSubObject):
    # no doc
    External = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: External(self: RfsaCalibration) -> RfsaExternalCalibration

"""

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Self(self: RfsaCalibration) -> RfsaSelfCalibration

"""



class RfsaChannelBasedDeembedding(RfsaSubObject):
    # no doc
    def ConfigureDeembeddingTableInterpolationLinear(self, tableName, format):
        """ ConfigureDeembeddingTableInterpolationLinear(self: RfsaChannelBasedDeembedding, tableName: str, format: RfsaLinearInterpolationFormat) """
        pass

    def ConfigureDeembeddingTableInterpolationNearest(self, tableName):
        """ ConfigureDeembeddingTableInterpolationNearest(self: RfsaChannelBasedDeembedding, tableName: str) """
        pass

    def ConfigureDeembeddingTableInterpolationSpline(self, tableName):
        """ ConfigureDeembeddingTableInterpolationSpline(self: RfsaChannelBasedDeembedding, tableName: str) """
        pass

    def CreateDeembeddingSParameterTableArray(self, tableName, frequencies, sParameterTable, sParameterOrientation):
        """ CreateDeembeddingSParameterTableArray(self: RfsaChannelBasedDeembedding, tableName: str, frequencies: Array[float], sParameterTable: Array[ComplexDouble], sParameterOrientation: RfsaSParameterOrientation) """
        pass

    def CreateDeembeddingSParameterTableS2pFile(self, tableName, s2pFilePath, sParameterOrientation):
        """ CreateDeembeddingSParameterTableS2pFile(self: RfsaChannelBasedDeembedding, tableName: str, s2pFilePath: str, sParameterOrientation: RfsaSParameterOrientation) """
        pass

    def DeleteDeembeddingTable(self, tableName):
        """ DeleteDeembeddingTable(self: RfsaChannelBasedDeembedding, tableName: str) """
        pass

    DeembeddingSelectedTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingSelectedTable(self: RfsaChannelBasedDeembedding) -> str

Set: DeembeddingSelectedTable(self: RfsaChannelBasedDeembedding) = value
"""

    DeembeddingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingType(self: RfsaChannelBasedDeembedding) -> RfsaDeembeddingType

Set: DeembeddingType(self: RfsaChannelBasedDeembedding) = value
"""



class RfsaChannelBasedDeviceCharacteristics(RfsaSubObject):
    # no doc
    def GetDeviceTemperature(self):
        """ GetDeviceTemperature(self: RfsaChannelBasedDeviceCharacteristics) -> float """
        pass


class RfsaChannelBasedLO(RfsaSubObject):
    # no doc
    DownconverterLoopBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterLoopBandwidth(self: RfsaChannelBasedLO) -> RfsaDownconverterLoopBandwidth

Set: DownconverterLoopBandwidth(self: RfsaChannelBasedLO) = value
"""

    LOExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOExportEnabled(self: RfsaChannelBasedLO) -> bool

Set: LOExportEnabled(self: RfsaChannelBasedLO) = value
"""

    LOFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequency(self: RfsaChannelBasedLO) -> float

Set: LOFrequency(self: RfsaChannelBasedLO) = value
"""

    LOInPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInPower(self: RfsaChannelBasedLO) -> float

Set: LOInPower(self: RfsaChannelBasedLO) = value
"""

    LOOutPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutPower(self: RfsaChannelBasedLO) -> float

Set: LOOutPower(self: RfsaChannelBasedLO) = value
"""

    LOPllFractionalModeEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOPllFractionalModeEnabled(self: RfsaChannelBasedLO) -> RfsaLOPllFractionalModeEnabled

Set: LOPllFractionalModeEnabled(self: RfsaChannelBasedLO) = value
"""

    LOSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOSource(self: RfsaChannelBasedLO) -> RfsaLOSource

Set: LOSource(self: RfsaChannelBasedLO) = value
"""



class RfsaChannelCoupling(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaChannelCoupling, values: AC (3001), DC (3002) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AC = None
    DC = None
    value__ = None


class RfsaCoefficientInfo(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaCoefficientInfo, obj: object) -> bool
        Equals(self: RfsaCoefficientInfo, coefficientInfo: RfsaCoefficientInfo) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaCoefficientInfo) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gain(self: RfsaCoefficientInfo) -> float

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: RfsaCoefficientInfo) -> float

"""

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved1(self: RfsaCoefficientInfo) -> float

"""

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved2(self: RfsaCoefficientInfo) -> float

"""



class RfsaConfiguration(RfsaSubObject):
    # no doc
    AcquisitionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcquisitionType(self: RfsaConfiguration) -> RfsaAcquisitionType

Set: AcquisitionType(self: RfsaConfiguration) = value
"""

    BasicConfigurationList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasicConfigurationList(self: RfsaConfiguration) -> RfsaBasicConfigurationList

"""

    CalibrationDigitizerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationDigitizerId(self: RfsaConfiguration) -> str

"""

    Deembedding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Deembedding(self: RfsaConfiguration) -> RfsaDeembedding

"""

    DigitizerSampleClock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitizerSampleClock(self: RfsaConfiguration) -> RfsaDigitizerSampleClock

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Events(self: RfsaConfiguration) -> RfsaEvents

"""

    IQ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQ(self: RfsaConfiguration) -> RfsaIQAcquisitionConfiguration

"""

    IQInPortChannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQInPortChannels(self: RfsaConfiguration) -> RfsaIQInPortChannelCollection

"""

    NoiseSourcePowerEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NoiseSourcePowerEnabled(self: RfsaConfiguration) -> RfsaNoiseSourcePowerEnabled

Set: NoiseSourcePowerEnabled(self: RfsaConfiguration) = value
"""

    ReferenceClock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceClock(self: RfsaConfiguration) -> RfsaReferenceClock

"""

    SignalPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalPath(self: RfsaConfiguration) -> RfsaSignalPath

"""

    Spectrum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spectrum(self: RfsaConfiguration) -> RfsaSpectrumAcquisitionConfiguration

"""

    Triggers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triggers(self: RfsaConfiguration) -> RfsaTriggers

"""

    Vertical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertical(self: RfsaConfiguration) -> RfsaVertical

"""



class RfsaConfigurationListProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaConfigurationListProperties, values: Attenuation (1150005), ChannelCoupling (1150149), DdcReferenceTriggerOverride (1150164), DeviceInstantaneousBandwidth (1150125), DownconverterCenterFrequency (1150082), DownConverterCenterFrequency (1150082), DownconverterFrequencyOffset (1150203), DownconverterPreselectorEnabled (1150132), ExternalGain (1150094), FrequencySettlingTime (1150088), IFFilterBandwidth (1150205), IFOutputPowerLevel (1150130), IFOutputPowerLevelOffset (1150131), IQCarrierFrequency (1150059), IqInPortCarrierFrequency (1150181), IqInPortVerticalRange (1150183), IQPowerEdgeRefTriggerLevel (1150056), LowFrequencyBypassEnabled (1150207), MechanicalAttenuation (1150128), MechanicalAttenuationEnabled (1150081), MechanicalAttenuatorEnabled (1150081), MinimumAcpr (1150142), MinimumReconfigurationTime (1150165), NotchFilterEnabled (1150167), NumberOfSamples (1150009), OspDataScalingFactor (1150151), ReferenceLevel (1150004), RFAttenuation (1150005), RFPreampEnabled (1150129), RFPreselectorFilter (1150166), TimerEventInterval (1150096) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attenuation = None
    ChannelCoupling = None
    DdcReferenceTriggerOverride = None
    DeviceInstantaneousBandwidth = None
    DownConverterCenterFrequency = None
    DownconverterCenterFrequency = None
    DownconverterFrequencyOffset = None
    DownconverterPreselectorEnabled = None
    ExternalGain = None
    FrequencySettlingTime = None
    IFFilterBandwidth = None
    IFOutputPowerLevel = None
    IFOutputPowerLevelOffset = None
    IQCarrierFrequency = None
    IqInPortCarrierFrequency = None
    IqInPortVerticalRange = None
    IQPowerEdgeRefTriggerLevel = None
    LowFrequencyBypassEnabled = None
    MechanicalAttenuation = None
    MechanicalAttenuationEnabled = None
    MechanicalAttenuatorEnabled = None
    MinimumAcpr = None
    MinimumReconfigurationTime = None
    NotchFilterEnabled = None
    NumberOfSamples = None
    OspDataScalingFactor = None
    ReferenceLevel = None
    RFAttenuation = None
    RFPreampEnabled = None
    RFPreselectorFilter = None
    TimerEventInterval = None
    value__ = None


class RfsaConfigurationListStepTrigger(RfsaSubObject):
    # no doc
    DigitalEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsaConfigurationListStepTrigger) -> RfsaDigitalEdgeConfigurationListStepTrigger

"""



class RfsaContiguousMultiRecordEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaContiguousMultiRecordEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaDeembedding(RfsaSubObject):
    # no doc
    def ConfigureDeembeddingTableInterpolationLinear(self, tableName, format):
        """ ConfigureDeembeddingTableInterpolationLinear(self: RfsaDeembedding, tableName: str, format: RfsaLinearInterpolationFormat) """
        pass

    def ConfigureDeembeddingTableInterpolationNearest(self, tableName):
        """ ConfigureDeembeddingTableInterpolationNearest(self: RfsaDeembedding, tableName: str) """
        pass

    def ConfigureDeembeddingTableInterpolationSpline(self, tableName):
        """ ConfigureDeembeddingTableInterpolationSpline(self: RfsaDeembedding, tableName: str) """
        pass

    def CreateDeembeddingSParameterTableArray(self, tableName, frequencies, sParameterTable, sParameterOrientation):
        """ CreateDeembeddingSParameterTableArray(self: RfsaDeembedding, tableName: str, frequencies: Array[float], sParameterTable: Array[ComplexDouble], sParameterOrientation: RfsaSParameterOrientation) """
        pass

    def CreateDeembeddingSParameterTableS2pFile(self, tableName, s2pFilePath, sParameterOrientation):
        """ CreateDeembeddingSParameterTableS2pFile(self: RfsaDeembedding, tableName: str, s2pFilePath: str, sParameterOrientation: RfsaSParameterOrientation) """
        pass

    def DeleteAllDeembeddingTables(self):
        """ DeleteAllDeembeddingTables(self: RfsaDeembedding) """
        pass

    def DeleteDeembeddingTable(self, tableName):
        """ DeleteDeembeddingTable(self: RfsaDeembedding, tableName: str) """
        pass

    def GetDeembeddingSParameters(self, sParameters):
        """ GetDeembeddingSParameters(self: RfsaDeembedding, sParameters: Array[ComplexDouble]) -> Array[ComplexDouble] """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    DeembeddingSelectedTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingSelectedTable(self: RfsaDeembedding) -> str

Set: DeembeddingSelectedTable(self: RfsaDeembedding) = value
"""

    DeembeddingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingType(self: RfsaDeembedding) -> RfsaDeembeddingType

Set: DeembeddingType(self: RfsaDeembedding) = value
"""



class RfsaDeembeddingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaDeembeddingType, values: None (3900), Scalar (3901), Vector (3902) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    Scalar = None
    value__ = None
    Vector = None


class RfsaDeviceCharacteristics(RfsaSubObject):
    # no doc
    def GetDeviceTemperature(self):
        """ GetDeviceTemperature(self: RfsaDeviceCharacteristics) -> float """
        pass

    def GetDigitizerTemperature(self):
        """ GetDigitizerTemperature(self: RfsaDeviceCharacteristics) -> float """
        pass

    def GetLOTemperature(self):
        """ GetLOTemperature(self: RfsaDeviceCharacteristics) -> float """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    FpgaBitfilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FpgaBitfilePath(self: RfsaDeviceCharacteristics) -> str

"""

    FpgaTargetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FpgaTargetName(self: RfsaDeviceCharacteristics) -> str

"""

    FpgaTemperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FpgaTemperature(self: RfsaDeviceCharacteristics) -> float

"""

    MaxInstantaneousBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxInstantaneousBandwidth(self: RfsaDeviceCharacteristics) -> float

"""

    MaxIQRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxIQRate(self: RfsaDeviceCharacteristics) -> float

"""

    MemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemorySize(self: RfsaDeviceCharacteristics) -> Int64

"""

    ModulePowerConsumption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModulePowerConsumption(self: RfsaDeviceCharacteristics) -> float

"""

    ModuleRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModuleRevision(self: RfsaDeviceCharacteristics) -> str

"""

    PreselectorPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreselectorPresent(self: RfsaDeviceCharacteristics) -> bool

"""

    RFPreamplifierPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFPreamplifierPresent(self: RfsaDeviceCharacteristics) -> bool

"""

    SerialNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumber(self: RfsaDeviceCharacteristics) -> str

"""

    TemperatureReadInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureReadInterval(self: RfsaDeviceCharacteristics) -> float

Set: TemperatureReadInterval(self: RfsaDeviceCharacteristics) = value
"""



class RfsaDeviceResponseType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaDeviceResponseType, values: DownconverterCombined (2802), DownconverterIF (2800), DownconverterRF (2801), VsaCombined (2804), VsaIF (2803) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DownconverterCombined = None
    DownconverterIF = None
    DownconverterRF = None
    value__ = None
    VsaCombined = None
    VsaIF = None


class RfsaDigitalEdgeAdvanceTrigger(RfsaSubObject):
    # no doc
    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaDigitalEdgeAdvanceTrigger) -> RfsaDigitalEdgeAdvanceTriggerSource

Set: Source(self: RfsaDigitalEdgeAdvanceTrigger) = value
"""



class RfsaDigitalEdgeAdvanceTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitalEdgeAdvanceTriggerSource, obj: object) -> bool
        Equals(self: RfsaDigitalEdgeAdvanceTriggerSource, source: RfsaDigitalEdgeAdvanceTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaDigitalEdgeAdvanceTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitalEdgeAdvanceTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitalEdgeAdvanceTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    PXIeDStarB = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    TimerEvent = None


class RfsaDigitalEdgeArmReferenceTrigger(RfsaSubObject):
    # no doc
    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaDigitalEdgeArmReferenceTrigger) -> RfsaDigitalEdgeArmReferenceTriggerSource

Set: Source(self: RfsaDigitalEdgeArmReferenceTrigger) = value
"""



class RfsaDigitalEdgeArmReferenceTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitalEdgeArmReferenceTriggerSource, obj: object) -> bool
        Equals(self: RfsaDigitalEdgeArmReferenceTriggerSource, source: RfsaDigitalEdgeArmReferenceTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaDigitalEdgeArmReferenceTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitalEdgeArmReferenceTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitalEdgeArmReferenceTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    PXIeDStarB = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    TimerEvent = None


class RfsaDigitalEdgeConfigurationListStepTrigger(RfsaSubObject):
    # no doc
    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaDigitalEdgeConfigurationListStepTrigger) -> RfsaDigitalEdgeConfigurationListStepTriggerSource

Set: Source(self: RfsaDigitalEdgeConfigurationListStepTrigger) = value
"""



class RfsaDigitalEdgeConfigurationListStepTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitalEdgeConfigurationListStepTriggerSource, obj: object) -> bool
        Equals(self: RfsaDigitalEdgeConfigurationListStepTriggerSource, source: RfsaDigitalEdgeConfigurationListStepTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaDigitalEdgeConfigurationListStepTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitalEdgeConfigurationListStepTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitalEdgeConfigurationListStepTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    EndOfRecordEvent = None
    TimerEvent = None


class RfsaDigitalEdgeReferenceTrigger(RfsaSubObject):
    # no doc
    def Configure(self, source, edge, pretriggerSamples):
        """ Configure(self: RfsaDigitalEdgeReferenceTrigger, source: RfsaDigitalEdgeReferenceTriggerSource, edge: RfsaTriggerEdge, pretriggerSamples: Int64) """
        pass

    Edge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: RfsaDigitalEdgeReferenceTrigger) -> RfsaTriggerEdge

Set: Edge(self: RfsaDigitalEdgeReferenceTrigger) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaDigitalEdgeReferenceTrigger) -> RfsaDigitalEdgeReferenceTriggerSource

Set: Source(self: RfsaDigitalEdgeReferenceTrigger) = value
"""



class RfsaDigitalEdgeReferenceTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitalEdgeReferenceTriggerSource, obj: object) -> bool
        Equals(self: RfsaDigitalEdgeReferenceTriggerSource, source: RfsaDigitalEdgeReferenceTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaDigitalEdgeReferenceTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitalEdgeReferenceTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitalEdgeReferenceTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    PXIeDStarB = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    TimerEvent = None


class RfsaDigitalEdgeStartTrigger(RfsaSubObject):
    # no doc
    def Configure(self, source, edge):
        """ Configure(self: RfsaDigitalEdgeStartTrigger, source: RfsaDigitalEdgeStartTriggerSource, edge: RfsaTriggerEdge) """
        pass

    Edge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: RfsaDigitalEdgeStartTrigger) -> RfsaTriggerEdge

Set: Edge(self: RfsaDigitalEdgeStartTrigger) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaDigitalEdgeStartTrigger) -> RfsaDigitalEdgeStartTriggerSource

Set: Source(self: RfsaDigitalEdgeStartTrigger) = value
"""



class RfsaDigitalEdgeStartTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitalEdgeStartTriggerSource, obj: object) -> bool
        Equals(self: RfsaDigitalEdgeStartTriggerSource, source: RfsaDigitalEdgeStartTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaDigitalEdgeStartTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitalEdgeStartTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitalEdgeStartTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    PXIeDStarB = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    TimerEvent = None


class RfsaDigitizerDitherEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaDigitizerDitherEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaDigitizerSampleClock(RfsaSubObject):
    # no doc
    ClockRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClockRate(self: RfsaDigitizerSampleClock) -> float

"""

    Export = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Export(self: RfsaDigitizerSampleClock) -> RfsaExportDigitizerSampleClock

"""

    TimebaseRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimebaseRate(self: RfsaDigitizerSampleClock) -> float

Set: TimebaseRate(self: RfsaDigitizerSampleClock) = value
"""

    TimebaseSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimebaseSource(self: RfsaDigitizerSampleClock) -> RfsaDigitizerSampleClockTimebaseSource

Set: TimebaseSource(self: RfsaDigitizerSampleClock) = value
"""



class RfsaDigitizerSampleClockSynchronizationDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitizerSampleClockSynchronizationDistributionLine, obj: object) -> bool
        Equals(self: RfsaDigitizerSampleClockSynchronizationDistributionLine, source: RfsaDigitizerSampleClockSynchronizationDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaDigitizerSampleClockSynchronizationDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitizerSampleClockSynchronizationDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitizerSampleClockSynchronizationDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    PxiTrig0 = None
    PxiTrig1 = None
    PxiTrig2 = None
    PxiTrig3 = None
    PxiTrig4 = None
    PxiTrig5 = None
    PxiTrig6 = None
    PxiTrig7 = None


class RfsaDigitizerSampleClockTimebaseSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDigitizerSampleClockTimebaseSource, obj: object) -> bool
        Equals(self: RfsaDigitizerSampleClockTimebaseSource, timebaseSource: RfsaDigitizerSampleClockTimebaseSource) -> bool
        """
        pass

    @staticmethod
    def FromString(timebaseSource):
        """ FromString(timebaseSource: str) -> RfsaDigitizerSampleClockTimebaseSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDigitizerSampleClockTimebaseSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDigitizerSampleClockTimebaseSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockIn = None
    LOReferenceClock = None
    OnboardClock = None
    PxiStar = None


class RfsaDoneEvent(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaDoneEvent) -> RfsaDoneEventExportedOutputTerminal

Set: OutputTerminal(self: RfsaDoneEvent) = value
"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaDoneEvent) -> str

"""



class RfsaDoneEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaDoneEventExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaDoneEventExportedOutputTerminal, outputTerminal: RfsaDoneEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaDoneEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaDoneEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaDoneEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaDownconverterFrequencyOffsetMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaDownconverterFrequencyOffsetMode, values: Automatic (1903), Enabled (1901), UserDefined (1904) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Enabled = None
    UserDefined = None
    value__ = None


class RfsaDownconverterLoopBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaDownconverterLoopBandwidth, values: Medium (801), Narrow (800), Wide (802) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Medium = None
    Narrow = None
    value__ = None
    Wide = None


class RfsaDownconverterPreselectorEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaDownconverterPreselectorEnabled, values: Disabled (2600), Enabled (2602), EnabledWhenInSignalPath (2601) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    EnabledWhenInSignalPath = None
    value__ = None


class RfsaDriverIdentity(RfsaSubObject, IIviDriverIdentity, IIviComponentIdentity):
    # no doc
    def GetGroupCapabilities(self):
        """ GetGroupCapabilities(self: RfsaDriverIdentity) -> Array[str] """
        pass

    def GetSupportedInstrumentModels(self):
        """ GetSupportedInstrumentModels(self: RfsaDriverIdentity) -> Array[str] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: RfsaDriverIdentity) -> str

"""

    InstrumentFirmwareRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentFirmwareRevision(self: RfsaDriverIdentity) -> str

"""

    InstrumentManufacturer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentManufacturer(self: RfsaDriverIdentity) -> str

"""

    InstrumentModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentModel(self: RfsaDriverIdentity) -> str

"""

    SpecificDriverDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificDriverDescription(self: RfsaDriverIdentity) -> str

"""

    SpecificDriverRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificDriverRevision(self: RfsaDriverIdentity) -> str

"""

    SpecificDriverVendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificDriverVendor(self: RfsaDriverIdentity) -> str

"""



class RfsaDriverLock(object):
    """ RfsaDriverLock(iviDriverLock: IIviDriverLock) """
    def Unlock(self):
        """ Unlock(self: RfsaDriverLock) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iviDriverLock):
        """ __new__(cls: type, iviDriverLock: IIviDriverLock) """
        pass


class RfsaDriverOperation(RfsaSubObject, IIviDriverOperation, IDisposable, ISupportSynchronizationContext):
    # no doc
    def Dispose(self):
        """ Dispose(self: RfsaDriverOperation) """
        pass

    def InvalidateAllAttributes(self):
        """ InvalidateAllAttributes(self: RfsaDriverOperation) """
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

    Cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cache(self: RfsaDriverOperation) -> bool

Set: Cache(self: RfsaDriverOperation) = value
"""

    DriverSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverSetup(self: RfsaDriverOperation) -> str

"""

    InterchangeCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterchangeCheck(self: RfsaDriverOperation) -> bool

Set: InterchangeCheck(self: RfsaDriverOperation) = value
"""

    IOResourceDescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IOResourceDescriptor(self: RfsaDriverOperation) -> str

"""

    LogicalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalName(self: RfsaDriverOperation) -> str

"""

    QueryInstrumentStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QueryInstrumentStatus(self: RfsaDriverOperation) -> bool

Set: QueryInstrumentStatus(self: RfsaDriverOperation) = value
"""

    RangeCheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeCheck(self: RfsaDriverOperation) -> bool

Set: RangeCheck(self: RfsaDriverOperation) = value
"""

    RecordCoercions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecordCoercions(self: RfsaDriverOperation) -> bool

Set: RecordCoercions(self: RfsaDriverOperation) = value
"""

    Simulate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Simulate(self: RfsaDriverOperation) -> bool

Set: Simulate(self: RfsaDriverOperation) = value
"""

    SynchronizeCallbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizeCallbacks(self: RfsaDriverOperation) -> bool

Set: SynchronizeCallbacks(self: RfsaDriverOperation) = value
"""


    Warning = None


class RfsaDriverUtility(RfsaSubObject, IIviDriverUtility):
    # no doc
    def Commit(self):
        """ Commit(self: RfsaDriverUtility) """
        pass

    def Disable(self):
        """ Disable(self: RfsaDriverUtility) """
        pass

    def EnableSessionAccess(self, enable):
        """ EnableSessionAccess(self: RfsaDriverUtility, enable: bool) """
        pass

    def GetDeviceResponse(self, responseType, frequencies, magnitudeResponse, phaseResponse):
        """ GetDeviceResponse(self: RfsaDriverUtility, responseType: RfsaDeviceResponseType) -> (Array[float], Array[float], Array[float]) """
        pass

    def GetGainReferenceCalibrationBaseline(self):
        """ GetGainReferenceCalibrationBaseline(self: RfsaDriverUtility) -> Array[float] """
        pass

    def GetRelayName(self, indexOfRelay):
        """ GetRelayName(self: RfsaDriverUtility, indexOfRelay: int) -> str """
        pass

    def GetRelayOperationsCount(self):
        """ GetRelayOperationsCount(self: RfsaDriverUtility) -> Array[int] """
        pass

    def GetScalingCoefficients(self):
        """ GetScalingCoefficients(self: RfsaDriverUtility) -> Array[RfsaCoefficientInfo] """
        pass

    def Lock(self, maximumTime=None):
        """
        Lock(self: RfsaDriverUtility) -> RfsaDriverLock
        Lock(self: RfsaDriverUtility, maximumTime: PrecisionTimeSpan) -> RfsaDriverLock
        """
        pass

    def PerformThermalCorrection(self):
        """ PerformThermalCorrection(self: RfsaDriverUtility) """
        pass

    def Reset(self):
        """ Reset(self: RfsaDriverUtility) """
        pass

    def ResetAttribute(self, *__args):
        """ ResetAttribute(self: RfsaDriverUtility, property: PropertyInfo)ResetAttribute(self: RfsaDriverUtility, channelName: str, property: PropertyInfo) """
        pass

    def ResetDevice(self):
        """ ResetDevice(self: RfsaDriverUtility) """
        pass

    def ResetWithDefaults(self):
        """ ResetWithDefaults(self: RfsaDriverUtility) """
        pass

    def ResetWithOptions(self, stepsToOmit):
        """ ResetWithOptions(self: RfsaDriverUtility, stepsToOmit: RfsaResetStepsToOmit) """
        pass

    def RevisionQuery(self):
        """ RevisionQuery(self: RfsaDriverUtility) -> RfsaRevisionQueryResult """
        pass

    def SelfTest(self):
        """ SelfTest(self: RfsaDriverUtility) -> RfsaSelfTestResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RfsaEndOfRecordEvent(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaEndOfRecordEvent) -> RfsaEndOfRecordEventExportedOutputTerminal

Set: OutputTerminal(self: RfsaEndOfRecordEvent) = value
"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaEndOfRecordEvent) -> str

"""



class RfsaEndOfRecordEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaEndOfRecordEventExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaEndOfRecordEventExportedOutputTerminal, outputTerminal: RfsaEndOfRecordEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaEndOfRecordEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaEndOfRecordEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaEndOfRecordEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaErrorInfoUtility(RfsaSubObject):
    # no doc
    def ClearError(self):
        """ ClearError(self: RfsaErrorInfoUtility) """
        pass

    def ErrorMessage(self, errorCode):
        """ ErrorMessage(self: RfsaErrorInfoUtility, errorCode: int) -> str """
        pass

    def GetError(self):
        """ GetError(self: RfsaErrorInfoUtility) -> RfsaErrorQueryResult """
        pass

    def GetException(self):
        """ GetException(self: RfsaErrorInfoUtility) -> Exception """
        pass

    def GetStaticException(self, errorCode):
        """ GetStaticException(self: RfsaErrorInfoUtility, errorCode: int) -> Exception """
        pass

    def GetStaticWarning(self, warningCode):
        """ GetStaticWarning(self: RfsaErrorInfoUtility, warningCode: int) -> RfsaWarning """
        pass

    def GetWarning(self, warningCode=None):
        """
        GetWarning(self: RfsaErrorInfoUtility) -> RfsaWarning
        GetWarning(self: RfsaErrorInfoUtility, warningCode: int) -> RfsaWarning
        """
        pass


class RfsaErrorQueryResult(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaErrorQueryResult, obj: object) -> bool
        Equals(self: RfsaErrorQueryResult, result: RfsaErrorQueryResult) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaErrorQueryResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorCode(self: RfsaErrorQueryResult) -> int

"""

    ErrorMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessage(self: RfsaErrorQueryResult) -> str

"""



class RfsaEvents(RfsaSubObject):
    # no doc
    DoneEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoneEvent(self: RfsaEvents) -> RfsaDoneEvent

"""

    EndOfRecordEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOfRecordEvent(self: RfsaEvents) -> RfsaEndOfRecordEvent

"""

    ReadyForAdvanceEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadyForAdvanceEvent(self: RfsaEvents) -> RfsaReadyForAdvanceEvent

"""

    ReadyForReferenceEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadyForReferenceEvent(self: RfsaEvents) -> RfsaReadyForReferenceEvent

"""

    ReadyForStartEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadyForStartEvent(self: RfsaEvents) -> RfsaReadyForStartEvent

"""



class RfsaExportAdvanceTrigger(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaExportAdvanceTrigger) -> RfsaExportAdvanceTriggerExportedOutputTerminal

Set: OutputTerminal(self: RfsaExportAdvanceTrigger) = value
"""



class RfsaExportAdvanceTriggerExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaExportAdvanceTriggerExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaExportAdvanceTriggerExportedOutputTerminal, outputTerminal: RfsaExportAdvanceTriggerExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaExportAdvanceTriggerExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaExportAdvanceTriggerExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaExportAdvanceTriggerExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaExportDigitizerSampleClock(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaExportDigitizerSampleClock) -> RfsaExportDigitizerSampleClockExportedOutputTerminal

Set: OutputTerminal(self: RfsaExportDigitizerSampleClock) = value
"""



class RfsaExportDigitizerSampleClockExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaExportDigitizerSampleClockExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaExportDigitizerSampleClockExportedOutputTerminal, outputTerminal: RfsaExportDigitizerSampleClockExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaExportDigitizerSampleClockExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaExportDigitizerSampleClockExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaExportDigitizerSampleClockExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaExportReferenceClock(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaExportReferenceClock) -> RfsaExportReferenceClockExportedOutputTerminal

Set: OutputTerminal(self: RfsaExportReferenceClock) = value
"""



class RfsaExportReferenceClockExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaExportReferenceClockExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaExportReferenceClockExportedOutputTerminal, outputTerminal: RfsaExportReferenceClockExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaExportReferenceClockExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaExportReferenceClockExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaExportReferenceClockExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    IFCondRefOut = None
    None = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaExportReferenceTrigger(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaExportReferenceTrigger) -> RfsaExportReferenceTriggerExportedOutputTerminal

Set: OutputTerminal(self: RfsaExportReferenceTrigger) = value
"""



class RfsaExportReferenceTriggerExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaExportReferenceTriggerExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaExportReferenceTriggerExportedOutputTerminal, outputTerminal: RfsaExportReferenceTriggerExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaExportReferenceTriggerExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaExportReferenceTriggerExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaExportReferenceTriggerExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaExportStartTrigger(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaExportStartTrigger) -> RfsaExportStartTriggerExportedOutputTerminal

Set: OutputTerminal(self: RfsaExportStartTrigger) = value
"""



class RfsaExportStartTriggerExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaExportStartTriggerExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaExportStartTriggerExportedOutputTerminal, outputTerminal: RfsaExportStartTriggerExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaExportStartTriggerExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaExportStartTriggerExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaExportStartTriggerExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaExternalCalibration(RfsaSubObject):
    # no doc
    def GetExternalCalibrationLastDateAndTime(self):
        """ GetExternalCalibrationLastDateAndTime(self: RfsaExternalCalibration) -> DateTime """
        pass

    def GetExternalCalibrationLastTemperature(self):
        """ GetExternalCalibrationLastTemperature(self: RfsaExternalCalibration) -> float """
        pass

    def GetExternalCalibrationRecommendedInterval(self):
        """ GetExternalCalibrationRecommendedInterval(self: RfsaExternalCalibration) -> int """
        pass

    CalibrationUserDefinedInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationUserDefinedInfo(self: RfsaExternalCalibration) -> str

Set: CalibrationUserDefinedInfo(self: RfsaExternalCalibration) = value
"""

    CalibrationUserDefinedInfoMaxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationUserDefinedInfoMaxSize(self: RfsaExternalCalibration) -> int

"""



class RfsaFetchRelativeTo(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaFetchRelativeTo, values: CurrentReadPosition (704), FirstPretriggerSample (703), FirstSample (701), MostRecentSample (700), ReferenceTrigger (702) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CurrentReadPosition = None
    FirstPretriggerSample = None
    FirstSample = None
    MostRecentSample = None
    ReferenceTrigger = None
    value__ = None


class RfsaFftWindowType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaFftWindowType, values: Blackman (505), BlackmanHarris (503), ExactBlackman (504), FlatTop (506), FourTermBlackmanHarris (507), Gaussian (510), Hamming (502), Hanning (501), KaiserBessel (511), LowSideLobe (509), SevenTermBlackmanHarris (508), Uniform (500) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    ExactBlackman = None
    FlatTop = None
    FourTermBlackmanHarris = None
    Gaussian = None
    Hamming = None
    Hanning = None
    KaiserBessel = None
    LowSideLobe = None
    SevenTermBlackmanHarris = None
    Uniform = None
    value__ = None


class RfsaFrequencySettlingUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaFrequencySettlingUnits, values: Ppm (2000), SecondsAfterIO (2002), SecondsAfterLock (2001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaIFConditioningDownconversionEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaIFConditioningDownconversionEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaIFFilter(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaIFFilter, values: IFFilter187_5MhzNarrow (1401), IFFilter187_5MhzWide (1400), IFFilter53Mhz (1402), IFFilterBypass (1403) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IFFilter187_5MhzNarrow = None
    IFFilter187_5MhzWide = None
    IFFilter53Mhz = None
    IFFilterBypass = None
    value__ = None


class RfsaInputIsolationEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaInputIsolationEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaInputPort(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaInputPort, values: CalIn (2002), IOnly (2003), IQIn (2001), RFIn (2000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CalIn = None
    IOnly = None
    IQIn = None
    RFIn = None
    value__ = None


class RfsaIQAcquisition(RfsaSubObject):
    # no doc
    def Abort(self):
        """ Abort(self: RfsaIQAcquisition) """
        pass

    def CheckAcquisitionStatus(self):
        """ CheckAcquisitionStatus(self: RfsaIQAcquisition) -> RfsaAcquisitionStatus """
        pass

    def FetchIQMultiRecordComplex(self, startingRecord, numberOfRecords, numberOfSamples, timeout, *__args):
        """
        FetchIQMultiRecordComplex[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> Array[T]
        FetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexDouble], Array[ComplexDouble])
        FetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexInt16], Array[ComplexInt16])
        FetchIQMultiRecordComplex[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[T], Array[RfsaWaveformInfo])
        FetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexDouble], Array[RfsaWaveformInfo], Array[ComplexDouble])
        FetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexInt16], Array[RfsaWaveformInfo], Array[ComplexInt16])
        FetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexSingle], Array[ComplexSingle])
        FetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexSingle], Array[RfsaWaveformInfo], Array[ComplexSingle])
        """
        pass

    def FetchIQMultiRecordComplexWaveforms(self, startingRecord, numberOfRecords, numberOfSamples, timeout, *__args):
        """
        FetchIQMultiRecordComplexWaveforms[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> ComplexWaveformCollection[T]
        FetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[ComplexDouble], ComplexWaveformCollection[ComplexDouble])
        FetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[ComplexInt16], ComplexWaveformCollection[ComplexInt16])
        FetchIQMultiRecordComplexWaveforms[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[T], Array[RfsaWaveformInfo])
        FetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[ComplexDouble], Array[RfsaWaveformInfo], ComplexWaveformCollection[ComplexDouble])
        FetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[ComplexInt16], Array[RfsaWaveformInfo], ComplexWaveformCollection[ComplexInt16])
        FetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[ComplexSingle], ComplexWaveformCollection[ComplexSingle])
        FetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveformCollection[ComplexSingle], Array[RfsaWaveformInfo], ComplexWaveformCollection[ComplexSingle])
        """
        pass

    def FetchIQSingleRecordComplex(self, recordNumber, numberOfSamples, timeout, *__args):
        """
        FetchIQSingleRecordComplex[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[T], RfsaWaveformInfo)
        FetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexDouble], RfsaWaveformInfo, Array[ComplexDouble])
        FetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexInt16], RfsaWaveformInfo, Array[ComplexInt16])
        FetchIQSingleRecordComplex[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> Array[T]
        FetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexDouble], Array[ComplexDouble])
        FetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexInt16], Array[ComplexInt16])
        FetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexSingle], Array[ComplexSingle])
        FetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (Array[ComplexSingle], RfsaWaveformInfo, Array[ComplexSingle])
        """
        pass

    def FetchIQSingleRecordComplexWaveform(self, recordNumber, numberOfSamples, timeout, *__args):
        """
        FetchIQSingleRecordComplexWaveform[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[T], RfsaWaveformInfo)
        FetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexDouble], RfsaWaveformInfo, ComplexWaveform[ComplexDouble])
        FetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexInt16], RfsaWaveformInfo, ComplexWaveform[ComplexInt16])
        FetchIQSingleRecordComplexWaveform[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> ComplexWaveform[T]
        FetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexDouble], ComplexWaveform[ComplexDouble])
        FetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexInt16], ComplexWaveform[ComplexInt16])
        FetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexSingle], ComplexWaveform[ComplexSingle])
        FetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexSingle], RfsaWaveformInfo, ComplexWaveform[ComplexSingle])
        """
        pass

    def GetFetchBacklog(self, recordNumber):
        """ GetFetchBacklog(self: RfsaIQAcquisition, recordNumber: Int64) -> Int64 """
        pass

    def Initiate(self):
        """ Initiate(self: RfsaIQAcquisition) """
        pass

    def MemoryOptimizedFetchIQMultiRecordComplex(self, startingRecord, numberOfRecords, numberOfSamples, timeout, data, waveformInfo=None):
        """
        MemoryOptimizedFetchIQMultiRecordComplex[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[T]) -> (Array[T], Array[T], Array[RfsaWaveformInfo])
        MemoryOptimizedFetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexDouble]) -> (Array[ComplexDouble], Array[ComplexDouble], Array[RfsaWaveformInfo])
        MemoryOptimizedFetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexInt16]) -> (Array[ComplexInt16], Array[ComplexInt16], Array[RfsaWaveformInfo])
        MemoryOptimizedFetchIQMultiRecordComplex[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[T]) -> (Array[T], Array[T])
        MemoryOptimizedFetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexDouble]) -> (Array[ComplexDouble], Array[ComplexDouble])
        MemoryOptimizedFetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexInt16]) -> (Array[ComplexInt16], Array[ComplexInt16])
        MemoryOptimizedFetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexSingle]) -> (Array[ComplexSingle], Array[ComplexSingle])
        MemoryOptimizedFetchIQMultiRecordComplex(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexSingle]) -> (Array[ComplexSingle], Array[ComplexSingle], Array[RfsaWaveformInfo])
        """
        pass

    def MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self, startingRecord, numberOfRecords, numberOfSamples, timeout, waveforms, waveformInfo=None):
        """
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[T]) -> (ComplexWaveformCollection[T], ComplexWaveformCollection[T])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[ComplexDouble]) -> (ComplexWaveformCollection[ComplexDouble], ComplexWaveformCollection[ComplexDouble])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[ComplexInt16]) -> (ComplexWaveformCollection[ComplexInt16], ComplexWaveformCollection[ComplexInt16])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms[T](self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[T]) -> (ComplexWaveformCollection[T], ComplexWaveformCollection[T], Array[RfsaWaveformInfo])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[ComplexDouble]) -> (ComplexWaveformCollection[ComplexDouble], ComplexWaveformCollection[ComplexDouble], Array[RfsaWaveformInfo])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[ComplexInt16]) -> (ComplexWaveformCollection[ComplexInt16], ComplexWaveformCollection[ComplexInt16], Array[RfsaWaveformInfo])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[ComplexSingle]) -> (ComplexWaveformCollection[ComplexSingle], ComplexWaveformCollection[ComplexSingle])
        MemoryOptimizedFetchIQMultiRecordComplexWaveforms(self: RfsaIQAcquisition, startingRecord: Int64, numberOfRecords: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveforms: ComplexWaveformCollection[ComplexSingle]) -> (ComplexWaveformCollection[ComplexSingle], ComplexWaveformCollection[ComplexSingle], Array[RfsaWaveformInfo])
        """
        pass

    def MemoryOptimizedFetchIQSingleRecordComplex(self, recordNumber, numberOfSamples, timeout, data, waveformInfo=None):
        """
        MemoryOptimizedFetchIQSingleRecordComplex[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[T]) -> (Array[T], Array[T], RfsaWaveformInfo)
        MemoryOptimizedFetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexDouble]) -> (Array[ComplexDouble], Array[ComplexDouble], RfsaWaveformInfo)
        MemoryOptimizedFetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexInt16]) -> (Array[ComplexInt16], Array[ComplexInt16], RfsaWaveformInfo)
        MemoryOptimizedFetchIQSingleRecordComplex[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[T]) -> (Array[T], Array[T])
        MemoryOptimizedFetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexDouble]) -> (Array[ComplexDouble], Array[ComplexDouble])
        MemoryOptimizedFetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexInt16]) -> (Array[ComplexInt16], Array[ComplexInt16])
        MemoryOptimizedFetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexSingle]) -> (Array[ComplexSingle], Array[ComplexSingle])
        MemoryOptimizedFetchIQSingleRecordComplex(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, data: Array[ComplexSingle]) -> (Array[ComplexSingle], Array[ComplexSingle], RfsaWaveformInfo)
        """
        pass

    def MemoryOptimizedFetchIQSingleRecordComplexWaveform(self, recordNumber, numberOfSamples, timeout, waveform, waveformInfo=None):
        """
        MemoryOptimizedFetchIQSingleRecordComplexWaveform[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[T]) -> (ComplexWaveform[T], ComplexWaveform[T])
        MemoryOptimizedFetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexDouble]) -> (ComplexWaveform[ComplexDouble], ComplexWaveform[ComplexDouble])
        MemoryOptimizedFetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexInt16]) -> (ComplexWaveform[ComplexInt16], ComplexWaveform[ComplexInt16])
        MemoryOptimizedFetchIQSingleRecordComplexWaveform[T](self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[T]) -> (ComplexWaveform[T], ComplexWaveform[T], RfsaWaveformInfo)
        MemoryOptimizedFetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexDouble]) -> (ComplexWaveform[ComplexDouble], ComplexWaveform[ComplexDouble], RfsaWaveformInfo)
        MemoryOptimizedFetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexInt16]) -> (ComplexWaveform[ComplexInt16], ComplexWaveform[ComplexInt16], RfsaWaveformInfo)
        MemoryOptimizedFetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexSingle]) -> (ComplexWaveform[ComplexSingle], ComplexWaveform[ComplexSingle])
        MemoryOptimizedFetchIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, recordNumber: Int64, numberOfSamples: Int64, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexSingle]) -> (ComplexWaveform[ComplexSingle], ComplexWaveform[ComplexSingle], RfsaWaveformInfo)
        """
        pass

    def MemoryOptimizedReadIQSingleRecordComplex(self, timeout, data, waveformInfo=None):
        """
        MemoryOptimizedReadIQSingleRecordComplex(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan, data: Array[ComplexDouble]) -> (Array[ComplexDouble], Array[ComplexDouble], RfsaWaveformInfo)
        MemoryOptimizedReadIQSingleRecordComplex(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan, data: Array[ComplexDouble]) -> (Array[ComplexDouble], Array[ComplexDouble])
        """
        pass

    def MemoryOptimizedReadIQSingleRecordComplexWaveform(self, timeout, waveform, waveformInfo=None):
        """
        MemoryOptimizedReadIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexDouble]) -> (ComplexWaveform[ComplexDouble], ComplexWaveform[ComplexDouble], RfsaWaveformInfo)
        MemoryOptimizedReadIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan, waveform: ComplexWaveform[ComplexDouble]) -> (ComplexWaveform[ComplexDouble], ComplexWaveform[ComplexDouble])
        """
        pass

    def ReadIQSingleRecordComplex(self, timeout, waveformInfo=None):
        """
        ReadIQSingleRecordComplex(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan) -> (Array[ComplexDouble], RfsaWaveformInfo)
        ReadIQSingleRecordComplex(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan) -> Array[ComplexDouble]
        """
        pass

    def ReadIQSingleRecordComplexWaveform(self, timeout, waveformInfo=None):
        """
        ReadIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan) -> (ComplexWaveform[ComplexDouble], RfsaWaveformInfo)
        ReadIQSingleRecordComplexWaveform(self: RfsaIQAcquisition, timeout: PrecisionTimeSpan) -> ComplexWaveform[ComplexDouble]
        """
        pass

    FetchOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FetchOffset(self: RfsaIQAcquisition) -> Int64

Set: FetchOffset(self: RfsaIQAcquisition) = value
"""

    FetchRelativeTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FetchRelativeTo(self: RfsaIQAcquisition) -> RfsaFetchRelativeTo

Set: FetchRelativeTo(self: RfsaIQAcquisition) = value
"""

    RecordsDone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecordsDone(self: RfsaIQAcquisition) -> int

"""



class RfsaIQAcquisitionConfiguration(RfsaSubObject):
    # no doc
    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaIQAcquisitionConfiguration) -> RfsaAdvancedIQAcquisitionConfiguration

"""

    AllowMoreRecordsThanMemory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowMoreRecordsThanMemory(self: RfsaIQAcquisitionConfiguration) -> bool

Set: AllowMoreRecordsThanMemory(self: RfsaIQAcquisitionConfiguration) = value
"""

    CarrierFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CarrierFrequency(self: RfsaIQAcquisitionConfiguration) -> float

Set: CarrierFrequency(self: RfsaIQAcquisitionConfiguration) = value
"""

    IQRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQRate(self: RfsaIQAcquisitionConfiguration) -> float

Set: IQRate(self: RfsaIQAcquisitionConfiguration) = value
"""

    NumberOfRecords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRecords(self: RfsaIQAcquisitionConfiguration) -> Int64

Set: NumberOfRecords(self: RfsaIQAcquisitionConfiguration) = value
"""

    NumberOfRecordsIsFinite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRecordsIsFinite(self: RfsaIQAcquisitionConfiguration) -> bool

Set: NumberOfRecordsIsFinite(self: RfsaIQAcquisitionConfiguration) = value
"""

    NumberOfSamples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSamples(self: RfsaIQAcquisitionConfiguration) -> Int64

Set: NumberOfSamples(self: RfsaIQAcquisitionConfiguration) = value
"""

    NumberOfSamplesIsFinite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSamplesIsFinite(self: RfsaIQAcquisitionConfiguration) -> bool

Set: NumberOfSamplesIsFinite(self: RfsaIQAcquisitionConfiguration) = value
"""

    PhaseOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseOffset(self: RfsaIQAcquisitionConfiguration) -> float

Set: PhaseOffset(self: RfsaIQAcquisitionConfiguration) = value
"""

    SignalBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalBandwidth(self: RfsaIQAcquisitionConfiguration) -> float

Set: SignalBandwidth(self: RfsaIQAcquisitionConfiguration) = value
"""



class RfsaIQAnalogEdge(RfsaSubObject):
    # no doc
    Hysteresis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hysteresis(self: RfsaIQAnalogEdge) -> float

Set: Hysteresis(self: RfsaIQAnalogEdge) = value
"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: RfsaIQAnalogEdge) -> float

Set: Level(self: RfsaIQAnalogEdge) = value
"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slope(self: RfsaIQAnalogEdge) -> RfsaIQAnalogEdgeReferenceTriggerSlope

Set: Slope(self: RfsaIQAnalogEdge) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaIQAnalogEdge) -> RfsaIQAnalogEdgeSource

Set: Source(self: RfsaIQAnalogEdge) = value
"""



class RfsaIQAnalogEdgeReferenceTriggerSlope(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaIQAnalogEdgeReferenceTriggerSlope, values: Falling (1001), Rising (1000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaIQAnalogEdgeSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaIQAnalogEdgeSource, obj: object) -> bool
        Equals(self: RfsaIQAnalogEdgeSource, source: RfsaIQAnalogEdgeSource) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaIQAnalogEdgeSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaIQAnalogEdgeSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    I = None
    IQ = None
    Q = None
    QI = None


class RfsaIQInPortChannel(RfsaSubObject):
    # no doc
    TerminalConfiguration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalConfiguration(self: RfsaIQInPortChannel) -> RfsaIQInPortTerminalConfiguration

Set: TerminalConfiguration(self: RfsaIQInPortChannel) = value
"""

    VerticalRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalRange(self: RfsaIQInPortChannel) -> float

Set: VerticalRange(self: RfsaIQInPortChannel) = value
"""



class RfsaIQInPortChannelCollection(RfsaSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    CarrierFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CarrierFrequency(self: RfsaIQInPortChannelCollection) -> float

Set: CarrierFrequency(self: RfsaIQInPortChannelCollection) = value
"""

    CommonMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommonMode(self: RfsaIQInPortChannelCollection) -> float

Set: CommonMode(self: RfsaIQInPortChannelCollection) = value
"""

    Temperature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Temperature(self: RfsaIQInPortChannelCollection) -> float

"""



class RfsaIQInPortTerminalConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaIQInPortTerminalConfiguration, values: Differential (2100), SingleEnded (2101) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaIQPowerEdge(RfsaSubObject):
    # no doc
    def Configure(self, source, level, slope, pretriggerSamples):
        """ Configure(self: RfsaIQPowerEdge, source: RfsaIQPowerEdgeReferenceTriggerSource, level: float, slope: RfsaIQPowerEdgeReferenceTriggerSlope, pretriggerSamples: Int64) """
        pass

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: RfsaIQPowerEdge) -> float

Set: Level(self: RfsaIQPowerEdge) = value
"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slope(self: RfsaIQPowerEdge) -> RfsaIQPowerEdgeReferenceTriggerSlope

Set: Slope(self: RfsaIQPowerEdge) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaIQPowerEdge) -> RfsaIQPowerEdgeReferenceTriggerSource

Set: Source(self: RfsaIQPowerEdge) = value
"""



class RfsaIQPowerEdgeReferenceTriggerSlope(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaIQPowerEdgeReferenceTriggerSlope, values: Falling (1001), Rising (1000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaIQPowerEdgeReferenceTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaIQPowerEdgeReferenceTriggerSource, obj: object) -> bool
        Equals(self: RfsaIQPowerEdgeReferenceTriggerSource, source: RfsaIQPowerEdgeReferenceTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaIQPowerEdgeReferenceTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaIQPowerEdgeReferenceTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaIQPowerEdgeReferenceTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Zero = None


class RfsaLinearInterpolationFormat(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLinearInterpolationFormat, values: MagnitudeAndPhase (4001), MagnitudeInDecibelAndPhase (4002), RealAndImaginary (4000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    MagnitudeInDecibelAndPhase = None
    RealAndImaginary = None
    value__ = None


class RfsaLO2ExportEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLO2ExportEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaLocalOscillator(RfsaSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    DownconverterLoopBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterLoopBandwidth(self: RfsaLocalOscillator) -> RfsaDownconverterLoopBandwidth

Set: DownconverterLoopBandwidth(self: RfsaLocalOscillator) = value
"""

    FrequencySettlingTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencySettlingTime(self: RfsaLocalOscillator) -> float

Set: FrequencySettlingTime(self: RfsaLocalOscillator) = value
"""

    FrequencySettlingUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencySettlingUnits(self: RfsaLocalOscillator) -> RfsaFrequencySettlingUnits

Set: FrequencySettlingUnits(self: RfsaLocalOscillator) = value
"""

    LO2ExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LO2ExportEnabled(self: RfsaLocalOscillator) -> RfsaLO2ExportEnabled

Set: LO2ExportEnabled(self: RfsaLocalOscillator) = value
"""

    LOExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOExportEnabled(self: RfsaLocalOscillator) -> bool

Set: LOExportEnabled(self: RfsaLocalOscillator) = value
"""

    LOFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequency(self: RfsaLocalOscillator) -> float

Set: LOFrequency(self: RfsaLocalOscillator) = value
"""

    LOFrequencyStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequencyStepSize(self: RfsaLocalOscillator) -> float

Set: LOFrequencyStepSize(self: RfsaLocalOscillator) = value
"""

    LOInjectionSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInjectionSide(self: RfsaLocalOscillator) -> RfsaLOInjectionSide

Set: LOInjectionSide(self: RfsaLocalOscillator) = value
"""

    LOInPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInPower(self: RfsaLocalOscillator) -> float

Set: LOInPower(self: RfsaLocalOscillator) = value
"""

    LOOutExportConfigureFromRfsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutExportConfigureFromRfsg(self: RfsaLocalOscillator) -> RfsaLOOutExportConfigureFromRfsg

Set: LOOutExportConfigureFromRfsg(self: RfsaLocalOscillator) = value
"""

    LOOutPower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutPower(self: RfsaLocalOscillator) -> float

Set: LOOutPower(self: RfsaLocalOscillator) = value
"""

    LOPllFractionalModeEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOPllFractionalModeEnabled(self: RfsaLocalOscillator) -> RfsaLOPllFractionalModeEnabled

Set: LOPllFractionalModeEnabled(self: RfsaLocalOscillator) = value
"""

    LOSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOSource(self: RfsaLocalOscillator) -> RfsaLOSource

Set: LOSource(self: RfsaLocalOscillator) = value
"""

    LOVcoFrequencyStepSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOVcoFrequencyStepSize(self: RfsaLocalOscillator) -> float

Set: LOVcoFrequencyStepSize(self: RfsaLocalOscillator) = value
"""

    LOYigMainCoilDrive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOYigMainCoilDrive(self: RfsaLocalOscillator) -> RfsaLOYigMainCoilDrive

Set: LOYigMainCoilDrive(self: RfsaLocalOscillator) = value
"""

    RFOutLOExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFOutLOExportEnabled(self: RfsaLocalOscillator) -> RfsaRFOutLOExportEnabled

Set: RFOutLOExportEnabled(self: RfsaLocalOscillator) = value
"""



class RfsaLOInjectionSide(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLOInjectionSide, values: High (1300), Low (1301) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    High = None
    Low = None
    value__ = None


class RfsaLOOutExportConfigureFromRfsg(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLOOutExportConfigureFromRfsg, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaLOPllFractionalModeEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLOPllFractionalModeEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaLOSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaLOSource, obj: object) -> bool
        Equals(self: RfsaLOSource, source: RfsaLOSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaLOSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaLOSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaLOSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    LOIn = None
    None = None
    Onboard = None
    Secondary = None
    SGSAShared = None


class RfsaLowFrequencyBypassEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLowFrequencyBypassEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaLOYigMainCoilDrive(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaLOYigMainCoilDrive, values: Fast (2401), Normal (2400) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Normal = None
    value__ = None


class RfsaNI5663AdvancedVertical(RfsaSubObject):
    # no doc
    MechanicalAttenuatorEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MechanicalAttenuatorEnabled(self: RfsaNI5663AdvancedVertical) -> MechanicalAttenuatorEnabled

Set: MechanicalAttenuatorEnabled(self: RfsaNI5663AdvancedVertical) = value
"""



class RfsaNI5663SignalPath(RfsaSubObject):
    # no doc
    IF1AttenuationValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IF1AttenuationValue(self: RfsaNI5663SignalPath) -> float

Set: IF1AttenuationValue(self: RfsaNI5663SignalPath) = value
"""

    IF2AttenuationValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IF2AttenuationValue(self: RfsaNI5663SignalPath) -> float

Set: IF2AttenuationValue(self: RfsaNI5663SignalPath) = value
"""

    IFAttenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFAttenuation(self: RfsaNI5663SignalPath) -> float

Set: IFAttenuation(self: RfsaNI5663SignalPath) = value
"""

    IFFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFFilter(self: RfsaNI5663SignalPath) -> RfsaIFFilter

Set: IFFilter(self: RfsaNI5663SignalPath) = value
"""

    RFAttenuationIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFAttenuationIndex(self: RfsaNI5663SignalPath) -> int

Set: RFAttenuationIndex(self: RfsaNI5663SignalPath) = value
"""

    RFAttenuationTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFAttenuationTable(self: RfsaNI5663SignalPath) -> int

Set: RFAttenuationTable(self: RfsaNI5663SignalPath) = value
"""



class RfsaNI5665AdvancedVertical(RfsaSubObject):
    # no doc
    ChannelCoupling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelCoupling(self: RfsaNI5665AdvancedVertical) -> RfsaChannelCoupling

Set: ChannelCoupling(self: RfsaNI5665AdvancedVertical) = value
"""

    RFPreampEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFPreampEnabled(self: RfsaNI5665AdvancedVertical) -> RfsaRFPreamplifierEnabled

Set: RFPreampEnabled(self: RfsaNI5665AdvancedVertical) = value
"""



class RfsaNI5665SignalPath(RfsaSubObject):
    # no doc
    LOYigMainCoilDrive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOYigMainCoilDrive(self: RfsaNI5665SignalPath) -> RfsaLOYigMainCoilDrive

Set: LOYigMainCoilDrive(self: RfsaNI5665SignalPath) = value
"""

    PreselectorEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreselectorEnabled(self: RfsaNI5665SignalPath) -> RfsaPreselectorEnabled

Set: PreselectorEnabled(self: RfsaNI5665SignalPath) = value
"""



class RfsaNI5693AdvancedVertical(RfsaSubObject):
    # no doc
    CalibrationTonePowerReferredToRFIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationTonePowerReferredToRFIn(self: RfsaNI5693AdvancedVertical) -> float

"""



class RfsaNI5693RFConditioningCalibrationToneMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaNI5693RFConditioningCalibrationToneMode, values: Disabled (2700), HighbandRF (2702), LowbandRF (2701) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    HighbandRF = None
    LowbandRF = None
    value__ = None


class RfsaNI5693RFPreselectorCalibrationToneMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaNI5693RFPreselectorCalibrationToneMode, values: Disabled (2700), HighbandRF (2702), LowbandRF (2701) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    HighbandRF = None
    LowbandRF = None
    value__ = None


class RfsaNI5693SelfCalibration(RfsaSubObject):
    # no doc
    RFConditioningCalibrationToneFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFConditioningCalibrationToneFrequency(self: RfsaNI5693SelfCalibration) -> float

Set: RFConditioningCalibrationToneFrequency(self: RfsaNI5693SelfCalibration) = value
"""

    RFConditioningCalibrationToneMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFConditioningCalibrationToneMode(self: RfsaNI5693SelfCalibration) -> RfsaNI5693RFConditioningCalibrationToneMode

Set: RFConditioningCalibrationToneMode(self: RfsaNI5693SelfCalibration) = value
"""

    RFPreselectorCalibrationToneFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFPreselectorCalibrationToneFrequency(self: RfsaNI5693SelfCalibration) -> float

Set: RFPreselectorCalibrationToneFrequency(self: RfsaNI5693SelfCalibration) = value
"""

    RFPreselectorCalibrationToneMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFPreselectorCalibrationToneMode(self: RfsaNI5693SelfCalibration) -> RfsaNI5693RFPreselectorCalibrationToneMode

Set: RFPreselectorCalibrationToneMode(self: RfsaNI5693SelfCalibration) = value
"""



class RfsaNI5694AdvancedVertical(RfsaSubObject):
    # no doc
    StepGainEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StepGainEnabled(self: RfsaNI5694AdvancedVertical) -> RfsaStepGainEnabled

Set: StepGainEnabled(self: RfsaNI5694AdvancedVertical) = value
"""



class RfsaNI5694SignalPath(RfsaSubObject):
    # no doc
    SignalConditioningEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalConditioningEnabled(self: RfsaNI5694SignalPath) -> RfsaSignalConditioningEnabled

Set: SignalConditioningEnabled(self: RfsaNI5694SignalPath) = value
"""



class RfsaNISelfCalibrationToneMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaNISelfCalibrationToneMode, values: Disabled (2700), HighbandIF (2703), HighbandRF (2702), LowbandRF (2701) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    HighbandIF = None
    HighbandRF = None
    LowbandRF = None
    value__ = None


class RfsaNoiseSourcePowerEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaNoiseSourcePowerEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaNotchFilterEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaNotchFilterEnabled, values: Disabled (3400), Enabled (3402), EnabledWhenInSignalPath (3401) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    EnabledWhenInSignalPath = None
    value__ = None


class RfsaOspDelayEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaOspDelayEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaOverflowErrorReporting(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaOverflowErrorReporting, values: Disabled (1302), Warning (1301) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaPowerSpectrumUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaPowerSpectrumUnits, values: dBm (200), dBmV (202), dBuV (203), Volts (204), VoltsSquared (201), Watts (205) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    value__ = None
    Volts = None
    VoltsSquared = None
    Watts = None


class RfsaPreselectorEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaPreselectorEnabled, values: Disabled (2600), Enabled (2602), EnabledWhenInSignalPath (2601) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    EnabledWhenInSignalPath = None
    value__ = None


class RfsaPxiChassisClk10Source(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaPxiChassisClk10Source, obj: object) -> bool
        Equals(self: RfsaPxiChassisClk10Source, source: RfsaPxiChassisClk10Source) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaPxiChassisClk10Source """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaPxiChassisClk10Source) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaPxiChassisClk10Source) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    None = None
    OnboardClock = None
    ReferenceIn = None


class RfsaReadyForAdvanceEvent(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaReadyForAdvanceEvent) -> RfsaReadyForAdvanceEventExportedOutputTerminal

Set: OutputTerminal(self: RfsaReadyForAdvanceEvent) = value
"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaReadyForAdvanceEvent) -> str

"""



class RfsaReadyForAdvanceEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaReadyForAdvanceEventExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaReadyForAdvanceEventExportedOutputTerminal, outputTerminal: RfsaReadyForAdvanceEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaReadyForAdvanceEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaReadyForAdvanceEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaReadyForAdvanceEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaReadyForReferenceEvent(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaReadyForReferenceEvent) -> RfsaReadyForReferenceEventExportedOutputTerminal

Set: OutputTerminal(self: RfsaReadyForReferenceEvent) = value
"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaReadyForReferenceEvent) -> str

"""



class RfsaReadyForReferenceEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaReadyForReferenceEventExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaReadyForReferenceEventExportedOutputTerminal, outputTerminal: RfsaReadyForReferenceEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaReadyForReferenceEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaReadyForReferenceEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaReadyForReferenceEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaReadyForStartEvent(RfsaSubObject):
    # no doc
    OutputTerminal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsaReadyForStartEvent) -> RfsaReadyForStartEventExportedOutputTerminal

Set: OutputTerminal(self: RfsaReadyForStartEvent) = value
"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaReadyForStartEvent) -> str

"""



class RfsaReadyForStartEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaReadyForStartEventExportedOutputTerminal, obj: object) -> bool
        Equals(self: RfsaReadyForStartEventExportedOutputTerminal, outputTerminal: RfsaReadyForStartEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsaReadyForStartEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaReadyForStartEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaReadyForStartEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiStarLine = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsaReferenceClock(RfsaSubObject):
    # no doc
    def Configure(self, referenceClockSource, referenceClockRate):
        """ Configure(self: RfsaReferenceClock, referenceClockSource: RfsaReferenceClockSource, referenceClockRate: float) """
        pass

    Export = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Export(self: RfsaReferenceClock) -> RfsaExportReferenceClock

"""

    PxiChassisClk10Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PxiChassisClk10Source(self: RfsaReferenceClock) -> RfsaPxiChassisClk10Source

Set: PxiChassisClk10Source(self: RfsaReferenceClock) = value
"""

    Rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rate(self: RfsaReferenceClock) -> float

Set: Rate(self: RfsaReferenceClock) = value
"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsaReferenceClock) -> RfsaReferenceClockSource

Set: Source(self: RfsaReferenceClock) = value
"""



class RfsaReferenceClockSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaReferenceClockSource, obj: object) -> bool
        Equals(self: RfsaReferenceClockSource, source: RfsaReferenceClockSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaReferenceClockSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaReferenceClockSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaReferenceClockSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockIn = None
    None = None
    OnboardClock = None
    PxiClock = None
    ReferenceIn = None


class RfsaReferenceTrigger(RfsaSubObject):
    # no doc
    def Disable(self):
        """ Disable(self: RfsaReferenceTrigger) """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RfsaReferenceTrigger) """
        pass

    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaReferenceTrigger) -> RfsaAdvancedReferenceTrigger

"""

    DigitalEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsaReferenceTrigger) -> RfsaDigitalEdgeReferenceTrigger

"""

    Export = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Export(self: RfsaReferenceTrigger) -> RfsaExportReferenceTrigger

"""

    IQAnalogEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQAnalogEdge(self: RfsaReferenceTrigger) -> RfsaIQAnalogEdge

"""

    IQPowerEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IQPowerEdge(self: RfsaReferenceTrigger) -> RfsaIQPowerEdge

"""

    MinimumQuietTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumQuietTime(self: RfsaReferenceTrigger) -> float

Set: MinimumQuietTime(self: RfsaReferenceTrigger) = value
"""

    PreTriggerSamples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreTriggerSamples(self: RfsaReferenceTrigger) -> Int64

Set: PreTriggerSamples(self: RfsaReferenceTrigger) = value
"""

    Synchronization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronization(self: RfsaReferenceTrigger) -> RfsaReferenceTriggerSynchronization

"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaReferenceTrigger) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RfsaReferenceTrigger) -> RfsaReferenceTriggerType

Set: Type(self: RfsaReferenceTrigger) = value
"""



class RfsaReferenceTriggerSynchronization(RfsaSubObject):
    # no doc
    DelayEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DelayEnabled(self: RfsaReferenceTriggerSynchronization) -> RfsaReferenceTriggerSynchronizationDelayEnabled

Set: DelayEnabled(self: RfsaReferenceTriggerSynchronization) = value
"""

    DistributionLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionLine(self: RfsaReferenceTriggerSynchronization) -> RfsaReferenceTriggerSynchronizationDistributionLine

Set: DistributionLine(self: RfsaReferenceTriggerSynchronization) = value
"""

    IsMaster = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMaster(self: RfsaReferenceTriggerSynchronization) -> bool

Set: IsMaster(self: RfsaReferenceTriggerSynchronization) = value
"""



class RfsaReferenceTriggerSynchronizationDelayEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaReferenceTriggerSynchronizationDelayEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaReferenceTriggerSynchronizationDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaReferenceTriggerSynchronizationDistributionLine, obj: object) -> bool
        Equals(self: RfsaReferenceTriggerSynchronizationDistributionLine, source: RfsaReferenceTriggerSynchronizationDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaReferenceTriggerSynchronizationDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaReferenceTriggerSynchronizationDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaReferenceTriggerSynchronizationDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    PxiTrig0 = None
    PxiTrig1 = None
    PxiTrig2 = None
    PxiTrig3 = None
    PxiTrig4 = None
    PxiTrig5 = None
    PxiTrig6 = None
    PxiTrig7 = None


class RfsaReferenceTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaReferenceTriggerType, values: DigitalEdge (601), IQAnalogEdge (605), IQPowerEdge (603), None (600), SoftwareEdge (604) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    IQAnalogEdge = None
    IQPowerEdge = None
    None = None
    SoftwareEdge = None
    value__ = None


class RfsaResetStepsToOmit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaResetStepsToOmit, values: DeembeddingTables (2), None (0), Routes (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DeembeddingTables = None
    None = None
    Routes = None
    value__ = None


class RfsaResolutionBandwidthType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaResolutionBandwidthType, values: Rbw3dB (300), Rbw6dB (301), RbwBinWidth (302), RbwEnbw (303) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Rbw3dB = None
    Rbw6dB = None
    RbwBinWidth = None
    RbwEnbw = None
    value__ = None


class RfsaRevisionQueryResult(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaRevisionQueryResult, obj: object) -> bool
        Equals(self: RfsaRevisionQueryResult, result: RfsaRevisionQueryResult) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaRevisionQueryResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    FirmwareRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirmwareRevision(self: RfsaRevisionQueryResult) -> str

"""

    InstrumentRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentRevision(self: RfsaRevisionQueryResult) -> str

"""



class RfsaRFOutLOExportEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaRFOutLOExportEnabled, values: Disabled (1900), Enabled (1901), Unspecified (1902) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Unspecified = None
    value__ = None


class RfsaRFPreamplifierEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaRFPreamplifierEnabled, values: Automatic (2503), Disabled (2500), Enabled (2502), EnabledWhenInSignalPath (2501) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    EnabledWhenInSignalPath = None
    value__ = None


class RfsaRFPreselectorFilter(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaRFPreselectorFilter, values: External (3317), None (3300), Path1 (3301), Path10 (3310), Path11 (3311), Path12 (3312), Path13 (3313), Path14 (3314), Path15 (3315), Path16 (3316), Path2 (3302), Path3 (3303), Path4 (3304), Path5 (3305), Path6 (3306), Path7 (3307), Path8 (3308), Path9 (3309) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    External = None
    None = None
    Path1 = None
    Path10 = None
    Path11 = None
    Path12 = None
    Path13 = None
    Path14 = None
    Path15 = None
    Path16 = None
    Path2 = None
    Path3 = None
    Path4 = None
    Path5 = None
    Path6 = None
    Path7 = None
    Path8 = None
    Path9 = None
    value__ = None


class RfsaSelfCalibration(RfsaSubObject):
    # no doc
    def ClearSelfCalibrateRange(self):
        """ ClearSelfCalibrateRange(self: RfsaSelfCalibration) """
        pass

    def GetSelfCalibrationLastDateAndTime(self, selfCalibrationStep):
        """ GetSelfCalibrationLastDateAndTime(self: RfsaSelfCalibration, selfCalibrationStep: RfsaSelfCalibrationSteps) -> DateTime """
        pass

    def GetSelfCalibrationLastTemp(self, selfCalibrationStep):
        """ GetSelfCalibrationLastTemp(self: RfsaSelfCalibration, selfCalibrationStep: RfsaSelfCalibrationSteps) -> float """
        pass

    def IsSelfCalibrationValid(self, validSteps=None):
        """
        IsSelfCalibrationValid(self: RfsaSelfCalibration) -> bool
        IsSelfCalibrationValid(self: RfsaSelfCalibration) -> (bool, RfsaSelfCalibrationSteps)
        """
        pass

    def SelfCalibrate(self, stepsToOmit):
        """ SelfCalibrate(self: RfsaSelfCalibration, stepsToOmit: RfsaSelfCalibrationSteps) """
        pass

    def SelfCalibrateRange(self, stepsToOmit, minimumFrequency, maximumFrequency, minimumReferenceLevel, maximumReferenceLevel):
        """ SelfCalibrateRange(self: RfsaSelfCalibration, stepsToOmit: RfsaSelfCalibrationSteps, minimumFrequency: float, maximumFrequency: float, minimumReferenceLevel: float, maximumReferenceLevel: float) """
        pass

    CalibrationToneFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationToneFrequency(self: RfsaSelfCalibration) -> float

Set: CalibrationToneFrequency(self: RfsaSelfCalibration) = value
"""

    CalibrationToneMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalibrationToneMode(self: RfsaSelfCalibration) -> RfsaNISelfCalibrationToneMode

Set: CalibrationToneMode(self: RfsaSelfCalibration) = value
"""

    Correction100MhzFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Correction100MhzFilter(self: RfsaSelfCalibration) -> float

Set: Correction100MhzFilter(self: RfsaSelfCalibration) = value
"""

    Correction300KhzFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Correction300KhzFilter(self: RfsaSelfCalibration) -> float

Set: Correction300KhzFilter(self: RfsaSelfCalibration) = value
"""

    Correction320MhzFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Correction320MhzFilter(self: RfsaSelfCalibration) -> float

Set: Correction320MhzFilter(self: RfsaSelfCalibration) = value
"""

    Correction5MhzFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Correction5MhzFilter(self: RfsaSelfCalibration) -> float

Set: Correction5MhzFilter(self: RfsaSelfCalibration) = value
"""

    Correction765MhzFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Correction765MhzFilter(self: RfsaSelfCalibration) -> float

Set: Correction765MhzFilter(self: RfsaSelfCalibration) = value
"""

    CorrectionThroughFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorrectionThroughFilter(self: RfsaSelfCalibration) -> float

Set: CorrectionThroughFilter(self: RfsaSelfCalibration) = value
"""

    DownconverterCalibrationToneFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterCalibrationToneFrequency(self: RfsaSelfCalibration) -> float

Set: DownconverterCalibrationToneFrequency(self: RfsaSelfCalibration) = value
"""

    DownconverterCalibrationToneMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterCalibrationToneMode(self: RfsaSelfCalibration) -> RfsaSelfCalibrationDownconverterToneMode

Set: DownconverterCalibrationToneMode(self: RfsaSelfCalibration) = value
"""

    NI5693 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5693(self: RfsaSelfCalibration) -> RfsaNI5693SelfCalibration

"""



class RfsaSelfCalibrationDownconverterToneMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaSelfCalibrationDownconverterToneMode, values: CombGenerator (2705), Disabled (2700), HighbandIF (2703), HighbandRF (2702), LowbandRF (2701), LowbandRFWithoutAlc (2704) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CombGenerator = None
    Disabled = None
    HighbandIF = None
    HighbandRF = None
    LowbandRF = None
    LowbandRFWithoutAlc = None
    value__ = None


class RfsaSelfCalibrationSteps(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RfsaSelfCalibrationSteps, values: AmplitudeAccuracy (32), DCOffset (512), DigitizerSelfCalibration (8), GainReference (2), IFFlatness (4), ImageSuppression (128), LOSelfCalibration (16), None (0), PreselectorAlignment (1), PreSelectorAlignment (1), ResidualLOPower (64), SynthesizerAlignment (256) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    DigitizerSelfCalibration = None
    GainReference = None
    IFFlatness = None
    ImageSuppression = None
    LOSelfCalibration = None
    None = None
    PreselectorAlignment = None
    PreSelectorAlignment = None
    ResidualLOPower = None
    SynthesizerAlignment = None
    value__ = None


class RfsaSelfTestResult(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaSelfTestResult, obj: object) -> bool
        Equals(self: RfsaSelfTestResult, result: RfsaSelfTestResult) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaSelfTestResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: RfsaSelfTestResult) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: RfsaSelfTestResult) -> str

"""



class RfsaSignalConditioningEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaSignalConditioningEnabled, values: Bypassed (3601), Enabled (3600) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Bypassed = None
    Enabled = None
    value__ = None


class RfsaSignalPath(RfsaSubObject):
    # no doc
    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaSignalPath) -> RfsaAdvancedSignalPath

"""

    AvailablePorts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AvailablePorts(self: RfsaSignalPath) -> str

"""

    DigitalIFEqualizationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalIFEqualizationEnabled(self: RfsaSignalPath) -> bool

Set: DigitalIFEqualizationEnabled(self: RfsaSignalPath) = value
"""

    DigitizerDitherEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitizerDitherEnabled(self: RfsaSignalPath) -> RfsaDigitizerDitherEnabled

Set: DigitizerDitherEnabled(self: RfsaSignalPath) = value
"""

    DigitizerVerticalRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitizerVerticalRange(self: RfsaSignalPath) -> float

Set: DigitizerVerticalRange(self: RfsaSignalPath) = value
"""

    EnableFractionalResampling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableFractionalResampling(self: RfsaSignalPath) -> bool

Set: EnableFractionalResampling(self: RfsaSignalPath) = value
"""

    IFFilterBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFFilterBandwidth(self: RfsaSignalPath) -> float

Set: IFFilterBandwidth(self: RfsaSignalPath) = value
"""

    LO2ExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LO2ExportEnabled(self: RfsaSignalPath) -> bool

Set: LO2ExportEnabled(self: RfsaSignalPath) = value
"""

    LocalOscillator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalOscillator(self: RfsaSignalPath) -> RfsaLocalOscillator

"""

    LOExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOExportEnabled(self: RfsaSignalPath) -> bool

Set: LOExportEnabled(self: RfsaSignalPath) = value
"""

    LOFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequency(self: RfsaSignalPath) -> float

Set: LOFrequency(self: RfsaSignalPath) = value
"""

    LOOutExportConfigureFromRfsg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutExportConfigureFromRfsg(self: RfsaSignalPath) -> RfsaLOOutExportConfigureFromRfsg

Set: LOOutExportConfigureFromRfsg(self: RfsaSignalPath) = value
"""

    LOSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LOSource(self: RfsaSignalPath) -> RfsaLOSource

Set: LOSource(self: RfsaSignalPath) = value
"""

    NI5663 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5663(self: RfsaSignalPath) -> RfsaNI5663SignalPath

"""

    NI5665 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5665(self: RfsaSignalPath) -> RfsaNI5665SignalPath

"""

    NI5694 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NI5694(self: RfsaSignalPath) -> RfsaNI5694SignalPath

"""

    RFOutLOExportEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RFOutLOExportEnabled(self: RfsaSignalPath) -> RfsaRFOutLOExportEnabled

Set: RFOutLOExportEnabled(self: RfsaSignalPath) = value
"""

    SelectedPorts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedPorts(self: RfsaSignalPath) -> str

Set: SelectedPorts(self: RfsaSignalPath) = value
"""



class RfsaSmoothSpectrumEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaSmoothSpectrumEnabled, values: Disabled (1900), Enabled (1901) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaSParameterOrientation(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaSParameterOrientation, values: Port1TowardsDut (3800), Port2TowardsDut (3801) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaSpectrumAcquisition(RfsaSubObject):
    # no doc
    def MemoryOptimizedReadPowerSpectrum(self, timeout, data, spectrumInfo=None):
        """
        MemoryOptimizedReadPowerSpectrum(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan, data: Array[float]) -> (Array[float], Array[float])
        MemoryOptimizedReadPowerSpectrum(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan, data: Array[float]) -> (Array[float], Array[float], RfsaSpectrumInfo)
        MemoryOptimizedReadPowerSpectrum(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan, data: Array[Single]) -> (Array[Single], Array[Single])
        MemoryOptimizedReadPowerSpectrum(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan, data: Array[Single]) -> (Array[Single], Array[Single], RfsaSpectrumInfo)
        """
        pass

    def ReadPowerSpectrum(self, timeout, spectrumInfo=None):
        """
        ReadPowerSpectrum(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan) -> Array[float]
        ReadPowerSpectrum(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan) -> (Array[float], RfsaSpectrumInfo)
        """
        pass

    def ReadPowerSpectrumSingle(self, timeout, spectrumInfo=None):
        """
        ReadPowerSpectrumSingle(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan) -> (Array[Single], RfsaSpectrumInfo)
        ReadPowerSpectrumSingle(self: RfsaSpectrumAcquisition, timeout: PrecisionTimeSpan) -> Array[Single]
        """
        pass


class RfsaSpectrumAcquisitionConfiguration(RfsaSubObject):
    # no doc
    def ConfigureSpectrumFrequencyCenterSpan(self, centerFrequency, span):
        """ ConfigureSpectrumFrequencyCenterSpan(self: RfsaSpectrumAcquisitionConfiguration, centerFrequency: float, span: float) """
        pass

    def ConfigureSpectrumFrequencyStartStop(self, startFrequency, stopFrequency):
        """ ConfigureSpectrumFrequencyStartStop(self: RfsaSpectrumAcquisitionConfiguration, startFrequency: float, stopFrequency: float) """
        pass

    AveragingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AveragingMode(self: RfsaSpectrumAcquisitionConfiguration) -> RfsaSpectrumAveragingMode

Set: AveragingMode(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    CenterFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterFrequency(self: RfsaSpectrumAcquisitionConfiguration) -> float

Set: CenterFrequency(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    FftSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FftSize(self: RfsaSpectrumAcquisitionConfiguration) -> int

"""

    FftWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FftWidth(self: RfsaSpectrumAcquisitionConfiguration) -> float

Set: FftWidth(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    FftWindowShapeFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FftWindowShapeFactor(self: RfsaSpectrumAcquisitionConfiguration) -> float

"""

    FftWindowSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FftWindowSize(self: RfsaSpectrumAcquisitionConfiguration) -> int

"""

    FftWindowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FftWindowType(self: RfsaSpectrumAcquisitionConfiguration) -> RfsaFftWindowType

Set: FftWindowType(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    NumberOfAverages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfAverages(self: RfsaSpectrumAcquisitionConfiguration) -> int

Set: NumberOfAverages(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    NumberOfSpectralLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSpectralLines(self: RfsaSpectrumAcquisitionConfiguration) -> int

Set: NumberOfSpectralLines(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    PowerSpectrumUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerSpectrumUnits(self: RfsaSpectrumAcquisitionConfiguration) -> RfsaPowerSpectrumUnits

Set: PowerSpectrumUnits(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    ResolutionBandwidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResolutionBandwidth(self: RfsaSpectrumAcquisitionConfiguration) -> float

Set: ResolutionBandwidth(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    ResolutionBandwidthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResolutionBandwidthType(self: RfsaSpectrumAcquisitionConfiguration) -> RfsaResolutionBandwidthType

Set: ResolutionBandwidthType(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    SmoothSpectrumEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothSpectrumEnabled(self: RfsaSpectrumAcquisitionConfiguration) -> RfsaSmoothSpectrumEnabled

Set: SmoothSpectrumEnabled(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    Span = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Span(self: RfsaSpectrumAcquisitionConfiguration) -> float

Set: Span(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    SpectrumOspSamplingRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpectrumOspSamplingRatio(self: RfsaSpectrumAcquisitionConfiguration) -> float

Set: SpectrumOspSamplingRatio(self: RfsaSpectrumAcquisitionConfiguration) = value
"""

    SubspanOverlap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubspanOverlap(self: RfsaSpectrumAcquisitionConfiguration) -> float

Set: SubspanOverlap(self: RfsaSpectrumAcquisitionConfiguration) = value
"""



class RfsaSpectrumAveragingMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaSpectrumAveragingMode, values: Log (406), MinimumHold (404), None (400), PeakHold (403), Rms (401), Scalar (405), Vector (402) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    MinimumHold = None
    None = None
    PeakHold = None
    Rms = None
    Scalar = None
    value__ = None
    Vector = None


class RfsaSpectrumInfo(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaSpectrumInfo, obj: object) -> bool
        Equals(self: RfsaSpectrumInfo, spectrumInfo: RfsaSpectrumInfo) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaSpectrumInfo) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    FrequencyIncrement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyIncrement(self: RfsaSpectrumInfo) -> float

"""

    InitialFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialFrequency(self: RfsaSpectrumInfo) -> float

"""

    NumberOfSpectralLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfSpectralLines(self: RfsaSpectrumInfo) -> int

"""

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved1(self: RfsaSpectrumInfo) -> float

"""

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved2(self: RfsaSpectrumInfo) -> float

"""

    Reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved3(self: RfsaSpectrumInfo) -> float

"""

    Reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved4(self: RfsaSpectrumInfo) -> float

"""

    Reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved5(self: RfsaSpectrumInfo) -> float

"""



class RfsaStartTrigger(RfsaSubObject):
    # no doc
    def Disable(self):
        """ Disable(self: RfsaStartTrigger) """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RfsaStartTrigger) """
        pass

    DigitalEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsaStartTrigger) -> RfsaDigitalEdgeStartTrigger

"""

    Export = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Export(self: RfsaStartTrigger) -> RfsaExportStartTrigger

"""

    Synchronization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronization(self: RfsaStartTrigger) -> RfsaStartTriggerSynchronization

"""

    TerminalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsaStartTrigger) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RfsaStartTrigger) -> RfsaStartTriggerType

Set: Type(self: RfsaStartTrigger) = value
"""



class RfsaStartTriggerSynchronization(RfsaSubObject):
    # no doc
    DistributionLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionLine(self: RfsaStartTriggerSynchronization) -> RfsaStartTriggerSynchronizationDistributionLine

Set: DistributionLine(self: RfsaStartTriggerSynchronization) = value
"""

    IsMaster = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMaster(self: RfsaStartTriggerSynchronization) -> bool

Set: IsMaster(self: RfsaStartTriggerSynchronization) = value
"""



class RfsaStartTriggerSynchronizationDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaStartTriggerSynchronizationDistributionLine, obj: object) -> bool
        Equals(self: RfsaStartTriggerSynchronizationDistributionLine, source: RfsaStartTriggerSynchronizationDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaStartTriggerSynchronizationDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaStartTriggerSynchronizationDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaStartTriggerSynchronizationDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    PxiTrig0 = None
    PxiTrig1 = None
    PxiTrig2 = None
    PxiTrig3 = None
    PxiTrig4 = None
    PxiTrig5 = None
    PxiTrig6 = None
    PxiTrig7 = None


class RfsaStartTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaStartTriggerType, values: DigitalEdge (601), None (600), SoftwareEdge (604) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    None = None
    SoftwareEdge = None
    value__ = None


class RfsaStepGainEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaStepGainEnabled, values: Disabled (3200), Enabled (3201) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaTimerStartSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaTimerStartSource, obj: object) -> bool
        Equals(self: RfsaTimerStartSource, source: RfsaTimerStartSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsaTimerStartSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaTimerStartSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaTimerStartSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ReferenceTrigger = None
    StartTrigger = None


class RfsaTriggerEdge(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsaTriggerEdge, values: Falling (901), Rising (900) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsaTriggers(RfsaSubObject):
    # no doc
    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaTriggers) -> RfsaAdvancedTrigger

"""

    AdvanceTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdvanceTrigger(self: RfsaTriggers) -> RfsaAdvanceTrigger

"""

    ArmReferenceTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArmReferenceTrigger(self: RfsaTriggers) -> RfsaArmReferenceTrigger

"""

    ConfigurationListStepTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationListStepTrigger(self: RfsaTriggers) -> RfsaConfigurationListStepTrigger

"""

    ReferenceTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceTrigger(self: RfsaTriggers) -> RfsaReferenceTrigger

"""

    StartTrigger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartTrigger(self: RfsaTriggers) -> RfsaStartTrigger

"""



class RfsaVertical(RfsaSubObject):
    # no doc
    Advanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsaVertical) -> RfsaAdvancedVertical

"""

    DownconverterGain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownconverterGain(self: RfsaVertical) -> float

Set: DownconverterGain(self: RfsaVertical) = value
"""

    IFOutputPowerLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFOutputPowerLevel(self: RfsaVertical) -> float

Set: IFOutputPowerLevel(self: RfsaVertical) = value
"""

    IFOutputPowerLevelOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IFOutputPowerLevelOffset(self: RfsaVertical) -> float

Set: IFOutputPowerLevelOffset(self: RfsaVertical) = value
"""

    MixerLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MixerLevel(self: RfsaVertical) -> float

Set: MixerLevel(self: RfsaVertical) = value
"""

    MixerLevelOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MixerLevelOffset(self: RfsaVertical) -> float

Set: MixerLevelOffset(self: RfsaVertical) = value
"""

    ReferenceLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceLevel(self: RfsaVertical) -> float

Set: ReferenceLevel(self: RfsaVertical) = value
"""



class RfsaWarning(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaWarning, obj: object) -> bool
        Equals(self: RfsaWarning, warning: RfsaWarning) -> bool
        Equals(self: RfsaWarning, warning: RfsaWarning, ignoreWarningMessage: bool) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaWarning) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsaWarning) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: RfsaWarning) -> Guid

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: RfsaWarning) -> str

"""


    AttenuationConstraintsNotCalibratedWarningCode = None
    CacheNotSufficientToStoreAcquiredWaveformWarningCode = None
    CalibrationDataMissingOrInvalidWarningCode = None
    CalibrationIFEqualizationDataNotPresentWarningCode = None
    CenterFrequencyOutsideSpecificationWarningCode = None
    CurrentChannelCouplingConfigurationNotCalibratedWarningCode = None
    DigitizerPllWarningCode = None
    DigitizerWarningCode = None
    DspOverflowWarningCode = None
    ErrorQueryNotSupportedWarningCode = None
    ExternalCalibrationConstantsInvalidWarningCode = None
    ExternalCalibrationDataFormatInvalidWarningCode = None
    ExternalCalibrationDataTooNewForSoftwareWarningCode = None
    FrequencyContentOutsideSpecificationWarningCode = None
    IFConditioningDeviceWarningCode = None
    IFOverloadProtectionNeedToBeCalibratedWarningCode = None
    IFStateNotPresentWarningCode = None
    LOWarningCode = None
    ReferenceClockPllNotLockedWarningCode = None
    RFConditioningDeviceWarningCode = None
    RFConfigurationNotValidWarningCode = None
    SelfCalibrationOffsetOutOfBoundsWarningCode = None
    TemperatureDeviationLimitExceededWarningCode = None
    UnexpectedDriverWarningCode = None


class RfsaWarningEventArgs(EventArgs):
    # no doc
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: RfsaWarningEventArgs) -> Guid

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: RfsaWarningEventArgs) -> str

"""

    Warning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Warning(self: RfsaWarningEventArgs) -> RfsaWarning

"""



class RfsaWaveformInfo(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsaWaveformInfo, obj: object) -> bool
        Equals(self: RfsaWaveformInfo, waveformInfo: RfsaWaveformInfo) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsaWaveformInfo) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AbsoluteInitialX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsoluteInitialX(self: RfsaWaveformInfo) -> float

"""

    ActualSamples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualSamples(self: RfsaWaveformInfo) -> Int64

"""

    Gain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gain(self: RfsaWaveformInfo) -> float

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: RfsaWaveformInfo) -> float

"""

    RelativeInitialX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeInitialX(self: RfsaWaveformInfo) -> float

"""

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved1(self: RfsaWaveformInfo) -> float

"""

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reserved2(self: RfsaWaveformInfo) -> float

"""

    XIncrement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XIncrement(self: RfsaWaveformInfo) -> float

"""



