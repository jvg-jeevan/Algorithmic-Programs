def linear_search(arr: list, n: int, target: int) -> int:
    """
    performs a linear search through the given list.

    args:
    arr (list): the list to search.
    n (int): the number of elements in the list.
    target (int): the value to search for.

    returns:
    int: the index of the target if found, otherwise -1.
    """
    # iterate through each index in the list
    for i in range(n):
        # check if the current element matches the target
        if arr[i] == target:
            # if it matches, return the index
            return i
    
    # if no element matches the target, return -1
    return -1

if __name__ == "__main__":

    arr = [29, 15, 37, 8, 22, 41, 56, 13, 7, 18, 32, 49, 25, 11, 60]
    n = len(arr)
    print("Array =", arr)
    
    # user inpur for the target value
    target = int(input("Enter the target value: "))
    
    # search for the target and get its index
    index = linear_search(arr, n, target)
    
    # display the result
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found.")
