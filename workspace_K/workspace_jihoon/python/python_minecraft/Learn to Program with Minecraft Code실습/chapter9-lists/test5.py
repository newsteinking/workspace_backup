x="2018-03-10"


#print(x[start:end])
print(x[0:4])
print(x[5:7])
print(x[8:10])

def getdate(x):
    year=int(x[0:4])
    month=int(x[5:7])
    day=int(x[8:10])
    return year,month,day

print(getdate("2019-04-20"))

def getdate2(x):
    year=x[0:4]
    month=x[5:7]
    day=x[8:10]
    return year,month,day

print(getdate2("2019-04-20"))

def reverse(x):
    b=x[::-1]
    return b

print(reverse(x))

