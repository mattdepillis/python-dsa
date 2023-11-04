"""

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node, visited):
    visited.append(node.value)

    if node.left: dfs(node.left, visited)
    if node.right: dfs(node.right, visited)

    return visited

def repair_bst(node):
    return node


if __name__ == "__main__":
    # nodes = [
    #     {"id": "10", "left": "5", "right": "13", "value": 10},
    #     {"id": "13", "left": "15", "right": "22", "value": 13},
    #     {"id": "22", "left": None, "right": None, "value": 22},
    #     {"id": "15", "left": None, "right": "14", "value": 15},
    #     {"id": "14", "left": None, "right": None, "value": 14},
    #     {"id": "5", "left": "2", "right": "6", "value": 5},
    #     {"id": "6", "left": None, "right": None, "value": 6},
    #     {"id": "2", "left": "1", "right": None, "value": 2},
    #     {"id": "1", "left": None, "right": None, "value": 1}
    # ]

    nodes = [
        {"id": "10", "left": "7", "right": "20", "value": 10},
        {"id": "7", "left": "3", "right": "12", "value": 7},
        {"id": "12", "left": None, "right": None, "value": 12},
        {"id": "20", "left": "8", "right": "22", "value": 20},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "3", "left": "2", "right": None, "value": 3},
        {"id": "8", "left": None, "right": "14", "value": 8},
        {"id": "14", "left": None, "right": None, "value": 14},
        {"id": "2", "left": None, "right": None, "value": 2}
    ]

    store = {}

    for obj in reversed(nodes):
        node = Node(obj["value"])
        if obj["left"]: node.left = store[obj["left"]]
        if obj["right"]: node.right = store[obj["right"]]
        store[obj["id"]] = node

    root = store[nodes[0]["id"]]
    
    print(repair_bst(root))

    print(dfs(root, []))