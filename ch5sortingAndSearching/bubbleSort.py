# basic implementation

def bubble_sort1(arr):
    # this loop creates a range object counting down starting at the length of the arr
    for pass_num in range(len(arr) - 1, 0, -1):
        # scan the array pass_num times
        for i in range(pass_num):
            # if the first is greater than the second, swap em
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

