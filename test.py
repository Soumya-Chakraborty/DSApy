from DSApy.algorithms import Searching, Sorting
from DSApy.dataStructure import Stack, Queue, LinkedList, Tree, Graph

# Create a stack
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2

# Create a queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue.dequeue())# Output: 1

# Create a linked list
linked_list = LinkedList()
linked_list.add_first(1)
linked_list.add_last(2)
linked_list.add_last(3)
linked_list.add_last(4)
linked_list.add_last(5)
linked_list.print_list()  # Output: 1 2

# Create a binary tree
tree = Tree()
tree.add(5)
tree.add(3)
tree.add(8)
tree.print_tree(tree.root)  # Output: 5 3 8
tree.print_tree() # Output: 3 5 8

# Create a graph
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_edge('A', 'B')
graph.print_graph()  # Output: A : ['B']

# Now you can create instances of the Searching and Sorting classes and use their methods
search_arr = Searching()
sort_arr = Sorting()

# Example usage:
search_result = search_arr.linear_search([1, 2, 3, 4, 5], 4)
print("Linear search result:", search_result)

array = [5, 2, 4, 6, 1, 3]
sort_arr.bubble_sort(array)
print("Sorted array:", array)