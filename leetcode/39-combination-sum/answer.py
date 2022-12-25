class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        l = []
        candidates.sort()
        
        def dfs(order, remain, picked):
            if remain == 0:
                l.append(picked[:])
                return
            
            for i in range(order, len(candidates)):
                val = candidates[i]
                if remain - val >= 0:
                    picked.append(val)
                    dfs(i, remain-val, picked)
                    picked.pop()
        
        for i in range(len(candidates)):
            val = candidates[i]
            dfs(i, target-val, [val])
        
        return l
        