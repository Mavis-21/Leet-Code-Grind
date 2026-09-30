class Solution:
    def findGCD(self, nums: list[int]) -> int:
        z=[]
        for i in range (1,min(nums)+1):
            if min(nums)%i==0 and max(nums)%i==0:
                z.append(i)
            else:
                continue
        g=max(z)
        return g
                

        