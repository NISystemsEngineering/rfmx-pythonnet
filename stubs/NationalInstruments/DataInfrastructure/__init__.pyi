# encoding: utf-8
# module NationalInstruments.DataInfrastructure calls itself DataInfrastructure
# from NationalInstruments.Common, Version=19.0.40.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Buffer(object, IBuffer, IIndicateDisposed, IDisposable, IServiceProvider, IList[TData], ICollection[TData], IEnumerable[TData], IEnumerable):
    # no doc
    def Contains(self, item):
        """ Contains(self: Buffer[TData], item: TData) -> bool """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: Buffer[TData], destination: Array[TData], destinationIndex: int)CopyTo(self: Buffer[TData], sourceIndex: int, destination: Array[TData], destinationIndex: int, length: int)CopyTo(self: Buffer[TData], sourceIndex: int, destination: WritableBuffer[TData], destinationIndex: int, length: int) """
        pass

    def Dispose(self):
        """ Dispose(self: Buffer[TData]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Buffer[TData]) -> IEnumerator[TData] """
        pass

    def GetReadable(self, traitFilter=None):
        """
        GetReadable(self: Buffer[TData]) -> Buffer[TData]
        GetReadable(self: Buffer[TData], traitFilter: Func[Trait, Trait]) -> Buffer[TData]
        """
        pass

    def GetWritable(self):
        """ GetWritable(self: Buffer[TData]) -> WritableBuffer[TData] """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: Buffer[TData], item: TData) -> int """
        pass

    def Join(self, other, unit, traitFilter=None):
        """
        Join(self: Buffer[TData], other: Buffer[TData], unit: Unit) -> Buffer[TData]
        Join(self: Buffer[TData], other: Buffer[TData], unit: Unit, traitFilter: Func[Trait, Trait]) -> Buffer[TData]
        """
        pass

    def MakeNonvolatile(self):
        """ MakeNonvolatile(self: Buffer[TData]) """
        pass

    def MakeWritable(self):
        """ MakeWritable(self: Buffer[TData]) -> WritableBuffer[TData] """
        pass

    def Slice(self, startIndex, length, traitFilter=None):
        """
        Slice(self: Buffer[TData], startIndex: int, length: int) -> Buffer[TData]
        Slice(self: Buffer[TData], startIndex: int, length: int, traitFilter: Func[Trait, Trait]) -> Buffer[TData]
        """
        pass

    def ToArray(self):
        """ ToArray(self: Buffer[TData]) -> Array[TData] """
        pass

    def ToString(self):
        """ ToString(self: Buffer[TData]) -> str """
        pass

    def Transform(self, transformer, *__args):
        """
        Transform[TResult](self: Buffer[TData], transformer: Func[TData, TResult], unit: Unit, traits: IEnumerable[Trait]) -> Buffer[TResult]
        Transform[TResult](self: Buffer[TData], transformer: Func[TData, TResult], unit: Unit, traitFilter: Func[Trait, Trait]) -> Buffer[TResult]
        Transform[TResult](self: Buffer[TData], transformer: Func[TData, int, TResult], unit: Unit, traits: IEnumerable[Trait]) -> Buffer[TResult]
        Transform[TResult](self: Buffer[TData], transformer: Func[TData, int, TResult], unit: Unit, traitFilter: Func[Trait, Trait]) -> Buffer[TResult]
        Transform[TResult](self: Buffer[TData], transformer: TryTransform[TData, TResult], fallbackResult: TResult, unit: Unit, traits: IEnumerable[Trait]) -> Buffer[TResult]
        Transform[TResult](self: Buffer[TData], transformer: TryTransform[TData, TResult], fallbackResult: TResult, unit: Unit, traitFilter: Func[Trait, Trait]) -> Buffer[TResult]
        """
        pass

    def TryGetArrayIndexer(self):
        """ TryGetArrayIndexer(self: Buffer[TData]) -> Nullable[ArrayDataStoreIndexer] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[TData], item: TData) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: ue if item is found in the System.Collections.Generic.ICollection; otherwise, lse.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: Buffer[TData]) -> Type

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: Buffer[TData]) -> bool

"""

    IsVolatile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVolatile(self: Buffer[TData]) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: Buffer[TData]) -> int

"""

    Traits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Traits(self: Buffer[TData]) -> TraitSet

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit(self: Buffer[TData]) -> Unit

"""


    ArrayDataStoreIndexer = None


class BufferPool(object):
    # no doc
    def CreateBuffer(self, *args): #cannot find CLR method
        """ CreateBuffer[TData](self: BufferPool, dataStore: RawDataStore[TData], unit: Unit) -> Buffer[TData] """
        pass

    def CreateWritableBuffer(self, *args): #cannot find CLR method
        """ CreateWritableBuffer[TData](self: BufferPool, dataStore: RawDataStore[TData], unit: Unit) -> WritableBuffer[TData] """
        pass

    @staticmethod
    def GetEmptyBuffer():
        """ GetEmptyBuffer[TData]() -> Buffer[TData] """
        pass

    @staticmethod
    def Join(buffers, unit, traitFilter=None):
        """
        Join[TData](buffers: IEnumerable[Buffer[TData]], unit: Unit) -> Buffer[TData]
        Join[TData](buffers: IEnumerable[Buffer[TData]], unit: Unit, traitFilter: Func[Trait, Trait]) -> Buffer[TData]
        """
        pass

    Default = None


class Trait(object, IEquatable[Trait]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: Trait, other: Trait) -> bool
        Equals(self: Trait, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Trait) -> int """
        pass

    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: Trait) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def HasSameStructure(self, other, includeScope=None):
        """
        HasSameStructure(self: Trait, other: Trait) -> bool
        HasSameStructure(self: Trait, other: Trait, includeScope: bool) -> bool
        """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: Trait, other: Trait) -> bool """
        pass

    def Slice(self, scope, offset, preserveGlobalTraits):
        """ Slice(self: Trait, scope: TraitScope, offset: int, preserveGlobalTraits: bool) -> Trait """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: Trait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: Trait) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, scope: TraitScope) """
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

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scope(self: Trait) -> TraitScope

"""



class CoordinateSystemTrait(Trait, IEquatable[Trait]):
    """ CoordinateSystemTrait(coordinateSystem: str) """
    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: CoordinateSystemTrait) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: CoordinateSystemTrait, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: CoordinateSystemTrait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: CoordinateSystemTrait) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, coordinateSystem):
        """ __new__(cls: type, coordinateSystem: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: CoordinateSystemTrait) -> str

"""


    Cartesian = None
    Polar = None


class DigitalSample(object, IList[DigitalState], ICollection[DigitalState], IEnumerable[DigitalState], IEnumerable, IEquatable[DigitalSample]):
    """
    DigitalSample(values: IList[DigitalState])
    DigitalSample(values: IList[DigitalState], parentIndex: int)
    DigitalSample(values: IList[DigitalState], parentIndex: int, stateIndex: int)
    """
    def ChangeParentIndex(self, parentIndex):
        """ ChangeParentIndex(self: DigitalSample, parentIndex: int) -> DigitalSample """
        pass

    def Contains(self, item):
        """ Contains(self: DigitalSample, item: DigitalState) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: DigitalSample, array: Array[DigitalState], arrayIndex: int) """
        pass

    def Equals(self, *__args):
        """
        Equals(self: DigitalSample, other: DigitalSample) -> bool
        Equals(self: DigitalSample, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromDigitalState(state):
        """ FromDigitalState(state: DigitalState) -> DigitalSample """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DigitalSample) -> IEnumerator[DigitalState] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DigitalSample) -> int """
        pass

    def GetValuesType(self):
        """ GetValuesType(self: DigitalSample) -> Type """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: DigitalSample, item: DigitalState) -> int """
        pass

    @staticmethod
    def Parse(input):
        """ Parse(input: str) -> DigitalSample """
        pass

    def ToString(self):
        """ ToString(self: DigitalSample) -> str """
        pass

    @staticmethod
    def TryParse(input, result):
        """ TryParse(input: str) -> (bool, DigitalSample) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[DigitalState], item: DigitalState) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
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
    def __new__(self, values, parentIndex=None, stateIndex=None):
        """
        __new__[DigitalSample]() -> DigitalSample
        
        __new__(cls: type, values: IList[DigitalState])
        __new__(cls: type, values: IList[DigitalState], parentIndex: int)
        __new__(cls: type, values: IList[DigitalState], parentIndex: int, stateIndex: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DigitalSample) -> int

"""

    ParentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentIndex(self: DigitalSample) -> int

"""

    StateIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateIndex(self: DigitalSample) -> int

"""



class ExtremeSamplesTrait(IndicesTrait, IEquatable[Trait]):
    """
    ExtremeSamplesTrait(scope: TraitScope, minimumIndex: int, maximumIndex: int)
    ExtremeSamplesTrait(scope: TraitScope, minimumIndices: IEnumerable[int], maximumIndices: IEnumerable[int])
    ExtremeSamplesTrait(scope: TraitScope, minimumIndices: IndexSet, maximumIndices: IndexSet)
    """
    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: ExtremeSamplesTrait) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: ExtremeSamplesTrait, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: ExtremeSamplesTrait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, scope, *__args):
        """
        __new__(cls: type, scope: TraitScope, minimumIndex: int, maximumIndex: int)
        __new__(cls: type, scope: TraitScope, minimumIndices: IEnumerable[int], maximumIndices: IEnumerable[int])
        __new__(cls: type, scope: TraitScope, minimumIndices: IndexSet, maximumIndices: IndexSet)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MaximumIndexSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumIndexSet(self: ExtremeSamplesTrait) -> IndexSet

"""

    MaximumIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumIndices(self: ExtremeSamplesTrait) -> IEnumerable[int]

"""

    MinimumIndexSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumIndexSet(self: ExtremeSamplesTrait) -> IndexSet

"""

    MinimumIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumIndices(self: ExtremeSamplesTrait) -> IEnumerable[int]

"""


    Empty = None


class IBuffer(IIndicateDisposed, IDisposable):
    # no doc
    def GetReadable(self, traitFilter=None):
        """
        GetReadable(self: IBuffer) -> IBuffer
        GetReadable(self: IBuffer, traitFilter: Func[Trait, Trait]) -> IBuffer
        """
        pass

    def Slice(self, startIndex, length, traitFilter=None):
        """
        Slice(self: IBuffer, startIndex: int, length: int) -> IBuffer
        Slice(self: IBuffer, startIndex: int, length: int, traitFilter: Func[Trait, Trait]) -> IBuffer
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: IBuffer) -> Type

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: IBuffer) -> int

"""

    Traits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Traits(self: IBuffer) -> TraitSet

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit(self: IBuffer) -> Unit

"""



class IndexBufferTrait(Trait, IEquatable[Trait]):
    # no doc
    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: IndexBufferTrait) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: IndexBufferTrait, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: IndexBufferTrait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: IndexBufferTrait) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Instance = None


class IUnitConverter:
    # no doc
    def TryConvert(self, value, result):
        """ TryConvert(self: IUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def TryConvertBack(self, value, result):
        """ TryConvertBack(self: IUnitConverter[TData], value: TData) -> (bool, TData) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanConvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvert(self: IUnitConverter[TData]) -> bool

"""

    CanConvertBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanConvertBack(self: IUnitConverter[TData]) -> bool

"""

    From = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: From(self: IUnitConverter[TData]) -> Unit

"""

    To = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: To(self: IUnitConverter[TData]) -> Unit

"""



class Monotonicity(Enum, IComparable, IFormattable, IConvertible):
    """ enum Monotonicity, values: Decreasing (2), Increasing (1), NonMonotonic (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Decreasing = None
    Increasing = None
    NonMonotonic = None
    value__ = None


class MonotonicityTrait(Trait, IEquatable[Trait]):
    # no doc
    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: MonotonicityTrait) -> int """
        pass

    @staticmethod
    def GetMonotonicity(traits, isSequence=None):
        """
        GetMonotonicity(traits: TraitSet) -> Monotonicity
        GetMonotonicity(traits: TraitSet) -> (Monotonicity, bool)
        """
        pass

    @staticmethod
    def GetTrait(scope, monotonicity, isSequence=None):
        """
        GetTrait(scope: TraitScope, monotonicity: Monotonicity) -> MonotonicityTrait
        GetTrait(scope: TraitScope, monotonicity: Monotonicity, isSequence: bool) -> MonotonicityTrait
        """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: Trait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: MonotonicityTrait, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: MonotonicityTrait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: MonotonicityTrait) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsMonotonic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMonotonic(self: MonotonicityTrait) -> bool

"""

    IsSequence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSequence(self: MonotonicityTrait) -> bool

"""

    Monotonicity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Monotonicity(self: MonotonicityTrait) -> Monotonicity

"""


    StreamDecreasing = None
    StreamDecreasingSequence = None
    StreamIncreasing = None
    StreamIncreasingSequence = None
    StreamNonMonotonic = None


class NamedIndicesTrait(IndicesTrait, IEquatable[Trait]):
    """
    NamedIndicesTrait(scope: TraitScope, name: str, indices: IEnumerable[int])
    NamedIndicesTrait(scope: TraitScope, name: str, indices: IndexSet)
    """
    @staticmethod
    def GetAllIndices(traits, name):
        """
        GetAllIndices(traits: TraitSet, name: str) -> IList[int]
        GetAllIndices(traits: IEnumerable[Trait], name: str) -> IList[int]
        """
        pass

    @staticmethod
    def GetAllSets(traits, name):
        """
        GetAllSets(traits: TraitSet, name: str) -> IndexSet
        GetAllSets(traits: IEnumerable[Trait], name: str) -> IndexSet
        """
        pass

    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: NamedIndicesTrait) -> int """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: NamedIndicesTrait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: NamedIndicesTrait, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: NamedIndicesTrait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: NamedIndicesTrait) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, scope, name, indices):
        """
        __new__(cls: type, scope: TraitScope, name: str, indices: IEnumerable[int])
        __new__(cls: type, scope: TraitScope, name: str, indices: IndexSet)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IndexSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndexSet(self: NamedIndicesTrait) -> IndexSet

"""

    Indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Indices(self: NamedIndicesTrait) -> IEnumerable[int]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NamedIndicesTrait) -> str

"""


    InvalidSamples = 'Invalid Samples'
    JoinLocations = 'Join Locations'
    RemoveLocations = 'Remove Locations'
    VisibleIndices = 'Visible Indices'


class NamedValueTrait(Trait, IEquatable[Trait]):
    """
    NamedValueTrait(name: str, value: object)
    NamedValueTrait(scope: TraitScope, name: str, value: object)
    """
    def GetLocalHashCode(self, *args): #cannot find CLR method
        """ GetLocalHashCode(self: NamedValueTrait) -> int """
        pass

    @staticmethod
    def GetNamedTrait(traits, scope, name):
        """ GetNamedTrait(traits: TraitSet, scope: TraitScope, name: str) -> NamedValueTrait """
        pass

    @staticmethod
    def GetNamedTraits(traits, name):
        """ GetNamedTraits(traits: TraitSet, name: str) -> IEnumerable[NamedValueTrait] """
        pass

    @staticmethod
    def GetNamedValue(traits, scope, name):
        """ GetNamedValue(traits: TraitSet, scope: TraitScope, name: str) -> object """
        pass

    def HasSameLocalStructure(self, *args): #cannot find CLR method
        """ HasSameLocalStructure(self: NamedValueTrait, other: Trait) -> bool """
        pass

    def LocalEquals(self, *args): #cannot find CLR method
        """ LocalEquals(self: NamedValueTrait, other: Trait) -> bool """
        pass

    def SliceCore(self, *args): #cannot find CLR method
        """ SliceCore(self: NamedValueTrait, newScope: TraitScope, offset: int) -> Trait """
        pass

    def ToString(self):
        """ ToString(self: NamedValueTrait) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, name: str, value: object)
        __new__(cls: type, scope: TraitScope, name: str, value: object)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NamedValueTrait) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: NamedValueTrait) -> object

"""


    AllowRelativeTiming = 'Allow Relative Timing'
    CopyVolatileData = 'Copy Volatile Data'
    Index = 'Index'
    Interval = 'Interval'
    LargestSampleSize = 'Largest Sample Size'
    Metadata = 'Metadata'
    NewSamplesCount = 'New Samples Count'
    Stride = 'Stride'


class RationalInt32(object, IEquatable[RationalInt32], IComparable[RationalInt32]):
    """
    RationalInt32(numerator: int)
    RationalInt32(numerator: int, denominator: int)
    """
    @staticmethod
    def Add(left, right):
        """ Add(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def CompareTo(self, other):
        """ CompareTo(self: RationalInt32, other: RationalInt32) -> int """
        pass

    @staticmethod
    def Divide(left, right):
        """ Divide(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def Equals(self, *__args):
        """
        Equals(self: RationalInt32, obj: object) -> bool
        Equals(self: RationalInt32, other: RationalInt32) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: RationalInt32) -> int """
        pass

    @staticmethod
    def Inverse(value):
        """ Inverse(value: RationalInt32) -> RationalInt32 """
        pass

    @staticmethod
    def IsNormalized(value):
        """ IsNormalized(value: RationalInt32) -> bool """
        pass

    @staticmethod
    def Multiply(left, right):
        """ Multiply(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    @staticmethod
    def Negate(value):
        """ Negate(value: RationalInt32) -> RationalInt32 """
        pass

    @staticmethod
    def Normalize(value):
        """ Normalize(value: RationalInt32) -> RationalInt32 """
        pass

    @staticmethod
    def Subtract(left, right):
        """ Subtract(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def ToString(self):
        """ ToString(self: RationalInt32) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(value: RationalInt32) -> float """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(value: RationalInt32) -> float """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(value: RationalInt32) -> int """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(value: RationalInt32) -> int """
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
    def __new__(self, numerator, denominator=None):
        """
        __new__[RationalInt32]() -> RationalInt32
        
        __new__(cls: type, numerator: int)
        __new__(cls: type, numerator: int, denominator: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(value: RationalInt32) -> RationalInt32 """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(left: RationalInt32, right: RationalInt32) -> RationalInt32 """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    Denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Denominator(self: RationalInt32) -> int

"""

    Numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Numerator(self: RationalInt32) -> int

"""


    MaxValue = None
    MinusOne = None
    MinValue = None
    One = None
    Zero = None


class Unit(object, IFormattable, IEquatable[Unit]):
    # no doc
    def CanConvert(self, to):
        """ CanConvert[TData](self: Unit, to: Unit) -> bool """
        pass

    def CreateConverter(self, *args): #cannot find CLR method
        """ CreateConverter[TData](self: Unit, to: Unit) -> IUnitConverter[TData] """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Unit, obj: object) -> bool
        Equals(self: Unit, other: Unit) -> bool
        """
        pass

    def EqualsCore(self, *args): #cannot find CLR method
        """ EqualsCore(self: Unit, other: Unit) -> bool """
        pass

    def GetConverter(self, to):
        """ GetConverter[TData](self: Unit, to: Unit) -> IUnitConverter[TData] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Unit) -> int """
        pass

    def GetHashCodeCore(self, *args): #cannot find CLR method
        """ GetHashCodeCore(self: Unit) -> int """
        pass

    def MatchStandardFormatArgument(self, *args): #cannot find CLR method
        """ MatchStandardFormatArgument[T](format: str, symbol: T, name: T, pluralName: T) -> T """
        pass

    def ToString(self, *__args):
        """
        ToString(self: Unit) -> str
        ToString(self: Unit, format: str) -> str
        ToString(self: Unit, formatProvider: IFormatProvider) -> str
        ToString(self: Unit, format: str, formatProvider: IFormatProvider) -> str
        """
        pass

    def ToStringCore(self, *args): #cannot find CLR method
        """ ToStringCore(self: Unit, format: str, formatProvider: IFormatProvider) -> str """
        pass

    def TryConvert(self, to, value, result):
        """ TryConvert[TData](self: Unit, to: Unit, value: TData) -> (bool, TData) """
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
    """Get: Name(self: Unit) -> str

"""

    PluralName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PluralName(self: Unit) -> str

"""

    Symbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Symbol(self: Unit) -> str

"""


    None = None


class ScientificUnit(Unit, IFormattable, IEquatable[Unit], IEquatable[ScientificUnit]):
    # no doc
    def ChangePrefix(self, prefix):
        """ ChangePrefix(self: ScientificUnit, prefix: SIPrefix) -> ScientificUnit """
        pass

    def CreateConverter(self, *args): #cannot find CLR method
        """ CreateConverter[TData](self: ScientificUnit, to: Unit) -> IUnitConverter[TData] """
        pass

    @staticmethod
    def Divide(left, right):
        """ Divide(left: ScientificUnit, right: ScientificUnit) -> ScientificUnit """
        pass

    def Equals(self, *__args):
        """ Equals(self: ScientificUnit, other: ScientificUnit) -> bool """
        pass

    def EqualsCore(self, *args): #cannot find CLR method
        """ EqualsCore(self: ScientificUnit, other: Unit) -> bool """
        pass

    def GetComponents(self):
        """ GetComponents(self: ScientificUnit) -> ReadOnlyCollection[ScientificUnit] """
        pass

    def GetFormula(self):
        """ GetFormula(self: ScientificUnit) -> ReadOnlyCollection[ScientificUnit] """
        pass

    def GetHashCodeCore(self, *args): #cannot find CLR method
        """ GetHashCodeCore(self: ScientificUnit) -> int """
        pass

    @staticmethod
    def Multiply(left, right):
        """ Multiply(left: ScientificUnit, right: ScientificUnit) -> ScientificUnit """
        pass

    @staticmethod
    def Parse(input, formatProvider=None):
        """
        Parse(input: str, formatProvider: IFormatProvider) -> ScientificUnit
        Parse(input: str) -> ScientificUnit
        """
        pass

    def RaiseToPower(self, power):
        """ RaiseToPower(self: ScientificUnit, power: RationalInt32) -> ScientificUnit """
        pass

    def ToStringCore(self, *args): #cannot find CLR method
        """ ToStringCore(self: ScientificUnit, format: str, formatProvider: IFormatProvider) -> str """
        pass

    @staticmethod
    def TryParse(input, *__args):
        """
        TryParse(input: str, formatProvider: IFormatProvider) -> (bool, ScientificUnit)
        TryParse(input: str) -> (bool, ScientificUnit)
        """
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

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(left: ScientificUnit, right: ScientificUnit) -> ScientificUnit """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(left: ScientificUnit, right: ScientificUnit) -> ScientificUnit """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsBaseUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBaseUnit(self: ScientificUnit) -> bool

"""

    IsNamedUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNamedUnit(self: ScientificUnit) -> bool

"""

    Power = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Power(self: ScientificUnit) -> RationalInt32

"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prefix(self: ScientificUnit) -> SIPrefix

"""


    Ampere = None
    Candela = None
    DegreeCelsius = None
    Hertz = None
    Joule = None
    Kelvin = None
    Kilogram = None
    Meter = None
    MeterPerSecond = None
    MeterPerSecondSquared = None
    Mole = None
    Newton = None
    Ohm = None
    One = None
    Pascal = None
    Radian = None
    Second = None
    Volt = None
    Watt = None


class ScopeComparison(Enum, IComparable, IFormattable, IConvertible):
    """ enum ScopeComparison, values: ContainedBy (3), Contains (2), Equals (0), Overlaps (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ContainedBy = None
    Contains = None
    Equals = None
    Overlaps = None
    value__ = None


class SequenceBufferPool(BufferPool):
    # no doc
    @staticmethod
    def CreateConstantBuffer(size, unit, value):
        """ CreateConstantBuffer[TData](size: int, unit: Unit, value: TData) -> Buffer[TData] """
        pass

    @staticmethod
    def CreateIntervalBuffer(size, unit, value, increment, stride=None):
        """
        CreateIntervalBuffer(size: int, unit: Unit, value: int, increment: int) -> Buffer[int]
        CreateIntervalBuffer(size: int, unit: Unit, value: int, increment: int, stride: int) -> Buffer[int]
        CreateIntervalBuffer(size: int, unit: Unit, value: float, increment: float) -> Buffer[float]
        CreateIntervalBuffer(size: int, unit: Unit, value: float, increment: float, stride: int) -> Buffer[float]
        CreateIntervalBuffer(size: int, unit: Unit, value: TimeSpan, increment: TimeSpan) -> Buffer[TimeSpan]
        CreateIntervalBuffer(size: int, unit: Unit, value: TimeSpan, increment: TimeSpan, stride: int) -> Buffer[TimeSpan]
        CreateIntervalBuffer(size: int, unit: Unit, value: DateTime, increment: TimeSpan) -> Buffer[DateTime]
        CreateIntervalBuffer(size: int, unit: Unit, value: DateTime, increment: TimeSpan, stride: int) -> Buffer[DateTime]
        CreateIntervalBuffer(size: int, unit: Unit, value: PrecisionTimeSpan, increment: PrecisionTimeSpan) -> Buffer[PrecisionTimeSpan]
        CreateIntervalBuffer(size: int, unit: Unit, value: PrecisionTimeSpan, increment: PrecisionTimeSpan, stride: int) -> Buffer[PrecisionTimeSpan]
        CreateIntervalBuffer(size: int, unit: Unit, value: PrecisionDateTime, increment: PrecisionTimeSpan) -> Buffer[PrecisionDateTime]
        CreateIntervalBuffer(size: int, unit: Unit, value: PrecisionDateTime, increment: PrecisionTimeSpan, stride: int) -> Buffer[PrecisionDateTime]
        CreateIntervalBuffer[(TData, TIncrement, TOperations)](size: int, unit: Unit, value: TData, increment: TIncrement, stride: int) -> Buffer[TData]
        """
        pass

    @staticmethod
    def TryCreateIntervalBuffer(size, unit, value, increment, stride=None):
        """
        TryCreateIntervalBuffer[(TData, TIncrement)](size: int, unit: Unit, value: TData, increment: TIncrement) -> Buffer[TData]
        TryCreateIntervalBuffer[(TData, TIncrement)](size: int, unit: Unit, value: TData, increment: TIncrement, stride: int) -> Buffer[TData]
        """
        pass


class SIPrefix(Enum, IComparable, IFormattable, IConvertible):
    """ enum SIPrefix, values: Atto (-18), Centi (-2), Deca (1), Deci (-1), Exa (18), Femto (-15), Giga (9), Hecto (2), Kilo (3), Mega (6), Micro (-6), Milli (-3), Nano (-9), None (0), Peta (15), Pico (-12), Tera (12), Yocto (-24), Yotta (24), Zepto (-21), Zetta (21) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Atto = None
    Centi = None
    Deca = None
    Deci = None
    Exa = None
    Femto = None
    Giga = None
    Hecto = None
    Kilo = None
    Mega = None
    Micro = None
    Milli = None
    Nano = None
    None = None
    Peta = None
    Pico = None
    Tera = None
    value__ = None
    Yocto = None
    Yotta = None
    Zepto = None
    Zetta = None


class TraitQueryOptions(object):
    """ TraitQueryOptions() """
    @staticmethod
    def CreateTrait():
        """ CreateTrait[TTrait]() -> TraitQueryOptions """
        pass

    @staticmethod
    def FindTrait(scope):
        """ FindTrait[TTrait](scope: TraitScope) -> TraitQueryOptions """
        pass

    @staticmethod
    def FindTraits(scope):
        """ FindTraits[TTrait](scope: TraitScope) -> TraitQueryOptions """
        pass

    def ToString(self):
        """ ToString(self: TraitQueryOptions) -> str """
        pass

    CreateMissingTraits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateMissingTraits(self: TraitQueryOptions) -> bool

Set: CreateMissingTraits(self: TraitQueryOptions) = value
"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scope(self: TraitQueryOptions) -> TraitScope

Set: Scope(self: TraitQueryOptions) = value
"""

    ScopeComparison = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScopeComparison(self: TraitQueryOptions) -> ScopeComparison

Set: ScopeComparison(self: TraitQueryOptions) = value
"""

    TraitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TraitType(self: TraitQueryOptions) -> Type

Set: TraitType(self: TraitQueryOptions) = value
"""



class TraitScope(object, IEquatable[TraitScope]):
    """
    TraitScope(sampleIndex: int)
    TraitScope(startIndex: int, length: int)
    """
    @staticmethod
    def Compare(left, right, scopeComparison):
        """ Compare(left: TraitScope, right: TraitScope, scopeComparison: ScopeComparison) -> bool """
        pass

    def Contains(self, *__args):
        """
        Contains(self: TraitScope, sampleIndex: int) -> bool
        Contains(self: TraitScope, scope: TraitScope) -> bool
        """
        pass

    @staticmethod
    def Cover(left, right):
        """ Cover(left: TraitScope, right: TraitScope) -> TraitScope """
        pass

    def Equals(self, *__args):
        """
        Equals(self: TraitScope, other: TraitScope) -> bool
        Equals(self: TraitScope, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TraitScope) -> int """
        pass

    @staticmethod
    def Intersect(left, right):
        """ Intersect(left: TraitScope, right: TraitScope) -> TraitScope """
        pass

    def Overlaps(self, scope):
        """ Overlaps(self: TraitScope, scope: TraitScope) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TraitScope) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[TraitScope]() -> TraitScope
        
        __new__(cls: type, sampleIndex: int)
        __new__(cls: type, startIndex: int, length: int)
        """
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

    EndIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndIndex(self: TraitScope) -> Nullable[int]

"""

    IsBufferScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBufferScope(self: TraitScope) -> bool

"""

    IsEmptyScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmptyScope(self: TraitScope) -> bool

"""

    IsStreamScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStreamScope(self: TraitScope) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: TraitScope) -> Nullable[int]

"""

    StartIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartIndex(self: TraitScope) -> Nullable[int]

"""


    BufferScope = None
    StreamScope = None


class TraitSet(object, ICollection[Trait], IEnumerable[Trait], IEnumerable):
    # no doc
    def Add(self, trait):
        """ Add(self: TraitSet, trait: Trait) -> bool """
        pass

    def Contains(self, trait):
        """ Contains(self: TraitSet, trait: Trait) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: TraitSet) -> IEnumerator[Trait] """
        pass

    def GetTraits(self, *__args):
        """
        GetTraits(self: TraitSet, query: TraitQueryOptions) -> IEnumerable[Trait]
        GetTraits(self: TraitSet, scope: TraitScope) -> IEnumerable[Trait]
        GetTraits[TTrait](self: TraitSet) -> IEnumerable[TTrait]
        GetTraits[TTrait](self: TraitSet, scope: TraitScope) -> IEnumerable[TTrait]
        """
        pass

    def Slice(self, scope, offset=None, preserveGlobalTraits=None, traitFilter=None):
        """
        Slice(self: TraitSet, scope: TraitScope) -> IEnumerable[Trait]
        Slice(self: TraitSet, scope: TraitScope, offset: int, preserveGlobalTraits: bool) -> IEnumerable[Trait]
        Slice(self: TraitSet, scope: TraitScope, offset: int, preserveGlobalTraits: bool, traitFilter: Func[Trait, Trait]) -> IEnumerable[Trait]
        """
        pass

    def ToString(self):
        """ ToString(self: TraitSet) -> str """
        pass

    def UnionWith(self, traits):
        """ UnionWith(self: TraitSet, traits: IEnumerable[Trait]) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[Trait], item: Trait) -> bool """
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


class TraitSetBuilder(object, ICollection[Trait], IEnumerable[Trait], IEnumerable):
    """
    TraitSetBuilder()
    TraitSetBuilder(traits: IEnumerable[Trait])
    """
    def Add(self, trait):
        """ Add(self: TraitSetBuilder, trait: Trait) """
        pass

    def AddRange(self, traits):
        """ AddRange(self: TraitSetBuilder, traits: IEnumerable[Trait]) """
        pass

    def Clear(self):
        """ Clear(self: TraitSetBuilder) """
        pass

    def Contains(self, trait):
        """ Contains(self: TraitSetBuilder, trait: Trait) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: TraitSetBuilder, array: Array[Trait], arrayIndex: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: TraitSetBuilder) -> IEnumerator[Trait] """
        pass

    def Remove(self, trait):
        """ Remove(self: TraitSetBuilder, trait: Trait) -> bool """
        pass

    def ToString(self):
        """ ToString(self: TraitSetBuilder) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[Trait], item: Trait) -> bool """
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
    def __new__(self, traits=None):
        """
        __new__(cls: type)
        __new__(cls: type, traits: IEnumerable[Trait])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: TraitSetBuilder) -> int

"""



class TryTransform(MulticastDelegate, ICloneable, ISerializable):
    """ TryTransform[TData, TResult](object: object, method: IntPtr) """
    def BeginInvoke(self, value, result, callback, object):
        """ BeginInvoke(self: TryTransform[TData, TResult], value: TData, callback: AsyncCallback, object: object) -> (IAsyncResult, TResult) """
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

    def EndInvoke(self, result, __result):
        """ EndInvoke(self: TryTransform[TData, TResult], __result: IAsyncResult) -> (bool, TResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, value, result):
        """ Invoke(self: TryTransform[TData, TResult], value: TData) -> (bool, TResult) """
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


class WritableBuffer(object, IIndicateDisposed, IDisposable, IList[TData], ICollection[TData], IEnumerable[TData], IEnumerable):
    # no doc
    def Contains(self, item):
        """ Contains(self: WritableBuffer[TData], item: TData) -> bool """
        pass

    def CopyTo(self, *__args):
        """ CopyTo(self: WritableBuffer[TData], destination: Array[TData], destinationIndex: int)CopyTo(self: WritableBuffer[TData], sourceIndex: int, destination: Array[TData], destinationIndex: int, length: int) """
        pass

    def Dispose(self):
        """ Dispose(self: WritableBuffer[TData]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: WritableBuffer[TData]) -> IEnumerator[TData] """
        pass

    def GetReadable(self):
        """ GetReadable(self: WritableBuffer[TData]) -> Buffer[TData] """
        pass

    def GetWritable(self):
        """ GetWritable(self: WritableBuffer[TData]) -> WritableBuffer[TData] """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: WritableBuffer[TData], item: TData) -> int """
        pass

    def MakeReadable(self):
        """ MakeReadable(self: WritableBuffer[TData]) -> Buffer[TData] """
        pass

    def ToString(self):
        """ ToString(self: WritableBuffer[TData]) -> str """
        pass

    def Transform(self, transformer, unit, traits):
        """
        Transform[TResult](self: WritableBuffer[TData], transformer: Func[TData, TResult], unit: Unit, traits: IEnumerable[Trait]) -> Buffer[TResult]
        Transform[TResult](self: WritableBuffer[TData], transformer: Func[TData, int, TResult], unit: Unit, traits: IEnumerable[Trait]) -> Buffer[TResult]
        """
        pass

    def TransformInline(self, *__args):
        """ TransformInline(self: WritableBuffer[TData], unit: Unit)TransformInline(self: WritableBuffer[TData], transformer: Func[TData, TData])TransformInline(self: WritableBuffer[TData], transformer: Func[TData, int, TData]) """
        pass

    def TryGetArrayIndexer(self):
        """ TryGetArrayIndexer(self: WritableBuffer[TData]) -> Nullable[ArrayDataStoreIndexer] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """
        __contains__(self: ICollection[TData], item: TData) -> bool
        
            Determines whether the System.Collections.Generic.ICollection contains a specific value.
        
            item: The object to locate in the System.Collections.Generic.ICollection.
            Returns: ue if item is found in the System.Collections.Generic.ICollection; otherwise, lse.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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

    def __str__(self, *args): #cannot find CLR method
        pass

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: WritableBuffer[TData]) -> Type

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: WritableBuffer[TData]) -> bool

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: WritableBuffer[TData]) -> int

"""

    Traits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Traits(self: WritableBuffer[TData]) -> TraitSetBuilder

"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit(self: WritableBuffer[TData]) -> Unit

Set: Unit(self: WritableBuffer[TData]) = value
"""


    ArrayDataStoreIndexer = None


# variables with complex values

