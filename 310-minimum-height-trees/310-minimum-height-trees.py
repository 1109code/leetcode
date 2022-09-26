class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        # 양방향 그래프
        graph = collections.defaultdict(list)
        for i, j in edges:                              # 양방향이므로 딕셔너리로 양쪽에 추가
            graph[i].append(j)
            graph[j].append(i)
        
        # 첫 번쨰 리프 노드 추가
        leaves = []
        for i in range(n + 1):                          # 연결된 노드가 하나일 때 leaf
            if len(graph[i]) == 1:
                leaves.append(i)
        
        # 루트 노드만 남을 때 까지 반복 제거
        while n > 2:                                    # 마지막 남은게 1 혹은 2일때 이므로 2이상
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:                         # leaf 순회하며 양쪽 graph에서 제거
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:           # 다시 리프노드 찾아서
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves                         # leaves에 초기화
        
        return leaves