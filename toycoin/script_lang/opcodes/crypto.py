from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD160
from Crypto.Signature import DSS
from Crypto.PublicKey import ECC
from toycoin.util import keypub_to_keypubhash
from binascii import hexlify, unhexlify

class Crypto_Mixin(object):
    
    def OP_RIPEMD160(self):
        pass

    def OP_SHA1(self):
        pass

    def OP_SHA256(self):
        pass

    def OP_HASH160(self):
        key_pub = self.stack.pop()
        key_pub_hash = keypub_to_keypubhash(key_pub)
        self.stack.append(key_pub_hash)

    def OP_HASH256(self):
        pass

    def OP_CODESEPARATOR(self):
        pass

    def OP_CHECKSIG(self):
        key_pub = unhexlify(self.stack.pop())
        sig = self.stack.pop()
        key = ECC.import_key(key_pub)
        h = SHA256.new(key_pub)
        verifier = DSS.new(key, 'fips-186-3')
        try:
            verifier.verify(h, sig)
            return True
        except ValueError:
            return False

    def OP_CHECKSIGVERIFY(self):
        pass


    def OP_CHECKMULTISIG(self):
        pass
    
    def OP_CHECKMULTISIGVERIFY(self):
        pass
