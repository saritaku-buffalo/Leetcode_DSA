class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valiParantheses = {")":"(", "]":"[", "}":"{"}
        
        for c in s:
            if c in valiParantheses:
                if stack and stack[-1] == valiParantheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)    
        return True if not stack else False
            