def indexFalse(bool_list):
    num = 0
    for each in bool_list:
        if not each:
            return num
        else:
            num+=1
bool=[True,True,False,True]
def b(c):
    if c:return  1
    else: return 0
print([b(x) for x in bool ])