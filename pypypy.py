#Задание 1
my_list = [2, 71, 25, 41, 13, 3, 56, 91, 85, 83]
list1 = [int(i) for i in my_list if int(i) < 5]
print('меньше 5', list1)
list2 = [int(i)/2 for i in my_list]
print('деленые на 2', list2)
list3 = [int(i)*2 for i in my_list if int(i) > 17]
print('больше 17 умноженные на 2', list3)
list4 = [int(i)*int(i) for i in range(0, int(input()))]
print('от 0 до введенного пользователем в квадрате', list4)
print('метод split',*[int(i)*int(i) for i in input().split()])
print(*[int(i)*int(i) for i in input().split() if int(i)%2 != 0 and str(int(i)*int(i))[-1] != '9'])

#Задание 2
list = input().split()
for i in list:print('*' * int(i))

#Задание 3
def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('Это треугольник')
    else:
        print('Это не треугольник')
a, b, c,  = int(input("a:")), int(input("b:")), int(input("c:"))
triangle(a, b, c)

#Задание 4
from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
x1, y1, x2, y2 = int(input("x1:")), int(input("y1:")), int(input("x2:")), int(input("y2:"))
print(distance(x1, y1, x2, y2))

#Задание 5
def number_to_words(n):
    l1 = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать",
          "двенадцать","тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    l2 = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    f = n // 10
    s = n % 10
    print(f, s)
    if f <= 0:
        return print(l1[s - 1])
    else:
        return print(l2[f - 2], l1[s - 1])
number_to_words(int(input("n:")))

#Задание 6
def bracket_check(test):
    while "()" in test:
        test = test.replace("()", "")
    print('YES' if test == '' else 'NO')
bracket_check('()(()')
#Задание 7
def palindrome(test_str : str):
    a = test_str.replace(' ', '').lower()
    if a == a[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'

print(palindrome('а роза упала на лапу Азора'))
print(palindrome('не палиндром'))

#Задание 8
def tik_tac_toe(game_field):
    values = []
    for i in game_field[0] + game_field[1] + game_field[2]:
        values.append(i)
    for i in game_field:
        if i[0] == i[1] == i[2]:
            return f'{i[0]} win'
    for i in range(0, 3):
        print(values[0 + i:7 + i:3])
        if values[0+i:7+i:3] == ['0', '0', '0']:
            return "0 win"
        if values[0+i:7+i:3] == ['x', 'x', 'x']:
            return "x win"
    if (values[0] == values[4] == values[8]) or (values[2] == values[4] == values[6]):
        return f'{values[4]} win'
    return 'draw'

data = '''0 - 0
x x x
0 0 -'''
field = [line.split() for line in data.split('\n')]
print(tik_tac_toe(field))

#Задание 9
memory = []
def print_without_duplicates(message):
    if message not in memory:
        print(message)
        memory.append(message)
print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Не могу до тебя дозвониться")
print_without_duplicates("Когда доедешь до дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")

#Задание 10
persons = {}
def add_friends(name_of_person, list_of_friends):
    a = persons.get(name_of_person)
    if a:
        persons[name_of_person] = a + list_of_friends
    else:
        persons[name_of_person] = list_of_friends
def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in persons[name_of_person1]:
        return True
    return False
def print_friends(name_of_person):
    s = reversed(persons[name_of_person])
    for i in s:
        print(i, end=' ')
    print()

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))

#Задание 11
keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def to_roman(n):
    pointer = 0
    result = ''
    while n > 0:
        while n >= keys[pointer]:
            n -= keys[pointer]
            result += values[pointer]
        pointer += 1
    return result

def roman():
    global one, two, three
    three = one + two
    print(to_roman(one), "+", to_roman(two), "=", to_roman(three))

one = 5
two = 4
roman()

#Задание 12
a = [1, 2, 3]
b = a          
a += [4, 5, 6] 
print(b)

a = [1, 2, 3]
b = a          
a = a + [4, 5, 6]
print(b)

#Задание 13
arr = ['1', '3', '4', '2']
arr2 = ['1', '3', '4', '2']
arr.sort() 
print(arr)
arr_sorted = sorted(arr2) 
print(arr2)
print(arr_sorted)

#Задание 14
numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(odd)
print(even)

#Задание 15
fractal = []
def create_fractal(rep):
    global fractal
    for i in range(0,rep):
        fractal.extend([0, fractal, fractal, 2])
    print(fractal)

create_fractal(2)

#Задание 16
def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)

sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 5)
print(*sequence)

#Задание 17
def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)

arr = [1, 2]
mirror(arr)
print(*arr)

#Задание 18
def from_string_to_list(string, container):
    container.extend(string.split())

a = [1, 2, 'abc']
from_string_to_list("1 3 99 52", a)
print(*a)

#Задание 19
import numpy
def transpose(matrix):
    matrix[:] = numpy.transpose(matrix)

matrix = [[1,5], [3, 4], [2, 45]]
transpose(matrix)
for line in matrix:
    print(*line)

#Задание 20
def swap(first, second):
    first[:], second[:] = second[:], first[:]

first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)

#Задание 21
def defractalize(fractal):
    fractal[:] = [x for x in fractal if x is not fractal]

fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)

#Задание 22
def fractal_print(fractal):
    print('[' + ', '.join(map(str, fractal)) + ']')

fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)

#Задание 23
def matrix(n=None,m=None,a=0):
    if n==None and m==None:
        n=1
        m=1
    elif m==None:
        m=n
    return [[a for i in range(m)] for j in range(n)]

rows = matrix(2)
for row in rows:
    print(*row)

#Задание 24
def partial_sums(*a):
    res = [0]
    for i in range(len(a)):
        res.append(res[i] + a[i])
    return res

print(partial_sums(1, 0.5, 0.25, 0.125))

# Задание 25
def solve(*coefficients):
    if len(coefficients) == 0 or len(coefficients) > 3:
        return None
    if len(coefficients) == 3:
        a, b, c = coefficients
        if a == 0 and b == 0 and c == 0:
            return ["all"]
        elif a == 0 and b == 0:
            return []
        elif a == 0:
            return [-c / b]
        D = b**2 - 4*a*c 
        if D < 0:
            return []
        elif D == 0:
            return [-b / (2*a)]
        else:
            x1 = (-b + D**0.5) / (2*a)
            x2 = (-b - D**0.5) / (2*a)
            return sorted([x1, x2])
    elif len(coefficients) == 2:
        b, c = coefficients
        if b == 0 and c == 0:
            return ["all"]
        elif b == 0:
            return []
        else:
            return [-c / b]
    elif len(coefficients) == 1:
        c = coefficients[0]
        if c == 0:
            return ["all"]
        else:
            return []

print(solve(1,8,9))