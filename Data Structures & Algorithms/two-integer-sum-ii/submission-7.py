class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        op = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    op.append(i+1)
                    op.append(j+1)
        return op
