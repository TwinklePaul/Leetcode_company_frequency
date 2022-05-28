'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12.

'''


class Solution:
    # def recRob(self, nums, n, robbery_list):
    #     if n < 0:return 0

    #     if robbery_list[n] != -1: return robbery_list[n]
    #     rob = nums[n] + self.recRob(nums, n-2, robbery_list)
    #     not_rob = self.recRob(nums, n-1, robbery_list)

    #     robbery_list[n] = max(rob, not_rob)
    #     return robbery_list[n]

    def rob(self, nums: List[int]) -> int:
        # robbery_list = [-1]*(len(nums))

        # To convert to tabulation: shift indexes to right by 1.
        # robbery_list = [-1]*(len(nums)+1)
        # robbery_list[0] = 0
        # robbery_list[1] = nums[0]

        # Space Optimization: Store values of 2 previous steps.
        alternate_house, neighbor, curr_house = 0, nums[0], nums[0]

        for i in range(2, len(nums)+1):
            # robbery_list[i] = max(nums[i-1]+robbery_list[i-2], robbery_list[i-1])
            curr_house = max(nums[i-1]+alternate_house, neighbor)
            alternate_house, neighbor = neighbor, curr_house

        # return self.recRob(nums, len(nums)-1, robbery_list)
        # return robbery_list[-1]
        return curr_house
