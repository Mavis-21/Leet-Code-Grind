class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res_list = []
        carry_value = 0
        
        pointer_a = len(a) - 1
        pointer_b = len(b) - 1
        
        while pointer_a >= 0 or pointer_b >= 0 or carry_value > 0:
            current_sum = carry_value
            
            if pointer_a >= 0:
                current_sum = current_sum + int(a[pointer_a])
                pointer_a = pointer_a - 1
                
            if pointer_b >= 0:
                current_sum = current_sum + int(b[pointer_b])
                pointer_b = pointer_b - 1
                
            remainder = current_sum % 2
            res_list.append(str(remainder))
            
            carry_value = current_sum // 2
            
        res_list.reverse()
        final_answer = "".join(res_list)
        return final_answer
        