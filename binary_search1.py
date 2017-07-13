##Finding first 1 in an sorted array of 0 and 1
def binary_search1(arr,f,l):
    m = (f+l)/2
    if arr[m] == 1:
        if (m>0 and arr[m-1] == 0) or m == 0:
            return m
        else:
            return binary_search1(arr,f,m)
    elif f < l:
        return binary_search1(arr,m,l)
    return -1
def binary_search(arr):
    if arr[len(arr)-1] == 0:
        return -1
    return binary_search1(arr,0,len(arr)-1)
arr = [0,0,0,0,0,0,0]
print binary_search(arr)
