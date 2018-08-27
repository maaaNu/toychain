class Constants_Mixin(object):

    def OP_0(self):
        self.stack.append([])
    
    def OP_1NEGATE(self):
        self.stack.append(-1)
    
    def OP_1(self):
        self.append(1)
    
    def OP_TRUE(self):
        self.append(1)
    
    def OP_2(self):
        self.append(2)

    def OP_3(self):
        self.append(3)
    
    def OP_4(self):
        self.append(4)
    
    def OP_5(self):
        self.append(5)
    
    def OP_6(self):
        self.append(6)
    
    def OP_7(self):
        self.append(7)

    def OP_8(self):
        self.append(8)

    def OP_9(self):
        self.append(9)

    def OP_10(self):
        self.append(hex(10))

    def OP_11(self):
        self.append(hex(11))

    def OP_12(self):
        self.append(hex(12))

    def OP_13(self):
        self.append(hex(13))

    def OP_14(self):
        self.append(hex(14))

    def OP_15(self):
        self.append(hex(15))

    def OP_16(self):
        self.append(hex(16))
