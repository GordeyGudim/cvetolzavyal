count_t = 6 #int(input())
lst_t = [3, 2, 1, 10, 5, 4] # list(map(int, input().split(' '))))
count_p = 4 #int(input())
lst_p = [5, 1, 2, 3] # list(map(int, input().split(' '))))
k = 2 #int(input())
lst_p[k-1] = {'незнайка':lst_p[k-1]}
n = lst_p[k-1]
count_n = 0
while len(lst_t) > 0:
    strong = 0
    count = 0
    i = -1
    while lst_t[0] > strong:
        count+=1
        i+=1
        if type(lst_p[i]) == type({'незнайка':lst_p[k-1]}):
            strong+=lst_p[i]['незнайка']
            count_n+=1
        else:
            strong+=lst_p[i]
    lst_p=lst_p+lst_p[:count]
    del lst_p[:count]
    del lst_t[0]
print(count_n)