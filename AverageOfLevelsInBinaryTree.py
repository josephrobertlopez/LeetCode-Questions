# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def bfsMST(root: Optional[TreeNode]):
            MST = dict()
            queue = deque()
            queue.append(root)
            visited = []
            MST[root] = [root,0]
            while queue:
                v_i = queue.popleft()
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
            return MST   
        MST = bfsMST(root)
        depths = dict()
        for node in MST:
            depth = MST[node][1]
            if depth not in depths:
                depths[depth] = [node.val]
            else:
                depths[depth].append(node.val)
        print(depths)
        avg_of_lvls = []
        for depth in depths:
            nums = depths[depth]
            avg = sum(nums)/len(nums)
            avg_of_lvls.append(avg)
        return avg_of_lvls