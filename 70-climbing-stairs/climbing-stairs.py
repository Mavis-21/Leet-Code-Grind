class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
            
        first_step_count = 1
        second_step_count = 2
        current_total = 0
        
        for i in range(3, n + 1):
            current_total = first_step_count + second_step_count
            first_step_count = second_step_count
            second_step_count = current_total
            
        return second_step_count