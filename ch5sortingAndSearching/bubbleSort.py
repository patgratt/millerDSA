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

# better implementation to stop the process if the arr is already sorted

def bubble_sort2(arr):
    exchanges = True
    pass_num = len(arr) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                exchanges = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                pass_num = pass_num - 1
    return arr

arr2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort2(arr2))