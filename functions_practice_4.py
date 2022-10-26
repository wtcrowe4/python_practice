# Functions Practice Part 4

#1 max_num
def max_num(*n):
    return max(n)

print('1.)')
print(max_num(1, 2, 3, 4, 5))
print(max_num(1, 2, 33, 4, 5, 6, 77, 8, 9, 10))
print(' ')

#2 mult_list multiply a list of numbers
def mult_list(*n):
    total = 1
    if len(n) == 0:
        return 0
    for i in n:
        total *= i
    return total

print('2.)')
print(mult_list(1, 2, 3, 4, 5))
print(mult_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(' ')

#3 rev_string
def rev_string(string):
    return string[::-1]

print('3.)')
print(rev_string('hello'))
print(rev_string('hello world'))
print(' ')

#4 num_within
def num_within(x, small, big):
    return small <= x <= big

print('4.)')
print(num_within(1, 2, 3))
print(num_within(2, 1, 3))
print(' ')

#5 pascal
triangle = [[1], [1, 1]]
def pascal(n):
    
    if n <= 0:
        print([]) 
    elif n == 1:
        print([[1]]) 
    else:
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        for row in triangle:
            print(row)
        
# When calling this a second time, the triangle list is not reset.
print('5.)')
pascal(10)
print(' ')