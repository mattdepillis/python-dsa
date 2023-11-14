"""

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def linked_list_palindrome(head):
    return


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

    while head:
        print(head.value)
        head = head.next


    print(linked_list_palindrome(head))