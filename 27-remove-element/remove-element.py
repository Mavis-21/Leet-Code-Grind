class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        idx_counter = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx_counter] = nums[i]
                idx_counter = idx_counter + 1
                
        return idx_counter