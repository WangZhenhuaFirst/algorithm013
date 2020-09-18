'''
https://leetcode-cn.com/problems/relative-sort-array/

1122. 数组的相对排序 （谷歌在半年内面试中考过）

思路：计数排序，唯一不同的是排序时要按照arr2的顺序排












'''


def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    '''
    时间复杂度O(N+M)，N为 arr1的长度,M为arr2的长度
    空间复杂度O(N)，N为 arr1 的长度
    '''
    # 题目说arr1的范围在0-1000，所以生成一个1001大小的数组用来存放每个数出现的次数
    arr = [0] * 1001
    ans = []
    # 遍历arr1，把整个arr1的数的出现次数储存在arr上，arr的下标对应arr1的值，arr的值对应arr1中的值出现的次数
    for i in range(len(arr1)):
        arr[arr1[i]] += 1
    for i in range(len(arr2)):
        # 如果arr2的值在arr所对应的下标位置出现次数大于0，那么就说明arr中的这个位置存在值
        while arr[arr2[i]] > 0:
            ans.append(arr2[i])
            arr[arr2[i]] -= 1
    for i in range(len(arr)):
        while arr[i] > 0:
            # 注意，在数组arr中，i才是arr1中的值
            ans.append(i)
            arr[i] -= 1
    return ans
