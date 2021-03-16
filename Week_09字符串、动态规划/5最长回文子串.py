'''
https://leetcode-cn.com/problems/longest-palindromic-substring/

5. 最长回文子串（亚马逊、华为、字节跳动在半年内面试常考）

思路：
1.暴力解法：暴力解法时间复杂度高，但思路清晰、编写简单。
由于编写正确的可能性很大，可以使用暴力匹配算法 检验我们编写的其它算法是否正确。
优化的解法在很多时候，是基于“暴力解法”，以空间换时间得到的，
因此思考清楚暴力解法，分析其缺点，很多时候 能为我们打开思路

2.中间向两边扩张法

3.动态规划：
「回文」天然具有「状态转移」性质：一个回文去掉两头以后，剩下的部分 依然是回文
dp[i][j]表示子串 s[i..j] 是否为回文子串,这里子串 s[i..j] 定义为 左闭右闭区间，可以取到 s[i] 和 s[j]
dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]



'''


def longestPalindrome(self, s: str) -> str:
    '''
    暴力，O(N^3)
    '''
    size = len(s)
    if size < 2:
        return s
    if s == s[::-1]:
        return s
    max_len = 1
    res = s[0]

    # 验证子串 s[left, right] 是否为回文串
    def valid(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    # 枚举所有长度大于等于 2 的子串
    for i in range(size - 1):
        for j in range(i + 1, size):
            # > max_len ，只针对大于“当前得到的最长回文子串长度”的子串进行“回文验证”
            if j - i + 1 > max_len and valid(s, i, j):
                max_len = j - i + 1
                res = s[i:j + 1]
    return res


def longestPalindrome(self, s: str) -> str:
    '''
    动态规划:时间O(N^2),空间O(N^2)
    '''
    n = len(s)
    if n < 2:
        return s
    if s == s[::-1]:
        return s

    dp = [[0] * n for _ in range(n)]
    res = s[0]

    # 由于要构成字串，所以i <= j, 所以只需要填对角线以上的部分,且不包括对角线
    for j in range(1, n):
        for i in range(j):
            if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                # j - i < 3，即 j - i + 1 < 4
                # 即当字串长度为 2 或 3时，只需要判断头尾两个字符是否相等即可直接下结论了
                dp[i][j] = 1
                res = max(res, s[i:j+1], key=len)
    return res


def longestPalindrome(self, s: str) -> str:
    '''
    中心扩散法
    '''
    if len(s) < 2:
        return s
    if s == s[::-1]:
        return s

    self.res = s[0]

    def center_spread(s, left, right):
        # left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        # right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 注意，是right - left - 1 ，而不是 right - left + 1
        # 因为上面的while循环多执行了一次 left -= 1 和 right += 1
        if len(self.res) < right - left - 1:
            self.res = s[left+1:right]  # 这里也要注意是[left+1:right]

    for i in range(len(s)):  # 以任意一个位置为中心，向两侧扩散
        center_spread(s, i, i)
        center_spread(s, i, i+1)

    # 当前找到的最长回文子串
    return self.res
