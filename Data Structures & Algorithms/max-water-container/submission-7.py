class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            w = right - left
            h = min(heights[left], heights[right])
            area = w * h

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1

            elif heights[left] > heights[right]:
                right -= 1

            else:
                right -= 1      # left += 1 also works

        return max_area

