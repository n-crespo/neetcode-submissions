class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        # if opening, add sto stack
        # if closing,
        #   if top off stack has matching pair, pop and move on
        #   else return false
        stack = []
        for char in s:
            if char in pairs.keys(): # keys
                # we have an closing 
                if len(stack) == 0 or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
                    print("removing..")
                    print(stack)
            else:
                # we have a opening
                stack.append(char)
                print("adding...")
                print(stack)
        return len(stack) == 0
        


        