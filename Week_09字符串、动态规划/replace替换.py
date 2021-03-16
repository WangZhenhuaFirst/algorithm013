'''
实现一个字符串替换的类。
    有一个多行词表，格式：string1  string2
输入：一个字符串。
输出：把输入字符串中包含string1的部分用string2替换。

注意：想想有哪些特殊情况。

例子：
词表： 
    上海  shanghai
    北京  beijing

输入字符串：
    我是北京人，现在在上海。

输出字符串：
    我是beijing人，现在在shanghai。
'''

dic = {'上海': 'shanghai', '北京': 'beijing'}


class Replace:
    def replace_str(self, input):
        if not input:
            return input

        for key, value in dic.items():
            input = input.replace(key, value)

        return input


if __name__ == "__main__":
    r = Replace()
    input = '我是北京人，现在在上海。'
    res = r.replace_str(input)
    print(res)
