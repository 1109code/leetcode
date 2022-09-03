class Solution(object):
    dp = collections.defaultdict(int)
    
    def fib(self, N):
        """
        :type n: int
        :rtype: int
        """
        # N이 1보다 작거나 같으면 그냥 반환
        if N <= 1:
            return N
        
        # 원하는 dp[N] 값이 있으면 반환
        if self.dp[N]:
            return self.dp[N]
        
        # 원하는 값이 없으면 재귀로 저장
        self.dp[N] = self.fib(N-1) + self.fib(N-2)
        return self.dp[N]