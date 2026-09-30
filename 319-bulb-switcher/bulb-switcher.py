class Solution:
    def bulbSwitch(self, n: int) -> int:
        '''import math
        z=0
        for i in range(1,1+n):
            a=math.sqrt(i)
            if a==int(a):
                z=z+1
        return z'''
        import math
        return int(math.sqrt(n))

        