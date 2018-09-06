from toycoin.script_lang.opcodes.arithmetic import Arithmetic_Mixin
from toycoin.script_lang.opcodes.constants import Constants_Mixin
from toycoin.script_lang.opcodes.crypto import Crypto_Mixin
from toycoin.script_lang.opcodes.flow_control import FlowControl_Mixin
from toycoin.script_lang.opcodes.stack import Stack_Mixin
from toycoin.script_lang.opcodes.various import Various_Mixin


class Interpreter(Arithmetic_Mixin, Constants_Mixin, Crypto_Mixin, Stack_Mixin, FlowControl_Mixin, Various_Mixin):
    
    def __init__(self, execution_code):
        self.stack = []
        self.execution_code = execution_code

    def execute(self):
        for statement in self.execution_code:
            if statement.startswith('OP_'):
                getattr(self, statement)()
            else:
                self.stack.append(statement)
                
                
    @staticmethod
    def init(script_as_string):
        return Interpreter([c.strip() for c in script_as_string.split('\n')])
