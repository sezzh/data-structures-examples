class LinkedList(object):
    def __init__(self):
      self.head = None

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Result(object):
    def __init__(self):
        self.value = "" 


def print_every_node(node, result):
    result.value = result.value + " " + node.data
    if (node.next != None):
        print_every_node(node.next, result)

def print_nodes(linked_list):
    result = Result()
    if (linked_list.head != None):
        print_every_node(linked_list.head, result)
    return result.value



if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = Node('a')
    second_node = Node('b')
    third_node = Node('c')

    linked_list.head.next = second_node

    second_node.next = third_node

    print(print_nodes(linked_list))

