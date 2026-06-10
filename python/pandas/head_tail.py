import pandas as pd

url = 'sales.csv'
df = pd.read_csv(url)

# head -- print first 5 lines,data of file
print(df.head)
print()

# print first 2 lines
print(df.head(3))
print()

# negative number
print(df.head(-3))
print()

# tail -- print last 5 lines,data of file
print(df.tail)
print()

# print last 3 lines
print(df.tail(3))
print()

# negative for tail
print(df.tail(-3))
print()
