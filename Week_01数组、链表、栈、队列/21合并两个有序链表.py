'''
https://leetcode-cn.com/problems/merge-two-sorted-lists/

21. 合并两个有序链表（亚马逊、字节跳动在半年内面试常考）

思路：递归













'''


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    '''O(m+n), m、n为l1和l2的元素个数'''
    # 终止条件：l1为空 或 l2为空
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1  # 每层都返回 排序好的链表头
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
