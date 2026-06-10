import pandas as pd

# use json file
# url = "file_json.json"
# df = pd.read_json(url)
# print(df)

#convert into csv
# dfc = df.to_csv()

#  convert to excel
# dff = df.to_excel()



# use execl file
# url = "file_excel.xlsx"
# df = pd.read_excel(url)
# print(df)
 
# convert into csv
# dfc = df.to_csv()

# convert into json
# dfj = df.to_json()



# use csv file 
# url = "file1.csv"
# df = pd.read_csv(url)
# print(df)

#  convert to excel
# dff = df.to_excel()

# convert into json
# dfj = df.to_json()



data = {
"Emp_ID": [101, 102, 103, 104, 105, 106],
"Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
"Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
"Salary": [50000, 45000, 60000, 55000, 48000, 52000],
"Experience": [2, 3, 5, 4, 1, 3]

}

df = pd.DataFrame(data)

print(df.head())
print(df.head(2))
print(df.head(-3))

print(df.tail())
print(df.tail(2))
print(df.tail(-2))

print(df.info())
print(df.info(False))

print(df.rename(columns={
    'Name': "Emp_name",
    "Experience": "Experience_(in_year)"
},inplace=False))

df.rename(columns={
    'Name': "Emp_name",
    "Experience": "Experience_(in_year)"
},inplace=True)
print(df)

print(df.describe())
print(df.Salary.describe())