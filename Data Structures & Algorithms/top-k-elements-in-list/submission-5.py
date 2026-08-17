class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        op = []
        for x in nums:
            freq[x] = freq.get(x,0)+ 1

        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        for number,frequency in freq.items():
            bucket[frequency].append(number) #bucket[2].append[5] here frequency is a number we r appending the value to the number(frequency) which is from freq dict hidden comaprison we did without explicitly writing comparison so we directly assigning and accesing the exact index in bucket corresponding to frequency in freq dict
        for i in range(len(nums), 0, -1):
            for number in bucket[i]:
                op.append(number) 
                if len(op) == k:
                    return op  
