class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

class MyHashMap:

    def __init__(self, size):
        self.size = size
        self.array = []
        self.count = 0

        for i in range(self.size):
            linked_list = SLinkedList()
            linked_list.headval = None
            self.array.append(linked_list)

    def add_item(self, key, value):
        key_hash = hash(key)
        index = key_hash % self.size

        if(self.array[index].headval == None):
            self.array[index].headval = Node(key, value)
            self.count += 1
        else:
            node = self.array[index].headval
            print(node.key)
            print(node.value)
            print(node.nextval)
            while(node.nextval != None):
                node = node.nextval
            node.nextval = Node(key, value)
            print(node.nextval)
            self.count += 1
            print(self.count)
    
    def print_map(self):
        print(self.count)
        for item in self.array:

            node = item.headval
            while(node != None):
                print(node.key + " " + node.value)
                node = node.nextval


my_map = MyHashMap(10)
my_map.add_item('abcd', 'def')
my_map.add_item('abcd', 'def')
my_map.add_item('abcd', 'def')
my_map.add_item('xxx', 'def')
my_map.add_item('xxx', 'def')
my_map.print_map()
