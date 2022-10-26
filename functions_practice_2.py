# Function Fun Part 2

# 1.
def arb_args(*args):
    for i in args:
        print(i)
print('1.)')
arb_args(1, 2, 3, 4, 5)
print(' ')

# 2.
def inner_func(x, y):
    def nest_1():
        return x * y
    def nest_2():
        return x + y
    print(nest_1() + nest_2())
print('2.)')
inner_func(2, 3)
print(' ')

# 3.
def lunch_lady(student, lunch='mystery meat'):
    print(student + ' is having ' + lunch)
print('3.)')
lunch_lady('John')
print(' ')

# 4.
def sum_n_product(x, y):
    return x + y, x * y
print('4.)')
print(sum_n_product(2, 3))
print(' ')

# 5.
alias_arb_args = arb_args
print('5.)')
alias_arb_args(1, 2, 3, 4, 5)
print(' ')

# 6.
def arb_mean(*nums):
    total =  0
    for i in nums:
        total += i
    print(total / len(nums))
print('6.)')
arb_mean(1, 2, 3, 4, 5)
print(' ')

# 7.
def arb_longest_string(*strings):
    longest = ''
    for string in strings:
        if len(string) > len(longest):
            longest = string
    print(longest)
print('7.)')
arb_longest_string('a', 'bb', 'ccc', 'dddd', 'eeeee')
print(' ')








