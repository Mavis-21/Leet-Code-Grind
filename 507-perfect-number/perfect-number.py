'''class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        l=[]
        for i in range(1,num+1):
            if num%i==0:
                l.append(i)
        return sum(l)-num==num'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 1 is not a perfect number because it has no proper divisors
        if num <= 1:
            return False
            
        divisors_sum = 1 
        import math
        limit = int(math.sqrt(num))
        
        # Only check up to the square root
        for i in range(2, limit + 1):
            if num % i == 0:
                divisors_sum += i
                # Add the paired factor (and make sure we don't add the square root twice)
                if i != num // i:
                    divisors_sum += num // i
                    
        return divisors_sum == num       

