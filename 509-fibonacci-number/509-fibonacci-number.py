# 타뷸레이션
class Solution(object):
    dp = collections.defaultdict(int)
    
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 초기 값 저장
        self.dp[1] = 1
        
        # 작은 값부터 직접 계산하면서 타뷸레이션
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]