# Iterative Binary Search

## Theory

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. The iterative approach avoids the overhead of recursive function calls.

### Steps:

1. **Initialization**:
   - the search starts with the entire array and the initial indices `low` and `high` representing the current search bounds.
   
2. **Calculate the Middle**:
   - calculate the middle index of the current bounds: `mid = (low + high) // 2`.

3. **Compare the Middle Element**:
   - compare the target element with the middle element of the array:
     - if the target is equal to the middle element, return the middle index.
     - if the target is less than the middle element, search the left half by updating `high` to `mid - 1`.
     - if the target is greater than the middle element, search the right half by updating `low` to `mid + 1`.

4. **Loop Until Found or Bounds Invalid**:
   - repeat steps 2 and 3 until the target is found or the current bounds are invalid (`low > high`).
   - if the target is not found, return `-1`.

### Pseudocode:
```python
function binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1
```

### Time Complexity
- **Best Case**: O(1) - when the middle element is the target.
- **Average Case**: O(log n) - the list is halved every time.
- **Worst Case**: O(log n) - the list is halved every time.

### Space Complexity
- **O(1)** - no additional space is required apart from the input list.

### Example

Suppose you have a sorted array `[3, 9, 14, 18, 27, 31, 38, 42, 56, 63, 72, 85, 93, 97]` and you want to find the index of the element `9`.

1. **Initial Call**:
   - `binary_search(arr, 9)`

2. **First Iteration**:
   - calculate `mid = (0 + 13) // 2 = 6`
   - compare `arr[6] (38)` with `9`: `38 > 9`
   - search left half: `high = 5`

3. **Second Iteration**:
   - calculate `mid = (0 + 5) // 2 = 2`
   - compare `arr[2] (14)` with `9`: `14 > 9`
   - search left half: `high = 1`

4. **Third Iteration**:
   - calculate `mid = (0 + 1) // 2 = 0`
   - compare `arr[0] (3)` with `9`: `3 < 9`
   - search right half: `low = 1`

5. **Fourth Iteration**:
   - calculate `mid = (1 + 1) // 2 = 1`
   - compare `arr[1] (9)` with `9`: `9 == 9`
   - target found, return `1`
### Conclusion

iterative binary search is a powerful technique for searching through a sorted list, providing efficient time complexity compared to linear search. it avoids the overhead of recursion by using a loop.
