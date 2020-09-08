'''
https://leetcode-cn.com/problems/task-scheduler/

621. 任务调度器

思路：完成所有任务的最短时间取决于出现次数最多的任务数量

tasks = ["A","A","A","B","B","B"], n = 2
先把出现次数最多的任务A安排上
A->()->()->A->()->()->A
尽可能把中间间隔的冷却时间 安排上其他任务
A->B ->()->A->B ->()->A->B

(A的次数 - 1) * (n+1) + 出现次数为3的任务个数

所以解题步骤如下：
计算每个任务出现的次数
找出出现次数最多的任务，假设为x次
计算至少需要的时间(x - 1) * (n + 1),记为 min_time
计算出现次数为 x 的任务总数count,最终结果为min_time + count

特殊情况：
tasks = ["A","A","A","B","B","B","C","C","D","D"], n = 2
A -> B -> C -> A -> B -> D -> A -> B -> C -> D
此时如果按照上述方法计算将得到结果为8，比数组总长度10要小，应返回数组长度。


'''


def leastInterval(self, tasks: List[str], n: int) -> int:
    length = len(tasks)
    if length <= 1:
        return length

    task_map = dict()
    for task in tasks:
        task_map[task] = task_map.get(task, 0) + 1
    task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

    max_task_count = task_sort[0][1]
    res = (max_task_count - 1) * (n + 1)

    for sort in task_sort:
        if sort[1] == max_task_count:
            res += 1
    # 如果还存在冷却时间，肯定是res 大
    # 如果不存在冷却时间，也就是每个任务之间都不存在空余，那执行所有任务需要的时间，就是任务的数量
    return max(res, length)
