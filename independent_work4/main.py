from random import randint

def task1():
    a = set()
    while(len(a) != 5):
        a.add(randint(0, 10))
    while(len(a) != 15):
        a.add(randint(10, 30))
    print(a)

def task2():
    first = input("Enter the first number >> ")
    second = input("Enter the second number >> ")
    one = set(int(i) for i in first)
    two = set(int(i) for i in second)
    print(one & two)

def task3():
    a = set("aAeEiIoOuUyY")
    b = input("Enter the text >> ")
    for i in b:
        if i in a:
            print(i, end=" ")

def task4():
    a = set(i for i in range(50+1) if i % 3 == 0)
    b = set(i for i in range(50+1) if i % 4 == 0)
    print(a)
    print(b)
    print(a.symmetric_difference(b))

def task5():
    n = int(input("Enter the size >> "))
    a = set((i, i + 2) for i in range(1, n+1, 2))
    print(a)

def task6():
    n = int(input("Enter the size >> "))
    a = [i for i in range(n+1)]
    c = tuple(a)
    b = dict(zip(c, reversed(c)))
    print(b)

def task7():
    txt = input("Enter the text >> ")
    a = tuple(txt)
    b = {i: a.count(i) for i in a}
    print(b)

def task8():
    b = {"Дюма": "Граф Монте-Кристо", "Глуховского": "Метро", "Стугацких": "Сталкер"}
    count = 0
    for i in b.keys():
        temp = input("Напишите название произведения " + i + " >> ")
        if temp == b[i]:
            count += 1
    print("Вы угадали " + str(count) + " раз!")

def task9():
    txt = input("Enter the text >> ")
    temp = []
    b = tuple(set(txt))
    res = dict()
    for i in b:
        for j in txt:
            if j != i:
                temp.append(j)
        res[i] = tuple(temp)
        temp.clear()
    print(res)

def task10():
    a = {"a": 1, "b": 2, "c": 3}
    b = {"d": 4, "e": 5, "f": 6}
    c = {}
    for i in a.keys():
        c[i] = a[i]
    for i in b.keys():
        c[i] = b[i]
    print(c)

task10()