class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0)+1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        for number,frequency in freq.items():
            bucket[frequency].append(number)

        op = []
        for i in range(len(nums), 0, -1):
            for number in bucket[i]:
                op.append(number)
                if len(op) == k:
                    return op
