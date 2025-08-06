# Strings: ordered, immutable, text representation.
# Formatted f strings
my_string = "    Hello    "

for i in my_string.strip():
    print(i)

print(my_string.strip() + " " + "World")
print(my_string.lstrip() + " " + "World")
print(my_string.rstrip() + " " + "World")
print(my_string.find("H"))

print(my_string.upper(), my_string.lower())
print(my_string.startswith(" "))
print(my_string.strip().endswith("o"))
print(my_string.count('l'))
print(my_string.replace('l','L'))

new_string = "How are you doing?"
list_of_strings = new_string.split(" ")

print(list_of_strings)
print(' '.join(list_of_strings))

