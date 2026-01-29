class Solution:
    def trap(self, height: List[int]) -> int:
        #[0,1,0,2,1,0,1,3,2,1,2,1]
        water = 0
        left = 0
        right = len(height)-1
        maxLeft, maxRight = height[left],height[right]

        while left<right:
            if height[left]<height[right]:
                left+=1
                maxLeft = max(height[left],maxLeft)
                water += maxLeft-height[left]

            else:
                right-=1
                maxRight = max(height[right],maxRight)
                water += maxRight-height[right]

        return water
            