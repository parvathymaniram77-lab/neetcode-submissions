class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for x in strs:
            result += str(len(x)) + "#" + x
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            word = s[j:j + length]
            ans.append(word)
            i = j + length
        return ans