from toycoin.data_structures.block import Block
from Crypto.Hash import SHA256
from collections import namedtuple


class Mine(object):

    def __init__(self, difficulty, transactions, hashPrevBlock):
        block = Block()
        block.header['target'] = difficulty
        block.header['hashMerkleRoot'] = self.construct_merkleTree(transactions)
        block.header['hashPrevBlock'] = hashPrevBlock
        self.block = block

    def mining_step(self):
        if hash(self.block) < self.block.header['target']:
            self.block.increment_nounce()
            return False
        return True

    def construct_merkleTree(self, transactions):
        if not len(transactions) % 2 is 0:
            transactions.append(transactions[-1])
        nodes = [hash(t) for t in transactions]

        h = SHA256.new()
        while len(nodes) > 1:
            nodes = [str(hash(t1) + hash(t2)) for t1,t2 in zip(nodes[::2], nodes[1::2])]
        h.update(str(nodes[0]).encode())
        return h.hexdigest()