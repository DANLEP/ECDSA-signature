from .curve import secp256k1, Point
from .math import Math
from .utils.binary import hexFromInt, intFromHex


class PublicKey:

    def __init__(self, point, curve):
        self.point = point
        self.curve = curve

    def toString(self):
        baseLength = 2 * self.curve.length()
        xHex = hexFromInt(self.point.x).zfill(baseLength)
        yHex = hexFromInt(self.point.y).zfill(baseLength)
        string = xHex + yHex
        return string

    @classmethod
    def fromString(cls, string, curve=secp256k1, validatePoint=True):
        baseLength = 2 * curve.length()
        if len(string) > 2 * baseLength and string[:4] == "0004":
            string = string[4:]

        xs = string[:baseLength]
        ys = string[baseLength:]

        p = Point(
            x=intFromHex(xs),
            y=intFromHex(ys)
        )
        publicKey = PublicKey(point=p, curve=curve)
        if not validatePoint:
            return publicKey
        if p.isAtInfinity():
            raise Exception("Public key point is at infinity")
        if not curve.contains(p):
            raise Exception("Point ({x},{y}) is not valid for curve {name}".format(x=p.x, y=p.y, name=curve.name))
        if not Math.multiply(p=p, n=curve.N, N=curve.N, A=curve.A, P=curve.P).isAtInfinity():
            raise Exception("Point ({x},{y}) * {name}.N is not at infinity".format(x=p.x, y=p.y, name=curve.name))
        return publicKey
