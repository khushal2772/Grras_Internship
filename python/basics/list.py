# friends = ["apple", 'orange',4 , 48.32, 'aakash']

# print(friends[1:4])

# friends.append("khushal")
# print(friends)

# l1 = [5, 4, 8, 2, 1, 3, 10]
# # l1.sort()
# # l1.reverse()
# # l1.insert(4, 45)
# # a = l1.pop(2)
# # l1.remove(1)
# # l1.append(23)
# l1.insert(5, 23)
# print(l1)
# # print(a)

# table = [2*i for i in range(1,11)]
# print(table)


l = [10,20,30,["hello","hello1","hello2",[True,False]]]
for i in range(len(l)):
 if type(l[i]) == list:
    for j in range(len(l[i])):
        if type(l[i][j]) == list:
            for k in range(len(l[i][j])):
                print(l[i][j][k])
        else:
            print(l[i][j])
 else:
    print(l[i])