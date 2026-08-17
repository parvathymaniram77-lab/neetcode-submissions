class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = sorted(nums)
        op = []
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        s = sorted(freq.items(),key=lambda x:x[1],reverse = True)
        for x in s[:k]:
            op.append(x[0])
        return op

