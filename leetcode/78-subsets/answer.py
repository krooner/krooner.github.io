class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        l = [[]]
        
        def dfs(idx, picked):
            l.append(picked[:])
            
            for i in range(idx+1, len(nums)):
                picked.append(nums[i])
                dfs(i, picked)
                picked.pop()

        for i in range(len(nums)):
            dfs(i, [nums[i]])
        
        return l
        
        