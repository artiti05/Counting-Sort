import time

def counting_sort_floats(arr, k, d):
    """
    Counting Sort for floating-point numbers in the range [0, k] with up to d decimal places.
    :param arr: List of floating-point numbers to be sorted.
    :param k: Maximum value in the range [0, k].
    :param d: Maximum number of decimal places.
    :return: Sorted list of floating-point numbers.
    """
    # Step 1: Scale numbers to integers
    scale = 10 ** d
    scaled_arr = [round(num * scale) for num in arr]

    # Step 2: Perform Counting Sort on scaled integers
    max_val = int(k * scale)
    counting_arr = [0] * (max_val + 1)
    
    # Count occurrences
    for num in scaled_arr:
        counting_arr[num] += 1
    
    # Reconstruct sorted array
    sorted_scaled_arr = []
    for i, count in enumerate(counting_arr):
        sorted_scaled_arr.extend([i] * count)
    
    # Step 3: Scale back to floating-point numbers
    sorted_arr = [num / scale for num in sorted_scaled_arr]
    return sorted_arr


# Example usage
arr = [0.21, 1.35, 1.02, 0.75, 2.10]
k = 2  # Maximum value in the range [0, k]
d = 2  # At most 2 decimal places

initial_time = time.time()
sorted_arr = counting_sort_floats(arr, k, d)
end_time = time.time()

print("Sorted Array:", sorted_arr)
print(f"Time taken: {end_time - initial_time:.6f} sec")

# Reverse the sorted array
sorted_arr.reverse()
print("Reversed Sorted Array:", sorted_arr)
