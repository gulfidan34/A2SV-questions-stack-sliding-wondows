class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            tmp = [1,2]
            for i in range(2,n):
                tmp.append(tmp[i-1] + tmp[i-2])
            return tmp[-1]