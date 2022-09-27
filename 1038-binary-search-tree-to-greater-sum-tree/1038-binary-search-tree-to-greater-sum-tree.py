# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)       # 오른쪽 자식부터
            self.val += root.val            # val(class 변수)에 root의 val 추가하고
            root.val = self.val             # root에 val 초기화(오른쪽 자식만 크므로 오른쪽만 추가)
            self.bstToGst(root.left)        # 왼쪽 자식 재귀
        
        return root