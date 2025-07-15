def counting_sort(arr):
    max_ = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_:
            max_ = arr[i]
    count = [0 for ] * (max_ + 1)
    for num in arr:
        count[num] += 1
    ans = []
    for i in range(len(count)):
        ans.extend([i] * count[i])
    return ans

arr=[2,3,5,4,2,4,3]
print(counting_sort(arr))
#sort the char (alphabets and digits) using counting sort