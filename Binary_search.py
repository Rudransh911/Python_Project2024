def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        
        else:
            return binary_search(arr, mid+1, high, x)
    
    else:
        return -1

arr=[1,2,3,4,5,6]
x=6
result= binary_search(arr, 0, len(arr)-1, x)
if result == -1:
    print(x,'is not found in list')
else:
    print(x,'is found in list at index',result)