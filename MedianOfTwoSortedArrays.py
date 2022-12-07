class Solution:
    def findMedianofSortedArrays(self, num1, num2):
        nums = num1 + num2
        nums = sorted(nums)

        mid = len(nums)//2
        if len(mid) % 2 !=0:
            return nums[mid]
        else:
            mid = nums[mid-1] + nums[mid]
            return mid/2.0