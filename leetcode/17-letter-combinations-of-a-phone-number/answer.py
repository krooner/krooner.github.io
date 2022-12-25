class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        table = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        
        l = []
        
        def dfs(i, text):
            if i == len(digits):
                l.append(text)
                return
            
            digit = digits[i]
            chars = table[int(digit)]
            for c in list(chars):
                dfs(i+1, text+c)
            
            return
            
            
        dfs(0, "")
        
        return l