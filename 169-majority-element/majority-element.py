class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate_val = None
        vote_counter = 0
        
        for current_num in nums:
            if vote_counter == 0:
                candidate_val = current_num
                
            if current_num == candidate_val:
                vote_counter = vote_counter + 1
            else:
                vote_counter = vote_counter - 1
                
        return candidate_val