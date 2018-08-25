import pytest
from src.data_structures.wallet import Wallet, Wallet_as_Json

@pytest.fixture
def wallet_json():
    json_module = Wallet_as_Json()
    return Wallet(json_module)


@pytest.fixture
def wallet_default():
    json_module = Wallet_as_Json()
    return Wallet(json_module)


def test_newWallet_noAddress(wallet_default):
    addresses = wallet_default.get_addresses()
    assert len(addresses) == 0
    

def test_newWallet_addAddress(wallet_default):
    wallet_default.new_address()
    addresses = wallet_default.get_addresses()
    assert len(addresses) == 1


def test_serialize_as_json(wallet_json):
    json = wallet_json.serialize()
    assert 'addresses' in json


def test_withtwoaddress_serialize_as_json(wallet_json):
    wallet_json.new_address()
    wallet_json.new_address()
    json = wallet_json.serialize()
    assert 'addresses' in json
    assert 'address' in json
    assert 'key' in json
    assert 'key_pub' in json

def test_serialize_and_deserialize_json_wallet(wallet_json):
    wallet_json.new_address()
    json = wallet_json.serialize()
    wallet_deserialize = Wallet_as_Json.deserialize(json)
    assert wallet_deserialize == wallet_json