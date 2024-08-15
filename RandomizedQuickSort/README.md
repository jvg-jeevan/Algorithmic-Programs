# Quick Sort Algorithm

This repository contains an implementation of the Quick Sort algorithm using a random pivot selection method. Quick Sort is an efficient, divide-and-conquer sorting algorithm that sorts an array by partitioning it into smaller sub-arrays.

## Description

The Quick Sort algorithm works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays: those less than the pivot and those greater than the pivot. The sub-arrays are then sorted recursively.

### Key Features
- **Random Pivot Selection**: A random index is chosen as the pivot to enhance performance and reduce the likelihood of worst-case scenarios.
- **In-Place Sorting**: The algorithm sorts the array without requiring additional storage.

## Implementation

### Code Structure

- **`quick_sort.py`**: Contains the implementation of the Quick Sort algorithm, including the `partition` and `select_random` functions.

### Functions

1. **`select_random(arr: list, low: int, high: int) -> int`**
   - Selects a random index as the pivot and swaps it with the last element, then calls the `partition` function.
   - **Parameters**:
     - `arr`: The list of elements to be partitioned.
     - `low`: The starting index of the section of the list to partition.
     - `high`: The ending index of the section of the list to partition.
   - **Returns**: The partitioning index where the pivot is placed.

2. **`partition(arr: list, low: int, high: int) -> int`**
   - Rearranges the elements in the array such that all elements less than the pivot are on the left, and all elements greater are on the right.
   - **Parameters**:
     - `arr`: The list of elements to be partitioned.
     - `low`: The starting index of the section of the list to partition.
     - `high`: The ending index of the section of the list to partition.
   - **Returns**: The partitioning index where the pivot is placed.

3. **`quick_sort(arr: list, low: int, high: int) -> None`**
   - Sorts the array using the Quick Sort algorithm by repeatedly partitioning the array.
   - **Parameters**:
     - `arr`: The list of elements to be sorted.
     - `low`: The starting index of the section of the list to sort.
     - `high`: The ending index of the section of the list to sort.
   - **Returns**: None (the function sorts the array in place).


## Time and Space Complexity

- **Time Complexity**: 
  - Average case: \(O(n \log n)\)
  - Worst case: \(O(n^2)\) (occurs when the smallest or largest element is always chosen as the pivot)
  
- **Space Complexity**: \(O(\log n)\) due to the recursion stack.

### Conclusion
The Quick Sort algorithm is a powerful and efficient sorting method widely used in computer science for its performance in average cases. This implementation, which incorporates random pivot selection, further enhances its efficiency by reducing the likelihood of encountering worst-case scenarios.
