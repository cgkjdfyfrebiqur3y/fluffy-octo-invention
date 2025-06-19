"""Custom exceptions for development and feature control."""
class BaseDataTypesException(Exception):
    pass

class BaseDataTypesWarning(Warning):
    pass

class WriteOnlyReadError(BaseDataTypesException):
    pass

class ImportDisabledError(ImportError):
    """Raised when attempting to import a disabled feature."""
    pass

class ImportDisabledWarning(ImportWarning):
    """Warning issued when attempting to import a disabled feature."""
    pass

class NotDevError(BaseDataTypesException):
    """Raised when attempting to access development-only features."""
    pass

class DevKeyError(BaseDataTypesException):
    """Base exception for development key related errors."""
    pass

class InvalidDevKeyError(DevKeyError):
    """Base exception for invalid development key errors."""
    pass

class KeyNotActivatedError(InvalidDevKeyError):
    """Raised when the development key has not been activated."""
    pass

class KeyNotAuthorized(KeyNotActivatedError):
    """Raised when the development key is not authorized."""
    pass

class KeyLockedError(InvalidDevKeyError):
    """Base exception for locked key errors."""
    pass

class KeyUserLocked(KeyLockedError):
    """Raised when the key is locked by the user."""
    pass

class KeyAdminLocked(KeyLockedError):
    """Raised when the key is locked by an administrator."""
    pass

class KeyExpiredError(InvalidDevKeyError):
    """Raised when the development key has expired."""
    pass

class KeyNotReadyError(InvalidDevKeyError):
    """Raised when the development key is not ready for use."""
    pass

class IndevError(BaseDataTypesException):
    """Base exception for in-development related errors."""
    pass

class TestCaseFailedError(IndevError):
    """Raised when a test case fails during development."""
    pass

class IndevWarning(BaseDataTypesWarning):
    """Base warning for in-development related issues."""
    pass

class VersionIsIndevWarning(IndevWarning):
    """Warning issued when using an in-development version."""
    pass

class VersionIsIndevError(IndevError):
    """Raised when attempting to use an in-development version in production."""
    pass

class DepractedError(BaseDataTypesException):
    """Raised when using deprecated features."""
    pass

class CircularListIndexError(BaseDataTypesException):
    pass