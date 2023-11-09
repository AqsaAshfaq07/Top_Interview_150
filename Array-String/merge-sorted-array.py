class Solution:
    """ This class will be used for implementation of the problem Merge Sorted Array - leetcode"""
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = []
        nums1.extend(nums2)
        return nums1.sort()

obj = Solution()
print(obj.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
