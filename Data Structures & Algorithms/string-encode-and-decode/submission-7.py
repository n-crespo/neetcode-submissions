class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
            


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
