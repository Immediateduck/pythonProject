import sys
from operator_box import Operator
class Controller():
    def __init__(self):
        self.boxlist=[]

    def connect(self,b1,b2):
        if not b1 in self.boxlist:
            self.boxlist.append(b1)
        if not b2 in self.boxlist:
            self.boxlist.append(b2)

        if isinstance(b2,Operator) or isinstance(b1,Operator):
            b1.connectBox(b2)
            b2.connectBox(b1)
        else:
            b1.connectBox(b2)


    def startwork(self,probe):
        while True:
            for each in self.boxlist:
                each.work()
                if each==probe and probe.hasValue():
                    print("the value of the requested variable is",each.getValue())
                    sys.exit()

