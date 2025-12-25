# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
from util.common_imports import *

# 解答一：首先明确，我们二分的是 元素值。它的初始范围是 [matrix[0][0],matrix[n−1][n−1]]，它一定包含目标答案 ans。二分不断进行，但是我们始终确保 [left,right] 一定包含 目标值。从二分的角度看，小于等于 left 的个数 <k 个，而小于等于 right 的个数 ≥k 个。那么，等到最后区间长度缩小至 1 时，剩下的那个数就正好是 k 个。

# 同时，如果最终的 x 不是矩阵的数，假设 x>ans，表明区间长度大于 1，那就可以继续缩小区间。直到最后长度为 1 时，它就“恰好”(只能)是矩阵中的数。


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = matrix[0][0]  # 第0个，最小的值
        r = matrix[n - 1][n - 1]  # 最大的值，right

        while l < r:
            mid = (r + l) // 2
            num = 0  # number of elements <= mid
            j = 0  # index of column
            for i in range(n - 1, -1, -1):  # index of row
                while j < n:
                    if matrix[i][j] > mid:
                        break
                    j += 1  # 从第1大的数开始，往后到第2大，第3大
                num += j

            if num >= k:
                r = mid
            else:
                l = mid + 1
        return l


print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=5))
