import numpy as np

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
[1, 150000, 180000, 220000, 250000], # Paradise Biryani
[2, 120000, 140000, 160000, 190000], # Beijing Bites
[3, 200000, 230000, 260000, 300000], # Pizza Hub
[4, 180000, 210000, 240000, 270000],
[5, 160000, 185000, 205000, 230000]
])

'''
Questions :-

1. Print the complete dataset
2. Find the shape of the array.
3. Find the number of dimensions.
4. Find the total number of elements.
5. Print only Restaurant IDs.
6. Print 2021 sales data.
7. Print 2024 sales data
8. Find the maximum sales value
9. Find the minimum sales value.
10. Find total sales of all restaurants in 2021.
11. Find average sales in 2024.
12. Find total sales of each restaurant.
13. Find average sales of each restaurant.
'''
# 1.
'''i=0
while i < len(sales_data):
    print(sales_data[i])
    i+=1'''

# 2.
# print(sales_data.shape)

# 3.
# print(sales_data.ndim)

# 4.
# print(sales_data.size)

# 5.
# print(sales_data[:,0])

# 6.
# print(sales_data[:,1])

# 7.
# print(sales_data[:,-1])

# 8.
print(np.max(sales_data))

# 9.
print(np.min(sales_data))
# 10.
'''i=0