# optimised with Current code: O(n) time, O(n) extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for i in range(len(nums)-1,-1,-1):
            result.append(product)
            product *= nums[i]
        result.reverse()

        product = 1
        for j in range(len(nums)):
            result[j] = result[j] * product 
            product *= nums[j]

        return result