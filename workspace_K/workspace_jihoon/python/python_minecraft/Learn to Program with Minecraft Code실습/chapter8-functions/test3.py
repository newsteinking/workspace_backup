def wordtonumber(word):
    if word=="one":
        num=1
    elif word=="two":
        num=2
    elif word=="three":
        num=3
    else :
        num=0
    return num
a=input("input your word:")
print(wordtonumber(a))