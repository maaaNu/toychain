from Crypto.PublicKey import ECC
from Crypto.Hash import SHA1

class Wallet(object):

    def __init__(self):
        self.adresses = []
    

    def new_adress(self):
        key = ECC.generate(curve='P-256')
        pub = key.public_key()
        self.adresses.append({
            'key': key,
            'key_pub': pub
        })

    def get_adresses(self):
        result = []
        for adress in self.adresses:
            key_pub = adress['key_pub'].export_key(format='DER')
            result.append(SHA1.new(key_pub))
        return result