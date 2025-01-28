import time

def counting_sort(A, k):
    n = len(A)
    # Step 1: Initialize arrays
    B = [0] * n
    C = [0] * (k + 1)
    
    # Step 2: Count the elements
    for j in range(n):
        C[A[j]] += 1
    
    # Step 3: Accumulate counts
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    
    # Step 4: Build the sorted array
    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    
    return B


# Test the function and measure time

# Example input
A = [4, 2, 2, 8, 3, 3, 1]
k = max(A)

# Record start time
start_time = time.time()

# Call the Counting Sort function
sorted_A = counting_sort(A, k)

# Record end time
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

print("Sorted Array:", sorted_A)
print("Time taken (seconds):", time_taken)
