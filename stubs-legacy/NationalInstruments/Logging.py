# encoding: utf-8
# module NationalInstruments.Logging calls itself Logging
# from NationalInstruments.Common, Version=19.0.40.49152, Culture=neutral, PublicKeyToken=dc6ad606294fc298
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ILoggerRegistration(IDisposable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsRegistered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRegistered(self: ILoggerRegistration) -> bool

"""

    Logger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Logger(self: ILoggerRegistration) -> NILoggerBase

"""

    MinimumLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumLevel(self: ILoggerRegistration) -> NILogMessageLevel

"""



class NILoggerBase(MarshalByRefObject):
    # no doc
    def LogCore(self, *args): #cannot find CLR method
        """ LogCore(self: NILoggerBase, message: NILogMessage) """
        pass

    def OnRegister(self, *args): #cannot find CLR method
        """ OnRegister(self: NILoggerBase, minimumLevel: NILogMessageLevel) """
        pass

    def OnUnregister(self, *args): #cannot find CLR method
        """ OnUnregister(self: NILoggerBase, minimumLevel: NILogMessageLevel) """
        pass

    @staticmethod
    def Register(logger, minimumLevel):
        """ Register(logger: NILoggerBase, minimumLevel: NILogMessageLevel) -> ILoggerRegistration """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, categoryFilter: Func[str, bool])
        __new__(cls: type)
        """
        pass

    CategoryFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CategoryFilter(self: NILoggerBase) -> Func[str, bool]

"""



class NILogMessage(object):
    # no doc
    def ToString(self):
        """ ToString(self: NILogMessage) -> str """
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Category(self: NILogMessage) -> str

"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Level(self: NILogMessage) -> NILogMessageLevel

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: NILogMessage) -> str

"""

    ThreadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThreadId(self: NILogMessage) -> int

"""

    TimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TimeStamp(self: NILogMessage) -> DateTimeOffset

"""



class NILogMessageLevel(Enum, IComparable, IFormattable, IConvertible):
    """ enum NILogMessageLevel, values: Error (3), Info (1), Verbose (0), Warning (2) """
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

    Error = None
    Info = None
    value__ = None
    Verbose = None
    Warning = None


