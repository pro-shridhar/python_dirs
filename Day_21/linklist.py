class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinlList:

    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        if not self.head:
            self.add_first(data)
            return

        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def show_list(self):
        temp = self.head
        # print(temp.data)
        while temp:
            print(temp.data, "->", end="")
            temp = temp.next
        print("null")


llist = LinlList()

llist.add_first(3)
llist.add_first(4)
llist.add_first(5)
llist.add_first(6)
llist.add_last(10)
llist.add_last(12)

llist.show_list()
