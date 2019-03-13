import random
randomlist=[]
number=int(input("input your number : "))
for i in range(number):
    #b=random.randint(1,20)
    b=random.randrange(1,20,2)
    randomlist.append(b)
print(randomlist)