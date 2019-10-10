
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
sfasdfsdf
sdfsdaf



