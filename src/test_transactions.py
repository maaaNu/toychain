from transactions import isValidTxn


def test_basic_valid_transaction():
    state = {u'Alice': 5, u'Bob': 5}
    assert isValidTxn({u'Alice': -3, u'Bob': 3}, state) == True

def test_cant_destroy_token():
    state = {u'Alice': 5, u'Bob': 5}
    assert isValidTxn({u'Alice': -4, u'Bob': 3}, state) == False

def test_cant_overdraft():
    state = {u'Alice': 5, u'Bob': 5}
    assert isValidTxn({u'Alice': -6, u'Bob': 6}, state) == False

def test_can_create_user():
    state = {u'Alice': 5, u'Bob': 5}
    assert isValidTxn({u'Alice': -4, u'Bob': 2, 'Lisa': 2}, state) == True

def test_cant_create_token():
    state = {u'Alice': 5, u'Bob': 5}
    assert isValidTxn({u'Alice': -4, u'Bob': 3, 'Lisa': 2}, state) == False
