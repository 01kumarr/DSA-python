'''
Given an array of intergers, we need to find the sum of particular subarray then use prefix sum

'''

arr = [2,3,8,5,9,24,65]

prefix_sum = [-1 for i in range(len(arr))]

prefix_sum[0] = arr[0]

for i in range(1, len(arr)):
    prefix_sum[i] = arr[i] + arr[i-1]


print(prefix_sum)