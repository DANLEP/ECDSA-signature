from unittest.case import TestCase
from ECDSA.privateKey import PrivateKey

class PrivateKeyTest(TestCase):

    def testPemConversion(self):
        privateKey1 = PrivateKey()
        pem = privateKey1.toPem()
        print("PrivateKey1 in pem: " + pem)
        privateKey2 = PrivateKey.fromPem(pem)
        print("PrivateKey2 in pem: " + privateKey2.toPem())
        self.assertEqual(privateKey1.secret, privateKey2.secret)
        self.assertEqual(privateKey1.curve, privateKey2.curve)

    def testDerConversion(self):
        privateKey1 = PrivateKey()
        der = privateKey1.toDer()
        privateKey2 = PrivateKey.fromDer(der)
        self.assertEqual(privateKey1.secret, privateKey2.secret)
        self.assertEqual(privateKey1.curve, privateKey2.curve)

    def testStringConversion(self):
        privateKey1 = PrivateKey()
        string = privateKey1.toString()
        print("PrivateKey1 in string: "+string)
        privateKey2 = PrivateKey.fromString(string)
        print("PrivateKey2 in string: " + privateKey2.toString())
        self.assertEqual(privateKey1.secret, privateKey2.secret)
        self.assertEqual(privateKey1.curve, privateKey2.curve)