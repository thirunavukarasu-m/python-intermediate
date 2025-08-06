# Dictionary: key: value pairs, unordered, mutable
# Can only have immutable data types as keys.

my_dict = {
    1: 100,
    2: 200,
    3: 300
}

new_dict = {i*2:j*2 for i,j in my_dict.items()}
print(new_dict)
my_dict.update(new_dict)
print(my_dict)

for i,j in my_dict.items():
    print(i,j)
    
for i in my_dict.values():
    print(i)
    
for i in my_dict:
    print(i)
    
print(my_dict[1])
my_dict[4] = 400

my_dict.pop(3)
my_dict.popitem()

print(1 in my_dict)
print(my_dict)


try:
    print(my_dict[89])
except:
    print('error')
    
new_dict = {i*2:j*2 for i,j in my_dict.items()}