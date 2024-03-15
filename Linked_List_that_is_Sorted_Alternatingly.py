class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def sort(self, h1):
        if not h1 or not h1.next:
            return h1
        def merge(l1, l2):
            dummy = Node(0)
            curr = dummy
            while l1 and l2:
                if l1.data <= l2.data:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            return dummy.next 
        def split(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid
        def merge_sort(head):
            if not head or not head.next:
                return he
            left, right = split(head)
            left_sorted = merge_sort(left)
            right_sorted = merge_sort(right)

            return merge(left_sorted, right_sorted)
        return merge_sort(h1)
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()
