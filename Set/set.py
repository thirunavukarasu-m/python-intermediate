# Set: Unordered, mutable, don't allow duplicates
# These are like keys in dictionaries. 
# Can't have mutable data types in them.

my_set = {1,2,3,4,4,4,4}
my_set.add(5)
my_set.remove(4)
my_set.discard(100) # Won't throw error if it can't find the value.
print(my_set.pop())
print(my_set)

for i in my_set:
    print(i) 
    
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}


combined = odds.union(evens)
print(combined)
intersection = evens.intersection(primes)
print(intersection)

difference = evens.difference(primes)
print(difference)

sym_diff = evens.symmetric_difference(primes)
print(sym_diff)

odds.update(evens)
print(odds)

print(primes.issubset(odds))

print(primes.isdisjoint(odds))

# Frozenset immutable version of set.
