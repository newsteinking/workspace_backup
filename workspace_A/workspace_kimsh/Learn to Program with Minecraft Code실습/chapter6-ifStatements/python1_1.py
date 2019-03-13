num=int(input("Input your number : "))

if num%2==1:
    print("Weird")
     
elif 2<=num<=5 or num>20:
    if num%2==0:
        print("Not Weird")
         
elif 6<=num<=20:
    if num%2==0:
        print("Weird")
else:
    print("test")
         
#===============================================================================
# elif 20<num:
#     if num%2==0:
#         print("Not Weird")
#===============================================================================