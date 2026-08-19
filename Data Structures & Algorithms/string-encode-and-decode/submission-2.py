class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:            
            s += str(len(x))+"#"+x  
        return s

    def decode(self, s: str) -> List[str]:
        op = []
        i = 0
        while i < len(s):
            num = ""
            while s[i] != "#":
                num += s[i]
                i+= 1
            num = int(num)
            i += 1
  
            word = ""
            for j in range(i,i+num):
                word += s[j]
            op.append(word)
            i += num
        return op

          

                    

# logical Algorithm
# ENCODE
# for each string x:
#     length + "#" + x
# DECODE
# i = 0
# while i < len(s):
#     read length
#     find "#"
#     move past "#"
#     take `length` characters
#     append that string to op
#     move i past those characters

            
