"""
Given an integer array, check if it contains a contiguous subarray having zero-sum.
Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: True
Explanation: The subarrays with zero-sum are

[3, 4, -7]
[4, -7, 3]
[-7, 3, 1, 3]
[3, 1, -4]
[3, 1, 3, 1, -4, -2, -2]
[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

Input : [4, -7, 1, -2, -1]
Output: False
Explanation: The subarray with zero-sum doesn't exist.

"""
def subarray_zero_sum(arr):
    zero_sum=0
    for n in range(0,len(arr)):
        zero_sum=zero_sum + arr[n]
    if zero_sum==0:
        return True
    return False


if __name__ =="__main__":
    # arr=[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    arr=[4, -7, 1, -2, -1]
    print(subarray_zero_sum(arr))

