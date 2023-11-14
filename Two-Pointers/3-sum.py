class Solution:
    def threeSum(self, nums):
        nums.sort()
        results = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values for the first element of the triplet         
            left, right = i+1, len(nums)-1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0: left += 1
                elif current_sum > 0: right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # Adjust pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return results
