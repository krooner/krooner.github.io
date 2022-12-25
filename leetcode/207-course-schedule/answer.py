from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        
        for c, p in prerequisites:
            graph[c].append(p)
            
        traced = set()
        visited = set()
        
        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            
            traced.add(i)
            for c in graph[i]:
                if not dfs(c):
                    return False
            
            traced.remove(i)
            visited.add(i)
            
            return True
        
        for c in list(graph.keys()):
            if not dfs(c):
                return False
        
        return True