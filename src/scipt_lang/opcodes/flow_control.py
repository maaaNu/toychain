class FlowControl_Mixin(object):

    def OP_NOP(self):
        pass

    def OP_IF(self):
        if self.stack[-1] is 0:
            #jmp to line
            pass

    def OP_NOTIF(self):
        self.OP_IF()
    
    def OP_ELSE(self):
        pass
    
    def OP_ENDIF(self):
        pass

    def OP_VERIFY(self):
        if self.stack[-1] is 0:
            raise Exception('transaction is invalid')
    
    def OP_RETURN(self):
        raise Exception('transaction is invalid')
