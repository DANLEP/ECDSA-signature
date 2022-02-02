from .point import Point

class CurveFp:

    def __init__(self, A, B, P, N, Gx, Gy, name, oid, nistName=None):
        self.A = A
        self.B = B
        self.P = P
        self.N = N
        self.G = Point(Gx, Gy)
        self.name = name
        self.nistName = nistName
        self.oid = oid

    def contains(self, p):
        #if the point p is on the curve
        if not 0 <= p.x <= self.P -1:
            return False
        if not 0 <= p.y <= self.P -1:
            return False
        if (p.y**2 - (p.x**3 + self.A * p.x + self.B)) % self.P != 0:
            return False
        return True

    def length(self):
        return (1 + len("%x" % self.N)) // 2


#y^2 = x^3 + 0*x + 7 (mod 115792089237316195423570985008687907853269984665640564039457584007908834671663)
secp256k1 = CurveFp(
    name="secp256k1",
    A=0x0000000000000000000000000000000000000000000000000000000000000000,
    B=0x0000000000000000000000000000000000000000000000000000000000000007,
    P=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    N=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    Gx=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    Gy=0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
    oid=[1, 3, 132, 0, 10]
)

supportedCurves = [secp256k1]

_curvesByOid = {tuple(curve.oid): curve for curve in supportedCurves}

def getCurveByOid(oid):
    if oid not in _curvesByOid:
        raise Exception("Unknown curve")
    return _curvesByOid[oid]