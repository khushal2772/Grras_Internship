import pandas as pd

df = pd.Series([10,20,30])
print(df)
print(df[0])

# dict
dict = {"name": ["dheeraj", "kunal","praveen","anjali","abhishek singh"],
    "age": [20,21,22,23,24] ,
    "salary": [{"In-hand":"15000","ctc":"1.2lpa"},{"In-hand":"20000","ctc":"2.2lpa"},
    {"In-hand": "25000","ctc":"3.2lpa"}, {"In-hand": "30000","ctc":"3.2lpa"},
    {"In-hand": "40000", "ctc":"4.2lpa"}]
}
df = pd.DataFrame(dict)
print(df)

# use csv file
url = 'file1.csv'
df = pd.read_csv(url)
print(df)

# use json file
url = "file_json.json"
df = pd.read_json(url)
print(df)

# use excel file
url = "file_excel.xlsx"
df = pd.read_excel(url)
print(df)
