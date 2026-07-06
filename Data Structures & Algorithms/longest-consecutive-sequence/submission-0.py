class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        curr_num = 0
        length = 1

        numSet = set(nums)
        for x in numSet:
            curr_num = x
            if curr_num - 1 in numSet:
                continue
            while curr_num + 1 in numSet:                           
                curr_num = curr_num + 1
                length += 1
            max_len = max(max_len,length)
            length = 1
        return max_len
      