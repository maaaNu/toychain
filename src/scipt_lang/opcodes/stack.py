class Stack_Mixin(object):

    def OP_IFDUP(self):
        if self.stack[-1] is not 0:
            self.OP_DUP()

    def OP_DEPTH(self):
        self.stack.append(len(self.stack))

    def OP_DROP(self):
        self.stack.pop()

    def OP_DUP(self):
        self.stack.append(self.stack[-1])

    def OP_NIP(self):
        self.stack.pop(-2)

    def OP_OVER(self):
        self.stack.append(self.stack[-2])

    def OP_PICK(self):
        n = self.stack[-1] + 1
        if len(self.stack) < n:
            raise Exception('Illegal Argument')
        self.stack.append(self.stack[n * -1])
    
    def OP_ROLL(self):
        n = self.stack[-1] + 1
        if len(self.stack) < n:
            raise Exception('Illegal Argument')
        self.stack.append(self.stack.pop(n * -1))
    

    def OP_ROT(self):
        pass

    def OP_SWAP(self):
        pass

    def OP_TUCK(self):
        pass

    def OP_2DROP(self):
        pass

    def OP_2DUP(self):
        pass

    def OP_3DUP(self):
        pass
    
    def OP_2OVER(self):
        pass

    def OP_2ROT(self):
        pass

    def OP_2SWAP(self):
        pass