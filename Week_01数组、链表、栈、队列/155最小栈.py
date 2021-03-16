'''
https://leetcode-cn.com/problems/min-stack/

155. 最小栈（亚马逊在半年内面试常考）

思路：除了栈应该拥有的入栈、出栈、查看栈顶元素的功能，还需要增加一个特殊功能————得到当前栈里最小的元素。
题目要求在常数时间内 获得栈中的最小值，因此不能在 getMin() 时再去计算最小值，而应该在push或pop
时就已经计算好了当前栈中的最小值。

用两个栈，一个存正常的入栈、出栈值，另一个栈存最小值。
1.辅助栈和数据栈同步：编码简单，不用考虑一些边界情况。但辅助栈可能会存一些不必要的元素
时间复杂度O(1):出栈、入栈、查看栈顶元素 的操作不论数据规模多大，都只是有限个步骤
空间复杂度O(N):

2.辅助栈和数据栈不同步：
辅助栈为空时，新来的数肯定要放进来；
辅助栈不为空时，新来的数<=辅助栈栈顶元素，才放入。注意，“等于”要考虑进去，因为出栈时，连续的、
相等的且是最小值的元素要同步出栈
出栈时，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈

同步更好一些，因为简单；不同步虽然减少了一些空间浪费，但出栈、入栈时还要做判断，也有性能消耗。


3.用一个栈实现,每次新元素入栈时保存一个元组（当前值x,插入该值后的栈内最小值)

只用一个变量去保存最小值
要解决的关键问题就是，当有新的更小值时，之前的最小值怎么办？

4.有更小的值来的时候，只需要把之前的最小值入栈，当前的更小值再入栈即可。
当这个最小值要出栈时，下一个值便是之前的最小值了。

5.栈里不再保存原来的值，而是存 入栈的值和最小值的差。
想得到之前的最小值，可以用 min 和栈顶元素得到。
'''


class MinStack:
    # 1.两个栈，同步
    def __init__(self):
        self.data = []  # 数据栈
        self.helper = []  # 辅助栈

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        self.helper.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]

    # 2.两个栈，不同步
    def __init__(self):
        self.data = []  # 数据栈
        self.helper = []  # 辅助栈

    def push(self, x):
        self.data.append(x)
        # 关键 1：辅助栈的元素空的时候，必须放入新进来的数
        # 关键 2：新来的数小于或等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        # 不论怎么样，数据栈都要 pop 出元素。题目中说pop只在非空时才会调用，所以这里不用判断是否为空
        top = self.data.pop()
        # 关键 3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即"出栈保持同步"就可以了
        # 因为辅助栈加入元素时只加入了一部分，所以只需要出这一部分，别的也没有啊
        if self.helper and top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.helper[-1]

    # 3.用一个栈实现,每次新元素入栈时保存一个元组（当前值x,插入该值后的栈内最小值)
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            # 比较当前新插入元素x和当前栈内最小值
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

    # 4.只用一个变量保存最小值
    def __init__(self):
        self.stack = []
        self.min_value = float('inf')

    def push(self, x):
        if x <= self.min_value:
            self.stack.append(self.min_value)  # 保存之前的最小值
            self.min_value = x  # 更新最小值
        self.stack.append(x)

    def pop(self):
        # 如果弹出的值是最小值，那么将下一个元素更新为最小值
        # 把push 和 pop 联系起来看：
        # push时，如果出现了更小的值，就把原来的最小值压入栈
        # pop时，如果pop的是现在的最小值，那就把栈中下一个值更新为新的最小值
        top = self.stack.pop()
        if top == self.min_value:
            self.min_value = self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_value

    # 5.保存差 ？？？
    def __init__(self):
        self.stack = []
        self.min_value = -1

    def push(self, x: int) -> None:
        # 栈里保存 入栈的值 - 当前最小值
        if not self.stack:
            self.stack.append(0)
            self.min_value = x
        else:
            self.stack.append(x - self.min_value)
            if x < self.min_value:
                self.min_value = x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value - diff
                self.min_value = top
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value
