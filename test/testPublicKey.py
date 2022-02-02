from unittest.case import TestCase
from ECDSA.privateKey import PrivateKey
from ECDSA.publicKey import PublicKey
from ECDSA.utils.compatibility import *


class PublicKeyTest(TestCase):

    def testPemConversion(self):
        privateKey = PrivateKey()
        publicKey1 = privateKey.publicKey()
        pem = publicKey1.toPem()
        print("PublicKey1 in pem:"+pem)
        publicKey2 = PublicKey.fromPem(pem)
        print("PublicKey2 in pem:" + publicKey2.toPem())
        self.assertEqual(publicKey1.point.x, publicKey2.point.x)
        self.assertEqual(publicKey1.point.y, publicKey2.point.y)
        self.assertEqual(publicKey1.curve, publicKey2.curve)

    def testDerConversion(self):
        privateKey = PrivateKey()
        publicKey1 = privateKey.publicKey()
        der = publicKey1.toDer()
        publicKey2 = PublicKey.fromDer(der)
        self.assertEqual(publicKey1.point.x, publicKey2.point.x)
        self.assertEqual(publicKey1.point.y, publicKey2.point.y)
        self.assertEqual(publicKey1.curve, publicKey2.curve)

    def testStringConversion(self):
        privateKey = PrivateKey()
        publicKey1 = privateKey.publicKey()
        string = publicKey1.toString()
        print("PublicKey in string:" + string)
        publicKey2 = PublicKey.fromString(toBytes(string))
        self.assertEqual(publicKey1.point.x, publicKey2.point.x)
        self.assertEqual(publicKey1.point.y, publicKey2.point.y)
        self.assertEqual(publicKey1.curve, publicKey2.curve)
