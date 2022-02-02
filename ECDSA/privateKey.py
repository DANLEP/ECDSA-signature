from random import SystemRandom
from .math import Math
from .curve import secp256k1
from .publicKey import PublicKey
from .utils.binary import hexFromInt, intFromHex


class PrivateKey:

    def __init__(self, curve=secp256k1, secret=None):
        self.curve = curve
        self.secret = secret or SystemRandom().randrange(1, curve.N)

    def publicKey(self):
        curve = self.curve
        publicPoint = Math.multiply(
            p=curve.G,
            n=self.secret,
            N=curve.N,
            A=curve.A,
            P=curve.P
        )
        return PublicKey(point=publicPoint, curve=curve)

    def toString(self):
        return hexFromInt(self.secret)

    @classmethod
    def fromString(cls, string, curve=secp256k1):
        return PrivateKey(secret=intFromHex(string), curve=curve)
