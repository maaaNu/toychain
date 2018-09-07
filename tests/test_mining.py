from toycoin.data_structures.transaction import Transaction, Tx_Type, Tx_Output
from toycoin.mining import Mine

def test_simple_mining():
    t_1 = build_transaction(500000)
    t_2 = build_transaction(600000)
    t_3 = build_transaction(450000)
    t_4 = build_transaction(500001)
    t_5 = build_transaction(523490)
    mine = Mine(2297526641161484781, [t_1, t_2, t_3, t_4, t_5], "0")
    hash_found = mine.mining_step()
    while not hash_found:
        hash_found = mine.mining_step()
    assert hash_found is True


def build_transaction(amount):
    lock_script = """304502207cd05e378a92e7c41198c698c7d54a387e495502a8cf2a8f214c748e22b090dd0221008980c14bc6b428d45d8735eed92da67e9f086d3e412d3dbbb2a50b2abdf729b5 
    3059301306072a8648ce3d020106082a8648ce3d03010703420004a469fee792b56101a51a1e98ec3e5f264e1293a03f8f18624da69ca9f19ed6abf3b24cd049d23aef3e42dbc27b5635654ee17552135c48c34972570e6a72f9ca 
    OP_DUP 
    OP_HASH160 
    0caf8c91f73362bd58adee5e58c74e4c3bb237b0 
    OP_EQUALVERIFY 
    OP_CHECKSIG
    """
    t_out = Tx_Output(amount, [lock_script])
    t = Transaction(Tx_Type.P2PH, [], [t_out])
    return t
