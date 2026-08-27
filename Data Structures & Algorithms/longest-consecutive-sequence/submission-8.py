class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
        max = 0
        for x in seen:
            count = 1
            if x-1 not in seen:
                while x+1 in seen:
                    x += 1
                    count += 1
            if max < count:
                max = count

        return max

            


            
        