def insertion_sort(arr, n):
    """
    function to sort the elements in the array in increasing order using insertion sort.
    in this sorting technique, each element is placed in its correct position within the already sorted part of the array.

    parameters:
    arr (list): the list of elements to be sorted.
    n (int): the number of elements in the list.

    returns:
    none: the function sorts the array in place, so it does not return anything.
    """

    # iterate over the array starting from the second element
    for i in range(1, n):
        # key element is chosen as the ith index element
        key = arr[i]
        # initialize the variable j for comparison with i - 1 in each iteration
        j = i - 1
        
        # move elements of arr[0..i-1] that are greater than the key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # store the key at the resultant j+1th index
        arr[j + 1] = key

    # no return type as this is an in-place sorting algorithm
    
if __name__ == "__main__":
    arr = [29, 10, 14, 37, 13, 12, 34, 25, 18, 22, 30, 8, 17, 11, 33, 21, 19, 28, 24, 27]
    n = len(arr)
    print("unsorted =", arr)
    insertion_sort(arr, n)
    print("sorted =", arr)
