



'''
Given an integer array, find the maximum difference between two elements in it such that the smaller element appears before the larger element. If no such pair exists, return any negative number.

Input : [2, 7, 9, 5, 1, 3, 5]
Output: 7
Explanation: The pair with the maximum difference is (2, 9).

Input : [5, 4, 3, 2, 1]
Output: -1 (or any other negative number)
Explanation: No pair with the maximum difference exists.

'''



def max_diff(arr):
    n = len(arr)
    if n < 2:
        return -1
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
    for i in range(1, n):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
        if (arr[i] < min_element):
            min_element = arr[i]
    if max_diff <= 0:
        return -1
    
    return max_diff



if __name__=="__main__":
    arr=[2, 7, 9, 5, 1, 3, 5]
    print(max_diff(arr))