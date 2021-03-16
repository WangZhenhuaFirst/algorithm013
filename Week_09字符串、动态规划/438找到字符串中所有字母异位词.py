'''
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

438. 找到字符串中所有字母异位词（Facebook 在半年内面试中常考）

思路：













'''


def findAnagrams(self, s: str, p: str) -> List[int]:
    '''排序（超时）暴力方法，每次选取和 p等长的字符串比较'''
    n = len(p)
    p = ''.join(sorted(p))
    res = []
    for i in range(len(s) - n + 1):
        if ''.join(sorted(s[i:i+n])) == p:
            res.append(i)
    return res


def findAnagrams(self, s: str, p: str) -> List[int]:
    '''滑动窗口'''
    res = []
    window = {}  # 记录窗口中各个字符数量的字典
    need = {}  # 记录目标字符串中各个字符数量的字典
    for c in p:  # 统计目标字符串的信息
        need[c] = need.get(c, 0) + 1

    length = len(p)
    limit = len(s)
    left = right = 0  # 定义两个指针，分别表示窗口的左、右界限

    while right < limit:
        c = s[right]
        if c not in need:  # 当遇到没有的字符时
            window.clear()  # 将之前统计的信息全部放弃
            # 注意是left = right，也就是让left和right重新放到同一位置
            # 而不是 left += 1, right += 1
            left = right = right + 1  # 从下一位置开始重新统计
        else:
            window[c] = window.get(c, 0) + 1  # 统计窗口内各种字符出现的次数
            if right - left + 1 == length:  # 当窗口大小与目标字符串长度一致时
                if window == need:  # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    res.append(left)
                window[s[left]] -= 1  # 并将要移除的字符数量减一
                left += 1  # left右移，只要window长度达到了，left必定右移
            right += 1  # right右移，不论window的长度是否达到，right都必然要右移
    return res
