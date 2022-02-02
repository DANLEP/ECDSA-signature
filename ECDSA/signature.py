from .utils.binary import byteStringFromHex
from .utils.der import encodeConstructed, encodePrimitive, DerFieldType, parse


class Signature:

    def __init__(self, r, s):
        self.r = r
        self.s = s

    def _toString(self):
        return encodeConstructed(
            encodePrimitive(DerFieldType.integer, self.r),
            encodePrimitive(DerFieldType.integer, self.s),
        )

    @classmethod
    def _fromString(cls, string, recoveryId=None):
        r, s = parse(string)[0]
        return Signature(r=r, s=s, recoveryId=recoveryId)