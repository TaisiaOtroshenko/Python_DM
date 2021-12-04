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
cur = 1
nxt = 0

length_min = 0
Q = [source-1] # очередь обхода графа
QM =[[source-1],] # ярусы в очереди
head = 0
# Обход в ширину с поиском минимальной длины
while head<len(Q):
    u = Q[head]
    for v in range(n):
        if v == target-1 and A[u][v]==1:
            Q.append(v)
            head = n
            break
        if A[u][v]==1 and not Mark[v]:
            Mark[v] = True
            Q.append(v)
            nxt+=1
    cur-=1
    if (cur==0):
        cur = nxt
        QM.append([Q[i] for i in range(len(Q)-nxt, len(Q))])
        nxt = 0
        length_min+=1
    head += 1

way = []
def Back(cur, i = len(QM)-1):
    global A, QM
    if QM[i][0]==source-1:
        way.append(cur+1)
        return 
    for prew in QM[i-1]:
        if A[cur][prew]==1:
            Back(prew,i-1)
            way.append(cur+1)
            
Back(target-1)
print (way, "- Way from %(0)i to %(1)i BFS with minimum length -" % {'0':source, '1':target}, length_min)
