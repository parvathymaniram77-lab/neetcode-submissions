class Solution: # same code explained below
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftmax = 0
        rightmax = 0
        total = 0

        while left < right:
            if height[left] < height[right]:
                leftmax = max(height[left],leftmax)
                total += leftmax - height[left]
                left += 1
            else:
                rightmax = max(height[right],rightmax)
                total += rightmax - height[right]
                right -= 1
        return total  




# same code above explained below
class Solution: #refer notes
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        total = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left],left_max)
                total += left_max - height[left] 
                #same as :- 
                #[total = min(left_max, right_max) - current_height],as left is less we proceess left (if condition used above identifies it)
                left += 1
            else:
                right_max = max(height[right],right_max)
                total += right_max - height[right]
                right -= 1

        return total
        
       
# Your logic of calculation 

# Compare the current two heights
# height[left] vs height[right]
# If height[left] is smaller/equal:
# Process the left position.

# Update left_max:

# left_max = maximum of existing left_max and current height[left]

# Calculate trapped water:

# left_max - height[left]

# Add that water to total.
# Move left.
# Otherwise:
# Process the right position.
# Update right_max.

# Calculate:

# right_max - height[right]

# Add to total.
# Move right.