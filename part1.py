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
######## floor division, modulo

135 // 4
135 % 4

type(1+1)

type(2*3)

type(4-10)

type(3**6)

type(2/3)

10/2
print(10/2)

import math
math.floor(3.15)
math.floor(3.999)
math.floor(-3.14)

math.ceil(3.999)
math.floor(-3.000001)

math.floor(-3.0000001)
math.floor(-3.0000000000000000000001)

a = 33
b = 16

print(a/b)
print(a//b)
print(math.floor(a/b))

a//b is math.floor(a/b)
a//b == math.floor(a/b)

a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))


######## truncation

math.trunc(a/b) != math.floor(a/b)

a = b * (a//b) + (a%b)

a = 13
b = 4
print('{0}/{1} = {2}'.format(a,b, a/b))
print('{0}//{1} = {2}'.format(a,b, a//b))
print('{0}%{1} = {2}'.format(a,b, a%b))
print(a == b * (a//b) + (a%b))

a = -13
b = 4
print('{0}/{1} = {2}'.format(a,b, a/b))
print('{0}//{1} = {2}'.format(a,b, a//b))
print('{0}%{1} = {2}'.format(a,b, a%b))
print(a == b * (a//b) + (a%b))

a = 13
b = -4
print('{0}/{1} = {2}'.format(a,b, a/b))
print('{0}//{1} = {2}'.format(a,b, a//b))
print('{0}%{1} = {2}'.format(a,b, a%b))
print(a == b * (a//b) + (a%b))

a = -13
b = -4
print('{0}/{1} = {2}'.format(a,b, a/b))
print('{0}//{1} = {2}'.format(a,b, a//b))
print('{0}%{1} = {2}'.format(a,b, a%b))
print(a == b * (a//b) + (a%b))

###################### Integers and bases ############

type(10)

help(int)
int(10.5)
int(True)


import fractions
a = fractions.Fraction(22, 7)
print(a)

float(a)
int(a)

int('12345')
int('101', 2)

int('ff', 16)

int('B', 11)

bin(10)
bin(5)
oct(10)
hex(255)
a = int('101', 2)
b = 0b101
a
b

def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >=0')
    if n == 0:
        return [0]

    digits = []
    while n > 0:
        # m, n =  n % b, n // b
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


from_base10(10, 2)
from_base10(255, 16)

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode digits')
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    return encoding

encode([15, 15], '0123456789ABCDEF')


######### simpler expression
def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode digits')
    return ''.join([digit_map[d] for d in digits])

encode([15, 15], '0123456789ABCDEF')


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYX'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base >= 36')

    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding



e = rebase_from10(314, 2)
print(e)
print(int(e, base=2))

e = rebase_from10(3451, 16)
print(e)
print(int(e, base=16))



# import string
# string.digits+string.ascii_letters

from fractions import Fraction
help(Fraction)
Fraction(1)
Fraction(1, 2)
Fraction(numerator=1, denominator=5)
Fraction('0.34545')
Fraction('34/76')
x = Fraction(2,3)
y = Fraction(3,4)
c = Fraction(0, 1)
print(c)

x + y
x * y
x / y

Fraction(8, 16)
Fraction(-1, -4)
x = Fraction(1, -5)
x._denominator
x.numerator

import math
x = Fraction(math.pi)
x
float(x)
y = Fraction(math.sqrt(2))
float(y)

a = 0.125
a
b = 0.3
b
Fraction(a)
Fraction(b)

format(b, '0.5f')
format(b, '0.15f')
format(b, '0.26f')
Fraction(b)
x = Fraction(0.3)
x.limit_denominator(10)

x = Fraction(math.pi)
x
float(x)
x.limit_denominator(10)
22/7
x.limit_denominator(10000)
355/113

######################## Floats
#########################################################################
help(float)
float(10)
float('12.5')
float('22/5')
from fractions import Fraction
a = Fraction('22/6')
float(a)

print(0.1)
format(0.1, '.15f')
format(0.1, '.20f')
print(0.125)
0.125.as_integer_ratio()

1/8
format(0.125, '.25f')
a = 0.1 + 0.1 + 0.1
b = 0.3
a == b
format(a, '.25f')
format(b, '.25f')


##################################################
######### Floats equality testing

x = 0.1
format(x, '.25f')
print(x)
x = 0.125
format(x, '.25f')

x = 0.125 + 0.125 + 0.125
y = 0.375
x == y

x = 0.1 + 0.1 + 0.1
y = 0.3
x == y


format(x, '.25f')
format(y, '.25f')
round(x, 3) == round(y, 3)
a = round(x, 5)
format(a, '.3f')

x = 10000.01
y = 10000.02

delta = y - x
delta
y/x

x = 0.01
y = 0.02

y / x

round(x, 1) == round(y, 1)

from math import isclose
help(isclose)


x = 0.1 + 0.1 + 0.1
y = 0.3
x == y
isclose(x,y)

x = 1212121212112.01
y = 1212121212112.02
isclose(x, y, rel_tol=0.001)

x = 0.0000001
y = 0.0000002
isclose(x, y, rel_tol=0.001, abs_tol=0.001)

y - x

a = 123456789.01
b = 123456789.02
print(isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
b - a
print(isclose(a, b, abs_tol=0.001, rel_tol=0.01))


############# Coerse Float to Integer
#### trunc - plucks the decimal out
#### int does the same for floats
#### floor leaves the smalles integer (differs from trunc with negative numbers)
#### ceiling leaves the largest integer from the float

from math import trunc, floor, ceil

trunc(10.3), trunc(10.5), trunc(10.9)

int(10.3), int(10.5), int(10.9)
floor(10.3), floor(10.5), floor(10.9)

ceil(10.3), ceil(10.5), ceil(10.9)

floor(-10.3), floor(-10.5), floor(-10.9)
ceil(-10.3), ceil(-10.5), ceil(-10.9)

round(2.6, 0) # searches multiples of 1
round(1.25, 1) # searches multiples of 0.1
round(1.35, 1) # searches multiples of 0.1
round(15, -1) # searches multiples of 10 (10 to the power of (-10))
round(25, -1) # searches multiples of 10


#######################################################################
########### rounding

a = round(1.9)
a, type(a)
a = round(1.9, 0)
a, type(a)

n > 0
round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0)

# 3 decimals, 2 decimals, 1 decimal and zero (or a multiple of one)

#### n < 0

round(888.888, 1), round(888.888, 0), \
round(888.888, -1), round(888.888, -2), round(888.888, -3), round(888.888, -4)

## one decimal, zero decimals, round to 10, round to 100, round to 1000 and
# round closer to zero because it's the closest multiple of 10000 as
# rounding to 10 to the power of -4 means rouding to the closest 10000


###### Ties
round(1.25, 1)
round(1.35, 1)
#### again the bankint in work - rounding to the closest even number
#### and in the first case, the 1.2 is even and 1.3 is not, therefore 1.25
#### becomes 1.2 and not the expected 1.3


def _round(x): # rounding to the integral value
    from math import copysign
    return int(x + 0.5 * copysign(1, x)) # copysign(1, x) multiplies sign of x by 1


round(1.5), _round(1.5)
round(2.5), _round(2.5)
round(-2.5), _round(-2.5)

round(10.5)


#########################################################################
############ Decimals ###################################################

import decimal
from decimal import Decimal

decimal.getcontext().rounding
decimal.getcontext().prec = 6
decimal.getcontext()
g_ctx = decimal.getcontext()
type(g_ctx)
g_ctx.rounding = decimal.ROUND_HALF_UP
g_ctx

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN

decimal.localcontext()
with decimal.localcontext() as ctx:
    print(type(ctx))
    print(ctx)


with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print(decimal.getcontext())
    print(id(ctx) == id(decimal.getcontext()))


x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx: # executred locally - disappears after
    # the with bloc is over
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1))
    print(round(y, 1))

# executed globally. on the lever of the module
print(round(x, 1))
print(round(y, 1))


import decimal
from decimal import Decimal

help(Decimal)
Decimal()
Decimal(10)
Decimal(-10)
Decimal('10.2')
Decimal('-10.56')
# passing decimal from tuples. firstt arg 0 = negative, 1 - positive 
t = (0, (3,1,4,1,5), -4)
t2 = (0, (3,1,4,1,5), -3)
Decimal(t)
Decimal(t2)

format(0.1, '.25f')
Decimal(0.1)

Decimal('0.1')
Decimal('0.1') == Decimal(0.1)
Decimal(10) == Decimal('10')

### contenxt

decimal.getcontext()
decimal.getcontext().prec = 6
a = Decimal('0.123456789')
b = Decimal('0.123456789')

a, b
a + b

0.123456789 + 0.123456789

a = Decimal('0.123456789')
b = Decimal('0.123456789')

print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))

print('c within global context: {0}'.format(c))


###### div and mod 
 ##  n = d * (n//d) + (n%d)

x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))


x = Decimal(-10)
y = Decimal(3)

print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))


x = Decimal(-10)
y = Decimal(3)

print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

decimal.getcontext().prec = 28
a = Decimal('1.5')
print(a.ln())
print(a.exp())
print(a.sqrt())


import math

a = Decimal('0.1')
print(a.sqrt())
print(math.sqrt(a))


x = 2
x_dec = Decimal(2)
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)


x = 0.01
print(format(x, '.27f'))

x_dec = Decimal('0.01')
print(x_dec)
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

################# Decimals - Performance

import sys
a = 3.1415
b = Decimal('3.1415')

sys.getsizeof(a)
sys.getsizeof(b)

import time
def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')

n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)

##################
import time
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a
        

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a
        

n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)


#######################

import math
n = 5000000

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)
        

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()
        

n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)


start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('float: ', end-start)

###########################################################
###### Boolean ############################################


help(bool)
issubclass(bool, int)

type(True), id(True), int(True)
type(False), id(False), int(False)

3 < 4
type(3 < 4)
id(3 < 4)
(3 < 4) == True
(3 < 4) is True

None is False
(1 == 2) == False
(1 == 2) is False
1 == 2 == False ## careful with this chain comparison
# the code above checks:
1 == 2 and 2 == False

int(True), int(False)
1 + True
100 * False
True > False
(True + True + True) % 2
-True
bool(0)
bool(1)

bool(100)
bool(-100)
#### any integer other than 0 has the value of True

## every object in Python evaluates to True except:
## None, False, 0 in any form
## empty list, tuple, string, dictionary, set
## custom classes that implement a __bool__ or __len__ method that returns False or 0

bool(1)
bool(0)
bool(-2)

help(bool)
bool(100)
(100).__bool__()
a = []
bool(a.__len__())


bool(0.0), bool(0+0j)

from decimal import Decimal
from fractions import Fraction

bool(Fraction(0,1)), bool(Decimal('0.0'))
bool(10.5), bool(Fraction(1, 3)), bool(Decimal('2.4'))

a = []
b = ''
c = ()

bool(a), bool(b), bool(c)

a = [1, 2, 3]
b = '1, 2, 3'
c = (1, 2, 3)
bool(a), bool(b), bool(c)

a = {}
b = set()

bool(a), bool(b)


a = {'cat' : 23}
b = {1, 2}

bool(a), bool(b)

bool(None)

########## two way to write the same logic
a = [1,2,3]
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('Nothing to see here...')

## now with boolean logic

if a:
    print(a[0])
else:
    print('Nothing to see here...')


a = [1,2,3]
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('Nothing to see here...')


##########################################################
#### Boolean operators
# Operator Precedence
# ()
# <> <= >= == != in is
# not
# and
# or

not --> and --> or

True or True and False

True or (True and False)

(True or True) and False

# True or Y --> always True
# False and Y --> always False

a = 10
b = 2

if a /b > 2:
    print('a is at least twice b')
#################
a = 10
b = 0
# b = None

if a /b > 2:
    print('a is at least twice b')
###############
if b > 0 and a/b > 2:
    print('a is at least twice b')

##########################

if b and a/b > 2: # even shorter version - short-cicuit
    print('a is at least twice b')

import string
help(string)

a = 'c'
a in string.ascii_uppercase
a in string.ascii_lowercase

name = 'Bob'
if name[0] in string.digits:
    print('name cannot start with a digit')

name = '' # if it's an empty string, it'll return an error
if name[0] in string.digits:
    print('name cannot start with a digit')

name = '' # if it's an empty string, it'll return an error
if len(name) > 0 and name[0] in string.digits:
    print('name cannot start with a digit')

name = '' # if it's an empty string, it'll return an error
if name and name[0] in string.digits:
    print('name cannot start with a digit')


##########################################################
######## Boolean Operators

# X or Y: if X is truthy, returns X, otherwise evaluates and returns it
'a' or [1,2]
'' or [1,2]

1 or 1/0  # doesn't even checks the 1/0 since 1 is truthy
0 or 1/0 # evaluates the 1/0 since 0 is truthy

# this pattern can be used for setting up default values
s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'

print(s1, s2, s3)

[] or [0]
None or [0]

######### and
# X and Y: if X is falsy, returns X, otherwise evaluate and return Y


None and 100

[] and [0]
# for example it can be used to avoid division by zero
#

# return zero if b == 0 , else evaluate and return a/b
a = 2
b = 0
# b = 4

b and a/b

###
# None or empty string or check the first charachter in string if exists

s1 = None
s2 = ''
s3 = 'abc'

print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])
## add condition if None or empty, set default value as '' - empty string
print(s1 and s1[0] or '')
print(s2 and s2[0] or '')
print(s3 and s3[0] or '')

## add condition if None or empty, set default value as 'n/a' - empty string
print(s1 and s1[0] or 'n/a')
print(s2 and s2[0] or 'n/a')
print(s3 and s3[0] or 'n/a')


############### not operator

not True
not False

bool('abc')

not bool('abc')
not bool()

## the same
not 'abc'
not ''

not bool(None)
not None

###############################################################
####### Comparison Operators

0.1 is (3 + 4j)

3 is 3
[1,2] is [1,2] # False

'a' in 'this is a test'
3 in [1,2,3]

3 not in [1,2,3]

'key1' in {'key1' : 1} # checks only the key, hence True
1 in {'key1': 1} # False as only cheks keys in dictionaries

3 < 5

1 + 1j < 3 + 4J # can't use comparison < or > with mix complex numbers 
# but the == sometimes can be used
from decimal import Decimal
from fractions import Fraction

Fraction(2,3) < Decimal('0.5')
4 == 4 + 0j

True == Fraction(2,2)

True < Fraction(3,2)


1 < 2 < 3
1 < 2 and 2 < 3


3 < 2 < 1/0 # it evaluates first part as False and doesn't even go to
# the second one even though it's mathematically wrong (no div by zero) 
3 < 2 and 2 < 1/0

3 < 4 < 1/0

1 < 2 > -5

1 < 2 > -5 == Decimal('-5.0')

import string

'A' < 'a' # I don't get it for now
string.ascii_letters

'A' < 'a' < 'z' > 'Z' in string.ascii_letters

min  = 0
max = 100
age = 34
min < age < max


#######################################################
### Functions

def my_func(a, b, c):
    print('a={0}, b={1}, c={2}'.format(a, b, c))

my_func(1,2,3)

def my_func(a, b=2, c=2):
    print('a={0}, b={1}, c={2}'.format(a, b, c))

my_func(10, 20, 30)

my_func(10, 20)

my_func(10)

def my_func(a=1, b=2, c=3):
    print('a={0}, b={1}, c={2}'.format(a, b, c))

my_func()


###########################################################
####### keyword parameters

def my_func(a, b=2, c=3):
    print('a={0}, b={1}, c={2}'.format(a, b, c))

my_func(c=30, b=20, a=10) # even with wrong oder, it works correctly
## because we use named arguments here

my_func(10, c=20, b=10)

 my_func(10, c=30)

##########################################################
#### Upacking tuples, lists, or any iterables

a = (1,2,3)
type(a)

a = 1, 2, 3
type(a)
a
a = (1) # not a definition of tuple, it's the coma that does it

a = 1,
a
a = (1,) # it's the same as without parens, just easier to read

type(a)

a = , # no
a = (,)  # no

a, b, c = [1, 'a', 3.14]
a
b
c
(a, b, c) = [1, 'a', 3.14] # the same as before

a, b = (1, 2)
a
b

a, b = 10, 20 # remeber, it's the comma that makes the tuple, 
# not the parens
a

a,b,c, = 10, {1, 2}, ['a', 'b']
a
b
c

######### swap variables

a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)

for e in 'XYZ':
    print(e)

a, b, c = 'XYZ'
a
b
c

s = 'XYZ'
s[0]

s = {1, 2, 3}
s[0] # doesn't work since sets don't have this functionality

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)

for e in s:
    print(e)

a, b, c, d, e, f = s # sets unpacked not in order, since they're not ordered
a
b

d = {'a':1, 'b':2, 'c':3}
for e in d:
    print(e)

a,b,c = d
a
b

d = {'a':1, 'b':2, 'c':3, 'd':4}
a,b, c, d = d

a
b
d, a, b, c = d
d
a
b
c
# sets and dictionaries are unordered types, therefore what might
# come back after iterating through it, might not alwayse come
# in the same order as it was input originally

for e in d:
    print(e)

d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d.values():
    print(e)

a, b, c, d = d.values()
a

d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d.items():
    print(e)

for e in d.items():
    a, b = e
    print(f'key={a}, value={b}')


for a, b in d.items():
    print(f'key={a}, value={b}')



#######################################################
##### unpacking using slices and extended unpacking with * !!!!!!!
##### important note: 
##### slicing only workd with indexable/subscriptable iterables
##### extended unpacking works with any iterable


l = [1,2,3,4,5,6]

a = l[0]
b = l[1:]

print(a)
print(b)

a, b = l[0], l[1:]
print(a, b)

a, *b = l
a
b

# with sets or dictionaries we can't use slicing
# as they don't have a concept of ordering
s = {1,2,3}
a = s[0]
b = s[1:]
## error

s = 'python'
a, *b = s
a
b
# to pack list into a string again
b_string = ''.join(b)
b_string

t = ('a', 'b', 'c')
a, *b = t
a
b

# unpacking to a lists
[a, b, c] = 'XYZ'
a
b

a, b, *c = 'python'
a
b
c

a, b, *c, d = 'python'
c
d
a, b, c, *d, e, f, g = 'a brown fox jumped over a lazy dog'
d
## note: words are not the units in a string, characters are

a, b, *c, d = s
a
b
c
d

### slicing is a bit more complicated
### but the slicing returns a string back, not a list as ectended unpacking

a, b, c, d = s[0], s[1], s[2:-1] , s[-1]
a
b
c
d
# now tha c is a string, if we want to have it as a list, we unpack it too
# since unpacking always generates a list, here we create a tuple
# of one element (by adding a comma and nothing after it)
*c, = c
list(c)

### unpacking two lists into one
l1 = [1,2,3]
l2 = [4,5,6]

l = [*l1, *l2]
l

l1 = [1,2,3]
s = 'abc'
[*l1, *s]


l1 = [1,2,3]
s1 = {'x', 'y', 'z'}

[*l1, *s1]
[*'python']
st = 'python'
[*st]
list('python')


## pack back into a string
b_string = ''.join([*'python'])

b_string = ''.join(s1)

##################
s1 = 'abc'
s2 = 'cde'

[*s1, *s2]
{*s1, *s2}

### sets remove the repeated values

s = {10, -99, 3, 'd'}
for c in s:
    print(c)


a,b,c,d = s
print(a,b,c,d)

a,b, *c = s
## there is no ordering in sets so doing the type of unpacking 
## as abofe is not too useful as it'll make assignement arbitrarily

a
b
c
### transform set into a list

list(s)
## or we can unpack it

*c, = s
c

s1 = {1,2,3}
s2 = {3,4,5}

*s1, *s2 # without parens it creates a tuple because we used a comma
{*s1, *s2}

### orr we can use a standard method union on set
s1.union(s2)


s1 = {1,2,3}
s2 = {3,4,5}
s3 = {5,6,7}
s4 = {7,8,9}

s1.union(s2).union(s3).union(s4)

s1.union(s2,s3,s4)

## or unpack it to a set or a list
{*s1, *s2, *s3, *s4}
[*s1, *s2, *s3, *s4]


d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}

# inpacking a dict will result in unpacking dict's keys into a set
{*d1, *d2}

# to unpack both keys and the values we use **
{**d1, **d2}

# we can upack dict while creting a new dict :)
{'a': 1, 'b': 2, **d1, 'c': 3}


## nested unpack
a, b, e = [1, 2, 'XY']

a
b
e
c, d = e
c
a, b, (c, d) = [1, 2, 'XY']
c

###################
a, b, (c, d, *e) = [1, 2, 'python']
d
e

l = [1,2, 3, 4, 'python']
a, *b, (c, d, *e) = l
print(a, b, c, d, e)

# now using slicing
a, b, c = l[0], l[1:4], l[-1]
a
b
c
a, b, c, d, e = l[0], l[1:4], l[-1][0], l[-1][1], l[-1][2:] 
a
b
c
d
e

print(a, b, c, d, e)

a, b, c, d, e = l[0], l[1:4], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)
 

####### now instead of a list we use a tuple
l = (1,2, 3, 4, ['a', 'b', 'c', 'd'])

a, *b, (c, d, *e) = l
print(a, b, c, d, e)

## slicing works here too since they're both indexable/subscriptable,

a, b, c, d, e = l[0], l[1:4], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)

## but if want the same output format as above, we need convert it to a list
## that is, 'b' expressed as a list and not a tuple
a, b, c, d, e = l[0], list(l[1:-1]), l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)

#################################################################

#### *args with functions

a, b, *c = 10, 20, 'a', 'b'
a
b
c
def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

func1(10, 20) # it's ok to have only 2 params as *s is not a mandatory 
## and there can be any amount of these params after the two mandatory ones
func1(10, 20, 1, 2, 3, 4, 5) # the rests of params become a tuple

func1(a, b, c)

def avg(*args):
    print(args)


avg(10, 20)

avg(1, 2, 6, 0, 0, 'tonto')


def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count
    # print(total/count)


avg(10, 20, 30, 44, 55, 4.45)
avg(2,2,4,4)

avg() # if called with no params, it will crash with "division by zero"

def avg(*args):
    count = len(args)
    total = sum(args)
    if not args:
        return 0
    else: 
        return total/count

## other way to do the same
def avg(*args):
    count = len(args)
    total = sum(args)
    if not args:
        return 0
    else: 
        return total/count

## or below using boolean 'and' logic to set up a default value
## and avoid the if statement
### awesome ! it reduces the code by three lines
def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count


avg()
avg(2,2,4,4)

## or force user to specify to input at least one parameter
def avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count

avg() # now the error is not a division by zero, but a missing parameter
avg(2,2,4,4)

### unpack iterable into a positional argument
def func1(a, b, c):
    print(a)    
    print(b)
    print(c)

l = [10, 20, 30]

func1(l) # we can pass the list with three items, we need to unpack it

func1(*l) ### beauty!!

func1(10, 20, 30, 40) # if we pass more params, it'll break
                      # so to avoid it, we can add *args
                      # this way there won't be any errors in number of params


def func1(a, b, c, *args):
    print(a)    
    print(b)
    print(c)
    print(args)

l = [10, 20, 30, 40, 50]

func1(*l)

#############################################################
## Keyword agruments 
def func1(a,b,c):
    print(a,b,c)

func1(1,2,3)

func1(1, c=3, b=2)

func1(c=3, b=2, a=1)


def func1(a,b,*args, d):
    print(a,b, args, d)

func1(1, 2, 3, 4, 5) # will not work as no positional arguments are 
### allowed after args
### we need either remove 'd' from the function definition, 
### or add 'd' as a named argument when calling the function

func1(1, 2, 3, 4, 5, d=10)

def func1(*args, d):
    print(args, d)

func1(1, 2, 3, d='a')

func1(d='a') # still ok since *args can be empty

def func1(*, d): # still valid. the * indicates the end of positional
### arguments 
    print(d)

func1(1,2,3, d=10) # error as I gave 3 pos arguments
func1(19) # error since the funcion definition stipulates no pos arguments
########### but does demands one keyword argument
func1(d=10)

def func(a,b, *, d):
    print(a, b, d)


func(1, 2, d=3)# ok
func(1, 2, 3, d=5) # error as I gave more than 2 pos parameters

def func(a, b=2, *args, d):
    print(a, b, args, d)

func(1, 5, 3, 4, d='a') # here b is the second pos agrument, 
### therefore even though it has a default value, since the second
### argument is 5, b takes the value of this 5. 
### args is (3,4) and d = 'a'
### everything that comes after *args is a keyword argument

def func(a, b= 20, *args, d=0, e):
    print(a, b, args, d, e)

func(5, 4, 3, 2, 1) # error as required keyword argument 'e' was not passed

func(5, 4, 3, 2, 1, e='are you talking to me?')

func(0, 600, d='goood morning', e='vitnam!')# args is empty here
### as it it's not mandatory for args to be filled with somethin

func(11, 'm/s', 24, 'mph', d='unladen', e='swallow')

####################################################################
######### **kwargs ###################################################
def func(**others):
    print(others)


func(a=1, b=2, c=3)

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, x=100, y=200)

def func(a, b, *, **kwargs): # error - can only use named (d=20) keyword
##### arguments after a single * , but not **kwargs since they are not named, but
##### takes all the keyword agruments into one place

def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)

func(1, 3, 'tonto', d=1, e='cuanto te echo de menos', f=2) # error
### one pos agrument extra - 'tonto'

func(1, 3, d=1, e='cuanto te echo de menos', f=2)
func(1, 3, e='cuanto te echo de menos', f=2, d=1)# order doesn't matter
### as it's a named argument

def func(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)

func(1, 2, x=100, y=200)


############################################
def func(a,b, *args):
    print(a, b, args)


func(1, 2, 'x', 'y', 'z')

func(a=1, b=2, 'x', 'y', 'z') # error as we use keyword arguments 
###                             before we use positional and it needs
###                             to be other way around

def func(a, b=4, c=5, *args):
    print(a, b, c, args)

func(1, 2, 3, 'x', 'y', 'z')

func(1, 5, 'x', 'y', 'z')

def func(a, b=2, *args, c=3, d):
    print(a,b, args, c, d)

func(10, 20, 'x', 'y', 'z', c=4, d=1)
func(10, 20, 'x', 'y', 'z', d = 10)

func(1, 'x', 'y', 'z', b=4, d=10)
## error since 'b' has alreay been assigned the value of 'x' and later
## the value of 2, therefore it breaks

def func(a, b, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)

func(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)


 print(1, 2, 3, sep='-')
 print(4, 5, 6, sep='-', end=' *** ')


#########################################
### find min, max and their average

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    
    # lo = int(bool(args)) and min(args) # using boolean logic
    # using the good old if, else
    if len(args) == 0:
        lo = 0
    else:
        lo = min(args)

    ### using turnery operator
    # lo = min(args) if len(args) > 0 else 0
    lo = min(args) if args else 0

    ## average
    avg = (hi + lo)/ 2
    if log_to_console:
        print(f'high={hi}, low={lo}, avg={avg}')
    return avg


avg = calc_hi_lo_avg(1, 2, 3, 4, 5)
print(avg)     

avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)

is_debug = True # using the debug flag and later passing it to the func
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=is_debug)
print(avg)



def func(*, ): # maybe you want to use keyword only parameters
    pass

################################################################

### A Simple Function Timer
import time
def time_it(fn, *args, **kwargs):
    print(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' *** ')

#### above just prints arguments but don't execute anything
#################################
def time_it(fn, *args, **kwargs):
    fn(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' *** ')
### this will not work as it will interpret it as arguments for
### the print function. fn becomes print and it prints what it inside 
### args and kwargs treating the contents as two tuples of underlying
### values

### for it to work, we need to unpack the args and kwargs so the
### fn takes as arguments the content of args and kwargs
def time_it(fn, *args, **kwargs):
    fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' *** ')

############################################
def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' *** ', rep=5)
time_it(print, 1, 2, 3, sep=' - ', end=' *** \n', rep=5)

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep
    # print(f'it took: {end - start} to run')
    
time_it(print, 1, 2, 3, sep=' - ', end=' *** \n', rep=5)


#####################################################

def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)

    return results

compute_powers_1(2, end=5)


#######################################################
def compute_powers_2(n, *, start=1, end):
    # using list comprehension
    return [n**i for i in range(start, end)]

compute_powers_2(2, end=5)

########################################################
def compute_powers_3(n, *, start=1, end):
    # using generators
    return (n**i for i in range(start, end))

compute_powers_3(2, end=5) # generators do not show immediate results
list(compute_powers_2(2, end=5))

### now time it
def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep
    # print(f'it took: {end - start} to run')



time_it(compute_powers_1, 2, end=20000, rep=5)

time_it(compute_powers_2, 2, end=20000, rep=5)

time_it(compute_powers_3, 2, end=20000, rep=5)

### we can specify n by naming it too. Even thogh it's a pos argument
### we can still specify it, but it will get absorbed by **kwargs
time_it(compute_powers_3, n=2, end=20000, rep=5)

### generator doesn't generate results when the funcion is called
### to see it's data we need to convert it to a list or something else
### but it's quite quick 

a = (2**i for i in range(5))
list(a)

def compute_powers_4(n, *, start=1, end):
    # using generators

    return list((n**i for i in range(start, end)))

compute_powers_4(2, end=5)

time_it(compute_powers_4, 2, end=20000, rep=5)


##########################################################
######### default value = beware!
######### careful with mutable and immutable types
from datetime import datetime

datetime.utcnow()
print(datetime.utcnow())

### because the code is read at the time of importing a module or packge
### or the function creation
### the below default parameter dt, will be read at the moment of
### the function creaton and will not change when we call it.
### therefore a trick is needed
def log(msg, *, dt=datetime.utcnow()):
    print(f'{dt} : {msg} ')


log('message 1', dt='2001-01-02 00:00:00.000')


log('message 1', dt='2011-01-02 00:00:00.000')


log('message 2')  # the same default value even for utcnow()

log('message 3')  # the same default value even for utcnow()

##############
### now we use defaut value of None and assign the value later
### this will produce the correct result
def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f'{dt} : {msg} ')

log('message 3')
log('message 3', dt='2011-01-02 00:00:00.000')
log('message 3', dt=None)

###############################
my_list = [1, 2, 3]
def func(a=my_list):
    print(a)

func(a)
func(['a', 'b'])

########### if I change the list and later call the func again
########### it will have the new list, not the original one 
########### even though I put as the default in the func definition

my_list.append(4)
func()

############# the solution to this is to use a tuple instead of 
############# the list as the tuple can't be changed
my_list = (1, 2, 3)
def func(a=my_list):
    print(a)

my_list.append(4) # error as append and tuple are not friends
my_list


#################################################################
def add_item(name, quantity, unit, grocery_list):
    grocery_list.append(f'{name} ({quantity} {unit})')
    return grocery_list



store1 = []
store2 = []

add_item('banana', 2, 'units', store1)
add_item('milk', 1, 'litre', store1)

add_item('python', 1, 'medium-rare', store2)

##### in case above I defined the store as a list before running a function
##### let's make it easier
##### if the store/grocery list is not provided, it will be created !

def add_item(name, quantity, unit, grocery_list=[]): # we start an empty list
    grocery_list.append(f'{name} ({quantity} {unit})')
    return grocery_list

del store1
del store2

store1 = add_item('banana', 2, 'units')
store1 = add_item('milk', 1, 'litre')


store2 = add_item('python', 1, 'medium-rare') 

##### the problem is that now we have the same information in both variables:
##### store1 and store2, wtf?
##### the memory addresses are the same!!  

##### how to deal with it....
##### during the function definion, do not use mutable default types

def add_item(name, quantity, unit=1, grocery_list=None): # we start an empty list
    # if not grocery_list:
    #     grocery_list = []
    grocery_list = grocery_list or []
    grocery_list.append(f'{name} ({quantity} {unit})')
    return grocery_list

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'litre', store1)

print(store1)

store2 = add_item('python', 1, 'medium-rare') 
print(store2)

store1 is store2 # to check if the two have same memory address

##################################################################
## now a situation where we might want have a datastructure or a variable keeping
## an initial value that was defined at the time of the code being first run or imported
## side note: the concept of factorials is confusing.....
def factorial(n):
    if n < 1:
        return 1
    else:
        print(f'calculating {n}!')
        return n * factorial(n-1)

factorial(3)



###  the same as above but using the concept of cashe = !confusing for me!

def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f'calculating {n}!')
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result

cache = {}

factorial(3, cache=cache)

cache[3]

factorial(3, cache=cache)

factorial(4, cache=cache)

#### the above is very user friendly code or very efficient
#### every time we run this function, we need to remember and ask to
#### run it while defining cache all the time
#### let' change it so we have a defalt value

def factorial(n, cache={}): # now we define the dict automaticaly if not passed
    # it's important the fact that dict is mutable and in this case
    # it's important to have it initialised to an empty {} and not None
    # as the use case calles for the values to be kept saved in that 
    # variable cache and not overwritten as in case of assigning it to
    # None as in the previous cases
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f'calculating {n}!')
        result = n * factorial(n-1)
        cache[n] = result
        return result

factorial(3)

factorial(3)
factorial(4)

##############################################################

### Docstrings and annotations

help(int)

def my_func(a, b=1):
    """this is a func that returns a * b
       docs here
    """

    return a * b

help(my_func)

my_func.__doc__

def my_func(a: 'annotation for a',
            b: 'annotation for b' =1) -> 'something':
    """Documentation for my_func"""
    return a * b

help(my_func)
my_func.__doc__
my_func.__annotations__

x = 30
y = 5
def my_func(a: 'some character', b= max(x,y)) -> 'character a repeated ' + str(max(x,y)) + ' times':
    print(b)
    return a * max(x,y)

my_func('a')
my_func.__annotations__ # it will actually calculate the math in the annotation
# need to be careful with the default valuus as in the above chapters
# as if we use a formula or calculation in the annotation, it will get
# evaluated during the function creation step and will stay the same
# as the very first set of value for the vars x and y and will not change
# if the x and y do

def my_func(a: str,
            b: 'int > 0' = 1,
            *args: 'some extra pos args',
            k1: 'keyword-only arg 1',
            k2: 'keyword-only arg 2' = 100,
            **kwargs: 'some extra keword-only args' ) -> ' something':

    print(a, b, args, k1, k2, kwargs)

my_func.__annotations__

my_func(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)

###############################################################
###### lambda expressions 

def sq(x):
    return x**2

type(sq)

sq

lambda x: x**2

lambda x,y: x+y

f = sq
id(f), id(sq)

f(3)
sq(3)
f

f = lambda x: x**2
f(3)

g = lambda x, y =10: x+y
g
g(1, 2)
g(1)

f = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
f()
f(1, 'a', 'b', y=100, a=10, b=20)

def sq(x):
    return x**2

def apply_func(x, fn):
    return fn(x)

apply_func(5, sq)

apply_func(5, lambda x: x **2)

apply_func(5, lambda x: x**3)

def apply_func(fn, *args, **kwargs):
    # return fn(args, **kwargs) # we can't use it this way, we need to unpack
    return fn(*args, **kwargs)

apply_func(sq, 3)

# or we can do the same with lambda below
apply_func(lambda x: x**2, 3)

apply_func(lambda x, y: x + y, 1, 2)

apply_func(lambda x, *, y: x+y, 1, y=20)

apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)

apply_func(sum, 1, 2, 3, 4, 5) # this will not work bcause fn sum expects a tuple
apply_func(sum, (1, 2, 3, 4, 5)) # this will work
sum(1, 2, 3, 4, 5) # sum works with 2 arguments max, so we need to put it in a tuple
sum((1, 2, 3, 4, 5))

##################################################
### lambdas ans sorting
help(sorted)

l = 1, 5, 4, 10, 9, 6
sorted(l)
l # l stays the same. sorted() returns a sorted l, but doesn't change the l itself

l = ['c', 'B', 'D', 'a']
sorted(l)

ord('a')
ord('A')

sorted(l, key=lambda s: s.upper()) # we use lambda function as key to change the functionality of
# sorting !! pretty awesome

d = {'abc': 200, 'def': 300, 'ghi': 100}
d
for e in d:
    print(e)

sorted(d)

sorted(d, key=lambda e: d[e])

####
def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

dist_sq(1+1j)

l = [3+3j, 1-1j, 0, 3+0j]

sorted(l) # ordering doesn't support complex numbers

sorted(l, key=dist_sq) # here we're using fn dist_sq as the key because it produces a list of 
#### numbers and sorts accordingly to that list
#### we can also do it with lambda


sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2) # just copy paste the return from dist_sq()

##### 
a = ['hasta', 'la', 'vista', 'baby']
sorted(a, key=lambda x: len(x)) # the letter used after word lambda has to be used in expresion,
# the content of the var a is automatically passed to the funcion

l = ['Cleese', 'Idle', 'Palin', 'Gilliam', 'Jones', 'Champan', 'Palin']
sorted(l)

### sort by the last letter in each word

sorted(l, key=lambda x: x[-1]) # it goes through each value of the list l because the fn sorted()
### does it in its definition. It doesn't mean each fn will apply the for loop automatically

l = [1, 2, 3, 4, 5]
import random

sorted(l, key=lambda x: random.random())

###################################################################
### Function Introspection

def my_func(a: 'mandatory pos param',
            b: 'optional pos' =1, # very important! after assigning a default value to 
            ####################### a positional param, all following pos params
            ####################### must also have defaut values
            c: 'optional pos' =2,
            *args: 'add extra pos here',
            kw1: 'mandatory keyword param',
            kw2: 'optional keyword param' =100,
            kw3: 'optional keyword param' =200,
            **kwargs: 'optional extra keyword only params') -> 'does nothing':
    """
    This function does nothing but does have
    various parameters and annotations
    """
    i = 10
    j = 20


my_func.__doc__
my_func.__annotations__ 
# we can create a var attached to this function like below
my_func.short_description = 'this is a functin that does nothing much'

my_func.short_description

id(my_func)

dir(my_func)
my_func.__name__

def func_call(f):
    print(id(f))
    print(f.__name__)

func_call(my_func)


my_func.__defaults__ # returns the default values of the positional parameters
my_func.__kwdefaults__ # returns the default values of the keyword only parameters

my_func.__code__
dir(my_func.__code__)

my_func.__code__.co_name
my_func.__code__.co_varnames # lists all the param and local vars - only local vars

my_func.__code__.co_argcount # careful - only shows positional agruments

# import inspect
from inspect import isfunction, ismethod, isroutine
a = 10
isfunction(a)
isfunction(my_func)

ismethod(my_func)

class MyClass:
    def f(self):
        pass

isfunction(MyClass.f) # True because it's a fn of a class
ismethod(MyClass.f) # False as there is no instance of that class yet

my_obj = MyClass()

isfunction(my_obj.f) # False because there is already an obj to which this fn belongs
ismethod(my_obj.f) # True as there is already an object, therefore this fn is bound to it
#################### meaning, the fn became a method

isroutine(my_obj.f) # an fn and a method are both routines
isroutine(MyClass.f) # an fn and a method are both routines


### let's add a couple of lines of code to the same fn

# TODO: Fix this function  - it can be read later through inspect.getcomments()
# more sample text
def my_func(a: 'mandatory pos param',
            b: 'optional pos' =1, # very important! after assigning a default value to 
            ####################### a positional param, all following pos params
            ####################### must also have defaut values
            c: 'optional pos' =2,
            *args: 'add extra pos here',
            kw1: 'mandatory keyword param',
            kw2: 'optional keyword param' =100,
            kw3: 'optional keyword param' =200,
            **kwargs: 'optional extra keyword only params') -> 'does nothing':
    """
    This function does nothing but does have
    various parameters and annotations
    """
    i = 10
    j = 20
    a = i + j
    return a 


import inspect
inspect.getsource(my_func) # returs all the code as a string
print(inspect.getsource(my_func))

## we still can assign a fn to a var and get the same data
f = my_func
print(inspect.getsource(f))

inspect.getmodule(my_func) # shows where the fn lives
inspect.getmodule(print)

import math
inspect.getmodule(math.sin)

inspect.getcomments(my_func) # should return the comment immediately above the fn,
############################## but for some reason doesn't work in interactive python
############################## in VSCODE

############ signature

inspect.signature(my_func) # it returns attrubutes and we can use __dir__ to read them

dir(inspect.signature(my_func))


dir(inspect.signature(my_func))
my_func.__annotations__
inspect.signature(my_func).return_annotation

sig = inspect.signature(my_func)
sig.parameters
for k, v in sig.parameters.items():
    print(k, type(v)) # v is a Parameter object, meaning it has properties 
    ################## we can check these properties with __dir__

for k, param in sig.parameters.items():
    print('Key:', k)
    print('Name:', param.name) # name is one of properties of th object Parameter
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind:', param.kind)
    print('-----------------------------')



### simplify
for param in sig.parameters.values():

    print('Name:', param.name) # name is one of properties of th object Parameter
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind:', param.kind)
    print('-----------------------------')




### positional only parameters
help(divmod) # example - the '/' sign means only positional params before the /
for param in inspect.signature(divmod).parameters.values():
    print(param.kind)

### it's an internal python option - we can't create positional only params in our code

###########################################################################
#### Callables 
##############
callable(print)

## every callable returns a value
result = print('hello')
print(result)

l = [1, 2, 3]
callable(l.append)
result = l.append(4)
print(result)

s = 'abc'
callable(s.upper) # True, but be careful not to add the ()
callable(s.upper()) # False
result = s.upper()
print(result)

from decimal import Decimal
callable(Decimal)

a = Decimal('29.65')
a
## all classed are callable, but not all the instances are callable

class MyClass:
    def __init__(self, x=0):
        print('initialing...')
        self.counter = x
        

callable(MyClass) # the class is callable

a = MyClass(100)
a.counter
callable(a) # False but the instance is not

## let's make sure the instances are also callable
class MyClass:
    def __init__(self, x=0):
        print('initialing...')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x

b = MyClass()
c = MyClass # careful with ending with () or not, when you add () it runs the class 
############# and initalizes it
callable(b)
MyClass.__call__(b, 10)
b.counter
callable(b)
b()


