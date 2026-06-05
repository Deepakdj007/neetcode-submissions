class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0;
        left = 0
        right = len(heights)-1

        while(left<right):
            newMax = (right-left) * min(heights[left],heights[right])
            if newMax>maxAr:
                maxAr = newMax
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxAr