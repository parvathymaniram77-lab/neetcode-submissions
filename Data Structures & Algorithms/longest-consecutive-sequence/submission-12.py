class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        seen = set()
        for x in nums:
            if x in seen:
                continue
            seen.add(x)
        max = 0
        for x in seen: 
            count = 1
            if x-1 not in seen:
                while x+1 in seen:
                    x += 1
                    count += 1

            if count > max:
                max = count

        return max


