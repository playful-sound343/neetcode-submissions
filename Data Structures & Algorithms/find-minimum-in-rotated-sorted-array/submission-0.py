class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        while left<right:
            mid=(left+right)//2

            if nums[left]<nums[mid]:
                left=mid+1
            if nums[right]>nums[mid]:
                right=mid

        return nums[left]