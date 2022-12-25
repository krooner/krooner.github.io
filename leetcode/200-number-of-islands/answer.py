class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        rlen, clen = len(grid), len(grid[0])
    
        def dfs(r, c):
            grid[r][c] = "0"
            for k in range(4):
                rr, cc = r+dr[k], c+dc[k]
                if 0<=rr<rlen and 0<=cc<clen and grid[rr][cc] == "1":
                    dfs(rr, cc)
        
        answer = 0
        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == "1":
                    answer += 1
                    dfs(i, j)
        
        return answer