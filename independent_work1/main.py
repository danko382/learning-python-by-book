from heapq import nlargest

def task1():
    day = int(input("enter the day >> "))
    may = int(input("enter the may >> "))
    print("Текущий день " + str(day) + "." + str(may) + ".2022")

def task2():
    year_burn = int(input("enter the your burn year >> "))
    year = int(input("enter tekushii year >> "))
    print("Ваш возраст = ", year - year_burn)

def task3():
    kilometrs = int(input("enter the distance >> "))
    print(kilometrs * 1.6 , " milies")

def task4():
    n = int(input("enter the n >> "))
    a = [2**k for k in range(n+1)]
    print(a)

def task5():
    n = int(input("enter the n >> "))
    a = [5*k + 3 for k in range(n+1)]
    print(a)

def task6():
    n = int(input("enter the number >> "))
    if(n % 3 == 0):
        print("Yes!")
    else:
        print("No!")

def task7():
    n = int(input("enter the n >> "))
    for i in range(n+1):
        b = 1
        for j in range(1, i+1):
            b *= j
        print(b)

def task8():
    n = int(input("enter the n >> "))
    pos1, pos2, res = 1, 1, 1
    if n > 1:
        print(res, end=" ")
    if n > 2:
        print(res, end=" ")
    for i in range(2, n):
        pos1 = pos2
        pos2 = res
        res = pos1 + pos2
        print(res, end=" ")

def task9():
    a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(nlargest(2, a)[1])

def task10():
    n = int(input("enter the n >> "))
    a = [2*k+1 for k in range(n+1)]
    print(sum(a))
