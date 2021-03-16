'''
输入一个10进制数字，输出这个数8进制表示

例子：
输入： 10
输出： 12

测试输入：1000000

参考：https://juejin.cn/post/6844903930200064014
'''


def dec_to_oct(num):
    res = []
    while True:
        num, reminder = divmod(num, 8)
        res.append(str(reminder))
        if num == 0:
            return int(''.join(res[::-1]))


if __name__ == "__main__":
    num = 1000000
    res = dec_to_oct(num)
    print(res)
