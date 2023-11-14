class Solution:
    def minSubArrayLen(self, target, nums):
        # nums, target , 
        # return length of subarray sum >= target
        # else return 0

        left, right = 0, 0
        window_sum, min_length = 0, float('inf')

        while right < len(nums):
            window_sum += nums[right]
            right += 1
            while window_sum >= target:
                min_length = min(min_length, right - left)
                window_sum -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length
            