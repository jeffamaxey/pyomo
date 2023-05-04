# functions.py

# @all:
def Apply(f, a):
    return [f(a[i]) for i in range(len(a))]
 
def SqifOdd(x):
    # if x is odd, 2*int(x/2) is not x
    # due to integer divide of x/2
    return x if 2*int(x/2) == x else x*x
 
ShortList = range(4)
B = Apply(SqifOdd, ShortList)
print(B)
# @:all
