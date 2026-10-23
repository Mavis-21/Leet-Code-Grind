class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        idx_one = m - 1
        idx_two = n - 1
        tail_idx = m + n - 1
        
        while idx_one >= 0 and idx_two >= 0:
            if nums1[idx_one] > nums2[idx_two]:
                nums1[tail_idx] = nums1[idx_one]
                idx_one = idx_one - 1
            else:
                nums1[tail_idx] = nums2[idx_two]
                idx_two = idx_two - 1
            tail_idx = tail_idx - 1
            
        while idx_two >= 0:
            nums1[tail_idx] = nums2[idx_two]
            idx_two = idx_two - 1
            tail_idx = tail_idx - 1
        