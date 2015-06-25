#!/user/bin/python
"""
"""
import re

from .errors import InvalidVersionString

class SemanticVersion(object):
    """
    Three-element semantic version (MAJOR.MINOR.PATCH), with optional prefix.
    """
    REGEX = re.compile(r'^([^\d]+)?(\d+).(\d+).(\d+)$', flags=0)
    DEFAULTS = {
        'prefix': "v"
    }

    prefix = None  # @type: str
    major = None  # @type: int
    minor = None  # @type: int
    patch = None  # @type: int

    def __str__(self):
        return str.format(
            "{prefix}{major}.{minor}.{patch}",
            prefix=self.prefix,
            major=self.major,
            minor=self.minor,
            patch=self.patch
        )

    def __repr__(self):
        return str.format(
            "{name}({major}, {minor}, {patch}, prefix='{prefix}')",
            name=type(self).__name__,
            prefix=self.prefix,
            major=self.major,
            minor=self.minor,
            patch=self.patch
        )

    @classmethod
    def is_valid_string(cls, raw):
        return bool(re.match(cls.REGEX, raw, flags=0))

    @classmethod
    def validate_string(cls, raw):
        if not cls.is_valid_string(raw):
            raise InvalidVersionString(
                "Invalid version string. Should match '{prefix}{major}.{minor}.{patch}'")
        return raw

    def __new__(cls, *positional, **keywords):
        """Dispatches over two possible constructors.
        ... this would probably be simpler to just modify the arguments
        and always feed into __init__
        """
        if len(positional) == 1 and len(keywords) == 0:
            return cls.from_string(*positional)
        elif 3 <= len(positional) <= 4:
            return cls.from_explicit(*positional, **keywords)

    @classmethod
    def from_string(cls, raw):
        """Constructor. Extracts version numbers, and defers to cls.from_explicit"""
        raw = cls.validate_string(raw)
        prefix, major, minor, patch = cls.REGEX.match(raw).groups()
        return cls.from_explicit(major, minor, patch, prefix=prefix)

    @classmethod
    def from_explicit(cls, major, minor, patch, prefix=None):
        """Constructor."""
        self = object.__new__(cls)
        self.init(major, minor, patch, prefix=prefix)
        return self

    def init(self, major, minor, patch, prefix=None):
        """
        Note: We are not using __init__, because we don't want it to be automatically
        called AFTER __new__ (which Python does by default, using the arguments passed
        to __new__ - which causes issues since we want two distinct constructors).
        """
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch)
        if prefix is None:
            prefix = self.DEFAULTS['prefix']
        self.prefix = prefix

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        elif isinstance(other, SemanticVersion):
            return all([
                self.major == other.major,
                self.minor == other.minor,
                self.patch == other.patch,
                self.prefix == other.prefix
            ])
        else:
            return False
