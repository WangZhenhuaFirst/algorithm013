'''
https://leetcode-cn.com/problems/n-queens-ii/description/

52. N皇后II （亚马逊在半年内面试中考过）

思路：
参考：https://mp.weixin.qq.com/s/45mfS3ciiVt8nghUSjezFg

column = 10010000
pie    = 00100000
na     = 00101000








'''


def totalNQueens(self, n: int) -> int:
    def dfs(cols, xy_dif, xy_sum):
        p = len(cols)
        if p == n:
            self.count += 1
            return
        for q in range(n):
            if q not in cols and p - q not in xy_dif and p + q not in xy_sum:
                dfs(cols + [q], xy_dif + [p-q], xy_sum + [p + q])

    self.count = 0
    dfs([], [], [])
    return self.count


def totalNQueens(self, n: int) -> int:
    '''位运算'''
    def dfs(row, cols, xy_diff, xy_sum):
        if row == n:
            self.count += 1  # 解法加1
            return
        # cols | xy_diff | xy_sum，列、撇、捺 方向 所有已经被占的位置 标为1
        # 取反后 所有可用的位置标为 1,但cols、xy_diff、xy_sum 都是 32位，取反后 高位的 0 都变成了 1
        # 而我们只想保留 低8位，想把高位都置为0, ((1<<n) - 1) 表示先把1左移8位——> 100000000
        # 再减1，则变成了 011111111，再做与运算，即可保留低八位，去除高位
        bits = (~(cols | xy_diff | xy_sum)) & ((1 << n) - 1)  # 得到当前行 可放置皇后的格子

        while bits:  # bits中还包含1
            p = bits & -bits  # 取到最低位的1，即从当前行可用的格子中取出最右边 为1 的格子
            bits = bits & (bits - 1)  # 将当前行最右边的 1置为0，表示在P位置上放上皇后
            # (xy_diff | p) << 1 ，在这一行 | p，相当于加上这个放了皇后的列，但作用域下一行时，要把这个1左移一位
            # 左斜线往下一行的格子延展时，相当于左移一位
            dfs(row + 1, cols | p, (xy_diff | p) << 1, (xy_sum | p) >> 1)
    self.count = 0
    dfs(0, 0, 0, 0)
    return self.count
