from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256, RIPEMD160
from Crypto.Signature import DSS
from abc import abstractmethod
from functools import partial
import base58
import json
from toycoin import util

class Wallet(object):

    def __init__(self, io_module):
        self.keypairs = []
        self.transactions = []
        self.set_serializable_module(io_module)

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            False
        other_addresses = other.get_keypairs()
        self_addresses = self.get_keypairs()
        for address in self_addresses:
            if address not in other_addresses:
                return False
        return True
    
    def new_keypair(self):
        key = ECC.generate(curve='P-256')
        pub = key.public_key()
        self.keypairs.append({
            'key': key,
            'key_pub': pub
        })        

    def get_keypairs(self):
        result = []
        for keypair in self.keypairs:
            key_pub = keypair['key_pub'].export_key(format='DER')
            result.append(util.keypub_to_address(key_pub))
        return result

    def create_sig(self, key, key_pub):
        signer = DSS.new(key, 'fips-186-3', encoding='der')
        msg = SHA256.new(key_pub.encode())
        return signer.sign(msg)

    def set_serializable_module(self, io_module):
        if io_module is None:
            self.serialize = self.serialize_nop
        else:
            self.serialize = partial(io_module.serialize, self)

    def serialize_nop(self):
        pass


class Wallet_IO(object):
    @abstractmethod
    def serialize(self, wallet):
        pass
    
    @staticmethod
    def deserialize(object):
        pass

class Wallet_as_Json(Wallet_IO):
    
    def serialize(self, wallet):
        json_file = {}
        wallet_json = []
        for address in wallet.keypairs:
            wallet_json.append(self._address_to_json(address))
        json_file['keypairs'] = wallet_json
        return json.dumps(json_file, sort_keys=True, indent=4)

    def _address_to_json(self, key):
        address_json = {}
        key_pub = key['key_pub'].export_key(format='DER')
        address_json['key'] = key['key'].export_key(format='DER').hex()
        address_json['key_pub'] = key_pub.hex()
        address_json['address'] = util.keypub_to_address(
            key_pub).decode('utf-8')
        return address_json
    
    @staticmethod
    def deserialize(json_string):
        data = json.loads(json_string)
        wallet = Wallet(Wallet_as_Json())
        addresses = []
        for address_object in data['keypairs']:
            byte_string = bytearray.fromhex(address_object['key'])
            key = ECC.import_key(bytes(byte_string))
            pub = key.public_key()
            addresses.append({
                'key': key,
                'key_pub': pub
            })
        wallet.keypairs = addresses
        return wallet
