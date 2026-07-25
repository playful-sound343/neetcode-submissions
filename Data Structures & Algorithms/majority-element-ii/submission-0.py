from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # --- PASS 1: Find potential candidates ---
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                # 3-way showdown: eliminate 1 vote from each candidate
                count1 -= 1
                count2 -= 1

        # --- PASS 2: Audit / Recount ---
        result = []
        threshold = len(nums) // 3

        for cand in (candidate1, candidate2):
            if (
                cand is not None
                and cand not in result
                and nums.count(cand) > threshold
            ):
                result.append(cand)

        return result
    

        
        