class Solution:
    def maxArea(self, height):
        maximum, left, right = 0, 0, len(height) - 1

        while left < right:
            w = right - left
            h =  min(height[left], height[right])
            area = h * w
            maximum = max(maximum, area)
            if height[left] < height[right]: left += 1
            else: right -= 1

        return maximum