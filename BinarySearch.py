def binarySearch(arr,target):
    st=0
    end=len(arr)-1
    while(st<=end):
        mid = st+(end-st)//2
        if(arr[mid]==target):
            return mid
        if(arr[mid]<target):
            st=mid+1
        elif(arr[mid]>target):
            end=mid-1
    return -1
    
arr = [1,2,3,4,5]
target = 3
index = binarySearch(arr, target)
if index != -1:
    print("Target element found at index", index)
else:
    print("Target element not found")
