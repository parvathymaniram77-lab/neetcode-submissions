
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right: 
            w = abs(left-right)
            h = min(heights[left],heights[right]) 
            area = w * h         
            max_area = max(area,max_area)

            if heights[left] < heights[right]: #refer notes only shorter height we move
                left += 1                       #bcoz water will get colected only till 
            else:                               #shorter
                right -= 1 #here we also manage == ,as if condition fails auto right -= 1
        return max_area
