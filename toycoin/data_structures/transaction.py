from enum import Enum
from Crypto.Hash import SHA256

class Transaction(object):
    
    def __init__(self, type, v_in, v_out):
        self.version = '1'
        self.type = type
        self.v_in = v_in
        self.v_out = v_out

    def __hash__(self):
        h = SHA256.new()
        v_ins_hashed = ''.join(str(hash(v)) for v in self.v_in)
        v_out_hashed = ''.join(str(hash(v)) for v in self.v_out)
        h.update(self.version.encode())
        h.update(self.type.value)
        h.update(v_ins_hashed.encode())
        h.update(v_out_hashed.encode())

        double_hash = SHA256.new()
        double_hash.update(str(h.hexdigest()).encode())
        return int(double_hash.hexdigest(), 16)

class Tx_Type(Enum):
    COINBASE = b'COINBASE'
    FEE_TRANSACTION = b'FEE_TRANSACTION'
    P2PH = b'P2PH'

class Tx_Input(object):

    def __init__(self):
        self.outpoint = ''  # The outpoint references a previous output
        self.amount = 0
        self.unlock_scripts = []

    def __hash__(self):
        h = SHA256.new()
        unlock_scripts_hashed = ''.join(str(hash(l)) for l in self.unlock_scripts).encode()
        h.update(unlock_scripts_hashed)
        h.update(self.outpoint.encode())
        h.update(str(self.amount).encode())
        
        double_hash = SHA256.new()
        double_hash.update(str(h.hexdigest()).encode())
        return int(double_hash.hexdigest(), 16)

class Tx_Output(object):
    
    def __init__(self, amount, lock_scripts):
        self.amount = amount
        self.lock_scripts = lock_scripts

    def __hash__(self):
        h = SHA256.new()
        lock_scripts_hashed = ''.join(str(hash(l)) for l in self.lock_scripts).encode()
        h.update(lock_scripts_hashed)
        h.update(str(self.amount).encode())
        
        double_hash = SHA256.new()
        double_hash.update(str(h.hexdigest()).encode())
        return int(double_hash.hexdigest(), 16)
