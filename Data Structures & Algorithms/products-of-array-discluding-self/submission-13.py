# optimised with Current code: O(n) time, O(n) extra space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        product = 1
        for i in range(len(nums)-1,-1,-1):
            right.append(product)
            product *= nums[i]
        right.reverse()

        product = 1
        for j in range(len(nums)):
            right[j] = right[j]*product
            product *= nums[j]

        return right