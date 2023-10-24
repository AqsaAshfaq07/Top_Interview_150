class Solution:
    def canJump(self, nums):
        # base cases: diff of first and second step > 0 

        # make a jump of 1
        # now at step 2 - value 3
        # now make a jump of 3 steps 
        # currently at index-1 and after 3 steps -> 1 + 3 -> 4
        # last index of nums -> 4 
        # return true

        # steps count 
        # if final step count == len(nums) - 1:  return true else false

        # approach 
        # start from first index
        # nums[1] - nums[0] -> value 
        # steps_count += value
        # steps_count += nums[2] 
        # and so on

        steps_count = 0
        for i in range(len(nums)):
            if i > steps_count: return False
            steps_count = max(steps_count, i + nums[i])
            if steps_count >= len(nums)-1: return True
        return True
        