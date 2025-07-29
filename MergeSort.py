def mergeSortedArray(arr1, arr2):
    i = 0
    j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

def mergesort(arr):
    if(len(arr)<=1):
        return arr
    mid=int(len(arr)/2)
    left=arr[:mid]
    right=arr[mid:]
    left=mergesort(left)
    right=mergesort(right)
    return mergeSortedArray(left, right)

arr=[2,3,5,4,2,4,3]
print(mergesort(arr))