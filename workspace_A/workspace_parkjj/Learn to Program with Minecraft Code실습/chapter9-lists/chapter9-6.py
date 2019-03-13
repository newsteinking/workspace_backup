def get_date(date):
    year=int(date[0:4])
    month=int(date[5:7])
    day=int(date[8:10])
    return year,month,day 
    
x,y,z=get_date("2019-02-21")
print("{}, {}, {}".format(x,y,z))
print(get_date("2019-02-21"))