USER_NOT_FOUND = "USER_NOT_FOUND"
TOKEN_AUTHENTICATION_FAILED = "TOKEN_AUTHENTICATION_FAILED"
USERNAME_TAKEN = "USERNAME_TAKEN"
INVALID_BET = "INVALID_BET"
INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
REQUEST_MAXIMUM_LENGTH_EXCEEDED = "REQUEST_MAXIMUM_LENGTH_EXCEEDED"
UNKNOWN_ERROR_OCCURRED = "UNKNOWN_ERROR_OCCURRED"
TYPE_VALIDATION_ERROR = "TYPE_VALIDATION_ERROR"
MISSING_AUTHENTICATION_TOKEN = "MISSING_AUTHENTICATION_TOKEN"
MISSING_FIELD_VALUES = "MISSING_FIELD_VALUES"
MALFORMED_REQUEST_ERROR = "MALFORMED_REQUEST_ERROR"
QR_NOT_FOUND_ERROR = "QR_NOT_FOUND_ERROR"


class UserNotFoundError(Exception):
    """Exception raised when no users be found when querrying a database"""

    pass


class UsernameNotUniqueError(Exception):
    """Exception raised when a non-unique username is added to the database"""

    pass


class InvalidCredentialsError(Exception):
    """Exception raised when users attempt to log in with invalid credentials"""

    pass


class MissingAuthenticationTokenError(Exception):
    """Exception raised when users are missing an authentication token"""

    pass


class InvalidAuthenticationTokenError(Exception):
    """Exception raised when users use an invalid authentication token"""

    pass


class InvalidUserQueryError(Exception):
    """Exception raised for invalid query to the user database table"""

    pass


class TypeErrorUndefined(Exception):
    pass


class QRNotFoundError(Exception):
    """Exception raised when the queried SURVEY cannot be found in the database"""

    pass

