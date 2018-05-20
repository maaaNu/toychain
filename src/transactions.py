import hashlib, json, sys, random


def hashing(msg=""):
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys=True)

    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(), 'utf-8')
    # else
    return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()


def updateState(txn, state):
    state = state.copy()
    for k in txn:
        if k in state.keys():
            state[k] += txn[k]
        else:
            state[k] = txn[k]
    return state


def isValidTxn(txn, state):
    if sum(txn.values()) is not 0:
        return False

    for k in txn.keys():
        if k in state.keys():
            acctBalance = state[k]
        else:
            acctBalance = 0
        if (acctBalance + txn[k]) < 0:
            return False

    return True

