def palindrome(number):
    number1=str(number)
    number2=str(number)[::-1]
    return number1==number2
print(palindrome(23))
#====================================
def palindrome2(number):
    length=0
    while not palindrome(number):
        number=number+int(str(number)[::-1])
        length+=1    
    return length,number
#===============================================================================
# print(palindrome2(87))
# print(palindrome2(165))
# print(palindrome2(726))
# print(palindrome2(1353))
# print(palindrome2(4883))
# print(palindrome2(27))
#===============================================================================
print(palindrome2(4887))