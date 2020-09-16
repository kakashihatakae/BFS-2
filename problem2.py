class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        count = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[0 for r in range(len(grid))] for c in range(len(grid[0]))]
        flag = 1
        
        while queue:
            temp = []
            for r,c in queue:
                for d in dirs:
                    cr = r + d[0]
                    cc = c + d[1]
                    
                    if (cr>=0) and (cr<len(grid))\
                    and (cc>=0) and (cc<len(grid[0])) and \
                    grid[cr][cc] == 1:
                        grid[cr][cc] = 2
                        temp.append((cr, cc))
            queue = temp
            if flag:
                flag = 0
                continue
            count += 1
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
            
        return count