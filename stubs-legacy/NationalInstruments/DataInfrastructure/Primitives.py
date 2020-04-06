# encoding: utf-8
# module NationalInstruments.DataInfrastructure.Primitives calls itself Primitives
# from NationalInstruments.Common, Version=19.0.40.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# functions

def RawDataStore(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class AllocatingBufferPool(BufferPool):
    # no doc
    def GetBuffer(self, samples, unit):
        """ GetBuffer[TData](self: AllocatingBufferPool, samples: IEnumerable[TData], unit: Unit) -> Buffer[TData] """
        pass

    def GetRawDataStore(self, *args): #cannot find CLR method
        """
        GetRawDataStore[TData](self: AllocatingBufferPool, size: int) -> RawDataStore[TData]
        GetRawDataStore[TData](self: AllocatingBufferPool, samples: IEnumerable[TData]) -> RawDataStore[TData]
        """
        pass

    def GetRawDataStoreCore(self, *args): #cannot find CLR method
        """
        GetRawDataStoreCore[TData](self: AllocatingBufferPool, size: int) -> RawDataStore[TData]
        GetRawDataStoreCore[TData](self: AllocatingBufferPool, samples: IEnumerable[TData]) -> RawDataStore[TData]
        """
        pass

    def GetWritableBuffer(self, size, unit):
        """ GetWritableBuffer[TData](self: AllocatingBufferPool, size: int, unit: Unit) -> WritableBuffer[TData] """
        pass


class AnalogWaveformDescriptor(object, IOpMultiSample[AnalogWaveform[TData]], IDataTypeDescriptor[AnalogWaveform[TData]], IOpObservable[AnalogWaveform[TData]]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: AnalogWaveformDescriptor[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> AnalogWaveform[TData] """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: AnalogWaveformDescriptor[TData], value: AnalogWaveform[TData], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: AnalogWaveformDescriptor[TData]) -> AnalogWaveform[TData] """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: AnalogWaveformDescriptor[TData], value: AnalogWaveform[TData], decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def GetValueObserver(self, value, decomposeOption):
        """ GetValueObserver(self: AnalogWaveformDescriptor[TData], value: AnalogWaveform[TData], decomposeOption: Trait) -> IValueObserver[AnalogWaveform[TData]] """
        pass

    def ToString(self):
        """ ToString(self: AnalogWaveformDescriptor[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Array1DDescriptor(object, IOpMultiSample[Array[TData]], IDataTypeDescriptor[Array[TData]]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: Array1DDescriptor[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> Array[TData] """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: Array1DDescriptor[TData], value: Array[TData], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: Array1DDescriptor[TData]) -> Array[TData] """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: Array1DDescriptor[TData], value: Array[TData], decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def ToString(self):
        """ ToString(self: Array1DDescriptor[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class Array2DDescriptor(object, IOpMultiSample[Array[TData]], IDataTypeDescriptor[Array[TData]]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: Array2DDescriptor[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> Array[TData] """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: Array2DDescriptor[TData], value: Array[TData], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: Array2DDescriptor[TData]) -> Array[TData] """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: Array2DDescriptor[TData], value: Array[TData], decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def ToString(self):
        """ ToString(self: Array2DDescriptor[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class ArrayBufferPool(AllocatingBufferPool):
    """ ArrayBufferPool() """

class BooleanDescriptor(object, IOpComparison[bool], IDataTypeDescriptor[bool], IOpFormatInBase[bool], IOpFormat[bool], IOpConversion[str, bool], IOpNumeric[bool], IOpBounded[bool], IOpDigitPosition[bool], IOpBitwise[bool], IOpAddition[bool, bool], IOpSubtraction[bool, bool], IOpMultiplication[bool, bool], IOpScalarMultiplication[bool], IOpDivision[bool, bool], IOpRatio[bool], IOpConversion[bool, str], IOpLosslessConversion[bool, bool], IOpConversion[bool, bool], IOpLosslessConversion[bool, float], IOpConversion[bool, float], IOpConversion[float, bool], IOpLosslessConversion[bool, Single], IOpConversion[bool, Single], IOpConversion[Single, bool], IOpLosslessConversion[bool, SByte], IOpConversion[bool, SByte], IOpConversion[SByte, bool], IOpLosslessConversion[bool, Byte], IOpConversion[bool, Byte], IOpConversion[Byte, bool]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: BooleanDescriptor, value: bool, offset: bool) -> bool """
        pass

    def And(self, left, right):
        """ And(self: BooleanDescriptor, left: bool, right: bool) -> bool """
        pass

    def Compare(self, left, right):
        """ Compare(self: BooleanDescriptor, left: bool, right: bool) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: BooleanDescriptor, left: bool, right: bool) -> bool """
        pass

    def Divide(self, value, factor):
        """ Divide(self: BooleanDescriptor, value: bool, factor: bool) -> bool """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: BooleanDescriptor, value: bool) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: BooleanDescriptor, value: bool) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: BooleanDescriptor, value: bool) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: BooleanDescriptor, value: bool) -> bool """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: BooleanDescriptor, value: bool, factor: bool) -> bool
        Multiply(self: BooleanDescriptor, value: bool, factor: float) -> bool
        """
        pass

    def Not(self, value):
        """ Not(self: BooleanDescriptor, value: bool) -> bool """
        pass

    def Or(self, left, right):
        """ Or(self: BooleanDescriptor, left: bool, right: bool) -> bool """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: BooleanDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> bool
        Parse(self: BooleanDescriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> bool
        """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: BooleanDescriptor, left: bool, right: bool) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: BooleanDescriptor, value: bool, factor: bool) -> bool """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: BooleanDescriptor, value: bool, amount: int) -> bool """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: BooleanDescriptor, value: bool, amount: int) -> bool """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: BooleanDescriptor, value: bool, offset: bool) -> bool """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: BooleanDescriptor) -> str
        ToString(self: BooleanDescriptor, value: bool, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: BooleanDescriptor, value: bool, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: BooleanDescriptor, value: bool) -> (ConversionResult, str)
        TryConvert(self: BooleanDescriptor, value: str) -> (ConversionResult, bool)
        TryConvert(self: BooleanDescriptor, value: bool) -> (ConversionResult, bool)
        TryConvert(self: BooleanDescriptor, value: bool) -> (ConversionResult, float)
        TryConvert(self: BooleanDescriptor, value: float) -> (ConversionResult, bool)
        TryConvert(self: BooleanDescriptor, value: bool) -> (ConversionResult, Single)
        TryConvert(self: BooleanDescriptor, value: Single) -> (ConversionResult, bool)
        TryConvert(self: BooleanDescriptor, value: bool) -> (ConversionResult, SByte)
        TryConvert(self: BooleanDescriptor, value: SByte) -> (ConversionResult, bool)
        TryConvert(self: BooleanDescriptor, value: bool) -> (ConversionResult, Byte)
        TryConvert(self: BooleanDescriptor, value: Byte) -> (ConversionResult, bool)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: BooleanDescriptor, value: bool, factor: float) -> (ConversionResult, bool) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: BooleanDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, bool)
        TryParse(self: BooleanDescriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, bool)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: BooleanDescriptor, left: bool, right: bool) -> bool """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: BooleanDescriptor) -> bool

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: BooleanDescriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: BooleanDescriptor) -> bool

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: BooleanDescriptor) -> bool

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: BooleanDescriptor) -> bool

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: BooleanDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: BooleanDescriptor) -> bool

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: BooleanDescriptor) -> bool

"""



class ByteDescriptor(object, IOpComparison[Byte], IDataTypeDescriptor[Byte], IOpFormatInBase[Byte], IOpFormat[Byte], IOpConversion[str, Byte], IOpNumeric[Byte], IOpBounded[Byte], IOpDigitPosition[Byte], IOpBitwise[Byte], IOpAddition[Byte, Byte], IOpSubtraction[Byte, Byte], IOpMultiplication[Byte, Byte], IOpScalarMultiplication[Byte], IOpDivision[Byte, Byte], IOpRatio[Byte], IOpPower[Byte, float], IOpConversion[Byte, str], IOpLosslessConversion[Byte, Byte], IOpConversion[Byte, Byte], IOpLosslessConversion[Byte, float], IOpConversion[Byte, float], IOpConversion[float, Byte], IOpLosslessConversion[Byte, Single], IOpConversion[Byte, Single], IOpConversion[Single, Byte], IOpConversion[Byte, SByte], IOpConversion[SByte, Byte], IOpLosslessConversion[Byte, UInt16], IOpConversion[Byte, UInt16], IOpConversion[UInt16, Byte], IOpLosslessConversion[Byte, UInt32], IOpConversion[Byte, UInt32], IOpConversion[UInt32, Byte], IOpLosslessConversion[Byte, UInt64], IOpConversion[Byte, UInt64], IOpConversion[UInt64, Byte]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: ByteDescriptor, value: Byte, offset: Byte) -> Byte """
        pass

    def And(self, left, right):
        """ And(self: ByteDescriptor, left: Byte, right: Byte) -> Byte """
        pass

    def Compare(self, left, right):
        """ Compare(self: ByteDescriptor, left: Byte, right: Byte) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: ByteDescriptor, left: Byte, right: Byte) -> Byte """
        pass

    def Divide(self, value, factor):
        """ Divide(self: ByteDescriptor, value: Byte, factor: Byte) -> Byte """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: ByteDescriptor, value: Byte) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: ByteDescriptor, value: Byte) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: ByteDescriptor, value: Byte) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: ByteDescriptor, value: Byte) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: ByteDescriptor, logBase: float, value: Byte) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: ByteDescriptor, value: Byte, factor: Byte) -> Byte
        Multiply(self: ByteDescriptor, value: Byte, factor: float) -> Byte
        """
        pass

    def Not(self, value):
        """ Not(self: ByteDescriptor, value: Byte) -> Byte """
        pass

    def Or(self, left, right):
        """ Or(self: ByteDescriptor, left: Byte, right: Byte) -> Byte """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: ByteDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> Byte
        Parse(self: ByteDescriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> Byte
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: ByteDescriptor, logBase: float, power: float) -> Byte """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: ByteDescriptor, left: Byte, right: Byte) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: ByteDescriptor, value: Byte, factor: Byte) -> Byte """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: ByteDescriptor, value: Byte, amount: int) -> Byte """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: ByteDescriptor, value: Byte, amount: int) -> Byte """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: ByteDescriptor, value: Byte, offset: Byte) -> Byte """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: ByteDescriptor) -> str
        ToString(self: ByteDescriptor, value: Byte, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: ByteDescriptor, value: Byte, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, str)
        TryConvert(self: ByteDescriptor, value: str) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, float)
        TryConvert(self: ByteDescriptor, value: float) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, Single)
        TryConvert(self: ByteDescriptor, value: Single) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, SByte)
        TryConvert(self: ByteDescriptor, value: SByte) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, UInt16)
        TryConvert(self: ByteDescriptor, value: UInt16) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, UInt32)
        TryConvert(self: ByteDescriptor, value: UInt32) -> (ConversionResult, Byte)
        TryConvert(self: ByteDescriptor, value: Byte) -> (ConversionResult, UInt64)
        TryConvert(self: ByteDescriptor, value: UInt64) -> (ConversionResult, Byte)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: ByteDescriptor, value: Byte, factor: float) -> (ConversionResult, Byte) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: ByteDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, Byte)
        TryParse(self: ByteDescriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, Byte)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: ByteDescriptor, left: Byte, right: Byte) -> Byte """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: ByteDescriptor) -> Byte

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: ByteDescriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: ByteDescriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: ByteDescriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: ByteDescriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: ByteDescriptor) -> Byte

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: ByteDescriptor) -> Byte

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: ByteDescriptor) -> Byte

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: ByteDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: ByteDescriptor) -> Byte

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: ByteDescriptor) -> Byte

"""



class ComplexDoubleDescriptor(object, IOpMultiDimensional[ComplexDouble], IDataTypeDescriptor[ComplexDouble], IOpComparison[ComplexDouble], IOpFormat[ComplexDouble], IOpConversion[str, ComplexDouble], IOpNumeric[ComplexDouble], IOpBounded[ComplexDouble], IOpAddition[ComplexDouble, ComplexDouble], IOpSubtraction[ComplexDouble, ComplexDouble], IOpConversion[ComplexDouble, str], IOpLosslessConversion[ComplexDouble, ComplexDouble], IOpConversion[ComplexDouble, ComplexDouble], IOpConversion[ComplexDouble, float], IOpConversion[float, ComplexDouble]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: ComplexDoubleDescriptor, value: ComplexDouble, offset: ComplexDouble) -> ComplexDouble """
        pass

    def Compare(self, left, right):
        """ Compare(self: ComplexDoubleDescriptor, left: ComplexDouble, right: ComplexDouble) -> int """
        pass

    def ComposeValues(self, dimensionValues, composeOption):
        """ ComposeValues(self: ComplexDoubleDescriptor, dimensionValues: IList[IBuffer], composeOption: Trait) -> Buffer[ComplexDouble] """
        pass

    def Convert(self, value):
        """ Convert(self: ComplexDoubleDescriptor, value: ComplexDouble) -> ComplexDouble """
        pass

    def DecomposeValues(self, values, decomposeOption):
        """ DecomposeValues(self: ComplexDoubleDescriptor, values: Buffer[ComplexDouble], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def Difference(self, left, right):
        """ Difference(self: ComplexDoubleDescriptor, left: ComplexDouble, right: ComplexDouble) -> ComplexDouble """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: ComplexDoubleDescriptor) -> ComplexDouble """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: ComplexDoubleDescriptor, value: ComplexDouble, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: ComplexDoubleDescriptor, value: ComplexDouble) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: ComplexDoubleDescriptor, value: ComplexDouble) -> bool """
        pass

    def Parse(self, input, format, formatProvider):
        """ Parse(self: ComplexDoubleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> ComplexDouble """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: ComplexDoubleDescriptor, value: ComplexDouble, offset: ComplexDouble) -> ComplexDouble """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: ComplexDoubleDescriptor) -> str
        ToString(self: ComplexDoubleDescriptor, value: ComplexDouble, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: ComplexDoubleDescriptor, value: ComplexDouble) -> (ConversionResult, str)
        TryConvert(self: ComplexDoubleDescriptor, value: str) -> (ConversionResult, ComplexDouble)
        TryConvert(self: ComplexDoubleDescriptor, value: ComplexDouble) -> (ConversionResult, ComplexDouble)
        TryConvert(self: ComplexDoubleDescriptor, value: ComplexDouble) -> (ConversionResult, float)
        TryConvert(self: ComplexDoubleDescriptor, value: float) -> (ConversionResult, ComplexDouble)
        """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """ TryParse(self: ComplexDoubleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, ComplexDouble) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: ComplexDoubleDescriptor) -> ComplexDouble

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: ComplexDoubleDescriptor) -> ComplexDouble

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: ComplexDoubleDescriptor) -> ComplexDouble

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: ComplexDoubleDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: ComplexDoubleDescriptor) -> ComplexDouble

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: ComplexDoubleDescriptor) -> ComplexDouble

"""



class ComplexInt16Descriptor(object, IOpMultiDimensional[ComplexInt16], IDataTypeDescriptor[ComplexInt16], IOpComparison[ComplexInt16], IOpFormat[ComplexInt16], IOpConversion[str, ComplexInt16], IOpNumeric[ComplexInt16], IOpBounded[ComplexInt16], IOpAddition[ComplexInt16, ComplexInt16], IOpSubtraction[ComplexInt16, ComplexInt16], IOpConversion[ComplexInt16, str], IOpLosslessConversion[ComplexInt16, ComplexInt16], IOpConversion[ComplexInt16, ComplexInt16], IOpConversion[ComplexInt16, Int16], IOpConversion[ComplexInt16, float], IOpConversion[float, ComplexInt16], IOpConversion[Int16, ComplexInt16]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: ComplexInt16Descriptor, value: ComplexInt16, offset: ComplexInt16) -> ComplexInt16 """
        pass

    def Compare(self, left, right):
        """ Compare(self: ComplexInt16Descriptor, left: ComplexInt16, right: ComplexInt16) -> int """
        pass

    def ComposeValues(self, dimensionValues, composeOption):
        """ ComposeValues(self: ComplexInt16Descriptor, dimensionValues: IList[IBuffer], composeOption: Trait) -> Buffer[ComplexInt16] """
        pass

    def Convert(self, value):
        """ Convert(self: ComplexInt16Descriptor, value: ComplexInt16) -> ComplexInt16 """
        pass

    def DecomposeValues(self, values, decomposeOption):
        """ DecomposeValues(self: ComplexInt16Descriptor, values: Buffer[ComplexInt16], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def Difference(self, left, right):
        """ Difference(self: ComplexInt16Descriptor, left: ComplexInt16, right: ComplexInt16) -> ComplexInt16 """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: ComplexInt16Descriptor) -> ComplexInt16 """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: ComplexInt16Descriptor, value: ComplexInt16, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: ComplexInt16Descriptor, value: ComplexInt16) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: ComplexInt16Descriptor, value: ComplexInt16) -> bool """
        pass

    def Parse(self, input, format, formatProvider):
        """ Parse(self: ComplexInt16Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> ComplexInt16 """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: ComplexInt16Descriptor, value: ComplexInt16, offset: ComplexInt16) -> ComplexInt16 """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: ComplexInt16Descriptor) -> str
        ToString(self: ComplexInt16Descriptor, value: ComplexInt16, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: ComplexInt16Descriptor, value: ComplexInt16) -> (ConversionResult, str)
        TryConvert(self: ComplexInt16Descriptor, value: str) -> (ConversionResult, ComplexInt16)
        TryConvert(self: ComplexInt16Descriptor, value: ComplexInt16) -> (ConversionResult, ComplexInt16)
        TryConvert(self: ComplexInt16Descriptor, value: ComplexInt16) -> (ConversionResult, float)
        TryConvert(self: ComplexInt16Descriptor, value: float) -> (ConversionResult, ComplexInt16)
        TryConvert(self: ComplexInt16Descriptor, value: ComplexInt16) -> (ConversionResult, Int16)
        TryConvert(self: ComplexInt16Descriptor, value: Int16) -> (ConversionResult, ComplexInt16)
        """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """ TryParse(self: ComplexInt16Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, ComplexInt16) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: ComplexInt16Descriptor) -> ComplexInt16

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: ComplexInt16Descriptor) -> ComplexInt16

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: ComplexInt16Descriptor) -> ComplexInt16

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: ComplexInt16Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: ComplexInt16Descriptor) -> ComplexInt16

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: ComplexInt16Descriptor) -> ComplexInt16

"""



class ComplexSingleDescriptor(object, IOpMultiDimensional[ComplexSingle], IDataTypeDescriptor[ComplexSingle], IOpComparison[ComplexSingle], IOpFormat[ComplexSingle], IOpConversion[str, ComplexSingle], IOpNumeric[ComplexSingle], IOpBounded[ComplexSingle], IOpAddition[ComplexSingle, ComplexSingle], IOpSubtraction[ComplexSingle, ComplexSingle], IOpConversion[ComplexSingle, str], IOpLosslessConversion[ComplexSingle, ComplexSingle], IOpConversion[ComplexSingle, ComplexSingle], IOpConversion[ComplexSingle, Single], IOpConversion[ComplexSingle, float], IOpConversion[float, ComplexSingle], IOpConversion[Single, ComplexSingle]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: ComplexSingleDescriptor, value: ComplexSingle, offset: ComplexSingle) -> ComplexSingle """
        pass

    def Compare(self, left, right):
        """ Compare(self: ComplexSingleDescriptor, left: ComplexSingle, right: ComplexSingle) -> int """
        pass

    def ComposeValues(self, dimensionValues, composeOption):
        """ ComposeValues(self: ComplexSingleDescriptor, dimensionValues: IList[IBuffer], composeOption: Trait) -> Buffer[ComplexSingle] """
        pass

    def Convert(self, value):
        """ Convert(self: ComplexSingleDescriptor, value: ComplexSingle) -> ComplexSingle """
        pass

    def DecomposeValues(self, values, decomposeOption):
        """ DecomposeValues(self: ComplexSingleDescriptor, values: Buffer[ComplexSingle], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def Difference(self, left, right):
        """ Difference(self: ComplexSingleDescriptor, left: ComplexSingle, right: ComplexSingle) -> ComplexSingle """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: ComplexSingleDescriptor) -> ComplexSingle """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: ComplexSingleDescriptor, value: ComplexSingle, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: ComplexSingleDescriptor, value: ComplexSingle) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: ComplexSingleDescriptor, value: ComplexSingle) -> bool """
        pass

    def Parse(self, input, format, formatProvider):
        """ Parse(self: ComplexSingleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> ComplexSingle """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: ComplexSingleDescriptor, value: ComplexSingle, offset: ComplexSingle) -> ComplexSingle """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: ComplexSingleDescriptor) -> str
        ToString(self: ComplexSingleDescriptor, value: ComplexSingle, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: ComplexSingleDescriptor, value: ComplexSingle) -> (ConversionResult, str)
        TryConvert(self: ComplexSingleDescriptor, value: str) -> (ConversionResult, ComplexSingle)
        TryConvert(self: ComplexSingleDescriptor, value: ComplexSingle) -> (ConversionResult, ComplexSingle)
        TryConvert(self: ComplexSingleDescriptor, value: ComplexSingle) -> (ConversionResult, float)
        TryConvert(self: ComplexSingleDescriptor, value: float) -> (ConversionResult, ComplexSingle)
        TryConvert(self: ComplexSingleDescriptor, value: ComplexSingle) -> (ConversionResult, Single)
        TryConvert(self: ComplexSingleDescriptor, value: Single) -> (ConversionResult, ComplexSingle)
        """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """ TryParse(self: ComplexSingleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, ComplexSingle) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: ComplexSingleDescriptor) -> ComplexSingle

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: ComplexSingleDescriptor) -> ComplexSingle

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: ComplexSingleDescriptor) -> ComplexSingle

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: ComplexSingleDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: ComplexSingleDescriptor) -> ComplexSingle

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: ComplexSingleDescriptor) -> ComplexSingle

"""



class ComplexWaveformDescriptor(object, IOpMultiSample[ComplexWaveform[TData]], IDataTypeDescriptor[ComplexWaveform[TData]], IOpObservable[ComplexWaveform[TData]]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: ComplexWaveformDescriptor[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> ComplexWaveform[TData] """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: ComplexWaveformDescriptor[TData], value: ComplexWaveform[TData], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: ComplexWaveformDescriptor[TData]) -> ComplexWaveform[TData] """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: ComplexWaveformDescriptor[TData], value: ComplexWaveform[TData], decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def GetValueObserver(self, value, decomposeOption):
        """ GetValueObserver(self: ComplexWaveformDescriptor[TData], value: ComplexWaveform[TData], decomposeOption: Trait) -> IValueObserver[ComplexWaveform[TData]] """
        pass

    def ToString(self):
        """ ToString(self: ComplexWaveformDescriptor[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class CompositeUnitConverter(object, IUnitConverter[TData]):
    """ CompositeUnitConverter[TData](fromConverter: IUnitConverter[TData], toConverter: IUnitConverter[TData]) """
    def ToString(self):
        """ ToString(self: CompositeUnitConverter[TData]) -> str """
        pass

    def TryConvert(self, value, result):
        """ TryConvert(self: CompositeUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def TryConvertBack(self, value, result):
        """ TryConvertBack(self: CompositeUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fromConverter, toConverter):
        """ __new__(cls: type, fromConverter: IUnitConverter[TData], toConverter: IUnitConverter[TData]) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanConvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvert(self: CompositeUnitConverter[TData]) -> bool

"""

    CanConvertBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvertBack(self: CompositeUnitConverter[TData]) -> bool

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: CompositeUnitConverter[TData]) -> Unit

"""

    FromConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromConverter(self: CompositeUnitConverter[TData]) -> IUnitConverter[TData]

"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: CompositeUnitConverter[TData]) -> Unit

"""

    ToConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToConverter(self: CompositeUnitConverter[TData]) -> IUnitConverter[TData]

"""



class DigitalSampleDescriptor(object, IDataTypeDescriptor[DigitalSample], IOpLosslessConversion[DigitalSample, DigitalSample], IOpConversion[DigitalSample, DigitalSample], IOpLosslessConversion[DigitalState, DigitalSample], IOpConversion[DigitalState, DigitalSample], IOpConversion[DigitalSample, DigitalState], IOpConversion[DigitalSample, str], IOpConversion[str, DigitalSample]):
    # no doc
    def Convert(self, value):
        """
        Convert(self: DigitalSampleDescriptor, value: DigitalSample) -> DigitalSample
        Convert(self: DigitalSampleDescriptor, value: DigitalState) -> DigitalSample
        """
        pass

    def ToString(self):
        """ ToString(self: DigitalSampleDescriptor) -> str """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: DigitalSampleDescriptor, value: DigitalSample) -> (ConversionResult, DigitalSample)
        TryConvert(self: DigitalSampleDescriptor, value: DigitalState) -> (ConversionResult, DigitalSample)
        TryConvert(self: DigitalSampleDescriptor, value: DigitalSample) -> (ConversionResult, DigitalState)
        TryConvert(self: DigitalSampleDescriptor, value: DigitalSample) -> (ConversionResult, str)
        TryConvert(self: DigitalSampleDescriptor, value: str) -> (ConversionResult, DigitalSample)
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DigitalWaveformDescriptor(object, IOpObservable[DigitalWaveform], IOpMultiSample[DigitalWaveform], IDataTypeDescriptor[DigitalWaveform]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: DigitalWaveformDescriptor, dimensionValues: IList[IBuffer], composeOption: Trait) -> DigitalWaveform """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: DigitalWaveformDescriptor, value: DigitalWaveform, decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: DigitalWaveformDescriptor) -> DigitalWaveform """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: DigitalWaveformDescriptor, value: DigitalWaveform, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def GetValueObserver(self, value, decomposeOption):
        """ GetValueObserver(self: DigitalWaveformDescriptor, value: DigitalWaveform, decomposeOption: Trait) -> IValueObserver[DigitalWaveform] """
        pass

    def ToString(self):
        """ ToString(self: DigitalWaveformDescriptor) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class DoubleDescriptor(object, IOpComparison[float], IDataTypeDescriptor[float], IOpFormat[float], IOpConversion[str, float], IOpNumeric[float], IOpBounded[float], IOpDigitPosition[float], IOpSigned[float], IOpInfinity[float], IOpContinuous[float], IOpAddition[float, float], IOpSubtraction[float, float], IOpMultiplication[float, float], IOpScalarMultiplication[float], IOpDivision[float, float], IOpRatio[float], IOpPower[float, float], IOpConversion[float, str], IOpLosslessConversion[float, float], IOpConversion[float, float]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: DoubleDescriptor, value: float) -> float """
        pass

    def Add(self, value, offset):
        """ Add(self: DoubleDescriptor, value: float, offset: float) -> float """
        pass

    def Ceiling(self, value):
        """ Ceiling(self: DoubleDescriptor, value: float) -> float """
        pass

    def Compare(self, left, right):
        """ Compare(self: DoubleDescriptor, left: float, right: float) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: DoubleDescriptor, left: float, right: float) -> float """
        pass

    def Divide(self, value, factor):
        """ Divide(self: DoubleDescriptor, value: float, factor: float) -> float """
        pass

    def Floor(self, value):
        """ Floor(self: DoubleDescriptor, value: float) -> float """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: DoubleDescriptor, value: float) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: DoubleDescriptor, value: float) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: DoubleDescriptor, value: float) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: DoubleDescriptor, value: float) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: DoubleDescriptor, logBase: float, value: float) -> float """
        pass

    def Multiply(self, value, factor):
        """ Multiply(self: DoubleDescriptor, value: float, factor: float) -> float """
        pass

    def Negate(self, value):
        """ Negate(self: DoubleDescriptor, value: float) -> float """
        pass

    def Parse(self, input, format, formatProvider):
        """ Parse(self: DoubleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> float """
        pass

    def Power(self, logBase, power):
        """ Power(self: DoubleDescriptor, logBase: float, power: float) -> float """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: DoubleDescriptor, left: float, right: float) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: DoubleDescriptor, value: float, factor: float) -> float """
        pass

    def Round(self, value, digits=None):
        """
        Round(self: DoubleDescriptor, value: float) -> float
        Round(self: DoubleDescriptor, value: float, digits: int) -> float
        """
        pass

    def Sign(self, value):
        """ Sign(self: DoubleDescriptor, value: float) -> int """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: DoubleDescriptor, value: float, offset: float) -> float """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: DoubleDescriptor) -> str
        ToString(self: DoubleDescriptor, value: float, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def Truncate(self, value):
        """ Truncate(self: DoubleDescriptor, value: float) -> float """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: DoubleDescriptor, value: float) -> (ConversionResult, str)
        TryConvert(self: DoubleDescriptor, value: str) -> (ConversionResult, float)
        TryConvert(self: DoubleDescriptor, value: float) -> (ConversionResult, float)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: DoubleDescriptor, value: float, factor: float) -> (ConversionResult, float) """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """ TryParse(self: DoubleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, float) """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: DoubleDescriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: DoubleDescriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: DoubleDescriptor) -> float

"""

    Infinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Infinity(self: DoubleDescriptor) -> float

"""

    MaximumRoundDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumRoundDigits(self: DoubleDescriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: DoubleDescriptor) -> float

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: DoubleDescriptor) -> float

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: DoubleDescriptor) -> float

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: DoubleDescriptor) -> float

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: DoubleDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: DoubleDescriptor) -> float

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: DoubleDescriptor) -> float

"""



class EnumerableDescriptor(object, IOpMultiSample[TEnumerable], IDataTypeDescriptor[TEnumerable]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
# Error generating skeleton for function Compose: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: EnumerableDescriptor[TEnumerable, TData], value: TEnumerable, decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
# Error generating skeleton for function GetDefaultValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: EnumerableDescriptor[TEnumerable, TData], value: TEnumerable, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def ToString(self):
        """ ToString(self: EnumerableDescriptor[TEnumerable, TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class TraitFactory(MarshalByRefObject):
    # no doc
    def Aggregate(self, buffer, traits):
        """
        Aggregate[TData](self: TraitFactory, buffer: Buffer[TData], *traits: Array[Trait]) -> Trait
        Aggregate[TData](self: TraitFactory, buffer: Buffer[TData], traits: IEnumerable[Trait]) -> Trait
        """
        pass

    def AggregateCore(self, *args): #cannot find CLR method
        """ AggregateCore[TData](self: TraitFactory, buffer: Buffer[TData], traits: Array[Trait]) -> Trait """
        pass

    def Create(self, buffer, scope=None, invalidSamples=None):
        """
        Create[TData](self: TraitFactory, buffer: Buffer[TData]) -> IEnumerable[Trait]
        Create[TData](self: TraitFactory, buffer: Buffer[TData], scope: TraitScope, invalidSamples: IList[int]) -> IEnumerable[Trait]
        """
        pass

    def CreateCore(self, *args): #cannot find CLR method
        """ CreateCore[TData](self: TraitFactory, buffer: Buffer[TData], scope: TraitScope, invalidSamples: IList[int]) -> IEnumerable[Trait] """
        pass

    TraitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TraitType(self: TraitFactory) -> Type

"""



class ExtremeSamplesTraitFactory(TraitFactory):
    """ ExtremeSamplesTraitFactory() """
    def ToString(self):
        """ ToString(self: ExtremeSamplesTraitFactory) -> str """
        pass

    TraitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TraitType(self: ExtremeSamplesTraitFactory) -> Type

"""



class IdentityUnitConverter(object, IUnitConverter[TData]):
    """ IdentityUnitConverter[TData](unit: Unit) """
    def ToString(self):
        """ ToString(self: IdentityUnitConverter[TData]) -> str """
        pass

    def TryConvert(self, value, result):
        """ TryConvert(self: IdentityUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def TryConvertBack(self, value, result):
        """ TryConvertBack(self: IdentityUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unit):
        """ __new__(cls: type, unit: Unit) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanConvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvert(self: IdentityUnitConverter[TData]) -> bool

"""

    CanConvertBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvertBack(self: IdentityUnitConverter[TData]) -> bool

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: IdentityUnitConverter[TData]) -> Unit

"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: IdentityUnitConverter[TData]) -> Unit

"""



class IndexSet(object, IEquatable[IndexSet]):
    # no doc
    def Contains(self, index):
        """ Contains(self: IndexSet, index: int) -> bool """
        pass

    @staticmethod
    def Create(indices):
        """
        Create(indices: TraitScope) -> IndexSet
        Create(indices: IEnumerable[TraitScope]) -> IndexSet
        Create(indices: IEnumerable[int]) -> IndexSet
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: IndexSet, other: IndexSet) -> bool
        Equals(self: IndexSet, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: IndexSet) -> int """
        pass

    def InScope(self, scope):
        """ InScope(self: IndexSet, scope: TraitScope) -> IndexSet """
        pass

    def ToList(self):
        """ ToList(self: IndexSet) -> IList[int] """
        pass

    def ToScope(self, scope, offset):
        """ ToScope(self: IndexSet, scope: TraitScope, offset: int) -> IndexSet """
        pass

    def ToString(self):
        """ ToString(self: IndexSet) -> str """
        pass

    @staticmethod
    def Union(sets):
        """ Union(sets: IEnumerable[IndexSet]) -> IndexSet """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: IndexSet) -> bool

"""

    RangeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeCount(self: IndexSet) -> int

"""

    Ranges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ranges(self: IndexSet) -> IEnumerable[TraitScope]

"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scope(self: IndexSet) -> TraitScope

"""

    ValueCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueCount(self: IndexSet) -> int

"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: IndexSet) -> IEnumerable[int]

"""


    All = None
    Empty = None


class IndicesTrait(Trait, IEquatable[Trait]):
    # no doc
    def GetIndices(self, *args): #cannot find CLR method
        """ GetIndices(scope: TraitScope, indices: Array[int]) -> IEnumerable[int] """
        pass

    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: Trait) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: Trait, other: Trait) -> bool """
        pass

    def RetargetIndices(self, *args): #cannot find CLR method
        """ RetargetIndices(indices: Array[int], newScope: TraitScope, offset: int) -> (bool, Array[int]) """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: Trait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def UpdateHashCode(self, *args): #cannot find CLR method
        """ UpdateHashCode(indices: Array[int], hash: int) -> int """
        pass

    def ValidateIndexSet(self, *args): #cannot find CLR method
        """ ValidateIndexSet(scope: TraitScope, indicesName: str, indices: IEnumerable[int]) -> IndexSet """
        pass

    def ValidateIndices(self, *args): #cannot find CLR method
        """ ValidateIndices(scope: TraitScope, indicesName: str, indices: IEnumerable[int]) -> Array[int] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, scope: TraitScope) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AllIndicesInScope = None


class Int16Descriptor(object, IOpComparison[Int16], IDataTypeDescriptor[Int16], IOpFormatInBase[Int16], IOpFormat[Int16], IOpConversion[str, Int16], IOpNumeric[Int16], IOpBounded[Int16], IOpDigitPosition[Int16], IOpSigned[Int16], IOpBitwise[Int16], IOpAddition[Int16, Int16], IOpSubtraction[Int16, Int16], IOpMultiplication[Int16, Int16], IOpScalarMultiplication[Int16], IOpDivision[Int16, Int16], IOpRatio[Int16], IOpPower[Int16, float], IOpConversion[Int16, str], IOpLosslessConversion[Int16, Int16], IOpConversion[Int16, Int16], IOpLosslessConversion[Int16, float], IOpConversion[Int16, float], IOpConversion[float, Int16], IOpLosslessConversion[Int16, Single], IOpConversion[Int16, Single], IOpConversion[Single, Int16], IOpLosslessConversion[Int16, int], IOpConversion[Int16, int], IOpConversion[int, Int16], IOpLosslessConversion[Int16, Int64], IOpConversion[Int16, Int64], IOpConversion[Int64, Int16]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: Int16Descriptor, value: Int16) -> Int16 """
        pass

    def Add(self, value, offset):
        """ Add(self: Int16Descriptor, value: Int16, offset: Int16) -> Int16 """
        pass

    def And(self, left, right):
        """ And(self: Int16Descriptor, left: Int16, right: Int16) -> Int16 """
        pass

    def Compare(self, left, right):
        """ Compare(self: Int16Descriptor, left: Int16, right: Int16) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: Int16Descriptor, left: Int16, right: Int16) -> Int16 """
        pass

    def Divide(self, value, factor):
        """ Divide(self: Int16Descriptor, value: Int16, factor: Int16) -> Int16 """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: Int16Descriptor, value: Int16) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: Int16Descriptor, value: Int16) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: Int16Descriptor, value: Int16) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: Int16Descriptor, value: Int16) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: Int16Descriptor, logBase: float, value: Int16) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: Int16Descriptor, value: Int16, factor: Int16) -> Int16
        Multiply(self: Int16Descriptor, value: Int16, factor: float) -> Int16
        """
        pass

    def Negate(self, value):
        """ Negate(self: Int16Descriptor, value: Int16) -> Int16 """
        pass

    def Not(self, value):
        """ Not(self: Int16Descriptor, value: Int16) -> Int16 """
        pass

    def Or(self, left, right):
        """ Or(self: Int16Descriptor, left: Int16, right: Int16) -> Int16 """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: Int16Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> Int16
        Parse(self: Int16Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> Int16
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: Int16Descriptor, logBase: float, power: float) -> Int16 """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: Int16Descriptor, left: Int16, right: Int16) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: Int16Descriptor, value: Int16, factor: Int16) -> Int16 """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: Int16Descriptor, value: Int16, amount: int) -> Int16 """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: Int16Descriptor, value: Int16, amount: int) -> Int16 """
        pass

    def Sign(self, value):
        """ Sign(self: Int16Descriptor, value: Int16) -> int """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: Int16Descriptor, value: Int16, offset: Int16) -> Int16 """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: Int16Descriptor) -> str
        ToString(self: Int16Descriptor, value: Int16, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: Int16Descriptor, value: Int16, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: Int16Descriptor, value: Int16) -> (ConversionResult, str)
        TryConvert(self: Int16Descriptor, value: str) -> (ConversionResult, Int16)
        TryConvert(self: Int16Descriptor, value: Int16) -> (ConversionResult, Int16)
        TryConvert(self: Int16Descriptor, value: Int16) -> (ConversionResult, float)
        TryConvert(self: Int16Descriptor, value: float) -> (ConversionResult, Int16)
        TryConvert(self: Int16Descriptor, value: Int16) -> (ConversionResult, Single)
        TryConvert(self: Int16Descriptor, value: Single) -> (ConversionResult, Int16)
        TryConvert(self: Int16Descriptor, value: Int16) -> (ConversionResult, int)
        TryConvert(self: Int16Descriptor, value: int) -> (ConversionResult, Int16)
        TryConvert(self: Int16Descriptor, value: Int16) -> (ConversionResult, Int64)
        TryConvert(self: Int16Descriptor, value: Int64) -> (ConversionResult, Int16)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: Int16Descriptor, value: Int16, factor: float) -> (ConversionResult, Int16) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: Int16Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, Int16)
        TryParse(self: Int16Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, Int16)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: Int16Descriptor, left: Int16, right: Int16) -> Int16 """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: Int16Descriptor) -> Int16

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: Int16Descriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: Int16Descriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: Int16Descriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: Int16Descriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: Int16Descriptor) -> Int16

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: Int16Descriptor) -> Int16

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: Int16Descriptor) -> Int16

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: Int16Descriptor) -> Int16

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: Int16Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: Int16Descriptor) -> Int16

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: Int16Descriptor) -> Int16

"""



class Int32Descriptor(object, IOpComparison[int], IDataTypeDescriptor[int], IOpFormatInBase[int], IOpFormat[int], IOpConversion[str, int], IOpNumeric[int], IOpBounded[int], IOpDigitPosition[int], IOpSigned[int], IOpBitwise[int], IOpAddition[int, int], IOpSubtraction[int, int], IOpMultiplication[int, int], IOpScalarMultiplication[int], IOpDivision[int, int], IOpRatio[int], IOpPower[int, float], IOpConversion[int, str], IOpLosslessConversion[int, int], IOpConversion[int, int], IOpLosslessConversion[int, float], IOpConversion[int, float], IOpConversion[float, int], IOpConversion[int, Single], IOpConversion[Single, int], IOpLosslessConversion[int, Int64], IOpConversion[int, Int64], IOpConversion[Int64, int]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: Int32Descriptor, value: int) -> int """
        pass

    def Add(self, value, offset):
        """ Add(self: Int32Descriptor, value: int, offset: int) -> int """
        pass

    def And(self, left, right):
        """ And(self: Int32Descriptor, left: int, right: int) -> int """
        pass

    def Compare(self, left, right):
        """ Compare(self: Int32Descriptor, left: int, right: int) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: Int32Descriptor, left: int, right: int) -> int """
        pass

    def Divide(self, value, factor):
        """ Divide(self: Int32Descriptor, value: int, factor: int) -> int """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: Int32Descriptor, value: int) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: Int32Descriptor, value: int) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: Int32Descriptor, value: int) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: Int32Descriptor, value: int) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: Int32Descriptor, logBase: float, value: int) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: Int32Descriptor, value: int, factor: int) -> int
        Multiply(self: Int32Descriptor, value: int, factor: float) -> int
        """
        pass

    def Negate(self, value):
        """ Negate(self: Int32Descriptor, value: int) -> int """
        pass

    def Not(self, value):
        """ Not(self: Int32Descriptor, value: int) -> int """
        pass

    def Or(self, left, right):
        """ Or(self: Int32Descriptor, left: int, right: int) -> int """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: Int32Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> int
        Parse(self: Int32Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> int
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: Int32Descriptor, logBase: float, power: float) -> int """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: Int32Descriptor, left: int, right: int) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: Int32Descriptor, value: int, factor: int) -> int """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: Int32Descriptor, value: int, amount: int) -> int """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: Int32Descriptor, value: int, amount: int) -> int """
        pass

    def Sign(self, value):
        """ Sign(self: Int32Descriptor, value: int) -> int """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: Int32Descriptor, value: int, offset: int) -> int """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: Int32Descriptor) -> str
        ToString(self: Int32Descriptor, value: int, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: Int32Descriptor, value: int, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: Int32Descriptor, value: int) -> (ConversionResult, str)
        TryConvert(self: Int32Descriptor, value: str) -> (ConversionResult, int)
        TryConvert(self: Int32Descriptor, value: int) -> (ConversionResult, int)
        TryConvert(self: Int32Descriptor, value: int) -> (ConversionResult, float)
        TryConvert(self: Int32Descriptor, value: float) -> (ConversionResult, int)
        TryConvert(self: Int32Descriptor, value: int) -> (ConversionResult, Single)
        TryConvert(self: Int32Descriptor, value: Single) -> (ConversionResult, int)
        TryConvert(self: Int32Descriptor, value: int) -> (ConversionResult, Int64)
        TryConvert(self: Int32Descriptor, value: Int64) -> (ConversionResult, int)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: Int32Descriptor, value: int, factor: float) -> (ConversionResult, int) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: Int32Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, int)
        TryParse(self: Int32Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, int)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: Int32Descriptor, left: int, right: int) -> int """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: Int32Descriptor) -> int

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: Int32Descriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: Int32Descriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: Int32Descriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: Int32Descriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: Int32Descriptor) -> int

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: Int32Descriptor) -> int

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: Int32Descriptor) -> int

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: Int32Descriptor) -> int

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: Int32Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: Int32Descriptor) -> int

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: Int32Descriptor) -> int

"""



class Int64Descriptor(object, IOpComparison[Int64], IDataTypeDescriptor[Int64], IOpFormatInBase[Int64], IOpFormat[Int64], IOpConversion[str, Int64], IOpNumeric[Int64], IOpBounded[Int64], IOpDigitPosition[Int64], IOpSigned[Int64], IOpBitwise[Int64], IOpAddition[Int64, Int64], IOpSubtraction[Int64, Int64], IOpMultiplication[Int64, Int64], IOpScalarMultiplication[Int64], IOpDivision[Int64, Int64], IOpRatio[Int64], IOpPower[Int64, float], IOpConversion[Int64, str], IOpLosslessConversion[Int64, Int64], IOpConversion[Int64, Int64], IOpConversion[Int64, float], IOpConversion[float, Int64], IOpConversion[Int64, Single], IOpConversion[Single, Int64]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: Int64Descriptor, value: Int64) -> Int64 """
        pass

    def Add(self, value, offset):
        """ Add(self: Int64Descriptor, value: Int64, offset: Int64) -> Int64 """
        pass

    def And(self, left, right):
        """ And(self: Int64Descriptor, left: Int64, right: Int64) -> Int64 """
        pass

    def Compare(self, left, right):
        """ Compare(self: Int64Descriptor, left: Int64, right: Int64) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: Int64Descriptor, left: Int64, right: Int64) -> Int64 """
        pass

    def Divide(self, value, factor):
        """ Divide(self: Int64Descriptor, value: Int64, factor: Int64) -> Int64 """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: Int64Descriptor, value: Int64) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: Int64Descriptor, value: Int64) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: Int64Descriptor, value: Int64) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: Int64Descriptor, value: Int64) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: Int64Descriptor, logBase: float, value: Int64) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: Int64Descriptor, value: Int64, factor: Int64) -> Int64
        Multiply(self: Int64Descriptor, value: Int64, factor: float) -> Int64
        """
        pass

    def Negate(self, value):
        """ Negate(self: Int64Descriptor, value: Int64) -> Int64 """
        pass

    def Not(self, value):
        """ Not(self: Int64Descriptor, value: Int64) -> Int64 """
        pass

    def Or(self, left, right):
        """ Or(self: Int64Descriptor, left: Int64, right: Int64) -> Int64 """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: Int64Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> Int64
        Parse(self: Int64Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> Int64
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: Int64Descriptor, logBase: float, power: float) -> Int64 """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: Int64Descriptor, left: Int64, right: Int64) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: Int64Descriptor, value: Int64, factor: Int64) -> Int64 """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: Int64Descriptor, value: Int64, amount: int) -> Int64 """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: Int64Descriptor, value: Int64, amount: int) -> Int64 """
        pass

    def Sign(self, value):
        """ Sign(self: Int64Descriptor, value: Int64) -> int """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: Int64Descriptor, value: Int64, offset: Int64) -> Int64 """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: Int64Descriptor) -> str
        ToString(self: Int64Descriptor, value: Int64, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: Int64Descriptor, value: Int64, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: Int64Descriptor, value: Int64) -> (ConversionResult, str)
        TryConvert(self: Int64Descriptor, value: str) -> (ConversionResult, Int64)
        TryConvert(self: Int64Descriptor, value: Int64) -> (ConversionResult, Int64)
        TryConvert(self: Int64Descriptor, value: Int64) -> (ConversionResult, float)
        TryConvert(self: Int64Descriptor, value: float) -> (ConversionResult, Int64)
        TryConvert(self: Int64Descriptor, value: Int64) -> (ConversionResult, Single)
        TryConvert(self: Int64Descriptor, value: Single) -> (ConversionResult, Int64)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: Int64Descriptor, value: Int64, factor: float) -> (ConversionResult, Int64) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: Int64Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, Int64)
        TryParse(self: Int64Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, Int64)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: Int64Descriptor, left: Int64, right: Int64) -> Int64 """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: Int64Descriptor) -> Int64

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: Int64Descriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: Int64Descriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: Int64Descriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: Int64Descriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: Int64Descriptor) -> Int64

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: Int64Descriptor) -> Int64

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: Int64Descriptor) -> Int64

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: Int64Descriptor) -> Int64

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: Int64Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: Int64Descriptor) -> Int64

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: Int64Descriptor) -> Int64

"""



class NoOpUnitConverter(object, IUnitConverter[TData]):
    """ NoOpUnitConverter[TData](from: Unit, to: Unit) """
    def ToString(self):
        """ ToString(self: NoOpUnitConverter[TData]) -> str """
        pass

    def TryConvert(self, value, result):
        """ TryConvert(self: NoOpUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def TryConvertBack(self, value, result):
        """ TryConvertBack(self: NoOpUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, from, to):
        """ __new__(cls: type, from: Unit, to: Unit) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanConvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvert(self: NoOpUnitConverter[TData]) -> bool

"""

    CanConvertBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvertBack(self: NoOpUnitConverter[TData]) -> bool

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: NoOpUnitConverter[TData]) -> Unit

"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: NoOpUnitConverter[TData]) -> Unit

"""



class ObservableCollectionDescriptor(object, IOpObservable[TCollection], IOpMultiSample[TCollection], IDataTypeDescriptor[TCollection]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
# Error generating skeleton for function Compose: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: ObservableCollectionDescriptor[TCollection, TData], value: TCollection, decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
# Error generating skeleton for function GetDefaultValue: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: ObservableCollectionDescriptor[TCollection, TData], value: TCollection, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def GetValueObserver(self, value, decomposeOption):
        """ GetValueObserver(self: ObservableCollectionDescriptor[TCollection, TData], value: TCollection, decomposeOption: Trait) -> IValueObserver[TCollection] """
        pass

    def ToString(self):
        """ ToString(self: ObservableCollectionDescriptor[TCollection, TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class PowerOffsetUnitConverter(object):
    # no doc
    @staticmethod
    def Create(from, to, power, offset=None):
        """
        Create[TData](from: Unit, to: Unit, power: RationalInt32, offset: RationalInt32) -> IUnitConverter[TData]
        Create[TData](from: Unit, to: Unit, power: RationalInt32) -> IUnitConverter[TData]
        """
        pass

    def ToString(self):
        """ ToString(self: PowerOffsetUnitConverter) -> str """
        pass

    CanConvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvert(self: PowerOffsetUnitConverter) -> bool

"""

    CanConvertBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvertBack(self: PowerOffsetUnitConverter) -> bool

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: PowerOffsetUnitConverter) -> Unit

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: PowerOffsetUnitConverter) -> RationalInt32

"""

    Power = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Power(self: PowerOffsetUnitConverter) -> RationalInt32

"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: PowerOffsetUnitConverter) -> Unit

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: PowerOffsetUnitConverter) -> Type

"""



class PrecisionTimeDescriptor(object, IOpComparison[PrecisionDateTime], IDataTypeDescriptor[PrecisionDateTime], IOpComparison[PrecisionTimeSpan], IDataTypeDescriptor[PrecisionTimeSpan], IOpFormat[PrecisionDateTime], IOpConversion[str, PrecisionDateTime], IOpFormat[PrecisionTimeSpan], IOpConversion[str, PrecisionTimeSpan], IOpNumeric[PrecisionDateTime], IOpNumeric[PrecisionTimeSpan], IOpBounded[PrecisionDateTime], IOpBounded[PrecisionTimeSpan], IOpDigitPosition[PrecisionDateTime], IOpDigitPosition[PrecisionTimeSpan], IOpSigned[PrecisionTimeSpan], IOpContinuous[PrecisionDateTime], IOpContinuous[PrecisionTimeSpan], IOpAddition[PrecisionDateTime, PrecisionTimeSpan], IOpAddition[PrecisionTimeSpan, PrecisionTimeSpan], IOpSubtraction[PrecisionDateTime, PrecisionTimeSpan], IOpSubtraction[PrecisionTimeSpan, PrecisionTimeSpan], IOpDivision[PrecisionDateTime, PrecisionTimeSpan], IOpDivision[PrecisionTimeSpan, PrecisionTimeSpan], IOpRatio[PrecisionTimeSpan], IOpMultiplication[PrecisionDateTime, PrecisionTimeSpan], IOpMultiplication[PrecisionTimeSpan, PrecisionTimeSpan], IOpScalarMultiplication[PrecisionTimeSpan], IOpScalarMultiplication[PrecisionDateTime], IOpLosslessConversion[PrecisionDateTime, PrecisionDateTime], IOpConversion[PrecisionDateTime, PrecisionDateTime], IOpLosslessConversion[PrecisionTimeSpan, PrecisionTimeSpan], IOpConversion[PrecisionTimeSpan, PrecisionTimeSpan], IOpConversion[PrecisionDateTime, str], IOpConversion[PrecisionTimeSpan, str], IOpConversion[PrecisionDateTime, PrecisionTimeSpan], IOpConversion[PrecisionTimeSpan, PrecisionDateTime], IOpConversion[PrecisionDateTime, float], IOpConversion[float, PrecisionDateTime], IOpConversion[PrecisionTimeSpan, float], IOpConversion[float, PrecisionTimeSpan], IOpConversion[PrecisionDateTime, DateTime], IOpConversion[PrecisionTimeSpan, TimeSpan], IOpConversion[DateTime, PrecisionDateTime], IOpConversion[TimeSpan, PrecisionTimeSpan]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def Add(self, value, offset):
        """
        Add(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, offset: PrecisionTimeSpan) -> PrecisionTimeSpan
        Add(self: PrecisionTimeDescriptor, value: PrecisionDateTime, offset: PrecisionTimeSpan) -> PrecisionDateTime
        """
        pass

    def Ceiling(self, value):
        """
        Ceiling(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> PrecisionDateTime
        Ceiling(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def Compare(self, left, right):
        """
        Compare(self: PrecisionTimeDescriptor, left: PrecisionDateTime, right: PrecisionDateTime) -> int
        Compare(self: PrecisionTimeDescriptor, left: PrecisionTimeSpan, right: PrecisionTimeSpan) -> int
        """
        pass

    def Convert(self, value):
        """
        Convert(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> PrecisionDateTime
        Convert(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def Difference(self, left, right):
        """
        Difference(self: PrecisionTimeDescriptor, left: PrecisionDateTime, right: PrecisionDateTime) -> PrecisionTimeSpan
        Difference(self: PrecisionTimeDescriptor, left: PrecisionTimeSpan, right: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def Divide(self, value, factor):
        """
        Divide(self: PrecisionTimeDescriptor, value: PrecisionDateTime, factor: PrecisionTimeSpan) -> PrecisionDateTime
        Divide(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, factor: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def Floor(self, value):
        """
        Floor(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> PrecisionDateTime
        Floor(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """
        GetLargestFractionalDigitPosition(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> int
        GetLargestFractionalDigitPosition(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> int
        """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """
        GetLargestIntegralDigitPosition(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> int
        GetLargestIntegralDigitPosition(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> int
        """
        pass

    def IsDefined(self, value):
        """
        IsDefined(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> bool
        IsDefined(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> bool
        """
        pass

    def IsInfinite(self, value):
        """
        IsInfinite(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> bool
        IsInfinite(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> bool
        """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, factor: float) -> PrecisionTimeSpan
        Multiply(self: PrecisionTimeDescriptor, value: PrecisionDateTime, factor: float) -> PrecisionDateTime
        Multiply(self: PrecisionTimeDescriptor, value: PrecisionDateTime, factor: PrecisionTimeSpan) -> PrecisionDateTime
        Multiply(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, factor: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def Negate(self, value):
        """ Negate(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: PrecisionTimeDescriptor, left: PrecisionTimeSpan, right: PrecisionTimeSpan) -> float """
        pass

    def Remainder(self, value, factor):
        """
        Remainder(self: PrecisionTimeDescriptor, value: PrecisionDateTime, factor: PrecisionTimeSpan) -> PrecisionTimeSpan
        Remainder(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, factor: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def Round(self, value, digits=None):
        """
        Round(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> PrecisionDateTime
        Round(self: PrecisionTimeDescriptor, value: PrecisionDateTime, digits: int) -> PrecisionDateTime
        Round(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan
        Round(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, digits: int) -> PrecisionTimeSpan
        """
        pass

    def Sign(self, value):
        """ Sign(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> int """
        pass

    def Subtract(self, value, offset):
        """
        Subtract(self: PrecisionTimeDescriptor, value: PrecisionDateTime, offset: PrecisionTimeSpan) -> PrecisionDateTime
        Subtract(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, offset: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: PrecisionTimeDescriptor) -> str
        ToString(self: PrecisionTimeDescriptor, value: PrecisionDateTime, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def Truncate(self, value):
        """
        Truncate(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> PrecisionDateTime
        Truncate(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> PrecisionTimeSpan
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> (ConversionResult, PrecisionTimeSpan)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> (ConversionResult, str)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> (ConversionResult, str)
        TryConvert(self: PrecisionTimeDescriptor, value: str) -> (ConversionResult, PrecisionDateTime)
        TryConvert(self: PrecisionTimeDescriptor, value: str) -> (ConversionResult, PrecisionTimeSpan)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> (ConversionResult, PrecisionTimeSpan)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> (ConversionResult, PrecisionDateTime)
        TryConvert(self: PrecisionTimeDescriptor, value: float) -> (ConversionResult, PrecisionDateTime)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> (ConversionResult, float)
        TryConvert(self: PrecisionTimeDescriptor, value: float) -> (ConversionResult, PrecisionTimeSpan)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> (ConversionResult, float)
        TryConvert(self: PrecisionTimeDescriptor, value: DateTime) -> (ConversionResult, PrecisionDateTime)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> (ConversionResult, DateTime)
        TryConvert(self: PrecisionTimeDescriptor, value: TimeSpan) -> (ConversionResult, PrecisionTimeSpan)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan) -> (ConversionResult, TimeSpan)
        TryConvert(self: PrecisionTimeDescriptor, value: PrecisionDateTime) -> (ConversionResult, PrecisionDateTime)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """
        TryMultiply(self: PrecisionTimeDescriptor, value: PrecisionTimeSpan, factor: float) -> (ConversionResult, PrecisionTimeSpan)
        TryMultiply(self: PrecisionTimeDescriptor, value: PrecisionDateTime, factor: float) -> (ConversionResult, PrecisionDateTime)
        """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """
        TryParse(self: PrecisionTimeDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, PrecisionDateTime)
        TryParse(self: PrecisionTimeDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, PrecisionTimeSpan)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    MaximumRoundDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumRoundDigits(self: PrecisionTimeDescriptor) -> int

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: PrecisionTimeDescriptor) -> PrecisionTimeSpan

"""



class ReversedUnitConverter(object, IUnitConverter[TData]):
    """ ReversedUnitConverter[TData](converter: IUnitConverter[TData]) """
    def ToString(self):
        """ ToString(self: ReversedUnitConverter[TData]) -> str """
        pass

    def TryConvert(self, value, result):
        """ TryConvert(self: ReversedUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def TryConvertBack(self, value, result):
        """ TryConvertBack(self: ReversedUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, converter):
        """ __new__(cls: type, converter: IUnitConverter[TData]) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CanConvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvert(self: ReversedUnitConverter[TData]) -> bool

"""

    CanConvertBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvertBack(self: ReversedUnitConverter[TData]) -> bool

"""

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Converter(self: ReversedUnitConverter[TData]) -> IUnitConverter[TData]

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: ReversedUnitConverter[TData]) -> Unit

"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: ReversedUnitConverter[TData]) -> Unit

"""



class SByteDescriptor(object, IOpComparison[SByte], IDataTypeDescriptor[SByte], IOpFormatInBase[SByte], IOpFormat[SByte], IOpConversion[str, SByte], IOpNumeric[SByte], IOpBounded[SByte], IOpDigitPosition[SByte], IOpSigned[SByte], IOpBitwise[SByte], IOpAddition[SByte, SByte], IOpSubtraction[SByte, SByte], IOpMultiplication[SByte, SByte], IOpScalarMultiplication[SByte], IOpDivision[SByte, SByte], IOpRatio[SByte], IOpPower[SByte, float], IOpConversion[SByte, str], IOpLosslessConversion[SByte, SByte], IOpConversion[SByte, SByte], IOpLosslessConversion[SByte, float], IOpConversion[SByte, float], IOpConversion[float, SByte], IOpLosslessConversion[SByte, Single], IOpConversion[SByte, Single], IOpConversion[Single, SByte], IOpLosslessConversion[SByte, Int16], IOpConversion[SByte, Int16], IOpConversion[Int16, SByte], IOpLosslessConversion[SByte, int], IOpConversion[SByte, int], IOpConversion[int, SByte], IOpLosslessConversion[SByte, Int64], IOpConversion[SByte, Int64], IOpConversion[Int64, SByte]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: SByteDescriptor, value: SByte) -> SByte """
        pass

    def Add(self, value, offset):
        """ Add(self: SByteDescriptor, value: SByte, offset: SByte) -> SByte """
        pass

    def And(self, left, right):
        """ And(self: SByteDescriptor, left: SByte, right: SByte) -> SByte """
        pass

    def Compare(self, left, right):
        """ Compare(self: SByteDescriptor, left: SByte, right: SByte) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: SByteDescriptor, left: SByte, right: SByte) -> SByte """
        pass

    def Divide(self, value, factor):
        """ Divide(self: SByteDescriptor, value: SByte, factor: SByte) -> SByte """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: SByteDescriptor, value: SByte) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: SByteDescriptor, value: SByte) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: SByteDescriptor, value: SByte) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: SByteDescriptor, value: SByte) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: SByteDescriptor, logBase: float, value: SByte) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: SByteDescriptor, value: SByte, factor: SByte) -> SByte
        Multiply(self: SByteDescriptor, value: SByte, factor: float) -> SByte
        """
        pass

    def Negate(self, value):
        """ Negate(self: SByteDescriptor, value: SByte) -> SByte """
        pass

    def Not(self, value):
        """ Not(self: SByteDescriptor, value: SByte) -> SByte """
        pass

    def Or(self, left, right):
        """ Or(self: SByteDescriptor, left: SByte, right: SByte) -> SByte """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: SByteDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> SByte
        Parse(self: SByteDescriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> SByte
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: SByteDescriptor, logBase: float, power: float) -> SByte """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: SByteDescriptor, left: SByte, right: SByte) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: SByteDescriptor, value: SByte, factor: SByte) -> SByte """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: SByteDescriptor, value: SByte, amount: int) -> SByte """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: SByteDescriptor, value: SByte, amount: int) -> SByte """
        pass

    def Sign(self, value):
        """ Sign(self: SByteDescriptor, value: SByte) -> int """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: SByteDescriptor, value: SByte, offset: SByte) -> SByte """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: SByteDescriptor) -> str
        ToString(self: SByteDescriptor, value: SByte, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: SByteDescriptor, value: SByte, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, str)
        TryConvert(self: SByteDescriptor, value: str) -> (ConversionResult, SByte)
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, SByte)
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, float)
        TryConvert(self: SByteDescriptor, value: float) -> (ConversionResult, SByte)
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, Single)
        TryConvert(self: SByteDescriptor, value: Single) -> (ConversionResult, SByte)
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, Int16)
        TryConvert(self: SByteDescriptor, value: Int16) -> (ConversionResult, SByte)
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, int)
        TryConvert(self: SByteDescriptor, value: int) -> (ConversionResult, SByte)
        TryConvert(self: SByteDescriptor, value: SByte) -> (ConversionResult, Int64)
        TryConvert(self: SByteDescriptor, value: Int64) -> (ConversionResult, SByte)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: SByteDescriptor, value: SByte, factor: float) -> (ConversionResult, SByte) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: SByteDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, SByte)
        TryParse(self: SByteDescriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, SByte)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: SByteDescriptor, left: SByte, right: SByte) -> SByte """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: SByteDescriptor) -> SByte

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: SByteDescriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: SByteDescriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: SByteDescriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: SByteDescriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: SByteDescriptor) -> SByte

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: SByteDescriptor) -> SByte

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: SByteDescriptor) -> SByte

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: SByteDescriptor) -> SByte

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: SByteDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: SByteDescriptor) -> SByte

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: SByteDescriptor) -> SByte

"""



class SingleDescriptor(object, IOpComparison[Single], IDataTypeDescriptor[Single], IOpFormat[Single], IOpConversion[str, Single], IOpNumeric[Single], IOpBounded[Single], IOpDigitPosition[Single], IOpSigned[Single], IOpInfinity[Single], IOpContinuous[Single], IOpAddition[Single, Single], IOpSubtraction[Single, Single], IOpMultiplication[Single, Single], IOpScalarMultiplication[Single], IOpDivision[Single, Single], IOpRatio[Single], IOpPower[Single, float], IOpConversion[Single, str], IOpLosslessConversion[Single, Single], IOpConversion[Single, Single], IOpLosslessConversion[Single, float], IOpConversion[Single, float], IOpConversion[float, Single]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: SingleDescriptor, value: Single) -> Single """
        pass

    def Add(self, value, offset):
        """ Add(self: SingleDescriptor, value: Single, offset: Single) -> Single """
        pass

    def Ceiling(self, value):
        """ Ceiling(self: SingleDescriptor, value: Single) -> Single """
        pass

    def Compare(self, left, right):
        """ Compare(self: SingleDescriptor, left: Single, right: Single) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: SingleDescriptor, left: Single, right: Single) -> Single """
        pass

    def Divide(self, value, factor):
        """ Divide(self: SingleDescriptor, value: Single, factor: Single) -> Single """
        pass

    def Floor(self, value):
        """ Floor(self: SingleDescriptor, value: Single) -> Single """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: SingleDescriptor, value: Single) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: SingleDescriptor, value: Single) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: SingleDescriptor, value: Single) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: SingleDescriptor, value: Single) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: SingleDescriptor, logBase: float, value: Single) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: SingleDescriptor, value: Single, factor: Single) -> Single
        Multiply(self: SingleDescriptor, value: Single, factor: float) -> Single
        """
        pass

    def Negate(self, value):
        """ Negate(self: SingleDescriptor, value: Single) -> Single """
        pass

    def Parse(self, input, format, formatProvider):
        """ Parse(self: SingleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> Single """
        pass

    def Power(self, logBase, power):
        """ Power(self: SingleDescriptor, logBase: float, power: float) -> Single """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: SingleDescriptor, left: Single, right: Single) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: SingleDescriptor, value: Single, factor: Single) -> Single """
        pass

    def Round(self, value, digits=None):
        """
        Round(self: SingleDescriptor, value: Single) -> Single
        Round(self: SingleDescriptor, value: Single, digits: int) -> Single
        """
        pass

    def Sign(self, value):
        """ Sign(self: SingleDescriptor, value: Single) -> int """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: SingleDescriptor, value: Single, offset: Single) -> Single """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: SingleDescriptor) -> str
        ToString(self: SingleDescriptor, value: Single, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def Truncate(self, value):
        """ Truncate(self: SingleDescriptor, value: Single) -> Single """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: SingleDescriptor, value: Single) -> (ConversionResult, str)
        TryConvert(self: SingleDescriptor, value: str) -> (ConversionResult, Single)
        TryConvert(self: SingleDescriptor, value: Single) -> (ConversionResult, Single)
        TryConvert(self: SingleDescriptor, value: Single) -> (ConversionResult, float)
        TryConvert(self: SingleDescriptor, value: float) -> (ConversionResult, Single)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: SingleDescriptor, value: Single, factor: float) -> (ConversionResult, Single) """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """ TryParse(self: SingleDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, Single) """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: SingleDescriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: SingleDescriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: SingleDescriptor) -> float

"""

    Infinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Infinity(self: SingleDescriptor) -> Single

"""

    MaximumRoundDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumRoundDigits(self: SingleDescriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: SingleDescriptor) -> Single

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: SingleDescriptor) -> Single

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: SingleDescriptor) -> Single

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: SingleDescriptor) -> Single

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: SingleDescriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: SingleDescriptor) -> Single

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: SingleDescriptor) -> Single

"""



class SpectrumDescriptor(object, IOpMultiSample[Spectrum[TData]], IDataTypeDescriptor[Spectrum[TData]], IOpObservable[Spectrum[TData]]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: SpectrumDescriptor[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> Spectrum[TData] """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: SpectrumDescriptor[TData], value: Spectrum[TData], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: SpectrumDescriptor[TData]) -> Spectrum[TData] """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: SpectrumDescriptor[TData], value: Spectrum[TData], decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def GetValueObserver(self, value, decomposeOption):
        """ GetValueObserver(self: SpectrumDescriptor[TData], value: Spectrum[TData], decomposeOption: Trait) -> IValueObserver[Spectrum[TData]] """
        pass

    def ToString(self):
        """ ToString(self: SpectrumDescriptor[TData]) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class StringDescriptor(object, IDataTypeDescriptor[str], IOpLosslessConversion[str, str], IOpConversion[str, str]):
    # no doc
    def Convert(self, value):
        """ Convert(self: StringDescriptor, value: str) -> str """
        pass

    def ToString(self):
        """ ToString(self: StringDescriptor) -> str """
        pass

    def TryConvert(self, value, result):
        """ TryConvert(self: StringDescriptor, value: str) -> (ConversionResult, str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass


class TimeDescriptor(object, IOpComparison[DateTime], IDataTypeDescriptor[DateTime], IOpComparison[TimeSpan], IDataTypeDescriptor[TimeSpan], IOpFormat[DateTime], IOpConversion[str, DateTime], IOpFormat[TimeSpan], IOpConversion[str, TimeSpan], IOpNumeric[DateTime], IOpNumeric[TimeSpan], IOpBounded[DateTime], IOpBounded[TimeSpan], IOpDigitPosition[DateTime], IOpDigitPosition[TimeSpan], IOpSigned[TimeSpan], IOpContinuous[DateTime], IOpContinuous[TimeSpan], IOpAddition[DateTime, TimeSpan], IOpAddition[TimeSpan, TimeSpan], IOpSubtraction[DateTime, TimeSpan], IOpSubtraction[TimeSpan, TimeSpan], IOpDivision[DateTime, TimeSpan], IOpDivision[TimeSpan, TimeSpan], IOpRatio[TimeSpan], IOpMultiplication[DateTime, TimeSpan], IOpMultiplication[TimeSpan, TimeSpan], IOpScalarMultiplication[TimeSpan], IOpScalarMultiplication[DateTime], IOpLosslessConversion[DateTime, DateTime], IOpConversion[DateTime, DateTime], IOpLosslessConversion[TimeSpan, TimeSpan], IOpConversion[TimeSpan, TimeSpan], IOpConversion[DateTime, str], IOpConversion[TimeSpan, str], IOpConversion[DateTime, TimeSpan], IOpConversion[TimeSpan, DateTime], IOpConversion[DateTime, float], IOpConversion[float, DateTime], IOpConversion[TimeSpan, float], IOpConversion[float, TimeSpan]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: TimeDescriptor, value: TimeSpan) -> TimeSpan """
        pass

    def Add(self, value, offset):
        """
        Add(self: TimeDescriptor, value: TimeSpan, offset: TimeSpan) -> TimeSpan
        Add(self: TimeDescriptor, value: DateTime, offset: TimeSpan) -> DateTime
        """
        pass

    def Ceiling(self, value):
        """
        Ceiling(self: TimeDescriptor, value: DateTime) -> DateTime
        Ceiling(self: TimeDescriptor, value: TimeSpan) -> TimeSpan
        """
        pass

    def Compare(self, left, right):
        """
        Compare(self: TimeDescriptor, left: DateTime, right: DateTime) -> int
        Compare(self: TimeDescriptor, left: TimeSpan, right: TimeSpan) -> int
        """
        pass

    def Convert(self, value):
        """
        Convert(self: TimeDescriptor, value: DateTime) -> DateTime
        Convert(self: TimeDescriptor, value: TimeSpan) -> TimeSpan
        """
        pass

    def Difference(self, left, right):
        """
        Difference(self: TimeDescriptor, left: DateTime, right: DateTime) -> TimeSpan
        Difference(self: TimeDescriptor, left: TimeSpan, right: TimeSpan) -> TimeSpan
        """
        pass

    def Divide(self, value, factor):
        """
        Divide(self: TimeDescriptor, value: DateTime, factor: TimeSpan) -> DateTime
        Divide(self: TimeDescriptor, value: TimeSpan, factor: TimeSpan) -> TimeSpan
        """
        pass

    def Floor(self, value):
        """
        Floor(self: TimeDescriptor, value: DateTime) -> DateTime
        Floor(self: TimeDescriptor, value: TimeSpan) -> TimeSpan
        """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """
        GetLargestFractionalDigitPosition(self: TimeDescriptor, value: DateTime) -> int
        GetLargestFractionalDigitPosition(self: TimeDescriptor, value: TimeSpan) -> int
        """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """
        GetLargestIntegralDigitPosition(self: TimeDescriptor, value: DateTime) -> int
        GetLargestIntegralDigitPosition(self: TimeDescriptor, value: TimeSpan) -> int
        """
        pass

    def IsDefined(self, value):
        """
        IsDefined(self: TimeDescriptor, value: DateTime) -> bool
        IsDefined(self: TimeDescriptor, value: TimeSpan) -> bool
        """
        pass

    def IsInfinite(self, value):
        """
        IsInfinite(self: TimeDescriptor, value: DateTime) -> bool
        IsInfinite(self: TimeDescriptor, value: TimeSpan) -> bool
        """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: TimeDescriptor, value: TimeSpan, factor: float) -> TimeSpan
        Multiply(self: TimeDescriptor, value: DateTime, factor: float) -> DateTime
        Multiply(self: TimeDescriptor, value: DateTime, factor: TimeSpan) -> DateTime
        Multiply(self: TimeDescriptor, value: TimeSpan, factor: TimeSpan) -> TimeSpan
        """
        pass

    def Negate(self, value):
        """ Negate(self: TimeDescriptor, value: TimeSpan) -> TimeSpan """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: TimeDescriptor, left: TimeSpan, right: TimeSpan) -> float """
        pass

    def Remainder(self, value, factor):
        """
        Remainder(self: TimeDescriptor, value: DateTime, factor: TimeSpan) -> TimeSpan
        Remainder(self: TimeDescriptor, value: TimeSpan, factor: TimeSpan) -> TimeSpan
        """
        pass

    def Round(self, value, digits=None):
        """
        Round(self: TimeDescriptor, value: DateTime) -> DateTime
        Round(self: TimeDescriptor, value: DateTime, digits: int) -> DateTime
        Round(self: TimeDescriptor, value: TimeSpan) -> TimeSpan
        Round(self: TimeDescriptor, value: TimeSpan, digits: int) -> TimeSpan
        """
        pass

    def Sign(self, value):
        """ Sign(self: TimeDescriptor, value: TimeSpan) -> int """
        pass

    def Subtract(self, value, offset):
        """
        Subtract(self: TimeDescriptor, value: DateTime, offset: TimeSpan) -> DateTime
        Subtract(self: TimeDescriptor, value: TimeSpan, offset: TimeSpan) -> TimeSpan
        """
        pass

    def ToString(self, value=None, format=None, formatProvider=None):
        """
        ToString(self: TimeDescriptor) -> str
        ToString(self: TimeDescriptor, value: DateTime, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: TimeDescriptor, value: TimeSpan, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def Truncate(self, value):
        """
        Truncate(self: TimeDescriptor, value: DateTime) -> DateTime
        Truncate(self: TimeDescriptor, value: TimeSpan) -> TimeSpan
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: TimeDescriptor, value: TimeSpan) -> (ConversionResult, TimeSpan)
        TryConvert(self: TimeDescriptor, value: DateTime) -> (ConversionResult, str)
        TryConvert(self: TimeDescriptor, value: TimeSpan) -> (ConversionResult, str)
        TryConvert(self: TimeDescriptor, value: str) -> (ConversionResult, DateTime)
        TryConvert(self: TimeDescriptor, value: str) -> (ConversionResult, TimeSpan)
        TryConvert(self: TimeDescriptor, value: DateTime) -> (ConversionResult, TimeSpan)
        TryConvert(self: TimeDescriptor, value: TimeSpan) -> (ConversionResult, DateTime)
        TryConvert(self: TimeDescriptor, value: float) -> (ConversionResult, DateTime)
        TryConvert(self: TimeDescriptor, value: DateTime) -> (ConversionResult, float)
        TryConvert(self: TimeDescriptor, value: float) -> (ConversionResult, TimeSpan)
        TryConvert(self: TimeDescriptor, value: TimeSpan) -> (ConversionResult, float)
        TryConvert(value: Int64) -> (ConversionResult, DateTime)
        TryConvert(value: DateTime) -> (ConversionResult, Int64)
        TryConvert(self: TimeDescriptor, value: DateTime) -> (ConversionResult, DateTime)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """
        TryMultiply(self: TimeDescriptor, value: TimeSpan, factor: float) -> (ConversionResult, TimeSpan)
        TryMultiply(self: TimeDescriptor, value: DateTime, factor: float) -> (ConversionResult, DateTime)
        """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """
        TryParse(self: TimeDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, DateTime)
        TryParse(self: TimeDescriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, TimeSpan)
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    MaximumRoundDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumRoundDigits(self: TimeDescriptor) -> int

"""

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: TimeDescriptor) -> TimeSpan

"""



class TraitFactoryAttribute(Attribute, _Attribute):
    """ TraitFactoryAttribute(traitFactoryType: Type) """
    def ToString(self):
        """ ToString(self: TraitFactoryAttribute) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, traitFactoryType):
        """ __new__(cls: type, traitFactoryType: Type) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    TraitFactoryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TraitFactoryType(self: TraitFactoryAttribute) -> Type

"""



class TraitGroup(Trait, IEquatable[Trait]):
    """ TraitGroup(*traits: Array[Trait]) """
    @staticmethod
    def Contains(trait, target):
        """ Contains(trait: Trait, target: Trait) -> bool """
        pass

    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: TraitGroup) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: TraitGroup, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: TraitGroup, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: TraitGroup) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, traits):
        """ __new__(cls: type, *traits: Array[Trait]) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Traits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Traits(self: TraitGroup) -> ReadOnlyCollection[Trait]

"""



class UInt16Descriptor(object, IOpComparison[UInt16], IDataTypeDescriptor[UInt16], IOpFormatInBase[UInt16], IOpFormat[UInt16], IOpConversion[str, UInt16], IOpNumeric[UInt16], IOpBounded[UInt16], IOpDigitPosition[UInt16], IOpBitwise[UInt16], IOpAddition[UInt16, UInt16], IOpSubtraction[UInt16, UInt16], IOpMultiplication[UInt16, UInt16], IOpScalarMultiplication[UInt16], IOpDivision[UInt16, UInt16], IOpRatio[UInt16], IOpPower[UInt16, float], IOpConversion[UInt16, str], IOpLosslessConversion[UInt16, UInt16], IOpConversion[UInt16, UInt16], IOpLosslessConversion[UInt16, float], IOpConversion[UInt16, float], IOpConversion[float, UInt16], IOpLosslessConversion[UInt16, Single], IOpConversion[UInt16, Single], IOpConversion[Single, UInt16], IOpConversion[UInt16, Int16], IOpConversion[Int16, UInt16], IOpLosslessConversion[UInt16, UInt32], IOpConversion[UInt16, UInt32], IOpConversion[UInt32, UInt16], IOpLosslessConversion[UInt16, UInt64], IOpConversion[UInt16, UInt64], IOpConversion[UInt64, UInt16]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: UInt16Descriptor, value: UInt16, offset: UInt16) -> UInt16 """
        pass

    def And(self, left, right):
        """ And(self: UInt16Descriptor, left: UInt16, right: UInt16) -> UInt16 """
        pass

    def Compare(self, left, right):
        """ Compare(self: UInt16Descriptor, left: UInt16, right: UInt16) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: UInt16Descriptor, left: UInt16, right: UInt16) -> UInt16 """
        pass

    def Divide(self, value, factor):
        """ Divide(self: UInt16Descriptor, value: UInt16, factor: UInt16) -> UInt16 """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: UInt16Descriptor, value: UInt16) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: UInt16Descriptor, value: UInt16) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: UInt16Descriptor, value: UInt16) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: UInt16Descriptor, value: UInt16) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: UInt16Descriptor, logBase: float, value: UInt16) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: UInt16Descriptor, value: UInt16, factor: UInt16) -> UInt16
        Multiply(self: UInt16Descriptor, value: UInt16, factor: float) -> UInt16
        """
        pass

    def Not(self, value):
        """ Not(self: UInt16Descriptor, value: UInt16) -> UInt16 """
        pass

    def Or(self, left, right):
        """ Or(self: UInt16Descriptor, left: UInt16, right: UInt16) -> UInt16 """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: UInt16Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> UInt16
        Parse(self: UInt16Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> UInt16
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: UInt16Descriptor, logBase: float, power: float) -> UInt16 """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: UInt16Descriptor, left: UInt16, right: UInt16) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: UInt16Descriptor, value: UInt16, factor: UInt16) -> UInt16 """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: UInt16Descriptor, value: UInt16, amount: int) -> UInt16 """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: UInt16Descriptor, value: UInt16, amount: int) -> UInt16 """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: UInt16Descriptor, value: UInt16, offset: UInt16) -> UInt16 """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: UInt16Descriptor) -> str
        ToString(self: UInt16Descriptor, value: UInt16, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: UInt16Descriptor, value: UInt16, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, str)
        TryConvert(self: UInt16Descriptor, value: str) -> (ConversionResult, UInt16)
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, UInt16)
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, float)
        TryConvert(self: UInt16Descriptor, value: float) -> (ConversionResult, UInt16)
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, Single)
        TryConvert(self: UInt16Descriptor, value: Single) -> (ConversionResult, UInt16)
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, Int16)
        TryConvert(self: UInt16Descriptor, value: Int16) -> (ConversionResult, UInt16)
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, UInt32)
        TryConvert(self: UInt16Descriptor, value: UInt32) -> (ConversionResult, UInt16)
        TryConvert(self: UInt16Descriptor, value: UInt16) -> (ConversionResult, UInt64)
        TryConvert(self: UInt16Descriptor, value: UInt64) -> (ConversionResult, UInt16)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: UInt16Descriptor, value: UInt16, factor: float) -> (ConversionResult, UInt16) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: UInt16Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, UInt16)
        TryParse(self: UInt16Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, UInt16)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: UInt16Descriptor, left: UInt16, right: UInt16) -> UInt16 """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: UInt16Descriptor) -> UInt16

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: UInt16Descriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: UInt16Descriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: UInt16Descriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: UInt16Descriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: UInt16Descriptor) -> UInt16

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: UInt16Descriptor) -> UInt16

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: UInt16Descriptor) -> UInt16

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: UInt16Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: UInt16Descriptor) -> UInt16

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: UInt16Descriptor) -> UInt16

"""



class UInt32Descriptor(object, IOpComparison[UInt32], IDataTypeDescriptor[UInt32], IOpFormatInBase[UInt32], IOpFormat[UInt32], IOpConversion[str, UInt32], IOpNumeric[UInt32], IOpBounded[UInt32], IOpDigitPosition[UInt32], IOpBitwise[UInt32], IOpAddition[UInt32, UInt32], IOpSubtraction[UInt32, UInt32], IOpMultiplication[UInt32, UInt32], IOpScalarMultiplication[UInt32], IOpDivision[UInt32, UInt32], IOpRatio[UInt32], IOpPower[UInt32, float], IOpConversion[UInt32, str], IOpLosslessConversion[UInt32, UInt32], IOpConversion[UInt32, UInt32], IOpLosslessConversion[UInt32, float], IOpConversion[UInt32, float], IOpConversion[float, UInt32], IOpConversion[UInt32, Single], IOpConversion[Single, UInt32], IOpConversion[UInt32, int], IOpConversion[int, UInt32], IOpLosslessConversion[UInt32, UInt64], IOpConversion[UInt32, UInt64], IOpConversion[UInt64, UInt32]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: UInt32Descriptor, value: UInt32, offset: UInt32) -> UInt32 """
        pass

    def And(self, left, right):
        """ And(self: UInt32Descriptor, left: UInt32, right: UInt32) -> UInt32 """
        pass

    def Compare(self, left, right):
        """ Compare(self: UInt32Descriptor, left: UInt32, right: UInt32) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: UInt32Descriptor, left: UInt32, right: UInt32) -> UInt32 """
        pass

    def Divide(self, value, factor):
        """ Divide(self: UInt32Descriptor, value: UInt32, factor: UInt32) -> UInt32 """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: UInt32Descriptor, value: UInt32) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: UInt32Descriptor, value: UInt32) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: UInt32Descriptor, value: UInt32) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: UInt32Descriptor, value: UInt32) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: UInt32Descriptor, logBase: float, value: UInt32) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: UInt32Descriptor, value: UInt32, factor: UInt32) -> UInt32
        Multiply(self: UInt32Descriptor, value: UInt32, factor: float) -> UInt32
        """
        pass

    def Not(self, value):
        """ Not(self: UInt32Descriptor, value: UInt32) -> UInt32 """
        pass

    def Or(self, left, right):
        """ Or(self: UInt32Descriptor, left: UInt32, right: UInt32) -> UInt32 """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: UInt32Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> UInt32
        Parse(self: UInt32Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> UInt32
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: UInt32Descriptor, logBase: float, power: float) -> UInt32 """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: UInt32Descriptor, left: UInt32, right: UInt32) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: UInt32Descriptor, value: UInt32, factor: UInt32) -> UInt32 """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: UInt32Descriptor, value: UInt32, amount: int) -> UInt32 """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: UInt32Descriptor, value: UInt32, amount: int) -> UInt32 """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: UInt32Descriptor, value: UInt32, offset: UInt32) -> UInt32 """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: UInt32Descriptor) -> str
        ToString(self: UInt32Descriptor, value: UInt32, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: UInt32Descriptor, value: UInt32, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: UInt32Descriptor, value: UInt32) -> (ConversionResult, str)
        TryConvert(self: UInt32Descriptor, value: str) -> (ConversionResult, UInt32)
        TryConvert(self: UInt32Descriptor, value: UInt32) -> (ConversionResult, UInt32)
        TryConvert(self: UInt32Descriptor, value: UInt32) -> (ConversionResult, float)
        TryConvert(self: UInt32Descriptor, value: float) -> (ConversionResult, UInt32)
        TryConvert(self: UInt32Descriptor, value: UInt32) -> (ConversionResult, Single)
        TryConvert(self: UInt32Descriptor, value: Single) -> (ConversionResult, UInt32)
        TryConvert(self: UInt32Descriptor, value: UInt32) -> (ConversionResult, int)
        TryConvert(self: UInt32Descriptor, value: int) -> (ConversionResult, UInt32)
        TryConvert(self: UInt32Descriptor, value: UInt32) -> (ConversionResult, UInt64)
        TryConvert(self: UInt32Descriptor, value: UInt64) -> (ConversionResult, UInt32)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: UInt32Descriptor, value: UInt32, factor: float) -> (ConversionResult, UInt32) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: UInt32Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, UInt32)
        TryParse(self: UInt32Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, UInt32)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: UInt32Descriptor, left: UInt32, right: UInt32) -> UInt32 """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: UInt32Descriptor) -> UInt32

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: UInt32Descriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: UInt32Descriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: UInt32Descriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: UInt32Descriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: UInt32Descriptor) -> UInt32

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: UInt32Descriptor) -> UInt32

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: UInt32Descriptor) -> UInt32

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: UInt32Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: UInt32Descriptor) -> UInt32

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: UInt32Descriptor) -> UInt32

"""



class UInt64Descriptor(object, IOpComparison[UInt64], IDataTypeDescriptor[UInt64], IOpFormatInBase[UInt64], IOpFormat[UInt64], IOpConversion[str, UInt64], IOpNumeric[UInt64], IOpBounded[UInt64], IOpDigitPosition[UInt64], IOpBitwise[UInt64], IOpAddition[UInt64, UInt64], IOpSubtraction[UInt64, UInt64], IOpMultiplication[UInt64, UInt64], IOpScalarMultiplication[UInt64], IOpDivision[UInt64, UInt64], IOpRatio[UInt64], IOpPower[UInt64, float], IOpConversion[UInt64, str], IOpLosslessConversion[UInt64, UInt64], IOpConversion[UInt64, UInt64], IOpConversion[UInt64, float], IOpConversion[float, UInt64], IOpConversion[UInt64, Single], IOpConversion[Single, UInt64], IOpConversion[UInt64, Int64], IOpConversion[Int64, UInt64]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: UInt64Descriptor, value: UInt64, offset: UInt64) -> UInt64 """
        pass

    def And(self, left, right):
        """ And(self: UInt64Descriptor, left: UInt64, right: UInt64) -> UInt64 """
        pass

    def Compare(self, left, right):
        """ Compare(self: UInt64Descriptor, left: UInt64, right: UInt64) -> int """
        pass

    def Difference(self, left, right):
        """ Difference(self: UInt64Descriptor, left: UInt64, right: UInt64) -> UInt64 """
        pass

    def Divide(self, value, factor):
        """ Divide(self: UInt64Descriptor, value: UInt64, factor: UInt64) -> UInt64 """
        pass

    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: UInt64Descriptor, value: UInt64) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: UInt64Descriptor, value: UInt64) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: UInt64Descriptor, value: UInt64) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: UInt64Descriptor, value: UInt64) -> bool """
        pass

    def Logarithm(self, logBase, value):
        """ Logarithm(self: UInt64Descriptor, logBase: float, value: UInt64) -> float """
        pass

    def Multiply(self, value, factor):
        """
        Multiply(self: UInt64Descriptor, value: UInt64, factor: UInt64) -> UInt64
        Multiply(self: UInt64Descriptor, value: UInt64, factor: float) -> UInt64
        """
        pass

    def Not(self, value):
        """ Not(self: UInt64Descriptor, value: UInt64) -> UInt64 """
        pass

    def Or(self, left, right):
        """ Or(self: UInt64Descriptor, left: UInt64, right: UInt64) -> UInt64 """
        pass

    def Parse(self, input, *__args):
        """
        Parse(self: UInt64Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> UInt64
        Parse(self: UInt64Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> UInt64
        """
        pass

    def Power(self, logBase, power):
        """ Power(self: UInt64Descriptor, logBase: float, power: float) -> UInt64 """
        pass

    def Ratio(self, left, right):
        """ Ratio(self: UInt64Descriptor, left: UInt64, right: UInt64) -> float """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: UInt64Descriptor, value: UInt64, factor: UInt64) -> UInt64 """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: UInt64Descriptor, value: UInt64, amount: int) -> UInt64 """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: UInt64Descriptor, value: UInt64, amount: int) -> UInt64 """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: UInt64Descriptor, value: UInt64, offset: UInt64) -> UInt64 """
        pass

    def ToString(self, value=None, *__args):
        """
        ToString(self: UInt64Descriptor) -> str
        ToString(self: UInt64Descriptor, value: UInt64, format: str, formatProvider: IFormatProvider) -> str
        ToString(self: UInt64Descriptor, value: UInt64, toBase: int, formatProvider: IFormatProvider) -> str
        """
        pass

    def TryConvert(self, value, result):
        """
        TryConvert(self: UInt64Descriptor, value: UInt64) -> (ConversionResult, str)
        TryConvert(self: UInt64Descriptor, value: str) -> (ConversionResult, UInt64)
        TryConvert(self: UInt64Descriptor, value: UInt64) -> (ConversionResult, UInt64)
        TryConvert(self: UInt64Descriptor, value: UInt64) -> (ConversionResult, float)
        TryConvert(self: UInt64Descriptor, value: float) -> (ConversionResult, UInt64)
        TryConvert(self: UInt64Descriptor, value: UInt64) -> (ConversionResult, Single)
        TryConvert(self: UInt64Descriptor, value: Single) -> (ConversionResult, UInt64)
        TryConvert(self: UInt64Descriptor, value: UInt64) -> (ConversionResult, Int64)
        TryConvert(self: UInt64Descriptor, value: Int64) -> (ConversionResult, UInt64)
        """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: UInt64Descriptor, value: UInt64, factor: float) -> (ConversionResult, UInt64) """
        pass

    def TryParse(self, input, *__args):
        """
        TryParse(self: UInt64Descriptor, input: str, format: str, formatProvider: IFormatProvider) -> (bool, UInt64)
        TryParse(self: UInt64Descriptor, input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, UInt64)
        """
        pass

    def Xor(self, left, right):
        """ Xor(self: UInt64Descriptor, left: UInt64, right: UInt64) -> UInt64 """
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

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: UInt64Descriptor) -> UInt64

"""

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: UInt64Descriptor) -> float

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: UInt64Descriptor) -> float

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: UInt64Descriptor) -> float

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: UInt64Descriptor) -> int

"""

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: UInt64Descriptor) -> UInt64

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: UInt64Descriptor) -> UInt64

"""

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: UInt64Descriptor) -> UInt64

"""

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: UInt64Descriptor) -> str

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: UInt64Descriptor) -> UInt64

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: UInt64Descriptor) -> UInt64

"""



