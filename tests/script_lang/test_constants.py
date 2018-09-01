import pytest
from toycoin.script_lang.opcodes.constants import Constants_Mixin

class Mock_Stack(Constants_Mixin):

    def __init__(self):
        self.stack = []

@pytest.fixture
def mock_stack():
    return Mock_Stack()

def test_OP_0(mock_stack):
    mock_stack.OP_0()
    stack = mock_stack.stack
    assert len(stack) is 1
    assert stack[0] == []

def test_OP_1NEGATE(mock_stack):
    mock_stack.OP_1NEGATE()
    stack = mock_stack.stack
    assert stack[0] is -1

def test_OP_1(mock_stack):
    mock_stack.OP_1()
    stack = mock_stack.stack
    assert stack[0] is 1

def test_OP_16(mock_stack):
    mock_stack.OP_16()
    stack = mock_stack.stack
    assert stack[0] is 16
