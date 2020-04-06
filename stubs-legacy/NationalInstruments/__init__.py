# encoding: utf-8
# module NationalInstruments
# from NationalInstruments.Common, Version=19.0.40.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AccessibleAfterDisposeAttribute(Attribute, _Attribute):
    """ AccessibleAfterDisposeAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class IWaveform(IServiceProvider):
    # no doc
    def MakeSamplesReadOnly(self):
        """ MakeSamplesReadOnly(self: IWaveform) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: IWaveform) -> int

Set: Capacity(self: IWaveform) = value
"""

    ChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelName(self: IWaveform) -> str

Set: ChannelName(self: IWaveform) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: IWaveform) -> Type

"""

    ExtendedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedProperties(self: IWaveform) -> ExtendedPropertyDictionary

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: IWaveform) -> bool

"""

    SampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleCount(self: IWaveform) -> int

"""

    UnitDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitDescription(self: IWaveform) -> str

Set: UnitDescription(self: IWaveform) = value
"""



class ITimedWaveform(IWaveform, IServiceProvider):
    # no doc
    def GetPrecisionTimeStampBuffer(self):
        """ GetPrecisionTimeStampBuffer(self: ITimedWaveform) -> Buffer[PrecisionDateTime] """
        pass

    def GetPrecisionTimeStamps(self, sampleIndex=None, count=None):
        """
        GetPrecisionTimeStamps(self: ITimedWaveform) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: ITimedWaveform, sampleIndex: int, count: int) -> Array[PrecisionDateTime]
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    PrecisionTiming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTiming(self: ITimedWaveform) -> PrecisionWaveformTiming

Set: PrecisionTiming(self: ITimedWaveform) = value
"""



class AnalogWaveform(object, ITimedWaveform, IWaveform, IServiceProvider, ICloneable, ISerializable):
    """
    AnalogWaveform[TData](sampleCount: int)
    AnalogWaveform[TData](sampleCount: int, capacity: int)
    """
    def Append(self, *__args):
        """ Append(self: AnalogWaveform[TData], data: Array[TData])Append(self: AnalogWaveform[TData], data: Array[TData], timeStamps: Array[PrecisionDateTime])Append(self: AnalogWaveform[TData], data: Array[TData], timeStamps: Array[DateTime])Append(self: AnalogWaveform[TData], waveform: AnalogWaveform[TData])Append(self: AnalogWaveform[TData], waveforms: Array[AnalogWaveform[TData]]) """
        pass

    def Clone(self):
        """ Clone(self: AnalogWaveform[TData]) -> AnalogWaveform[TData] """
        pass

    @staticmethod
    def CopySamples(sourceWaveform, *__args):
        """ CopySamples(sourceWaveform: AnalogWaveform[TData], destinationWaveform: AnalogWaveform[TData], sampleCount: int)CopySamples(sourceWaveform: AnalogWaveform[TData], sourceSampleIndex: int, destinationWaveform: AnalogWaveform[TData], destinationSampleIndex: int, sampleCount: int) """
        pass

    @staticmethod
    def FromArray1D(array):
        """ FromArray1D(array: Array[TData]) -> AnalogWaveform[TData] """
        pass

    @staticmethod
    def FromArray2D(array):
        """ FromArray2D(array: Array[TData]) -> Array[AnalogWaveform[TData]] """
        pass

    def GetBuffer(self, copy):
        """ GetBuffer(self: AnalogWaveform[TData], copy: bool) -> Buffer[TData] """
        pass

    def GetPrecisionTimeStampBuffer(self):
        """ GetPrecisionTimeStampBuffer(self: AnalogWaveform[TData]) -> Buffer[PrecisionDateTime] """
        pass

    def GetPrecisionTimeStamps(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetPrecisionTimeStamps(self: AnalogWaveform[TData]) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: AnalogWaveform[TData], sampleIndex: int, count: int) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[PrecisionDateTime], arrayIndex: int)
        """
        pass

    def GetRawData(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetRawData(self: AnalogWaveform[TData]) -> Array[TData]
        GetRawData(self: AnalogWaveform[TData], sampleIndex: int, count: int) -> Array[TData]
        GetRawData(self: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[TData], arrayIndex: int)
        """
        pass

    def GetScaledData(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetScaledData(self: AnalogWaveform[TData]) -> Array[float]
        GetScaledData(self: AnalogWaveform[TData], sampleIndex: int, count: int) -> Array[float]
        GetScaledData(self: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[float], arrayIndex: int)GetScaledData(self: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[Single], arrayIndex: int)
        """
        pass

    def GetTimeStampBuffer(self):
        """ GetTimeStampBuffer(self: AnalogWaveform[TData]) -> Buffer[DateTime] """
        pass

    def GetTimeStamps(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetTimeStamps(self: AnalogWaveform[TData]) -> Array[DateTime]
        GetTimeStamps(self: AnalogWaveform[TData], sampleIndex: int, count: int) -> Array[DateTime]
        GetTimeStamps(self: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[DateTime], arrayIndex: int)
        """
        pass

    def GetWritableBuffer(self):
        """ GetWritableBuffer(self: AnalogWaveform[TData]) -> WritableBuffer[TData] """
        pass

    def ToString(self):
        """ ToString(self: AnalogWaveform[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sampleCount, capacity=None):
        """
        __new__(cls: type, sampleCount: int)
        __new__(cls: type, sampleCount: int, capacity: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: AnalogWaveform[TData]) -> int

Set: Capacity(self: AnalogWaveform[TData]) = value
"""

    ChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelName(self: AnalogWaveform[TData]) -> str

Set: ChannelName(self: AnalogWaveform[TData]) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: AnalogWaveform[TData]) -> Type

"""

    ExtendedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedProperties(self: AnalogWaveform[TData]) -> ExtendedPropertyDictionary

"""

    IsPrecisionTimingInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrecisionTimingInitialized(self: AnalogWaveform[TData]) -> bool

"""

    PrecisionTiming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTiming(self: AnalogWaveform[TData]) -> PrecisionWaveformTiming

Set: PrecisionTiming(self: AnalogWaveform[TData]) = value
"""

    SampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleCount(self: AnalogWaveform[TData]) -> int

"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Samples(self: AnalogWaveform[TData]) -> AnalogWaveformSampleCollection[TData]

"""

    ScaleMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleMode(self: AnalogWaveform[TData]) -> WaveformScaleMode

Set: ScaleMode(self: AnalogWaveform[TData]) = value
"""

    Timing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Timing(self: AnalogWaveform[TData]) -> WaveformTiming

Set: Timing(self: AnalogWaveform[TData]) = value
"""

    UnitDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitDescription(self: AnalogWaveform[TData]) -> str

Set: UnitDescription(self: AnalogWaveform[TData]) = value
"""



class AnalogWaveformCollection(object, IServiceProvider, ICollection, IEnumerable, ICloneable, ISerializable, ICollection[AnalogWaveform[TData]], IEnumerable[AnalogWaveform[TData]]):
    """ AnalogWaveformCollection[TData]() """
    def Clone(self):
        """ Clone(self: AnalogWaveformCollection[TData]) -> AnalogWaveformCollection[TData] """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: AnalogWaveformCollection[TData], array: Array[AnalogWaveform[TData]], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AnalogWaveformCollection[TData]) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[AnalogWaveform[TData]], item: AnalogWaveform[TData]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Channels(self: AnalogWaveformCollection[TData]) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AnalogWaveformCollection[TData]) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: AnalogWaveformCollection[TData]) -> bool

"""

    Records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Records(self: AnalogWaveformCollection[TData]) -> int

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: AnalogWaveformCollection[TData]) -> object

"""



class AnalogWaveformSample(object):
    # no doc
    def ToString(self):
        """ ToString(self: AnalogWaveformSample[TData]) -> str """
        pass

    HasTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTimeStamp(self: AnalogWaveformSample[TData]) -> bool

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: AnalogWaveformSample[TData]) -> int

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: AnalogWaveformSample[TData]) -> AnalogWaveform[TData]

"""

    PrecisionTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTimeStamp(self: AnalogWaveformSample[TData]) -> PrecisionDateTime

"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: AnalogWaveformSample[TData]) -> DateTime

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: AnalogWaveformSample[TData]) -> TData

Set: Value(self: AnalogWaveformSample[TData]) = value
"""



class AnalogWaveformSampleCollection(object, ICollection, IEnumerable, ICollection[AnalogWaveformSample[TData]], IEnumerable[AnalogWaveformSample[TData]]):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: AnalogWaveformSampleCollection[TData], array: Array[AnalogWaveformSample[TData]], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AnalogWaveformSampleCollection[TData]) -> IEnumerator[AnalogWaveformSample[TData]] """
        pass

    def IndexOf(self, sample):
        """ IndexOf(self: AnalogWaveformSampleCollection[TData], sample: AnalogWaveformSample[TData]) -> int """
        pass

    def ToString(self):
        """ ToString(self: AnalogWaveformSampleCollection[TData]) -> str """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[AnalogWaveformSample[TData]], item: AnalogWaveformSample[TData]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AnalogWaveformSampleCollection[TData]) -> int

"""



class ComplexDouble(object, IFormattable, ISerializable, IEquatable[ComplexDouble]):
    """ ComplexDouble(real: float, imaginary: float) """
    def Add(self, c):
        """ Add(self: ComplexDouble, c: ComplexDouble) -> ComplexDouble """
        pass

    @staticmethod
    def ComposeArray(realData, imaginaryData, startIndex=None, length=None):
        """
        ComposeArray(realData: Array[float], imaginaryData: Array[float]) -> Array[ComplexDouble]
        ComposeArray(realData: Array[float], imaginaryData: Array[float], startIndex: int, length: int) -> Array[ComplexDouble]
        """
        pass

    @staticmethod
    def ComposeArrayPolar(magnitudes, phases, startIndex=None, length=None):
        """
        ComposeArrayPolar(magnitudes: Array[float], phases: Array[float]) -> Array[ComplexDouble]
        ComposeArrayPolar(magnitudes: Array[float], phases: Array[float], startIndex: int, length: int) -> Array[ComplexDouble]
        """
        pass

    @staticmethod
    def DecomposeArray(complexData, *__args):
        """
        DecomposeArray(complexData: Array[ComplexDouble]) -> (Array[float], Array[float])
        DecomposeArray(complexData: Array[ComplexDouble], startIndex: int, length: int) -> (Array[float], Array[float])
        """
        pass

    @staticmethod
    def DecomposeArrayPolar(complexData, *__args):
        """
        DecomposeArrayPolar(complexData: Array[ComplexDouble]) -> (Array[float], Array[float])
        DecomposeArrayPolar(complexData: Array[ComplexDouble], startIndex: int, length: int) -> (Array[float], Array[float])
        """
        pass

    def Divide(self, c):
        """ Divide(self: ComplexDouble, c: ComplexDouble) -> ComplexDouble """
        pass

    def Equals(self, *__args):
        """
        Equals(self: ComplexDouble, other: ComplexDouble) -> bool
        Equals(self: ComplexDouble, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromDouble(real):
        """ FromDouble(real: float) -> ComplexDouble """
        pass

    @staticmethod
    def FromPolar(magnitude, phase):
        """ FromPolar(magnitude: float, phase: float) -> ComplexDouble """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ComplexDouble) -> int """
        pass

    @staticmethod
    def GetMagnitudes(complexData):
        """ GetMagnitudes(complexData: Array[ComplexDouble]) -> Array[float] """
        pass

    @staticmethod
    def GetPhases(complexData):
        """ GetPhases(complexData: Array[ComplexDouble]) -> Array[float] """
        pass

    def Multiply(self, c):
        """ Multiply(self: ComplexDouble, c: ComplexDouble) -> ComplexDouble """
        pass

    def Negate(self):
        """ Negate(self: ComplexDouble) -> ComplexDouble """
        pass

    @staticmethod
    def Parse(input, provider=None):
        """
        Parse(input: str) -> ComplexDouble
        Parse(input: str, provider: IFormatProvider) -> ComplexDouble
        """
        pass

    def Plus(self):
        """ Plus(self: ComplexDouble) -> ComplexDouble """
        pass

    def Subtract(self, c):
        """ Subtract(self: ComplexDouble, c: ComplexDouble) -> ComplexDouble """
        pass

    def ToString(self, *__args):
        """
        ToString(self: ComplexDouble) -> str
        ToString(self: ComplexDouble, format: str) -> str
        ToString(self: ComplexDouble, formatProvider: IFormatProvider) -> str
        ToString(self: ComplexDouble, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str) -> (bool, ComplexDouble)
        TryParse(input: str, provider: IFormatProvider) -> (bool, ComplexDouble)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, real, imaginary):
        """
        __new__[ComplexDouble]() -> ComplexDouble
        
        __new__(cls: type, real: float, imaginary: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(c: ComplexDouble) -> ComplexDouble """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(c1: ComplexDouble, c2: ComplexDouble) -> ComplexDouble """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(c1: ComplexDouble, c2: ComplexDouble) -> ComplexDouble """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(c1: ComplexDouble, c2: ComplexDouble) -> ComplexDouble """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(c1: ComplexDouble, c2: ComplexDouble) -> ComplexDouble """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    ComplexConjugate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComplexConjugate(self: ComplexDouble) -> ComplexDouble

"""

    Imaginary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Imaginary(self: ComplexDouble) -> float

Set: Imaginary(self: ComplexDouble) = value
"""

    Magnitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Magnitude(self: ComplexDouble) -> float

"""

    Phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Phase(self: ComplexDouble) -> float

"""

    Real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Real(self: ComplexDouble) -> float

Set: Real(self: ComplexDouble) = value
"""


    Zero = None


class ComplexInt16(object, IFormattable, ISerializable, IEquatable[ComplexInt16]):
    """ ComplexInt16(real: Int16, imaginary: Int16) """
    def Add(self, c):
        """ Add(self: ComplexInt16, c: ComplexInt16) -> ComplexInt16 """
        pass

    @staticmethod
    def ComposeArray(realData, imaginaryData, startIndex=None, length=None):
        """
        ComposeArray(realData: Array[Int16], imaginaryData: Array[Int16]) -> Array[ComplexInt16]
        ComposeArray(realData: Array[Int16], imaginaryData: Array[Int16], startIndex: int, length: int) -> Array[ComplexInt16]
        """
        pass

    @staticmethod
    def DecomposeArray(complexData, *__args):
        """
        DecomposeArray(complexData: Array[ComplexInt16]) -> (Array[Int16], Array[Int16])
        DecomposeArray(complexData: Array[ComplexInt16], startIndex: int, length: int) -> (Array[Int16], Array[Int16])
        """
        pass

    def Divide(self, c):
        """ Divide(self: ComplexInt16, c: ComplexInt16) -> ComplexInt16 """
        pass

    def Equals(self, *__args):
        """
        Equals(self: ComplexInt16, other: ComplexInt16) -> bool
        Equals(self: ComplexInt16, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromInt16(real):
        """ FromInt16(real: Int16) -> ComplexInt16 """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ComplexInt16) -> int """
        pass

    def Multiply(self, c):
        """ Multiply(self: ComplexInt16, c: ComplexInt16) -> ComplexInt16 """
        pass

    def Negate(self):
        """ Negate(self: ComplexInt16) -> ComplexInt16 """
        pass

    @staticmethod
    def Parse(input, provider=None):
        """
        Parse(input: str) -> ComplexInt16
        Parse(input: str, provider: IFormatProvider) -> ComplexInt16
        """
        pass

    def Plus(self):
        """ Plus(self: ComplexInt16) -> ComplexInt16 """
        pass

    def Subtract(self, c):
        """ Subtract(self: ComplexInt16, c: ComplexInt16) -> ComplexInt16 """
        pass

    def ToString(self, *__args):
        """
        ToString(self: ComplexInt16) -> str
        ToString(self: ComplexInt16, format: str) -> str
        ToString(self: ComplexInt16, formatProvider: IFormatProvider) -> str
        ToString(self: ComplexInt16, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str) -> (bool, ComplexInt16)
        TryParse(input: str, provider: IFormatProvider) -> (bool, ComplexInt16)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, real, imaginary):
        """
        __new__[ComplexInt16]() -> ComplexInt16
        
        __new__(cls: type, real: Int16, imaginary: Int16)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(c: ComplexInt16) -> ComplexInt16 """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(c1: ComplexInt16, c2: ComplexInt16) -> ComplexInt16 """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(c1: ComplexInt16, c2: ComplexInt16) -> ComplexInt16 """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(c1: ComplexInt16, c2: ComplexInt16) -> ComplexInt16 """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(c1: ComplexInt16, c2: ComplexInt16) -> ComplexInt16 """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    ComplexConjugate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComplexConjugate(self: ComplexInt16) -> ComplexInt16

"""

    Imaginary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Imaginary(self: ComplexInt16) -> Int16

Set: Imaginary(self: ComplexInt16) = value
"""

    Real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Real(self: ComplexInt16) -> Int16

Set: Real(self: ComplexInt16) = value
"""


    Zero = None


class ComplexSingle(object, IFormattable, ISerializable, IEquatable[ComplexSingle]):
    """ ComplexSingle(real: Single, imaginary: Single) """
    def Add(self, c):
        """ Add(self: ComplexSingle, c: ComplexSingle) -> ComplexSingle """
        pass

    @staticmethod
    def ComposeArray(realData, imaginaryData, startIndex=None, length=None):
        """
        ComposeArray(realData: Array[Single], imaginaryData: Array[Single]) -> Array[ComplexSingle]
        ComposeArray(realData: Array[Single], imaginaryData: Array[Single], startIndex: int, length: int) -> Array[ComplexSingle]
        """
        pass

    @staticmethod
    def ComposeArrayPolar(magnitudes, phases, startIndex=None, length=None):
        """
        ComposeArrayPolar(magnitudes: Array[Single], phases: Array[Single]) -> Array[ComplexSingle]
        ComposeArrayPolar(magnitudes: Array[Single], phases: Array[Single], startIndex: int, length: int) -> Array[ComplexSingle]
        """
        pass

    @staticmethod
    def DecomposeArray(complexData, *__args):
        """
        DecomposeArray(complexData: Array[ComplexSingle]) -> (Array[Single], Array[Single])
        DecomposeArray(complexData: Array[ComplexSingle], startIndex: int, length: int) -> (Array[Single], Array[Single])
        """
        pass

    @staticmethod
    def DecomposeArrayPolar(complexData, *__args):
        """
        DecomposeArrayPolar(complexData: Array[ComplexSingle]) -> (Array[Single], Array[Single])
        DecomposeArrayPolar(complexData: Array[ComplexSingle], startIndex: int, length: int) -> (Array[Single], Array[Single])
        """
        pass

    def Divide(self, c):
        """ Divide(self: ComplexSingle, c: ComplexSingle) -> ComplexSingle """
        pass

    def Equals(self, *__args):
        """
        Equals(self: ComplexSingle, other: ComplexSingle) -> bool
        Equals(self: ComplexSingle, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromPolar(magnitude, phase):
        """ FromPolar(magnitude: Single, phase: Single) -> ComplexSingle """
        pass

    @staticmethod
    def FromSingle(real):
        """ FromSingle(real: Single) -> ComplexSingle """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ComplexSingle) -> int """
        pass

    @staticmethod
    def GetMagnitudes(complexData):
        """ GetMagnitudes(complexData: Array[ComplexSingle]) -> Array[Single] """
        pass

    @staticmethod
    def GetPhases(complexData):
        """ GetPhases(complexData: Array[ComplexSingle]) -> Array[Single] """
        pass

    def Multiply(self, c):
        """ Multiply(self: ComplexSingle, c: ComplexSingle) -> ComplexSingle """
        pass

    def Negate(self):
        """ Negate(self: ComplexSingle) -> ComplexSingle """
        pass

    @staticmethod
    def Parse(input, provider=None):
        """
        Parse(input: str) -> ComplexSingle
        Parse(input: str, provider: IFormatProvider) -> ComplexSingle
        """
        pass

    def Plus(self):
        """ Plus(self: ComplexSingle) -> ComplexSingle """
        pass

    def Subtract(self, c):
        """ Subtract(self: ComplexSingle, c: ComplexSingle) -> ComplexSingle """
        pass

    def ToString(self, *__args):
        """
        ToString(self: ComplexSingle) -> str
        ToString(self: ComplexSingle, format: str) -> str
        ToString(self: ComplexSingle, formatProvider: IFormatProvider) -> str
        ToString(self: ComplexSingle, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str) -> (bool, ComplexSingle)
        TryParse(input: str, provider: IFormatProvider) -> (bool, ComplexSingle)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, real, imaginary):
        """
        __new__[ComplexSingle]() -> ComplexSingle
        
        __new__(cls: type, real: Single, imaginary: Single)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(c: ComplexSingle) -> ComplexSingle """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(c1: ComplexSingle, c2: ComplexSingle) -> ComplexSingle """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(c1: ComplexSingle, c2: ComplexSingle) -> ComplexSingle """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(c1: ComplexSingle, c2: ComplexSingle) -> ComplexSingle """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(c1: ComplexSingle, c2: ComplexSingle) -> ComplexSingle """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    ComplexConjugate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComplexConjugate(self: ComplexSingle) -> ComplexSingle

"""

    Imaginary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Imaginary(self: ComplexSingle) -> Single

Set: Imaginary(self: ComplexSingle) = value
"""

    Magnitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Magnitude(self: ComplexSingle) -> Single

"""

    Phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Phase(self: ComplexSingle) -> Single

"""

    Real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Real(self: ComplexSingle) -> Single

Set: Real(self: ComplexSingle) = value
"""


    Zero = None


class ComplexWaveform(object, ITimedWaveform, IWaveform, IServiceProvider, ICloneable, ISerializable):
    """
    ComplexWaveform[TData](sampleCount: int)
    ComplexWaveform[TData](sampleCount: int, capacity: int)
    """
    def Append(self, *__args):
        """ Append(self: ComplexWaveform[TData], data: Array[TData])Append(self: ComplexWaveform[TData], data: Array[TData], timeStamps: Array[PrecisionDateTime])Append(self: ComplexWaveform[TData], waveform: ComplexWaveform[TData])Append(self: ComplexWaveform[TData], waveforms: Array[ComplexWaveform[TData]]) """
        pass

    def Clone(self):
        """ Clone(self: ComplexWaveform[TData]) -> ComplexWaveform[TData] """
        pass

    @staticmethod
    def CopySamples(sourceWaveform, *__args):
        """ CopySamples(sourceWaveform: ComplexWaveform[TData], destinationWaveform: ComplexWaveform[TData], sampleCount: int)CopySamples(sourceWaveform: ComplexWaveform[TData], sourceSampleIndex: int, destinationWaveform: ComplexWaveform[TData], destinationSampleIndex: int, sampleCount: int) """
        pass

    @staticmethod
    def FromArray1D(array):
        """ FromArray1D(array: Array[TData]) -> ComplexWaveform[TData] """
        pass

    @staticmethod
    def FromArray2D(array):
        """ FromArray2D(array: Array[TData]) -> Array[ComplexWaveform[TData]] """
        pass

    def GetBuffer(self, copy):
        """ GetBuffer(self: ComplexWaveform[TData], copy: bool) -> Buffer[TData] """
        pass

    def GetImaginaryDataArray(self, applyScaling):
        """ GetImaginaryDataArray(self: ComplexWaveform[TData], applyScaling: bool) -> Array[float] """
        pass

    def GetImaginaryDataWaveform(self, applyScaling):
        """ GetImaginaryDataWaveform(self: ComplexWaveform[TData], applyScaling: bool) -> AnalogWaveform[float] """
        pass

    def GetMagnitudeDataArray(self, applyScaling):
        """ GetMagnitudeDataArray(self: ComplexWaveform[TData], applyScaling: bool) -> Array[float] """
        pass

    def GetMagnitudeDataWaveform(self, applyScaling):
        """ GetMagnitudeDataWaveform(self: ComplexWaveform[TData], applyScaling: bool) -> AnalogWaveform[float] """
        pass

    def GetPhaseDataArray(self, applyScaling):
        """ GetPhaseDataArray(self: ComplexWaveform[TData], applyScaling: bool) -> Array[float] """
        pass

    def GetPhaseDataWaveform(self, applyScaling):
        """ GetPhaseDataWaveform(self: ComplexWaveform[TData], applyScaling: bool) -> AnalogWaveform[float] """
        pass

    def GetPrecisionTimeStampBuffer(self):
        """ GetPrecisionTimeStampBuffer(self: ComplexWaveform[TData]) -> Buffer[PrecisionDateTime] """
        pass

    def GetPrecisionTimeStamps(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetPrecisionTimeStamps(self: ComplexWaveform[TData]) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: ComplexWaveform[TData], sampleIndex: int, count: int) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: ComplexWaveform[TData], sampleIndex: int, count: int, buffer: Array[PrecisionDateTime], arrayIndex: int)
        """
        pass

    def GetRawData(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetRawData(self: ComplexWaveform[TData]) -> Array[TData]
        GetRawData(self: ComplexWaveform[TData], sampleIndex: int, count: int) -> Array[TData]
        GetRawData(self: ComplexWaveform[TData], sampleIndex: int, count: int, buffer: Array[TData], arrayIndex: int)
        """
        pass

    def GetRealDataArray(self, applyScaling):
        """ GetRealDataArray(self: ComplexWaveform[TData], applyScaling: bool) -> Array[float] """
        pass

    def GetRealDataWaveform(self, applyScaling):
        """ GetRealDataWaveform(self: ComplexWaveform[TData], applyScaling: bool) -> AnalogWaveform[float] """
        pass

    def GetScaledData(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetScaledData(self: ComplexWaveform[TData]) -> Array[ComplexDouble]
        GetScaledData(self: ComplexWaveform[TData], sampleIndex: int, count: int) -> Array[ComplexDouble]
        GetScaledData(self: ComplexWaveform[TData], sampleIndex: int, count: int, buffer: Array[ComplexDouble], arrayIndex: int)GetScaledData(self: ComplexWaveform[TData], sampleIndex: int, count: int, buffer: Array[ComplexSingle], arrayIndex: int)
        """
        pass

    def GetWritableBuffer(self):
        """ GetWritableBuffer(self: ComplexWaveform[TData]) -> WritableBuffer[TData] """
        pass

    def ToString(self):
        """ ToString(self: ComplexWaveform[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sampleCount, capacity=None):
        """
        __new__(cls: type, sampleCount: int)
        __new__(cls: type, sampleCount: int, capacity: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: ComplexWaveform[TData]) -> int

Set: Capacity(self: ComplexWaveform[TData]) = value
"""

    ChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelName(self: ComplexWaveform[TData]) -> str

Set: ChannelName(self: ComplexWaveform[TData]) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: ComplexWaveform[TData]) -> Type

"""

    ExtendedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedProperties(self: ComplexWaveform[TData]) -> ExtendedPropertyDictionary

"""

    PrecisionTiming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTiming(self: ComplexWaveform[TData]) -> PrecisionWaveformTiming

Set: PrecisionTiming(self: ComplexWaveform[TData]) = value
"""

    SampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleCount(self: ComplexWaveform[TData]) -> int

"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Samples(self: ComplexWaveform[TData]) -> ComplexWaveformSampleCollection[TData]

"""

    ScaleMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleMode(self: ComplexWaveform[TData]) -> ComplexWaveformScaleMode

Set: ScaleMode(self: ComplexWaveform[TData]) = value
"""

    UnitDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitDescription(self: ComplexWaveform[TData]) -> str

Set: UnitDescription(self: ComplexWaveform[TData]) = value
"""



class ComplexWaveformCollection(object, ICloneable, ISerializable, IServiceProvider, ICollection, IEnumerable, ICollection[ComplexWaveform[TData]], IEnumerable[ComplexWaveform[TData]]):
    """ ComplexWaveformCollection[TData]() """
    def Clone(self):
        """ Clone(self: ComplexWaveformCollection[TData]) -> ComplexWaveformCollection[TData] """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: ComplexWaveformCollection[TData], array: Array[ComplexWaveform[TData]], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ComplexWaveformCollection[TData]) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[ComplexWaveform[TData]], item: ComplexWaveform[TData]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Channels(self: ComplexWaveformCollection[TData]) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ComplexWaveformCollection[TData]) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: ComplexWaveformCollection[TData]) -> bool

"""

    Records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Records(self: ComplexWaveformCollection[TData]) -> int

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: ComplexWaveformCollection[TData]) -> object

"""



class ComplexWaveformSample(object):
    # no doc
    def ToString(self):
        """ ToString(self: ComplexWaveformSample[TData]) -> str """
        pass

    HasTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTimeStamp(self: ComplexWaveformSample[TData]) -> bool

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: ComplexWaveformSample[TData]) -> int

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: ComplexWaveformSample[TData]) -> ComplexWaveform[TData]

"""

    PrecisionTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTimeStamp(self: ComplexWaveformSample[TData]) -> PrecisionDateTime

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ComplexWaveformSample[TData]) -> TData

Set: Value(self: ComplexWaveformSample[TData]) = value
"""



class ComplexWaveformSampleCollection(object, ICollection, IEnumerable, ICollection[ComplexWaveformSample[TData]], IEnumerable[ComplexWaveformSample[TData]]):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: ComplexWaveformSampleCollection[TData], array: Array[ComplexWaveformSample[TData]], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ComplexWaveformSampleCollection[TData]) -> IEnumerator[ComplexWaveformSample[TData]] """
        pass

    def IndexOf(self, sample):
        """ IndexOf(self: ComplexWaveformSampleCollection[TData], sample: ComplexWaveformSample[TData]) -> int """
        pass

    def ToString(self):
        """ ToString(self: ComplexWaveformSampleCollection[TData]) -> str """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[ComplexWaveformSample[TData]], item: ComplexWaveformSample[TData]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ComplexWaveformSampleCollection[TData]) -> int

"""



class ComplexWaveformScaleMode(object):
    # no doc
    @staticmethod
    def CreateLinearMode(gain, offset):
        """ CreateLinearMode(gain: float, offset: float) -> ComplexWaveformScaleMode """
        pass

    def GetPropertyValues(self, *args): #cannot find CLR method
        """ GetPropertyValues(self: ComplexWaveformScaleMode) -> IEnumerable[KeyValuePair[str, object]] """
        pass

    def GetScaledData(self, waveform, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetScaledData[TData](self: ComplexWaveformScaleMode, waveform: ComplexWaveform[TData]) -> Array[ComplexDouble]
        GetScaledData[TData](self: ComplexWaveformScaleMode, waveform: ComplexWaveform[TData], sampleIndex: int, count: int) -> Array[ComplexDouble]
        GetScaledData[TData](self: ComplexWaveformScaleMode, waveform: ComplexWaveform[TData], sampleIndex: int, count: int, buffer: Array[ComplexDouble], arrayIndex: int)GetScaledData[TData](self: ComplexWaveformScaleMode, waveform: ComplexWaveform[TData], sampleIndex: int, count: int, buffer: Array[ComplexSingle], arrayIndex: int)
        """
        pass

    def TransformData(self, *args): #cannot find CLR method
        """
        TransformData(self: ComplexWaveformScaleMode, data: Array[ComplexDouble]) -> Array[ComplexDouble]
        TransformData(self: ComplexWaveformScaleMode, data: Array[ComplexSingle]) -> Array[ComplexSingle]
        """
        pass

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: ComplexWaveformScaleMode) -> ExtendedPropertyDictionary

"""


    None = None


class ISupportSynchronizationContext:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SynchronizeCallbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizeCallbacks(self: ISupportSynchronizationContext) -> bool

Set: SynchronizeCallbacks(self: ISupportSynchronizationContext) = value
"""



class ISynchronizeCallbacks:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    SynchronizingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizingObject(self: ISynchronizeCallbacks) -> ISynchronizeInvoke

Set: SynchronizingObject(self: ISynchronizeCallbacks) = value
"""



class ComponentBase(Component, IComponent, IDisposable, ISupportSynchronizationContext, ISynchronizeCallbacks, IServiceProvider):
    # no doc
    def AddEventHandler(self, *args): #cannot find CLR method
        """ AddEventHandler(self: ComponentBase, eventKey: object, handler: Delegate) """
        pass

    def Dispose(self):
        """ Dispose(self: ComponentBase, disposing: bool) """
        pass

    def GetService(self, *args): #cannot find CLR method
        """ GetService(self: ComponentBase, service: Type) -> object """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value 
             of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote 
             server object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def OnSynchronizingObjectChanged(self, *args): #cannot find CLR method
        """ OnSynchronizingObjectChanged(self: ComponentBase, e: EventArgs) """
        pass

    def RaiseEvent(self, *args): #cannot find CLR method
        """ RaiseEvent(self: ComponentBase, eventKey: object, e: EventArgs) """
        pass

    def RaiseEventAsync(self, *args): #cannot find CLR method
        """ RaiseEventAsync(self: ComponentBase, eventKey: object, e: EventArgs) """
        pass

    def RaiseEventDirect(self, *args): #cannot find CLR method
        """ RaiseEventDirect(self: ComponentBase, eventKey: object, e: EventArgs) """
        pass

    def RaiseExceptionIfDisposed(self, *args): #cannot find CLR method
        """ RaiseExceptionIfDisposed(self: ComponentBase) """
        pass

    def RaiseGenericEvent(self, *args): #cannot find CLR method
        """ RaiseGenericEvent[TEventArgs](self: ComponentBase, eventKey: object, e: TEventArgs)RaiseGenericEvent[TEventArgs](self: ComponentBase, operation: AsyncOperation, callback: EventSynchronizationCallback[TEventArgs], e: TEventArgs) """
        pass

    def RaiseGenericEventAsync(self, *args): #cannot find CLR method
        """ RaiseGenericEventAsync[TEventArgs](self: ComponentBase, eventKey: object, e: TEventArgs)RaiseGenericEventAsync[TEventArgs](self: ComponentBase, operation: AsyncOperation, callback: EventSynchronizationCallback[TEventArgs], e: TEventArgs) """
        pass

    def RaiseGenericEventDirect(self, *args): #cannot find CLR method
        """ RaiseGenericEventDirect[TEventArgs](self: ComponentBase, eventKey: object, e: TEventArgs) """
        pass

    def RemoveEventHandler(self, *args): #cannot find CLR method
        """ RemoveEventHandler(self: ComponentBase, eventKey: object, handler: Delegate) """
        pass

    def ThrowExceptionIfDisposed(self, *args): #cannot find CLR method
        """ ThrowExceptionIfDisposed(self: ComponentBase) """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the component can raise an event.

"""

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: ComponentBase) -> bool

"""

    SynchronizeCallbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizeCallbacks(self: ComponentBase) -> bool

Set: SynchronizeCallbacks(self: ComponentBase) = value
"""

    SynchronizingObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizingObject(self: ComponentBase) -> ISynchronizeInvoke

Set: SynchronizingObject(self: ComponentBase) = value
"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tag(self: ComponentBase) -> object

Set: Tag(self: ComponentBase) = value
"""


    SynchronizingObjectChanged = None


class DataConverter(object):
    # no doc
    @staticmethod
    def CanConvert(source, targetType=None):
        """
        CanConvert(source: object, targetType: Type) -> bool
        CanConvert[TData](source: object) -> bool
        """
        pass

    @staticmethod
    def Convert(*__args):
        """
        Convert(source: object, targetType: Type) -> object
        Convert[TData](source: object) -> TData
        Convert[TData](sourceDateTime: DateTime) -> TData
        Convert[TData](sourcePrecisionDateTime: PrecisionDateTime) -> TData
        Convert[TData](sourceTimeSpan: TimeSpan) -> TData
        Convert[TData](sourcePrecisionTimeSpan: PrecisionTimeSpan) -> TData
        """
        pass


class DigitalState(Enum, IComparable, IFormattable, IConvertible):
    """ enum DigitalState, values: CompareHigh (4), CompareLow (3), CompareOff (6), CompareUnknown (5), CompareValid (7), ForceDown (0), ForceOff (2), ForceUp (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CompareHigh = None
    CompareLow = None
    CompareOff = None
    CompareUnknown = None
    CompareValid = None
    ForceDown = None
    ForceOff = None
    ForceUp = None
    value__ = None


class DigitalStateCollection(object, ICollection, IEnumerable, ICollection[DigitalState], IEnumerable[DigitalState]):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: DigitalStateCollection, array: Array[DigitalState], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DigitalStateCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[DigitalState], item: DigitalState) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DigitalStateCollection) -> int

"""



class DigitalStateUtility(object):
    # no doc
    @staticmethod
    def Test(state1, state2):
        """ Test(state1: DigitalState, state2: DigitalState) -> bool """
        pass

    @staticmethod
    def ToChar(state):
        """ ToChar(state: DigitalState) -> Char """
        pass

    @staticmethod
    def TryGetChar(state, charState):
        """ TryGetChar(state: DigitalState) -> (bool, Char) """
        pass

    @staticmethod
    def TryGetState(input, state):
        """ TryGetState(input: Char) -> (bool, DigitalState) """
        pass


class DigitalWaveform(object, ITimedWaveform, IWaveform, IServiceProvider, ISerializable, ICloneable):
    """
    DigitalWaveform(sampleCount: int, signalCount: int)
    DigitalWaveform(sampleCount: int, signalCount: int, defaultValue: DigitalState)
    """
    def Clone(self):
        """ Clone(self: DigitalWaveform) -> DigitalWaveform """
        pass

    @staticmethod
    def CopyStates(sourceWaveform, *__args):
        """ CopyStates(sourceWaveform: DigitalWaveform, destinationWaveform: DigitalWaveform, sampleCount: int, signalCount: int)CopyStates(sourceWaveform: DigitalWaveform, sourceSampleIndex: int, sourceSignalIndex: int, destinationWaveform: DigitalWaveform, destinationSampleIndex: int, destinationSignalIndex: int, sampleCount: int, signalCount: int) """
        pass

    @staticmethod
    def FromPort(samples, mask=None):
        """
        FromPort(samples: Array[Byte]) -> DigitalWaveform
        FromPort(samples: Array[Byte], mask: Byte) -> DigitalWaveform
        FromPort(samples: Array[Int16]) -> DigitalWaveform
        FromPort(samples: Array[Int16], mask: Int16) -> DigitalWaveform
        FromPort(samples: Array[UInt16]) -> DigitalWaveform
        FromPort(samples: Array[UInt16], mask: UInt16) -> DigitalWaveform
        FromPort(samples: Array[int]) -> DigitalWaveform
        FromPort(samples: Array[int], mask: int) -> DigitalWaveform
        FromPort(samples: Array[UInt32]) -> DigitalWaveform
        FromPort(samples: Array[UInt32], mask: UInt32) -> DigitalWaveform
        """
        pass

    @staticmethod
    def FromPorts(samples, masks=None):
        """
        FromPorts(samples: Array[Byte]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[Byte], masks: Array[Byte]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[Int16]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[Int16], masks: Array[Int16]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[UInt16]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[UInt16], masks: Array[UInt16]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[int]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[int], masks: Array[int]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[UInt32]) -> Array[DigitalWaveform]
        FromPorts(samples: Array[UInt32], masks: Array[UInt32]) -> Array[DigitalWaveform]
        """
        pass

    def GetBuffer(self, copy):
        """ GetBuffer(self: DigitalWaveform, copy: bool) -> Buffer[DigitalSample] """
        pass

    def GetPrecisionTimeStampBuffer(self):
        """ GetPrecisionTimeStampBuffer(self: DigitalWaveform) -> Buffer[PrecisionDateTime] """
        pass

    def GetPrecisionTimeStamps(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetPrecisionTimeStamps(self: DigitalWaveform) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: DigitalWaveform, sampleIndex: int, count: int) -> Array[PrecisionDateTime]
        GetPrecisionTimeStamps(self: DigitalWaveform, sampleIndex: int, count: int, buffer: Array[PrecisionDateTime], arrayIndex: int)
        """
        pass

    def GetTimeStampBuffer(self):
        """ GetTimeStampBuffer(self: DigitalWaveform) -> Buffer[DateTime] """
        pass

    def GetTimeStamps(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetTimeStamps(self: DigitalWaveform) -> Array[DateTime]
        GetTimeStamps(self: DigitalWaveform, sampleIndex: int, count: int) -> Array[DateTime]
        GetTimeStamps(self: DigitalWaveform, sampleIndex: int, count: int, buffer: Array[DateTime], arrayIndex: int)
        """
        pass

    def GetWritableBuffer(self):
        """ GetWritableBuffer(self: DigitalWaveform) -> WritableBuffer[DigitalSample] """
        pass

    def Test(self, *__args):
        """
        Test(self: DigitalWaveform, expectedWaveform: DigitalWaveform) -> DigitalWaveformTestResult
        Test(self: DigitalWaveform, startSample: int, expectedWaveform: DigitalWaveform, expectedStartSample: int, sampleCount: int) -> DigitalWaveformTestResult
        """
        pass

    def ToString(self):
        """ ToString(self: DigitalWaveform) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sampleCount, signalCount, defaultValue=None):
        """
        __new__(cls: type, sampleCount: int, signalCount: int)
        __new__(cls: type, sampleCount: int, signalCount: int, defaultValue: DigitalState)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelName(self: DigitalWaveform) -> str

Set: ChannelName(self: DigitalWaveform) = value
"""

    ExtendedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedProperties(self: DigitalWaveform) -> ExtendedPropertyDictionary

"""

    IsPrecisionTimingInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrecisionTimingInitialized(self: DigitalWaveform) -> bool

"""

    PrecisionTiming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTiming(self: DigitalWaveform) -> PrecisionWaveformTiming

Set: PrecisionTiming(self: DigitalWaveform) = value
"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Samples(self: DigitalWaveform) -> DigitalWaveformSampleCollection

"""

    Signals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Signals(self: DigitalWaveform) -> DigitalWaveformSignalCollection

"""

    Timing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Timing(self: DigitalWaveform) -> WaveformTiming

Set: Timing(self: DigitalWaveform) = value
"""



class DigitalWaveformFailure(object, ISerializable):
    # no doc
    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: DigitalWaveformFailure, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ActualState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualState(self: DigitalWaveformFailure) -> DigitalState

"""

    ExpectedSampleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpectedSampleIndex(self: DigitalWaveformFailure) -> int

"""

    ExpectedState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpectedState(self: DigitalWaveformFailure) -> DigitalState

"""

    SampleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleIndex(self: DigitalWaveformFailure) -> int

"""

    SignalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalIndex(self: DigitalWaveformFailure) -> int

"""



class DigitalWaveformSample(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: DigitalWaveformSample, obj: object) -> bool
        Equals(self: DigitalWaveformSample, sample: DigitalWaveformSample) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DigitalWaveformSample) -> int """
        pass

    def TryConvert(self, busValue):
        """ TryConvert(self: DigitalWaveformSample) -> (bool, Int64) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    HasTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTimeStamp(self: DigitalWaveformSample) -> bool

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: DigitalWaveformSample) -> DigitalWaveform

"""

    PrecisionTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrecisionTimeStamp(self: DigitalWaveformSample) -> PrecisionDateTime

"""

    States = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: States(self: DigitalWaveformSample) -> DigitalStateCollection

"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: DigitalWaveformSample) -> DateTime

"""



class DigitalWaveformSampleCollection(object, ICollection, IEnumerable, ICollection[DigitalWaveformSample], IEnumerable[DigitalWaveformSample]):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: DigitalWaveformSampleCollection, array: Array[DigitalWaveformSample], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DigitalWaveformSampleCollection) -> IEnumerator """
        pass

    def IndexOf(self, sample):
        """ IndexOf(self: DigitalWaveformSampleCollection, sample: DigitalWaveformSample) -> int """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[DigitalWaveformSample], item: DigitalWaveformSample) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DigitalWaveformSampleCollection) -> int

"""



class DigitalWaveformSignal(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: DigitalWaveformSignal, obj: object) -> bool
        Equals(self: DigitalWaveformSignal, signal: DigitalWaveformSignal) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DigitalWaveformSignal) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DigitalWaveformSignal) -> str

Set: Name(self: DigitalWaveformSignal) = value
"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: DigitalWaveformSignal) -> DigitalWaveform

"""

    States = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: States(self: DigitalWaveformSignal) -> DigitalStateCollection

"""



class DigitalWaveformSignalCollection(object, ICollection, IEnumerable, ICollection[DigitalWaveformSignal], IEnumerable[DigitalWaveformSignal]):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: DigitalWaveformSignalCollection, array: Array[DigitalWaveformSignal], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DigitalWaveformSignalCollection) -> IEnumerator """
        pass

    def IndexOf(self, signal):
        """ IndexOf(self: DigitalWaveformSignalCollection, signal: DigitalWaveformSignal) -> int """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[DigitalWaveformSignal], item: DigitalWaveformSignal) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DigitalWaveformSignalCollection) -> int

"""



class DigitalWaveformTestResult(object, ISerializable):
    # no doc
    def GetFailures(self):
        """ GetFailures(self: DigitalWaveformTestResult) -> Array[DigitalWaveformFailure] """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: DigitalWaveformTestResult, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Success = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Success(self: DigitalWaveformTestResult) -> bool

"""



class EngineeringFormatInfo(object, IFormatProvider, ICustomFormatter, ICloneable, ISerializable):
    """ EngineeringFormatInfo() """
    def Clone(self):
        """ Clone(self: EngineeringFormatInfo) -> object """
        pass

    def Format(self, format, arg, formatProvider):
        """ Format(self: EngineeringFormatInfo, format: str, arg: object, formatProvider: IFormatProvider) -> str """
        pass

    def GetFormat(self, formatType):
        """ GetFormat(self: EngineeringFormatInfo, formatType: Type) -> object """
        pass

    @staticmethod
    def GetInstance(provider):
        """ GetInstance(provider: IFormatProvider) -> EngineeringFormatInfo """
        pass

    def Parse(self, format, s, formatProvider=None):
        """
        Parse(self: EngineeringFormatInfo, format: str, s: str) -> float
        Parse(self: EngineeringFormatInfo, format: str, s: str, formatProvider: IFormatProvider) -> float
        """
        pass

    @staticmethod
    def ReadOnly(efi):
        """ ReadOnly(efi: EngineeringFormatInfo) -> EngineeringFormatInfo """
        pass

    def TryParse(self, format, s, formatProvider, value):
        """ TryParse(self: EngineeringFormatInfo, format: str, s: str, formatProvider: IFormatProvider) -> (bool, float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AttoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttoPrefix(self: EngineeringFormatInfo) -> str

Set: AttoPrefix(self: EngineeringFormatInfo) = value
"""

    AttoSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttoSymbol(self: EngineeringFormatInfo) -> str

Set: AttoSymbol(self: EngineeringFormatInfo) = value
"""

    ExaPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExaPrefix(self: EngineeringFormatInfo) -> str

Set: ExaPrefix(self: EngineeringFormatInfo) = value
"""

    ExaSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExaSymbol(self: EngineeringFormatInfo) -> str

Set: ExaSymbol(self: EngineeringFormatInfo) = value
"""

    FemtoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FemtoPrefix(self: EngineeringFormatInfo) -> str

Set: FemtoPrefix(self: EngineeringFormatInfo) = value
"""

    FemtoSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FemtoSymbol(self: EngineeringFormatInfo) -> str

Set: FemtoSymbol(self: EngineeringFormatInfo) = value
"""

    GigaPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GigaPrefix(self: EngineeringFormatInfo) -> str

Set: GigaPrefix(self: EngineeringFormatInfo) = value
"""

    GigaSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GigaSymbol(self: EngineeringFormatInfo) -> str

Set: GigaSymbol(self: EngineeringFormatInfo) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: EngineeringFormatInfo) -> bool

"""

    KiloPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KiloPrefix(self: EngineeringFormatInfo) -> str

Set: KiloPrefix(self: EngineeringFormatInfo) = value
"""

    KiloSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KiloSymbol(self: EngineeringFormatInfo) -> str

Set: KiloSymbol(self: EngineeringFormatInfo) = value
"""

    MegaPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MegaPrefix(self: EngineeringFormatInfo) -> str

Set: MegaPrefix(self: EngineeringFormatInfo) = value
"""

    MegaSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MegaSymbol(self: EngineeringFormatInfo) -> str

Set: MegaSymbol(self: EngineeringFormatInfo) = value
"""

    MicroPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MicroPrefix(self: EngineeringFormatInfo) -> str

Set: MicroPrefix(self: EngineeringFormatInfo) = value
"""

    MicroSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MicroSymbol(self: EngineeringFormatInfo) -> str

Set: MicroSymbol(self: EngineeringFormatInfo) = value
"""

    MilliPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MilliPrefix(self: EngineeringFormatInfo) -> str

Set: MilliPrefix(self: EngineeringFormatInfo) = value
"""

    MilliSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MilliSymbol(self: EngineeringFormatInfo) -> str

Set: MilliSymbol(self: EngineeringFormatInfo) = value
"""

    NanoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NanoPrefix(self: EngineeringFormatInfo) -> str

Set: NanoPrefix(self: EngineeringFormatInfo) = value
"""

    NanoSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NanoSymbol(self: EngineeringFormatInfo) -> str

Set: NanoSymbol(self: EngineeringFormatInfo) = value
"""

    PetaPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PetaPrefix(self: EngineeringFormatInfo) -> str

Set: PetaPrefix(self: EngineeringFormatInfo) = value
"""

    PetaSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PetaSymbol(self: EngineeringFormatInfo) -> str

Set: PetaSymbol(self: EngineeringFormatInfo) = value
"""

    PicoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PicoPrefix(self: EngineeringFormatInfo) -> str

Set: PicoPrefix(self: EngineeringFormatInfo) = value
"""

    PicoSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PicoSymbol(self: EngineeringFormatInfo) -> str

Set: PicoSymbol(self: EngineeringFormatInfo) = value
"""

    TeraPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TeraPrefix(self: EngineeringFormatInfo) -> str

Set: TeraPrefix(self: EngineeringFormatInfo) = value
"""

    TeraSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TeraSymbol(self: EngineeringFormatInfo) -> str

Set: TeraSymbol(self: EngineeringFormatInfo) = value
"""

    YoctoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YoctoPrefix(self: EngineeringFormatInfo) -> str

Set: YoctoPrefix(self: EngineeringFormatInfo) = value
"""

    YoctoSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YoctoSymbol(self: EngineeringFormatInfo) -> str

Set: YoctoSymbol(self: EngineeringFormatInfo) = value
"""

    YottaPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YottaPrefix(self: EngineeringFormatInfo) -> str

Set: YottaPrefix(self: EngineeringFormatInfo) = value
"""

    YottaSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YottaSymbol(self: EngineeringFormatInfo) -> str

Set: YottaSymbol(self: EngineeringFormatInfo) = value
"""

    ZeptoPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZeptoPrefix(self: EngineeringFormatInfo) -> str

Set: ZeptoPrefix(self: EngineeringFormatInfo) = value
"""

    ZeptoSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZeptoSymbol(self: EngineeringFormatInfo) -> str

Set: ZeptoSymbol(self: EngineeringFormatInfo) = value
"""

    ZettaPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZettaPrefix(self: EngineeringFormatInfo) -> str

Set: ZettaPrefix(self: EngineeringFormatInfo) = value
"""

    ZettaSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZettaSymbol(self: EngineeringFormatInfo) -> str

Set: ZettaSymbol(self: EngineeringFormatInfo) = value
"""


    Default = None


class EnumObject(object, IComparable):
    # no doc
    def CompareParameters(self, *args): #cannot find CLR method
        """ CompareParameters(self: EnumObject, other: EnumObject) -> int """
        pass

    def CompareTo(self, obj):
        """ CompareTo(self: EnumObject, obj: object) -> int """
        pass

    def Equals(self, obj):
        """ Equals(self: EnumObject, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EnumObject) -> int """
        pass

    @staticmethod
    def GetNames(type):
        """ GetNames(type: Type) -> Array[str] """
        pass

    @staticmethod
    def GetValues(type=None):
        """
        GetValues(type: Type) -> Array
        GetValues[T]() -> Array[T]
        """
        pass

    @staticmethod
    def Parse(type, value, ignoreCase=None):
        """
        Parse(type: Type, value: str) -> object
        Parse(type: Type, value: str, ignoreCase: bool) -> object
        """
        pass

    def ToString(self):
        """ ToString(self: EnumObject) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EnumObject) -> str

"""

    UnderlyingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnderlyingType(self: EnumObject) -> Type

"""



class EventSynchronizationCallback(MulticastDelegate, ICloneable, ISerializable):
    """ EventSynchronizationCallback[TEventArgs](object: object, method: IntPtr) """
    def BeginInvoke(self, e, callback, object):
        """ BeginInvoke(self: EventSynchronizationCallback[TEventArgs], e: TEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.  
         -or-  
         ll, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EventSynchronizationCallback[TEventArgs], result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, e):
        """ Invoke(self: EventSynchronizationCallback[TEventArgs], e: TEventArgs) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class ExtendedPropertyDictionary(object, IDictionary, ICollection, IEnumerable, ISerializable, ICloneable):
    """ ExtendedPropertyDictionary() """
    def Add(self, key, value):
        """ Add(self: ExtendedPropertyDictionary, key: str, value: object) """
        pass

    def Clear(self):
        """ Clear(self: ExtendedPropertyDictionary) """
        pass

    def Clone(self):
        """ Clone(self: ExtendedPropertyDictionary) -> ExtendedPropertyDictionary """
        pass

    def Contains(self, key):
        """ Contains(self: ExtendedPropertyDictionary, key: str) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ExtendedPropertyDictionary) -> IDictionaryEnumerator """
        pass

    def GetObjectData(self, *args): #cannot find CLR method
        """ GetObjectData(self: ExtendedPropertyDictionary, info: SerializationInfo, context: StreamingContext) """
        pass

    def Remove(self, key):
        """ Remove(self: ExtendedPropertyDictionary, key: str) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: IDictionary, key: object) -> bool
        
            Determines whether the System.Collections.IDictionary object contains an element with the 
             specified key.
        
        
            key: The key to locate in the System.Collections.IDictionary object.
            Returns: ue if the System.Collections.IDictionary contains an element with the key; otherwise, lse.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ExtendedPropertyDictionary) -> int

"""

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: ExtendedPropertyDictionary) -> ICollection

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: ExtendedPropertyDictionary) -> ICollection

"""



class IIndicateDisposed(IDisposable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: IIndicateDisposed) -> bool

"""



class PrecisionDateTime(object, ISerializable, IComparable, IFormattable, IConvertible, IComparable[PrecisionDateTime], IEquatable[PrecisionDateTime], IServiceProvider):
    """
    PrecisionDateTime(wholeSeconds: Int64, fractionalSecondTicks: UInt64)
    PrecisionDateTime(wholeSeconds: Int64, fractionalSecondTicks: UInt64, kind: DateTimeKind)
    PrecisionDateTime(wholeSeconds: Int64, fractionalSecondTicks: Int64)
    PrecisionDateTime(wholeSeconds: Int64, fractionalSecondTicks: Int64, kind: DateTimeKind)
    PrecisionDateTime(dateTime: DateTime)
    PrecisionDateTime(seconds: float)
    PrecisionDateTime(seconds: float, kind: DateTimeKind)
    """
    def Add(self, value):
        """ Add(self: PrecisionDateTime, value: PrecisionTimeSpan) -> PrecisionDateTime """
        pass

    def AddDays(self, value):
        """ AddDays(self: PrecisionDateTime, value: float) -> PrecisionDateTime """
        pass

    def AddHours(self, value):
        """ AddHours(self: PrecisionDateTime, value: float) -> PrecisionDateTime """
        pass

    def AddMilliseconds(self, value):
        """ AddMilliseconds(self: PrecisionDateTime, value: float) -> PrecisionDateTime """
        pass

    def AddMinutes(self, value):
        """ AddMinutes(self: PrecisionDateTime, value: float) -> PrecisionDateTime """
        pass

    def AddMonths(self, value):
        """ AddMonths(self: PrecisionDateTime, value: int) -> PrecisionDateTime """
        pass

    def AddSeconds(self, value):
        """ AddSeconds(self: PrecisionDateTime, value: float) -> PrecisionDateTime """
        pass

    def AddYears(self, value):
        """ AddYears(self: PrecisionDateTime, value: int) -> PrecisionDateTime """
        pass

    @staticmethod
    def Compare(precisionDateTime1, precisionDateTime2):
        """ Compare(precisionDateTime1: PrecisionDateTime, precisionDateTime2: PrecisionDateTime) -> int """
        pass

    def CompareTo(self, *__args):
        """
        CompareTo(self: PrecisionDateTime, obj: object) -> int
        CompareTo(self: PrecisionDateTime, other: PrecisionDateTime) -> int
        """
        pass

    @staticmethod
    def DaysInMonth(year, month):
        """ DaysInMonth(year: int, month: int) -> int """
        pass

    def Equals(self, *__args):
        """
        Equals(self: PrecisionDateTime, obj: object) -> bool
        Equals(self: PrecisionDateTime, other: PrecisionDateTime) -> bool
        Equals(t1: PrecisionDateTime, t2: PrecisionDateTime) -> bool
        """
        pass

    @staticmethod
    def FromCTime(seconds, kind=None):
        """
        FromCTime(seconds: Int64) -> PrecisionDateTime
        FromCTime(seconds: Int64, kind: DateTimeKind) -> PrecisionDateTime
        """
        pass

    @staticmethod
    def FromDateTime(dateTime):
        """ FromDateTime(dateTime: DateTime) -> PrecisionDateTime """
        pass

    @staticmethod
    def FromFileTime(fileTime, kind=None):
        """
        FromFileTime(fileTime: Int64) -> PrecisionDateTime
        FromFileTime(fileTime: Int64, kind: DateTimeKind) -> PrecisionDateTime
        """
        pass

    @staticmethod
    def FromLabViewTime(wholeSeconds, fractionalSecondTicks, kind=None):
        """
        FromLabViewTime(wholeSeconds: Int64, fractionalSecondTicks: UInt64) -> PrecisionDateTime
        FromLabViewTime(wholeSeconds: Int64, fractionalSecondTicks: UInt64, kind: DateTimeKind) -> PrecisionDateTime
        FromLabViewTime(wholeSeconds: Int64, fractionalSecondTicks: Int64) -> PrecisionDateTime
        FromLabViewTime(wholeSeconds: Int64, fractionalSecondTicks: Int64, kind: DateTimeKind) -> PrecisionDateTime
        """
        pass

    def GetDateTimeFormats(self, *__args):
        """
        GetDateTimeFormats(self: PrecisionDateTime) -> Array[str]
        GetDateTimeFormats(self: PrecisionDateTime, format: Char) -> Array[str]
        GetDateTimeFormats(self: PrecisionDateTime, provider: IFormatProvider) -> Array[str]
        GetDateTimeFormats(self: PrecisionDateTime, format: Char, provider: IFormatProvider) -> Array[str]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PrecisionDateTime) -> int """
        pass

    def GetTypeCode(self):
        """ GetTypeCode(self: PrecisionDateTime) -> TypeCode """
        pass

    @staticmethod
    def Parse(dateTime, provider=None, styles=None):
        """
        Parse(dateTime: str) -> PrecisionDateTime
        Parse(dateTime: str, provider: IFormatProvider) -> PrecisionDateTime
        Parse(dateTime: str, provider: IFormatProvider, styles: DateTimeStyles) -> PrecisionDateTime
        """
        pass

    @staticmethod
    def ParseExact(dateTime, *__args):
        """
        ParseExact(dateTime: str, format: str, provider: IFormatProvider) -> PrecisionDateTime
        ParseExact(dateTime: str, format: str, provider: IFormatProvider, style: DateTimeStyles) -> PrecisionDateTime
        ParseExact(dateTime: str, formats: Array[str], provider: IFormatProvider, style: DateTimeStyles) -> PrecisionDateTime
        """
        pass

    @staticmethod
    def SpecifyKind(value, kind):
        """ SpecifyKind(value: PrecisionDateTime, kind: DateTimeKind) -> PrecisionDateTime """
        pass

    def Subtract(self, value):
        """
        Subtract(self: PrecisionDateTime, value: PrecisionDateTime) -> PrecisionTimeSpan
        Subtract(self: PrecisionDateTime, value: PrecisionTimeSpan) -> PrecisionDateTime
        """
        pass

    def ToCTime(self):
        """ ToCTime(self: PrecisionDateTime) -> Int64 """
        pass

    def ToDateTime(self):
        """ ToDateTime(self: PrecisionDateTime) -> DateTime """
        pass

    def ToFileTime(self):
        """ ToFileTime(self: PrecisionDateTime) -> Int64 """
        pass

    def ToLabViewTime(self, wholeSeconds, fractionalSecondTicks):
        """
        ToLabViewTime(self: PrecisionDateTime) -> (Int64, Int64)
        ToLabViewTime(self: PrecisionDateTime) -> (Int64, UInt64)
        """
        pass

    def ToLocalTime(self):
        """ ToLocalTime(self: PrecisionDateTime) -> PrecisionDateTime """
        pass

    def ToLongDateString(self):
        """ ToLongDateString(self: PrecisionDateTime) -> str """
        pass

    def ToLongTimeString(self):
        """ ToLongTimeString(self: PrecisionDateTime) -> str """
        pass

    def ToShortDateString(self):
        """ ToShortDateString(self: PrecisionDateTime) -> str """
        pass

    def ToShortTimeString(self):
        """ ToShortTimeString(self: PrecisionDateTime) -> str """
        pass

    def ToString(self, *__args):
        """
        ToString(self: PrecisionDateTime) -> str
        ToString(self: PrecisionDateTime, provider: IFormatProvider) -> str
        ToString(self: PrecisionDateTime, format: str) -> str
        ToString(self: PrecisionDateTime, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def ToUniversalTime(self):
        """ ToUniversalTime(self: PrecisionDateTime) -> PrecisionDateTime """
        pass

    @staticmethod
    def TryParse(dateTime, *__args):
        """
        TryParse(dateTime: str) -> (bool, PrecisionDateTime)
        TryParse(dateTime: str, provider: IFormatProvider, styles: DateTimeStyles) -> (bool, PrecisionDateTime)
        """
        pass

    @staticmethod
    def TryParseExact(dateTime, *__args):
        """
        TryParseExact(dateTime: str, format: str, provider: IFormatProvider, styles: DateTimeStyles) -> (bool, PrecisionDateTime)
        TryParseExact(dateTime: str, formats: Array[str], provider: IFormatProvider, styles: DateTimeStyles) -> (bool, PrecisionDateTime)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[PrecisionDateTime]() -> PrecisionDateTime
        
        __new__(cls: type, wholeSeconds: Int64, fractionalSecondTicks: UInt64)
        __new__(cls: type, wholeSeconds: Int64, fractionalSecondTicks: UInt64, kind: DateTimeKind)
        __new__(cls: type, wholeSeconds: Int64, fractionalSecondTicks: Int64)
        __new__(cls: type, wholeSeconds: Int64, fractionalSecondTicks: Int64, kind: DateTimeKind)
        __new__(cls: type, dateTime: DateTime)
        __new__(cls: type, seconds: float)
        __new__(cls: type, seconds: float, kind: DateTimeKind)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(precisionDateTime1: PrecisionDateTime, precisionDateTime2: PrecisionDateTime) -> PrecisionTimeSpan """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: PrecisionDateTime) -> PrecisionDateTime

"""

    Day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Day(self: PrecisionDateTime) -> int

"""

    DayOfWeek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DayOfWeek(self: PrecisionDateTime) -> DayOfWeek

"""

    DayOfYear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DayOfYear(self: PrecisionDateTime) -> int

"""

    FractionalSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FractionalSeconds(self: PrecisionDateTime) -> float

"""

    FractionalSecondTicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FractionalSecondTicks(self: PrecisionDateTime) -> UInt64

"""

    Hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hour(self: PrecisionDateTime) -> int

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: PrecisionDateTime) -> DateTimeKind

"""

    Millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Millisecond(self: PrecisionDateTime) -> int

"""

    Minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minute(self: PrecisionDateTime) -> int

"""

    Month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Month(self: PrecisionDateTime) -> int

"""

    Second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Second(self: PrecisionDateTime) -> int

"""

    TimeOfDay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeOfDay(self: PrecisionDateTime) -> PrecisionTimeSpan

"""

    WholeSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WholeSeconds(self: PrecisionDateTime) -> Int64

"""

    Year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Year(self: PrecisionDateTime) -> int

"""

    YearLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YearLong(self: PrecisionDateTime) -> Int64

"""


    MaxValue = None
    MinValue = None
    Now = None
    SecondsPerFractionalTicks = 5.4210108624275222e-20
    Today = None
    UtcNow = None


class PrecisionTimeSpan(object, ISerializable, IComparable, IComparable[PrecisionTimeSpan], IEquatable[PrecisionTimeSpan]):
    """
    PrecisionTimeSpan(wholeSeconds: Int64, fractionalSecondTicks: UInt64)
    PrecisionTimeSpan(wholeSeconds: Int64, fractionalSecondTicks: Int64)
    PrecisionTimeSpan(timeSpan: TimeSpan)
    PrecisionTimeSpan(seconds: float)
    """
    def Add(self, ts):
        """ Add(self: PrecisionTimeSpan, ts: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def Compare(t1, t2):
        """ Compare(t1: PrecisionTimeSpan, t2: PrecisionTimeSpan) -> int """
        pass

    def CompareTo(self, *__args):
        """
        CompareTo(self: PrecisionTimeSpan, obj: object) -> int
        CompareTo(self: PrecisionTimeSpan, other: PrecisionTimeSpan) -> int
        """
        pass

    def Divide(self, value):
        """ Divide(self: PrecisionTimeSpan, value: Int64) -> PrecisionTimeSpan """
        pass

    def Duration(self):
        """ Duration(self: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def Equals(self, *__args):
        """
        Equals(self: PrecisionTimeSpan, obj: object) -> bool
        Equals(self: PrecisionTimeSpan, other: PrecisionTimeSpan) -> bool
        Equals(t1: PrecisionTimeSpan, t2: PrecisionTimeSpan) -> bool
        """
        pass

    @staticmethod
    def FromDays(value):
        """ FromDays(value: float) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def FromHours(value):
        """ FromHours(value: float) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def FromMilliseconds(value):
        """ FromMilliseconds(value: float) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def FromMinutes(value):
        """ FromMinutes(value: float) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def FromSeconds(value):
        """ FromSeconds(value: float) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def FromTimeSpan(timeSpan):
        """ FromTimeSpan(timeSpan: TimeSpan) -> PrecisionTimeSpan """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PrecisionTimeSpan) -> int """
        pass

    def Multiply(self, value):
        """ Multiply(self: PrecisionTimeSpan, value: Int64) -> PrecisionTimeSpan """
        pass

    def Negate(self):
        """ Negate(self: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    @staticmethod
    def Parse(timeSpan, formatProvider=None):
        """
        Parse(timeSpan: str) -> PrecisionTimeSpan
        Parse(timeSpan: str, formatProvider: IFormatProvider) -> PrecisionTimeSpan
        """
        pass

    def Subtract(self, ts):
        """ Subtract(self: PrecisionTimeSpan, ts: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def ToString(self, format=None, provider=None):
        """
        ToString(self: PrecisionTimeSpan) -> str
        ToString(self: PrecisionTimeSpan, format: str) -> str
        ToString(self: PrecisionTimeSpan, format: str, provider: IFormatProvider) -> str
        """
        pass

    def ToTimeSpan(self):
        """ ToTimeSpan(self: PrecisionTimeSpan) -> TimeSpan """
        pass

    @staticmethod
    def TryParse(timeSpan, *__args):
        """
        TryParse(timeSpan: str) -> (bool, PrecisionTimeSpan)
        TryParse(timeSpan: str, formatProvider: IFormatProvider) -> (bool, PrecisionTimeSpan)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[PrecisionTimeSpan]() -> PrecisionTimeSpan
        
        __new__(cls: type, wholeSeconds: Int64, fractionalSecondTicks: UInt64)
        __new__(cls: type, wholeSeconds: Int64, fractionalSecondTicks: Int64)
        __new__(cls: type, timeSpan: TimeSpan)
        __new__(cls: type, seconds: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(ts: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(t1: PrecisionTimeSpan, t2: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(t1: PrecisionTimeSpan, t2: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Days(self: PrecisionTimeSpan) -> Int64

"""

    FractionalSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FractionalSeconds(self: PrecisionTimeSpan) -> float

"""

    FractionalSecondTicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FractionalSecondTicks(self: PrecisionTimeSpan) -> UInt64

"""

    Hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hours(self: PrecisionTimeSpan) -> int

"""

    Milliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Milliseconds(self: PrecisionTimeSpan) -> int

"""

    Minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minutes(self: PrecisionTimeSpan) -> int

"""

    Seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Seconds(self: PrecisionTimeSpan) -> int

"""

    TotalDays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalDays(self: PrecisionTimeSpan) -> float

"""

    TotalHours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalHours(self: PrecisionTimeSpan) -> float

"""

    TotalMilliseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalMilliseconds(self: PrecisionTimeSpan) -> float

"""

    TotalMinutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalMinutes(self: PrecisionTimeSpan) -> float

"""

    TotalSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalSeconds(self: PrecisionTimeSpan) -> float

"""

    WholeSeconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WholeSeconds(self: PrecisionTimeSpan) -> Int64

"""


    MaxValue = None
    MinValue = None
    SecondsPerFractionalTicks = 5.4210108624275222e-20
    Zero = None


class PrecisionWaveformTiming(object, IWaveformTimingInternal, ISerializable, IEquatable[PrecisionWaveformTiming]):
    # no doc
    @staticmethod
    def CreateWithIrregularInterval(timeStamps):
        """ CreateWithIrregularInterval(timeStamps: Array[PrecisionDateTime]) -> PrecisionWaveformTiming """
        pass

    @staticmethod
    def CreateWithNoInterval(*__args):
        """
        CreateWithNoInterval(timeStamp: PrecisionDateTime) -> PrecisionWaveformTiming
        CreateWithNoInterval(timeOffset: PrecisionTimeSpan) -> PrecisionWaveformTiming
        CreateWithNoInterval(timeStamp: PrecisionDateTime, timeOffset: PrecisionTimeSpan) -> PrecisionWaveformTiming
        """
        pass

    @staticmethod
    def CreateWithRegularInterval(sampleInterval, *__args):
        """
        CreateWithRegularInterval(sampleInterval: PrecisionTimeSpan) -> PrecisionWaveformTiming
        CreateWithRegularInterval(sampleInterval: PrecisionTimeSpan, timeOffset: PrecisionTimeSpan) -> PrecisionWaveformTiming
        CreateWithRegularInterval(sampleInterval: PrecisionTimeSpan, timeStamp: PrecisionDateTime) -> PrecisionWaveformTiming
        CreateWithRegularInterval(sampleInterval: PrecisionTimeSpan, timeStamp: PrecisionDateTime, timeOffset: PrecisionTimeSpan) -> PrecisionWaveformTiming
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: PrecisionWaveformTiming, other: PrecisionWaveformTiming) -> bool
        Equals(self: PrecisionWaveformTiming, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromWaveformTiming(timing):
        """ FromWaveformTiming(timing: WaveformTiming) -> PrecisionWaveformTiming """
        pass

    def GetBuffer(self, count):
        """ GetBuffer(self: PrecisionWaveformTiming, count: int) -> Buffer[PrecisionDateTime] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PrecisionWaveformTiming) -> int """
        pass

    def GetTimeStamps(self, *__args):
        """
        GetTimeStamps(self: PrecisionWaveformTiming, count: int) -> Array[PrecisionDateTime]
        GetTimeStamps(self: PrecisionWaveformTiming, sampleIndex: int, count: int) -> Array[PrecisionDateTime]
        GetTimeStamps(self: PrecisionWaveformTiming, sampleIndex: int, count: int, buffer: Array[PrecisionDateTime], arrayIndex: int)
        """
        pass

    def ToString(self):
        """ ToString(self: PrecisionWaveformTiming) -> str """
        pass

    def ToWaveformTiming(self):
        """ ToWaveformTiming(self: PrecisionWaveformTiming) -> WaveformTiming """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HasTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTimeStamp(self: PrecisionWaveformTiming) -> bool

"""

    SampleInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleInterval(self: PrecisionWaveformTiming) -> PrecisionTimeSpan

"""

    SampleIntervalMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleIntervalMode(self: PrecisionWaveformTiming) -> WaveformSampleIntervalMode

"""

    StartTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartTime(self: PrecisionWaveformTiming) -> PrecisionDateTime

"""

    TimeOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeOffset(self: PrecisionWaveformTiming) -> PrecisionTimeSpan

"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: PrecisionWaveformTiming) -> PrecisionDateTime

"""


    Empty = None


class Spectrum(object, IWaveform, IServiceProvider, ICloneable, ISerializable):
    """
    Spectrum[TData](sampleCount: int)
    Spectrum[TData](sampleCount: int, capacity: int)
    """
    def Append(self, *__args):
        """ Append(self: Spectrum[TData], data: Array[TData])Append(self: Spectrum[TData], spectrum: Spectrum[TData])Append(self: Spectrum[TData], spectrums: Array[Spectrum[TData]]) """
        pass

    def Clone(self):
        """ Clone(self: Spectrum[TData]) -> Spectrum[TData] """
        pass

    @staticmethod
    def CopySamples(source, *__args):
        """ CopySamples(source: Spectrum[TData], destination: Spectrum[TData], sampleCount: int)CopySamples(source: Spectrum[TData], sourceSampleIndex: int, destination: Spectrum[TData], destinationSampleIndex: int, sampleCount: int) """
        pass

    @staticmethod
    def FromArray1D(array):
        """ FromArray1D(array: Array[TData]) -> Spectrum[TData] """
        pass

    @staticmethod
    def FromArray2D(array):
        """ FromArray2D(array: Array[TData]) -> Array[Spectrum[TData]] """
        pass

    def GetBuffer(self, copy):
        """ GetBuffer(self: Spectrum[TData], copy: bool) -> Buffer[TData] """
        pass

    def GetData(self, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetData(self: Spectrum[TData]) -> Array[TData]
        GetData(self: Spectrum[TData], sampleIndex: int, count: int) -> Array[TData]
        GetData(self: Spectrum[TData], sampleIndex: int, count: int, buffer: Array[TData], arrayIndex: int)
        """
        pass

    def GetWritableBuffer(self):
        """ GetWritableBuffer(self: Spectrum[TData]) -> WritableBuffer[TData] """
        pass

    def ToString(self):
        """ ToString(self: Spectrum[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sampleCount, capacity=None):
        """
        __new__(cls: type, sampleCount: int)
        __new__(cls: type, sampleCount: int, capacity: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: Spectrum[TData]) -> int

Set: Capacity(self: Spectrum[TData]) = value
"""

    ChannelName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChannelName(self: Spectrum[TData]) -> str

Set: ChannelName(self: Spectrum[TData]) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: Spectrum[TData]) -> Type

"""

    ExtendedProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedProperties(self: Spectrum[TData]) -> ExtendedPropertyDictionary

"""

    FrequencyIncrement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyIncrement(self: Spectrum[TData]) -> float

Set: FrequencyIncrement(self: Spectrum[TData]) = value
"""

    SampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleCount(self: Spectrum[TData]) -> int

"""

    Samples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Samples(self: Spectrum[TData]) -> Buffer[TData]

"""

    StartFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartFrequency(self: Spectrum[TData]) -> float

Set: StartFrequency(self: Spectrum[TData]) = value
"""

    UnitDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitDescription(self: Spectrum[TData]) -> str

Set: UnitDescription(self: Spectrum[TData]) = value
"""



class SpectrumCollection(object, IServiceProvider, ICollection, IEnumerable, ICloneable, ISerializable, ICollection[Spectrum[TData]], IEnumerable[Spectrum[TData]]):
    """ SpectrumCollection[TData]() """
    def Clone(self):
        """ Clone(self: SpectrumCollection[TData]) -> SpectrumCollection[TData] """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: SpectrumCollection[TData], array: Array[Spectrum[TData]], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SpectrumCollection[TData]) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[Spectrum[TData]], item: Spectrum[TData]) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Channels(self: SpectrumCollection[TData]) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SpectrumCollection[TData]) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: SpectrumCollection[TData]) -> bool

"""

    Records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Records(self: SpectrumCollection[TData]) -> int

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: SpectrumCollection[TData]) -> object

"""



class WaveformSampleIntervalMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum WaveformSampleIntervalMode, values: Irregular (2), None (0), Regular (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Irregular = None
    None = None
    Regular = None
    value__ = None


class WaveformScaleMode(object):
    # no doc
    @staticmethod
    def CreateLinearMode(gain, offset):
        """ CreateLinearMode(gain: float, offset: float) -> WaveformScaleMode """
        pass

    def GetPropertyValues(self, *args): #cannot find CLR method
        """ GetPropertyValues(self: WaveformScaleMode) -> IEnumerable[KeyValuePair[str, object]] """
        pass

    def GetScaledData(self, waveform, sampleIndex=None, count=None, buffer=None, arrayIndex=None):
        """
        GetScaledData[TData](self: WaveformScaleMode, waveform: AnalogWaveform[TData]) -> Array[float]
        GetScaledData[TData](self: WaveformScaleMode, waveform: AnalogWaveform[TData], sampleIndex: int, count: int) -> Array[float]
        GetScaledData[TData](self: WaveformScaleMode, waveform: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[float], arrayIndex: int)GetScaledData[TData](self: WaveformScaleMode, waveform: AnalogWaveform[TData], sampleIndex: int, count: int, buffer: Array[Single], arrayIndex: int)
        """
        pass

    def TransformData(self, *args): #cannot find CLR method
        """
        TransformData(self: WaveformScaleMode, data: Array[float]) -> Array[float]
        TransformData(self: WaveformScaleMode, data: Array[Single]) -> Array[Single]
        """
        pass

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: WaveformScaleMode) -> ExtendedPropertyDictionary

"""


    None = None


class WaveformTiming(object, IWaveformTimingInternal, ISerializable, IEquatable[WaveformTiming]):
    # no doc
    @staticmethod
    def CreateWithIrregularInterval(timeStamps):
        """ CreateWithIrregularInterval(timeStamps: Array[DateTime]) -> WaveformTiming """
        pass

    @staticmethod
    def CreateWithNoInterval(*__args):
        """
        CreateWithNoInterval(timeStamp: DateTime) -> WaveformTiming
        CreateWithNoInterval(timeOffset: TimeSpan) -> WaveformTiming
        CreateWithNoInterval(timeStamp: DateTime, timeOffset: TimeSpan) -> WaveformTiming
        """
        pass

    @staticmethod
    def CreateWithRegularInterval(sampleInterval, *__args):
        """
        CreateWithRegularInterval(sampleInterval: TimeSpan) -> WaveformTiming
        CreateWithRegularInterval(sampleInterval: TimeSpan, timeOffset: TimeSpan) -> WaveformTiming
        CreateWithRegularInterval(sampleInterval: TimeSpan, timeStamp: DateTime) -> WaveformTiming
        CreateWithRegularInterval(sampleInterval: TimeSpan, timeStamp: DateTime, timeOffset: TimeSpan) -> WaveformTiming
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: WaveformTiming, other: WaveformTiming) -> bool
        Equals(self: WaveformTiming, obj: object) -> bool
        """
        pass

    def GetBuffer(self, count):
        """ GetBuffer(self: WaveformTiming, count: int) -> Buffer[DateTime] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: WaveformTiming) -> int """
        pass

    def GetTimeStamps(self, *__args):
        """
        GetTimeStamps(self: WaveformTiming, count: int) -> Array[DateTime]
        GetTimeStamps(self: WaveformTiming, sampleIndex: int, count: int) -> Array[DateTime]
        GetTimeStamps(self: WaveformTiming, sampleIndex: int, count: int, buffer: Array[DateTime], arrayIndex: int)
        """
        pass

    def ToString(self):
        """ ToString(self: WaveformTiming) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HasTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTimeStamp(self: WaveformTiming) -> bool

"""

    SampleInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleInterval(self: WaveformTiming) -> TimeSpan

"""

    SampleIntervalMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleIntervalMode(self: WaveformTiming) -> WaveformSampleIntervalMode

"""

    StartTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartTime(self: WaveformTiming) -> DateTime

"""

    TimeOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeOffset(self: WaveformTiming) -> TimeSpan

"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: WaveformTiming) -> DateTime

"""


    Empty = None


# variables with complex values

