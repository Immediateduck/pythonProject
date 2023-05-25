class Operator():
    def __init__(self,name,first_mode,op="nil",rop="nil"):
        """the first variable tells which mode is being used
        the first mode (TRUE) is for commutative operations and can have as many as wanted arguments
        op works on a list of args and returns the value itself for only 1 arg
        (i suggest a method for turning methods to above)
        rop works on 2 args only
        the last box added in box list should be the result(subject to change)
        the second mode is for non commutative operations which require 1 operation and 2 reverse operations"""
        self.boxlist=[]
        self.first_mode=first_mode
        self.value="nil"
        self.hasvalue=False
        self.op="nil"
        self.rop="nil"
        self.name=name
        if self.first_mode:
            self.op=op
            self.rop=rop

    def hasValue(self):
        if self.value=="nil":
            self.hasvalue=False
        else:
            self.hasvalue=True
        return self.hasvalue

    def getValue(self):
        if self.hasvalue:
            return self.value

    def connectBox(self,box):
        if self.first_mode:
            self.boxlist.append(box)

    def work(self):
        bool_list=[x.hasValue() for x in self.boxlist]
        val_list=[x.getValue() for x in self.boxlist]
        if numbool(bool_list) == (len(self.boxlist) - 1):
            temp_list=self.boxlist[:]
            if self.boxlist[-1].hasValue():
                temp_list.remove(self.boxlist[indexFalse(bool_list)])
                temp_list.remove(self.boxlist[-1])
                self.value=self.rop(self.boxlist[-1].getValue(),self.op([x.getValue() for x in temp_list]))
            else:
                temp_list.remove(self.boxlist[-1])
                self.value=self.op([x.getValue() for x in temp_list])






#/////////////////////////////////////////////////////////////////
def numbool(bool_list):
    num = 0
    for each in bool_list:
        if each:
            num += 1
    return num

def indexFalse(bool_list):
    num = 0
    for each in bool_list:
        if not each:
            return num
        else:
            num+=1