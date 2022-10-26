# Functions Practice Part 3

#1 name_args
def name_args(**args):
    for i in args:
        print(f'{i}: {args[i]}')

print('1.)')
name_args(name='Bob', age=25, job='dev')
print(' ')

#2 all_true
def all_true(iterable):
    # for i in iterable:
    #     if not i:
    #         return False
    # return True
    return all(iterable)

print('2.)')
print(all_true([True, True, True]))
print(all_true([True, False, True]))
print(' ')

#3 one_true
def one_true(iterable):
    # for i in iterable:
    #     if i:
    #         return True
    # return False
    return any(iterable)

print('3.)')
print(one_true([True, True, False]))
print(one_true([False, False, False]))
print(' ')

#4 recursive_factorial
def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print('4.)')
print(recursive_factorial(5))
print(recursive_factorial(10))
print(' ')

#5 recursive_deduplicate
def recursive_deduplicate(string):
    if len(string) <= 1:
        return string
    elif string[0] == string[1]:
        return recursive_deduplicate(string[1:])
    else:
        return string[0] + recursive_deduplicate(string[1:])

print('5.)')
print(recursive_deduplicate('aaaaabbbbbbcccccc'))
print(recursive_deduplicate('aaaaabbbbbbccccccdddddd'))
print(' ')

#6 recursive_reverse
def recursive_reverse(string):
    if len(string) <= 1:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]

print('6.)')
print(recursive_reverse('hello'))
print(recursive_reverse('hello world'))
print(' ')