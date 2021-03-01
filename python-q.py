# 1 Counter
from collections import namedtuple
from collections import OrderedDict
from collections import Counter
import copy

s1 = "ashjkdhalksdjlkajsd"
s1_counter = Counter(s1)
temp_s1_counter = copy.deepcopy(dict(s1_counter))


# 2 Ternary Operator (falseValue, trueValue)[condition]
print((False, True)[10 < 13])

# 3 OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# 4 OrderedCounter

s = "asioruqwporuoenfksjdbvisdaog fjwhgbvof"
s_normal_counter = dict(Counter(s))
s_ordered_counter = OrderedDict(
    sorted(s_normal_counter.items()), key=lambda t: t[0])
s_ordered_counter.pop('key')
s_con = s_ordered_counter

print(s_normal_counter)
print(s_con == s_normal_counter)   # True
print(s_con)

# 5 namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)       # instantiate with positional or keyword arguments
print(p[0] + p[1])          # indexable like the plain tuple (11, 22)
x, y = p                    # unpack like a regular tuple
print(x, y)
p.x + p.y                   # fields also accessible by name

t = [11, 22]
# Class method that makes a new instance from an existing sequence or iterable.
Point._make(t)

p = Point(x=11, y=22)
# Return a new OrderedDict which maps field names to their corresponding values
p._asdict()
# Return a new instance of the named tuple replacing specified fields with new values
p._replace(x=33)
p._fields   # ('x', 'y')    # view the field names
getattr(p, 'x')  # 11

d = {'x': 11, 'y': 22}
Point(**d)  # Point(x=11, y=22)


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)


for p in Point(3, 4), Point(14, 5/7):
    print(p)

# Point: x= 3.000  y= 4.000  hypot= 5.000
# Point: x=14.000  y= 0.714  hypot=14.018
