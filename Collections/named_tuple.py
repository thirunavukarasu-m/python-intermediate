from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1,2)
print(pt, pt.x, pt.y)