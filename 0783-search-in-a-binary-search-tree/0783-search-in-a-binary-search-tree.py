# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if not node:
                return None
            if node.val == val:
                return node            
            if node.val < val:
                return search(node.right)
            if node.val > val:
                return search(node.left)
        
        return search(root)
        """
        while root:
            if root and root.val > val:
                root = rootleft

            elif root and root.val < val:
                root = root.right
            else:
                return root
        
        """
            
        