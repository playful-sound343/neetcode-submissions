from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts=Counter(nums)
        threshold=len(nums)//2

        for num,freq in counts.items():
            if freq>threshold:
                return num