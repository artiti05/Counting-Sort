import time
import random

def counting_sort(arr):
    if not arr:
        return []
    
    lil = min(arr)
    k = max(arr)
    
    ran = k - lil + 1
    
    counting_arr = [0]*(ran)
    for num in arr:
        counting_arr[num - lil] += 1
    j = 0
    for i in range(len(counting_arr)):
        while counting_arr[i] > 0:
            arr[j] = i + lil
            j += 1
            counting_arr[i] -= 1
    return arr



initial_time = time.time()

random_values = [random.randint(-1000, 0) for _ in range(100)]

print(counting_sort(random_values = [random.randint(-1000, 0) for _ in range(100)]))
end_time = time.time()

print(f"Time taken: {end_time-initial_time} sec")
x = counting_sort(random_values)
x.reverse()
print(x)