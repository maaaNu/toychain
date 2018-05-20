from transactions import hashing, updateState


def createBlock(txns, chain):
    parentBlock = chain[-1]
    parentHash = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    txnCount = len(txns)
    blockContents = {u'blockNumber': blockNumber, u'parentHash': parentHash,
                     u'txnCount': len(txns), 'txns': txns}
    blockHash = hashing(blockContents)
    block = {u'hash': blockHash, u'contents': blockContents}

    return block


def checkBlockHash(block):
    expectedHash = hashing(block['contents'])
    if block['hash'] != expectedHash:
        raise Exception('Hash does not match contents of block %s' %
                        block['contents']['blockNumber'])
    return


def checkBlockValidity(block, parent, state):
    parentNumber = parent['contents']['blockNumber']
    parentHash = parent['hash']
    blockNumber = block['contents']['blockNumber']

    # Check transaction validity; throw an error if an invalid transaction was found.
    for txn in block['contents']['txns']:
        if isValidTxn(txn, state):
            state = updateState(txn, state)
        else:
            raise Exception('Invalid transaction in block %s: %s' %
                            (blockNumber, txn))

    checkBlockHash(block)  # Check hash integrity; raises error if inaccurate

    if blockNumber != (parentNumber+1):
        raise Exception(
            'Hash does not match contents of block %s' % blockNumber)

    if block['contents']['parentHash'] != parentHash:
        raise Exception('Parent hash not accurate at block %s' % blockNumber)

    return state


def checkChain(chain):
    if type(chain) == str:
        try:
            chain = json.loads(chain)
            assert(type(chain) == list)
        except:  # This is a catch-all, admittedly crude
            return False
    elif type(chain) != list:
        return False

    state = {}
    ## Prime the pump by checking the genesis block
    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents

    for txn in chain[0]['contents']['txns']:
        state = updateState(txn, state)
    checkBlockHash(chain[0])
    parent = chain[0]

    ## Checking subsequent blocks: These additionally need to check
    #    - the reference to the parent block's hash
    #    - the validity of the block number
    for block in chain[1:]:
        state = checkBlockValidity(block, parent, state)
        parent = block

    return state
