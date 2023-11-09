from collections import Counter

class Solution:
    def majorityElement(self, nums):
        # n = len(nums)
        # for num in nums:
        #     if nums.count(num) >= n / 2: return num

        counter = Counter(nums)
        max_val = max(counter, key=counter.get)
        return max_val
obj = Solution()
print(obj.majorityElement([3, 2, 2, 3]))