from random import seed
from random import randint

def task1():
    s = input("Enter the text >> ")
    n = int(input("Enter the step >> "))
    a = tuple(s[::n])
    print(a)

def task2():
    s = input("Enter the number >> ")
    a = list(s)
    b = tuple([eval(i) for i in a])
    a.reverse()
    c = tuple([eval(i) for i in a])
    print(b)
    print(c)

def task3():
    width = int(input("Enter the width >> "))
    height = int(input("Enter the height >> "))
    a = [[chr(ord('A')+randint(0, 26)) for j in range(width)] for i in range(height)]
    print(a)

def task5():
    width = int(input("Enter the width >> "))
    height = int(input("Enter the height >> "))
    a = [[randint(0, 100) for j in range(width)] for i in range(height)]
    for i in a:
        for j in i:
            print(j, end="\t")
        print()
    row = int(input("Enter the number of row >> "))
    col = int(input("Enter the number of col >> "))
    a = a[:row] + a[row+1:]
    for i in range(len(a)):
        a[i] = a[i][:col] + a[i][col+1:]
    for i in a:
        for j in i:
            print(j, end="\t")
        print()

def task6():
    n = int(input("Enter the size of array >> "))
    a = [randint(0, 100) for i in range(n)]
    print(a)
    while(True):
        flag = 1
        for i in range(n-1):
            if(a[i] > a[i+1]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                flag = 0
        if (flag):
            break
    print(a)

def task7():
    n = int(input("Enter the size of array >> "))
    a = [randint(0, 100) for i in range(n)]
    b = [max(a), a.index(max(a))]
    print(a)
    print(b)

def task8():
    n = int(input("Enter the size of array >> "))
    a = [randint(0, 100) for i in range(n)]
    print(a)
    while (True):
        flag = 1
        for i in range(0, n - 2, 2):
            if (a[i] > a[i + 2]):
                temp = a[i]
                a[i] = a[i + 2]
                a[i + 2] = temp
                flag = 0
        if (flag):
            break
    while (True):
        flag = 1
        for i in range(1, n - 2, 2):
            if (a[i] < a[i + 2]):
                temp = a[i]
                a[i] = a[i + 2]
                a[i + 2] = temp
                flag = 0
        if (flag):
            break
    print(a)

def task9():
    n = int(input("Enter the size of array >> "))
    a = [randint(0, 100) for i in range(n)]
    print(a)
    count = 0
    i = 0
    while(count < n and i < n + count - 1):
        a.insert(i+1, a[i]+a[i+1])
        count += 1
        i += 2
    print(a)

def task10():
    n = int(input("Enter the size of array >> "))
    a = [randint(0, 100) for i in range(n)]
    b = [randint(0, 100) for i in range(n)]
    print(a)
    print(b)
    c = []
    for i in range(n):
        c.append(a[i])
        c.append(b[i])
    print(c)
