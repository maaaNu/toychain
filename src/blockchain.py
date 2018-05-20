import json, random
from transactions import hashing, isValidTxn, updateState
from blocks import createBlock

def createRandomTransaction(max_integer=3):
    sign = int(random.getrandbits(1)) * 2 - 1
    amount = random.randint(1, max_integer)
    amountA = sign * amount
    amountB = -1 * amountA

    return {u'Alice': amountA, u'Bob': amountB}


state = {u'Alice': 50, u'Bob': 50}  # Define the initial state
blockSizeLimit = 5

genesisBlockTxns = [state]
genesisBlockContents = {u'blockNumber': 0, u'parentHash': None,
                        u'txnCount': 1, u'txns': genesisBlockTxns}
genesisBlock = {u'hash': hashing(genesisBlockContents), u'contents': genesisBlockContents}

chain = [genesisBlock]
txnBuffer = [createRandomTransaction() for i in range(30)]

while len(txnBuffer) > 0:
    bufferStartSize = len(txnBuffer)

    ## Gather a set of valid transactions for inclusion
    txnList = []
    while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
        newTxn = txnBuffer.pop()
        # This will return False if txn is invalid
        validTxn = isValidTxn(newTxn, state)

        if validTxn:           # If we got a valid state, not 'False'
            txnList.append(newTxn)
            state = updateState(newTxn, state)
        else:
            print("ignored transaction")
            sys.stdout.flush()
            continue  # This was an invalid transaction; ignore it and move on

    ## Make a block
    myBlock = createBlock(txnList, chain)
    chain.append(myBlock)


print(chain[0])
print(chain[1])
print(chain[2])
print(chain[3])
print(chain[4])

print(state)