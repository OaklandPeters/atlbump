#!/user/bin/python
"""
"""

class BumpException(Exception):
    """Base exception type for the Bump module"""
    pass


class InvalidVersionString(BumpException, ValueError):
    pass
