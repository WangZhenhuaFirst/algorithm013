'''
3. 无重复字符的最长子串

https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

思路：滑动窗口,O(N)
其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，
队列变成了 abca，这时候不满足要求。只要把队列左边的元素移出就行了，直到满足题目要求！











'''


def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
        return 0
    left = 0
    window = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1  # 因为每个字符都要加进window中的，所以cur_len肯定要加1

        # 这里是while，所以不管新出现的 字符 与之前window中哪个字符重复，都会一直移出，
        # 直到window中没有这个重复字符位置
        while s[i] in window:
            window.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len:
            max_len = cur_len
        window.add(s[i])
    return max_len
