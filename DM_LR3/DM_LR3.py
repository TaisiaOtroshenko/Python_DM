import random
import time

def consoleIn():
    return list(map(int, input("Введите элементы массива ").split()))
def randomIn():
    return [random.randint(0,20) for i in range(int(input("Введите количество элементов ")))]
def increasIn():
    return [ i+1 for i in range(int(input("Введите количество элементов ")))] 
def decreasIn():
    return [ i+1 for i in reversed(range(int(input("Введите количество элементов "))))] 

def menu():
    comand = int(input("1. concole \n2. random \n3. 1..N \n4. N..1\n>> "))
    func = [consoleIn, randomIn, increasIn, decreasIn]
    return func[comand-1]()


def sorted(m):
    b = True
    for i in range(len(m)-1):
        if (m[i]>m[i+1]):
            b = False
    return b
# ВЫБОРОМ
def select(m):
    if (sorted(m)==True):
        return m
    for i in range(len(m)-1):
        min = i 
        for j in range(i+1, len(m)): # выбор минимального после текущего элемента
            if (m[j]<m[min]):
                min = j
        m[min], m[i] = m[i], m[min] # обмен текущего с выбранным
    return m
# ОБМЕНОМ
def change(m):
    if (sorted(m)==True):
        return m
    for j in range(len(m)-1):
        for i in range(len(m)-j-1): # потому что после каждой итерации на "законное" место встает один элемент с конца
            if (m[i+1]<m[i]):
               m[i+1], m[i] = m[i], m[i+1] # обмен текущего со следующим
    return m
# ВСТАВКАМИ
def insert(m):
    if (sorted(m)==True):
        return m
    for i in range(1,len(m)):
        tmp = m[i]
        for j in reversed(range(-1,i)):
            if (tmp<m[j] and j>=0):
                m[j+1] = m[j]
            else:
                m[j+1] = tmp
                break
    return m
# ФОН НЕЙМАНА
def neumann(m): # разбиение
    if (sorted(m)==True):
        return m
    if(len(m)>1):
        pivot = random.randint(0,len(m)-1) # int(len(m)/2)
        return merge(neumann(m[:pivot]),neumann(m[pivot:]))
    else:
        return m
def merge(a, b): # слияние
    m =[]
    i, j = 0,0
    while(i<len(a) and j<len(b)):
        if(a[i]>b[j]):
            m.append(b[j])
            j+=1
        else:
            m.append(a[i])
            i+=1
    return m+a[i:]+b[j:]
# КВИКСОРТ
def quicksort(m):
    if (sorted(m)==True):
        return m
    if(len(m)>1):
        pivot = random.randint(0,len(m)-1)
        s, b = [],[]
        for i in range(len(m)):
            if(m[i]<m[pivot]):
                s.append(m[i])
            else:
                b.append(m[i])
        return quicksort(s)+quicksort(b)
    else:
        return m
# Контрольное значение
def controlNum(m):
    a = []
    for i in range(len(m)-1):
         a[i] = m[i+1]-m[i]
    return min(a)
    
while (True):
    mass = decreasIn()
    print("Изначальный массив", mass)
    s = time.time()
    mass = select(mass)
    # mass = change(mass)
    # mass = insert(mass)
    # mass = neumann(mass)
    # mass = quicksort(mass)
    f = time.time() - s
    print("Отсортированный массив", mass)
    print("Время - ", f)
