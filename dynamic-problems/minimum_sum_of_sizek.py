def get_subsequence_of_k(arr,k):
    maxNum = max(arr)
    newArr = [maxNum for i in range(0,len(arr)+1)]
    newArr[0] = 0
    for i in range(0,len(arr)):
        for j in range(1,i+1):
            if newArr[j-1]+arr[i] < newArr[j]:
                newArr[j] = newArr[j-1]+arr[i]
                break
    print(newArr)
    return newArr[k]
def main():
    arrStr = "58 12 11 12 82 30 20 77 16 86"
    arr = map(int,arrStr.split(" "))
    print(arr)
    k = 3
    print(get_subsequence_of_k(arr,k))

if __name__ == "__main__":
    main()
