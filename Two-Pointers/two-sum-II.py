class Solution:
    def twoSum(self, numbers, target):
        result = {}
        for i, num in enumerate(numbers):
            second = target - num 
            if second in result:
                return [result[second] + 1, i + 1]
            result[num] = i
        return []
