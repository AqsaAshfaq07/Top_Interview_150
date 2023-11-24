class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = {}

        for idx, val in enumerate(nums):
            if val in d and abs(idx - d[val]) <= k:
                return True
            else:
                d[val] = idx
        return False