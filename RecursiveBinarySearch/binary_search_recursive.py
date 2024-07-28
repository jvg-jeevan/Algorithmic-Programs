def binary_search(arr: list, low: int, high: int, target: int) -> int:
    """
    function to find the index of the target element in an array using recursive binary search.

    parameters:
    arr (list): the list of elements to search through.
    low (int): the lower bound index of the list.
    high (int): the upper bound index of the list.
    target (int): the target element to search for.

    returns:
    int: the index of the target element if found, otherwise -1.
    """
    
    # continue the search while the lower bound is less than or equal to the upper bound
    if low <= high:
        # calculate the middle index
        mid = (low + high) // 2

        # if the target is greater than the middle element, search the right half, i.e assign the value of mid+1 to low
        if arr[mid] < target:
            return binary_search(arr, mid + 1, high, target)
        
        # if the target is less than the middle element, search the left half, i.e assign the value of mid-1 to high
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        
        # if the target is equal to the middle element, return the middle index
        else:
            return mid
        
    # if the target is not found, return -1
    else:
        return -1

if __name__ == "__main__":
    arr = [3, 9, 14, 18, 27, 31, 38, 42, 56, 63, 72, 85, 93, 97]
    target = 27
    low = 0
    high = len(arr) - 1
    res = binary_search(arr, low, high, target)

    print("array:", arr)
    print("target:", target)
    print("result index:", res)