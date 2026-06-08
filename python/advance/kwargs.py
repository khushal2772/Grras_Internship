def marks(**kwargs):  #kwargs is a dictonary that store passed values in dict
    for value in kwargs.keys():
        print(f"{value} obtain {kwargs[value]}")

marks(khushal=78, kanishk=98, bansal=80)

def fun(*args, **kwargs):
    print(args)
    print(kwargs)
    
fun(312,3,124,32, khushal=32,wukjf=21,bkwf=13)