# Given an array and some query ranges we have to find the sum of each query range
# Input
# First Line contains a number n for the number of elements in the array
# Second Line contains n space separated numbers
# Third Line contains a number q for number of query ranges
# Next q line contains two space separated numbers
# Example
#Input
# 9
# 1 1 2 1 3 4 5 2 8
# 3
# 0 4
# 1 3
# 2 4
#Output
# 8
# 4
# 6
n = long(raw_input())
arr = map(long,raw_input().split(' '))
sum_arr = []
sum_of_arr = 0
for i in range(0,n):
    sum_of_arr = sum_of_arr+arr[i]
    sum_arr.append(sum_of_arr)
q = long(raw_input())
results = []
for i in range(0,q):
    q_arr = map(long,raw_input().split(' '))
    if len(q_arr) == 2:
        num_to_sub = 0
        if not(q_arr[0] == 0):
            num_to_sub = sum_arr[q_arr[0]-1]
        results.append(sum_arr[q_arr[1]]-num_to_sub)
for result in results:
    print result
