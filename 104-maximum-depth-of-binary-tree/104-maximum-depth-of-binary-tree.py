# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:                   # 현재 루트의 왼쪽 값이 있으면 queue에 삽입
                    queue.append(cur_root.left)
                if cur_root.right:                  # 현재 루투의 오른쪽 값이 있으면 queue에 삽입
                    queue.append(cur_root.right)
        
        return depth