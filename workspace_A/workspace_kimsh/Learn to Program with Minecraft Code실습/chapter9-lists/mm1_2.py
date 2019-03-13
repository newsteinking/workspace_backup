import random

def Python(datastring):
    year=int(datastring[0:4])
    month=int(datastring[5:7])
    day=int(datastring[8:10])
    return year,month,day
    
print(Python("2019-01-21"))


#"2018-01-21"