class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  
        op = []
        seen= set()   
        nums.sort()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
        
            target = -nums[i]
            
            while left < right:
                if nums[left] + nums[right] < target:
                    left +=1
                    continue   
                if nums[left] + nums[right] > target:
                    right -=1
                    continue
                if nums[left] + nums[right] == target:
                    triplet = [nums[left],nums[right],nums[i]]
                    left += 1
                    right -= 1   
                    triplet.sort()
                    seen.add(tuple(triplet))
   
        for triplet in seen:
            op.append(list(triplet))
        return op
        
        
       