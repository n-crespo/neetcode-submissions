class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
            
        return res
            


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""

            while s[i] != "#":
                length += s[i]
                i+=1
                
            i+=1 # skip past the #
                
            res.append(s[i:i+int(length)])
            i += int(length)

        return res
