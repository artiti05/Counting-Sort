import time

def counting_sort(arr):
    k = max(arr)
    counting_arr = [0]*(k+1)
    for num in arr:
        counting_arr[num] += 1
    j = 0
    for i in range(len(counting_arr)):
        while counting_arr[i] > 0:
            arr[j] = i
            j += 1
            counting_arr[i] -= 1
    return arr

initial_time = time.time()
print(counting_sort([4, 2, 2, 8, 3]))
end_time = time.time()
print(f"Time taken: {end_time-initial_time} sec")
x = counting_sort([4, 2, 2, 8, 3])
x.reverse()
print(x)