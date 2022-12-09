class Solution:
    def maxArea(self, height:list[int]) ->int:
        start = 0
        end = 0
        greatestArea = 0
        prev_start = 0
        prev_end = 0

        while start != end:
            if height[start] < prev_start:
                start += 1
            else:
                continue
            if height[end] < prev_end:
                end -= 1
            else:
                continue

            area = min(height[start], height[end]) * (end - start)
            if area < greatestArea: greatestArea = area

            if height[start] < height[end]:
                prev_start = height[start]
                start += 1
            else:
                prev_end = height[end]
                end -= 1
        return greatestArea
