number=int(input("input your number : "))
numlist=[]
for i in range(0,number):
    num=int(input("input your num : "))
    numlist.append(num)
b=[sum(numlist[0:x+1]) for x in range(0,len(numlist))]
print(numlist)
print(b)

c=[]
sumnum=0
for x in numlist:
    sumnum=sumnum+int(x)
    print(sumnum,x)
    c.append(sumnum)
print(c)