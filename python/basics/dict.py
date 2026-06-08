# marks = {
#     "aman": 85,
#     "khushal": 81,
#     "kanishk": 78
# }

# # print(marks.items())
# # print(marks.values()) #second elements 
# # print(marks.keys())  # first elements
# # marks.update({"khushal": 95})
# # print(marks)
# print(marks.get("khushal"))
# print(marks["khushal"])
# print(marks.pop("aman"))
# print(marks.popitem()) #pop last item
# marks.clear() # clear all list
# m2 = marks.copy()

# square = {x: x**2 for x in range(1,11)}
# print(square)

# a = input("enter first movie name: ").lower()
# b = input("enter second movie name: ").lower()
# c = input("enter third movie name: ").lower()
# movies = {
#     "Movie1": a,
#     "Movie2": b,
#     "Movie3": c
# }

# search = input("enter movie name to search: ").lower()

# for key, value in movies.items():
#     if search == value:
#         print(f"Found at {key}")
#     else:
#         print("Not Found")
        
        
# b = input("enter car name: ").upper()
# c = input("enter car name: ").upper()

# a = {"car":{
#     "Mahindra": b,
#     "Honda": c,
# }}

# search = input("enter car name to search: ").upper()
# found = False
# for key, value in a["car"].items():
#     if search in value:
#         found = True
#         break
#     else:
#         print("Not Found")
#         found = False

# if found:
#     print("avaliable")
# else:
#     print("not avaliable")

# a = {}

# a[marks["kanishk"]] = marks
# print(a)