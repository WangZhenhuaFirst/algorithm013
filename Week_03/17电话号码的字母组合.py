'''
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

思路：
1.暴力，嵌套循环
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/tong-su-yi-dong-dong-hua-yan-shi-17-dian-hua-hao-m/

当输入是字符串'23'时：
result = []
for i in 'abc':
    for j in 'def':
        tmp = i + j
        result.add(tmp)
return result

输入字符串长度是2，循环就是2层。但问题是输入字符串的长度是不固定的，怎么解决？递归



2.回溯，在循环里套用递归
代码参考：https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8339/Concise-python-solution


'''


class Solution:
    def letter_combinations_recursion(self, digits):
        if not digits:
            return []
        results = ['']
        map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for digit in digits:
            results = [
                result + letter for result in results for letter in map[digit]]
        return results
