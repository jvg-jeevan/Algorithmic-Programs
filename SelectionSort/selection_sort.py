def selection_sort(arr: list, n: int) -> None:
    """
    function to sort the array in increasing order using selection sort.
    in selection sort, in each iteration, the smallest element is selected and placed at the correct position.

    parameters:
    arr (list): the list of elements to be sorted.
    n (int): the number of elements in the list.

    returns:
    none: the function sorts the array in place, so it does not return anything.
    """

    # i iteration until the second last element
    for i in range(n-1):
        # min variable to track the minimum element index, initialized with index i
        min = i
        
        # j iteration from i+1 to the last index
        for j in range(i+1, n):
            # if value at index j is less than the min index value, assign value of j to min
            if arr[j] < arr[min]:
                min = j

        # if the initial min i.e., i is not equal to min index (i.e., if change of min occurs)
        if min != i:
            # swap the values of indexes i and min (this brings the minimum value to the beginning of the list)
            arr[i], arr[min] = arr[min], arr[i]

    # inplace sorting algorithm, no return type


if __name__ == "__main__":
    arr = [64, 34, 25, 90, 88, 77, 45, 23, 56, 43, 67, 29, 15, 80, 66, 54, 31]
    n = len(arr)
    print("unsorted =", arr)
    selection_sort(arr, n)
    print("sorted =", arr)