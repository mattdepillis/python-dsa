"""

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def assign_prev_node(head):
    prev, curr = None, head

    while curr:
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