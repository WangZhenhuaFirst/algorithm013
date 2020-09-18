## 位运算

参考：https://www.cnblogs.com/Neeo/articles/10536202.html

计算机中的数 在内存中都是以二进制形式存储的，用位运算就是直接对整数在内存中的二进制位 进行操作，
或者说是 把数字转换为 **机器语言**，也就是二进制 来进行计算的一种运算形式。
因此其执行效率非常高，在程序中尽量使用位运算进行操作，会大大提高程序的性能。


## 位图 bitmap

https://mp.weixin.qq.com/s/xxauNrJY9HlVNvLrL5j2hg

## 布隆过滤器
可以挡在数据库前面作为一个快速查询工具，如果查到某个元素不存在，那可以肯定不存在；如果查到其存在，
可以去MySQL中复查其到底是否存在。


## 排序
[十大经典排序算法](https://www.cnblogs.com/onepixel/p/7674659.html)


## 冒泡排序

```
from typing import List

def bubbleSort(nums: List[int]) -> None:
    n = len(nums)
    if n < 2:
        return 
    
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                falg = True
        if not falg:
            break

nums = [2, 3, 5, 7, 1, 9, 3]
bubbleSort(nums)
print(nums)
```


## 插入排序

```
from typing import List

def insertionSort(nums: List[int]) -> None:
    n = len(nums)
    if n < 2:
        return
    for i in range(1, n):
        value = nums[i]
        j = i - 1
        while j > -1:
            if nums[j] > value:
                nums[j+1] = nums[j]
            else:
                break
            j = j - 1
        nums[j+1] = value

nums = [2, 3, 5, 7, 1, 9, 3]
insertionSort(nums)
print(nums)
```


## 选择排序

```
from typing import List

def selectSort(nums: List[int]) -> None:
    n = len(nums)
    if n < 2:
        return

    for i in range(0, n-1):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

nums = [2, 3, 5, 7, 1, 9, 3]
selectSort(nums)
print(nums)
```






## 快速排序代码示例
https://shimo.im/docs/TX9bDbSC7C0CR5XO/read

```
def quick_sort(begin, end, nums):
    if beigin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index - 1, nums)
    quick_sort(pivot_index + 1, end, nums)

def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```



## 归并排序代码示例
https://shimo.im/docs/sDXxjjiKf3gLVVAU/read

```
def mergesort(nums, left, right):
    if left >= right:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    tmp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    while i <= mid:
        tmp.append(nums[i])
        i += 1
    while j <= right:
        tmp.append(nums[j])
        j += 1
    nums[left:right] = tmp
```


## 堆排序代码示例
https://shimo.im/docs/M2xfacKvwzAykhz6/read

