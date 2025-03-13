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

#Задание 6
def bracket_check(test):
    while "()" in test:
        test = test.replace("()", "")
    print('YES' if test == '' else 'NO')
bracket_check('()(()')


