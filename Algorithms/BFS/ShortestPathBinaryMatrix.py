# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List
def find_adjacent_cells(grid: List[List[int]], v: list[int]) -> list[list[int]]:
        n = len(grid)
        possible_moves = [[1,1],[1,0],[0,1],[-1,0],[0,-1],[1,-1],[-1,1]]
        adjacency_list = list()
        for move in possible_moves:
            v_hat = [v[0]+move[0],v[1]+move[1]]
            if v_hat[0] in range(n) and v_hat[1] in range(n):
                if grid[v_hat[0]][v_hat[1]] != 1:
                    adjacency_list.append(v_hat)
        return adjacency_list
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
        frontier = list()
        v_0 = [0,0]
        n = len(grid)
        steps = 0
        frontier.append(v_0)
        while len(frontier)>0:
            v_i = frontier.pop(0)
            if grid[v_i[0]][v_i[1]] == 1:
                continue
            grid[v_i[0]][v_i[1]] = 1
            steps+=1
            adjacency_list = find_adjacent_cells(grid,v_i)
            print("adjacency List"+str(adjacency_list))
            for v in adjacency_list:
                frontier.append(v)
            print("frontier"+str(frontier))
            if v_i[0] == n-1 and v_i[0] == n-1:
                return steps
            print("vi"+str(v_i))
            print("grid"+str(grid))
            print("steps "+str(steps))
            print()
        return -1

if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(shortestPathBinaryMatrix(grid))