# 1. recursive printing
def recursive_printing(n):
    if n > 0:
        recursive_printing(n - 1)
        print(n, end='')
print('1. Recursive Printing recursive_printing(5)')
recursive_printing(5)
print()
# ''.join([str(c) for c in range(1,6)])


# 2. recursive multiplication
recursive_multiplication = lambda x, y : 0 if y == 0 else x + recursive_multiplication(x, y - 1)
print('2. Recursive Multiplication', recursive_multiplication(4,6))
# x * y


# 3. recursive lines
def recursive_lines(lines):
    if lines > 1:
        recursive_lines(lines - 1)
    print('*' * lines)
print('3. Recursive Lines: recursive_lines(5)')
recursive_lines(5)
# print('\n'.join(['*' * c for c in range(1,6)]))


# 4. largest list item
def max_in_list(the_list):
    if len(the_list) == 1:
        return the_list[0]
    else:
        m = max_in_list(the_list[1:])
        return m if m > the_list[0] else the_list[0]
print('4. Max in List', max_in_list([1,3,8,7,9,2,4,6,5]))
# max([1,3,8,7,9,2,4,6,5])


# 5. recursive list sum
sum_the_list = lambda the_list : the_list[0] + sum_the_list(the_list[1:]) if len(the_list) else 0
print('5. Recursive List Sum', sum_the_list([3,6,3,8,6,4,7]))
# sum([1,3,8,7,9,2,4,6,5])


# 6. sum of numbers
sum_of_numbers = lambda num : 0 if num == 0 else num + sum_of_numbers(num - 1)
print('6. Sum of Numbers', sum_of_numbers(10))
# sum(range(1,num))


# 7. recursive power
recursive_power = lambda x, y : x * recursive_power(x, y - 1) if y >= 1 else 1
print('7. Recursive Power', recursive_power(3, 4))
# x**y

# 8. ackermann's function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m -1, 1)
    return ackermann(m - 1, ackermann(m, n -1))
print('8. Ackermann\'s Function', ackermann(3, 4))
