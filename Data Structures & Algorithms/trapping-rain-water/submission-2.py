class Solution:
    def trap(self, height: List[int]) -> int:
        
        totalwater = 0
        left = 0
        right = len(height)-1
        leftmax = 0
        rightmax = 0

        while left < right:
                leftmax = max(leftmax,height[left])
                rightmax = max(rightmax,height[right])
                
                if leftmax < rightmax:
                        leftmax = max(leftmax,height[left])
                        water = leftmax-height[left]
                        if water > 0:
                                totalwater += water
                        left += 1
                else:
                        rightmax = max(rightmax,height[right])
                        water = rightmax - height[right]
                        if water > 0:
                                totalwater += water
                        right -= 1           
        return totalwater 