from unittest.case import TestCase
from ECDSA import ECDSA, PrivateKey, Signature


class EcdsaTest(TestCase):

    def testVerifyRightMessage(self):
        privateKey = PrivateKey()
        publicKey = privateKey.publicKey()

        message = "This is the right message"

        signature = ECDSA.sign(message, privateKey)

        self.assertTrue(ECDSA.verify(message, signature, publicKey))

    def testVerifyWrongMessage(self):
        privateKey = PrivateKey()
        publicKey = privateKey.publicKey()

        message1 = "This is the right message"
        message2 = "This is the wrong message"

        signature = ECDSA.sign(message1, privateKey)

        self.assertFalse(ECDSA.verify(message2, signature, publicKey))

    def testZeroSignature(self):
        privateKey = PrivateKey()
        publicKey = privateKey.publicKey()

        message2 = "This is the wrong message"

        self.assertFalse(ECDSA.verify(message2, Signature(0, 0), publicKey))
