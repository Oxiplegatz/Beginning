from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children


root = TreeNode('root')
child1 = TreeNode('branch1')
child2 = TreeNode('branch2')

root.add_child(child1)
root.add_child(child2)

root.traverse()


# Breadth-first search function
def bfs(root_node, goal_value):
    # initialize frontier queue
    path_queue = deque()

    # add root path to the frontier
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    # search loop that continues as long as
    # there are paths in the frontier
    while path_queue:
        # get the next path and node
        # then output node value
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f"Searching node with value: {current_node.value}")

        # check if the goal node is found
        if current_node.value == goal_value:
            return current_path

        # add paths to children to the  frontier
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    # return an empty path if goal not found
    return None
