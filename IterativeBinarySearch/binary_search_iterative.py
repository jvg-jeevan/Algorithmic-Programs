def binary_search(arr: list, target: int) -> int:
    """
    function to find the target element in a sorted array using iterative binary search approach

    parameters:
    arr (list): a sorted list of elements to search within
    target (int): the element to search for in the array

    returns:
    int: the index of the target element if found, otherwise -1
    """
    low = 0
    high = len(arr) - 1

    # continue until value of high remains greater than or equal to low
    while high >= low:
        # mid is middle index of the array
        mid = (low + high) // 2

        # if the target is greater than mid element then move the low index to mid + 1
        if arr[mid] < target:
            low = mid + 1
        
        # if the target is less than mid element then move the high index to mid - 1
        elif arr[mid] > target:
            high = mid - 1
        
        # if target found at mid index then return mid
        else:
            return mid

    # if target not found in the array return -1
    return -1
        
if __name__ == "__main__":
    arr = [3, 9, 14, 18, 27, 31, 38, 42, 56, 63, 72, 85, 93, 97]
    target = 9
    res = binary_search(arr, target)

    print("arr =", arr)
    print("target =", target)
    print("res =", res)