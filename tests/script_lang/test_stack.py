import pytest
from toycoin.script_lang.opcodes.stack import Stack_Mixin

class Mock_Stack(Stack_Mixin):

    def __init__(self):
        self.stack = []

@pytest.fixture
def mock_stack():
    return Mock_Stack()

def test_OP_IFDUP(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.OP_IFDUP()
    assert len(mock_stack.stack) is 2
    assert mock_stack.stack[-1] is 1

def test_OP_DEPTH(mock_stack):
    mock_stack.OP_DEPTH()
    assert len(mock_stack.stack) is 1
    assert mock_stack.stack[0] is 0

def test_OP_DROP(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.OP_DROP()
    assert len(mock_stack.stack) is 0

def test_OP_DUP(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.OP_DUP()
    assert len(mock_stack.stack) is 2
    assert mock_stack.stack[-1] is 1

def test_OP_NIP(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.stack.append(2)
    mock_stack.OP_NIP()
    assert len(mock_stack.stack) is 1
    assert mock_stack.stack[0] is 2

def test_OP_OVER(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.stack.append(2)
    mock_stack.OP_OVER()
    assert len(mock_stack.stack) is 3
    assert mock_stack.stack[-1] is 1    

def test_OP_PICK(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.stack.append(2)
    mock_stack.stack.append(3)
    mock_stack.stack.append(3)
    mock_stack.OP_PICK()
    assert len(mock_stack.stack) is 5
    assert mock_stack.stack[-1] is 1

def test_OP_ROLL(mock_stack):
    mock_stack.stack.append(1)
    mock_stack.stack.append(2)
    mock_stack.stack.append(3)
    mock_stack.stack.append(3)
    mock_stack.OP_ROLL()
    assert len(mock_stack.stack) is 4
    assert mock_stack.stack[-1] is 1

    