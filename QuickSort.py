def partition(arr, low, high):
    pivot = arr[high]
    pIndex = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex = pIndex + 1
    arr[high], arr[pIndex] = arr[pIndex], arr[high]
    return pIndex

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

arr = [2,8,9,3,1,7,6]
quicksort(arr, 0, len(arr) - 1)
print(arr)
