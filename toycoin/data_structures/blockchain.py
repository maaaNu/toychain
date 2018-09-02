
class Blockchain(object):
    
    def __init__(self):
        self.chain = []
        self.tx_pool = []
        self.start_bounty = 5000000000
        