from src.data_structures.wallet import Wallet

def test_create_adress():
    h = Wallet()
    h.new_adress()
    for adress in h.get_adresses():
        print(adress.hexdigest())