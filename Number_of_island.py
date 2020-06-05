def dfs(grid,i,j):
        grid[i][j]="-1"
        try:
            if(grid[i][j+1]=="1"):
                dfs(grid,i,j+1)
        except:
            pass
        try:
            if(j>0):
                if(grid[i][j-1]=="1"):
                    dfs(grid,i,j-1)
        except:
            pass
        try:
            if(i>0):
                if(grid[i-1][j]=="1"):
                    dfs(grid,i-1,j)
        except:
            pass
        try:
            if(grid[i+1][j]=="1"):
                dfs(grid,i+1,j)
        except:
            pass

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    dfs(grid,i,j)
                    s=s+1
        return s