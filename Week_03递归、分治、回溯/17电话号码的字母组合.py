'''
https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

17. 电话号码的字母组合（亚马逊在半年内面试常考）

思路：













'''


class Solution:
    def letterCombinations(self, digits):
        '''
        暴力嵌套循环,实际上利用了队列，类似于BFS，
        只是编码的方式是一直在修改results中的元素，
        而不是将原来的元素出队列后，修改完，再入队。
        类似于78题的迭代解法
        '''
        if not digits:
            return []
        results = ['']
        digit_hash = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for digit in digits:
            # 两个for循环没有先后顺序
            results = [
                result + letter for result in results for letter in digit_hash[digit]]
        return results

    def letterCombinations(self, digits):
        if not digits:
            return []
        results = ['']
        tmp = []
        digit_hash = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        for digit in digits:
            # 不pythonic的写法
            for result in results:
                for letter in digit_hash[digit]:
                    tmp.append(result + letter)
            results = tmp
            tmp = []
        return results

    def letterCombinations(self, digits):
        '''
        当题目中出现 “所有组合” 等类似字眼时，就要想到用回溯
        回溯，在循环里 套用递归
        输入字符串长度是2，循环就是2层。但问题是输入字符串的长度是不固定的，怎么解决？递归
        每次调用下一层递归时，都需要将本层的一些处理结果 放到一个临时变量中，再传递到下一层
        '''
        if not digits:
            return []
        digit_hash = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        results = []

        def dfs(index, tmp):
            # 递归终止条件
            if index == len(digits):
                results.append(tmp)
                return

            letters = digit_hash[digits[index]]
            for letter in letters:  # 在循环中使用递归
                dfs(index+1, tmp+letter)
        dfs(0, '')
        return results
