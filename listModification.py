"""Первая версия функции извлекает первый аргумент (args – это кортеж) и обходит
остальную часть коллекции, отсекая первый элемент (нет никакого
смысла сравнивать объект сам с собой, особенно если это довольно крупная
структура данных)."""
def min1(*args):
    current = args[0]
    for i in args[1:]:  # all but the first element
        if i < current:
            current = i
    print(current)


#min1(1,55,3,2)

"""Вторая версия позволяет интерпретатору самому выбрать первый аргумент
и остаток, благодаря чему отпадает необходимость извлекать первый аргумент
и получать срез."""

def min2(first,*rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

#print(min2(999,44,24,66))

"""Третья версия преобразует кортеж в список с помощью встроенной функции
list и использует метод списка sort."""

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]
#print(min3(8,2,45))
""" обобщить функцию так, что она будет отыскивать
либо минимальное, либо максимальное значение, определяя отношения
элементов за счет интерпретации строки выражения с помощью таких средств,
как встроенная функция eval """
def minmax(func, *args):
    current = args[0]
    for i in args[1:]:
        if func(i, current):
            current = i
    return current

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

#print(minmax(lessthan, 4,3,2,5,6))
#print(minmax(grtrthan, 4,3,2,5,6))
"""found unic  I don't know why but it is works only for 2 arg not for all shit"""
def union (*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
        return res

s1, s2, s3 = "SPAM", "SCAM", "SLAM"
print(union(s1, s2, s3))

"""write map funciton"""
def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

"""lessons for the map function
you have different city with temperature"""
teps = [("berlin", 23), ("kharkiv", 33), ("barsa", 45)]
c_to_t= lambda data: (data[0], (9/5)*data[1]+32)# formula fro the celsius to farengait

print(list(map(c_to_t, teps)))

"""write your own reduce"""
def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

#testing
myreduce((lambda x, y: x + y), [1,2,3,4,5])

"""write your own reduce with for"""
L = [1,2,3,4,5]
res = L[0]
for x in L[1:]:
    res = res + x

"""create list with map function for n**2 in range (10)"""
list(map((lambda x: x **2), (range(10))))

"""wrire generator witch will be concatanate first letter of the spam SPAM like sS sP sA"""
print([x + y for x in 'spam' for y in 'SPAM'])
""""row in matrix"""
M = [[1,2,3],[4,5,6],[7,8,9]]
[row[1] for row in M]

"""matrix diagonal"""
[M[i][i] for i in range(len(M))]

"""multiply 2 matrix"""
res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)
res
"""write the same with lambda"""
def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4

L = [f1,f2,f3]

for f in L:
    print(f(2))

print(L[0](3))
#answer
M = [lambda z: z+1,
     lambda z: z+2,
     lambda z: z+3]

for k in M:
    print(k(3))

print(M[2](3))
"""create new list with modifided previous list"""
counters_ = [1, 2, 3, 4]
updated=[]
for x in counters_:
    updated.append(x + 10)
print(updated)
"""create the same with map function"""
def inc(x) : x + 10
map(inc, counters_)
"""put lambda inside map"""
list(map((lambda x: x + 3), counters_))

"""range"""
#1 line of odd numbers
res = []
for i in range(1, 25, 2):
    res.append(i)

print(res)
#2use the list comprehension
res = [x for x in range(1, 20, 2)]
print(res)
#3 exclude the squares and don't show squares multiples 3
res = [x ** 2 for x in range (1, 100, 2) if x %3 != 0]
#4 you have dic = {'John': 1200, 'Paul': 1000, 'jones':450}
# output the John = 1200
dic = {'John': 1200, 'Paul': 1000, 'jones':450}
print = ("\n".join([f"{name} = {salary:d}" for name, salary in dic.items()]))
