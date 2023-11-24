class Solution(object):
    ''' https://leetcode.com/problems/two-sum/'''
    def two_sum(self, nums, target):
        ''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''
        seen = {}  # val -> index
        for i, num in enumerate(nums):  # returns both index and the number
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i