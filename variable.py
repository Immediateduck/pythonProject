class Variable():
    def __init__(self,name,value="nil"):
        self.hasvalue=False
        self.value=value
        self.name=name
        if value!="nil":
            self.hasvalue=True
        self.connectedBox="nil"

    def connectBox(self,box):
        if self.connectedBox=="nil":
            self.connectedBox=box
        else:
            raise ValueError

    def hasValue(self):
        if self.value=="nil":
            self.hasvalue=False
        else:
            self.hasvalue=True
        return self.hasvalue

    def getValue(self):
        if self.hasvalue:
            return self.value

    def work(self):
        if not self.hasvalue and self.connectedBox.hasValue():
            self.value=self.connectedBox.getValue()