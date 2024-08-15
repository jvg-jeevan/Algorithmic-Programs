from random import randint

def select_random(arr: list, low: int, high: int) -> int:
    """Function to select a random index as key (pivot) and swap the key element with the high element,
    then implement the partition algorithm.

    parameters:
    arr (list): the list of elements to be partitioned.
    low (int): the starting index of the section of the list to partition.
    high (int): the ending index of the section of the list to partition.

    returns:
    int: the partitioning index where the pivot is placed.
    """
    # randint to choose a random integer as key
    key = randint(low, high)
    # swap the key index and high index element
    arr[key], arr[high] = arr[high], arr[key]
    # call the partition function using the updated key value
    return partition(arr, low, high)

def partition(arr: list, low: int, high: int) -> int:
    """Function to put the elements smaller than pivot to the left and greater elements to the right of pivot.

    parameters:
    arr (list): the list of elements to be partitioned.
    low (int): the starting index of the section of the list to partition.
    high (int): the ending index of the section of the list to partition.

    returns:
    int: the partitioning index where the pivot is placed.
    """
    
    # initialize i variable to low-1
    i = low - 1
    # select the last element as pivot
    pivot = arr[high]

    # iterate in j loop from low index to high - 1 index
    for j in range(low, high):
        # if element at j index is less than pivot (this enables the elements smaller than the pivot to stay at left)
        if arr[j] <= pivot:
            # increment the value of i
            i += 1
            # swap value at index i and index j
            arr[i], arr[j] = arr[j], arr[i]

    # swap index i+1 with high index value (this enables the elements greater than the pivot to stay at right)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # return the partitioning index as i + 1
    return i + 1

def quick_sort(arr: list, low: int, high: int) -> None:
    """Quick sort algorithm uses a divide-and-conquer approach to sort the array.
    
    In this approach, the pivot element is selected, and the elements less than the pivot are placed on the left,
    while elements greater than the pivot are placed on the right. This process continues until the array is sorted.

    parameters:
    arr (list): the list of elements to be sorted.
    low (int): the starting index of the section of the list to sort.
    high (int): the ending index of the section of the list to sort.

    returns:
    none: the function sorts the array in place, so it does not return anything.
    """
    
    # divide the array until the low index is less than that of high index
    if low < high:
        # pi stores the index for partitioning
        pi = select_random(arr, low, high)
        # divide the array into two parts and recursively call quick sort for divided parts excluding the pi
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [29, 15, 37, 8, 22, 41, 56, 13, 7, 18, 32, 49, 25, 11, 60]
    print("Unsorted =", arr)
    low = 0
    high = len(arr) - 1
    quick_sort(arr, low, high)
    print("Sorted =", arr)