class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        max_len = 0

        numSet = set(nums)
        for num in numSet:
            curr = num
            if curr-1 in numSet:
                continue
            while curr+1 in numSet:
                    curr = curr + 1
                    length +=1
            max_len = max(max_len,length)
            length = 1
        return max_len    
