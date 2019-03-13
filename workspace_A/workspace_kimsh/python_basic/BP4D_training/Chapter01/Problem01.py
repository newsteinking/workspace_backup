Numslist=[]
num=int(input("input your number : "))
for i in range(0,num):
    element=int(input("input number : "))
    Numslist.append(element)
avg=sum(Numslist)/num
F=round(avg,2)
print(avg)
print(f'avg = {F}')