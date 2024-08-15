def bubble_sort(arr: list, n: int) -> None:
    """
    function to sort the input array in increasing order using bubble sort algorithm.
    in bubble sort, in each iteration, the largest element is selected and placed in the correct position.

    parameters:
    arr (list): the list of elements to be sorted.
    n (int): the number of elements in the list.

    returns:
    none: the function sorts the array in place, so it does not return anything.
    """
    
    # i loop represents the number of passes
    for i in range(n):
        # flag variable to check whether swapping is done or not
        flag = False
        # iteration in j goes until the last but one element in each pass
        for j in range(0, n-i-1):
            # check whether the jth element is greater than the (j+1)th element, if yes, then swap the elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # update the flag variable to true indicating swapping is done
                flag = True

        # if no swapping is done, then break out of the loop indicating the array is already sorted
        if not flag:
            break

# no return value as this is an in-place sorting algorithm
    
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 88, 77, 45, 23, 56, 43, 67, 29, 15, 80, 66, 54, 31]
    n = len(arr)
    print("unsorted arr =", arr)
    bubble_sort(arr, n)
    print("sorted arr =", arr)