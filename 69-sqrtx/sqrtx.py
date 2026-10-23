class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        left_val = 1
        right_val = x // 2
        ans_val = 0
        
        while left_val <= right_val:
            mid_val = (left_val + right_val) // 2
            
            if mid_val * mid_val == x:
                return mid_val
            elif mid_val * mid_val < x:
                ans_val = mid_val
                left_val = mid_val + 1
            else:
                right_val = mid_val - 1
                
        return ans_val