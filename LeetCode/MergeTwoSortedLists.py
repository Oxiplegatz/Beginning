# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1, list2):

        # merged_list = []
        # while list1 and list2:
        #     if list1.val > list2.val:
        #         merged_list.append(list2)
        #         list2 = list2.next
        #     elif list1.val <= list2.val:
        #         merged_list.append(list1)
        #         list1 = list1.next
        # if list1:
        #     while list1:
        #         merged_list.append(list1)
        #         list1 = list1.next
        # if list2:
        #     while list2:
        #         merged_list.append(list2)
        #         list2 = list2.next
        # if len(merged_list) >= 1:
        #     for i in range(len(merged_list) - 1):
        #         merged_list[i].next = merged_list[i+1]
        #     return merged_list[0]
        # else:
        #     return list1

        head_node = ListNode()
        pointer = head_node
        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next

        if list1:
            pointer.next = list1
        if list2:
            pointer.next = list2

        return head_node.next


a = ListNode(0, ListNode(5, ListNode(11)))
d = ListNode(6, ListNode(9, ListNode(56)))

print(Solution().merge_two_lists(a, d).val)
