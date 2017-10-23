#Charlie Goodrich
#10/23/17
#localDemo.py - demo on local variables

def f():
    x = 77 #x is a local variable
    y = 10 #y is a local variable

x = 5
f() #x doesn't change
print(x)
print(y) #this will cause an error
