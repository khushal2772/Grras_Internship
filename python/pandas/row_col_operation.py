import pandas as pd
df = pd.read_json("sales_json.json")

# col operations

# print(df.shape,"\n")

# print(df.info(False), "\n")
# print(df.info(),"\n") # by default True


dfr = df.rename(columns={
    "Item": "Item_name",
    "Units": "no_of_unit"
    },inplace=False) # change col name without effect original data
# print(dfr.info())
df.rename(columns={"Item": "Item_name"},inplace=True) # change col name and effect original data
# print(df.info())

# print(df.describe())
# print(df.Units.describe())

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df1 = pd.read_json(url)
print(df1['name'],'\n')

# add col
df1["salary"] = df1["marks"] *12
df1["new_salary"] = (df1["salary"] / 10) + df1["salary"] # or df1["new_salary"] = df1["salary"] * 1.10 
# print(df1)

# del col
df1.drop(["salary"],axis=1,inplace=True)
# print(df1)

# loc and iloc
# print(df1.loc[2,"name"])
# print(df1.iloc[2,0])

# get single row data using loc
# print(df1.loc[2],"\n")

# get single row data using iloc
# print(df1.iloc[2])

url = "https://raw.githubusercontent.com/khushal2772/Grras_Internship/refs/heads/main/python/pandas/student-data.json"
df = pd.read_json(url)
# print(df,"\n")

# male students
# print(df[df["gender"] == "Male"])

# print(df.loc[:, ["name", "maths"]])
# print(df.iloc[3:10:5])

# filter
# print(df.loc[df["physics"] > 80, ["name", "physics"]])
# print(df.loc[df["physics"] <= 56, ["name", "physics"]])

# print(df.loc[(df["maths"] <= 90)&(df["physics"] >= 90)], ["name","physics","maths"])
# print(df.loc[(df["maths"] <= 90)&(df["physics"] >= 90) | (df["gender"] == "Male")], ["name","physics","maths"])

# sort according to a particular col
# print(df.sort_values("english"))

# sort in decending order
# print(df.sort_values("english",ascending=False))

# sorted using two col
# print(df.sort_values(by=["maths","english"],ascending=[False,False]))

df["name"] = df["name"].str.title()
# print(df.sort_values("name"))

# add row
df.loc[14] = ["khushal", "Male", 86, 76, 98]
# print(df)

# del row
df.drop([14],axis=0, inplace=False)
# print(df)

# update rows
df.iloc[5,2] = [98]
df.loc[2] = ["Khushal","Male", 25, 68, 97]
# print(df)

# add data to file
# df.to_csv("sample.csv", mode="w", index=False)

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.to_json("sample.json", mode="w", index=False)

# add new col
df["doj"] = ['2025-01-10','2025-02-10','2025-03-10','2025-04-10','2025-05-10']

print(df["doj"].dtype)
df["doj"] = pd.to_datetime(df["doj"])
print(df["doj"].dt.day_name())

# add 20 days
df["doj"] = df["doj"] + pd.Timedelta(days=10)
df["doj"] + pd.Timedelta(days=10) # not change in original
print(df)

                                                                                                                                                                                                                                           