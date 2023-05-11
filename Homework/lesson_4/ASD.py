num = 15
mun = num
arr = []
new_num = 0
while  num > 0:
    arr.append(num % 10)
    num = num // 10
dlina = len(arr)
new_arr = []
for i in range(dlina):
    new_arr.append(9)
for i in new_arr:
    new_num = new_num * 10 + i

arr_del3 = []
for i in range(new_num):
    if i % 3 == 0:
        arr_del3.append(i)
arr_znak = []
for i in arr_del3:
    if i >= 10**(dlina-1):
        arr_znak.append(i)
povtor = dlina
num = mun
arr_itog = []
gnom = 0
print(arr_znak)
for i in arr_znak:
    #print(i)
    povtor = dlina
    gnom = 0
    while povtor > 0:
        x = str(i)
        y = str(num)
        if x[povtor-1] == y[povtor-1]:
            #print(x[povtor-1], y[povtor-1])
            gnom += 1
        povtor = povtor - 1
    if gnom >= dlina-1:
        arr_itog.append(i)
new_num = max(arr_itog)

print(arr_itog)
print(new_num)
#arr_dec = []
#nabor = dlina
#n = 0
#while nabor >= 1:
    #n = 10**(nabor-1)
    #arr_dec.append(n)
    #nabor-=1
#num = 15
#arr_itog = []
#print(max(arr_znak))
#for i in arr_znak:
    #print(i)

    #for d in arr_dec:
        #print(d)
        #g = abs(num - i)
        #print(g)
        #if g == d:
            #arr_itog.append(i)
            #print(arr_itog)
#new_num = max(arr_itog)
#print(new_num)



#print(arr, dlina)
#print(new_arr, new_num)
#print(arr_znak)
#print(arr_dec)
#print(arr_itog)