class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_water=0
        width=0
        current_water=0
        

        while left<right:
            h=min(heights[left],heights[right])
            width=right-left

            current_water=h*width
            max_water=max(max_water,current_water)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1

        return max_water

        