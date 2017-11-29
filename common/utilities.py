import bcrypt
from enum import Enum, unique
from time import time, struct_time, gmtime, strftime


class TimeUtils:
    """
    Utilities for converting and displaying time.
    """
    @staticmethod
    def now() -> int:
        """
        Return the current time (tz-naive), expressed in seconds
        """
        return int(time())
    
    @staticmethod
    def time_from_seconds(seconds: int = None) -> struct_time:
        """
        Parse a time in seconds into a tz-naive time.struct_time class and return it.
        :param seconds: The number of seconds since the epoch, or None for current time.
        :return: A time.struct_time object built from the param seconds.
        """
        return gmtime(seconds)
        
    @staticmethod
    def time_string_from_seconds(seconds: int = None) -> str:
        """
        Get a time in seconds as a string in format 
        :param seconds: The number of seconds since the epoch, or None for current time.
        :return: A string in the format 'Thu, 28 Jun 2020 14:17:15'
        """
        return strftime("%a, %d %b %Y %H:%M:%S", gmtime(seconds))


class AuthUtils:
    
    @staticmethod
    def hash_password(plaintext_pw: str) -> str:
        """
        Returns a salted hashed password generated from the plaintext input.
        :param plaintext_pw: The password to hash as a string
        :return: A hashed password as a string
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(plaintext_pw, salt)

    @staticmethod
    def check_password(plaintext_pw: str, hashed_pw: str) -> bool:
        """
        Check to see if, when hashed, the given plaintext password matches the user's stored password.
        :param plaintext_pw: The plaintext password the user provided, as a string.
        :param hashed_pw: The hashed password to check against, as a string.
        :return: True if the passwords match, false otherwise.
        """
        return bcrypt.hashpw(plaintext_pw, hashed_pw) == hashed_pw


@unique
class DBFields(Enum):
    """
    An enum mapping readable database field names to the fields that are actually stored.
    In order to scale our document store vertically, we want to reduce the size of the keys 
    in the key/value pairs whenever possible. This allows us to do that without sacrificing readability.
    """
    username = 'u'
    password = 'p'
    email = 'e'
    first_name = 'fn'
    last_name = 'ln'
    created = 'c'
    bio = 'b'
