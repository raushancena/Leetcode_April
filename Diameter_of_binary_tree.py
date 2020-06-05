# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if(root==None):
            return 0
        left_height=self.HeightofBT(root.left)
        right_height=self.HeightofBT(root.right)
        return max((left_height+right_height),max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))
    def HeightofBT(self,root):
        if(root==None):
            return 0
        return max(self.HeightofBT(root.left),self.HeightofBT(root.right))+1
        
        
        
        
        
        