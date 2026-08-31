class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0

        while left < right:
            min_height = min(heights[left],heights[right])
            area = min_height * (right-left)
            max_area = max(area,max_area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
                continue
            
        return max_area

