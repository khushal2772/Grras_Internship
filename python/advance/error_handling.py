# while True:
#     try:
#         a = int(input("Enter no 1: "))
#         b = int(input("Enter no 2: "))
        
#         print(f'The sum id {a + b}\n')
        
#     except Exception as e:
#         print("Please enter valid integers (not string/float).\n")
    
while True:
    try:
        a = int(input("Enter no 1: "))
        b = int(input("Enter no 2: "))
        
        print(f'The division is {a / b}')
        
    except ZeroDivisionError:
        print("Cannot be divide by zero.\n")
    except ValueError:
        print("Please enter valid integers .\n")
        
    except Exception as e:
        print("Please enter valid integers (not string/float).\n")
    
    else:  # excute when no error in try block
        print('division done\n')
        
