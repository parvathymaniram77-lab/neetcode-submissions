class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
            
        key = sorted(freq.items(),key=lambda x:x[1],reverse = True)
        result = []
        for i in range(k):
            result.append (key[i][0])
        return result