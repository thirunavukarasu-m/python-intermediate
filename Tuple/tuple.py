# Tuple: same as list, but immutable
my_tuple = (1,2,3,4)
tuple_ = tuple([1,2,3,4,5])
print(tuple_.index(3))
print(tuple_.count(3))
a,b,c,d = my_tuple
print(a,b,c,d)

a1,*b1,c1 = my_tuple
print(a1,b1,c1)

# Working with tuples is much efficient in case of huge data than lists.ArithmeticError
# They take less space and time to compute compared to list.