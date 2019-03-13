
def getdate(str):
    year=int(str[0:4])
    month=int(str[5:7])
    day=int(str[8:10])
    
    return year,month,day


a="2018-03-09"


bb=getdate(a)
print(bb)

print(getdate(a))


#string slicing
#print(a[start:end])
print(a[0:4])
print(a[5:7])
print(a[8:10])


# a[  x : x :x]

b="abcdefg"
print(b[::-1])
print(b[:])


