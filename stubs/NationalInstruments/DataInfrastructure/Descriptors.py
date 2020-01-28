# encoding: utf-8
# module NationalInstruments.DataInfrastructure.Descriptors calls itself Descriptors
# from NationalInstruments.Common, Version=19.0.40.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AssemblyDataTypeDescriptorsAttribute(Attribute, _Attribute):
    """
    AssemblyDataTypeDescriptorsAttribute(*implementedDescriptorTypes: Array[Type])
    AssemblyDataTypeDescriptorsAttribute(implementedDescriptorType: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, *implementedDescriptorTypes: Array[Type])
        __new__(cls: type, implementedDescriptorType: Type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DescriptorTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DescriptorTypes(self: AssemblyDataTypeDescriptorsAttribute) -> ReadOnlyCollection[Type]

"""



class ConversionResult(Enum, IComparable, IFormattable, IConvertible):
    """ enum ConversionResult, values: Lossless (0), LossOfIdentity (3), LossOfPrecision (1), LossOfRange (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Lossless = None
    LossOfIdentity = None
    LossOfPrecision = None
    LossOfRange = None
    value__ = None


class DataTypeDescriptorAttribute(Attribute, _Attribute):
    """ DataTypeDescriptorAttribute(descriptorType: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, descriptorType):
        """ __new__(cls: type, descriptorType: Type) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DescriptorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DescriptorType(self: DataTypeDescriptorAttribute) -> Type

"""



class DataTypeDescriptors(object):
    # no doc
    @staticmethod
    def ExamineAssembly(assembly):
        """ ExamineAssembly(assembly: Assembly) -> IEnumerable[Type] """
        pass

    @staticmethod
    def GetConverter():
        """ GetConverter[(TData, TResult)]() -> IOpConversion[TData, TResult] """
        pass

    @staticmethod
    def GetCurrentRegisteredDataTypes():
        """ GetCurrentRegisteredDataTypes() -> Array[Type] """
        pass

    @staticmethod
    def GetDescriptorInstance():
        """ GetDescriptorInstance[T]() -> IDataTypeDescriptor[T] """
        pass

    @staticmethod
    def GetDescriptorType(dataType):
        """ GetDescriptorType(dataType: Type) -> Type """
        pass

    @staticmethod
    def GetLosslessConverter():
        """ GetLosslessConverter[(TData, TResult)]() -> IOpLosslessConversion[TData, TResult] """
        pass

    __all__ = [
        'ExamineAssembly',
        'GetConverter',
        'GetCurrentRegisteredDataTypes',
        'GetDescriptorInstance',
        'GetDescriptorType',
        'GetLosslessConverter',
    ]


class GenericMemberUtility(object):
    # no doc
    @staticmethod
    def CreateMethodMaker(candidates):
        """
        CreateMethodMaker[TResult](*candidates: Array[Expression[Func[TResult]]]) -> IGenericMaker[Func[TResult]]
        CreateMethodMaker[(T1, TResult)](*candidates: Array[Expression[Func[TResult]]]) -> IGenericMaker[Func[T1, TResult]]
        CreateMethodMaker[(T1, T2, TResult)](*candidates: Array[Expression[Func[TResult]]]) -> IGenericMaker[Func[T1, T2, TResult]]
        CreateMethodMaker[(T1, T2, T3, TResult)](*candidates: Array[Expression[Func[TResult]]]) -> IGenericMaker[Func[T1, T2, T3, TResult]]
        CreateMethodMaker[(T1, T2, T3, T4, TResult)](*candidates: Array[Expression[Func[TResult]]]) -> IGenericMaker[Func[T1, T2, T3, T4, TResult]]
        CreateMethodMaker[(T1, T2, T3, T4, T5, TResult)](*candidates: Array[Expression[Func[TResult]]]) -> IGenericMaker[Func[T1, T2, T3, T4, T5, TResult]]
        """
        pass

    @staticmethod
    def CreateTypeMaker(candidates):
        """
        CreateTypeMaker[TResult](*candidates: Array[Type]) -> IGenericMaker[Func[TResult]]
        CreateTypeMaker[(T1, TResult)](*candidates: Array[Type]) -> IGenericMaker[Func[T1, TResult]]
        CreateTypeMaker[(T1, T2, TResult)](*candidates: Array[Type]) -> IGenericMaker[Func[T1, T2, TResult]]
        CreateTypeMaker[(T1, T2, T3, TResult)](*candidates: Array[Type]) -> IGenericMaker[Func[T1, T2, T3, TResult]]
        CreateTypeMaker[(T1, T2, T3, T4, TResult)](*candidates: Array[Type]) -> IGenericMaker[Func[T1, T2, T3, T4, TResult]]
        CreateTypeMaker[(T1, T2, T3, T4, T5, TResult)](*candidates: Array[Type]) -> IGenericMaker[Func[T1, T2, T3, T4, T5, TResult]]
        """
        pass

    @staticmethod
    def GetAssignedTypeArguments(baseType, derivedType):
        """ GetAssignedTypeArguments(baseType: Type, derivedType: Type) -> ReadOnlyCollection[TypeArgumentAssignments] """
        pass

    __all__ = [
        'CreateMethodMaker',
        'CreateTypeMaker',
        'GetAssignedTypeArguments',
    ]


class IDataTypeDescriptor:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IGenericMaker:
    # no doc
    def Cache(self, specialization, expectedTypeArguments):
        """ Cache(self: IGenericMaker[TDelegate], specialization: TDelegate, *expectedTypeArguments: Array[Tuple[Type, Type]]) -> IGenericMaker[TDelegate] """
        pass

    def DisableCaching(self):
        """ DisableCaching(self: IGenericMaker[TDelegate]) -> IGenericMaker[TDelegate] """
        pass

    def Make(self, *__args):
        """
        Make(self: IGenericMaker[TDelegate], knownTypeArgument: Type) -> TDelegate
        Make(self: IGenericMaker[TDelegate], knownTypeArgument1: Type, knownTypeArgument2: Type) -> TDelegate
        Make(self: IGenericMaker[TDelegate], knownTypeArgument1: Type, knownTypeArgument2: Type, knownTypeArgument3: Type) -> TDelegate
        Make(self: IGenericMaker[TDelegate], *knownTypeArguments: Array[Type]) -> TDelegate
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Candidates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Candidates(self: IGenericMaker[TDelegate]) -> ReadOnlyCollection[MemberInfo]

"""

    IsCaching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCaching(self: IGenericMaker[TDelegate]) -> bool

"""



class IOpAddition(IDataTypeDescriptor[TData]):
    # no doc
    def Add(self, value, offset):
        """ Add(self: IOpAddition[TData, TOffset], value: TData, offset: TOffset) -> TData """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpBitwise(IDataTypeDescriptor[TData]):
    # no doc
    def And(self, left, right):
        """ And(self: IOpBitwise[TData], left: TData, right: TData) -> TData """
        pass

    def Not(self, value):
        """ Not(self: IOpBitwise[TData], value: TData) -> TData """
        pass

    def Or(self, left, right):
        """ Or(self: IOpBitwise[TData], left: TData, right: TData) -> TData """
        pass

    def ShiftLeft(self, value, amount):
        """ ShiftLeft(self: IOpBitwise[TData], value: TData, amount: int) -> TData """
        pass

    def ShiftRight(self, value, amount):
        """ ShiftRight(self: IOpBitwise[TData], value: TData, amount: int) -> TData """
        pass

    def Xor(self, left, right):
        """ Xor(self: IOpBitwise[TData], left: TData, right: TData) -> TData """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AllBits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllBits(self: IOpBitwise[TData]) -> TData

"""

    BitCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitCount(self: IOpBitwise[TData]) -> int

"""



class IOpBounded(IDataTypeDescriptor[TData]):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MaxValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxValue(self: IOpBounded[TData]) -> TData

"""

    MinValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinValue(self: IOpBounded[TData]) -> TData

"""



class IOpComparison(IDataTypeDescriptor[TData]):
    # no doc
    def Compare(self, left, right):
        """ Compare(self: IOpComparison[TData], left: TData, right: TData) -> int """
        pass

    def IsDefined(self, value):
        """ IsDefined(self: IOpComparison[TData], value: TData) -> bool """
        pass

    def IsInfinite(self, value):
        """ IsInfinite(self: IOpComparison[TData], value: TData) -> bool """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpContinuous(IDataTypeDescriptor[TData]):
    # no doc
    def Ceiling(self, value):
        """ Ceiling(self: IOpContinuous[TData], value: TData) -> TData """
        pass

    def Floor(self, value):
        """ Floor(self: IOpContinuous[TData], value: TData) -> TData """
        pass

    def Round(self, value, digits=None):
        """
        Round(self: IOpContinuous[TData], value: TData) -> TData
        Round(self: IOpContinuous[TData], value: TData, digits: int) -> TData
        """
        pass

    def Truncate(self, value):
        """ Truncate(self: IOpContinuous[TData], value: TData) -> TData """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MaximumRoundDigits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumRoundDigits(self: IOpContinuous[TData]) -> int

"""



class IOpConversion:
    # no doc
    def TryConvert(self, value, result):
        """ TryConvert(self: IOpConversion[TData, TResult], value: TData) -> (ConversionResult, TResult) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpDigitPosition(IDataTypeDescriptor[TData]):
    # no doc
    def GetLargestFractionalDigitPosition(self, value):
        """ GetLargestFractionalDigitPosition(self: IOpDigitPosition[TData], value: TData) -> int """
        pass

    def GetLargestIntegralDigitPosition(self, value):
        """ GetLargestIntegralDigitPosition(self: IOpDigitPosition[TData], value: TData) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpDivision(IDataTypeDescriptor[TData]):
    # no doc
    def Divide(self, value, factor):
        """ Divide(self: IOpDivision[TData, TFactor], value: TData, factor: TFactor) -> TData """
        pass

    def Remainder(self, value, factor):
        """ Remainder(self: IOpDivision[TData, TFactor], value: TData, factor: TFactor) -> TFactor """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpFormat(IDataTypeDescriptor[TData], IOpConversion[str, TData]):
    # no doc
    def Parse(self, input, format, formatProvider):
        """ Parse(self: IOpFormat[TData], input: str, format: str, formatProvider: IFormatProvider) -> TData """
        pass

    def ToString(self, value, format, formatProvider):
        """ ToString(self: IOpFormat[TData], value: TData, format: str, formatProvider: IFormatProvider) -> str """
        pass

    def TryParse(self, input, format, formatProvider, result):
        """ TryParse(self: IOpFormat[TData], input: str, format: str, formatProvider: IFormatProvider) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    RoundTripFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoundTripFormat(self: IOpFormat[TData]) -> str

"""



class IOpFormatInBase(IOpFormat[TData], IDataTypeDescriptor[TData], IOpConversion[str, TData]):
    # no doc
    def Parse(self, input, fromBase, formatProvider):
        """ Parse(self: IOpFormatInBase[TData], input: str, fromBase: int, formatProvider: IFormatProvider) -> TData """
        pass

    def ToString(self, value, toBase, formatProvider):
        """ ToString(self: IOpFormatInBase[TData], value: TData, toBase: int, formatProvider: IFormatProvider) -> str """
        pass

    def TryParse(self, input, fromBase, formatProvider, result):
        """ TryParse(self: IOpFormatInBase[TData], input: str, fromBase: int, formatProvider: IFormatProvider) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpInfinity(IDataTypeDescriptor[TData]):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Infinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Infinity(self: IOpInfinity[TData]) -> TData

"""



class IOpLosslessConversion(IOpConversion[TData, TResult]):
    # no doc
    def Convert(self, value):
        """ Convert(self: IOpLosslessConversion[TData, TResult], value: TData) -> TResult """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpMultiDimensional(IDataTypeDescriptor[TData]):
    # no doc
    def ComposeValues(self, dimensionValues, composeOption):
        """ ComposeValues(self: IOpMultiDimensional[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> Buffer[TData] """
        pass

    def DecomposeValues(self, values, decomposeOption):
        """ DecomposeValues(self: IOpMultiDimensional[TData], values: Buffer[TData], decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: IOpMultiDimensional[TData]) -> TData """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: IOpMultiDimensional[TData], value: TData, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpMultiplication(IDataTypeDescriptor[TData]):
    # no doc
    def Multiply(self, value, factor):
        """ Multiply(self: IOpMultiplication[TData, TFactor], value: TData, factor: TFactor) -> TData """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass


class IOpMultiSample(IDataTypeDescriptor[TData]):
    # no doc
    def Compose(self, dimensionValues, composeOption):
        """ Compose(self: IOpMultiSample[TData], dimensionValues: IList[IBuffer], composeOption: Trait) -> TData """
        pass

    def Decompose(self, value, decomposeOption):
        """ Decompose(self: IOpMultiSample[TData], value: TData, decomposeOption: Trait) -> IList[IBuffer] """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: IOpMultiSample[TData]) -> TData """
        pass

    def GetDimensionDataTypes(self, value, decomposeOption):
        """ GetDimensionDataTypes(self: IOpMultiSample[TData], value: TData, decomposeOption: Trait) -> ReadOnlyCollection[Type] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpNumeric(IDataTypeDescriptor[TData]):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    One = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: One(self: IOpNumeric[TData]) -> TData

"""

    SmallestPositiveValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallestPositiveValue(self: IOpNumeric[TData]) -> TData

"""

    Zero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Zero(self: IOpNumeric[TData]) -> TData

"""



class IOpObservable(IOpMultiSample[TData], IDataTypeDescriptor[TData]):
    # no doc
    def GetValueObserver(self, value, decomposeOption):
        """ GetValueObserver(self: IOpObservable[TData], value: TData, decomposeOption: Trait) -> IValueObserver[TData] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpPower(IDataTypeDescriptor[TData]):
    # no doc
    def Logarithm(self, logBase, value):
        """ Logarithm(self: IOpPower[TData, TLog], logBase: TLog, value: TData) -> TLog """
        pass

    def Power(self, logBase, power):
        """ Power(self: IOpPower[TData, TLog], logBase: TLog, power: TLog) -> TData """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    Base10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base10(self: IOpPower[TData, TLog]) -> TLog

"""

    Base2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Base2(self: IOpPower[TData, TLog]) -> TLog

"""

    BaseE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseE(self: IOpPower[TData, TLog]) -> TLog

"""



class IOpRatio(IDataTypeDescriptor[TData]):
    # no doc
    def Ratio(self, left, right):
        """ Ratio(self: IOpRatio[TData], left: TData, right: TData) -> float """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IOpScalarMultiplication(IDataTypeDescriptor[TData]):
    # no doc
    def Multiply(self, value, factor):
        """ Multiply(self: IOpScalarMultiplication[TData], value: TData, factor: float) -> TData """
        pass

    def TryMultiply(self, value, factor, product):
        """ TryMultiply(self: IOpScalarMultiplication[TData], value: TData, factor: float) -> (ConversionResult, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass


class IOpSigned(IDataTypeDescriptor[TData]):
    # no doc
    def AbsoluteValue(self, value):
        """ AbsoluteValue(self: IOpSigned[TData], value: TData) -> TData """
        pass

    def Negate(self, value):
        """ Negate(self: IOpSigned[TData], value: TData) -> TData """
        pass

    def Sign(self, value):
        """ Sign(self: IOpSigned[TData], value: TData) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    NegativeOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NegativeOne(self: IOpSigned[TData]) -> TData

"""



class IOpSubtraction(IDataTypeDescriptor[TData]):
    # no doc
    def Difference(self, left, right):
        """ Difference(self: IOpSubtraction[TData, TOffset], left: TData, right: TData) -> TOffset """
        pass

    def Subtract(self, value, offset):
        """ Subtract(self: IOpSubtraction[TData, TOffset], value: TData, offset: TOffset) -> TData """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass


class IValueObserver:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DecomposeOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DecomposeOption(self: IValueObserver[TData]) -> Trait

"""

    ObservedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObservedValue(self: IValueObserver[TData]) -> TData

Set: ObservedValue(self: IValueObserver[TData]) = value
"""


    ObservedValueChanged = None


class ObservedValueChangedEventArgs(EventArgs):
    """ ObservedValueChangedEventArgs(buffers: IList[IBuffer]) """
    def ToString(self):
        """ ToString(self: ObservedValueChangedEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, buffers):
        """ __new__(cls: type, buffers: IList[IBuffer]) """
        pass

    Buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Buffers(self: ObservedValueChangedEventArgs) -> ReadOnlyCollection[IBuffer]

"""


    MetadataChange = None


class TypeArgumentAssignments(object):
    # no doc
    def GetParameterAssignments(self):
        """ GetParameterAssignments(self: TypeArgumentAssignments) -> Array[Type] """
        pass

    def ToString(self):
        """ ToString(self: TypeArgumentAssignments) -> str """
        pass

    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arguments(self: TypeArgumentAssignments) -> ReadOnlyCollection[Type]

"""

    Assignments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Assignments(self: TypeArgumentAssignments) -> ReadOnlyCollection[Type]

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: TypeArgumentAssignments) -> Type

"""

    ClosedBaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClosedBaseType(self: TypeArgumentAssignments) -> Type

"""

    DerivedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DerivedType(self: TypeArgumentAssignments) -> Type

"""



