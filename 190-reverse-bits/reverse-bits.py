class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_result = 0
        bit_counter = 32
        
        while bit_counter > 0:
            reversed_result = (reversed_result << 1) | (n & 1)
            n = n >> 1
            bit_counter = bit_counter - 1
            
        return reversed_result
        