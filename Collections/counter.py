# collections: Counter, namedTuple, OrderedDict, defaultDict, deque

from collections import Counter

a = 'aacnascascasxasxfefawed'
counter = Counter(a)
print(counter)
print(counter.keys())
print(counter.values())
print(counter.most_common(2))
print(list(counter.elements()) == list(a))
print(list(counter.elements()),list(a))


