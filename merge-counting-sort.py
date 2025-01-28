def counting_sort(arr):
    if not arr:
        return []
    m = min(arr)
    k = max(arr)
    
    ran = k - m + 1
    counting_arr = [0] * ran
    for num in arr:
        counting_arr[num - m] += 1
    
    j = 0
    for i in range(ran):
        while counting_arr[i] > 0:
            arr[j] = i + m
            j += 1
            counting_arr[i] -= 1
    return arr
    
def compining(arr, num_subarrays=2):
    subarrays = [arr[i::2] for i in range(num_subarrays)]
    
    sorted_subArrays = [counting_sort(subarray) for subarray in subarrays]
    # print(sorted_subArrays)
    merged_result = sorted_subArrays[0]
    for i in range(1,len(sorted_subArrays)):
        merged_result = merging(merged_result, sorted_subArrays[i])
    
    return merged_result

def merging(f, s):
    merged = []
    i, j = 0, 0
    while i < len(f) and j < len(s):
        if f[i] >= s[j]:
            merged.append(s[j])
            j += 1
        else:
            merged.append(f[i])
            i += 1
    merged.extend(f[i:])
    merged.extend(s[j:])
    return merged



print(compining([4, 2, 2, 8, 3, -1, -2, 5, 7, 4], num_subarrays=2))