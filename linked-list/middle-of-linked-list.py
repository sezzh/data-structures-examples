class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
      self.head = None
    
    def insert(self, data):
        next_node = Node(data)
        self.add_to_end(next_node)

    def add_to_end(self, node_to_add):
        if (self.head == None):
            self.head = node_to_add
        else:
            temp_node = self.head
            if (temp_node.next == None):
                temp_node.next = node_to_add
            else:
                while (True):
                    if (temp_node.next == None):
                        temp_node.next = node_to_add
                        break
                    else:
                        temp_node = temp_node.next


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
    linked_list.insert('1')
    linked_list.insert('2')
    linked_list.insert('3')
    linked_list.insert('4')
    linked_list.insert('5')
    print(print_nodes(linked_list))

