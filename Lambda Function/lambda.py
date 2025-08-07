# lambda: a nameless small function
# lambda arguments: expression

from functools import reduce


add10 = lambda x: x + 10

print(add10(10))

mult = lambda x,y: x * y
print(mult(10,20))

def get_second(x):
    return x[1]
li = [(1,2), (15,1), (5,-1), (10,4)]
# li.sort(key=lambda x: x[1])
# li.sort(key=get_second)

li.sort(key=lambda x: x[0] + x[1])
print(li)

li_2 = [1,2,3,4,5,6,7,8,9]
li_3 = list(map(lambda x: x * 2,li_2))
li_4 = list(filter(lambda x: x % 2 == 0,li_2))

print(li_3)
print(li_4)

li_5 = reduce(lambda x,y: x*y, li_2)
print(li_5)