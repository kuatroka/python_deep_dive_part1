# min_length = 2
# name = input(' Please enter your name:')

# while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
#     name = input(' Please enter your name:')

# print('Hello, {0}'.format(name))



##############
min_length = 2
while True:
    name = input(' Please enter your name:')
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print('Hello, {0}'.format(name))