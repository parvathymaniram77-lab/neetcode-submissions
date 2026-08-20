class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        product = 1
        i = 0
        for i in range(len(nums)):
            left.append(product) #refer notes for understanding
            product *= nums[i] # we r mul after appending bcoz we need to avoid current num in mul and this mul including current num will be append in next iteration 

        right = []   
        product = 1
        for j in range(len(nums)-1,-1,-1):
            right.append(product)
            product *= nums[j] 
        right.reverse()
        
        op = []
        for k in range(len(nums)):
            final = left[k] * right[k]
            op.append(final)

        return op
        
        

        





        
# loop throght nums
# read and multiply except the i 
# input into a list the product
# return op