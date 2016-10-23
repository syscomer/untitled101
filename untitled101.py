x =102
print("outside printx, xid= ",  id(x))

def printx():
    #global x
    x=200
    print("inside printx, xid= ",  id(x))
    print("x= %d"%x )
    x=101
    print("inside printx, xid= ",  id(x))
    #print("inside printx, xid= ",  id(x))
printx()
print(x)
print(id(x))
print ("locals: ", locals())

print ("globals: ", globals())

