from Crypto.PublicKey import ECC
from Crypto.Hash import SHA1
from abc import abstractmethod
from functools import partial
import json

class Wallet(object):

    def __init__(self, io_module):
        self.addresses = []
        self.transactions = []
        self.set_serializable_module(io_module)

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            False
        other_addresses = other.get_addresses()
        self_addresses = self.get_addresses()
        for address in self_addresses:
            if address not in other_addresses:
                return False
        return True
            
    
    def new_address(self):
        key = ECC.generate(curve='P-256')
        pub = key.public_key()
        self.addresses.append({
            'key': key,
            'key_pub': pub
        })

    def get_addresses(self):
        result = []
        for address in self.addresses:
            key_pub = address['key_pub'].export_key(format='DER')
            result.append(SHA1.new(key_pub).hexdigest())
        return result

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
        addresses_json = []
        for address in wallet.addresses:
            addresses_json.append(self._address_to_json(address))
        json_file['addresses'] = addresses_json
        return json.dumps(json_file, sort_keys=True, indent=4)

    def _address_to_json(self, address):
        address_json = {}
        key_pub = address['key_pub'].export_key(format='DER')
        address_json['key'] = address['key'].export_key(format='DER').hex()
        address_json['key_pub'] = key_pub.hex()
        address_json['address'] = SHA1.new(key_pub).hexdigest()
        return address_json
    
    @staticmethod
    def deserialize(json_string):
        data = json.loads(json_string)
        wallet = Wallet(Wallet_as_Json())
        addresses = []
        for address_object in data['addresses']:
            byte_string = bytearray.fromhex(address_object['key'])
            key = ECC.import_key(bytes(byte_string))
            pub = key.public_key()
            addresses.append({
                'key': key,
                'key_pub': pub
            })
        wallet.addresses = addresses
        return wallet
