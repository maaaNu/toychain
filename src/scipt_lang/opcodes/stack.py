class Stack_Mixin(object):

    def OP_IFDUP(self):
        if self.stack[-1] is not 0:
            self.stack.append(self.stack[-1])

    def OP_DEPTH(self):
        self.stack.append(len(self.stack))

    