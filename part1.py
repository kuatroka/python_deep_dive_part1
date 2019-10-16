
##################
### multiline code ############
### implicit line continuation

a = [1,2,3]

a = [1,2,
    3,4,5]

a

a = [1 # item 1,
    ,2]

a = [1, # item 1,
    2]

a = (1 # comment 1
     ,2 # comment
     ,3)

 a = {'key1' : 1 # value for the key 1
     ,'key2' : 2 # value for the key 2
     }

def my_func(a, # comment for the argument 1
     b, # comment for the argument 2
      c):
    print(a,b,c)

my_func(10, # comment for value 1
     20,    # comment for value 2
      30    # comment for value 3
      )

##################################################
### explicit line continuation

a = 10
b = 20
c = 30

if a > 5 \
    and b > 10 \
        and c > 20:
        print('yes')



a = ''' this a string'''
print(a)

a = ''' this 
is a string'''
print(a)

a = '''this 
        is a string
        that is created over multiple lines'''
print(a)

## over multiple lines of a string, be careful as it's not always lines up
## as intented 

def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a

#### and the below are very different

def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a

print(my_func())


################################
a = '''
asfsdfasdfds
        asfsdfdsf
        '''

print(a)





## Multiline coding
## implicit multiline

 #() [] {}

 a = [1,2,3]

a = [1 # first argument
    ,2 # second argument
    ,3] # third agrument

b = (12, 23, 45)

b = (12, # sdfsdfd
     23 # sdfdsfds
    ,45) # sdfdsfsdf

c = {'a' : 23, # sdfsdfdsfd
 'b' : 56}

def my_func(a, # parameter 1 - years old
            b, # parameter 2 - how many gf I had :)
            c): # don't know anything about it!
    print(a, b, c)

my_func(2,3,5)

my_func(2,
        3,  
        5)

######## Explicit multiline code

a = 23  + \
    54 + \
    65

b = "sfdsfd sdf sdafasd asdf \
 asdf asdf"

###############################################################


 ##################  conditionals

a = 5 

if a < 10:
     print(' a > 5')
elif a < 10:
    print('5 <= a < 10')
elif a < 15:
    print('10 <= a < 20')
else:
    print('a > 20')


############################## turnery operator
a = 25
if a < 5:
    b = 'a < 5'
else:
    b = 'a >= 5'

print(b)

###
a = 3
b = 'a < 5' if a < 5 else 'a >= 5'
print(b)


############################### functions

def func1():
    print('running Func1')
    return 2 + 3

def func2():
    return func1()

func2()

#####  very important, when assigning a function to a variable, 
#####  do not add the () at the en of the function. a = func, NOT a = func()
#####  but... when calling that variable, then DO add the (). a() NOT a 
my_func = func2
my_func1 = func1
my_func()
my_func1()

print(my_func1())

################ lambdas
lambda x: x**2
a  = lambda x, y: x**2 - y
a(3, 2)

############# While loop
###########

i = 0
while i < 5:
    print(i)
    i += 1

i = 5

while True:
    print(i)
    if i >= 5:
        break
        print('after break')

######################  break
min_length = 2
name = input(' Please enter your name:')

while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input(' Please enter your name:')

print('Hello, {0}'.format(name))

##########

min_length = 2

while True:
    name = input(' Please enter your name:')
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print('Hello, {0}'.format(name))

################  continue

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

###########
l = [1,2,3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1

if not found:
    l.append(val)

print(l)

####  version with "else" and no flag "found"
l = [1,2,3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1

else:
    l.append(val)

print(l)

###########  break, continue within try and expect and whithin a while loop

a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('division by zero')
finally:
    print('this always executes')


a = 0
b = 2

while a < 4:
    print('--------------------')
    a += 1
    b -= 1

    try:
        a/b
    
    except ZeroDivisionError:
        print('{0}, {1} - division by zero'.format(a, b))
        continue
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop is over'.format(a, b))


#######  with break
a = 0
b = 2


while a < 4:
    print('--------------------')
    a += 1
    b -= 1

    try:
        a/b
    
    except ZeroDivisionError:
        print('{0}, {1} - division by zero'.format(a, b))
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop is over'.format(a, b))

############## adding else
a = 0
b = 10

while a < 4:
    print('--------------------')
    a += 1
    b -= 1

    try:
        a/b
    
    except ZeroDivisionError:
        print('{0}, {1} - division by zero'.format(a, b))
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))

    print('{0}, {1} - main loop is over'.format(a, b))

else:
    print('Code completed without the zero division error')

##################################################################
######### For Loop  ##############################################

for i in range(5):
    print(i)

for i in [1,2,3,4,5]:
    print(i)

for c in 'hello':
    print(c)

for x in ('a', 'b', 'c', 5, [1,2,4,5]):
    print(x)

for x in [(1,2), (3,4), (5,6)]:
    print(x)


for i, j in [(1,2), (3,4), (5,6)]:
    print(i, j)

for i in range(5):
    if i ==3:
        break
    print(i)

for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break

else:
    print('No multiple of 7 found')

##############

for i in range(1, 9):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break

else:
    print('No multiple of 7 found')

#################################
s = 'hello'
i = 0

for c in s:
    print(i, c)
    i += 1

##########
s = 'hello'
for i in range(len(s)):
    print(i, s[i])


#######
## the best way

s = 'hello'
for i, c in enumerate(s):
    print(i, c)



#####################################################################
######### Classes  ##################################################

class Rectangle:
       def __init__(self, width, height):
           self.width = width
           self.height = height

r1 = Rectangle(10, 20)
r1.width

r1.width = 100
r1.width


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)

r1 = Rectangle(10, 20)

r1.area()

r1.perimeter()


str(r1)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)

    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

r1 = Rectangle(10, 20)

str(r1)
r1.to_string()

####################### __repr__
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

r1 = Rectangle(10, 20)

str(r1)
r1

r2 = Rectangle(10, 20)

r1 is not r2
r1 == r2


##################### __eq__

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        return self.height == other.height and self.width == other.width

r1 = Rectangle(10, 20)

r2 = Rectangle(10, 20)

r1 == r2
r1 is not r2
r1 == 200

#'##################
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.height == other.height and self.width == other.width
        else:
            return False

r1 = Rectangle(10, 20)

r2 = Rectangle(10, 20)

r1 == r2
r1 is not r2
r1 == 200


############### less than

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.height == other.height and self.width == other.width
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    

r1 = Rectangle(10, 20)

r2 = Rectangle(100, 200)

r1 < r2
r2 < r
r1 <= r2

r1 == r2
r1 is not r2
r1 < 200

##################################### getter and setter java way
class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width musts be positive')
        else:
            self._width = width
  
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._height == other._height and self._width == other._width
        else:
            return False

r1 = Rectangle(10, 20)
r1.width
r1._width

r1.width = -100
r1.get_width()

r1.set_width(100)
r1
############### getter and setter pytonic way. Pay attention how decorator is used
############### and how it converts a method to a property
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width
            

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._height = height 

   
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.height == other.height and self.width == other.width
        else:
            return False

r1 = Rectangle(10, 20)

r1.width

r1.width = 300
r1.width = -2

r1 = Rectangle(10, 20)


############################################################################
############## variables and memory  #######################################

my_var = 10
print(my_var)
print(id(my_var))
print(hex(id(my_var)))

greeting = 'hello'
print(greeting)
print(hex(id(greeting)))

other_var = my_var

print(hex(id(other_var)))

sys.getrefcount(my_var)
import ctypes
ctypes.c_long.from_address(id(my_var))

import sys
a = [1,2,3]

id(a)
sys.getrefcount(a)

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

ref_count(id(a))



b = a
ref_count(id(b))

c = a
ref_count(id(c))
c = 10
b = None

import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return 'Object exists'
    return 'Object not found'
    
######### Circular reference 
class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()

my_var = A()

print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))


a_id = id(my_var)
b_id = id(my_var.b)

print(ref_count(a_id))
print(ref_count(b_id))

object_by_id(a_id)
object_by_id(b_id)

my_var = None

gc.collect()

########################################################
#########  var types

a = 'hello'
type(a)
a= 10
type(a)

a = lambda x: x**2
type(a)

########################################################
############ variables reassignment

a = 10
hex(id(a))
type(a)

a = 15
hex(id(a))

a = a + 1
hex(id(a))

a = 10
b = 10

hex(id(a))
hex(id(b))



#################################
##### mutable and immutable structures

my_list = [1, 2, 3]
type(my_list)

id(my_list)

my_list.append(4)
my_list
id(my_list)

my_list_1 = [1, 2, 3]
id(my_list_1)

my_list_1 = my_list_1 + [4]

my_list_1
id(my_list_1)

my_dict = dict(key1= 1, key2 = 'a')
id(my_dict)
my_dict['key3'] = 10.5
my_dict
id(my_dict)

t = (1, 2, 3)
id(t)

t[0]
id(t[2])

t = ([1,2], [3,4])
t[1]
t[0].append(3)

id(t)
t[1].append('34')

id(t)

#################################

def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + 'world'
    print('Final s # = {0}'.format(id(s)))

my_var = 'Hello'
print('my_var # = {0}'.format(id(my_var)))
process(my_var)



def modify_list(lst):
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100)
    print('Final lst # = {0}'.format(id(lst)))


my_list = [1,2,3]
id(my_list)
print('my_list # = {0}'.format(id(my_list)))

modify_list(my_list)



def modify_tuple(t):
    print('Initial t # = {0}'.format(id(t)))
    t[0].append(100)
    print('Final t # = {0}'.format(id(t)))

my_tuple = ([1,2], 'a')
id(my_tuple)

modify_tuple(my_tuple)

###########################################

a = 'hello'
b = a
hex(id(a))

hex(id(b))

a = 'hello'
b = 'hello'

hex(id(a))

hex(id(b))

b = 'hello world'

hex(id(b))

hex(id(a))

a = [1,2,3]

b = a 
hex(id(a))

hex(id(b))

b.append(100)
hex(id(a))

hex(id(b))

a

a = 10
b = 10

hex(id(a))
hex(id(b))

a = 500
b = 500

hex(id(a))
hex(id(b))

a is b
a is not b
not(a is b)
a == b

a != b
not(a == b)

a = [1,2,3]
b = [1,2,3]

hex(id(a))
hex(id(b))
a is b
a == b


a = 10
b = 10

id(a)
id(b)

a is b
a == b

a = 500
b = 500

id(a)
id(b)

a == b
a is b


a = 10 + 0j
type(a)
b = 10

a is b
a== b

id(None)

a = None
b = None
c = None


a is b
a is None
b is None

#####################################################

a = 10 
print(type(a))

b = 10
type(b)

print(type(b))

 help(int)

 c = int()
 c
 c = int('101', base=2)
 c

def square(a):
    return a **2

type(square)

f = square

id(square)

id(f)

square is f
square(2)
f(2)

def cube(a):
    return a **3

 
def select_function(fn_id):
    if fn_id == 1:
            return square
    else:
        return cube

f = select_function(1)
f is square

f == square
f(2)
f = select_function(4)

f(2)

select_function(2)(3) ### !!!!!  wow - this is how to pass parameters to 
                      ### the function within a function

select_function(1)(4)

def exec_function(fn, n):
    return fn(n)

exec_function(cube, 3)       

exec_function(square, 2)

##########################################################
##[-5, 256]
a = 10
b = 10

id(a)
id(b)


a = -5
b = -5

a is b

a = 256
b = 256

a is b

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
print(a,b,c,d)

print(id(a), id(b), id(c), id(d))


#################################################
a = 'hello'
b = 'hello'

id(a), id(b)

a = 'hello world'
b = 'hello world'
id(a), id(b)

a==b
a is b

a = '_this_is_a_long_string_that_could_be_used_as'

b = '_this_is_a_long_string_that_could_be_used_as'

a == b
a is b

import sys
a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'

id(a), id(b), id(c)

a is b
a is c
a == c

####################################################
## time how long does it take to run two comparisons

def compare_using_equals(n):
    a = 'a long string that is not interned' *  200
    b = 'a long string that is not interned' *  200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' *  200)
    b = sys.intern('a long string that is not interned' *  200)
    for i in range(n):
        if a is b:
            pass


import time
start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print('equality', end-start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print('equality', end-start)

######################################################

(1,2) * 5
'abc' * 3
'hello' + ' world'

def my_func():
    a = 24 * 60
    b = (1,2) * 5
    c = 'avc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3

my_func.__code__.co_consts

def my_func(e):
    if en in {1,2,3}:
        pass

my_func.__code__.co_consts



import string
import time
string.ascii_letters

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)

char_set = set(string.ascii_letters)


print(char_list)
print(char_tuple)
print(char_set)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list', end-start)

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple', end-start)

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set', end-start)

#################################
##### a set is the quickest iterator, so if possible or the 
##### speed is necessary, it's better to use sets

##########################################################
########## Integers #####################################

print(type(100))

import sys
sys.getsizeof(0)

sys.getsizeof(1)
sys.getsizeof(3 ** 1000)

import time

def calc(a):
    for i in range(10000000):
        a * 2

start = time.perf_counter()
calc(2 ** 100)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2 ** 10000)
end = time.perf_counter()
print(end - start)

########
########
