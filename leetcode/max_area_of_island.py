class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [] # 해당 칸을 방문했는지 검사용
        # areaList = [[0 for i in range(len(grid[0]))] for j in range(len(grid))] # 모든 칸에 대해서 area 계산을 수행할 필요 X, 왜냐하면 한 섬 내 모든 칸의 area는 똑같음
        areaMax = 0 # area최고값을 위한 변수
        area = 0
        
        def dfs(grid, x, y, area):
                if (x < 0 or x >= len(grid) or y >= len(grid[0]) or y < 0): # grid 밖
                    return area
            
                if ([x,y] in visited):
                    return area
                else:
                    if (grid[x][y] == 1): # 해당 칸이 육지면 visited에 넣고 area 증가
                        visited.append([x,y])
                        area += 1
                        
                        # 상하좌우 방향에 대해서 dfs 시행
                        area = dfs(grid, x+1, y,area)
                        area = dfs(grid, x-1, y,area)
                        area = dfs(grid, x, y+1,area)
                        area = dfs(grid, x, y-1,area)
                    else:
                        return area
                
                return area
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                # visited = []
                area = 0
                # areaList[i][j] = dfs(grid, i, j, area)
                areaMax = max(areaMax, dfs(grid, i, j, area))
                
        return areaMax
                        
                    
                    
            
            