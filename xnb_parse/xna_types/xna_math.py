"""
math types
"""

from collections import namedtuple


# pylint: disable-msg=E1001,W0232,E1101
#noinspection PyClassicStyleClass,PyOldStyleClasses,PyUnresolvedReferences
class Color(namedtuple('Color', ['r', 'g', 'b', 'a'])):
    __slots__ = ()

    def to_packed(self):
        return (self.r & 0xff) | ((self.g & 0xff) << 8) | ((self.b & 0xff) << 16) | ((self.a & 0xff) << 24)

    @staticmethod
    def from_packed(data):
        r = (data >> 0) & 0xff
        g = (data >> 8) & 0xff
        b = (data >> 16) & 0xff
        a = (data >> 24)
        return Color(r, g, b, a)
