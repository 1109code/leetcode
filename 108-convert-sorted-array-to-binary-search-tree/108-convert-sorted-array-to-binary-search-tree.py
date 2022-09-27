# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:            # 예외 처리
            return None
        
        mid = len(nums) // 2
        
        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])                          # 해당 노드에 중앙값 입력
        node.left = self.sortedArrayToBST(nums[:mid])       # 왼쪽에 대해 재귀
        node.right = self.sortedArrayToBST(nums[mid + 1:])  # 오른쪽
        
        return node