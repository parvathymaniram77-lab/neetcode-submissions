class Solution:
    def trap(self, height: List[int]) -> int:

        totalarea = 0

        for k in range(len(height)):
                leftMax = 0
                rightMax = 0               
                for i in range(k-1,-1,-1):
                        leftMax = max(leftMax,height[i])

                for j in range(k+1,len(height)): 
                        rightMax = max(rightMax,height[j])

                area = min(leftMax,rightMax) - height[k]
                if area > 0:
                        totalarea += area
       
        return totalarea



