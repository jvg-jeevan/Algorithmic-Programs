# Bubble Sort Implementation

This repository contains an implementation of the Bubble Sort algorithm in Python. Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## Algorithm Description

Bubble Sort works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items, and swapping them if they are in the wrong order. The process is repeated until no more swaps are needed, which indicates that the list is sorted.

### Steps:
1. Start from the first element in the list.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat step 2 until the end of the list.
5. Repeat steps 1-4 for the remaining elements until the list is sorted.

### Pseudocode:
```
function bubble_sort(arr, n):
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
```

### Time Complexity
- **Best Case**: O(n) - when the array is already sorted.
- **Average Case**: O(n²) - when the elements are in random order.
- **Worst Case**: O(n²) - when the array is sorted in reverse order.

### Space Complexity
- **O(1)** - because Bubble Sort is an in-place sorting algorithm.

### Example

Consider an unsorted array:
`arr = [64, 34, 25, 12, 22, 11, 90, 88, 77, 45, 23, 56, 43, 67, 29, 15, 80, 66, 54, 31]

After applying Bubble Sort, the sorted array will be:
`arr = [11, 12, 15, 22, 23, 25, 29, 31, 34, 43, 45, 54, 56, 64, 66, 67, 77, 80, 88, 90]`


### Conclusion

Bubble Sort is an easy-to-implement sorting algorithm, but it is not suitable for large datasets due to its O(n²) time complexity. However, it is a good choice for small datasets or for educational purposes to illustrate how sorting algorithms work.
