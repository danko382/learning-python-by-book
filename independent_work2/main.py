def task1():
    s = input("enter the number >> ")
    add = 0
    for i in range(10):
        add = 0
        for j in range(len(s)):
            if str(i) == s[j]:
                add += 1
        if(add != 0):
            print("количество цифр " + str(i) + " в числе = " + str(add))

def task2():
    s = input("enter the number >> ")
    for i in s:
        print(9 - int(i), end="")

def task3():
    a = []
    s = ""
    while True:
        temp = (input("enter the number >> "))
        if temp == "stop":
            break
        a.append(int(temp))
    for i in a:
        s += str(i)
    print(s)

def task4():
    a = []
    b = []
    while True:
        temp = (input("enter the number >> "))
        if temp == "stop":
            break
        a.append(int(temp))
    while True:
        temp = (input("enter the number >> "))
        if temp == "stop":
            break
        b.append(int(temp))
    if(len(a) == len(b)):
        for i in range(len(a)):
            if(a[i] != b[i]):
                print("Они не совпадают.")
                break
        else:
            print("Они совпадают.")
    else:
        print("Они не совпадают.")

def task5():
    a = []
    while True:
        temp = (input("enter the numbers >> "))
        if temp == "stop":
            break
        a.append(int(temp))
    n = int(input("enter the number >> "))
    summ = 0
    for i in range(n):
        for j in a:
            if (j == i):
                break
        else:
            summ += i
    print(summ)

def task6():
    a = int(input("enter the a >> "))
    b = int(input("enter the b >> "))
    c = int(input("enter the c >> "))
    if (a + b <= c):
        print("No")
    elif(a + c <= b):
        print("No")
    elif(b + c <= a):
        print("No")
    else:
        print("Yes")

def task7():
    a = int(input("enter the a >> "))
    b = int(input("enter the b >> "))
    c = int(input("enter the c >> "))
    if((b - a == c - b) or (c - a == b - a)):
        print("Yes")
    elif((a - b == c - a) or (c - b == a - c)):
        print("Yes")
    elif((a - c == b - a) or (b - c == a - b)):
        print("Yes")
    else:
        print("No")

def task8():
    a = int(input("enter the number day >> "))
    if(a == 1):
        print("Monday")
    elif(a == 2):
        print("Tuesday")
    elif(a == 3):
        print("Wednsday")
    elif(a == 4):
        print("Thursday")
    elif(a == 5):
        print("Friday")
    elif(a == 6):
        print("Saturday")
    else:
        print("Sunday")

def task9():
    a = int(input("enter the firs number >> "))
    b = int(input("enter the second number >> "))
    print("b" if a < b else "a")

def task10():
    try:
        a = int(input("enter the a >> "))
        b = int(input("enter the b >> "))

        print("answer = ", (b - a - 1) / a)
    except ValueError:
        print("Ошибка преобразования")
    except ZeroDivisionError:
        print("Попытка деления на ноль")
    except TypeError:
        print("Недопустимая операция")
    except:
        print("Что-то пошло не так")

task10()