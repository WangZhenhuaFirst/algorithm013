'''
https://leetcode-cn.com/problems/reverse-string-ii/

541. 反转字符串II （亚马逊在半年内面试中考过）

思路:













'''


def reverseStr(self, s: str, k: int) -> str:
    if not s:
        return s
    n = len(s)
    s = list(s)
    # 每隔 2k 个，翻译成代码就是 这一行
    for global_ptr in range(0, n, 2 * k):  # global_ptr每次走 2*k 步
        left = global_ptr
        # 如果剩余的字符数 大于 k个，那left + k - 1 是不会越过字符串结尾的
        # 如果剩余的字符数小于 k个，那right只能取 n - 1 了
        # 如果剩余字符小于K个，则将剩余字符全部反转
        # 也就是把剩余的字符串做完全的反转，这就是 min(j, len(s) - 1)的意义
        right = min(left + k - 1, n - 1)
        while left < right:
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1
    return ''.join(s)
