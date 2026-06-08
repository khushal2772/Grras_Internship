f = open("sample.txt", 'r')

content = f.read()

print(content)

f.close()

# read line by line 

f = open("sample.txt", 'r')

for line in f:
    print(line)

f.close()
