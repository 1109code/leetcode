# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)         # 이번에는 오르쪽 부터 탐색하며 자식이 없으면 
            return root                                                     # 왼쪽과 오른쪽 스왑
        return None