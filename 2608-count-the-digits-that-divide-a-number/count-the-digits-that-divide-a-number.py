class Solution:
    def countDigits(self, num: int) -> int:
        d=str(num)
        a=0
        for i in d:
            if num%int(i)==0:
                a+=1
        return a