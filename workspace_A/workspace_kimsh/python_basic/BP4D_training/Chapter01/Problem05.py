def math1(num):
    result=1
    if num<=0:
        return 0
    for i in range(1,num+1):
        result=result*i
       
    return result 
print(math1(0))
#8!=40,320
# No.2===============================================================================================================================
def math2(num2):
    if num2<=1:
        return 1
    else: 
        return (num2*math2(num2-1))
print(math2(8))