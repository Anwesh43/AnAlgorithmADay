def get_square_root(a,b,n):
    mid = int((a+b)/2)
    square = mid*mid
    if square == n:
        return mid
    if(a == b):
        return -1
    if square < n:
        return get_square_root(mid+1,b,n)
    else:
        return get_square_root(a,mid-1,n)
def square_root(n):
    if n == 1:
        return 1
    return get_square_root(0,n/2,n)
n = int(raw_input('enter a number'))
print square_root(n)
