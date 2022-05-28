'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

Example 3:
    Input: nums = [1,2,3]
    Output: 3
'''


class Solution:
    def getMaxLoot(self, nums):
        alternate_house, neighbor, curr_house = 0, nums[0], nums[0]

        for i in range(2, len(nums)+1):
            curr_house = max(nums[i-1]+alternate_house, neighbor)
            alternate_house, neighbor = neighbor, curr_house

        return curr_house

    def rob(self, nums: List[int]) -> int:
        '''
            This is same as house robber I, except for the circular array part.
            Here, we can't have both the first and the last in the same array.
            So, let's exclude first and compute max for the rest.
            Similarly, let's exclude last next and compute max for the rest.
            The max of the 2 answers is the result.
            Only exception is if there's a single house. Handle it separately.
        '''

        if len(nums) == 1:
            return nums[0]
        return max(self.getMaxLoot(nums[1:]), self.getMaxLoot(nums[:-1]))
