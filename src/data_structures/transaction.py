from enum import Enum

class Transaction(object):
    
    def __init__(self, type):
        self.hash = ''
        self.type = type
        self.tx_input = []
        self.tx_output = []


class Tx_Type(Enum):
    COINBASE = 1
    FEE_TRANSACTION = 2
    REGULAR_TRANSACTION = 3


class Tx_Input(object):

    def __init__(self):
        self.tx_id = ''
        self.amount = 0
        self.unlock_scripts = []

class Tx_Output(object):
    
    def __init__(self):
        self.amount = 0
        self.lock_scripts = []