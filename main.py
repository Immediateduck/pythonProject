from controller import Controller
from variable import Variable
from operator_box import Operator

def packageLambda(func):
    def new(val):
        if len(val)==1:
            return val[0]
        else:
            return func(val)
    return new

def pl(val):
    ans=val[0]
    for each in val[1:]:
        ans*=each
    return ans

ctrl=Controller()

x=Variable("x")
y=Variable("y",2)
z=Variable("z",3)
ans=Variable("ans",24)


plus=Operator("plus",True,packageLambda(pl),lambda a,b:a/b)

ctrl.connect(x,plus)
ctrl.connect(y,plus)
ctrl.connect(z,plus)
ctrl.connect(ans,plus)


ctrl.startwork(x)

