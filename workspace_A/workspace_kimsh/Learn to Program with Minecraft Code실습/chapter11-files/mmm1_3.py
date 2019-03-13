#number=input("input your people number : ")
#number.split()
#===============================================================================
# num2=number.split()
# print(num2)
#===============================================================================
#print(number)
# 3 7 7 8
#===============================================================================
# for i in num2:
#     print(i)
#===============================================================================
    
    
#    map(int,xxxx)
def map_function(Lstring):
    alist=[]
    for i in Lstring:
        a=int(i)
        alist.append(a)
        
    return alist

def damjang(aa,b):
    road=0
    for key in aa:
        if key<=b:
            road+=1
        else:
            road+=2
    return road

binput=input("input your people number : ")
numlist=map_function(binput.split())
n,h=map_function(binput.split())
print(numlist)
keyinput=input("input your key : ")
friendskey=map_function(keyinput.split())
print(damjang(friendskey, h))