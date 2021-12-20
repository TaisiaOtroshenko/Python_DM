# 1.	Прочитайте из файла «data.txt» значения переменной n и 
# весовую матрицу A размера  для своего варианта. 
# 2.	С помощью алгоритма Краскала найдите минимальное 
# остовное дерево заданного графа и его вес. 
# 3.	С помощью алгоритма Прима найдите минимальное 
# остовное дерево заданного графа и его вес. 
# 4.	Нарисуйте исходный граф и найденные каркасы 
# (если они разные, сделайте два рисунка). 
# Этот пункт задания можно сделать как с помощью компьютера, так и вручную.
import math

with open("D:\git_repos\Python_DM\DM_LR7\data.txt", "r") as f:
    n = int(f.readline().strip())
    A = [list(map(int,it.split())) for it in f.read().split("\n")]
    # for i in range(len(A)):
    #     A[i] = [math.inf if it==0 else it for it in A[i]]

# Выделение всех путей в отсортированный массив
WS = []
for i in range(n-1):
    for j in range(i+1,n):
        WS.append([A[i][j],i,j])
WS = sorted(WS)

Edges = WS
Comp = [i for i in range(n)]
Ans = 0
Three =[]
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        Ans += weight
        Three.append([weight, start+1, end+1])
        a = Comp[start]
        b = Comp[end]
        for i in range(n):
            if Comp[i] == b:
                Comp[i] = a
                
print ("Длина каркаса (алгоритм Краскала)-", Ans)
print ("\tКаркас -", *Three)

ways = [[i] for i in range(n)] # список кратчайших путей
dist = [math.inf] * n 
dist[0] = 0 
used = [False] * n 
ans = 0
for i in range(n): 
    # выбор новой вершины
    min_dist = math.inf 
    for j in range(n): 
        if not used[j] and dist[j] < min_dist: 
            min_dist = dist[j]
            u = j 
    ans += min_dist
    used[u] = True
    # выбор кратчайшего между известной и дорогой из новой вершины
    for v in range(n): 
        if dist[v]> A[u][v] and v!=u:
            ways[v] = ways[u] + [v]
        dist[v] = min(dist[v], A[u][v])
# преобразование кратчайших путей до вершин в дерево
Three = []
for way in ways:
    for i in range(len(way)-1):
        tmp = sorted([way[i], way[i+1]])
        if [A[tmp[0]][tmp[1]], tmp[0]+1,tmp[1]+1] not in Three:
            Three.append([A[tmp[0]][tmp[1]], tmp[0]+1,tmp[1]+1])
print ("Длина каркаса (алгоритм Прима)-", Ans)
print ("\tКаркас -", *Three)