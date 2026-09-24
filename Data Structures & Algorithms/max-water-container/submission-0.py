class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        # given 2 bars, we can find the area inside with:
        # height = min(bar1, bar2)
        # width = j - i
        # area = height * width

        l, r = 0, len(heights) -1
        while l < r:
            bar1, bar2 = heights[l], heights[r]
            area = min(bar1, bar2) * (r - l) # height * width

            result = max(result, area)
            if bar1 < bar2:
                l += 1
            else:
                r -= 1

        return result


        # options:
            # sort but keep the index attached to each value somehow? seems memory itensive
            # two pointers - but when to increment?
        