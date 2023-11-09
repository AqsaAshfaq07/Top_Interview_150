from collections import Counter

class Solution:
    def removeDuplicatesII(self, nums):
        counter = Counter(nums) 
        for item, val in counter.items():
            while val > 2:
                nums.remove(item)
                val -= 1
obj = Solution()
print(obj.removeDuplicatesII([[0,0,1,1,1,1,2,3,3]]))
