import math
import mymodule
import requests
print(math.sqrt(16))
print(mymodule.hello())

response = requests.get("https://api.github.com")
print(response.status_code)