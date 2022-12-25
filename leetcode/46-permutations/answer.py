class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        l = []
        def dfs(picked):
            if len(picked) == len(nums):
                l.append([nums[p] for p in picked])
                return
            
            for j in range(len(nums)):
                if j not in picked:
                    picked.append(j)
                    dfs(picked)
                    picked.pop()
            
        
        for i in range(len(nums)):
            dfs([i])
        
        return l
        
        