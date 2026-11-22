class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)-1):
            if s[i] == "a":
                continue
            elif s[i] == "b":
                if s[i + 1] == "b":
                    continue
                elif s[i + 1] == "a":
                    return False
                    break
        return True
