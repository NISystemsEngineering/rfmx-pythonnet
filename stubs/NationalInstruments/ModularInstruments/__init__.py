# encoding: utf-8
# module NationalInstruments.ModularInstruments calls itself ModularInstruments
# from NationalInstruments.ModularInstruments.Common, Version=19.0.45.49152, Culture=neutral, PublicKeyToken=4febd62461bf11a4
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AdvancedPropertyAccessService(object):
    """ AdvancedPropertyAccessService(advancedPropertyAccessServiceImplBase: AdvancedPropertyAccessServiceImplBase) """
    def GetAttributeBoolean(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeBoolean(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> bool
        GetAttributeBoolean(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> bool
        """
        pass

    def GetAttributeDouble(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeDouble(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> float
        GetAttributeDouble(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> float
        """
        pass

    def GetAttributeInt32(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeInt32(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> int
        GetAttributeInt32(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> int
        """
        pass

    def GetAttributeInt64(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeInt64(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> Int64
        GetAttributeInt64(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> Int64
        """
        pass

    def GetAttributeInteger(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeInteger(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> Int64
        GetAttributeInteger(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> Int64
        """
        pass

    def GetAttributeSession(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeSession(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> IntPtr
        GetAttributeSession(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> IntPtr
        """
        pass

    def GetAttributeString(self, attributeIdentifier, repeatedCapability=None):
        """
        GetAttributeString(self: AdvancedPropertyAccessService, attributeIdentifier: Int64) -> str
        GetAttributeString(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str) -> str
        """
        pass

    def SetAttributeBoolean(self, attributeIdentifier, *__args):
        """ SetAttributeBoolean(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: bool)SetAttributeBoolean(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: bool) """
        pass

    def SetAttributeDouble(self, attributeIdentifier, *__args):
        """ SetAttributeDouble(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: float)SetAttributeDouble(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: float) """
        pass

    def SetAttributeInt32(self, attributeIdentifier, *__args):
        """ SetAttributeInt32(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: int)SetAttributeInt32(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: int) """
        pass

    def SetAttributeInt64(self, attributeIdentifier, *__args):
        """ SetAttributeInt64(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: Int64)SetAttributeInt64(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: Int64) """
        pass

    def SetAttributeInteger(self, attributeIdentifier, *__args):
        """ SetAttributeInteger(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: Int64)SetAttributeInteger(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: Int64) """
        pass

    def SetAttributeSession(self, attributeIdentifier, *__args):
        """ SetAttributeSession(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: IntPtr)SetAttributeSession(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: IntPtr) """
        pass

    def SetAttributeString(self, attributeIdentifier, *__args):
        """ SetAttributeString(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, value: str)SetAttributeString(self: AdvancedPropertyAccessService, attributeIdentifier: Int64, repeatedCapability: str, value: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, advancedPropertyAccessServiceImplBase):
        """ __new__(cls: type, advancedPropertyAccessServiceImplBase: AdvancedPropertyAccessServiceImplBase) """
        pass


class ITClockSynchronizableDevice:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: ITClockSynchronizableDevice) -> HandleRef

"""



class ModularInstrumentsException(Exception, ISerializable, _Exception):
    """
    ModularInstrumentsException()
    ModularInstrumentsException(message: str)
    ModularInstrumentsException(message: str, innerException: Exception)
    ModularInstrumentsException(message: str, error: int)
    ModularInstrumentsException(message: str, error: int, innerException: Exception)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: ModularInstrumentsException, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, error: int)
        __new__(cls: type, message: str, error: int, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Error(self: ModularInstrumentsException) -> int

"""


    SerializeObjectState = None


class ModularInstrumentsWarning(object):
    # no doc
    SynchronizeCallbacks = True
    Warning = None
    __all__ = [
        'Warning',
    ]


class ModularInstrumentsWarningEventArgs(EventArgs):
    """ ModularInstrumentsWarningEventArgs(errorCode: int, message: str) """
    def ToString(self):
        """ ToString(self: ModularInstrumentsWarningEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, errorCode, message):
        """ __new__(cls: type, errorCode: int, message: str) """
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorCode(self: ModularInstrumentsWarningEventArgs) -> int

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ModularInstrumentsWarningEventArgs) -> str

"""



class ModularInstrumentsWarningEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ ModularInstrumentsWarningEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ModularInstrumentsWarningEventHandler, sender: object, e: ModularInstrumentsWarningEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
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
        """ EndInvoke(self: ModularInstrumentsWarningEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModularInstrumentsWarningEventHandler, sender: object, e: ModularInstrumentsWarningEventArgs) """
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


