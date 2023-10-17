class Solution:
    def removeDuplicates(self, nums):
        # nums, remove duplicates in-place
        if len(nums) < 2:
            return len(nums)
        k = 0
        for i in range(1, len(nums)):
            if nums[k-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k        
obj = Solution()
print(obj.removeDuplicates([1, 1, 2]))
