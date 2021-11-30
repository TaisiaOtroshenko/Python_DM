global x
global n 
n = 7
cost = [[0, 64, 63, 94, 59, 54, 79, 99], [64, 0, 57, 66, 79, 61, 65, 70], [63, 57, 0, 68, 69, 58, 60, 86], [94, 66, 68, 0, 92, 57, 63, 96], [59, 79, 69, 92, 0, 66, 78, 95], [54, 61, 58, 57, 66, 0, 66, 93], [79, 65, 60, 63, 78, 66, 0, 68], [99, 70, 86, 96, 95, 93, 68, 0]]

# алгоритм перестановки
# def next():
#     i = n-2
#     while(i>=0) and (x[i]>x[i+1]):
#         i -= 1
#     if (i>=0):
#         ind = x.index(min([it for it in x[i:] if it>x[i]]))
#         x[i], x[ind] = x[ind], x[i]
#         x[i:].sort()
#         return True
#     else:
#         return False

def next():
    i = n-2
    while(i>=0) and (x[i]>x[i+1]):
        i -= 1
    if (i>=0):
        ind = x.index(min([it for it in x[i:] if it>x[i]]))
        x[i], x[ind] = x[ind], x[i]
        x[i:].sort()
        return True
    else:
        return False

def cost_f(cost_arr, x_way):
    c = 0
    x_way = [0]+x_way+[0]
    for i in range(len(x_way)-1):
        c += cost_arr[x_way[i]][x_way[i+1]]
    return c

x = [i for i in range(1,n+1)]
# print("first way - ",x)
control_num = 0

cost_min = cost_f(cost,x)
x_min = [0]+x+[0]

while next():
    # print(x)
    control_num+=1 # control
    if (cost_f(cost,x)<cost_min):
        cost_min = cost_f(cost,x)
        x_min = [0]+x+[0]

# print("last way - ", x)
print("control num -", control_num)
print("way -", [it+1 for it in x_min])
print("cost -", cost_min)


