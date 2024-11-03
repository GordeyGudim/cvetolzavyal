m = 1 #int(input())
x0, y0 = 3, 7 #list(map(int, input().split()))
count_h = 9 #int(input())
lst_h = ['18 8 9', '25 1 9', '9 3 2', '3 4 8', '21 6 4', '13 6 10', '6 8 7', '16 2 6', '11 9 2']
# c = 0
# while c < count_h:
#     lst_h.append(input())
#     c+=1
lst_x_h = []
lst_y_h = []
lst_n_h = []
t = 0
count = 0

while t < m*60:
    
    for i in lst_h:
        n, x, y = i.split(' ')
        lst_n_h.append(n)
        lst_x_h.append(x)
        lst_y_h.append(y)
    numb = int(lst_n_h[0])
    
    l = abs(int(lst_x_h[0])-x0)+abs(int(lst_y_h[0])-y0)
    
    for i in range(1, count_h):

        if abs(int(lst_x_h[i])-x0)+abs(int(lst_y_h[i])-y0) < l:
            l = abs(int(lst_x_h[i])-x0)+abs(int(lst_y_h[i])-y0)
            numb = int(lst_n_h[i])

        if abs(int(lst_x_h[i])-x0)+abs(int(lst_y_h[i])-y0) == l and int(lst_n_h[i]) < numb:
            numb = int(lst_n_h[i])

    x0, y0 = int(lst_x_h[lst_n_h.index(str(numb))]), int(lst_y_h[lst_n_h.index(str(numb))])
    t+=l
    t+=10
    if t <= m*60:
        count+=1
    del lst_x_h[lst_n_h.index(str(numb))]
    del lst_y_h[lst_n_h.index(str(numb))]
    del lst_n_h[lst_n_h.index(str(numb))]
    if len(lst_n_h) == 0:
        break
print(count)