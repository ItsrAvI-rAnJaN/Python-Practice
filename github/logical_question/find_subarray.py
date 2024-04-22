'''
Given an integer array, find all contiguous subarrays with zero-sum.

Input : [4, 2, -3, -1, 0, 4]
Output: {(0), (-3, -1, 0, 4)}

Input : [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
Output: {(3, 4, -7, 3, 1, 3, 1, -4, -2, -2), (3, 4, -7), (3, 1, 3, 1, -4, -2, -2), (3, 1, -4), (-7, 3, 1, 3), (4, -7, 3)}

Input : [0, 0]
Output: {(0), (0, 0)}

Input : [1, 2, 3]
Output: {}

Note: Since an input can have multiple subarrays with zero-sum, the solution should return a set of tuples containing all the distinct subarrays.

'''

# def find_subarray(arr):
#     zero_sum_array=[]
#     zero_sum=0
#     for n in range(0,len(arr)):
#         zero_sum=zero_sum+arr[n]
#         zero_sum_array.append(arr[n])
#     if zero_sum==0:
#         return (zero_sum,zero_sum_array)
    


# if __name__ == "__main__":
#     arr=[4, 2, -3, -1, 0, 4]
#     print(find_subarray(arr))

def find_zero_sum_subarrays(arr):
    result = set()
    zero_sum = 0
    sum_dict = {0:-1}

    for i in range(len(arr)):
        zero_sum+= arr[i]

        if zero_sum in sum_dict:
            start_index = sum_dict[zero_sum] + 1
            subarray = tuple(arr[start_index:i+1])
            result.add(subarray)
        else:
            sum_dict[zero_sum] = i

    return result

if __name__ == "__main__":
    # arr=[3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    arr=[4, 2, -3, -1, 0, 4]
    print(find_zero_sum_subarrays(arr))
        

