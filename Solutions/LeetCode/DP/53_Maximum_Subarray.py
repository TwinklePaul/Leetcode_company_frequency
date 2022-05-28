'''
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

    Intuition: Summary/Kadane's Algorithm.md
'''


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            # local_maxima = max(nums[i], local_maxima+nums[i])
            max_so_far = max(nums[i], max_so_far + nums[i])
            # global_maxima = max(all local maximas)
            max_sum = max(max_sum, max_so_far)

        return max_sum
