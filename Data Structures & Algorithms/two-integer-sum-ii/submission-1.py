from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Problem requires 1-indexed output
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1   # Need a larger value
            else:
                right -= 1  # Need a smaller value

        return []

       
        
        