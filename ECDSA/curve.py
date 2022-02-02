class Curve:
    def __init__(self, A, B, P, N, Gx, Gy):
        self.A = A
        self.B = B
        self.P = P
        self.N = N
        self.G = Point(Gx, Gy)

    def contains(self, p):
        #if the point p is on the curve
        if not 0 <= p.x <= self.P - 1:
            return False
        if not 0 <= p.y <= self.P - 1:
            return False
        if (p.y ** 2 - (p.x ** 3 + self.A * p.x + self.B)) % self.P != 0:
            return False
        return True
    def length(self):
        return (1 + len("%x" % self.N)) // 2

class Point:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({x}, {y}, {z})".format(x=self.x, y=self.y, z=self.z)

    def isAtInfinity(self):
        return self.y == 0

secp256k1 = Curve(
    A=0x0000000000000000000000000000000000000000000000000000000000000000,
    B=0x0000000000000000000000000000000000000000000000000000000000000007,
    P=0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
    N=0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
    Gx=0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    Gy=0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
)