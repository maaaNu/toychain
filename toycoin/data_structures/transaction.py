from enum import Enum

class Transaction(object):
    
    def __init__(self, type):
        self.version = 1
        self.type = type
        self.v_in = []
        self.v_out = []

class Tx_Type(Enum):
    COINBASE = 1
    FEE_TRANSACTION = 2
    P2PH = 3

class Tx_Input(object):

    def __init__(self):
        self.outpoint = ''  # The outpoint references a previous output
        self.amount = 0
        self.unlock_scripts = []

class Tx_Output(object):
    
    def __init__(self):
        self.amount = 0
        self.lock_scripts = []
