from util.common_imports import *
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1  # 偏小，增加数值
            else:
                j -= 1  # 偏大，减小数值


print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
