# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#output=float("-inf")
class Solution:
    def __init__(self):
        self.output=float("-inf")
    def maxPathSum(self, root: TreeNode) -> int:
        self.dfs_tra(root)
        return self.output
        
    def dfs_tra(self,root):
        #print(self.output)
        if(root==None):
            return 0
        left_val=max(0,self.dfs_tra(root.left))
        right_val=max(0,self.dfs_tra(root.right))
        self.output=max(self.output,root.val+left_val+right_val)
        return max(left_val,right_val)+root.val