---
Problem: Remove Duplicates from Linked List
Type: Linked List
Date Written: 08-15-2022
---

# Problem
Implement a graph class and write a depth-first search method that traverses the graph from left to right, starting with the startNode. The method should return an array of all nodes, in the order in which they were visited on traversal.

For example, python```depth_first_search()``` on a graph that looks like the following:
      A
    /   \
   B     C
  / \
  D E
should return ```['A', 'B', 'D', 'E', 'C']```.

# Solution
I tried doing this with methods other than the recursive version; I think the recursive is easy to understand and eloquent since it allows you to traverse the tree in an orderly fashion with a few lines of code. I also haven't covered stacks yet - the easiest way to implement this iteratively, by my understanding.

**Pseudocode:**
- feed params through the function:
  - node: the key of the node itself.
  - visited: a list of already-visited nodes.
- check whether the node is in ```visited``` - we want to make sure we're not double-counting nodes in the traversal and/or sending the execution into an infinite loop. with a tree graph structure, this check likely won't be needed. if the node isn't in ```visited```:
  - add it to the visited list.
  - for each child/neighbor (in this case, they're children) of the node, listed in the graph:
    - recursively call the function on that node. This adds the function call to the stack for one child and its children and its children, etc. before it does for the rightward children for a given level.
- return the visited array once all

**Big O:**
- O(v + e) time, where v = number of nodes in the graph and e = number of edges in the graph
  - NOTE: on a tree, time complexity is O(v)
  - In a non-tree graph (where there's an adjacency list for each node, not a list of children), each item's adjacency list will be traversed once. That means that the function could be called on a node A (the start node for the traversal) since A is in node B's adjacency list. The addition of the nodes to the visited array is an extra operation only perfomed when a new node is visited. Overall, the algorithm will execute a new function call for each item in the adjacency list and will add to the list for each new node - resulting in O(v + e) complexity.
  - for a tree, edges are one-way (since it's a parent-child relationship) so every node visited will be automatically added to the list. This yields time complexity of O(v).
- O(v) space, where v = number of nodes in the graph
  - The algorithm needs to store each node in the list.

**An Alternative to the Recursive Solution**
[Here's how one could go about implementing this iteratively. (Included in the case I want to revisit with stacks later).](https://www.techiedelight.com/depth-first-search/#:~:text=Iterative-,Implementation,-of%20DFS)