#No.1=================================================
def simple(number):
    result=0
    if number<0:
        return "..."
    for i in range(1,number+1):
        result=result+i
    return result
print(simple(100))
#No.2=================================================
def simple2(number):
    
    if number<=1:
        return 1
    else:
        return number+simple2(number-1)
print(simple2(100))