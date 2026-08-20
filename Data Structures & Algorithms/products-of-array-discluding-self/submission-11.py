# optimised with Current code: O(n) time, O(n) extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        product = 1
        for i in range(len(nums)):
            left.append(product)
            product *= nums[i]

        right = []
        product = 1
        for j in range(len(nums)-1,-1,-1):
            right.append(product)
            product *= nums[j]
        right.reverse()

        op = []
        for k in range(len(nums)):
            result = left[k] * right[k]
            op.append(result)
        return op
            

        





        
# loop throght nums
# read and multiply except the i 
# input into a list the product
# return op