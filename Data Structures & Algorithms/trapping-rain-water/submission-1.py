class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for k in range(len(height)):
                leftmax = 0
                rightmax = 0

                for i in range(k):
                        leftmax = max(leftmax,height[i])
                for j in range(k+1,len(height)):
                        rightmax = max(rightmax,height[j])

                area = (min(leftmax,rightmax) - height[k])

                if area >0:
                        total += area

        return total