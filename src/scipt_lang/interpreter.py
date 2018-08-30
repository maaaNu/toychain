class Interpreter(object):
    
    def __init__(self, execution_code):
        self.stack = []
        self.execution_code = execution_code

    def execute(self):
        for command in self.execution_code:
            pass

    @staticmethod
    def interpret(script_as_string):
        return Interpreter(script_as_string.split('\n'))