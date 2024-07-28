# Linear Search

## Theory
Linear Search is a fundamental search algorithm that operates on a list of elements. It sequentially checks each element in the list until the desired element is found or the end of the list is reached. This algorithm does not require the list to be sorted and is straightforward to implement.

**Algorithm Steps**:
1. Start at the beginning of the list.
2. Compare the target value with the current element.
3. If the target value matches the current element, return the index of the current element.
4. If the target value does not match and the end of the list is reached, return a value indicating the target is not present (e.g., `-1`).

### Pseudocode:
```python
function linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

## Time Complexity
- **Worst-case Time Complexity**: O(n)
- **Best-case Time Complexity**: O(1)

## Space Complexity
- **Space Complexity**: O(1)

## Example
Suppose you have a list of integers `[4, 2, 7, 1, 9]` and you want to find the index of the number `7`.
- Start with the first element: `4` (not a match).
- Move to the next element: `2` (not a match).
- Move to the next element: `7` (match found at index `2`).

The algorithm returns `2`.
