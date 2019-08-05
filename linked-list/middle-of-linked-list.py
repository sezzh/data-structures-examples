from math import ceil

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
      self.head = None
      self.length = 0
    
    def insert(self, data):
        next_node = Node(data)
        self.add_to_end(next_node)

    def add_to_end(self, node_to_add):
        temp_length = 0
        if (self.head == None):
            self.head = node_to_add
            temp_length = 1
        else:
            temp_node = self.head
            if (temp_node.next == None):
                temp_node.next = node_to_add
                temp_length = 2
            else:
                temp_length = 1
                while (True):
                    temp_length = temp_length + 1
                    if (temp_node.next == None):
                        temp_node.next = node_to_add
                        break
                    else:
                        temp_node = temp_node.next
        self.length = temp_length

    def get_middle_value(self):
        length_type = self.get_even_or_odd()
        if (length_type == 'even'):
            node_index_to_get = self.length / 2
            return self.get_selected_node(node_index_to_get)
        node_index_to_get = round(self.length / 2)
        return self.get_selected_node(node_index_to_get)

    def get_even_or_odd(self):
        if (self.length % 2 == 0):
            return 'even'
        return 'odd'

    def get_selected_node(self, node_index):
        temp_node = self.head
        count = 0
        while (True):
            if (count == node_index):
                return temp_node
            temp_node = temp_node.next
            count = count + 1

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
    for i in range(5):
        linked_list.insert(str(i + 1))
        print("length of linked list: {}".format(linked_list.length))
        print("size of linked list is: {}".format(linked_list.get_even_or_odd()))
    print(print_nodes(linked_list))

    print("printing odd second middle value: {}".format(linked_list.get_middle_value().data))

    print("===================================")

    linked_list = LinkedList()
    for i in range(6):
        linked_list.insert(str(i + 1))
        print("length of linked list: {}".format(linked_list.length))
        print("size of linked list is: {}".format(linked_list.get_even_or_odd()))
    print(print_nodes(linked_list))
    
    print("printing even middle value: {}".format(linked_list.get_middle_value().data))

    print("linked_list data of HEAD: {}".format(linked_list.get_selected_node(0).data))

    print("linked_list data of 1: {}".format(linked_list.get_selected_node(1).data))



