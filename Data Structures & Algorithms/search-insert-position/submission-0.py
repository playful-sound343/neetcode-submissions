class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        m=len(nums)-1

        while l<=m:
            mid=(l+m)//2

            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l=mid+1
            if nums[mid]>target:
                m=mid-1

        return l