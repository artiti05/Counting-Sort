# Counting Sort Algorithm

This README provides an explanation of the Counting Sort algorithm and how it has been implemented in Python to handle floating-point numbers, negative values, non-duplicate values, and an alternative approach using Merge Sort for sorting.

## Overview of Counting Sort
Counting Sort is a non-comparison-based sorting algorithm that sorts elements by counting occurrences of each unique value. It works efficiently for integer keys or values that can be mapped to integers. While it is typically not suited for floating-point numbers or negative values, adaptations can be made to handle such cases.

### Time Complexity
- **Best Case**: O(n + k)
- **Worst Case**: O(n + k)
- **Space Complexity**: O(n + k)

Where:
- `n` is the number of elements to be sorted.
- `k` is the range of input values.

## Features of the Python Implementation
1. **Floating-Point Support**: Adapted to sort floating-point numbers by scaling them to integers.
2. **Negative Number Handling**: Adjusted to sort negative values by offsetting the range.
3. **Non-Duplicates**: Ensures the sorted output contains unique values only.
4. **Merge Sort Integration**: Provides an alternative way to sort the array after preprocessing the input.

## Implementation Details
### Floating-Point Adaptation
To handle floating-point numbers, we scale them to integers by multiplying with a factor (e.g., 10 or 100) based on the precision required. After sorting, we scale the values back to their original form.

### Negative Number Handling
We calculate an offset for negative numbers such that the smallest negative number maps to 0. After sorting, the offset is subtracted to return the values to their original range.

### Unique Values
Before sorting, the list is processed to remove duplicates using Python's built-in set data structure.

### Merge Sort Alternative
Merge Sort, a divide-and-conquer algorithm, is implemented as an alternative to Counting Sort when the input data does not fit the constraints of Counting Sort (e.g., very large ranges).

## Usage
1. **Counting Sort**:
   - Use when the input data is small or has a limited range.
   - Suitable for cases where unique values and specialized handling (e.g., negatives or floats) are required.

2. **Merge Sort**:
   - Use as a general-purpose alternative when the input range is too large for Counting Sort.

## Limitations
- Counting Sort can become inefficient if the range of values (`k`) is significantly larger than the number of elements (`n`).
- Additional processing is required for non-integer values, which can impact performance.

## Conclusion
This implementation of Counting Sort in Python demonstrates its versatility by adapting the algorithm to handle complex cases such as floating-point and negative numbers. By integrating an alternative Merge Sort approach, the solution becomes robust for a variety of use cases.

Feel free to explore and modify the code to suit your specific needs!
