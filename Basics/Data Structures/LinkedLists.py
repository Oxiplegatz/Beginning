class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ''
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_all_nodes(self, value_to_remove):
        current_node = self.get_head_node()
        while current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
            current_node = self.get_head_node()
        while current_node.get_next_node():
            next_node = current_node.get_next_node()
            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
            else:
                current_node = next_node

    def swap_nodes(self, val1, val2):
        print(f'Swapping {val1} with {val2}')

        node1_prev = None
        node2_prev = None
        node1 = self.head_node
        node2 = self.head_node

        if val1 == val2:
            print('Elements are the same - no swap needed')
            return

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1 is None or node2 is None:
            print('Swap not possible - one or more element is not in the list')
            return

        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)


test_ll = LinkedList()
test_ll.insert_beginning('The Extra Node')
test_ll.insert_beginning('The Last Node')
test_ll.insert_beginning(2)
test_ll.insert_beginning(3)
test_ll.insert_beginning('The Extra Node')
test_ll.insert_beginning('The Extra Node')
test_ll.insert_beginning(4)
test_ll.insert_beginning('Five')
test_ll.insert_beginning('The Problem Node')
test_ll.insert_beginning('The Extra Node')
test_ll.insert_beginning(6)
test_ll.insert_beginning('The Extra Node')

print('Original List:')
print(test_ll.stringify_list())

test_ll.remove_node('The Problem Node')

print('Problem Node removed:')
print(test_ll.stringify_list())

test_ll.remove_all_nodes('The Extra Node')

print('All Extra Nodes removed:')
print(test_ll.stringify_list())

print('Swapping two nodes:')
test_ll.swap_nodes('Five', 'The Last Node')
print(test_ll.stringify_list())
