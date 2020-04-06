# encoding: utf-8
# module NationalInstruments.Restricted calls itself Restricted
# from NationalInstruments.Common, Version=19.0.40.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# functions

def IAnalogWaveformService(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class AssertionConditionAttribute(Attribute, _Attribute):
    """ AssertionConditionAttribute(conditionType: AssertionConditionType) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, conditionType):
        """ __new__(cls: type, conditionType: AssertionConditionType) """
        pass

    ConditionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConditionType(self: AssertionConditionAttribute) -> AssertionConditionType

"""



class AssertionConditionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum AssertionConditionType, values: IS_FALSE (1), IS_NOT_NULL (3), IS_NULL (2), IS_TRUE (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IS_FALSE = None
    IS_NOT_NULL = None
    IS_NULL = None
    IS_TRUE = None
    value__ = None


class AssertionMethodAttribute(Attribute, _Attribute):
    """ AssertionMethodAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class BaseTypeRequiredAttribute(Attribute, _Attribute):
    """ BaseTypeRequiredAttribute(baseType: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, baseType):
        """ __new__(cls: type, baseType: Type) """
        pass

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: BaseTypeRequiredAttribute) -> Type

"""



class LicenseBase(License, IDisposable):
    # no doc
    def ComponentRunTimeCheck(self, *args): #cannot find CLR method
        """ ComponentRunTimeCheck(self: LicenseBase, type: Type, instance: object, licenseString: str) """
        pass

    def DesignTimeCheck(self, type):
        """ DesignTimeCheck(self: LicenseBase, type: Type) -> str """
        pass

    def DesignTimeRegLicense(self):
        """ DesignTimeRegLicense(self: LicenseBase) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: LicenseBase) """
        pass

    def GetUnencryptedLicenseContents(self):
        """ GetUnencryptedLicenseContents(self: LicenseBase) -> str """
        pass

    def IsCallingAssembly(self, *args): #cannot find CLR method
        """ IsCallingAssembly(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsCallingAssemblyUsingAssemblyCompare(self, *args): #cannot find CLR method
        """ IsCallingAssemblyUsingAssemblyCompare(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsCallingAssemblyUsingTypeCompare(self, *args): #cannot find CLR method
        """ IsCallingAssemblyUsingTypeCompare(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsValidLicense(self, cacheLicense=None):
        """
        IsValidLicense(self: LicenseBase) -> bool
        IsValidLicense(self: LicenseBase, cacheLicense: bool) -> bool
        """
        pass

    def IsValidLicenseFile(self, cacheLicense=None):
        """
        IsValidLicenseFile(self: LicenseBase) -> bool
        IsValidLicenseFile(self: LicenseBase, cacheLicense: bool) -> bool
        """
        pass

    def IsValidLMLicense(self, cacheLicense=None):
        """
        IsValidLMLicense(self: LicenseBase) -> bool
        IsValidLMLicense(self: LicenseBase, cacheLicense: bool) -> bool
        """
        pass

    def LoadRunTimeLicense(self):
        """ LoadRunTimeLicense(self: LicenseBase) -> str """
        pass

    def ParseCallStack(self, *args): #cannot find CLR method
        """ ParseCallStack(self: LicenseBase, type: Type) -> Assembly """
        pass

    def ParseCallStackViaAttributeSearch(self, *args): #cannot find CLR method
        """ ParseCallStackViaAttributeSearch(self: LicenseBase, licensedType: Type) -> Assembly """
        pass

    def RunTimeCheck(self, context, type, instance):
        """ RunTimeCheck(self: LicenseBase, context: LicenseContext, type: Type, instance: object) """
        pass

    def ShowUnLicensedBehavior(self, *args): #cannot find CLR method
        """ ShowUnLicensedBehavior(self: LicenseBase, type: Type, instance: object) """
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
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, fileName: str, fullVersion: str)
        __new__(cls: type, featureName: str, majorVersion: int, minorVersion: int, maintVersion: int, debugAllowed: bool)
        """
        pass

    DebugAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DecryptedFileLicenseString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Disposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Disposed(self: LicenseBase) -> bool

"""

    FeatureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FileExists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LicenseKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseKey(self: LicenseBase) -> str

"""

    LicenseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseType(self: LicenseBase) -> str

"""

    MajorMinorAssemblyVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BetaLicense(LicenseBase, IDisposable):
    """
    BetaLicense(betaLicenseRing: Array[str], fileName: str, fullVersion: str, startDate: DateTime, expireDate: DateTime)
    BetaLicense(betaLicenseRing: Array[str], featureName: str, majorVersion: int, minorVersion: int, maintVersion: int, startDate: DateTime, expireDate: DateTime, debugAllowed: bool)
    """
    def ComponentRunTimeCheck(self, *args): #cannot find CLR method
        """ ComponentRunTimeCheck(self: BetaLicense, type: Type, instance: object, licenseString: str) """
        pass

    def Dispose(self):
        """ Dispose(self: LicenseBase, disposing: bool) """
        pass

    def IsCallingAssembly(self, *args): #cannot find CLR method
        """ IsCallingAssembly(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsCallingAssemblyUsingAssemblyCompare(self, *args): #cannot find CLR method
        """ IsCallingAssemblyUsingAssemblyCompare(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsCallingAssemblyUsingTypeCompare(self, *args): #cannot find CLR method
        """ IsCallingAssemblyUsingTypeCompare(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def ParseCallStack(self, *args): #cannot find CLR method
        """ ParseCallStack(self: LicenseBase, type: Type) -> Assembly """
        pass

    def ParseCallStackViaAttributeSearch(self, *args): #cannot find CLR method
        """ ParseCallStackViaAttributeSearch(self: LicenseBase, licensedType: Type) -> Assembly """
        pass

    def ShowUnLicensedBehavior(self, *args): #cannot find CLR method
        """ ShowUnLicensedBehavior(self: LicenseBase, type: Type, instance: object) """
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
    def __new__(self, betaLicenseRing, *__args):
        """
        __new__(cls: type, betaLicenseRing: Array[str], fileName: str, fullVersion: str, startDate: DateTime, expireDate: DateTime)
        __new__(cls: type, betaLicenseRing: Array[str], featureName: str, majorVersion: int, minorVersion: int, maintVersion: int, startDate: DateTime, expireDate: DateTime, debugAllowed: bool)
        """
        pass

    DebugAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DecryptedFileLicenseString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FeatureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FileExists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LicenseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseType(self: BetaLicense) -> str

"""

    MajorMinorAssemblyVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CallbackManager(object, ISupportSynchronizationContext, IDisposable):
    """
    CallbackManager()
    CallbackManager(events: EventHandlerList)
    """
    def AddEventHandler(self, eventKey, value):
        """ AddEventHandler(self: CallbackManager, eventKey: object, value: Delegate) """
        pass

    def Dispose(self):
        """ Dispose(self: CallbackManager) """
        pass

    def GetHandlerCount(self, eventKey):
        """ GetHandlerCount(self: CallbackManager, eventKey: object) -> int """
        pass

    @staticmethod
    def InvokeAsyncCallback(operation, callback, result):
        """ InvokeAsyncCallback(operation: AsyncOperation, callback: AsyncCallback, result: IAsyncResult) """
        pass

    @staticmethod
    def InvokeAsyncCallbackAsync(operation, callback, result):
        """ InvokeAsyncCallbackAsync(operation: AsyncOperation, callback: AsyncCallback, result: IAsyncResult) """
        pass

    def RaiseEvent(self, eventKey, sender, e):
        """ RaiseEvent(self: CallbackManager, eventKey: object, sender: object, e: EventArgs) """
        pass

    def RaiseEventAsync(self, eventKey, sender, e):
        """ RaiseEventAsync(self: CallbackManager, eventKey: object, sender: object, e: EventArgs) """
        pass

    def RaiseEventDirect(self, eventKey, sender, e):
        """ RaiseEventDirect(self: CallbackManager, eventKey: object, sender: object, e: EventArgs) """
        pass

    @staticmethod
    def RaiseGenericEvent(*__args):
        """ RaiseGenericEvent[TEventArgs](operation: AsyncOperation, callback: EventSynchronizationCallback[TEventArgs], e: TEventArgs)RaiseGenericEvent[TEventArgs](self: CallbackManager, eventKey: object, sender: object, e: TEventArgs) """
        pass

    @staticmethod
    def RaiseGenericEventAsync(*__args):
        """ RaiseGenericEventAsync[TEventArgs](operation: AsyncOperation, callback: EventSynchronizationCallback[TEventArgs], e: TEventArgs)RaiseGenericEventAsync[TEventArgs](self: CallbackManager, eventKey: object, sender: object, e: TEventArgs) """
        pass

    def RaiseGenericEventDirect(self, eventKey, sender, e):
        """ RaiseGenericEventDirect[TEventArgs](self: CallbackManager, eventKey: object, sender: object, e: TEventArgs) """
        pass

    def RemoveEventHandler(self, eventKey, value):
        """ RemoveEventHandler(self: CallbackManager, eventKey: object, value: Delegate) """
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
    def __new__(self, events=None):
        """
        __new__(cls: type)
        __new__(cls: type, events: EventHandlerList)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsDiposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDiposed(self: CallbackManager) -> bool

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: CallbackManager) -> bool

"""

    SynchronizeCallbacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SynchronizeCallbacks(self: CallbackManager) -> bool

Set: SynchronizeCallbacks(self: CallbackManager) = value
"""



class CanBeNullAttribute(Attribute, _Attribute):
    """ CanBeNullAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CannotApplyEqualityOperatorAttribute(Attribute, _Attribute):
    """ CannotApplyEqualityOperatorAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Categories(object):
    # no doc
    Accessibility = 'Accessibility'
    Action = 'Action'
    Appearance = 'Appearance'
    Arrow = 'Arrow'
    Behavior = 'Behavior'
    Caption = 'Caption'
    Configurations = 'Configurations'
    Data = 'Data'
    Design = 'Design'
    DragDrop = 'DragDrop'
    Focus = 'Focus'
    Format = 'Format'
    Key = 'Key'
    Layout = 'Layout'
    Misc = 'Misc'
    Mouse = 'Mouse'
    PropertyChanged = 'Property Changed'
    Range = 'Range'
    Shape = 'Shape'
    WindowStyle = 'Window Style'


class CollectionAccessAttribute(Attribute, _Attribute):
    """ CollectionAccessAttribute(collectionAccessType: CollectionAccessType) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, collectionAccessType):
        """ __new__(cls: type, collectionAccessType: CollectionAccessType) """
        pass

    CollectionAccessType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectionAccessType(self: CollectionAccessAttribute) -> CollectionAccessType

"""



class CollectionAccessType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) CollectionAccessType, values: ModifyExistingContent (2), None (0), Read (1), UpdatedContent (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ModifyExistingContent = None
    None = None
    Read = None
    UpdatedContent = None
    value__ = None


class CollectionDebugView(object):
    """ CollectionDebugView(collection: IEnumerable) """
    @staticmethod # known case of __new__
    def __new__(self, collection):
        """ __new__(cls: type, collection: IEnumerable) """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: CollectionDebugView) -> Array

"""



class CommonExtensions(object):
    # no doc
    @staticmethod
    def FormatWithCurrentCulture(format, args):
        """ FormatWithCurrentCulture(format: str, *args: Array[object]) -> str """
        pass

    @staticmethod
    def GetCustomAttributes(*__args):
        """
        GetCustomAttributes[TAttribute](member: MemberInfo, inherit: bool) -> Array[TAttribute]
        GetCustomAttributes[TAttribute](assembly: Assembly) -> Array[TAttribute]
        """
        pass

    @staticmethod
    def GetDisplayName(type):
        """ GetDisplayName(type: Type) -> str """
        pass

    @staticmethod
    def GetService(serviceProvider):
        """ GetService[TService](serviceProvider: IServiceProvider) -> TService """
        pass

    @staticmethod
    def GetValueOrDefault(item, operation, defaultValue=None):
        """
        GetValueOrDefault[(TItem, TResult)](item: TItem, operation: Func[TItem, TResult]) -> TResult
        GetValueOrDefault[(TItem, TResult)](item: TItem, operation: Func[TItem, TResult], defaultValue: TResult) -> TResult
        """
        pass

    @staticmethod
    def IfNotNull(item, action):
        """ IfNotNull[T](item: T, action: Action[T]) """
        pass

    @staticmethod
    def Is(item):
        """ Is[T](item: object) -> bool """
        pass

    @staticmethod
    def IsAssignableTo(type, desired=None):
        """
        IsAssignableTo[T](type: Type) -> bool
        IsAssignableTo(type: Type, desired: Type) -> bool
        """
        pass

    @staticmethod
    def IsNegativeZero(value):
        """
        IsNegativeZero(value: float) -> bool
        IsNegativeZero(value: Single) -> bool
        """
        pass

    @staticmethod
    def IsSpecialValue(value):
        """
        IsSpecialValue(value: float) -> bool
        IsSpecialValue(value: Single) -> bool
        """
        pass

    @staticmethod
    def OrdinalEndsWith(value, end, ignoreCase):
        """ OrdinalEndsWith(value: str, end: str, ignoreCase: bool) -> bool """
        pass

    @staticmethod
    def OrdinalEqual(value, comparand, ignoreCase=None):
        """
        OrdinalEqual(value: str, comparand: str) -> bool
        OrdinalEqual(value: str, comparand: str, ignoreCase: bool) -> bool
        """
        pass

    @staticmethod
    def OrdinalIndexOf(value, comparand, ignoreCase):
        """ OrdinalIndexOf(value: str, comparand: str, ignoreCase: bool) -> Nullable[int] """
        pass

    @staticmethod
    def OrdinalLastIndexOf(value, comparand, ignoreCase):
        """ OrdinalLastIndexOf(value: str, comparand: str, ignoreCase: bool) -> Nullable[int] """
        pass

    @staticmethod
    def OrdinalStartsWith(value, start, ignoreCase):
        """ OrdinalStartsWith(value: str, start: str, ignoreCase: bool) -> bool """
        pass

    @staticmethod
    def TryGetValue(item, value):
        """ TryGetValue[T](item: Nullable[T]) -> (bool, T) """
        pass

    @staticmethod
    def TryProvideService(serviceType, candidate):
        """ TryProvideService(serviceType: Type, candidate: object) -> object """
        pass

    __all__ = [
        'FormatWithCurrentCulture',
        'GetCustomAttributes',
        'GetDisplayName',
        'GetService',
        'GetValueOrDefault',
        'IfNotNull',
        'Is',
        'IsAssignableTo',
        'IsNegativeZero',
        'IsSpecialValue',
        'OrdinalEndsWith',
        'OrdinalEqual',
        'OrdinalIndexOf',
        'OrdinalLastIndexOf',
        'OrdinalStartsWith',
        'TryGetValue',
        'TryProvideService',
    ]


class ComplexParser(object):
    # no doc
    @staticmethod
    def AttemptParse(input, numberStyle, provider, tryParse, real, imaginary):
        """ AttemptParse[T](input: str, numberStyle: NumberStyles, provider: IFormatProvider, tryParse: TryParse[T]) -> (bool, T, T) """
        pass

    @staticmethod
    def GetNumberFormat(provider):
        """ GetNumberFormat(provider: IFormatProvider) -> NumberFormatInfo """
        pass

    def TryParseDouble(self, *args): #cannot find CLR method
        """ TryParse[float](object: object, method: IntPtr) """
        pass

    def TryParseSingle(self, *args): #cannot find CLR method
        """ TryParse[Single](object: object, method: IntPtr) """
        pass

    FloatNumberStyle = None
    IntegerNumberStyle = None
    TryParse`1 = None
    __all__ = [
        'AttemptParse',
        'FloatNumberStyle',
        'GetNumberFormat',
        'IntegerNumberStyle',
        'TryParse`1',
        'TryParseDouble',
        'TryParseSingle',
    ]


class ContractAnnotationAttribute(Attribute, _Attribute):
    """
    ContractAnnotationAttribute(contract: str)
    ContractAnnotationAttribute(contract: str, forceFullStates: bool)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, contract, forceFullStates=None):
        """
        __new__(cls: type, contract: str)
        __new__(cls: type, contract: str, forceFullStates: bool)
        """
        pass

    Contract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contract(self: ContractAnnotationAttribute) -> str

"""

    ForceFullStates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceFullStates(self: ContractAnnotationAttribute) -> bool

"""



class DigitalChangeType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) DigitalChangeType, values: All (7), Data (1), Label (4), Timing (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    All = None
    Data = None
    Label = None
    Timing = None
    value__ = None


class DigitalWaveformChangedEventArgs(EventArgs):
    """
    DigitalWaveformChangedEventArgs(waveform: DigitalWaveform, changeType: DigitalChangeType)
    DigitalWaveformChangedEventArgs(waveform: DigitalWaveform, sampleIndex: int, signalIndex: int, changeType: DigitalChangeType)
    """
    @staticmethod # known case of __new__
    def __new__(self, waveform, *__args):
        """
        __new__(cls: type, waveform: DigitalWaveform, changeType: DigitalChangeType)
        __new__(cls: type, waveform: DigitalWaveform, sampleIndex: int, signalIndex: int, changeType: DigitalChangeType)
        """
        pass

    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: DigitalWaveformChangedEventArgs) -> DigitalChangeType

"""

    SampleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleIndex(self: DigitalWaveformChangedEventArgs) -> int

"""

    SignalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SignalIndex(self: DigitalWaveformChangedEventArgs) -> int

"""

    Waveform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Waveform(self: DigitalWaveformChangedEventArgs) -> DigitalWaveform

"""



class DigitalWaveformChangedEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ DigitalWaveformChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: DigitalWaveformChangedEventHandler, sender: object, e: DigitalWaveformChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: DigitalWaveformChangedEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DigitalWaveformChangedEventHandler, sender: object, e: DigitalWaveformChangedEventArgs) """
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


class EnumerableDebugView(object):
    """ EnumerableDebugView(collection: IEnumerable) """
    @staticmethod # known case of __new__
    def __new__(self, collection):
        """ __new__(cls: type, collection: IEnumerable) """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: EnumerableDebugView) -> Array

"""



class EnumerableExtensions(object):
    # no doc
    @staticmethod
    def AddRange(collection, items):
        """ AddRange[T](collection: ICollection[T], items: IEnumerable[T]) """
        pass

    @staticmethod
    def DisposeAll(collection):
        """ DisposeAll[T](collection: IEnumerable[T]) """
        pass

    @staticmethod
    def EmptyArray():
        """ EmptyArray[T]() -> Array[T] """
        pass

    @staticmethod
    def ForEach(collection, action):
        """ ForEach[T](collection: IEnumerable[T], action: Action[T])ForEach[T](collection: IEnumerable, action: Action[T])ForEach(collection: IEnumerable, action: Action[object]) """
        pass

    @staticmethod
    def Generate(initial, iterate, condition):
        """ Generate[T](initial: T, iterate: Func[T, T], condition: Func[T, bool]) -> IEnumerable[T] """
        pass

    @staticmethod
    def GenerateUntilNull(initial, iterate):
        """ GenerateUntilNull[T](initial: T, iterate: Func[T, T]) -> IEnumerable[T] """
        pass

    @staticmethod
    def GetNextIndexValue(indices, index, minimumIndex):
        """ GetNextIndexValue(indices: IList[int], index: int, minimumIndex: int) -> (int, int) """
        pass

    @staticmethod
    def IndexOf(collection, *__args):
        """
        IndexOf[T](collection: IEnumerable[T], condition: Func[T, bool]) -> int
        IndexOf[T](collection: IEnumerable[T], value: T) -> int
        IndexOf(collection: IEnumerable, condition: Func[object, bool]) -> int
        IndexOf(collection: IEnumerable, value: object) -> int
        """
        pass

    @staticmethod
    def IsEmpty(*__args):
        """
        IsEmpty[T](array: Array[T]) -> bool
        IsEmpty[T](collection: IEnumerable[T]) -> bool
        IsEmpty(collection: IEnumerable) -> bool
        """
        pass

    @staticmethod
    def MakeEnumerable(item):
        """ MakeEnumerable[T](item: T) -> IEnumerable[T] """
        pass

    @staticmethod
    def RemoveRange(list, index, count):
        """ RemoveRange(list: IList, index: int, count: int) """
        pass

    @staticmethod
    def SafeAsList(collection):
        """ SafeAsList[T](collection: IEnumerable[T]) -> IList[T] """
        pass

    @staticmethod
    def SafeForEach(collection, action):
        """ SafeForEach[T](collection: IEnumerable[T], action: Action[T])SafeForEach[T](collection: IEnumerable, action: Action[T])SafeForEach(collection: IEnumerable, action: Action[object]) """
        pass

    @staticmethod
    def ToReadOnlyCollection(list):
        """ ToReadOnlyCollection[T](list: IList[T]) -> ReadOnlyCollection[T] """
        pass

    @staticmethod
    def TryGetItem(list, index, value):
        """ TryGetItem[T](list: IList[T], index: int) -> (bool, T) """
        pass

    @staticmethod
    def UpdateItem(list, index, newItem):
        """ UpdateItem[T](list: IList[T], index: int, newItem: T) """
        pass

    @staticmethod
    def WhereNotNull(collection):
        """ WhereNotNull[T](collection: IEnumerable[T]) -> IEnumerable[T] """
        pass

    @staticmethod
    def WrapEnumerable(collection):
        """ WrapEnumerable[T](collection: IEnumerable[T]) -> IEnumerable[T] """
        pass

    __all__ = [
        'AddRange',
        'DisposeAll',
        'EmptyArray',
        'ForEach',
        'Generate',
        'GenerateUntilNull',
        'GetNextIndexValue',
        'IndexOf',
        'IsEmpty',
        'MakeEnumerable',
        'RemoveRange',
        'SafeAsList',
        'SafeForEach',
        'ToReadOnlyCollection',
        'TryGetItem',
        'UpdateItem',
        'WhereNotNull',
        'WrapEnumerable',
    ]


class EnumUtility(object):
    # no doc
    @staticmethod
    def GetValues():
        """ GetValues[TEnum]() -> Array[TEnum] """
        pass

    @staticmethod
    def IsDefined(value):
        """ IsDefined(value: Enum) -> bool """
        pass

    @staticmethod
    def IsExplicitlyDefined(value):
        """ IsExplicitlyDefined(value: Enum) -> bool """
        pass

    @staticmethod
    def Parse(value, ignoreCase):
        """ Parse[TEnum](value: str, ignoreCase: bool) -> TEnum """
        pass

    __all__ = [
        'GetValues',
        'IsDefined',
        'IsExplicitlyDefined',
        'Parse',
    ]


class EvalReleaseLicense(LicenseBase, IDisposable):
    """
    EvalReleaseLicense(releaseLicenseRing: Array[str], evalLicenseRing: Array[str], fileName: str, fullVersion: str)
    EvalReleaseLicense(releaseLicenseRing: Array[str], evalLicenseRing: Array[str], featureName: str, majorVersion: int, minorVersion: int, maintVersion: int, debugAllowed: bool)
    """
    def ComponentRunTimeCheck(self, *args): #cannot find CLR method
        """ ComponentRunTimeCheck(self: EvalReleaseLicense, type: Type, instance: object, licenseString: str) """
        pass

    def Dispose(self):
        """ Dispose(self: LicenseBase, disposing: bool) """
        pass

    def IsCallingAssembly(self, *args): #cannot find CLR method
        """ IsCallingAssembly(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsCallingAssemblyUsingAssemblyCompare(self, *args): #cannot find CLR method
        """ IsCallingAssemblyUsingAssemblyCompare(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def IsCallingAssemblyUsingTypeCompare(self, *args): #cannot find CLR method
        """ IsCallingAssemblyUsingTypeCompare(self: LicenseBase, currentType: Type, nextType: Type, licensedType: Type) -> bool """
        pass

    def ParseCallStack(self, *args): #cannot find CLR method
        """ ParseCallStack(self: LicenseBase, type: Type) -> Assembly """
        pass

    def ParseCallStackViaAttributeSearch(self, *args): #cannot find CLR method
        """ ParseCallStackViaAttributeSearch(self: LicenseBase, licensedType: Type) -> Assembly """
        pass

    def ShowEvalBehavior(self, *args): #cannot find CLR method
        """ ShowEvalBehavior(self: EvalReleaseLicense, type: Type, instance: object, licenseString: str) """
        pass

    def ShowUnLicensedBehavior(self, *args): #cannot find CLR method
        """ ShowUnLicensedBehavior(self: LicenseBase, type: Type, instance: object) """
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
    def __new__(self, releaseLicenseRing, evalLicenseRing, *__args):
        """
        __new__(cls: type, releaseLicenseRing: Array[str], evalLicenseRing: Array[str], fileName: str, fullVersion: str)
        __new__(cls: type, releaseLicenseRing: Array[str], evalLicenseRing: Array[str], featureName: str, majorVersion: int, minorVersion: int, maintVersion: int, debugAllowed: bool)
        """
        pass

    DebugAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DecryptedFileLicenseString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FeatureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FileExists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LicenseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseType(self: EvalReleaseLicense) -> str

"""

    MajorMinorAssemblyVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ExceptionBuilderBase(object):
    # no doc
    @staticmethod
    def ArgumentNull(argumentName, message=None):
        """
        ArgumentNull(argumentName: str) -> Exception
        ArgumentNull(argumentName: str, message: str) -> Exception
        """
        pass

    @staticmethod
    def ArgumentOutOfRange(argumentName, message=None):
        """
        ArgumentOutOfRange(argumentName: str, message: str) -> Exception
        ArgumentOutOfRange(argumentName: str) -> Exception
        """
        pass

    @staticmethod
    def ArgumentOutOfRangeInfinity(argumentName):
        """ ArgumentOutOfRangeInfinity(argumentName: str) -> Exception """
        pass

    @staticmethod
    def ArgumentOutOfRangeNaN(argumentName):
        """ ArgumentOutOfRangeNaN(argumentName: str) -> Exception """
        pass

    @staticmethod
    def ArgumentOutOfRangeNaNOrInfinity(argumentName):
        """ ArgumentOutOfRangeNaNOrInfinity(argumentName: str) -> Exception """
        pass

    @staticmethod
    def DllNotFound(message):
        """ DllNotFound(message: str) -> Exception """
        pass

    @staticmethod
    def EmptyString(argumentName):
        """ EmptyString(argumentName: str) -> Exception """
        pass

    @staticmethod
    def EntryPointNotFound(message):
        """ EntryPointNotFound(message: str) -> Exception """
        pass

    @staticmethod
    def Format(message=None, innerException=None):
        """
        Format() -> Exception
        Format(message: str) -> Exception
        Format(message: str, innerException: Exception) -> Exception
        """
        pass

    @staticmethod
    def IndexOutOfRange(message=None):
        """
        IndexOutOfRange() -> Exception
        IndexOutOfRange(message: str) -> Exception
        """
        pass

    @staticmethod
    def InvalidArgument(*__args):
        """
        InvalidArgument(argumentName: str, message: str, innerException: Exception) -> Exception
        InvalidArgument(argumentName: str, message: str) -> Exception
        InvalidArgument(message: str) -> Exception
        """
        pass

    @staticmethod
    def InvalidCast(argumentName, typeToCastFrom, typeToCastTo):
        """ InvalidCast(argumentName: str, typeToCastFrom: Type, typeToCastTo: Type) -> Exception """
        pass

    @staticmethod
    def InvalidEnumArgument(argumentName, invalidValue, enumType):
        """ InvalidEnumArgument(argumentName: str, invalidValue: int, enumType: Type) -> Exception """
        pass

    @staticmethod
    def InvalidOperation(message=None, innerException=None):
        """
        InvalidOperation(message: str, innerException: Exception) -> Exception
        InvalidOperation(message: str) -> Exception
        InvalidOperation() -> Exception
        """
        pass

    @staticmethod
    def LicenseException(type, instance, message):
        """ LicenseException(type: Type, instance: object, message: str) -> Exception """
        pass

    @staticmethod
    def NotFiniteNumber(message, offendingNumber):
        """ NotFiniteNumber(message: str, offendingNumber: float) -> Exception """
        pass

    @staticmethod
    def NotImplemented(message=None):
        """
        NotImplemented() -> Exception
        NotImplemented(message: str) -> Exception
        """
        pass

    @staticmethod
    def NotSupported(message=None):
        """
        NotSupported(message: str) -> Exception
        NotSupported() -> Exception
        """
        pass

    @staticmethod
    def ObjectDisposed(*__args):
        """
        ObjectDisposed(typeName: str) -> Exception
        ObjectDisposed(obj: object) -> Exception
        """
        pass

    @staticmethod
    def Serialization(message=None):
        """
        Serialization() -> Exception
        Serialization(message: str) -> Exception
        """
        pass

    def Trace(self, *args): #cannot find CLR method
        """ Trace(e: Exception) -> Exception """
        pass

    @staticmethod
    def TypedCollectionDoesNotSupportType(collectionType, invalidObject):
        """ TypedCollectionDoesNotSupportType(collectionType: Type, invalidObject: object) -> Exception """
        pass

    StackFramesToSkip = 2


class ExtendedPropertyKeys(object):
    # no doc
    ChannelName = 'NI_ChannelName'
    SignalNames = 'NI_LineNames'
    UnitDescription = 'NI_UnitDescription'
    __all__ = [
        'ChannelName',
        'SignalNames',
        'UnitDescription',
    ]


class Guard(object):
    """ Guard[T](isParam: bool, value: T, name: str) """
    def Is(self):
        """ Is[TTarget](self: Guard[T]) -> Guard[TTarget] """
        pass

    def Satisfies(self, condition, *__args):
        """
        Satisfies(self: Guard[T], condition: bool, exceptionCreator: Func[object, str, str, Exception], format: str, *args: Array[object]) -> Guard[T]
        Satisfies(self: Guard[T], condition: bool, format: str, *args: Array[object]) -> Guard[T]
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isParam, value, name):
        """
        __new__[Guard`1]() -> Guard[T]
        
        __new__(cls: type, isParam: bool, value: T, name: str)
        """
        pass

    IsParam = None
    Name = None
    Value = None


class GuardExceptions(object):
    # no doc
    def CreateArgumentException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def CreateArgumentNullException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def CreateArgumentOutOfRangeException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def CreateFormatException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def CreateInvalidEnumArgumentException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def CreateInvalidOperationException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def CreateObjectDisposedException(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def DefaultParamExceptionCreator(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    def DefaultValueExceptionCreator(self, *args): #cannot find CLR method
        """ Func[object, str, str, Exception](object: object, method: IntPtr) """
        pass

    BlankMessage = ' '
    __all__ = [
        'BlankMessage',
        'CreateArgumentException',
        'CreateArgumentNullException',
        'CreateArgumentOutOfRangeException',
        'CreateFormatException',
        'CreateInvalidEnumArgumentException',
        'CreateInvalidOperationException',
        'CreateObjectDisposedException',
        'DefaultParamExceptionCreator',
        'DefaultValueExceptionCreator',
    ]


class IAnalogWaveformCollectionService:
    # no doc
    def GetData(self):
        """ GetData(self: IAnalogWaveformCollectionService[TData]) -> Array[TData] """
        pass

    def LoadData(self, data, channelCount, recordCount, *__args):
        """ LoadData(self: IAnalogWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, sampleCount: int)LoadData(self: IAnalogWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, indexes: Array[int], lengths: Array[int]) """
        pass

    def LoadDataNoChangedEvent(self, data, channelCount, recordCount, *__args):
        """ LoadDataNoChangedEvent(self: IAnalogWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, sampleCount: int)LoadDataNoChangedEvent(self: IAnalogWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, indexes: Array[int], length: Array[int]) """
        pass

    def OnChanged(self, changeType):
        """ OnChanged(self: IAnalogWaveformCollectionService[TData], changeType: WaveformChangeType) """
        pass

    def SetTimingNoChangedEvent(self, timings):
        """ SetTimingNoChangedEvent(self: IAnalogWaveformCollectionService[TData], timings: Array[WaveformTiming])SetTimingNoChangedEvent(self: IAnalogWaveformCollectionService[TData], timings: Array[PrecisionWaveformTiming]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IAnalogWaveformService2:
    # no doc
    def GetBuffer(self):
        """ GetBuffer(self: IAnalogWaveformService2[TData]) -> ArraySegment[TData] """
        pass

    def InvalidateData(self):
        """ InvalidateData(self: IAnalogWaveformService2[TData]) """
        pass

    def LoadData(self, data, sampleIndex=None, sampleCount=None):
        """ LoadData(self: IAnalogWaveformService2[TData], data: Array[TData])LoadData(self: IAnalogWaveformService2[TData], data: Array[TData], sampleIndex: int, sampleCount: int) """
        pass

    def LoadDataNoChangedEvent(self, data, sampleIndex=None, sampleCount=None):
        """ LoadDataNoChangedEvent(self: IAnalogWaveformService2[TData], data: Array[TData])LoadDataNoChangedEvent(self: IAnalogWaveformService2[TData], data: Array[TData], sampleIndex: int, sampleCount: int) """
        pass

    def OnChanged(self, *__args):
        """ OnChanged(self: IAnalogWaveformService2[TData], sampleIndex: int, sampleCount: int, changeType: WaveformChangeType)OnChanged(self: IAnalogWaveformService2[TData], e: WaveformChangedEventArgs[TData]) """
        pass

    def RequestBuffer(self, requestedSize):
        """ RequestBuffer(self: IAnalogWaveformService2[TData], requestedSize: int) -> ArraySegment[TData] """
        pass

    def SetTimingNoChangedEvent(self, timing):
        """ SetTimingNoChangedEvent(self: IAnalogWaveformService2[TData], timing: WaveformTiming)SetTimingNoChangedEvent(self: IAnalogWaveformService2[TData], timing: PrecisionWaveformTiming) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: IAnalogWaveformService2[TData]) -> int

"""


    Changed = None


class IComplexWaveformCollectionService:
    # no doc
    def GetData(self):
        """ GetData(self: IComplexWaveformCollectionService[TData]) -> Array[TData] """
        pass

    def LoadData(self, data, channelCount, recordCount, *__args):
        """ LoadData(self: IComplexWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, sampleCount: int)LoadData(self: IComplexWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, indexes: Array[int], lengths: Array[int]) """
        pass

    def LoadDataNoChangedEvent(self, data, channelCount, recordCount, *__args):
        """ LoadDataNoChangedEvent(self: IComplexWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, sampleCount: int)LoadDataNoChangedEvent(self: IComplexWaveformCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, indexes: Array[int], length: Array[int]) """
        pass

    def OnChanged(self, changeType):
        """ OnChanged(self: IComplexWaveformCollectionService[TData], changeType: WaveformChangeType) """
        pass

    def SetTimingNoChangedEvent(self, timings):
        """ SetTimingNoChangedEvent(self: IComplexWaveformCollectionService[TData], timings: Array[PrecisionWaveformTiming]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IComplexWaveformService:
    # no doc
    def LoadData(self, data, sampleIndex=None, sampleCount=None):
        """ LoadData(self: IComplexWaveformService[TData], data: TData)LoadData(self: IComplexWaveformService[TData], data: TData, sampleIndex: int, sampleCount: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IComplexWaveformService2:
    # no doc
    def GetBuffer(self):
        """ GetBuffer(self: IComplexWaveformService2[TData]) -> ArraySegment[TData] """
        pass

    def InvalidateData(self):
        """ InvalidateData(self: IComplexWaveformService2[TData]) """
        pass

    def LoadData(self, data, sampleIndex=None, sampleCount=None):
        """ LoadData(self: IComplexWaveformService2[TData], data: Array[TData])LoadData(self: IComplexWaveformService2[TData], data: Array[TData], sampleIndex: int, sampleCount: int) """
        pass

    def LoadDataNoChangedEvent(self, data, sampleIndex=None, sampleCount=None):
        """ LoadDataNoChangedEvent(self: IComplexWaveformService2[TData], data: Array[TData])LoadDataNoChangedEvent(self: IComplexWaveformService2[TData], data: Array[TData], sampleIndex: int, sampleCount: int) """
        pass

    def OnChanged(self, *__args):
        """ OnChanged(self: IComplexWaveformService2[TData], sampleIndex: int, sampleCount: int, changeType: WaveformChangeType)OnChanged(self: IComplexWaveformService2[TData], e: WaveformChangedEventArgs[TData]) """
        pass

    def RequestBuffer(self, requestedSize):
        """ RequestBuffer(self: IComplexWaveformService2[TData], requestedSize: int) -> ArraySegment[TData] """
        pass

    def SetTimingNoChangedEvent(self, timing):
        """ SetTimingNoChangedEvent(self: IComplexWaveformService2[TData], timing: PrecisionWaveformTiming) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: IComplexWaveformService2[TData]) -> int

"""


    Changed = None


class IConvertibleType:
    # no doc
    def CanConvertTo(self, targetType):
        """ CanConvertTo(self: IConvertibleType, targetType: Type) -> bool """
        pass

    def ConvertTo(self, targetType):
        """ ConvertTo(self: IConvertibleType, targetType: Type) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDigitalWaveformService:
    # no doc
    def GetData(self):
        """ GetData(self: IDigitalWaveformService) -> Array[DigitalState] """
        pass

    def InvalidateData(self):
        """ InvalidateData(self: IDigitalWaveformService) """
        pass

    def LoadData(self, data):
        """ LoadData(self: IDigitalWaveformService, data: Array[DigitalState]) """
        pass

    def LoadDataNoChangedEvent(self, data):
        """ LoadDataNoChangedEvent(self: IDigitalWaveformService, data: Array[DigitalState]) """
        pass

    def OnChanged(self, e):
        """ OnChanged(self: IDigitalWaveformService, e: DigitalWaveformChangedEventArgs) """
        pass

    def SetTimingNoChangedEvent(self, timing):
        """ SetTimingNoChangedEvent(self: IDigitalWaveformService, timing: WaveformTiming)SetTimingNoChangedEvent(self: IDigitalWaveformService, timing: PrecisionWaveformTiming) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Changed = None


class ImplicitRefreshItem(object):
    # no doc
    def Refresh(self):
        """ Refresh(self: ImplicitRefreshItem) """
        pass


class ImplicitUseKindFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ImplicitUseKindFlags, values: Access (1), Assign (2), Default (7), InstantiatedNoFixedConstructorSignature (8), InstantiatedWithFixedConstructorSignature (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Access = None
    Assign = None
    Default = None
    InstantiatedNoFixedConstructorSignature = None
    InstantiatedWithFixedConstructorSignature = None
    value__ = None


class ImplicitUseTargetFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ImplicitUseTargetFlags, values: Default (1), Itself (1), Members (2), WithMembers (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Default = None
    Itself = None
    Members = None
    value__ = None
    WithMembers = None


class InstantHandleAttribute(Attribute, _Attribute):
    """ InstantHandleAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InvokerParameterNameAttribute(Attribute, _Attribute):
    """ InvokerParameterNameAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IPrecisionDateTimeService:
    # no doc
    def GetFractionalSecondTicksByEpoch(self, epoch):
        """ GetFractionalSecondTicksByEpoch(self: IPrecisionDateTimeService, epoch: PrecisionDateTimeEpoch) -> UInt64 """
        pass

    def GetWholeSecondsByEpoch(self, epoch):
        """ GetWholeSecondsByEpoch(self: IPrecisionDateTimeService, epoch: PrecisionDateTimeEpoch) -> Int64 """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IProxyLicenser:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    LicenseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseType(self: IProxyLicenser) -> Type

"""



class ISpectrumCollectionService:
    # no doc
    def GetData(self):
        """ GetData(self: ISpectrumCollectionService[TData]) -> Array[TData] """
        pass

    def LoadData(self, data, channelCount, recordCount, *__args):
        """ LoadData(self: ISpectrumCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, sampleCount: int)LoadData(self: ISpectrumCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, indexes: Array[int], lengths: Array[int]) """
        pass

    def LoadDataNoChangedEvent(self, data, channelCount, recordCount, *__args):
        """ LoadDataNoChangedEvent(self: ISpectrumCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, sampleCount: int)LoadDataNoChangedEvent(self: ISpectrumCollectionService[TData], data: Array[TData], channelCount: int, recordCount: int, indexes: Array[int], length: Array[int]) """
        pass

    def OnChanged(self, changeType):
        """ OnChanged(self: ISpectrumCollectionService[TData], changeType: SpectrumChangeType) """
        pass

    def SetFrequencyIncrementNoChangedEvent(self, frequencyIncrement):
        """ SetFrequencyIncrementNoChangedEvent(self: ISpectrumCollectionService[TData], frequencyIncrement: Array[float]) """
        pass

    def SetStartFrequencyNoChangedEvent(self, startFrequency):
        """ SetStartFrequencyNoChangedEvent(self: ISpectrumCollectionService[TData], startFrequency: Array[float]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISpectrumService:
    # no doc
    def GetBuffer(self):
        """ GetBuffer(self: ISpectrumService[TData]) -> ArraySegment[TData] """
        pass

    def InvalidateData(self):
        """ InvalidateData(self: ISpectrumService[TData]) """
        pass

    def LoadData(self, data, sampleIndex=None, sampleCount=None):
        """ LoadData(self: ISpectrumService[TData], data: Array[TData])LoadData(self: ISpectrumService[TData], data: Array[TData], sampleIndex: int, sampleCount: int) """
        pass

    def LoadDataNoChangedEvent(self, data, sampleIndex=None, sampleCount=None):
        """ LoadDataNoChangedEvent(self: ISpectrumService[TData], data: Array[TData])LoadDataNoChangedEvent(self: ISpectrumService[TData], data: Array[TData], sampleIndex: int, sampleCount: int) """
        pass

    def OnChanged(self, *__args):
        """ OnChanged(self: ISpectrumService[TData], sampleIndex: int, sampleCount: int, changeType: SpectrumChangeType)OnChanged(self: ISpectrumService[TData], e: SpectrumChangedEventArgs[TData]) """
        pass

    def RequestBuffer(self, requestedSize):
        """ RequestBuffer(self: ISpectrumService[TData], requestedSize: int) -> ArraySegment[TData] """
        pass

    def SetFrequencyIncrementNoChangedEvent(self, frequencyIncrement):
        """ SetFrequencyIncrementNoChangedEvent(self: ISpectrumService[TData], frequencyIncrement: float) """
        pass

    def SetStartFrequencyNoChangedEvent(self, startFrequency):
        """ SetStartFrequencyNoChangedEvent(self: ISpectrumService[TData], startFrequency: float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Capacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Capacity(self: ISpectrumService[TData]) -> int

"""


    Changed = None


class ItemCanBeNullAttribute(Attribute, _Attribute):
    """ ItemCanBeNullAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ItemNotNullAttribute(Attribute, _Attribute):
    """ ItemNotNullAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LazyLocalMap(object):
    """
    LazyLocalMap[TKey, TValue](initialize: Func[TKey, TValue], comparer: IEqualityComparer[TKey])
    LazyLocalMap[TKey, TValue](initialize: Func[TKey, TValue])
    LazyLocalMap[TKey, TValue]()
    """
    def Clear(self):
        """ Clear(self: LazyLocalMap[TKey, TValue]) """
        pass

    def CurrentlyContainsKey(self, key):
        """ CurrentlyContainsKey(self: LazyLocalMap[TKey, TValue], key: TKey) -> bool """
        pass

    def GetOrAdd(self, key, valueFactory):
        """ GetOrAdd(self: LazyLocalMap[TKey, TValue], key: TKey, valueFactory: Func[TKey, TValue]) -> TValue """
        pass

    def ToString(self):
        """ ToString(self: LazyLocalMap[TKey, TValue]) -> str """
        pass

    def TryGetCurrent(self, key, value):
        """ TryGetCurrent(self: LazyLocalMap[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def TryRemoveCurrent(self, key, value):
        """ TryRemoveCurrent(self: LazyLocalMap[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initialize=None, comparer=None):
        """
        __new__(cls: type, initialize: Func[TKey, TValue], comparer: IEqualityComparer[TKey])
        __new__(cls: type, initialize: Func[TKey, TValue])
        __new__(cls: type)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    CurrentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCount(self: LazyLocalMap[TKey, TValue]) -> int

"""

    CurrentItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentItems(self: LazyLocalMap[TKey, TValue]) -> IEnumerable[KeyValuePair[TKey, TValue]]

"""

    CurrentKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentKeys(self: LazyLocalMap[TKey, TValue]) -> ICollection[TKey]

"""

    CurrentValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValues(self: LazyLocalMap[TKey, TValue]) -> ICollection[TValue]

"""

    KeyFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyFilter(self: LazyLocalMap[TKey, TValue]) -> Func[TKey, bool]

Set: KeyFilter(self: LazyLocalMap[TKey, TValue]) = value
"""



class LazyMap(object):
    """
    LazyMap[TKey, TValue](initialize: Func[TKey, TValue], enableCaching: bool, comparer: IEqualityComparer[TKey])
    LazyMap[TKey, TValue](initialize: Func[TKey, TValue], enableCaching: bool)
    LazyMap[TKey, TValue](initialize: Func[TKey, TValue], comparer: IEqualityComparer[TKey])
    LazyMap[TKey, TValue](initialize: Func[TKey, TValue])
    LazyMap[TKey, TValue]()
    """
    def Clear(self):
        """ Clear(self: LazyMap[TKey, TValue]) """
        pass

    def CurrentlyContainsKey(self, key):
        """ CurrentlyContainsKey(self: LazyMap[TKey, TValue], key: TKey) -> bool """
        pass

    def DisableCaching(self):
        """ DisableCaching(self: LazyMap[TKey, TValue]) """
        pass

    def GetOrAdd(self, key, valueFactory):
        """ GetOrAdd(self: LazyMap[TKey, TValue], key: TKey, valueFactory: Func[TKey, TValue]) -> TValue """
        pass

    def ToString(self):
        """ ToString(self: LazyMap[TKey, TValue]) -> str """
        pass

    def TryGetCurrent(self, key, value):
        """ TryGetCurrent(self: LazyMap[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def TryRemoveCurrent(self, key, value):
        """ TryRemoveCurrent(self: LazyMap[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initialize=None, *__args):
        """
        __new__(cls: type, initialize: Func[TKey, TValue], enableCaching: bool, comparer: IEqualityComparer[TKey])
        __new__(cls: type, initialize: Func[TKey, TValue], enableCaching: bool)
        __new__(cls: type, initialize: Func[TKey, TValue], comparer: IEqualityComparer[TKey])
        __new__(cls: type, initialize: Func[TKey, TValue])
        __new__(cls: type)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    CurrentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCount(self: LazyMap[TKey, TValue]) -> int

"""

    CurrentItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentItems(self: LazyMap[TKey, TValue]) -> IEnumerable[KeyValuePair[TKey, TValue]]

"""

    CurrentKeys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentKeys(self: LazyMap[TKey, TValue]) -> IEnumerable[TKey]

"""

    CurrentValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValues(self: LazyMap[TKey, TValue]) -> IEnumerable[TValue]

"""

    IsCaching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCaching(self: LazyMap[TKey, TValue]) -> bool

"""

    KeyFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyFilter(self: LazyMap[TKey, TValue]) -> Func[TKey, bool]

Set: KeyFilter(self: LazyMap[TKey, TValue]) = value
"""



class LicenseManagerFeature(Enum, IComparable, IFormattable, IConvertible):
    """ enum LicenseManagerFeature, values: Compile (4), Debug (3), Enterprise (0), Professional (1), Standard (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Compile = None
    Debug = None
    Enterprise = None
    Professional = None
    Standard = None
    value__ = None


class LicenseManagerFeatureInfo(object):
    """ LicenseManagerFeatureInfo() """
    Expiration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Expiration(self: LicenseManagerFeatureInfo) -> DateTime

Set: Expiration(self: LicenseManagerFeatureInfo) = value
"""

    FeatureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureName(self: LicenseManagerFeatureInfo) -> str

Set: FeatureName(self: LicenseManagerFeatureInfo) = value
"""

    LicenseStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseStatus(self: LicenseManagerFeatureInfo) -> Status

Set: LicenseStatus(self: LicenseManagerFeatureInfo) = value
"""

    LicenseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseType(self: LicenseManagerFeatureInfo) -> LicenseType

Set: LicenseType(self: LicenseManagerFeatureInfo) = value
"""

    MaintVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaintVersion(self: LicenseManagerFeatureInfo) -> int

Set: MaintVersion(self: LicenseManagerFeatureInfo) = value
"""

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorVersion(self: LicenseManagerFeatureInfo) -> int

Set: MajorVersion(self: LicenseManagerFeatureInfo) = value
"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorVersion(self: LicenseManagerFeatureInfo) -> int

Set: MinorVersion(self: LicenseManagerFeatureInfo) = value
"""

    Package = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Package(self: LicenseManagerFeatureInfo) -> str

Set: Package(self: LicenseManagerFeatureInfo) = value
"""



class LicenseManagerFeatureInfoDictionary(object):
    """ LicenseManagerFeatureInfoDictionary() """
    ActivatedLicense = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActivatedLicense(self: LicenseManagerFeatureInfoDictionary) -> LicenseManagerFeature

Set: ActivatedLicense(self: LicenseManagerFeatureInfoDictionary) = value
"""

    CreateDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateDate(self: LicenseManagerFeatureInfoDictionary) -> DateTime

Set: CreateDate(self: LicenseManagerFeatureInfoDictionary) = value
"""

    FeatureInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureInfo(self: LicenseManagerFeatureInfoDictionary) -> Dictionary[LicenseManagerFeature, LicenseManagerFeatureInfo]

"""

    GuestAccountDialogLastDisplayTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GuestAccountDialogLastDisplayTime(self: LicenseManagerFeatureInfoDictionary) -> DateTime

Set: GuestAccountDialogLastDisplayTime(self: LicenseManagerFeatureInfoDictionary) = value
"""

    IsActivated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActivated(self: LicenseManagerFeatureInfoDictionary) -> bool

Set: IsActivated(self: LicenseManagerFeatureInfoDictionary) = value
"""

    IsAllowedAccount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAllowedAccount(self: LicenseManagerFeatureInfoDictionary) -> bool

Set: IsAllowedAccount(self: LicenseManagerFeatureInfoDictionary) = value
"""

    IsCheckoutFromServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCheckoutFromServer(self: LicenseManagerFeatureInfoDictionary) -> bool

Set: IsCheckoutFromServer(self: LicenseManagerFeatureInfoDictionary) = value
"""

    MachineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MachineName(self: LicenseManagerFeatureInfoDictionary) -> str

Set: MachineName(self: LicenseManagerFeatureInfoDictionary) = value
"""

    SuppressEvaluationDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuppressEvaluationDialog(self: LicenseManagerFeatureInfoDictionary) -> bool

Set: SuppressEvaluationDialog(self: LicenseManagerFeatureInfoDictionary) = value
"""

    SuppressGuestAccountDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuppressGuestAccountDialog(self: LicenseManagerFeatureInfoDictionary) -> bool

Set: SuppressGuestAccountDialog(self: LicenseManagerFeatureInfoDictionary) = value
"""

    SuppressUnlicensedDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuppressUnlicensedDialog(self: LicenseManagerFeatureInfoDictionary) -> bool

Set: SuppressUnlicensedDialog(self: LicenseManagerFeatureInfoDictionary) = value
"""

    UnlicensedDialogLastDisplayTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnlicensedDialogLastDisplayTime(self: LicenseManagerFeatureInfoDictionary) -> DateTime

Set: UnlicensedDialogLastDisplayTime(self: LicenseManagerFeatureInfoDictionary) = value
"""



class LicenseProviderBase(LicenseProvider):
    # no doc
    def GetLicense(self, context, type, instance, allowExceptions):
        """ GetLicense(self: LicenseProviderBase, context: LicenseContext, type: Type, instance: object, allowExceptions: bool) -> License """
        pass

    @staticmethod
    def RegisterNIAssembly(key):
        """ RegisterNIAssembly(key: str) """
        pass

    License = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: License(self: LicenseProviderBase) -> LicenseBase

"""



class LicenserHelper(object):
    # no doc
    @staticmethod
    def DecryptBase64(cypherText):
        """ DecryptBase64(cypherText: str) -> str """
        pass

    @staticmethod
    def Encrypt(plainText):
        """ Encrypt(plainText: str) -> str """
        pass


class LicenseType(Enum, IComparable, IFormattable, IConvertible):
    """ enum LicenseType, values: Beta (2), BetaRelease (4), Eval (1), Invalid (3), Release (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beta = None
    BetaRelease = None
    Eval = None
    Invalid = None
    Release = None
    value__ = None


class LinqTunnelAttribute(Attribute, _Attribute):
    """ LinqTunnelAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class MeansImplicitUseAttribute(Attribute, _Attribute):
    """
    MeansImplicitUseAttribute()
    MeansImplicitUseAttribute(useKindFlags: ImplicitUseKindFlags)
    MeansImplicitUseAttribute(targetFlags: ImplicitUseTargetFlags)
    MeansImplicitUseAttribute(useKindFlags: ImplicitUseKindFlags, targetFlags: ImplicitUseTargetFlags)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, useKindFlags: ImplicitUseKindFlags)
        __new__(cls: type, targetFlags: ImplicitUseTargetFlags)
        __new__(cls: type, useKindFlags: ImplicitUseKindFlags, targetFlags: ImplicitUseTargetFlags)
        """
        pass

    TargetFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetFlags(self: MeansImplicitUseAttribute) -> ImplicitUseTargetFlags

"""

    UseKindFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseKindFlags(self: MeansImplicitUseAttribute) -> ImplicitUseKindFlags

"""



class MSLicenseManager(object, IDisposable):
    """ MSLicenseManager(majorVersion: int, minorVersion: int, maintVersion: int, debugAllowed: bool) """
    def ActivateFamily(self, feature):
        """ ActivateFamily(self: MSLicenseManager, feature: LicenseManagerFeature) -> ActivateStatus """
        pass

    def CheckinAll(self):
        """ CheckinAll(self: MSLicenseManager) """
        pass

    def CheckinFeature(self, feature):
        """ CheckinFeature(self: MSLicenseManager, feature: LicenseManagerFeature) """
        pass

    def CheckInVLMLicenses(self):
        """ CheckInVLMLicenses(self: MSLicenseManager) """
        pass

    def CheckoutStartupFeature(self, startupFeature, suppressStartupDialog, showExitButton, isDesignTime, isConcurrentEnabled=None):
        """
        CheckoutStartupFeature(self: MSLicenseManager, startupFeature: LicenseManagerFeature, suppressStartupDialog: bool, showExitButton: bool, isDesignTime: bool) -> bool
        CheckoutStartupFeature(self: MSLicenseManager, startupFeature: LicenseManagerFeature, suppressStartupDialog: bool, showExitButton: bool, isDesignTime: bool, isConcurrentEnabled: bool) -> bool
        """
        pass

    def DeleteSerializedFiles(self):
        """ DeleteSerializedFiles(self: MSLicenseManager) """
        pass

    def Dispose(self, disposing=None):
        """ Dispose(self: MSLicenseManager)Dispose(self: MSLicenseManager, disposing: bool) """
        pass

    def GetExpiration(self, feature):
        """ GetExpiration(self: MSLicenseManager, feature: LicenseManagerFeature) -> DateTime """
        pass

    def GetFeatureInfo(self, feature, isDesignTime):
        """ GetFeatureInfo(self: MSLicenseManager, feature: LicenseManagerFeature, isDesignTime: bool) -> LicenseManagerFeatureInfo """
        pass

    def GetLicenseType(self, feature):
        """ GetLicenseType(self: MSLicenseManager, feature: LicenseManagerFeature) -> LicenseType """
        pass

    def GetStatus(self, feature):
        """ GetStatus(self: MSLicenseManager, feature: LicenseManagerFeature) -> Status """
        pass

    def HasFeature(self, feature):
        """ HasFeature(self: MSLicenseManager, feature: LicenseManagerFeature) -> bool """
        pass

    def IntegrationLicenseCheck(self, feature, suppressStartupDialog, showExitButton, isDesignTime):
        """ IntegrationLicenseCheck(self: MSLicenseManager, feature: LicenseManagerFeature, suppressStartupDialog: bool, showExitButton: bool, isDesignTime: bool) -> bool """
        pass

    def IsCheckoutFromServer(self):
        """ IsCheckoutFromServer(self: MSLicenseManager) -> bool """
        pass

    def IsLicenseFromVLM(self):
        """ IsLicenseFromVLM(self: MSLicenseManager) -> bool """
        pass

    def ShowStartupDialog(self, feature, showExitButton):
        """ ShowStartupDialog(self: MSLicenseManager, feature: LicenseManagerFeature, showExitButton: bool) """
        pass

    def ValidateLicenseManagerFeature(self, feature):
        """ ValidateLicenseManagerFeature(self: MSLicenseManager, feature: LicenseManagerFeature) """
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
    def __new__(self, majorVersion, minorVersion, maintVersion, debugAllowed):
        """ __new__(cls: type, majorVersion: int, minorVersion: int, maintVersion: int, debugAllowed: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Disposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Disposed(self: MSLicenseManager) -> bool

"""



class MultiKeyDictionary(object):
    """ MultiKeyDictionary[TKey1, TKey2, TValue]() """
    def Add(self, key1, key2, value):
        """ Add(self: MultiKeyDictionary[TKey1, TKey2, TValue], key1: TKey1, key2: TKey2, value: TValue) """
        pass

    def Clear(self):
        """ Clear(self: MultiKeyDictionary[TKey1, TKey2, TValue]) """
        pass

    def ContainsKey(self, key1, key2):
        """ ContainsKey(self: MultiKeyDictionary[TKey1, TKey2, TValue], key1: TKey1, key2: TKey2) -> bool """
        pass

    def Remove(self, key1, key2):
        """ Remove(self: MultiKeyDictionary[TKey1, TKey2, TValue], key1: TKey1, key2: TKey2) """
        pass

    def TryGetValue(self, key1, key2, value):
        """ TryGetValue(self: MultiKeyDictionary[TKey1, TKey2, TValue], key1: TKey1, key2: TKey2) -> (bool, TValue) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class MustUseReturnValueAttribute(Attribute, _Attribute):
    """
    MustUseReturnValueAttribute()
    MustUseReturnValueAttribute(justification: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, justification=None):
        """
        __new__(cls: type)
        __new__(cls: type, justification: str)
        """
        pass

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justification(self: MustUseReturnValueAttribute) -> str

"""



class NILog(object):
    # no doc
    @staticmethod
    def IsLevelEnabled(level):
        """ IsLevelEnabled(level: NILogMessageLevel) -> bool """
        pass

    @staticmethod
    def Message(level, category, *__args):
        """ Message(level: NILogMessageLevel, category: str, message: str)Message(level: NILogMessageLevel, category: str, format: str, arg1: object)Message(level: NILogMessageLevel, category: str, format: str, arg1: object, arg2: object)Message(level: NILogMessageLevel, category: str, format: str, arg1: object, arg2: object, arg3: object)Message(level: NILogMessageLevel, category: str, format: str, *args: Array[object]) """
        pass

    __all__ = [
        'IsLevelEnabled',
        'Message',
    ]


class NIValidation(object):
    # no doc
    @staticmethod
    def CopyToSufficientSize(guard, collectionCount, copyCount, message):
        """ CopyToSufficientSize(guard: Guard[int], collectionCount: int, copyCount: int, message: str) -> Guard[int] """
        pass

    @staticmethod
    def DebugAssignableTo(type, expected, info):
        """ DebugAssignableTo(type: Type, expected: Type, *info: Array[str]) """
        pass

    @staticmethod
    def DebugCondition(condition, format, args):
        """ DebugCondition(condition: bool, format: str, *args: Array[object]) """
        pass

    @staticmethod
    def DebugEqualTo(value, expected, info):
        """ DebugEqualTo[T](value: T, expected: T, *info: Array[str]) """
        pass

    @staticmethod
    def DebugFail(value, info):
        """ DebugFail[T](value: T, *info: Array[str]) """
        pass

    @staticmethod
    def DebugIndexInRange(index, count, info):
        """ DebugIndexInRange(index: int, count: int, *info: Array[str]) """
        pass

    @staticmethod
    def DebugIsNull(value, info):
        """ DebugIsNull[T](value: T, *info: Array[str]) """
        pass

    @staticmethod
    def DebugIsNullOrEmpty(value, info):
        """ DebugIsNullOrEmpty[T](value: IEnumerable[T], *info: Array[str])DebugIsNullOrEmpty(value: str, *info: Array[str]) """
        pass

    @staticmethod
    def DebugNonNegative(value, info):
        """ DebugNonNegative(value: int, *info: Array[str]) """
        pass

    @staticmethod
    def DebugNoNullElements(value, info):
        """ DebugNoNullElements[T](value: IEnumerable[T], *info: Array[str]) """
        pass

    @staticmethod
    def DebugNotEqualTo(value, expected, info):
        """ DebugNotEqualTo[T](value: T, expected: T, *info: Array[str]) """
        pass

    @staticmethod
    def DebugNotNull(value, info):
        """ DebugNotNull[T](value: T, *info: Array[str]) """
        pass

    @staticmethod
    def DebugNotNullOrEmpty(value, info):
        """ DebugNotNullOrEmpty[T](value: IEnumerable[T], *info: Array[str])DebugNotNullOrEmpty(value: str, *info: Array[str]) """
        pass

    @staticmethod
    def ElementSatisfies(guard, firstInvalidElement, format, args):
        """ ElementSatisfies[T](guard: Guard[T], firstInvalidElement: int, format: str, *args: Array[object]) -> Guard[T] """
        pass

    @staticmethod
    def EnumIsDefined(guard):
        """
        EnumIsDefined[T](guard: Guard[T]) -> Guard[T]
        EnumIsDefined(guard: Guard[ScopeComparison]) -> Guard[ScopeComparison]
        EnumIsDefined(guard: Guard[Monotonicity]) -> Guard[Monotonicity]
        """
        pass

    @staticmethod
    def FormatSatisfies(guard, condition, format, args):
        """ FormatSatisfies(guard: Guard[str], condition: bool, format: str, *args: Array[object]) -> Guard[str] """
        pass

    @staticmethod
    def FormatSuccessful(guard):
        """ FormatSuccessful(guard: Guard[str]) -> Guard[str] """
        pass

    @staticmethod
    def GuardCondition(condition, format, args):
        """ GuardCondition(condition: bool, format: str, *args: Array[object]) """
        pass

    @staticmethod
    def GuardParam(parameterValue, parameterName):
        """ GuardParam[T](parameterValue: T, parameterName: str) -> Guard[T] """
        pass

    @staticmethod
    def GuardValue(variableValue, variableDescription):
        """ GuardValue[T](variableValue: T, variableDescription: str) -> Guard[T] """
        pass

    @staticmethod
    def IndexInRange(guard, *__args):
        """
        IndexInRange(guard: Guard[int], scope: TraitScope) -> Guard[int]
        IndexInRange(guard: Guard[int], count: int) -> Guard[int]
        IndexInRange(guard: Guard[int], count: int, allowEmptyIndex: bool) -> Guard[int]
        """
        pass

    @staticmethod
    def IsEqualTo(guard, expected, format, args):
        """ IsEqualTo[T](guard: Guard[T], expected: T, format: str, *args: Array[object]) -> Guard[T] """
        pass

    @staticmethod
    def IsInRange(guard, isInRange, format, args):
        """ IsInRange[T](guard: Guard[T], isInRange: bool, format: str, *args: Array[object]) -> Guard[T] """
        pass

    @staticmethod
    def NonNegative(guard):
        """
        NonNegative(guard: Guard[int]) -> Guard[int]
        NonNegative(guard: Guard[float]) -> Guard[float]
        """
        pass

    @staticmethod
    def NoNullElements(guard):
        """
        NoNullElements[T](guard: Guard[T]) -> Guard[T]
        NoNullElements[T](guard: Guard[IList[T]]) -> Guard[IList[T]]
        NoNullElements[T](guard: Guard[Array[T]]) -> Guard[Array[T]]
        """
        pass

    @staticmethod
    def NotDisposed(guard):
        """ NotDisposed[T](guard: Guard[T]) -> Guard[T] """
        pass

    @staticmethod
    def NotEmpty(guard):
        """
        NotEmpty[T](guard: Guard[T]) -> Guard[T]
        NotEmpty[T](guard: Guard[Array[T]]) -> Guard[Array[T]]
        NotEmpty(guard: Guard[str]) -> Guard[str]
        """
        pass

    @staticmethod
    def NotNull(guard):
        """ NotNull[T](guard: Guard[T]) -> Guard[T] """
        pass

    @staticmethod
    def NotSpecialValue(guard):
        """ NotSpecialValue(guard: Guard[float]) -> Guard[float] """
        pass

    @staticmethod
    def ParseSuccessful(guard, sourceValue, targetType):
        """ ParseSuccessful[T](guard: Guard[T], sourceValue: str, targetType: Type) -> Guard[T] """
        pass

    DebugBuildSymbol = 'DEBUG'
    __all__ = [
        'CopyToSufficientSize',
        'DebugAssignableTo',
        'DebugBuildSymbol',
        'DebugCondition',
        'DebugEqualTo',
        'DebugFail',
        'DebugIndexInRange',
        'DebugIsNull',
        'DebugIsNullOrEmpty',
        'DebugNonNegative',
        'DebugNoNullElements',
        'DebugNotEqualTo',
        'DebugNotNull',
        'DebugNotNullOrEmpty',
        'ElementSatisfies',
        'EnumIsDefined',
        'FormatSatisfies',
        'FormatSuccessful',
        'GuardCondition',
        'GuardParam',
        'GuardValue',
        'IndexInRange',
        'IsEqualTo',
        'IsInRange',
        'NonNegative',
        'NoNullElements',
        'NotDisposed',
        'NotEmpty',
        'NotNull',
        'NotSpecialValue',
        'ParseSuccessful',
    ]


class NoEnumerationAttribute(Attribute, _Attribute):
    """ NoEnumerationAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class NotifyPropertyChangedInvocatorAttribute(Attribute, _Attribute):
    """
    NotifyPropertyChangedInvocatorAttribute()
    NotifyPropertyChangedInvocatorAttribute(parameterName: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parameterName=None):
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str)
        """
        pass

    ParameterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParameterName(self: NotifyPropertyChangedInvocatorAttribute) -> str

"""



class NotNullAttribute(Attribute, _Attribute):
    """ NotNullAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ObsoleteMessage(object):
    # no doc
    SynchronizingObject = 'Use SynchronizeCallbacks to specify that the object marshals callbacks across threads appropriately.'
    __all__ = [
        'SynchronizingObject',
    ]


class PerformsLicenseCheckAttribute(Attribute, _Attribute):
    """ PerformsLicenseCheckAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PrecisionDateTimeEpoch(Enum, IComparable, IFormattable, IConvertible):
    """ enum PrecisionDateTimeEpoch, values: CTimeEpoch (1), DotNetEpoch (0), FileTimeEpoch (3), LabViewEpoch (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CTimeEpoch = None
    DotNetEpoch = None
    FileTimeEpoch = None
    LabViewEpoch = None
    value__ = None


class PublicAPIAttribute(Attribute, _Attribute):
    """
    PublicAPIAttribute()
    PublicAPIAttribute(comment: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, comment=None):
        """
        __new__(cls: type)
        __new__(cls: type, comment: str)
        """
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: PublicAPIAttribute) -> str

"""



class PureAttribute(Attribute, _Attribute):
    """ PureAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class RegexPatternAttribute(Attribute, _Attribute):
    """ RegexPatternAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class SpectrumChangedEventArgs(EventArgs):
    """
    SpectrumChangedEventArgs[TData](spectrum: Spectrum[TData], changeType: SpectrumChangeType)
    SpectrumChangedEventArgs[TData](spectrum: Spectrum[TData], sampleIndex: int)
    SpectrumChangedEventArgs[TData](spectrum: Spectrum[TData], sampleIndex: int, sampleCount: int)
    SpectrumChangedEventArgs[TData](spectrum: Spectrum[TData], sampleIndex: int, sampleCount: int, changeType: SpectrumChangeType)
    """
    @staticmethod # known case of __new__
    def __new__(self, spectrum, *__args):
        """
        __new__(cls: type, spectrum: Spectrum[TData], changeType: SpectrumChangeType)
        __new__(cls: type, spectrum: Spectrum[TData], sampleIndex: int)
        __new__(cls: type, spectrum: Spectrum[TData], sampleIndex: int, sampleCount: int)
        __new__(cls: type, spectrum: Spectrum[TData], sampleIndex: int, sampleCount: int, changeType: SpectrumChangeType)
        """
        pass

    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: SpectrumChangedEventArgs[TData]) -> SpectrumChangeType

"""

    SampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleCount(self: SpectrumChangedEventArgs[TData]) -> int

"""

    SampleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleIndex(self: SpectrumChangedEventArgs[TData]) -> int

"""

    Spectrum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spectrum(self: SpectrumChangedEventArgs[TData]) -> Spectrum[TData]

"""



class SpectrumChangeType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) SpectrumChangeType, values: Data (1), Frequency (2), Label (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Data = None
    Frequency = None
    Label = None
    value__ = None


class StringFormatMethodAttribute(Attribute, _Attribute):
    """ StringFormatMethodAttribute(formatParameterName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, formatParameterName):
        """ __new__(cls: type, formatParameterName: str) """
        pass

    FormatParameterName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormatParameterName(self: StringFormatMethodAttribute) -> str

"""



class TypeConversionMap(object):
    """ TypeConversionMap() """
    def AddEntry(self, sourceType, targetType, handler):
        """ AddEntry(self: TypeConversionMap, sourceType: Type, targetType: Type, handler: ConversionHandler) """
        pass

    def DefaultHandler(self, *args): #cannot find CLR method
        """ ConversionHandler(object: object, method: IntPtr) """
        pass

    def HasEntry(self, sourceType, targetType):
        """ HasEntry(self: TypeConversionMap, sourceType: Type, targetType: Type) -> bool """
        pass

    def RemoveEntry(self, sourceType, targetType):
        """ RemoveEntry(self: TypeConversionMap, sourceType: Type, targetType: Type) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    ConversionHandler = None


class UnmanagedHandle(MarshalByRefObject, IDisposable):
    # no doc
    def CloseHandle(self, *args): #cannot find CLR method
        """ CloseHandle(self: UnmanagedHandle) """
        pass

    def Dispose(self):
        """ Dispose(self: UnmanagedHandle) """
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

    def ToHandle(self):
        """ ToHandle(self: UnmanagedHandle) -> IntPtr """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, handle: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class UsedImplicitlyAttribute(Attribute, _Attribute):
    """
    UsedImplicitlyAttribute()
    UsedImplicitlyAttribute(useKindFlags: ImplicitUseKindFlags)
    UsedImplicitlyAttribute(targetFlags: ImplicitUseTargetFlags)
    UsedImplicitlyAttribute(useKindFlags: ImplicitUseKindFlags, targetFlags: ImplicitUseTargetFlags)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, useKindFlags: ImplicitUseKindFlags)
        __new__(cls: type, targetFlags: ImplicitUseTargetFlags)
        __new__(cls: type, useKindFlags: ImplicitUseKindFlags, targetFlags: ImplicitUseTargetFlags)
        """
        pass

    TargetFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetFlags(self: UsedImplicitlyAttribute) -> ImplicitUseTargetFlags

"""

    UseKindFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseKindFlags(self: UsedImplicitlyAttribute) -> ImplicitUseKindFlags

"""



class ValueProviderAttribute(Attribute, _Attribute):
    """ ValueProviderAttribute(name: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ValueProviderAttribute) -> str

"""



class WaveformChangedEventArgs(EventArgs):
    """
    WaveformChangedEventArgs[TData](waveform: AnalogWaveform[TData], changeType: WaveformChangeType)
    WaveformChangedEventArgs[TData](waveform: ComplexWaveform[TData], changeType: WaveformChangeType)
    WaveformChangedEventArgs[TData](waveform: AnalogWaveform[TData], sampleIndex: int)
    WaveformChangedEventArgs[TData](waveform: AnalogWaveform[TData], sampleIndex: int, sampleCount: int)
    WaveformChangedEventArgs[TData](waveform: AnalogWaveform[TData], sampleIndex: int, sampleCount: int, changeType: WaveformChangeType)
    WaveformChangedEventArgs[TData](waveform: ComplexWaveform[TData], sampleIndex: int)
    WaveformChangedEventArgs[TData](waveform: ComplexWaveform[TData], sampleIndex: int, sampleCount: int)
    WaveformChangedEventArgs[TData](waveform: ComplexWaveform[TData], sampleIndex: int, sampleCount: int, changeType: WaveformChangeType)
    """
    @staticmethod # known case of __new__
    def __new__(self, waveform, *__args):
        """
        __new__(cls: type, waveform: AnalogWaveform[TData], changeType: WaveformChangeType)
        __new__(cls: type, waveform: ComplexWaveform[TData], changeType: WaveformChangeType)
        __new__(cls: type, waveform: AnalogWaveform[TData], sampleIndex: int)
        __new__(cls: type, waveform: AnalogWaveform[TData], sampleIndex: int, sampleCount: int)
        __new__(cls: type, waveform: AnalogWaveform[TData], sampleIndex: int, sampleCount: int, changeType: WaveformChangeType)
        __new__(cls: type, waveform: ComplexWaveform[TData], sampleIndex: int)
        __new__(cls: type, waveform: ComplexWaveform[TData], sampleIndex: int, sampleCount: int)
        __new__(cls: type, waveform: ComplexWaveform[TData], sampleIndex: int, sampleCount: int, changeType: WaveformChangeType)
        """
        pass

    AnalogWaveform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnalogWaveform(self: WaveformChangedEventArgs[TData]) -> AnalogWaveform[TData]

"""

    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: WaveformChangedEventArgs[TData]) -> WaveformChangeType

"""

    ComplexWaveform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComplexWaveform(self: WaveformChangedEventArgs[TData]) -> ComplexWaveform[TData]

"""

    SampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleCount(self: WaveformChangedEventArgs[TData]) -> int

"""

    SampleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleIndex(self: WaveformChangedEventArgs[TData]) -> int

"""

    WaveformType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaveformType(self: WaveformChangedEventArgs[TData]) -> WaveformType

"""



class WaveformChangeType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) WaveformChangeType, values: Data (1), Label (4), Timing (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Data = None
    Label = None
    Timing = None
    value__ = None


class WaveformType(Enum, IComparable, IFormattable, IConvertible):
    """ enum WaveformType, values: Analog (0), Complex (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Analog = None
    Complex = None
    value__ = None


