from datetime import datetime
from Crypto.Hash import SHA256
import json

class Block(object):

    def __init__(self):
        self.header = {
            'version': '1',
            'hashPrevBlock': '',
            'hashMerkleRoot': '',
            'time': datetime.now().isoformat(),
            'target': '',
            'nounce': 0
        }
        self.size = 0
        self.tx_ctr = 0
        self.txs = []

    def __hash__(self):
        h = SHA256.new()
        header = json.dumps(self.header).encode()
        h.update(header)
        h.update(''.join(str(hash(t)) for t in self.txs).encode())
        double_hash = SHA256.new()
        double_hash.update(str(h.hexdigest()).encode())
        return int(double_hash.hexdigest(), 16)

    def increment_nounce(self):
        self.header['nounce'] += 1