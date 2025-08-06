# Lists: Ordered, mutable, allows duplicate elements.ArithmeticError

my_list = [1,2,3,4,5,6]
# for i in my_list:
#     print(i)
    
my_list.append(7)
my_list.insert(1,100)
my_list.pop()
my_list.remove(3)
print(my_list.count(5))
my_list.reverse()
my_list.sort() # this sorts inplace.
print(my_list)

new_list = [0] * 5
new = my_list + new_list
print(new[::-1])
print(new)

# for i in range(len(new)-1, -1,-1):
#     print(new[i])
    

new_list_comp = [i * 2 for i in new]
print(new_list_comp)