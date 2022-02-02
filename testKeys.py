from ECDSA.privateKey import PrivateKey

#generate private key
privateKey1 = PrivateKey()
string = privateKey1.toString()
print("PrivateKey: " + string + "\nPublicKey: " + privateKey1.publicKey().toString()+"\n")

#import private key
privateKey2 = PrivateKey().fromString(string)
print("PrivateKey2: " + privateKey2.toString() + "\nPublicKey2: " + privateKey2.publicKey().toString()+"\n")