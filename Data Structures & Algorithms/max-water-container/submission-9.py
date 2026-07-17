# OPTIMAL CODE

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights)-1

        while left < right:
            w = abs(left - right)
            h = min(heights[left],heights[right])
            area = w * h
            max_area = max(area,max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
# ALGORITHM

# 1. Initialize:
#    left = 0
#    right = last index
#    max_area = 0

# 2. While left < right:

#    width = right - left

#    height = min(left wall, right wall)

#    area = width × height

#    Update maximum area

# 3. If left wall is smaller
#       left++

#    Else if right wall is smaller
#       right--

#    Else
#       move either pointer

# 4. Return maximum area