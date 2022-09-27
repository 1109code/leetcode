# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            if node.val < L:                # 어차피 왼쪽 가지들은 현재 노드보다 작으므로
                return dfs(node.right)      # 현재 노드가 L보다 작으면 왼쪽 노드는 탐색 할 필요 X
            elif node.val > R:
                return dfs(node.left)       # 동일
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)