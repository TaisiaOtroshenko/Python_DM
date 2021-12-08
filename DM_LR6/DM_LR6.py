# 1.	Прочитайте из файла «data.txt» значения переменных N, source, 
# target и весовую матрицу A размера  для своего варианта. 
# 2.	С помощью алгоритма Форда-Беллмана найдите расстояния 
# от вершины source до всех остальных вершин графа.
# 3.	С помощью алгоритма Дейкстры найдите расстояние и кратчайший путь 
# от вершины source до вершины target. Нарисуйте граф и найденный путь.
# 4.	С помощью алгоритма Флойда-Уоршалла найдите матрицу попарных 
# расстояний между всеми вершинами графа. 
# Нарисуйте на графе путь, найденный в пункте 3. Этот пункт задания 
# можно сделать как с помощью компьютера, так и вручную.
import math

# 1 Считывание данных из файла
with open("D:\git_repos\Python_DM\DM_LR6\data.txt", "r") as f:
    n, source, target = list(map(int, f.readline().split()))
    A = [list(map(int,it.split())) for it in f.read().split("\n")]
    for i in range(len(A)):
        A[i] = [math.inf if it==0 else it for it in A[i]]

# 2 s -> все
print("\tАлгоритм Форда-Беллмана:")
d = A[source-1].copy()
d[source-1] = 0
for k in range(n-2):
    for v in range(n):
        for u in range(n):
            d[v] = min(d[v],d[u]+A[u][v])
print(*d, sep=", ")

# 3 s -> t
print("\tАлгоритм Дейкстры:")
# В начале все вершины не помечены, а все расстояния равны бесконечности
Mark = [False]*n
d = A[source-1]
d[source-1] = 0
prev = [source-1]*n
# Находим расстояния
for i in range(n-1):
    m = math.inf
    for v in range(n):
        if (not Mark[v]) and (d[v]<m):
            m = d[v]
            u = v
    Mark[u] = True
    for v in range(n):
        if (not Mark[v]) and (d[u]+A[u][v]<d[v]):
            d[v] = d[u] + A[u][v]
            prev[v] = u

# Раскручиваем путь по масииву Prev
Path = [target]
v = target-1
while v!=source-1:
    v = prev[v]
    Path.insert(0,v+1)
print("Кратчайший путь: ", *Path, sep=" -> ")
print("Кратчайшее расстояние:", d[target-1])   

# 4 для всех путей
print("\tАлгоритм Флойда-Уоршалла:")
Q = A
for k in range(n):
    for u in range(n):
        for v in range(n):
            Q[u][v] = min(Q[u][v], Q[u][k]+Q[k][v])
print("Матрица расстояний:")
for i in range(n):
    for j in range(n):
        if Q[i][j]<100:
            Q[i][j] =str(Q[i][j])+" "
    print(*Q[i], sep="|")
