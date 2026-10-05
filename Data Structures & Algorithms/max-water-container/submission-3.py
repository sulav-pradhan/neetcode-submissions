class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_result = 0
        l, r = 0, len(heights)-1
        while l < r : 
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height 
            if area > max_result: 
                max_result = area
            if heights[l] < heights[r]: 
                l += 1
            else: 
                r -= 1
        return max_result