class Block(object):

    def __init__(self):
        self.header = {
            'version': '',
            'hashPrevBlock': '',
            'hashMerkleRoot': '',
            'time': '',
            'target': '',
            'nounce': ''
        }
        self.size = 0
        self.tx_ctr = 0
        self.txs = []

    def get_header(self):
        return self.header