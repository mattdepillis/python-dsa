"""
Write a function that takes in the head of a Singly Linked List and returns a boolean representing whether the linked list's nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

TC: O(n) -- iterate through the linked list 2 full times maximum
SC: O(n) -- add another property PREV to each list node. We can do better than this with a slight mod -- see solution 2.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def assign_prev_node(head):
    prev, curr = None, head

    while curr:
        # NOTE: there's a way to effectively achieve this without adding a prev property to each instance of Node -- reverse the linked list from the halfway mark of the list.
        curr.prev = prev
        curr, prev = curr.next, curr

    return head, prev

def linked_list_palindrome(head):
    left, right = assign_prev_node(head)

    while left is not right:
        if left.value != right.value: return False
        if left.next == right: break
        left, right = left.next, right.prev

    return True


if __name__ == "__main__":
    
    store = {}

    nodes = [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "2-2", "value": 2},
        {"id": "2-2", "next": "1-2", "value": 2},
        {"id": "1-2", "next": "0-2", "value": 1},
        {"id": "0-2", "next": None, "value": 0}
    ]

    head_id = nodes[0]["id"]

    for obj in reversed(nodes):
        node = Node(obj["value"])
        if obj["next"]: node.next = store[obj["next"]]
        store[obj["id"]] = node

    head = store[head_id]

    # while head:
    #     print(head.value)
    #     head = head.next


    print(linked_list_palindrome(head))