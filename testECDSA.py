from ECDSA.privateKey import PrivateKey
from ECDSA.ecdsa import ECDSA

privateKey = PrivateKey()
publicKey = privateKey.publicKey()
print("PrivateKey: " + privateKey.toString())
print("PublicKey: " + publicKey.toString())

message = "Hello world!"
print("Message: " + message)

signature = ECDSA.sign(message,privateKey)
print("Signature: " + signature._toString())

if ECDSA.verify(message, signature, publicKey):
    print("Text signed!")
else:
    print("This text was not signed!")