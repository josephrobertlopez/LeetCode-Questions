# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
#     MST = dict()
#     queue = [root]
#     MST[root] = [root,0]
#     visited = list()
#     step_i = 0
#     while queue:
#         v_i = queue.pop()
#         if v_i not in MST:
#             MST[v_i] = [v_i,step_i+1]
#         else:
#             MST 
def BFS(root: Optional[TreeNode]):
    MST = dict()
    queue = [root]
    visited = []
    MST[root] = [root,0]
    while queue:
        v_i = queue.pop(0)
        if v_i.left:
            if v_i.left not in visited:
                queue.append(v_i.left)
                if v_i.left not in MST:
                    MST[v_i.left] = [v_i,MST[v_i][1]+1]
                elif MST[v_i.left][1] > MST[v_i][1]+1:
                    MST[v_i.left][1] = [v_i,MST[v_i][1]+1]
        if v_i.right:
            if v_i.right not in visited:
                queue.append(v_i.right)
                if v_i.right not in MST:
                    MST[v_i.right] = [v_i,MST[v_i][1]+1]
                elif MST[v_i.right][1] > MST[v_i][1]+1:
                    MST[v_i.right] = [v_i,MST[v_i][1]+1]
        visited.append(v_i)
    print(str(MST))            
        
if __name__ == "__main__":
    root = TreeNode(val=3)
    root.left = TreeNode(val=9)
    root.right = TreeNode(val=20)
    root.right.left = TreeNode(val=15)
    root.right.right = TreeNode(val=7)
    print(BFS(root))
    