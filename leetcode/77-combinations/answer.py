class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        l = []
        
        def dfs(pick, picked):
            if len(picked) == k:
                l.append(picked[:])
                return
            
            for i in range(pick+1, n+1):
                picked.append(i)
                dfs(i, picked)
                picked.pop()
        
        
        for i in range(1, n+1):
            dfs(i, [i])
        
        return l