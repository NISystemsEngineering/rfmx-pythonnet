# encoding: utf-8
# module NationalInstruments.ModularInstruments.NIRfsg calls itself NIRfsg
# from NationalInstruments.ModularInstruments.NIRfsg.Fx40, Version=19.1.0.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class NIRfsg(object, IDisposable, IServiceProvider, IIviDriver, ITClockSynchronizableDevice):
    """
    NIRfsg(resourceName: str, idQuery: bool, reset: bool)

    NIRfsg(resourceName: str, idQuery: bool, reset: bool, optionString: str)

    NIRfsg(instrumentHandle: IntPtr)
    """
    def Abort(self):
        """ Abort(self: NIRfsg) """
        pass

    def CheckGenerationStatus(self):
        """ CheckGenerationStatus(self: NIRfsg) -> RfsgGenerationStatus """
        pass

    def Close(self):
        """ Close(self: NIRfsg) """
        pass

    def DangerousGetInstrumentHandle(self):
        """ DangerousGetInstrumentHandle(self: NIRfsg) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: NIRfsg) """
        pass

    def GetInstrumentHandle(self):
        """ GetInstrumentHandle(self: NIRfsg) -> SafeHandle """
        pass

    def GetService(self, serviceType):
        """ GetService(self: NIRfsg, serviceType: Type) -> object """
        pass

    def Initiate(self):
        """ Initiate(self: NIRfsg) """
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
        __new__(cls: type, resourceName: str, idQuery: bool, reset: bool)

        __new__(cls: type, resourceName: str, idQuery: bool, reset: bool, optionString: str)

        __new__(cls: type, instrumentHandle: IntPtr)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Arb = property(lambda self: RfsgArb(), lambda self, v: None, lambda self: None)  # default
    """Get: Arb(self: NIRfsg) -> RfsgArb



"""

    ArbSampleClock = property(lambda self: RfsgArbSampleClock(), lambda self, v: None, lambda self: None)  # default
    """Get: ArbSampleClock(self: NIRfsg) -> RfsgArbSampleClock



"""

    BasicConfigurationList = property(lambda self: RfsgBasicConfigurationList(), lambda self, v: None, lambda self: None)  # default
    """Get: BasicConfigurationList(self: NIRfsg) -> RfsgBasicConfigurationList



"""

    Calibration = property(lambda self: RfsgCalibration(), lambda self, v: None, lambda self: None)  # default
    """Get: Calibration(self: NIRfsg) -> RfsgCalibration



"""

    Deembedding = property(lambda self: RfsgDeembedding(), lambda self, v: None, lambda self: None)  # default
    """Get: Deembedding(self: NIRfsg) -> RfsgDeembedding



"""

    DeviceCharacteristics = property(lambda self: RfsgDeviceCharacteristics(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceCharacteristics(self: NIRfsg) -> RfsgDeviceCharacteristics



"""

    DeviceEvents = property(lambda self: RfsgDeviceEvents(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceEvents(self: NIRfsg) -> RfsgDeviceEvents



"""

    DriverIdentity = property(lambda self: RfsgDriverIdentity(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverIdentity(self: NIRfsg) -> RfsgDriverIdentity



"""

    DriverOperation = property(lambda self: RfsgDriverOperation(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverOperation(self: NIRfsg) -> RfsgDriverOperation



"""

    DriverUtility = property(lambda self: RfsgDriverUtility(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverUtility(self: NIRfsg) -> RfsgDriverUtility



"""

    ErrorInfoUtility = property(lambda self: RfsgErrorInfoUtility(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorInfoUtility(self: NIRfsg) -> RfsgErrorInfoUtility



"""

    FrequencyReference = property(lambda self: RfsgFrequencyReference(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyReference(self: NIRfsg) -> RfsgFrequencyReference



"""

    Identity = property(lambda self: RfsgDriverIdentity(), lambda self, v: None, lambda self: None)  # default
    """Get: Identity(self: NIRfsg) -> RfsgDriverIdentity



"""

    IQImpairments = property(lambda self: RfsgIQImpairment(), lambda self, v: None, lambda self: None)  # default
    """Get: IQImpairments(self: NIRfsg) -> RfsgIQImpairment



"""

    IQOutPort = property(lambda self: RfsgIQOutPort(), lambda self, v: None, lambda self: None)  # default
    """Get: IQOutPort(self: NIRfsg) -> RfsgIQOutPort



"""

    IsDisposed = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: NIRfsg) -> bool



"""

    Modulation = property(lambda self: RfsgModulation(), lambda self, v: None, lambda self: None)  # default
    """Get: Modulation(self: NIRfsg) -> RfsgModulation



"""

    RF = property(lambda self: RfsgRF(), lambda self, v: None, lambda self: None)  # default
    """Get: RF(self: NIRfsg) -> RfsgRF



"""

    SignalPath = property(lambda self: RfsgSignalPath(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalPath(self: NIRfsg) -> RfsgSignalPath



"""

    Triggers = property(lambda self: RfsgTriggers(), lambda self, v: None, lambda self: None)  # default
    """Get: Triggers(self: NIRfsg) -> RfsgTriggers



"""

    Utility = property(lambda self: RfsgDriverUtility(), lambda self, v: None, lambda self: None)  # default
    """Get: Utility(self: NIRfsg) -> RfsgDriverUtility



"""



class RfsgAlcControl(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAlcControl, values: Disable (0), Enable (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Disable = None
    Enable = None
    value__ = None


class RfsgAmplificationPath(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAmplificationPath, values: HighPower (16000), LowHarmonic (16001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HighPower = None
    LowHarmonic = None
    value__ = None


class RfsgSubObject(object):
    pass
    # no doc

class RfsgAnalogModulation(RfsgSubObject):
    # no doc
    AMSensitivity = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AMSensitivity(self: RfsgAnalogModulation) -> float



Set: AMSensitivity(self: RfsgAnalogModulation) = value

"""

    FMBand = property(lambda self: RfsgAnalogModulationFMBand(), lambda self, v: None, lambda self: None)  # default
    """Get: FMBand(self: RfsgAnalogModulation) -> RfsgAnalogModulationFMBand



Set: FMBand(self: RfsgAnalogModulation) = value

"""

    FMDeviation = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FMDeviation(self: RfsgAnalogModulation) -> float



Set: FMDeviation(self: RfsgAnalogModulation) = value

"""

    FMNarrowbandIntegrator = property(lambda self: RfsgAnalogModulationFMNarrowbandIntegrator(), lambda self, v: None, lambda self: None)  # default
    """Get: FMNarrowbandIntegrator(self: RfsgAnalogModulation) -> RfsgAnalogModulationFMNarrowbandIntegrator



Set: FMNarrowbandIntegrator(self: RfsgAnalogModulation) = value

"""

    FMSensitivity = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FMSensitivity(self: RfsgAnalogModulation) -> float



Set: FMSensitivity(self: RfsgAnalogModulation) = value

"""

    ModulationType = property(lambda self: RfsgAnalogModulationType(), lambda self, v: None, lambda self: None)  # default
    """Get: ModulationType(self: RfsgAnalogModulation) -> RfsgAnalogModulationType



Set: ModulationType(self: RfsgAnalogModulation) = value

"""

    PMDeviation = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PMDeviation(self: RfsgAnalogModulation) -> float



Set: PMDeviation(self: RfsgAnalogModulation) = value

"""

    PMMode = property(lambda self: RfsgAnalogModulationPMMode(), lambda self, v: None, lambda self: None)  # default
    """Get: PMMode(self: RfsgAnalogModulation) -> RfsgAnalogModulationPMMode



Set: PMMode(self: RfsgAnalogModulation) = value

"""

    PMSensitivity = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PMSensitivity(self: RfsgAnalogModulation) -> float



Set: PMSensitivity(self: RfsgAnalogModulation) = value

"""

    WaveformFrequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformFrequency(self: RfsgAnalogModulation) -> float



Set: WaveformFrequency(self: RfsgAnalogModulation) = value

"""

    WaveformType = property(lambda self: RfsgAnalogModulationWaveformType(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformType(self: RfsgAnalogModulation) -> RfsgAnalogModulationWaveformType



Set: WaveformType(self: RfsgAnalogModulation) = value

"""



class RfsgAnalogModulationFMBand(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAnalogModulationFMBand, values: Narrowband (17000), Wideband (17001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Narrowband = None
    value__ = None
    Wideband = None


class RfsgAnalogModulationFMNarrowbandIntegrator(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAnalogModulationFMNarrowbandIntegrator, values: FMNarrowband100HzTo1Khz (18000), FMNarrowband10KhzTo100Khz (18002), FMNarrowband1KhzTo10Khz (18001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FMNarrowband100HzTo1Khz = None
    FMNarrowband10KhzTo100Khz = None
    FMNarrowband1KhzTo10Khz = None
    value__ = None


class RfsgAnalogModulationPMMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAnalogModulationPMMode, values: HighDeviation (19000), LowPhaseNoise (19001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HighDeviation = None
    LowPhaseNoise = None
    value__ = None


class RfsgAnalogModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAnalogModulationType, values: AM (2002), FM (2000), None (0), PM (2001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AM = None
    FM = None
    None = None
    PM = None
    value__ = None


class RfsgAnalogModulationWaveformType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAnalogModulationWaveformType, values: Sine (3000), Square (3001), Triangle (3002) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Sine = None
    Square = None
    Triangle = None
    value__ = None


class RfsgArb(RfsgSubObject):
    # no doc
    def AllocateWaveform(self, name, sizeInSamples):
        """ AllocateWaveform(self: RfsgArb, name: str, sizeInSamples: int) """
        pass

    def CheckIfWaveformExists(self, waveformName):
        """ CheckIfWaveformExists(self: RfsgArb, waveformName: str) -> bool """
        pass

    def ClearAllWaveforms(self):
        """ ClearAllWaveforms(self: RfsgArb) """
        pass

    def ClearWaveform(self, name):
        """ ClearWaveform(self: RfsgArb, name: str) """
        pass

    def SetArbWaveformNextWritePosition(self, name, relativeTo, offset):
        """ SetArbWaveformNextWritePosition(self: RfsgArb, name: str, relativeTo: RfsgArbWaveformRelativeWritePosition, offset: int) """
        pass

    def WriteWaveform(self, name, *__args):
        """ WriteWaveform(self: RfsgArb, name: str, iData: Array[float], qData: Array[float])WriteWaveform[T](self: RfsgArb, name: str, data: ComplexWaveform[T])WriteWaveform(self: RfsgArb, name: str, data: ComplexWaveform[ComplexDouble])WriteWaveform(self: RfsgArb, name: str, data: ComplexWaveform[ComplexInt16])WriteWaveform[T](self: RfsgArb, name: str, data: Array[T])WriteWaveform(self: RfsgArb, name: str, data: Array[ComplexDouble])WriteWaveform(self: RfsgArb, name: str, data: Array[ComplexInt16])WriteWaveform(self: RfsgArb, name: str, data: Array[ComplexSingle])WriteWaveform(self: RfsgArb, name: str, data: ComplexWaveform[ComplexSingle]) """
        pass

    AbsoluteDelay = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsoluteDelay(self: RfsgArb) -> float



Set: AbsoluteDelay(self: RfsgArb) = value

"""

    CarrierFrequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: CarrierFrequency(self: RfsgArb) -> float



Set: CarrierFrequency(self: RfsgArb) = value

"""

    DataTransfer = property(lambda self: RfsgDataTransfer(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTransfer(self: RfsgArb) -> RfsgDataTransfer



"""

    DeviceInstantaneousBandwidth = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceInstantaneousBandwidth(self: RfsgArb) -> float



Set: DeviceInstantaneousBandwidth(self: RfsgArb) = value

"""

    DigitalEqualizationEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEqualizationEnabled(self: RfsgArb) -> bool



Set: DigitalEqualizationEnabled(self: RfsgArb) = value

"""

    DigitalGain = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalGain(self: RfsgArb) -> float



Set: DigitalGain(self: RfsgArb) = value

"""

    DigitalPatternEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalPatternEnabled(self: RfsgArb) -> bool



Set: DigitalPatternEnabled(self: RfsgArb) = value

"""

    GenerationMode = property(lambda self: RfsgWaveformGenerationMode(), lambda self, v: None, lambda self: None)  # default
    """Get: GenerationMode(self: RfsgArb) -> RfsgWaveformGenerationMode



Set: GenerationMode(self: RfsgArb) = value

"""

    InterpolationDelay = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: InterpolationDelay(self: RfsgArb) -> float



Set: InterpolationDelay(self: RfsgArb) = value

"""

    IQRate = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: IQRate(self: RfsgArb) -> float



Set: IQRate(self: RfsgArb) = value

"""

    IQSwapEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IQSwapEnabled(self: RfsgArb) -> bool



Set: IQSwapEnabled(self: RfsgArb) = value

"""

    IsWaveformRepeatCountFinite = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWaveformRepeatCountFinite(self: RfsgArb) -> bool



Set: IsWaveformRepeatCountFinite(self: RfsgArb) = value

"""

    MemorySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemorySize(self: RfsgArb) -> Int64



"""

    OutputPort = property(lambda self: RfsgOutputPort(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputPort(self: RfsgArb) -> RfsgOutputPort



Set: OutputPort(self: RfsgArb) = value

"""

    OverflowErrorReporting = property(lambda self: RfsgOverflowErrorReporting(), lambda self, v: None, lambda self: None)  # default
    """Get: OverflowErrorReporting(self: RfsgArb) -> RfsgOverflowErrorReporting



Set: OverflowErrorReporting(self: RfsgArb) = value

"""

    PhaseContinuityEnabled = property(lambda self: RfsgPhaseContinuityEnabled(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseContinuityEnabled(self: RfsgArb) -> RfsgPhaseContinuityEnabled



Set: PhaseContinuityEnabled(self: RfsgArb) = value

"""

    Power = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Power(self: RfsgArb) -> float



"""

    PreFilterGain = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PreFilterGain(self: RfsgArb) -> float



Set: PreFilterGain(self: RfsgArb) = value

"""

    PulseShaping = property(lambda self: RfsgPulseShaping(), lambda self, v: None, lambda self: None)  # default
    """Get: PulseShaping(self: RfsgArb) -> RfsgPulseShaping



"""

    RelativeDelay = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeDelay(self: RfsgArb) -> float



Set: RelativeDelay(self: RfsgArb) = value

"""

    Scripting = property(lambda self: RfsgScripting(), lambda self, v: None, lambda self: None)  # default
    """Get: Scripting(self: RfsgArb) -> RfsgScripting



"""

    SelectedWaveform = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedWaveform(self: RfsgArb) -> str



Set: SelectedWaveform(self: RfsgArb) = value

"""

    SignalBandwidth = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalBandwidth(self: RfsgArb) -> float



Set: SignalBandwidth(self: RfsgArb) = value

"""

    WaveformCapabilities = property(lambda self: RfsgWaveformCapabilities(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformCapabilities(self: RfsgArb) -> RfsgWaveformCapabilities



"""

    WaveformRepeatCount = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformRepeatCount(self: RfsgArb) -> int



Set: WaveformRepeatCount(self: RfsgArb) = value

"""

    WaveformSoftwareScalingFactor = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformSoftwareScalingFactor(self: RfsgArb) -> float



Set: WaveformSoftwareScalingFactor(self: RfsgArb) = value

"""



class RfsgArbSampleClock(RfsgSubObject):
    # no doc
    OnboardClockMode = property(lambda self: RfsgOnboardSampleClockMode(), lambda self, v: None, lambda self: None)  # default
    """Get: OnboardClockMode(self: RfsgArbSampleClock) -> RfsgOnboardSampleClockMode



Set: OnboardClockMode(self: RfsgArbSampleClock) = value

"""

    OscillatorPhaseDacValue = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: OscillatorPhaseDacValue(self: RfsgArbSampleClock) -> int



Set: OscillatorPhaseDacValue(self: RfsgArbSampleClock) = value

"""

    Rate = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Rate(self: RfsgArbSampleClock) -> float



"""

    Source = property(lambda self: RfsgArbSampleClockSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgArbSampleClock) -> RfsgArbSampleClockSource



Set: Source(self: RfsgArbSampleClock) = value

"""

    Synchronized = property(lambda self: RfsgSynchronizedSampleClock(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronized(self: RfsgArbSampleClock) -> RfsgSynchronizedSampleClock



"""



class RfsgArbSampleClockSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgArbSampleClockSource, obj: object) -> bool

        Equals(self: RfsgArbSampleClockSource, source: RfsgArbSampleClockSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgArbSampleClockSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgArbSampleClockSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgArbSampleClockSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockIn = None
    OnboardClock = None


class RfsgArbWaveformRelativeWritePosition(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgArbWaveformRelativeWritePosition, values: CurrentPosition (8001), StartOfWaveform (8000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CurrentPosition = None
    StartOfWaveform = None
    value__ = None


class RfsgAutoPowerSearch(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgAutoPowerSearch, values: Disable (0), Enable (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Disable = None
    Enable = None
    value__ = None


class RfsgBasicConfigurationList(RfsgSubObject):
    # no doc
    def CheckIfConfigurationListExists(self, listName):
        """ CheckIfConfigurationListExists(self: RfsgBasicConfigurationList, listName: str) -> bool """
        pass

    def CreateConfigurationList(self, listName, propertiesToSet, setAsActiveList):
        """ CreateConfigurationList(self: RfsgBasicConfigurationList, listName: str, propertiesToSet: Array[RfsgConfigurationListProperties], setAsActiveList: bool) """
        pass

    def CreateStep(self, setAsActiveStep):
        """ CreateStep(self: RfsgBasicConfigurationList, setAsActiveStep: bool) """
        pass

    def DeleteConfigurationList(self, listName):
        """ DeleteConfigurationList(self: RfsgBasicConfigurationList, listName: str) """
        pass

    ActiveList = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveList(self: RfsgBasicConfigurationList) -> str



Set: ActiveList(self: RfsgBasicConfigurationList) = value

"""

    ActiveStep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveStep(self: RfsgBasicConfigurationList) -> Int64



Set: ActiveStep(self: RfsgBasicConfigurationList) = value

"""

    IsDone = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDone(self: RfsgBasicConfigurationList) -> bool



"""

    Repeat = property(lambda self: RfsgBasicConfigurationListRepeat(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: RfsgBasicConfigurationList) -> RfsgBasicConfigurationListRepeat



Set: Repeat(self: RfsgBasicConfigurationList) = value

"""

    StepInProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StepInProgress(self: RfsgBasicConfigurationList) -> Int64



"""



class RfsgBasicConfigurationListRepeat(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgBasicConfigurationListRepeat, values: Continuous (0), Single (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Continuous = None
    Single = None
    value__ = None


class RfsgCalibration(RfsgSubObject):
    # no doc
    Self = property(lambda self: RfsgSelfCalibration(), lambda self, v: None, lambda self: None)  # default
    """Get: Self(self: RfsgCalibration) -> RfsgSelfCalibration



"""



class RfsgChannelBasedDeembedding(RfsgSubObject):
    # no doc
    def ConfigureDeembeddingTableInterpolationLinear(self, tableName, format):
        """ ConfigureDeembeddingTableInterpolationLinear(self: RfsgChannelBasedDeembedding, tableName: str, format: RfsgLinearInterpolationFormat) """
        pass

    def ConfigureDeembeddingTableInterpolationNearest(self, tableName):
        """ ConfigureDeembeddingTableInterpolationNearest(self: RfsgChannelBasedDeembedding, tableName: str) """
        pass

    def ConfigureDeembeddingTableInterpolationSpline(self, tableName):
        """ ConfigureDeembeddingTableInterpolationSpline(self: RfsgChannelBasedDeembedding, tableName: str) """
        pass

    def CreateDeembeddingSParameterTableArray(self, tableName, frequencies, sParameterTable, sParameterOrientation):
        """ CreateDeembeddingSParameterTableArray(self: RfsgChannelBasedDeembedding, tableName: str, frequencies: Array[float], sParameterTable: Array[ComplexDouble], sParameterOrientation: RfsgSParameterOrientation) """
        pass

    def CreateDeembeddingSParameterTableS2pFile(self, tableName, s2pFilePath, sParameterOrientation):
        """ CreateDeembeddingSParameterTableS2pFile(self: RfsgChannelBasedDeembedding, tableName: str, s2pFilePath: str, sParameterOrientation: RfsgSParameterOrientation) """
        pass

    def DeleteDeembeddingTable(self, tableName):
        """ DeleteDeembeddingTable(self: RfsgChannelBasedDeembedding, tableName: str) """
        pass

    DeembeddingSelectedTable = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingSelectedTable(self: RfsgChannelBasedDeembedding) -> str



Set: DeembeddingSelectedTable(self: RfsgChannelBasedDeembedding) = value

"""

    DeembeddingType = property(lambda self: RfsgDeembeddingType(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingType(self: RfsgChannelBasedDeembedding) -> RfsgDeembeddingType



Set: DeembeddingType(self: RfsgChannelBasedDeembedding) = value

"""



class RfsgChannelBasedDeviceCharacteristics(RfsgSubObject):
    # no doc
    DeviceTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceTemperature(self: RfsgChannelBasedDeviceCharacteristics) -> float



"""



class RfsgChannelBasedIQOutPort(RfsgSubObject):
    # no doc
    CommonModeOffset = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: CommonModeOffset(self: RfsgChannelBasedIQOutPort) -> float



Set: CommonModeOffset(self: RfsgChannelBasedIQOutPort) = value

"""

    Level = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: RfsgChannelBasedIQOutPort) -> float



Set: Level(self: RfsgChannelBasedIQOutPort) = value

"""

    LoadImpedance = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadImpedance(self: RfsgChannelBasedIQOutPort) -> float



Set: LoadImpedance(self: RfsgChannelBasedIQOutPort) = value

"""

    Offset = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: RfsgChannelBasedIQOutPort) -> float



Set: Offset(self: RfsgChannelBasedIQOutPort) = value

"""

    TerminalConfiguration = property(lambda self: RfsgTerminalConfiguration(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalConfiguration(self: RfsgChannelBasedIQOutPort) -> RfsgTerminalConfiguration



Set: TerminalConfiguration(self: RfsgChannelBasedIQOutPort) = value

"""



class RfsgChannelBasedLO(RfsgSubObject):
    # no doc
    LOFrequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequency(self: RfsgChannelBasedLO) -> float



Set: LOFrequency(self: RfsgChannelBasedLO) = value

"""

    LOInPower = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInPower(self: RfsgChannelBasedLO) -> float



Set: LOInPower(self: RfsgChannelBasedLO) = value

"""

    LoopBandwidth = property(lambda self: RfsgLoopBandwidth(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopBandwidth(self: RfsgChannelBasedLO) -> RfsgLoopBandwidth



Set: LoopBandwidth(self: RfsgChannelBasedLO) = value

"""

    LOOutEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutEnabled(self: RfsgChannelBasedLO) -> bool



Set: LOOutEnabled(self: RfsgChannelBasedLO) = value

"""

    LOOutPower = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutPower(self: RfsgChannelBasedLO) -> float



Set: LOOutPower(self: RfsgChannelBasedLO) = value

"""

    PllFractionalModeEnabled = property(lambda self: RfsgLOPllFractionalModeEnabled(), lambda self, v: None, lambda self: None)  # default
    """Get: PllFractionalModeEnabled(self: RfsgChannelBasedLO) -> RfsgLOPllFractionalModeEnabled



Set: PllFractionalModeEnabled(self: RfsgChannelBasedLO) = value

"""

    Source = property(lambda self: RfsgLocalOscillatorSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgChannelBasedLO) -> RfsgLocalOscillatorSource



Set: Source(self: RfsgChannelBasedLO) = value

"""



class RfsgConfigurationListProperties(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgConfigurationListProperties, values: AlcControl (1150195), AmplificationPath (1150185), AmplitudeSettling (1150137), ArbDigitalGain (1150204), ArbPreFilterGain (1150025), AttenuatorSetting (1150173), AutoPowerSearch (1150196), ExternalGain (1150085), Frequency (1250001), FrequencySettlingTime (1150083), IQOutPortCarrierFrequency (1150145), IQOutPortCommonModeOffset (1150148), IQOutPortLevel (1150147), IQOutPortOffset (1150149), OutputEnabled (1250004), PhaseOffset (1150024), PowerLevel (1250002), PulseModulationEnabled (1250051), SignalBandwidth (1150007), TimerEventInterval (1150100), UpconverterCenterFrequency (1154098), UpconverterFrequencyOffset (1150160) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AlcControl = None
    AmplificationPath = None
    AmplitudeSettling = None
    ArbDigitalGain = None
    ArbPreFilterGain = None
    AttenuatorSetting = None
    AutoPowerSearch = None
    ExternalGain = None
    Frequency = None
    FrequencySettlingTime = None
    IQOutPortCarrierFrequency = None
    IQOutPortCommonModeOffset = None
    IQOutPortLevel = None
    IQOutPortOffset = None
    OutputEnabled = None
    PhaseOffset = None
    PowerLevel = None
    PulseModulationEnabled = None
    SignalBandwidth = None
    TimerEventInterval = None
    UpconverterCenterFrequency = None
    UpconverterFrequencyOffset = None
    value__ = None


class RfsgConfigurationListStepTrigger(RfsgSubObject):
    # no doc
    def Disable(self):
        """ Disable(self: RfsgConfigurationListStepTrigger) """
        pass

    DigitalEdge = property(lambda self: RfsgDigitalEdgeConfigurationListStepTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsgConfigurationListStepTrigger) -> RfsgDigitalEdgeConfigurationListStepTrigger



"""

    ExportedOutputTerminal = property(lambda self: RfsgConfigurationListStepTriggerExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgConfigurationListStepTrigger) -> RfsgConfigurationListStepTriggerExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgConfigurationListStepTrigger) = value

"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgConfigurationListStepTrigger) -> str



"""

    TriggerType = property(lambda self: RfsgConfigurationListStepTriggerType(), lambda self, v: None, lambda self: None)  # default
    """Get: TriggerType(self: RfsgConfigurationListStepTrigger) -> RfsgConfigurationListStepTriggerType



Set: TriggerType(self: RfsgConfigurationListStepTrigger) = value

"""



class RfsgConfigurationListStepTriggerExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgConfigurationListStepTriggerExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgConfigurationListStepTriggerExportedOutputTerminal, outputTerminal: RfsgConfigurationListStepTriggerExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgConfigurationListStepTriggerExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgConfigurationListStepTriggerExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgConfigurationListStepTriggerExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None


class RfsgConfigurationListStepTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgConfigurationListStepTriggerType, values: DigitalEdge (1), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    value__ = None


class RfsgConfigurationSettledEvent(RfsgSubObject):
    # no doc
    OutputTerminal = property(lambda self: RfsgConfigurationSettledEventExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputTerminal(self: RfsgConfigurationSettledEvent) -> RfsgConfigurationSettledEventExportedOutputTerminal



Set: OutputTerminal(self: RfsgConfigurationSettledEvent) = value

"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgConfigurationSettledEvent) -> str



"""



class RfsgConfigurationSettledEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgConfigurationSettledEventExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgConfigurationSettledEventExportedOutputTerminal, outputTerminal: RfsgConfigurationSettledEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgConfigurationSettledEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgConfigurationSettledEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgConfigurationSettledEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    TriggerOutputTerminal = None


class RfsgDataTransfer(RfsgSubObject):
    # no doc
    Advanced = property(lambda self: RfsgDataTransferAdvanced(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsgDataTransfer) -> RfsgDataTransferAdvanced



"""

    BlockSize = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockSize(self: RfsgDataTransfer) -> int



Set: BlockSize(self: RfsgDataTransfer) = value

"""

    DirectDma = property(lambda self: RfsgDirectDma(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectDma(self: RfsgDataTransfer) -> RfsgDirectDma



"""

    DirectDownloadEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectDownloadEnabled(self: RfsgDataTransfer) -> bool



Set: DirectDownloadEnabled(self: RfsgDataTransfer) = value

"""

    MaximumBandwidth = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumBandwidth(self: RfsgDataTransfer) -> float



Set: MaximumBandwidth(self: RfsgDataTransfer) = value

"""

    Streaming = property(lambda self: RfsgStreaming(), lambda self, v: None, lambda self: None)  # default
    """Get: Streaming(self: RfsgDataTransfer) -> RfsgStreaming



"""



class RfsgDataTransferAdvanced(RfsgSubObject):
    # no doc
    MaximumInFlightReadRequests = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumInFlightReadRequests(self: RfsgDataTransferAdvanced) -> int



Set: MaximumInFlightReadRequests(self: RfsgDataTransferAdvanced) = value

"""

    PreferredPacketSize = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: PreferredPacketSize(self: RfsgDataTransferAdvanced) -> int



Set: PreferredPacketSize(self: RfsgDataTransferAdvanced) = value

"""



class RfsgDeembedding(RfsgSubObject):
    # no doc
    def ConfigureDeembeddingTableInterpolationLinear(self, tableName, format):
        """ ConfigureDeembeddingTableInterpolationLinear(self: RfsgDeembedding, tableName: str, format: RfsgLinearInterpolationFormat) """
        pass

    def ConfigureDeembeddingTableInterpolationNearest(self, tableName):
        """ ConfigureDeembeddingTableInterpolationNearest(self: RfsgDeembedding, tableName: str) """
        pass

    def ConfigureDeembeddingTableInterpolationSpline(self, tableName):
        """ ConfigureDeembeddingTableInterpolationSpline(self: RfsgDeembedding, tableName: str) """
        pass

    def CreateDeembeddingSParameterTableArray(self, tableName, frequencies, sParameterTable, sParameterOrientation):
        """ CreateDeembeddingSParameterTableArray(self: RfsgDeembedding, tableName: str, frequencies: Array[float], sParameterTable: Array[ComplexDouble], sParameterOrientation: RfsgSParameterOrientation) """
        pass

    def CreateDeembeddingSParameterTableS2pFile(self, tableName, s2pFilePath, sParameterOrientation):
        """ CreateDeembeddingSParameterTableS2pFile(self: RfsgDeembedding, tableName: str, s2pFilePath: str, sParameterOrientation: RfsgSParameterOrientation) """
        pass

    def DeleteAllDeembeddingTables(self):
        """ DeleteAllDeembeddingTables(self: RfsgDeembedding) """
        pass

    def DeleteDeembeddingTable(self, tableName):
        """ DeleteDeembeddingTable(self: RfsgDeembedding, tableName: str) """
        pass

    def GetDeembeddingSParameters(self, sParameters):
        """ GetDeembeddingSParameters(self: RfsgDeembedding, sParameters: Array[ComplexDouble]) -> Array[ComplexDouble] """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    DeembeddingSelectedTable = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingSelectedTable(self: RfsgDeembedding) -> str



Set: DeembeddingSelectedTable(self: RfsgDeembedding) = value

"""

    DeembeddingType = property(lambda self: RfsgDeembeddingType(), lambda self, v: None, lambda self: None)  # default
    """Get: DeembeddingType(self: RfsgDeembedding) -> RfsgDeembeddingType



Set: DeembeddingType(self: RfsgDeembedding) = value

"""



class RfsgDeembeddingType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgDeembeddingType, values: None (25000), Scalar (25001), Vector (25002) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgDeviceCharacteristics(RfsgSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    AETemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AETemperature(self: RfsgDeviceCharacteristics) -> float



"""

    AwgTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AwgTemperature(self: RfsgDeviceCharacteristics) -> float



"""

    DeviceTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceTemperature(self: RfsgDeviceCharacteristics) -> float



"""

    FpgaBitfilePath = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: FpgaBitfilePath(self: RfsgDeviceCharacteristics) -> str



"""

    FpgaTargetName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: FpgaTargetName(self: RfsgDeviceCharacteristics) -> str



"""

    FpgaTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FpgaTemperature(self: RfsgDeviceCharacteristics) -> float



"""

    LOTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOTemperature(self: RfsgDeviceCharacteristics) -> float



"""

    ModulePowerConsumption = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: ModulePowerConsumption(self: RfsgDeviceCharacteristics) -> float



"""

    ModuleRevision = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: ModuleRevision(self: RfsgDeviceCharacteristics) -> str



"""

    Option = property(lambda self: RfsgDeviceCharactersticsOptions(), lambda self, v: None, lambda self: None)  # default
    """Get: Option(self: RfsgDeviceCharacteristics) -> RfsgDeviceCharactersticsOptions



"""

    SerialNumber = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: SerialNumber(self: RfsgDeviceCharacteristics) -> str



"""

    TemperatureReadInterval = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: TemperatureReadInterval(self: RfsgDeviceCharacteristics) -> float



Set: TemperatureReadInterval(self: RfsgDeviceCharacteristics) = value

"""



class RfsgDeviceCharactersticsOptions(RfsgSubObject):
    # no doc
    FastTuningOption = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: FastTuningOption(self: RfsgDeviceCharactersticsOptions) -> bool



"""



class RfsgDeviceEvents(RfsgSubObject):
    # no doc
    ConfigurationSettledEvent = property(lambda self: RfsgConfigurationSettledEvent(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationSettledEvent(self: RfsgDeviceEvents) -> RfsgConfigurationSettledEvent



"""

    Delay = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Delay(self: RfsgDeviceEvents) -> float



Set: Delay(self: RfsgDeviceEvents) = value

"""

    DoneEvent = property(lambda self: RfsgDoneEvent(), lambda self, v: None, lambda self: None)  # default
    """Get: DoneEvent(self: RfsgDeviceEvents) -> RfsgDoneEvent



"""

    MarkerEvents = property(lambda self: RfsgMarkerEventCollection(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerEvents(self: RfsgDeviceEvents) -> RfsgMarkerEventCollection



"""

    StartedEvent = property(lambda self: RfsgStartedEvent(), lambda self, v: None, lambda self: None)  # default
    """Get: StartedEvent(self: RfsgDeviceEvents) -> RfsgStartedEvent



"""

    Timer = property(lambda self: RfsgTimerEvent(), lambda self, v: None, lambda self: None)  # default
    """Get: Timer(self: RfsgDeviceEvents) -> RfsgTimerEvent



"""



class RfsgDeviceModule(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgDeviceModule, values: Awg (13001), LO (13002), PrimaryModule (13000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Awg = None
    LO = None
    PrimaryModule = None
    value__ = None


class RfsgDigitalEdgeConfigurationListStepTrigger(RfsgSubObject):
    # no doc
    def Configure(self, source, edge):
        """ Configure(self: RfsgDigitalEdgeConfigurationListStepTrigger, source: RfsgDigitalEdgeConfigurationListStepTriggerSource, edge: RfsgTriggerEdge) """
        pass

    Edge = property(lambda self: RfsgTriggerEdge(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: RfsgDigitalEdgeConfigurationListStepTrigger) -> RfsgTriggerEdge



Set: Edge(self: RfsgDigitalEdgeConfigurationListStepTrigger) = value

"""

    Source = property(lambda self: RfsgDigitalEdgeConfigurationListStepTriggerSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgDigitalEdgeConfigurationListStepTrigger) -> RfsgDigitalEdgeConfigurationListStepTriggerSource



Set: Source(self: RfsgDigitalEdgeConfigurationListStepTrigger) = value

"""



class RfsgDigitalEdgeConfigurationListStepTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgDigitalEdgeConfigurationListStepTriggerSource, obj: object) -> bool

        Equals(self: RfsgDigitalEdgeConfigurationListStepTriggerSource, source: RfsgDigitalEdgeConfigurationListStepTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgDigitalEdgeConfigurationListStepTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgDigitalEdgeConfigurationListStepTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgDigitalEdgeConfigurationListStepTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Marker0Event = None
    Marker1Event = None
    Marker2Event = None
    Marker3Event = None
    Pfi0 = None
    Pfi1 = None
    PXIeDStarB = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None
    TimerEvent = None
    TriggerInputTerminal = None


class RfsgDigitalEdgeScriptTrigger(RfsgSubObject):
    # no doc
    def Configure(self, source, edge):
        """ Configure(self: RfsgDigitalEdgeScriptTrigger, source: RfsgDigitalEdgeScriptTriggerSource, edge: RfsgTriggerEdge) """
        pass

    Edge = property(lambda self: RfsgTriggerEdge(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: RfsgDigitalEdgeScriptTrigger) -> RfsgTriggerEdge



Set: Edge(self: RfsgDigitalEdgeScriptTrigger) = value

"""

    Source = property(lambda self: RfsgDigitalEdgeScriptTriggerSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgDigitalEdgeScriptTrigger) -> RfsgDigitalEdgeScriptTriggerSource



Set: Source(self: RfsgDigitalEdgeScriptTrigger) = value

"""



class RfsgDigitalEdgeScriptTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgDigitalEdgeScriptTriggerSource, obj: object) -> bool

        Equals(self: RfsgDigitalEdgeScriptTriggerSource, source: RfsgDigitalEdgeScriptTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgDigitalEdgeScriptTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgDigitalEdgeScriptTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgDigitalEdgeScriptTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    Pfi2 = None
    Pfi3 = None
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


class RfsgDigitalEdgeStartTrigger(RfsgSubObject):
    # no doc
    def Configure(self, source, edge):
        """ Configure(self: RfsgDigitalEdgeStartTrigger, source: RfsgDigitalEdgeStartTriggerSource, edge: RfsgTriggerEdge) """
        pass

    Edge = property(lambda self: RfsgTriggerEdge(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge(self: RfsgDigitalEdgeStartTrigger) -> RfsgTriggerEdge



Set: Edge(self: RfsgDigitalEdgeStartTrigger) = value

"""

    Source = property(lambda self: RfsgDigitalEdgeStartTriggerSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgDigitalEdgeStartTrigger) -> RfsgDigitalEdgeStartTriggerSource



Set: Source(self: RfsgDigitalEdgeStartTrigger) = value

"""



class RfsgDigitalEdgeStartTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgDigitalEdgeStartTriggerSource, obj: object) -> bool

        Equals(self: RfsgDigitalEdgeStartTriggerSource, source: RfsgDigitalEdgeStartTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgDigitalEdgeStartTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgDigitalEdgeStartTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgDigitalEdgeStartTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    Pfi2 = None
    Pfi3 = None
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
    SynchronizationStartTriggerLine = None
    TriggerInputTerminal = None


class RfsgDigitalLevelScriptTrigger(RfsgSubObject):
    # no doc
    def Configure(self, source, level):
        """ Configure(self: RfsgDigitalLevelScriptTrigger, source: RfsgDigitalLevelScriptTriggerSource, level: RfsgTriggerLevel) """
        pass

    Level = property(lambda self: RfsgTriggerLevel(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: RfsgDigitalLevelScriptTrigger) -> RfsgTriggerLevel



Set: Level(self: RfsgDigitalLevelScriptTrigger) = value

"""

    Source = property(lambda self: RfsgDigitalLevelScriptTriggerSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgDigitalLevelScriptTrigger) -> RfsgDigitalLevelScriptTriggerSource



Set: Source(self: RfsgDigitalLevelScriptTrigger) = value

"""



class RfsgDigitalLevelScriptTriggerSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgDigitalLevelScriptTriggerSource, obj: object) -> bool

        Equals(self: RfsgDigitalLevelScriptTriggerSource, source: RfsgDigitalLevelScriptTriggerSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgDigitalLevelScriptTriggerSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgDigitalLevelScriptTriggerSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgDigitalLevelScriptTriggerSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Pfi0 = None
    Pfi1 = None
    Pfi2 = None
    Pfi3 = None
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
    SynchronizationStartTriggerLine = None


class RfsgDigitalModulation(RfsgSubObject):
    # no doc
    def ConfigureUserDefinedWaveform(self, userDefinedWaveform):
        """ ConfigureUserDefinedWaveform(self: RfsgDigitalModulation, userDefinedWaveform: Array[Byte]) """
        pass

    FskDeviation = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FskDeviation(self: RfsgDigitalModulation) -> float



Set: FskDeviation(self: RfsgDigitalModulation) = value

"""

    ModulationType = property(lambda self: RfsgDigitalModulationType(), lambda self, v: None, lambda self: None)  # default
    """Get: ModulationType(self: RfsgDigitalModulation) -> RfsgDigitalModulationType



Set: ModulationType(self: RfsgDigitalModulation) = value

"""

    PrbsOrder = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: PrbsOrder(self: RfsgDigitalModulation) -> int



Set: PrbsOrder(self: RfsgDigitalModulation) = value

"""

    PrbsSeed = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: PrbsSeed(self: RfsgDigitalModulation) -> int



Set: PrbsSeed(self: RfsgDigitalModulation) = value

"""

    SymbolRate = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolRate(self: RfsgDigitalModulation) -> float



Set: SymbolRate(self: RfsgDigitalModulation) = value

"""

    WaveformType = property(lambda self: RfsgDigitalModulationWaveformType(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformType(self: RfsgDigitalModulation) -> RfsgDigitalModulationWaveformType



Set: WaveformType(self: RfsgDigitalModulation) = value

"""



class RfsgDigitalModulationType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgDigitalModulationType, values: Fsk (4000), None (0), Ook (4001), Psk (4002) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Fsk = None
    None = None
    Ook = None
    Psk = None
    value__ = None


class RfsgDigitalModulationWaveformType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgDigitalModulationWaveformType, values: Prbs (5000), UserDefined (5001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Prbs = None
    UserDefined = None
    value__ = None


class RfsgDirectDma(RfsgSubObject):
    # no doc
    Enabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: RfsgDirectDma) -> bool



Set: Enabled(self: RfsgDirectDma) = value

"""

    WindowAddress = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowAddress(self: RfsgDirectDma) -> int



Set: WindowAddress(self: RfsgDirectDma) = value

"""

    WindowSize = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowSize(self: RfsgDirectDma) -> int



Set: WindowSize(self: RfsgDirectDma) = value

"""



class RfsgDoneEvent(RfsgSubObject):
    # no doc
    ExportedOutputTerminal = property(lambda self: RfsgDoneEventExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgDoneEvent) -> RfsgDoneEventExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgDoneEvent) = value

"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgDoneEvent) -> str



"""



class RfsgDoneEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgDoneEventExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgDoneEventExportedOutputTerminal, outputTerminal: RfsgDoneEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgDoneEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgDoneEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgDoneEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    Pfi4 = None
    Pfi5 = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None


class RfsgDriverIdentity(RfsgSubObject, IIviDriverIdentity, IIviComponentIdentity):
    # no doc
    def GetGroupCapabilities(self):
        """ GetGroupCapabilities(self: RfsgDriverIdentity) -> Array[str] """
        pass

    def GetSupportedInstrumentModels(self):
        """ GetSupportedInstrumentModels(self: RfsgDriverIdentity) -> Array[str] """
        pass

    def RevisionQuery(self):
        """ RevisionQuery(self: RfsgDriverIdentity) -> RfsgRevisionQueryResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: RfsgDriverIdentity) -> str



"""

    Identifier = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: RfsgDriverIdentity) -> str



"""

    InstrumentFirmwareRevision = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentFirmwareRevision(self: RfsgDriverIdentity) -> str



"""

    InstrumentManufacturer = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentManufacturer(self: RfsgDriverIdentity) -> str



"""

    InstrumentModel = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentModel(self: RfsgDriverIdentity) -> str



"""

    Revision = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Revision(self: RfsgDriverIdentity) -> str



"""

    SpecificationMajorVersion = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificationMajorVersion(self: RfsgDriverIdentity) -> int



"""

    SpecificationMinorVersion = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificationMinorVersion(self: RfsgDriverIdentity) -> int



"""

    SpecificDriverMajorVersion = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificDriverMajorVersion(self: RfsgDriverIdentity) -> int



"""

    SpecificDriverMinorVersion = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificDriverMinorVersion(self: RfsgDriverIdentity) -> int



"""

    Vendor = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Vendor(self: RfsgDriverIdentity) -> str



"""



class RfsgDriverLock(object):
    """ RfsgDriverLock(iviDriverLock: IIviDriverLock) """
    def Unlock(self):
        """ Unlock(self: RfsgDriverLock) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iviDriverLock):
        """ __new__(cls: type, iviDriverLock: IIviDriverLock) """
        pass


class RfsgDriverOperation(RfsgSubObject, IIviDriverOperation, IDisposable, ISupportSynchronizationContext):
    # no doc
    def Dispose(self):
        """ Dispose(self: RfsgDriverOperation) """
        pass

    def InvalidateAllAttributes(self):
        """ InvalidateAllAttributes(self: RfsgDriverOperation) """
        pass

    def ResetInterchangeCheck(self):
        """ ResetInterchangeCheck(self: RfsgDriverOperation) """
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

    Cache = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: Cache(self: RfsgDriverOperation) -> bool



Set: Cache(self: RfsgDriverOperation) = value

"""

    DriverSetup = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverSetup(self: RfsgDriverOperation) -> str



"""

    InterchangeCheck = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: InterchangeCheck(self: RfsgDriverOperation) -> bool



Set: InterchangeCheck(self: RfsgDriverOperation) = value

"""

    IOResourceDescriptor = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: IOResourceDescriptor(self: RfsgDriverOperation) -> str



"""

    LogicalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalName(self: RfsgDriverOperation) -> str



"""

    QueryInstrumentStatus = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: QueryInstrumentStatus(self: RfsgDriverOperation) -> bool



Set: QueryInstrumentStatus(self: RfsgDriverOperation) = value

"""

    RangeCheck = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeCheck(self: RfsgDriverOperation) -> bool



Set: RangeCheck(self: RfsgDriverOperation) = value

"""

    RecordCoercions = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: RecordCoercions(self: RfsgDriverOperation) -> bool



Set: RecordCoercions(self: RfsgDriverOperation) = value

"""

    Simulate = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: Simulate(self: RfsgDriverOperation) -> bool



Set: Simulate(self: RfsgDriverOperation) = value

"""

    SynchronizeCallbacks = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizeCallbacks(self: RfsgDriverOperation) -> bool



Set: SynchronizeCallbacks(self: RfsgDriverOperation) = value

"""


    Warning = None


class RfsgDriverUtility(RfsgSubObject, IIviDriverUtility):
    # no doc
    def Commit(self):
        """ Commit(self: RfsgDriverUtility) """
        pass

    def Disable(self):
        """ Disable(self: RfsgDriverUtility) """
        pass

    def ErrorQuery(self):
        """ ErrorQuery(self: RfsgDriverUtility) -> RfsgErrorQueryResult """
        pass

    def Lock(self, maxTime=None):
        """
        Lock(self: RfsgDriverUtility) -> RfsgDriverLock

        Lock(self: RfsgDriverUtility, maxTime: PrecisionTimeSpan) -> RfsgDriverLock
        """
        pass

    def PerformPowerSearch(self):
        """ PerformPowerSearch(self: RfsgDriverUtility) """
        pass

    def PerformThermalCorrection(self):
        """ PerformThermalCorrection(self: RfsgDriverUtility) """
        pass

    def Reset(self):
        """ Reset(self: RfsgDriverUtility) """
        pass

    def ResetAttribute(self, *__args):
        """ ResetAttribute(self: RfsgDriverUtility, propertyToReset: PropertyInfo)ResetAttribute(self: RfsgDriverUtility, channelName: str, propertyToReset: PropertyInfo) """
        pass

    def ResetDevice(self):
        """ ResetDevice(self: RfsgDriverUtility) """
        pass

    def ResetWithDefaults(self):
        """ ResetWithDefaults(self: RfsgDriverUtility) """
        pass

    def ResetWithOptions(self, stepsToOmit):
        """ ResetWithOptions(self: RfsgDriverUtility, stepsToOmit: RfsgResetStepsToOmit) """
        pass

    def RevisionQuery(self):
        """ RevisionQuery(self: RfsgDriverUtility) -> RfsgRevisionQueryResult """
        pass

    def SelfCalibrate(self):
        """ SelfCalibrate(self: RfsgDriverUtility) """
        pass

    def SelfTest(self):
        """ SelfTest(self: RfsgDriverUtility) -> RfsgSelfTestResult """
        pass

    def WaitUntilSettled(self, maxTimeMilliseconds):
        """ WaitUntilSettled(self: RfsgDriverUtility, maxTimeMilliseconds: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RfsgErrorInfoUtility(RfsgSubObject):
    # no doc
    def ClearError(self):
        """ ClearError(self: RfsgErrorInfoUtility) """
        pass

    def ErrorMessage(self, errorCode):
        """ ErrorMessage(self: RfsgErrorInfoUtility, errorCode: int) -> str """
        pass

    def GetError(self):
        """ GetError(self: RfsgErrorInfoUtility) -> RfsgErrorQueryResult """
        pass

    def GetException(self):
        """ GetException(self: RfsgErrorInfoUtility) -> Exception """
        pass

    def GetStaticException(self, errorCode):
        """ GetStaticException(self: RfsgErrorInfoUtility, errorCode: int) -> Exception """
        pass

    def GetStaticWarning(self, errorCode):
        """ GetStaticWarning(self: RfsgErrorInfoUtility, errorCode: int) -> RfsgWarning """
        pass

    def GetWarning(self):
        """ GetWarning(self: RfsgErrorInfoUtility) -> RfsgWarning """
        pass


class RfsgErrorQueryResult(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgErrorQueryResult, obj: object) -> bool

        Equals(self: RfsgErrorQueryResult, result: RfsgErrorQueryResult) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgErrorQueryResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorCode(self: RfsgErrorQueryResult) -> int



"""

    ErrorMessage = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorMessage(self: RfsgErrorQueryResult) -> str



"""



class RfsgFilterType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgFilterType, values: None (10000), RaisedCosine (10002), RootRaisedCosine (10001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    RaisedCosine = None
    RootRaisedCosine = None
    value__ = None


class RfsgFrequencyReference(RfsgSubObject):
    # no doc
    def Configure(self, source, rate):
        """ Configure(self: RfsgFrequencyReference, source: RfsgFrequencyReferenceSource, rate: float) """
        pass

    ExportedOutputTerminal = property(lambda self: RfsgFrequencyReferenceExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgFrequencyReference) -> RfsgFrequencyReferenceExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgFrequencyReference) = value

"""

    PxiChassisClock10Source = property(lambda self: RfsgPxiChassisClock10Source(), lambda self, v: None, lambda self: None)  # default
    """Get: PxiChassisClock10Source(self: RfsgFrequencyReference) -> RfsgPxiChassisClock10Source



Set: PxiChassisClock10Source(self: RfsgFrequencyReference) = value

"""

    Rate = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Rate(self: RfsgFrequencyReference) -> float



Set: Rate(self: RfsgFrequencyReference) = value

"""

    Source = property(lambda self: RfsgFrequencyReferenceSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgFrequencyReference) -> RfsgFrequencyReferenceSource



Set: Source(self: RfsgFrequencyReference) = value

"""



class RfsgFrequencyReferenceExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgFrequencyReferenceExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgFrequencyReferenceExportedOutputTerminal, outputTerminal: RfsgFrequencyReferenceExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgFrequencyReferenceExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgFrequencyReferenceExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgFrequencyReferenceExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockOut = None
    DoNotExport = None
    ReferenceOut = None
    ReferenceOut2 = None


class RfsgFrequencyReferenceSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgFrequencyReferenceSource, obj: object) -> bool

        Equals(self: RfsgFrequencyReferenceSource, source: RfsgFrequencyReferenceSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgFrequencyReferenceSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgFrequencyReferenceSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgFrequencyReferenceSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ClockIn = None
    OnboardClock = None
    PxiClock = None
    ReferenceIn = None


class RfsgGenerationStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgGenerationStatus, values: Complete (1), InProgress (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Complete = None
    InProgress = None
    value__ = None


class RfsgIQImpairment(RfsgSubObject):
    # no doc
    Enabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: RfsgIQImpairment) -> bool



Set: Enabled(self: RfsgIQImpairment) = value

"""

    GainImbalance = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: GainImbalance(self: RfsgIQImpairment) -> float



Set: GainImbalance(self: RfsgIQImpairment) = value

"""

    IOffset = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: IOffset(self: RfsgIQImpairment) -> float



Set: IOffset(self: RfsgIQImpairment) = value

"""

    OffsetUnits = property(lambda self: RfsgIQOffsetUnits(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetUnits(self: RfsgIQImpairment) -> RfsgIQOffsetUnits



Set: OffsetUnits(self: RfsgIQImpairment) = value

"""

    QOffset = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: QOffset(self: RfsgIQImpairment) -> float



Set: QOffset(self: RfsgIQImpairment) = value

"""

    Skew = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Skew(self: RfsgIQImpairment) -> float



Set: Skew(self: RfsgIQImpairment) = value

"""



class RfsgIQOffsetUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgIQOffsetUnits, values: Percentage (11000), Volts (11001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Percentage = None
    value__ = None
    Volts = None


class RfsgIQOutPort(RfsgSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    CarrierFrequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: CarrierFrequency(self: RfsgIQOutPort) -> float



Set: CarrierFrequency(self: RfsgIQOutPort) = value

"""

    Temperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Temperature(self: RfsgIQOutPort) -> float



"""



class RfsgLinearInterpolationFormat(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgLinearInterpolationFormat, values: MagnitudeAndPhase (26001), MagnitudeInDecibelAndPhase (26002), RealAndImaginary (26000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgLocalOscillatorSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgLocalOscillatorSource, obj: object) -> bool

        Equals(self: RfsgLocalOscillatorSource, source: RfsgLocalOscillatorSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgLocalOscillatorSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgLocalOscillatorSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgLocalOscillatorSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    LOIn = None
    Onboard = None
    Secondary = None
    SGSAShared = None


class RfsgLoopBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgLoopBandwidth, values: High (2), Low (0), Medium (1), Narrow (0), Wide (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Medium = None
    Narrow = None
    value__ = None
    Wide = None


class RfsgLOOutExportConfigureFromRfsa(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgLOOutExportConfigureFromRfsa, values: Disabled (0), Enabled (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgLOPllFractionalModeEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgLOPllFractionalModeEnabled, values: Disable (0), Enable (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Disable = None
    Enable = None
    value__ = None


class RfsgMarkerEvent(RfsgSubObject):
    # no doc
    ExportedOutputTerminal = property(lambda self: RfsgMarkerEventExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgMarkerEvent) -> RfsgMarkerEventExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgMarkerEvent) = value

"""

    OutputBehaviour = property(lambda self: RfsgMarkerEventOutputBehaviour(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputBehaviour(self: RfsgMarkerEvent) -> RfsgMarkerEventOutputBehaviour



Set: OutputBehaviour(self: RfsgMarkerEvent) = value

"""

    PulseWidth = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PulseWidth(self: RfsgMarkerEvent) -> float



Set: PulseWidth(self: RfsgMarkerEvent) = value

"""

    PulseWidthUnits = property(lambda self: RfsgMarkerEventPulseWidthUnits(), lambda self, v: None, lambda self: None)  # default
    """Get: PulseWidthUnits(self: RfsgMarkerEvent) -> RfsgMarkerEventPulseWidthUnits



Set: PulseWidthUnits(self: RfsgMarkerEvent) = value

"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgMarkerEvent) -> str



"""

    ToggleInitialState = property(lambda self: RfsgMarkerEventToggleInitialState(), lambda self, v: None, lambda self: None)  # default
    """Get: ToggleInitialState(self: RfsgMarkerEvent) -> RfsgMarkerEventToggleInitialState



Set: ToggleInitialState(self: RfsgMarkerEvent) = value

"""



class RfsgMarkerEventCollection(RfsgSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass


class RfsgMarkerEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgMarkerEventExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgMarkerEventExportedOutputTerminal, outputTerminal: RfsgMarkerEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgMarkerEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgMarkerEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgMarkerEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    Pfi4 = None
    Pfi5 = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None


class RfsgMarkerEventOutputBehaviour(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgMarkerEventOutputBehaviour, values: Pulse (23000), Toggle (23001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Pulse = None
    Toggle = None
    value__ = None


class RfsgMarkerEventPulseWidthUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgMarkerEventPulseWidthUnits, values: SampleClockPeriods (22001), Seconds (22000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SampleClockPeriods = None
    Seconds = None
    value__ = None


class RfsgMarkerEventToggleInitialState(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgMarkerEventToggleInitialState, values: DigitalHigh (21001), DigitalLow (21000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DigitalHigh = None
    DigitalLow = None
    value__ = None


class RfsgModulation(RfsgSubObject):
    # no doc
    Analog = property(lambda self: RfsgAnalogModulation(), lambda self, v: None, lambda self: None)  # default
    """Get: Analog(self: RfsgModulation) -> RfsgAnalogModulation



"""

    Digital = property(lambda self: RfsgDigitalModulation(), lambda self, v: None, lambda self: None)  # default
    """Get: Digital(self: RfsgModulation) -> RfsgDigitalModulation



"""



class RfsgModule(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgModule, values: Awg (13001), LO (13002), PrimaryModule (13000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Awg = None
    LO = None
    PrimaryModule = None
    value__ = None


class RfsgOnboardSampleClockMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgOnboardSampleClockMode, values: DivideDown (6001), HighResolution (6000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DivideDown = None
    HighResolution = None
    value__ = None


class RfsgOutputPort(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgOutputPort, values: CalOut (14002), IOnly (14003), IQOut (14001), RFOut (14000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CalOut = None
    IOnly = None
    IQOut = None
    RFOut = None
    value__ = None


class RfsgOverflowErrorReporting(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgOverflowErrorReporting, values: Disabled (1302), Warning (1301) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgPeakPowerAdjustmentInheritance(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgPeakPowerAdjustmentInheritance, values: ExactMatch (0), Minimum (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ExactMatch = None
    Minimum = None
    value__ = None


class RfsgPhaseContinuityEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgPhaseContinuityEnabled, values: Auto (-1), Disabled (0), Enabled (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Enabled = None
    value__ = None


class RfsgPulseModulationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgPulseModulationMode, values: HighIsolation (20001), OptimalMatch (20000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HighIsolation = None
    OptimalMatch = None
    value__ = None


class RfsgPulseShaping(RfsgSubObject):
    # no doc
    Filter = property(lambda self: RfsgFilterType(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: RfsgPulseShaping) -> RfsgFilterType



Set: Filter(self: RfsgPulseShaping) = value

"""

    RaisedCosineAlpha = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: RaisedCosineAlpha(self: RfsgPulseShaping) -> float



Set: RaisedCosineAlpha(self: RfsgPulseShaping) = value

"""

    RootRaisedCosineAlpha = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: RootRaisedCosineAlpha(self: RfsgPulseShaping) -> float



Set: RootRaisedCosineAlpha(self: RfsgPulseShaping) = value

"""



class RfsgPxiChassisClock10Source(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgPxiChassisClock10Source, obj: object) -> bool

        Equals(self: RfsgPxiChassisClock10Source, source: RfsgPxiChassisClock10Source) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgPxiChassisClock10Source """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgPxiChassisClock10Source) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgPxiChassisClock10Source) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    None = None
    OnboardClock = None
    ReferenceIn = None


class RfsgReferencePllBandwidth(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgReferencePllBandwidth, values: High (2), Low (0), Medium (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Medium = None
    value__ = None


class RfsgResetStepsToOmit(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgResetStepsToOmit, values: DeembeddingTables (8), None (0), Routes (4), Scripts (2), Waveforms (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Scripts = None
    value__ = None
    Waveforms = None


class RfsgRevisionQueryResult(object):
    """ RfsgRevisionQueryResult(instrumentRevision: str, firmwareRevision: str) """
    def Equals(self, *__args):
        """
        Equals(self: RfsgRevisionQueryResult, obj: object) -> bool

        Equals(self: RfsgRevisionQueryResult, result: RfsgRevisionQueryResult) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgRevisionQueryResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, instrumentRevision, firmwareRevision):
        """
        __new__(cls: type, instrumentRevision: str, firmwareRevision: str)

        __new__[RfsgRevisionQueryResult]() -> RfsgRevisionQueryResult
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    FirmwareRevision = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: FirmwareRevision(self: RfsgRevisionQueryResult) -> str



"""

    InstrumentRevision = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: InstrumentRevision(self: RfsgRevisionQueryResult) -> str



"""



class RfsgRF(RfsgSubObject):
    # no doc
    def Configure(self, frequency, powerLevel):
        """ Configure(self: RfsgRF, frequency: float, powerLevel: float) """
        pass

    Advanced = property(lambda self: RfsgRFAdvanced(), lambda self, v: None, lambda self: None)  # default
    """Get: Advanced(self: RfsgRF) -> RfsgRFAdvanced



"""

    ExternalGain = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalGain(self: RfsgRF) -> float



Set: ExternalGain(self: RfsgRF) = value

"""

    Frequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Frequency(self: RfsgRF) -> float



Set: Frequency(self: RfsgRF) = value

"""

    LocalOscillator = property(lambda self: RfsgRFLocalOscillator(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalOscillator(self: RfsgRF) -> RfsgRFLocalOscillator



"""

    LOOutExportConfigureFromRfsa = property(lambda self: RfsgLOOutExportConfigureFromRfsa(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutExportConfigureFromRfsa(self: RfsgRF) -> RfsgLOOutExportConfigureFromRfsa



Set: LOOutExportConfigureFromRfsa(self: RfsgRF) = value

"""

    OutputEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputEnabled(self: RfsgRF) -> bool



Set: OutputEnabled(self: RfsgRF) = value

"""

    PhaseOffset = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PhaseOffset(self: RfsgRF) -> float



Set: PhaseOffset(self: RfsgRF) = value

"""

    PowerLevel = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerLevel(self: RfsgRF) -> float



Set: PowerLevel(self: RfsgRF) = value

"""

    PowerLevelType = property(lambda self: RfsgRFPowerLevelType(), lambda self, v: None, lambda self: None)  # default
    """Get: PowerLevelType(self: RfsgRF) -> RfsgRFPowerLevelType



Set: PowerLevelType(self: RfsgRF) = value

"""

    RFBlankingSource = property(lambda self: RfsgRFBlankingSource(), lambda self, v: None, lambda self: None)  # default
    """Get: RFBlankingSource(self: RfsgRF) -> RfsgRFBlankingSource



Set: RFBlankingSource(self: RfsgRF) = value

"""

    RFInLOExportEnabled = property(lambda self: RfsgRFInLOExportEnabled(), lambda self, v: None, lambda self: None)  # default
    """Get: RFInLOExportEnabled(self: RfsgRF) -> RfsgRFInLOExportEnabled



Set: RFInLOExportEnabled(self: RfsgRF) = value

"""

    Upconverter = property(lambda self: RfsgUpconverter(), lambda self, v: None, lambda self: None)  # default
    """Get: Upconverter(self: RfsgRF) -> RfsgUpconverter



"""



class RfsgRFAdvanced(RfsgSubObject):
    # no doc
    AlcControl = property(lambda self: RfsgAlcControl(), lambda self, v: None, lambda self: None)  # default
    """Get: AlcControl(self: RfsgRFAdvanced) -> RfsgAlcControl



Set: AlcControl(self: RfsgRFAdvanced) = value

"""

    AllowOutOfSpecificationUserSettings = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowOutOfSpecificationUserSettings(self: RfsgRFAdvanced) -> bool



Set: AllowOutOfSpecificationUserSettings(self: RfsgRFAdvanced) = value

"""

    AmplificationPath = property(lambda self: RfsgAmplificationPath(), lambda self, v: None, lambda self: None)  # default
    """Get: AmplificationPath(self: RfsgRFAdvanced) -> RfsgAmplificationPath



Set: AmplificationPath(self: RfsgRFAdvanced) = value

"""

    AmplitudeSettling = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AmplitudeSettling(self: RfsgRFAdvanced) -> float



Set: AmplitudeSettling(self: RfsgRFAdvanced) = value

"""

    AttenuatorHoldEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: AttenuatorHoldEnabled(self: RfsgRFAdvanced) -> bool



Set: AttenuatorHoldEnabled(self: RfsgRFAdvanced) = value

"""

    AttenuatorHoldMaximumPower = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AttenuatorHoldMaximumPower(self: RfsgRFAdvanced) -> float



Set: AttenuatorHoldMaximumPower(self: RfsgRFAdvanced) = value

"""

    AttenuatorSetting = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: AttenuatorSetting(self: RfsgRFAdvanced) -> float



Set: AttenuatorSetting(self: RfsgRFAdvanced) = value

"""

    AutomaticThermalCorrection = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticThermalCorrection(self: RfsgRFAdvanced) -> bool



Set: AutomaticThermalCorrection(self: RfsgRFAdvanced) = value

"""

    AutoPowerSearch = property(lambda self: RfsgAutoPowerSearch(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoPowerSearch(self: RfsgRFAdvanced) -> RfsgAutoPowerSearch



Set: AutoPowerSearch(self: RfsgRFAdvanced) = value

"""

    CorrectionTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: CorrectionTemperature(self: RfsgRFAdvanced) -> float



Set: CorrectionTemperature(self: RfsgRFAdvanced) = value

"""

    FrequencySettlingTime = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencySettlingTime(self: RfsgRFAdvanced) -> float



Set: FrequencySettlingTime(self: RfsgRFAdvanced) = value

"""

    FrequencySettlingUnits = property(lambda self: RfsgRFFrequencySettlingUnits(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencySettlingUnits(self: RfsgRFAdvanced) -> RfsgRFFrequencySettlingUnits



Set: FrequencySettlingUnits(self: RfsgRFAdvanced) = value

"""

    FrequencyTolerance = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyTolerance(self: RfsgRFAdvanced) -> float



Set: FrequencyTolerance(self: RfsgRFAdvanced) = value

"""

    LoopBandwidth = property(lambda self: RfsgLoopBandwidth(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopBandwidth(self: RfsgRFAdvanced) -> RfsgLoopBandwidth



Set: LoopBandwidth(self: RfsgRFAdvanced) = value

"""

    PeakEnvelopePower = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PeakEnvelopePower(self: RfsgRFAdvanced) -> float



"""

    PeakPowerAdjustment = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: PeakPowerAdjustment(self: RfsgRFAdvanced) -> float



Set: PeakPowerAdjustment(self: RfsgRFAdvanced) = value

"""

    PeakPowerAdjustmentInheritance = property(lambda self: RfsgPeakPowerAdjustmentInheritance(), lambda self, v: None, lambda self: None)  # default
    """Get: PeakPowerAdjustmentInheritance(self: RfsgRFAdvanced) -> RfsgPeakPowerAdjustmentInheritance



Set: PeakPowerAdjustmentInheritance(self: RfsgRFAdvanced) = value

"""

    PulseModulationEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: PulseModulationEnabled(self: RfsgRFAdvanced) -> bool



Set: PulseModulationEnabled(self: RfsgRFAdvanced) = value

"""

    PulseModulationMode = property(lambda self: RfsgPulseModulationMode(), lambda self, v: None, lambda self: None)  # default
    """Get: PulseModulationMode(self: RfsgRFAdvanced) -> RfsgPulseModulationMode



Set: PulseModulationMode(self: RfsgRFAdvanced) = value

"""

    ReferencePllBandwidth = property(lambda self: RfsgReferencePllBandwidth(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencePllBandwidth(self: RfsgRFAdvanced) -> RfsgReferencePllBandwidth



Set: ReferencePllBandwidth(self: RfsgRFAdvanced) = value

"""

    ThermalCorrectionHeadroomRange = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalCorrectionHeadroomRange(self: RfsgRFAdvanced) -> float



Set: ThermalCorrectionHeadroomRange(self: RfsgRFAdvanced) = value

"""

    ThermalCorrectionTemperatureResolution = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: ThermalCorrectionTemperatureResolution(self: RfsgRFAdvanced) -> float



Set: ThermalCorrectionTemperatureResolution(self: RfsgRFAdvanced) = value

"""

    YigMainCoilDrive = property(lambda self: RfsgYigMainCoilDriveType(), lambda self, v: None, lambda self: None)  # default
    """Get: YigMainCoilDrive(self: RfsgRFAdvanced) -> RfsgYigMainCoilDriveType



Set: YigMainCoilDrive(self: RfsgRFAdvanced) = value

"""



class RfsgRFBlankingSource(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgRFBlankingSource, obj: object) -> bool

        Equals(self: RfsgRFBlankingSource, source: RfsgRFBlankingSource) -> bool
        """
        pass

    @staticmethod
    def FromString(source):
        """ FromString(source: str) -> RfsgRFBlankingSource """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgRFBlankingSource) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgRFBlankingSource) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Disable = None
    Marker0 = None
    Marker1 = None
    Marker2 = None
    Marker3 = None


class RfsgRFFrequencySettlingUnits(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgRFFrequencySettlingUnits, values: Ppm (12002), TimeAfterIO (12001), TimeAfterLock (12000) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    TimeAfterIO = None
    TimeAfterLock = None
    value__ = None


class RfsgRFInLOExportEnabled(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgRFInLOExportEnabled, values: Disabled (0), Enabled (1), Unspecified (-2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgRFLocalOscillator(RfsgSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    FrequencyStepSize = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyStepSize(self: RfsgRFLocalOscillator) -> float



Set: FrequencyStepSize(self: RfsgRFLocalOscillator) = value

"""

    LOFrequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOFrequency(self: RfsgRFLocalOscillator) -> float



Set: LOFrequency(self: RfsgRFLocalOscillator) = value

"""

    LOInPower = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOInPower(self: RfsgRFLocalOscillator) -> float



Set: LOInPower(self: RfsgRFLocalOscillator) = value

"""

    LoopBandwidth = property(lambda self: RfsgLoopBandwidth(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopBandwidth(self: RfsgRFLocalOscillator) -> RfsgLoopBandwidth



Set: LoopBandwidth(self: RfsgRFLocalOscillator) = value

"""

    LOOutEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutEnabled(self: RfsgRFLocalOscillator) -> bool



Set: LOOutEnabled(self: RfsgRFLocalOscillator) = value

"""

    LOOutPower = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOOutPower(self: RfsgRFLocalOscillator) -> float



Set: LOOutPower(self: RfsgRFLocalOscillator) = value

"""

    LOVcoFrequencyStepSize = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LOVcoFrequencyStepSize(self: RfsgRFLocalOscillator) -> float



Set: LOVcoFrequencyStepSize(self: RfsgRFLocalOscillator) = value

"""

    PllFractionalModeEnabled = property(lambda self: RfsgLOPllFractionalModeEnabled(), lambda self, v: None, lambda self: None)  # default
    """Get: PllFractionalModeEnabled(self: RfsgRFLocalOscillator) -> RfsgLOPllFractionalModeEnabled



Set: PllFractionalModeEnabled(self: RfsgRFLocalOscillator) = value

"""

    Source = property(lambda self: RfsgLocalOscillatorSource(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: RfsgRFLocalOscillator) -> RfsgLocalOscillatorSource



Set: Source(self: RfsgRFLocalOscillator) = value

"""



class RfsgRFPortType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgRFPortType, values: PortRFIn (14500), PortRFOut (14501) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PortRFIn = None
    PortRFOut = None
    value__ = None


class RfsgRFPowerLevelType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgRFPowerLevelType, values: AveragePower (7000), PeakPower (7001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AveragePower = None
    PeakPower = None
    value__ = None


class RfsgScripting(RfsgSubObject):
    # no doc
    def CheckIfScriptExists(self, scriptName):
        """ CheckIfScriptExists(self: RfsgScripting, scriptName: str) -> bool """
        pass

    def WriteScript(self, script):
        """ WriteScript(self: RfsgScripting, script: str) """
        pass

    SelectedScriptName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedScriptName(self: RfsgScripting) -> str



Set: SelectedScriptName(self: RfsgScripting) = value

"""



class RfsgScriptTrigger(RfsgSubObject):
    # no doc
    def ConfigureSoftwareTrigger(self):
        """ ConfigureSoftwareTrigger(self: RfsgScriptTrigger) """
        pass

    def Disable(self):
        """ Disable(self: RfsgScriptTrigger) """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RfsgScriptTrigger) """
        pass

    DigitalEdge = property(lambda self: RfsgDigitalEdgeScriptTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsgScriptTrigger) -> RfsgDigitalEdgeScriptTrigger



"""

    DigitalLevel = property(lambda self: RfsgDigitalLevelScriptTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalLevel(self: RfsgScriptTrigger) -> RfsgDigitalLevelScriptTrigger



"""

    ExportedOutputTerminal = property(lambda self: RfsgScriptTriggerExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgScriptTrigger) -> RfsgScriptTriggerExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgScriptTrigger) = value

"""

    Synchronized = property(lambda self: RfsgSynchronizedScriptTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronized(self: RfsgScriptTrigger) -> RfsgSynchronizedScriptTrigger



"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgScriptTrigger) -> str



"""

    TriggerType = property(lambda self: RfsgScriptTriggerType(), lambda self, v: None, lambda self: None)  # default
    """Get: TriggerType(self: RfsgScriptTrigger) -> RfsgScriptTriggerType



Set: TriggerType(self: RfsgScriptTrigger) = value

"""



class RfsgScriptTriggerCollection(RfsgSubObject):
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass


class RfsgScriptTriggerExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgScriptTriggerExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgScriptTriggerExportedOutputTerminal, outputTerminal: RfsgScriptTriggerExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgScriptTriggerExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgScriptTriggerExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgScriptTriggerExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    Pfi4 = None
    Pfi5 = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None


class RfsgScriptTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgScriptTriggerType, values: DigitalEdge (1), DigitalLevel (8000), None (0), Software (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    DigitalLevel = None
    None = None
    Software = None
    value__ = None


class RfsgSelfCalibration(RfsgSubObject):
    # no doc
    def AlignLODaisyChain5840(self, useExternalLO, externalLO, resourceName, portTypes, startFrequency, stopFrequency):
        """ AlignLODaisyChain5840(self: RfsgSelfCalibration, useExternalLO: bool, externalLO: str, resourceName: str, portTypes: Array[RfsgRFPortType], startFrequency: float, stopFrequency: float) """
        pass

    def ClearSelfCalibrateRange(self):
        """ ClearSelfCalibrateRange(self: RfsgSelfCalibration) """
        pass

    def GetSelfCalibrationLastDateAndTime(self, module):
        """ GetSelfCalibrationLastDateAndTime(self: RfsgSelfCalibration, module: RfsgDeviceModule) -> DateTime """
        pass

    def GetSelfCalibrationTemperature(self, module):
        """ GetSelfCalibrationTemperature(self: RfsgSelfCalibration, module: RfsgDeviceModule) -> float """
        pass

    def SelfCalibrate(self):
        """ SelfCalibrate(self: RfsgSelfCalibration) """
        pass

    def SelfCalibrateRange(self, stepsToOmit, minFrequency, maxFrequency, minPowerLevel, maxPowerLevel):
        """ SelfCalibrateRange(self: RfsgSelfCalibration, stepsToOmit: RfsgSelfCalibrationSteps, minFrequency: float, maxFrequency: float, minPowerLevel: float, maxPowerLevel: float) """
        pass

    LastSelfCalibrationTemperature = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: LastSelfCalibrationTemperature(self: RfsgSelfCalibration) -> float



"""



class RfsgSelfCalibrationSteps(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RfsgSelfCalibrationSteps, values: ImageSuppression (8), LOSelfCal (1), OmitNone (0), PowerLevelAccuracy (2), ResidualLOPower (4), SynthesizerAlignment (16) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ImageSuppression = None
    LOSelfCal = None
    OmitNone = None
    PowerLevelAccuracy = None
    ResidualLOPower = None
    SynthesizerAlignment = None
    value__ = None


class RfsgSelfTestResult(object):
    """ RfsgSelfTestResult(code: int, message: str) """
    def Equals(self, *__args):
        """
        Equals(self: RfsgSelfTestResult, obj: object) -> bool

        Equals(self: RfsgSelfTestResult, result: RfsgSelfTestResult) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgSelfTestResult) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, code, message):
        """
        __new__(cls: type, code: int, message: str)

        __new__[RfsgSelfTestResult]() -> RfsgSelfTestResult
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Code = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: RfsgSelfTestResult) -> int



"""

    Message = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: RfsgSelfTestResult) -> str



"""



class RfsgSignalPath(RfsgSubObject):
    # no doc
    AvailablePorts = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: AvailablePorts(self: RfsgSignalPath) -> str



"""

    SelectedPorts = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedPorts(self: RfsgSignalPath) -> str



Set: SelectedPorts(self: RfsgSignalPath) = value

"""



class RfsgSParameterOrientation(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgSParameterOrientation, values: Port1TowardsDut (24000), Port2TowardsDut (24001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgStartedEvent(RfsgSubObject):
    # no doc
    ExportedOutputTerminal = property(lambda self: RfsgStartedEventExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgStartedEvent) -> RfsgStartedEventExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgStartedEvent) = value

"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgStartedEvent) -> str



"""



class RfsgStartedEventExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgStartedEventExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgStartedEventExportedOutputTerminal, outputTerminal: RfsgStartedEventExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgStartedEventExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgStartedEventExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgStartedEventExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    Pfi4 = None
    Pfi5 = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None


class RfsgStartTrigger(RfsgSubObject):
    # no doc
    def ConfigureSoftwareTrigger(self):
        """ ConfigureSoftwareTrigger(self: RfsgStartTrigger) """
        pass

    def Disable(self):
        """ Disable(self: RfsgStartTrigger) """
        pass

    def SendSoftwareEdgeTrigger(self):
        """ SendSoftwareEdgeTrigger(self: RfsgStartTrigger) """
        pass

    DigitalEdge = property(lambda self: RfsgDigitalEdgeStartTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: DigitalEdge(self: RfsgStartTrigger) -> RfsgDigitalEdgeStartTrigger



"""

    ExportedOutputTerminal = property(lambda self: RfsgStartTriggerExportedOutputTerminal(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedOutputTerminal(self: RfsgStartTrigger) -> RfsgStartTriggerExportedOutputTerminal



Set: ExportedOutputTerminal(self: RfsgStartTrigger) = value

"""

    Synchronized = property(lambda self: RfsgSynchronizedStartTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronized(self: RfsgStartTrigger) -> RfsgSynchronizedStartTrigger



"""

    TerminalName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: TerminalName(self: RfsgStartTrigger) -> str



"""

    TriggerType = property(lambda self: RfsgStartTriggerType(), lambda self, v: None, lambda self: None)  # default
    """Get: TriggerType(self: RfsgStartTrigger) -> RfsgStartTriggerType



Set: TriggerType(self: RfsgStartTrigger) = value

"""



class RfsgStartTriggerExportedOutputTerminal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgStartTriggerExportedOutputTerminal, obj: object) -> bool

        Equals(self: RfsgStartTriggerExportedOutputTerminal, outputTerminal: RfsgStartTriggerExportedOutputTerminal) -> bool
        """
        pass

    @staticmethod
    def FromString(outputTerminal):
        """ FromString(outputTerminal: str) -> RfsgStartTriggerExportedOutputTerminal """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgStartTriggerExportedOutputTerminal) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgStartTriggerExportedOutputTerminal) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    Pfi1 = None
    Pfi4 = None
    Pfi5 = None
    PXIeDStarC = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    TriggerOutputTerminal = None


class RfsgStartTriggerType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgStartTriggerType, values: DigitalEdge (1), None (0), Software (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Software = None
    value__ = None


class RfsgStreaming(RfsgSubObject):
    # no doc
    SpaceAvailableInWaveform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpaceAvailableInWaveform(self: RfsgStreaming) -> Int64



"""

    StreamingEnabled = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: StreamingEnabled(self: RfsgStreaming) -> bool



Set: StreamingEnabled(self: RfsgStreaming) = value

"""

    StreamingWaveformName = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: StreamingWaveformName(self: RfsgStreaming) -> str



Set: StreamingWaveformName(self: RfsgStreaming) = value

"""

    WriteTimeout = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteTimeout(self: RfsgStreaming) -> float



Set: WriteTimeout(self: RfsgStreaming) = value

"""



class RfsgSynchronizedSampleClock(RfsgSubObject):
    # no doc
    DistributionLine = property(lambda self: RfsgSynchronizedSampleClockDistributionLine(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionLine(self: RfsgSynchronizedSampleClock) -> RfsgSynchronizedSampleClockDistributionLine



Set: DistributionLine(self: RfsgSynchronizedSampleClock) = value

"""

    IsMaster = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMaster(self: RfsgSynchronizedSampleClock) -> bool



Set: IsMaster(self: RfsgSynchronizedSampleClock) = value

"""



class RfsgSynchronizedSampleClockDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgSynchronizedSampleClockDistributionLine, obj: object) -> bool

        Equals(self: RfsgSynchronizedSampleClockDistributionLine, distributionLine: RfsgSynchronizedSampleClockDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(distributionLine):
        """ FromString(distributionLine: str) -> RfsgSynchronizedSampleClockDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgSynchronizedSampleClockDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgSynchronizedSampleClockDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None


class RfsgSynchronizedScriptTrigger(RfsgSubObject):
    # no doc
    DistributionLine = property(lambda self: RfsgSynchronizedScriptTriggerDistributionLine(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionLine(self: RfsgSynchronizedScriptTrigger) -> RfsgSynchronizedScriptTriggerDistributionLine



Set: DistributionLine(self: RfsgSynchronizedScriptTrigger) = value

"""

    IsMaster = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMaster(self: RfsgSynchronizedScriptTrigger) -> bool



Set: IsMaster(self: RfsgSynchronizedScriptTrigger) = value

"""



class RfsgSynchronizedScriptTriggerDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgSynchronizedScriptTriggerDistributionLine, obj: object) -> bool

        Equals(self: RfsgSynchronizedScriptTriggerDistributionLine, distributionLine: RfsgSynchronizedScriptTriggerDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(distributionLine):
        """ FromString(distributionLine: str) -> RfsgSynchronizedScriptTriggerDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgSynchronizedScriptTriggerDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgSynchronizedScriptTriggerDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None


class RfsgSynchronizedStartTrigger(RfsgSubObject):
    # no doc
    DistributionLine = property(lambda self: RfsgSynchronizedStartTriggerDistributionLine(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionLine(self: RfsgSynchronizedStartTrigger) -> RfsgSynchronizedStartTriggerDistributionLine



Set: DistributionLine(self: RfsgSynchronizedStartTrigger) = value

"""

    IsMaster = property(lambda self: bool(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMaster(self: RfsgSynchronizedStartTrigger) -> bool



Set: IsMaster(self: RfsgSynchronizedStartTrigger) = value

"""



class RfsgSynchronizedStartTriggerDistributionLine(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgSynchronizedStartTriggerDistributionLine, obj: object) -> bool

        Equals(self: RfsgSynchronizedStartTriggerDistributionLine, distributionLine: RfsgSynchronizedStartTriggerDistributionLine) -> bool
        """
        pass

    @staticmethod
    def FromString(distributionLine):
        """ FromString(distributionLine: str) -> RfsgSynchronizedStartTriggerDistributionLine """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgSynchronizedStartTriggerDistributionLine) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgSynchronizedStartTriggerDistributionLine) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DoNotExport = None
    Pfi0 = None
    PxiTriggerLine0 = None
    PxiTriggerLine1 = None
    PxiTriggerLine2 = None
    PxiTriggerLine3 = None
    PxiTriggerLine4 = None
    PxiTriggerLine5 = None
    PxiTriggerLine6 = None
    PxiTriggerLine7 = None


class RfsgTerminalConfiguration(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgTerminalConfiguration, values: Differential (15000), SingleEnded (15001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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


class RfsgTimerEvent(RfsgSubObject):
    # no doc
    Interval = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Interval(self: RfsgTimerEvent) -> float



Set: Interval(self: RfsgTimerEvent) = value

"""



class RfsgTriggerEdge(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgTriggerEdge, values: FallingEdge (1), RisingEdge (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FallingEdge = None
    RisingEdge = None
    value__ = None


class RfsgTriggerLevel(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgTriggerLevel, values: ActiveHigh (9000), ActiveLow (9001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveHigh = None
    ActiveLow = None
    value__ = None


class RfsgTriggers(RfsgSubObject):
    # no doc
    ConfigurationListStepTrigger = property(lambda self: RfsgConfigurationListStepTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationListStepTrigger(self: RfsgTriggers) -> RfsgConfigurationListStepTrigger



"""

    ScriptTriggers = property(lambda self: RfsgScriptTriggerCollection(), lambda self, v: None, lambda self: None)  # default
    """Get: ScriptTriggers(self: RfsgTriggers) -> RfsgScriptTriggerCollection



"""

    StartTrigger = property(lambda self: RfsgStartTrigger(), lambda self, v: None, lambda self: None)  # default
    """Get: StartTrigger(self: RfsgTriggers) -> RfsgStartTrigger



"""



class RfsgUpconverter(RfsgSubObject):
    # no doc
    CenterFrequency = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterFrequency(self: RfsgUpconverter) -> float



Set: CenterFrequency(self: RfsgUpconverter) = value

"""

    FrequencyOffset = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyOffset(self: RfsgUpconverter) -> float



Set: FrequencyOffset(self: RfsgUpconverter) = value

"""

    FrequencyOffsetMode = property(lambda self: UpconverterFrequencyOffsetMode(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyOffsetMode(self: RfsgUpconverter) -> UpconverterFrequencyOffsetMode



Set: FrequencyOffsetMode(self: RfsgUpconverter) = value

"""

    Gain = property(lambda self: float(), lambda self, v: None, lambda self: None)  # default
    """Get: Gain(self: RfsgUpconverter) -> float



Set: Gain(self: RfsgUpconverter) = value

"""



class RfsgWarning(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: RfsgWarning, obj: object) -> bool

        Equals(self: RfsgWarning, warning: RfsgWarning) -> bool

        Equals(self: RfsgWarning, warning: RfsgWarning, ignoreWarningMessage: bool) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RfsgWarning) -> int """
        pass

    def ToString(self):
        """ ToString(self: RfsgWarning) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: RfsgWarning) -> Guid



"""

    Message = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: RfsgWarning) -> str



"""


    ArbOverflowDigitalGainWarningCode = None
    AwgWarningCode = None
    BandwidthExceededWarningCode = None
    CicFilterOverflowWarningCode = None
    CoercedIQRateNotReadWarningCode = None
    CompensationLimitedWarningCode = None
    FirFilterOverflowWarningCode = None
    InaccurateTemperatureWarningCode = None
    IncompatibleFileVersionWarningCode = None
    InternalWarningCode = None
    InvalidAttenuatorWarningCode = None
    InvalidAttributeNameWarningCode = None
    InvalidCalibrationConstantsWarningCode = None
    IQSumOverflowWarningCode = None
    LOWarningCode = None
    NotPhaseContinuousWarningCode = None
    OutOfRangeWarningCode = None
    OutOfSpecificationUserSettingWarningCode = None
    PowerLevelInaccuracyWarningCode = None
    PowerOutOfRangeWarningCode = None
    ReversePowerProtectionWarningCode = None
    SignalOutsidePassbandWarningCode = None
    UnexpectedDriverWarningCode = None
    UpconverterWarningCode = None


class RfsgWarningEventArgs(EventArgs):
    # no doc
    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: RfsgWarningEventArgs) -> Guid



"""

    Message = property(lambda self: str(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: RfsgWarningEventArgs) -> str



"""

    Warning = property(lambda self: RfsgWarning(), lambda self, v: None, lambda self: None)  # default
    """Get: Warning(self: RfsgWarningEventArgs) -> RfsgWarning



"""



class RfsgWaveformCapabilities(RfsgSubObject):
    # no doc
    MaximumNumberOfWaveforms = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumNumberOfWaveforms(self: RfsgWaveformCapabilities) -> int



"""

    WaveformQuantum = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformQuantum(self: RfsgWaveformCapabilities) -> int



"""

    WaveformSizeMaximum = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformSizeMaximum(self: RfsgWaveformCapabilities) -> int



"""

    WaveformSizeMinimum = property(lambda self: int(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformSizeMinimum(self: RfsgWaveformCapabilities) -> int



"""



class RfsgWaveformGenerationMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgWaveformGenerationMode, values: ArbitraryWaveform (1001), ContinuousWave (1000), Script (1002) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ArbitraryWaveform = None
    ContinuousWave = None
    Script = None
    value__ = None


class RfsgYigMainCoilDriveType(Enum, IComparable, IFormattable, IConvertible):
    """ enum RfsgYigMainCoilDriveType, values: Fast (1), Slow (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Slow = None
    value__ = None


class UpconverterFrequencyOffsetMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum UpconverterFrequencyOffsetMode, values: Auto (-1), Enable (1), UserDefined (5001) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
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
    Enable = None
    UserDefined = None
    value__ = None


