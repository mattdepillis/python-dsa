"""

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_three_nodes(node_one, node_two, node_three):
    return


if __name__ == "__main__":

    nodes = [
      {"id": "0", "left": None, "right": None, "value": 0},
      {"id": "1", "left": "0", "right": None, "value": 1},
      {"id": "2", "left": "1", "right": "4", "value": 2},
      {"id": "3", "left": None, "right": None, "value": 3},
      {"id": "4", "left": "3", "right": None, "value": 4},
      {"id": "5", "left": "2", "right": "7", "value": 5},
      {"id": "6", "left": None, "right": None, "value": 6},
      {"id": "7", "left": "6", "right": "8", "value": 7},
      {"id": "8", "left": None, "right": None, "value": 8}
    ]

    node_one_id = "5"
    node_two_id = "2"
    node_three_id = "3"

    node_one = node_two = node_three = None

    tree_nodes = {}

    for i in range(len(nodes)):
        node_info = nodes[i]
        tree_node = Node(node_info["value"])
        tree_nodes[node_info["id"]] = tree_node
        
    for i in range(len(nodes)):
        node_info = nodes[i]
        tree_node = tree_nodes[node_info["id"]]
        if node_info["left"]: tree_node.left = tree_nodes[node_info["left"]]
        if node_info["right"]: tree_node.right = tree_nodes[node_info["right"]]

        # assignment to variables node_one, node_two, node_three
        if node_info["id"] == node_one_id: node_one = tree_node
        elif node_info["id"] == node_two_id: node_two = tree_node
        elif node_info["id"] == node_three_id: node_three = tree_node

        tree_nodes[node_info["id"]] = tree_node


    print(validate_three_nodes(node_one, node_two, node_three)) # True