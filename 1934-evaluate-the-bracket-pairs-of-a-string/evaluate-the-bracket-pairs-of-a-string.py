class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k_map = {pair[0]: pair[1] for pair in knowledge}
        result = []
        n = len(s)
        i = 0
        
        while i < n:
            if s[i] == '(':
                i += 1
                key_start = i
                while i < n and s[i] != ')':
                    i += 1
                key = s[key_start:i]
                i += 1
                
                result.append(k_map.get(key, "?"))
            else:
                result.append(s[i])
                i += 1
                
        return "".join(result)