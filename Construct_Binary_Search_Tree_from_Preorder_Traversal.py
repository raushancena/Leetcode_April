# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder=sorted(preorder)    
        return self.BST(preorder,inorder)
    
    #fuction to make of Bst:-
    
    def BST(self,preorder,inorder):
        if(preorder==[]):
            return None
        root=TreeNode(preorder[0])
        #print(root.val)
        root_index=inorder.index(root.val)
        #print(root_index)
        
        root.left=self.BST(preorder[1:root_index+1],inorder[:root_index])
        root.right=self.BST(preorder[root_index+1:],inorder[root_index+1:])
        return root
        
        