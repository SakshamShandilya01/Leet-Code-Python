class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        cur = head
        while cur:
            nxt = cur.next
            prev = dummy
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
        return dummy.next