class Various_Mixin(object):

    def OP_SIZE(self):
        pass
    
    def OP_EQUAL(self):
        pass

    def OP_EQUALVERIFY(self):
        elem1 = self.stack.pop()
        elem2 = self.stack.pop()
        if(elem1 == elem2):
            self.stack.append(1)
        else:
            self.stack.append(0)
        self.OP_VERIFY()
