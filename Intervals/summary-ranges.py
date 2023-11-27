class Solution(object):
    def summaryRanges(self, nums):
    
        idx, res = 0, []
        while idx < len(nums):
            start = nums[idx]
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1] - 1:
                idx += 1
            stop = nums[idx]

            if start != stop:
                res.append("{}->{}".format(str(start), str(stop)))
            else:
                res.append(str(stop))
            
            idx += 1
        
        return res
        
        