'''
https://leetcode-cn.com/problems/linked-list-cycle/

141. 环形链表（阿里巴巴、字节跳动、腾讯在半年内面试常考）

思路：
1.暴力：遍历链表，用set记录下所有节点，看有没有重复的节点出现。
需要用额外的内存，所以空间复杂度不是O(1)

2.快慢指针：如果有环，快指针迟早会追上慢指针。
时间复杂度O(N)，空间复杂度O(1)








'''


from llist import sllist


def has_cycle_bad(head):
    '''暴力'''
    s = set()
    while head:
        if head in s:
            return True
        s.add(head)
        head = head.next
    return False


def has_cycle_good(head):
    i, j = head, head
    # 防止访问 null.next:
    # 如果没环，j指针会先走到头，就不用判断i是否为空；
    # 如果有环，那永远走不到头，也就不必担心为空的问题了
    while j and j.next:
        i = i.next
        j = j.next.next
        if i == j:
            return True
    return False


if __name__ == "__main__":
    lst = sllist([3, 2, 0, -4])
    head = lst.first
    res = has_cycle_good(head)
    print(res)
