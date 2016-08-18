# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers_1(self, l1, l2):
        """
        先将原来的 ListNode 的最高位添加了一个0方便指针判断(这里的尾节点总是指向一个 None 导致按照初始链表不好判断最后一位)
        然后两个指针一移动做加法运算,如果有指针到头了就只移动另一个.两个都到头了之后判断最高位是否要进1
        效率:24%
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = l1
        while i.next is not None:
            i = i.next
        i.next = ListNode(0)
        j = l2
        while j.next is not None:
            j = j.next
        j.next = ListNode(0)
        i, j = l1, l2
        ans = ListNode(None)
        cur = ans
        enough_ten = ListNode(False)
        while i.next or j.next:
            if i.next is None:
                cur.next = ListNode(j.val+1) if enough_ten.val is True else ListNode(j.val)
                j = j.next
            elif j.next is None:
                cur.next = ListNode(i.val+1) if enough_ten.val is True else ListNode(i.val)
                i = i.next
            else:
                cur.next = ListNode(i.val+j.val+1) if enough_ten.val is True else ListNode(i.val+j.val)
                i, j = i.next, j.next
            if cur.next.val > 9:
                cur.next.val -= 10
                enough_ten.next = ListNode(True)
            else:
                enough_ten.next = ListNode(False)
            enough_ten = enough_ten.next
            cur = cur.next
        if enough_ten.val is True:
            cur.next = ListNode(1)
        return ans.next


if __name__ == '__main__':

    def addNode(ln, node):
        # 添加节点
        ln.next = ListNode(node)


    def digit2ln(dg):
        # 将数字( list) 转换成 LsitNode
        ln = ListNode(dg[0])
        cur = ln
        for l in range(1, len(dg)):
            addNode(cur, dg[l])
            cur = cur.next
        return ln


    def showListNode(ln):
        # 打印 ListNode
        while ln.next is not None:
            print(str(ln.val) + ' ->', end=' ')
            ln = ln.next
        print(ln.val)


    slt = Solution()
    showListNode(slt.addTwoNumbers_1(digit2ln([5,9,9]), digit2ln([5])))
