class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프를 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            
        dfs('JFK')
        return route[::-1]