from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Step 1: Count frequency
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        # Step 2: Sort by frequency (highest first)
        pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Take the first k numbers
        result = []

        for i in range(k):
            result.append(pairs[i][0])

        return result


obj = Solution()
print(obj.topKFrequent([1,2,2,3,3,3], 2))