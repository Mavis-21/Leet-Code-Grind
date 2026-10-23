class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        
        while left_pointer <= right_pointer:
            mid_index = (left_pointer + right_pointer) // 2
            
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                left_pointer = mid_index + 1
            else:
                right_pointer = mid_index - 1
                
        return left_pointer