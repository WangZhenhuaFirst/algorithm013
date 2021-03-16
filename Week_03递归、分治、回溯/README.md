## 递归
递归和循环没有明显的边界，递归是通过函数体来进行的循环。
递归三要素：
- 确定递归函数的参数和返回值
- 确定终止条件
- 确定单层递归的逻辑


## 递归的代码我没理解透的一个原因是，比如最后一层的return，如果返回值，是否需要逐层返回？？？ 



### 递归代码模板

参考：https://shimo.im/docs/EICAr9lRPUIPHxsH/read


```
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed
```

### 递归思维要点
- 不要人肉递归，这是最大的误区：
- 找到最近最简单方法，将其拆解成 可重复的子问题：如果这个问题是可以通过编程、算法解决的，那肯定有重复子问题
- 数学归纳法思维：如果看完题目懵逼了，就先考虑n=1这种最简单的情况



## 分治和回溯

### 分治
核心思想——分而治之，也就是将原问题分解成 n个 规模较小，且结构与原问题相似的子问题，递归地解决这些子问题，
再合并其结果。

### 分治代码模板

https://shimo.im/docs/zvlDqLLMFvcAF79A/read

```
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
    
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)

    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level status
```

## 回溯
回溯的处理思想，有点类似枚举搜索，枚举所有的解，从而找到满足期望的解。
为了有规律地枚举 所有可能的解，避免遗漏和重复，我们把问题求解的过程分为多个阶段。每个阶段，先随意
选一条路走，发现不符合期望的解时，就回退到上一个岔路口，另选一种走法。
回溯算法多用于“搜索”类问题上，这里的搜索不是狭义上图的搜索，而是 在一组可能的解中，搜索满足期望的解。


### 回溯模板

https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/

回溯算法框架：解决一个回溯问题，实际上就是一个决策树的遍历过程，回溯算法就是个多叉树的遍历问题。
只需要考虑3个问题：
1.路径：即已经做出的选择
2.选择列表：你当前可以做的选择
3.结束条件：到达决策树底层，无法再做选择的条件


```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        #做选择
        选择列表.remove(该选择)
        路径.add(该选择)
        
        backtrack(路径, 选择列表)
        
        # 撤销选择
        路径.remove(该选择)
        选择列表.add(该选择)
```
核心是for循环里的递归，在递归调用之前 做选择，在递归调用之后 撤销选择


### 回溯的时间复杂度
回溯算法就是纯暴力穷举，复杂度一般都很高，且难以优化。



分治和回溯本质上就是递归的一个细分类，
碰到任何一个问题，都找它的重复性/递归：
- 最近重复性——分治、回溯
- 最优重复性————动态规划
