# Считывание матрицы из файла
with open("D:\git_repos\Python_DM\DM_LR5\data.txt", "r") as f:
    n, source, target = list(map(int, f.readline().split()))
    A = [ list(map(int, it.split())) for it in f.read().split("\n") ]

Mark = [False]*n
way = []
length = 0
# Рекурсивная процедура обхода в глубину
def DFS(u):
    global A, Mark, length
    Mark[u] = True
    
    length +=1
    for v in range(n):
        if (A[u][v]==1 and not Mark[v] and not Mark[target-1]):  
            DFS(v)
    if Mark[target-1]:  
        way.append(u+1)      
        return length-1 
    length-=1   
length = DFS(source-1)
way.reverse()
print (way, "- Way from %(0)i to %(1)i DFS with length -" % {'0':source, '1':target}, length)

Mark = [False]*n
Mark[source-1] = True
# Инициализация очереди и счетчика ярусов
Q = [source-1]
head = 0
length = 0
cur = 1
nxt = 0
# Обход в ширину с поиском минимальной длины
while head<len(Q):
    u = Q[head]
    
    for v in range(n):
        if v == target-1 and A[u][v]==1:
            head = n
            break
        if A[u][v]==1 and not Mark[v]:
            Mark[v] = True
            Q.append(v)
            nxt+=1
    cur-=1
    if (cur==0):
        cur = nxt
        nxt = 0
        length+=1
    head += 1
print ("Min length -", length)

Mark = [False]*n
way = [target]
length_tmp = 0
# Рекурсивная процедура обхода в глубину с поиском дороги заданной длины
def DFSway(u):
    global A, Mark, length_tmp, length
    Mark[u] = True
    length_tmp +=1
    for v in range(n):
        if (A[u][v]==1 and not Mark[v]):  
            DFSway(v)
    if Mark[target-1] and length_tmp==length:  
        way.append(u+1)      
        return way.reverse()
    length_tmp-=1   
DFSway(source-1)
print (way, "- Way from %(0)i to %(1)i BFS with length -" % {'0':source, '1':target}, length)