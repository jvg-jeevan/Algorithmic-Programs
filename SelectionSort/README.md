# Selection Sort Implementation

This repository contains an implementation of the Selection Sort algorithm in Python. Selection Sort is a simple comparison-based sorting algorithm that divides the list into two parts: the sorted part at the left end and the unsorted part at the right end. It repeatedly selects the smallest element from the unsorted part and swaps it with the leftmost unsorted element, moving the boundary between the sorted and unsorted parts one element to the right.

## Algorithm Description

Selection Sort works by repeatedly finding the minimum element (considering ascending order) from the unsorted part and swapping it with the first unsorted element. The algorithm maintains two subarrays in a given array:
- **Subarray 1**: The subarray which is already sorted.
- **Subarray 2**: The subarray which is unsorted.

In each iteration of Selection Sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray.

### Steps:
1. Start from the first element in the list.
2. Find the minimum element in the unsorted subarray.
3. Swap it with the first unsorted element.
4. Move the boundary between the sorted and unsorted parts one element to the right.
5. Repeat until the entire array is sorted.

### Pseudocode:
```
function selection_sort(arr, n):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
```

### Time Complexity
- **Best Case**: O(n²) - The number of comparisons is always the same, regardless of the initial order of elements.
- **Average Case**: O(n²) - The algorithm always performs O(n²) comparisons.
- **Worst Case**: O(n²) - Even if the array is sorted in reverse order, the algorithm will still perform O(n²) comparisons.

### Space Complexity
- **O(1)** - Selection Sort is an in-place sorting algorithm, so it requires a constant amount of additional memory.

### Example

Consider an unsorted array:
`arr = [64, 34, 25, 90, 88, 77, 45, 23, 56, 43, 67, 29, 15, 80, 66, 54, 31]
`

After applying Selection Sort, the sorted array will be:
`arr = [15, 23, 25, 29, 31, 34, 43, 45, 54, 56, 64, 66, 67, 77, 80, 88, 90]`


### Conclusion

Selection Sort is a straightforward and easy-to-implement sorting algorithm. However, it is not the most efficient algorithm for large datasets due to its O(n²) time complexity. It is primarily used for small arrays or as an educational tool to demonstrate basic sorting concepts.

