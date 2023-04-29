from Node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current_node = self.head
            while current_node.right:
                previous_node = current_node
                current_node = current_node.right
                current_node.left = previous_node
            current_node.right = node
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right        

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.value)
        return' -> '.join(nodes)    
    

    def insert_node(self, target, value):
        new_node = Node(value)
        if self.head:
            for node in self:
                if node.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print('empty list')
    
    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right.value == value:
                    node.right = node.right.right
                    return
    
    def get_tail(self):
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        return current_node.value

    def remove_tail(self):
        current_node = self.head
        if current_node.right:
            while current_node.right.right:
                current_node = current_node.right
            current_node.right = None
    
    def add_list(self, list):
        for e in list:
            self.add_node(e)
                

linked_list = LinkedList()


linked_list.add_node('sunday')
linked_list.add_node('monday')
linked_list.add_node('tuesday')
linked_list.add_node('thursday')


print(linked_list)

linked_list.insert_node('tuesday', 'wednesday')
print(linked_list)


linked_list.remove_node('sunday')



print(linked_list)

linked_list.get_tail
print(linked_list)

linked_list.remove_tail
print(linked_list)

linked_list.add_list(['september', 'october', 'november'])

print(linked_list)