class Solution:
    def jump(self, nums):
        if len(nums) < 2: return 0
        steps_count, jumps = nums[0], 1
        current_steps_count = nums[0]

        for i in range(1, len(nums)):
            if i > steps_count: 
                steps_count = current_steps_count
                jumps += 1
            current_steps_count = max(current_steps_count, i + nums[i])
        return jumps
