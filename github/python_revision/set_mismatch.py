class Solution(object):
    def find_error_nums(self, nums):
        n = len(nums)
        s = n * (n + 1) // 2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]


if __name__ == '__main__':
    # nums = [1, 2, 2, 4]
    nums = [1, 1]
    obj = Solution()
    print(obj.find_error_nums(nums))
