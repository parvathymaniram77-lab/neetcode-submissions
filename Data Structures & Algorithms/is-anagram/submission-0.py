class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):
            return False

        result1 = sorted(s)  
        result2 = sorted(t) 
  
        if result1 == result2:
            return True
    
        return False 

obj = Solution()
print(obj.isAnagram("racecar", "carrace"))