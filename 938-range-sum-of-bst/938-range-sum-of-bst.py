# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], L: int, R: int) -> int:
        if not root:            # 예외 처리
            return 0
        
        return (root.val if L <= root.val <= R else 0) + \
                self.rangeSumBST(root.left, L, R) + \
                self.rangeSumBST(root.right, L, R)