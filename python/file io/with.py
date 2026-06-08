# f = open("sample.txt", 'r')
# content = f.read()
# print(content)
# f.close()

with open("sample.txt",'r') as f:
    content = f.read()
    print(content)
    # in this no need to write f.close()