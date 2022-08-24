class Solution(object):
    def fib(self, n):
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y
        return x