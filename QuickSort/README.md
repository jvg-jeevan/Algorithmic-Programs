# Quick Sort Implementation

This repository contains an implementation of the Quick Sort algorithm in Python. Quick Sort is a highly efficient sorting algorithm that uses the divide-and-conquer approach to sort elements. It is one of the most popular algorithms due to its average-case time complexity of O(n log n) and its ability to sort large datasets quickly.

## Algorithm Description

Quick Sort works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

### Steps:
1. Choose the last element of the array as the pivot.
2. Reorder the array so that all elements with values less than the pivot come before it, and all elements with values greater than the pivot come after it.
3. The pivot is now in its final position.
4. Recursively apply the above steps to the sub-arrays formed by splitting at the pivot index.

### Pseudocode:
```
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
```

### Time Complexity
- **Best Case**: O(n log n) - Occurs when the pivot splits the array into two equal halves.
- **Average Case**: O(n log n) - Quick Sort is efficient on average.
- **Worst Case**: O(n²) - Occurs when the smallest or largest element is always chosen as the pivot.

### Space Complexity
- **O(log n)** - This is the space required for the recursive stack. Quick Sort is an in-place sorting algorithm, so it requires minimal additional memory.

### Example

Consider an unsorted array:
`arr = [29, 15, 37, 8, 22, 41, 56, 13, 7, 18, 32, 49, 25, 11, 60]`

After applying Quick Sort, the sorted array will be:
`arr = [7, 8, 11, 13, 15, 18, 22, 25, 29, 32, 37, 41, 49, 56, 60]`

### Conclusion

Quick Sort is particularly well-suited for large datasets due to its average-case efficiency. While it can degrade to O(n²) time complexity in the worst case, this can be mitigated by using a better pivot selection strategy, such as picking a random pivot or the median.
