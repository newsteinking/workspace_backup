def word_to_number(str_m):
    
    if str_m == "one":
        number=1
    elif str_m == "two":
        number=2
    elif str_m == "three":
        number=3
    else:
        number="error"
        
    return number
print(word_to_number("two"))
        