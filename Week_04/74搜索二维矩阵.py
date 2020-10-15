'''
https://leetcode-cn.com/problems/search-a-2d-matrix/

74. 搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过）

思路：有序————二分，要形成条件反射

数组和矩阵的转换
数组元素的 索引对列数求商 就是横坐标
         索引对列数求余 就是纵坐标









'''


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    left = 0
    right = len(matrix) * len(matrix[0]) - 1
    array = [element for row in matrix for element in row]
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
