
s = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s1 = 'ВЦРЮЪЦЬФЦКА'
s2 = 'ГОСЯЫЧФМОЛШ'
lst = []
lst_r = []
lst_l = []
tup = {}
for i in range(len(s1)):
    n = s.index(s2[i])-s.index(s1[i])
    if n > 0:
        tup['right'] = n
        lst.append(n)
        lst_r.append(n)
    elif n < 0:
        tup['left'] = n*-1
        lst.append(n*-1)
        lst_l.append(n*-1)
for i in range(len(lst)):
    if lst[i] == max(set(lst)):
        lst[i] = 33-lst[i]

for i in lst:
    if i in lst_r:
        r = i
    elif i in lst_l:
        l = i
res = ((33+l)-r)//2
sres = ''
for i in s2:
    c = s.index(i)+res
    while c > 32:
        c=c-33
    sres+=s[c]
print(sres) 

        
        
    


     
    