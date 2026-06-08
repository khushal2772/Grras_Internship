# a1 = int(input("enter number 1: "))
# a2 = int(input("enter number 2: "))
# a3 = int(input("enter number 3: "))
# a4 = int(input("enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print(f"{a1} is greater")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print(f"{a2} is greater")
# elif(a3>a1 and a3>a2 and a3>a4):
#     print(f"{a3} is greater")
# else:
#     print(f"{a4} is greater")

# s1 = int(input("enter marks: "))
# s2 = int(input("enter marks: "))
# s3 = int(input("enter marks: "))

# if(s1 >= 33 and s2 >= 33 and s3 >= 33):
#     if((s1+s2+s3)/3 >= 40):
#         print("Passed")
#     else:
#         print("Failed")
# else:
#     print("Failed")

# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("enter your comment: ")

# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("This is spam")
# else:
#     print("This is valid comment")

# username = input("enter username: ")

# if(len(username) > 10):
#     print("characters are greater than 10")
# else:
#     print("characters are less than 10")

# friends = ["apple", 'orange',4 , 48.32, 'aakash']
# item = input("enter item name: ")
# if(item in friends):
#     print("found")
# else:
#     print("Not found")

while True:
    age = int(input("Enter your age:"))
    if age >= 18:
        if age == 18:
            print(f"{age} are exactly 18")
        else:
            print(f"{age} are older than 18")
    else:
        print(f"{age} is less than 18")
