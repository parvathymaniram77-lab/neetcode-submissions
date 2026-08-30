class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            op = []
            seen = set()
            nums = sorted(nums)
            for i in range(len(nums)):
                        left = i+1
                        right = len(nums)-1
                        
                        while left < right:
                
                            if i == left:
                                left += 1
                                right -= 1
                                continue
                                
                            if i == right:
                                left += 1
                                right -= 1              
                                continue

                            if nums[left] + nums[right] + nums[i] < 0:
                                left += 1

                            elif nums[left] + nums[right] + nums[i] > 0 :
                                right -= 1

                            else:
                                if [nums[left], nums[right], nums[i]] not in op:
                                    op.append([nums[left], nums[right], nums[i]])
                                left += 1
                                right -= 1
                                
            return op