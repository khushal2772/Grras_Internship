import time as t
import numpy as np

start = t.time()
l = [i*2 for i in range(1000000)]
end = t.time()

print(f"time of perform list task: {end - start}")

start = t.time()
arr = np.array(1000000)*2
end = t.time()
print(f"time of perform array task: {end - start}")

