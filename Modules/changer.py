





print ('I am:', __name__)

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y):return x < y

def morethan(x, y): return x > y
print(minmax(lessthan, 4,2,1,5,6,3))
print(minmax(morethan, 4,2,1,5,6,3))