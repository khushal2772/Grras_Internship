import pandas as pd
df = pd.read_json("sales_json.json")

# print(df.shape,"\n")

# print(df.info(False), "\n")
# print(df.info(),"\n") # by default True


# dfr = df.rename(columns={
#     "Item": "Item_name",
#     "Units": "no_of_unit"
#     },inplace=False) # change col name without effect original data
# print(dfr.info())
# df.rename(columns={"Item": "Item_name"},inplace=True) # change col name and effect original data
# print(df.info())

# print(df.describe())
# print(df.Units.describe())

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df1 = pd.read_json(url)
print(df1['name'],'\n')

# add col
df1["salary"] = df1["marks"] *12
df1["new_salary"] = (df1["salary"] / 10) + df1["salary"] # or df1["new_salary"] = df1["salary"] * 1.10 

print(df1)
