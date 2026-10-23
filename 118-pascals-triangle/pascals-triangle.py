class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle_result = []
        
        for row_idx in range(numRows):
            current_row = [None] * (row_idx + 1)
            current_row[0] = 1
            current_row[row_idx] = 1
            
            for col_idx in range(1, row_idx):
                prev_row = triangle_result[row_idx - 1]
                current_row[col_idx] = prev_row[col_idx - 1] + prev_row[col_idx]
                
            triangle_result.append(current_row)
            
        return triangle_result