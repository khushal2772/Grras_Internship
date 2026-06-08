try:
    a = int(input("Enter no 1: "))
    b = int(input("Enter no 2: "))
        
    print(f'The division is {a / b}')

except Exception as e:
    print(e)

finally:  # this is always executed if error ocur or not
    print("this is always executed.")