class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total_result = 0
        
        for char in columnTitle:
            char_value = ord(char) - ord('A') + 1
            total_result = total_result * 26 + char_value
            
        return total_result
        