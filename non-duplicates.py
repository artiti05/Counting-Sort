

def counting_sort_no_duplicates(arr):
    # Handle empty array
    if not arr:
        return []
    
    # Find the minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)
    
    # Size of the counting array
    range_size = max_val - min_val + 1
    counting_arr = [0] * range_size
    
    # Fill the counting array
    for num in arr:
        counting_arr[num - min_val] += 1  # Shift index by min_val
    
    res = []
    for i in range(len(counting_arr)):
        if counting_arr[i] > 0:
            res.append(i+min_val)
    return res


print(f"the res: {counting_sort_no_duplicates([4, -2, 2, 8, -3, 2, 4])}")
