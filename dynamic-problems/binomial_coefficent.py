import sys
def compute_binomial_coeff(n):
    arr = []
    for i in range(0,n+1):
        arr.append([0 for x in range(0,i+1)])
    for i in range(0,n+1):
        arr[i][0] = 1
        arr[i][len(arr[i])-1] = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j<=i-1:
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    return arr[n]
def main(n):
    arr = compute_binomial_coeff(n)
    for num in arr:
        print(num)
if __name__ == "__main__" and len(sys.argv[1:]) == 1:
    main(int(sys.argv[1]))
