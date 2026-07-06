class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for x in strs:
            key = "".join(sorted(x))
            if key not in result:
                result[key] = []
            result[key].append(x)
            
        return list(result.values())


           