'''
https://leetcode-cn.com/problems/rotate-array/

189. 旋转数组（微软、亚马逊、PayPal 在半年内面试中考过）

思路：













'''


def rotate(self, nums: List[int], k: int) -> None:
    '''暴力，O(N*K), 旋转K次，每次旋转1个元素'''
    n = len(nums)
    for i in range(k):
        previous = nums[n - 1]  # previous是个变量，用来存旋转时被占据的位置的原来的元素
        for j in range(n):
            nums[j], previous = previous, nums[j]


def rotate(self, nums: List[int], k: int) -> None:
    '''插入'''
    n = len(nums)
    k %= n
    for _ in range(k):
        nums.insert(0, nums.pop())


def rotate(self, nums: List[int], k: int) -> None:
    '''拼接,利用了Python的切片实现'''
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]


def rotate(self, nums: List[int], k: int) -> None:
    '''三次翻转，前k翻转，后k翻转，整体翻转'''
    n = len(nums)
    k = k % n

    def swap(l, r):
        while(l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    swap(0, n-k-1)
    swap(n-k, n-1)
    swap(0, n-1)


def rotate(self, nums: List[int], k: int) -> None:
    '''
    模拟过程/环状替代
    把元素看做同学，把下标看做座位，大家换座位。第一个同学离开座位去第k+1个座位，
    第k+1个座位的同学被挤出去了，他就去坐他后k个座位，如此反复。但是会出现一种情况，
    就是其中一个同学被挤开之后，坐到了第一个同学的位置（空位置，没人被挤出来），
    但是此时还有人没有调换位置，这样就顺着让第二个同学换位置。 
    那么什么时候就可以保证每个同学都换完了呢？n个同学，换n次，所以用一个count来计数即可。
    '''
    n = len(nums)
    k %= n
    if k == 0:
        return
    start = 0
    tmp = nums[start]
    count = 0
    while count < n:  # 总共要交互n次
        nxt = (start + k) % n
        while nxt != start:
            nums[nxt], tmp = tmp, nums[nxt]
            count += 1
            nxt = (nxt + k) % n
        nums[nxt] = tmp
        count += 1

        start += 1
        tmp = nums[start]
