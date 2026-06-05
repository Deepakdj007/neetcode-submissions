class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0;
        left = 0
        right = len(heights)-1

        while(left<right):
            max_area = max(max_area,(right-left) * min(heights[left],heights[right]))
            
            if heights[left]<heights[right]:
                left+=1
                while left<right and heights[left]<=heights[left-1]:
                    left+=1
            else:
                right-=1
                while left<right and heights[right]<=heights[right+1]:
                    right-=1
        return max_area