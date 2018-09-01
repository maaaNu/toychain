import pytest
from toycoin.data_structures.wallet import Wallet, Wallet_as_Json
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
from Crypto.Util.asn1 import DerSequence
from binascii import hexlify, unhexlify

@pytest.fixture
def wallet_json():
    json_module = Wallet_as_Json()
    return Wallet(json_module)


@pytest.fixture
def wallet_default():
    json_module = Wallet_as_Json()
    return Wallet(json_module)


def test_newWallet_noAddress(wallet_default):
    keypairs = wallet_default.get_keypairs()
    assert len(keypairs) == 0
    

def test_newWallet_addAddress(wallet_default):
    wallet_default.new_keypair()
    keypairs = wallet_default.get_keypairs()
    assert len(keypairs) == 1


def test_serialize_as_json(wallet_json):
    json = wallet_json.serialize()
    assert 'keypairs' in json


def test_withtwoaddress_serialize_as_json(wallet_json):
    wallet_json.new_keypair()
    wallet_json.new_keypair()
    json = wallet_json.serialize()
    assert 'keypairs' in json
    assert 'keypair' in json
    assert 'key' in json
    assert 'key_pub' in json

def test_serialize_and_deserialize_json_wallet(wallet_json):
    wallet_json.new_keypair()
    json = wallet_json.serialize()
    wallet_deserialize = Wallet_as_Json.deserialize(json)
    assert wallet_deserialize == wallet_json

def test_generate_sig(wallet_json):
    wallet_json.new_keypair()    
    address = wallet_json.keypairs[0]
    key = address['key']
    key_pub = address['key_pub'].export_key(format='DER').hex()
    sig = wallet_json.create_sig(key, key_pub)
    t = unhexlify(sig.hex())
    msg = SHA256.new(key_pub.encode())
    verifier = DSS.new(key.public_key(), 'fips-186-3', encoding='der')
    try:
        verifier.verify(msg, t)
    except ValueError:
        pytest.fail("The message is not authentic.")
