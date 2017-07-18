def compute_fibonaci(n):
    arr = [0,1]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    return arr
def main():
    fib_array = compute_fibonaci(10)
    for num in fib_array:
        print(num)
if __name__ == "__main__":
    main()
