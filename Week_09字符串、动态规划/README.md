## 63. 不同路径II 的状态转移方程

dp[i,j]=dp[i−1,j]+dp[i,j−1]


## 动态规划

@liweiwei1419
动态规划我看一些高手的总结，他们说没有套路。但我个人觉得思想其实是很简单的：
1、从一个最小的子问题开始，以后遇到的问题 都可以从之前的子问题中得出答案；
动态规划不是直接针对问题求解，而是希望我们从一个最小的子问题出发，这一点大概是“动态”的意思。我们学习算法好不容易熟悉了递归，熟悉了自顶向下，现在又让我们自底向上。真的是够了。
2、由于要记录子问题的答案，这就是最最常见而且朴素的“以空间换时间”的思想，也是“规划”这个词英文的本意：“打表格”法。

加缓存思路在《算法导论》中也被称之为“动态规划”，这本书上叫“带备忘录的递归”，有些资料叫记忆化递归，是一个意思。
我其实就是把“动态规划”这四个字拆开来解释了一下，我很认同《算法导论》中把“规划”programming”这个词解释为“表格”，所以我更愿意叫“动态规划”为“打表格”法，它的基本思想就是“空间换时间”。“动态规划”难理解可能本身也有翻译问题，这个翻译有点让人捉摸不透。

我个人更愿意把自底向上递推的这种写法称之为“动态规划”，就我看到的“动态规划”问题基本都可以这么做，这种思路在空间使用上更有规律，使得压缩空间解决更大规模的问题成为了可能。

动态规划的基本问题和经典问题掌握好我觉得就行了，主要在体会思想，并且运用


### 思考状态转移方程

常见的推导技巧是：分类讨论。即：对状态空间进行分类


### 思考初始化

初始化是非常重要的，一步错，步步错。初始化状态一定要设置对，才可能得到正确的结果。
角度 1：直接从状态的语义出发；
角度 2：如果状态的语义不好思考，就考虑「状态转移方程」的边界需要什么样的初始化条件；
角度 3：从「状态转移方程」的下标看是否需要多设置一行、一列表示「哨兵」（sentinel），
这样可以避免一些特殊情况的讨论。


## 字符串匹配暴力法代码示例
https://shimo.im/docs/8G0aJqNL86wWrPUE/read

```
def forceSearch(txt, pat):
    n, m = len(txt), len(pat)
    for i in range(n-m+1):
        for j in range(m):
            if txt[i+j] != pat[j]:
                break
        if j == m:
            return i
    return -1
```


## Rabin-Karp 代码示例
https://shimo.im/docs/1wnsM7eaZ6Ab9j9M/read

```
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = 256
        q = 9997
        n = len(haystack)
        m = len(needle)
        h = pow(d, m-1)%q
        p = 0
        t = 0

        if m > n:
            return -1
        
        for i in range(m):
            p = (d*p + ord(needle[i]))%q
            t = (d*t + ord(haystack[i]))%q
        for s in range(n-m+1): # note the +1
            if p == t: # check character by character
                match = True
                for i in range(m):
                    if needle[i] != haystack[s+i]:
                        match = False
                        break
                if match:
                    return s
            if s < n-m:
                t = (t-h*ord(haystack[s]))%q
                t = (t*d+ord(haystack[s+m]))%q
                t = (t+q)%q
        return -1


```


## Boyer-Moore 算法

https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html


## Sunday 算法

https://blog.csdn.net/u012505432/article/details/52210975


