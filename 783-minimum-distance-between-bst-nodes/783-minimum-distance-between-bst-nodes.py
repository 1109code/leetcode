# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = - sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        
        # 반복 구조 중위 순회 비교 결과
        while stack or node:                        # 스택 or 노드 만 있어도 반복되게
            while node:                             # 오른쪽 노드가 없었으면 그냥 통과
                stack.append(node)
                node = node.left                    # 왼쪽먼저 계속 stack에 쌓기
                
            node = stack.pop()                      # 가장 마지막 왼쪽 node 부터
            
            result = min(result, node.val - prev)   # 비교
            prev = node.val                         # 현재 노드가 prev가 되고
            
            node = node.right                       # right 탐색 위해 node에 입력
                                                    # 다음에 pop 되는건 부모의 부모
        return result