class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        current_val = n
        
        while current_val > 0:
            if current_val % 2 == 1:
                bit_count = bit_count + 1
            current_val = current_val // 2
            
        return bit_count
        
        