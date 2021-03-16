'''
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

25.K个一组翻转链表（字节跳动、猿辅导在半年内面试常考）

思路：类似题目为 24. 两两交换链表中的节点
1.栈：每次把k个数压入栈，然后弹出来的顺序就是翻转的。

2.转圈法：

k = 3 for example:

step 0: a -> b -> c -> (next k-group)

step 1:      b -> c -> (next k-group)
                  a ---^

step 2:           c -> (next k-group)
             b -> a ---^

step 3:                (next k-group)
        c -> b -> a ---^

finish: c -> b -> a -> (next k-group)



3.尾插法：依次把cur移到tail后面

k = 3
pre   head    tail
dummy  1   2   3   4   5 

4.递归：链表是一种 兼具递归和迭代性质 的数据结构。
此题有递归性质，也就是翻转整条链表和翻转2、3、4个节点 是同样的问题，只是数据规模不同而已
'''


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''栈'''
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            # 每走过k个节点，这个循环就会跳出一次
            # 到最后不足k个节点时，tmp会先为空，也就会跳出这个循环，此时会进入if count
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意，此时tmp在k+1位置，也就是tmp = None，并且剩下的节点也不用再翻转了
            # 所以这时候不该再用p.next = tmp,而是用p.next = head
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next  # 把P的指向向前挪动一位
            # 与剩下的链表连接起来
            p.next = tmp
            head = tmp
        return dummy.next

    def reverseKGroup(self, head, k):
        '''转圈法'''
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:  # l,r define reversing range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    # standard reversing,实际上是转了个圈，你在脑子里想一个圈就可以了
                    # pre, cur: used in reversing, standard reverse linked list method
                    cur.next, cur, pre = pre, cur.next, cur
                # jump: used to connect last node in previous k-group to first node in following k-group
                # jump = l 没看懂
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''尾插法'''
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = pre.next
        while pre.next != tail:
            cur = pre.next  # 获取下一个元素
            pre.next = cur.next  # pre 与 cur.next 连起来，把cur 孤立出来
            cur.next = tail.next  # 和剩余的连起来
            tail.next = cur  # 插在tail后面
        pre = head
        tail = head
    return dummy.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        '''递归,和转圈法类似'''
        cur = head
        count = 0
        # 递归到最后一层，会先出现cur=null，此时count != k，直接return head
        while cur and count < k:
            cur = cur.next
            count += 1
        if count == k:
            # 下一层递归返回给上一层的是 完成时应该作为 这一段的 头 的节点
            cur = self.reverseKGroup(cur, k)
            while count:
                # 是要循环k次的，和转圈法类似，每次 都把一个元素 连接到 下一个元素上
                head.next, head, cur = cur, head.next, head
                count -= 1
            head = cur
        return head
