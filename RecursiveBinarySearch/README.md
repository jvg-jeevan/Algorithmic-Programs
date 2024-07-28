# Recursive Binary Search

## Theory

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

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

4. **Base Case**:
   - if the current bounds are invalid (`low > high`), the target is not in the array. return `-1`.

### Pseudocode:
```python
function binary_search(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)
```

### Time Complexity
- **Best Case**: O(1) - when the middle element is the target.
- **Average Case**: O(log n) - the list is halved every time.
- **Worst Case**: O(log n) - the list is halved every time.

### Space Complexity
- **O(log n)** - due to the recursion stack. each recursive call adds a new layer to the stack.

### Example

Suppose you have a sorted array `[3, 9, 14, 18, 27, 31, 38, 42, 56, 63, 72, 85, 93, 97]` and you want to find the index of the element `27`.

1. **Initial Call**:
   - `binary_search(arr, 0, 13, 27)`

2. **First Recursion**:
   - calculate `mid = (0 + 13) // 2 = 6`
   - compare `arr[6] (38)` with `27`: `38 > 27`
   - search left half: `binary_search(arr, 0, 5, 27)`

3. **Second Recursion**:
   - calculate `mid = (0 + 5) // 2 = 2`
   - compare `arr[2] (14)` with `27`: `14 < 27`
   - search right half: `binary_search(arr, 3, 5, 27)`

4. **Third Recursion**:
   - calculate `mid = (3 + 5) // 2 = 4`
   - compare `arr[4] (27)` with `27`: `27 == 27`
   - target found, return `4`

this example shows how binary search efficiently narrows down the search range, finding the target `27` at index `4`.

### Conclusion

recursive binary search is a powerful technique for searching through a sorted list, providing efficient time complexity compared to linear search. however, it requires that the list be sorted before the search is performed.
