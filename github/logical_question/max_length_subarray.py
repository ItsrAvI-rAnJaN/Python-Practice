'''
Given an integer array, find the maximum length contiguous subarray having a given sum.

Input : nums[] = [5, 6, -5, 5, 3, 5, 3, -2, 0], target = 8
Output: [-5, 5, 3, 5]
Explanation: The subarrays with sum 8 are [[-5, 5, 3, 5], [3, 5], [5, 3]]. The longest subarray is [-5, 5, 3, 5] having length 4.

Note: Since an input can contain several maximum length subarrays with given sum, the solution should return any one of the maximum length subarray.

'''
def find_max_length_subarray(nums, target):
    max_len = 0
    start_index = 0
    current_sum = 0
    start_pos = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        while current_sum > target:
            current_sum -= nums[start_pos]
            start_pos += 1

        if current_sum == target:
            if i - start_pos + 1 > max_len:
                max_len = i - start_pos + 1
                start_index = start_pos

    if max_len == 0:
        return []
    else:
        return nums[start_index:start_index + max_len]



if __name__ == "__main__":
    nums=[5, 6, -5, 5, 3, 5, 3, -2, 0]
    print(find_max_length_subarray(nums,8))