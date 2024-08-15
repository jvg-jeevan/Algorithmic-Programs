# Insertion Sort Implementation

This repository contains an implementation of the Insertion Sort algorithm in Python. Insertion Sort is a simple and intuitive comparison-based sorting algorithm that builds the final sorted array one item at a time. It is much like sorting playing cards in your hands; each card is inserted into its correct position in an already sorted part of the array.

## Algorithm Description

Insertion Sort works by dividing the array into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

### Steps:
1. Start with the second element (index 1) of the array.
2. Compare the selected element (key) with the elements in the sorted part (i.e., elements before it).
3. Shift all elements in the sorted part that are greater than the key one position to the right.
4. Insert the key element into the correct position in the sorted part.
5. Repeat the process for all elements in the unsorted part until the entire array is sorted.

### Pseudocode:
```
function insertion_sort(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

### Time Complexity
- **Best Case**: O(n) - When the array is already sorted, the algorithm only performs n-1 comparisons.
- **Average Case**: O(n²) - The algorithm performs a quadratic number of comparisons on average.
- **Worst Case**: O(n²) - When the array is sorted in reverse order, the algorithm performs the maximum number of comparisons and shifts.

### Space Complexity
- **O(1)** - Insertion Sort is an in-place sorting algorithm, requiring only a constant amount of additional memory.

### Example

Consider an unsorted array:
`arr = [29, 10, 14, 37, 13, 12, 34, 25, 18, 22, 30, 8, 17, 11, 33, 21, 19, 28, 24, 27]`

After applying Insertion Sort, the sorted array will be:
`arr = [8, 10, 11, 12, 13, 14, 17, 18, 19, 21, 22, 24, 25, 27, 28, 29, 30, 33, 34, 37]`
### Conclusion
Insertion Sort is efficient for small data sets or nearly sorted data. While it is not suitable for large datasets due to its O(n²) time complexity, it is easy to implement and understand, making it a useful algorithm in certain scenarios.
