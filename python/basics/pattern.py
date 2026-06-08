for i in range(6):
    print(f"{i}"*i)
    
for i in range(4, 0, -1):
    print(f"{i}"*i)
    
a = ""    
b = "khushal27"
while a!=b:
    a = input("enter your password: ")
    if a!=b:
        print("Incorrect Password")
    
print("Correct Password")