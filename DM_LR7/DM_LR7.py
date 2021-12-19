# 1.	Прочитайте из файла «data.txt» значения переменной N и 
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

# N, M = map(int, input().split())
# Edges = []
# for i in range(M):
#     start, end, weight = map(int, input().split())
#     Edges.append([weight, start, end])
# Edges.sort()

Edges = WS
Comp = [i for i in range(n)]
Ans = 0
Three =[]
for weight, start, end in Edges:
    if Comp[start] != Comp[end]:
        Ans += weight
        Three.append([weight, start, end])
        a = Comp[start]
        b = Comp[end]
        for i in range(n):
            if Comp[i] == b:
                Comp[i] = a
                
print (Ans)
print (Three)





















# # Соединяет все вершины между собой - возможен лес - Попытка разделения на множества
# Mark = [False]*n
# i = 0
# li = 0
# LV = [[i] for i in range(n)]
# LW = []

# # Sets = []
# while(len(LW) < n-1):
#     t1=Mark[WS[i][0]]
#     t2=Mark[WS[i][1]]

#     if t1 and t2 == 1:
#         LW.append(WS)
#         for 
#         LV[WS[i[0]]].append[WS[i][1]]
#         LV.
#         Mark[WS[i][0]] = True
#         Mark[WS[i][1]] = True
#     if t1 and t2==0:
#         Mark[WS[i][0]] = True
#         Mark[WS[i][1]] = True
#         i+=1
#     else:
        
#         WS.pop(i)
# WS = WS[:i]

# print(WS)


# # Соединяет все вершины между собой - возможен лес
# i = 0
# Mark = [False]*n
# while(sum(list(map(int, Mark)))!=n and i < len(WaySorted)):
#     m = WaySorted[i]
#     t1=Mark[WaySorted[i][0]]
#     t2  = Mark[WaySorted[i][1]]
#     if (t1*t2==0):
#         Mark[WaySorted[i][0]] = True
#         Mark[WaySorted[i][1]] = True
#         i+=1
#     else:
#         WaySorted.pop(i)
# WaySorted = WaySorted[:i]
# print(WaySorted)





# def cycle(G):
#     global Mark
#     cycle = False
#     Mark = [False]*n
#     vertice = []
#     for it in [it[:2] for it in G]:
#         vertice+= it
#     vertice = set(vertice)
#     for cur in vertice:
#         cycle = cycle or dfs(G,-1, cur)
#         return cycle

# def dfs(G, prew, cur):
#     cycle = False
#     Mark[cur] = True
#     next_ver = []
#     for it in G:
#         if it[0]==cur and it[0]!=prew and it[1]!=prew:
#             next_ver.append(it[1])
#         if it[1]==cur and it[1]!=prew and it[0]!=prew:
#             next_ver.append(it[0])
#     for w in next_ver:
#         if Mark[w]:
#             cycle = True
#         else:
#             dfs(G, cur, w)
#     if(cycle):
#         return cycle
        


# i = 2
# T = [WaySorted[0], WaySorted[1]]
# while(len(T)<n-1 and i<len(WaySorted)):
#     if (not cycle(T+[WaySorted[i]])):
#         T.append(WaySorted[i])
#     i+=1

# print("Общая длина дорог:", sum(list(map(lambda x: x[2], T))))
# print("Дроги графа:", *list(map(lambda x: str(x[0])+'->'+str(x[1]), T)))


# Mark = [False]*n
# way = []
# length = 0
# # Рекурсивная процедура обхода в глубину
# def DFSmy(u):
#     global A, Mark, length
#     Mark[u] = True
    
#     length +=1
#     for v in range(n):
#         if (A[u][v]==1 and not Mark[v] and not Mark[target-1]):  
#             DFSmy(v)
#     if Mark[target-1]:  
#         way.append(u+1)      
#         return length-1 
#     length-=1   
# length = DFSmy(source-1)
# way.reverse()
# print (way, "- Way from %(0)i to %(1)i DFS with length -" % {'0':source, '1':target}, length)

# Mark = [False]*n
# Mark[source-1] = True


# # Для обхода в глубину
# CurA =[]
# Mark = [[False]*n]
# c = False

# # Выделение всех путей в массив
# WaySorted = []
# for i in range(n-1):
#     for j in range(i+1,n):
#         m = [i,j,A[i][j]]
#         WaySorted.append(m)
# WaySorted = sorted(WaySorted, key=lambda x: x[2])



# # # Проверка на цикл изменяет переменную с, если он найден (Рекурсивная процедура обхода в глубину)
# # def DFScycle(u, prev):
# #     global CurA, Mark, c
# #     Mark[u] = True
# #     print(u, end = " ")  # выводит все пройденные дороги
# #     vertice = [i for i in range(n)]
# #     vertice.remove(u)
# #     if (prev != u):
# #         vertice.remove(prev)
    
# #     for v in vertice:
# #         if CurA[u][v]!=math.inf and not Mark[v]:
# #                 DFScycle(v, u)
# #         if CurA[u][v]!=math.inf and Mark[v]:
# #                 c = True
    
    
                

# iway =2
# ShortWay = [WaySorted[0], WaySorted[1]]
# while(len(ShortWay)<n):
#     ShortWay.append(WaySorted[iway])
#     if Cycle(ShortWay):
#         ShortWay.pop()
#     iway+=1
#     print ("\n\t", ShortWay)
# print (ShortWay)