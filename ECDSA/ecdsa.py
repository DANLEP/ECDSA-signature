from hashlib import sha256
from binascii import hexlify
from random import SystemRandom

from .math import Math
from .signature import Signature


class ECDSA:

    @classmethod
    def sign(cls, message, privateKey, hashfunc=sha256):
        byteMessage = hashfunc(message.encode("utf-8")).digest()
        numberMessage = int((hexlify(byteMessage)).decode("utf-8"), 16)
        curve = privateKey.curve

        r, s, randSignPoint = 0, 0, None
        while r == 0 or s == 0:
            randNum = SystemRandom().randrange(1, curve.N)
            randSignPoint = Math.multiply(curve.G, n=randNum, A=curve.A, P=curve.P, N=curve.N)
            r = randSignPoint.x % curve.N
            s = ((numberMessage + r * privateKey.secret) * (Math.inv(randNum, curve.N))) % curve.N

        return Signature(r=r, s=s)

    @classmethod
    def verify(cls, message, signature, publicKey, hashfunc=sha256):
        byteMessage = hashfunc(message.encode("utf-8")).digest()
        numberMessage = int((hexlify(byteMessage)).decode("utf-8"), 16)
        curve = publicKey.curve
        r = signature.r
        s = signature.s
        if not 1 <= r <= curve.N - 1:
            return False
        if not 1 <= s <= curve.N - 1:
            return False
        inv = Math.inv(s, curve.N)
        u1 = Math.multiply(curve.G, n=(numberMessage * inv) % curve.N, N=curve.N, A=curve.A, P=curve.P)
        u2 = Math.multiply(publicKey.point, n=(r * inv) % curve.N, N=curve.N, A=curve.A, P=curve.P)
        v = Math.add(u1, u2, A=curve.A, P=curve.P)
        if v.isAtInfinity():
            return False
        return v.x % curve.N == r
