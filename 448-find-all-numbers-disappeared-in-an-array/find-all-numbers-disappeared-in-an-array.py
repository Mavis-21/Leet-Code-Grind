class Solution:

  def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    # Mark the presence of each number by negating the value at the corresponding index
    for n in nums:
      index = abs(n) - 1
      if nums[index] > 0:
        nums[index] = -nums[index]

    # Any index that remains positive indicates that its corresponding number is missing
    result = []
    for i in range(len(nums)):
      if nums[i] > 0:
        result.append(i + 1)

    return result
        