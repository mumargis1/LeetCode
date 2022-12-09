class Solution:
    def twoSum(self, num, target):

        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1


        # num_dict = dict()
        # for i in range(len(nums)):
        #     num = nums[i]
        #     complement = target - num
        #     if num in num_dict:
        #         return [num_dict[num], i]
        #     else:
        #         num_dict[complement] = i
# -------------------2nd Solution--------------#
        # for i in range(len(nums)):
        #     for j in range(len(nums)+1):
        #         num = nums[i] + nums[j]
        #         if num == target:
        #             return [i, j]

a = Solution()
print(a.twoSum([2,7,11,15], 13))