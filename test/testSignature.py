from unittest.case import TestCase
from ECDSA import ECDSA, PrivateKey, Signature


class SignatureTest(TestCase):

    def testDerConversion(self):
        privateKey = PrivateKey()
        message = "This is a text message"

        signature1 = ECDSA.sign(message, privateKey)

        der = signature1.toDer()
        signature2 = Signature.fromDer(der)

        self.assertEqual(signature1.r, signature2.r)
        self.assertEqual(signature1.s, signature2.s)

    def testBase64Conversion(self):
        privateKey = PrivateKey()
        message = "This is a text message"

        signature1 = ECDSA.sign(message, privateKey)
        print("Signature1 in Base64:"+signature1.toBase64())

        base64 = signature1.toBase64()

        signature2 = Signature.fromBase64(base64)
        print("Signature2 in Base64:" + signature2.toBase64())

        self.assertEqual(signature1.r, signature2.r)
        self.assertEqual(signature1.s, signature2.s)
