
lista=[4,5,6,7]
listb=["test","test2"]
listc=[True,False]
print(len(lista))
print(listb[1])

for count,i in enumerate(lista):
    print("count:{} i:{}".format(count,i))
    
#tuple ()
#dictionary  {"key":value}
    
    
a=[]
foodlist=[]
foodlist.append("chicken")
foodlist.append("pizza")
foodlist.append("hambuger")
print(foodlist)
foodlist[1]="cola"
print(foodlist)
foodlist.insert(1,"rice")
print(foodlist)
foodlist.insert(10,"food")
print(foodlist)
print(foodlist*2)
foodlist.index("rice")
foodlist2=foodlist*2
print(foodlist2)
print(foodlist2.index("rice"))