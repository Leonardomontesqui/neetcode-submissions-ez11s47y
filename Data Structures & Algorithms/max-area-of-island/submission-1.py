class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        maxArea = 0
        visited = set()

        def area_bfs(r,c):
            area = 1
            visited.add((r,c))
            
            q = collections.deque()
            q.append((r,c))

            print(r)
            print(c)
            while q:
                r,c = q.popleft()
                
                for dr,dc in directions:
                    nr, nc= r+dr, c+dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                        if grid[nr][nc] == 1:
                            area +=1
                            visited.add((nr,nc))
                            q.append((nr,nc))

            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = area_bfs(r,c)
                    if area > maxArea:
                        maxArea = area

        return maxArea

        
        