class Stack:
    """Class implementing a stack"""

    def __init__(self):
        """Initialize the stack"""
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def push(self, item):
        """Push an item onto the stack"""
        self.stack.append(item)

    def pop(self):
        """Pop the last item off the stack and return it"""
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        """Return the top item of the stack without removing it"""
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        """Return the size of the stack"""
        return len(self.stack)


class Queue:
    """Class implementing a queue"""

    def __init__(self):
        """Initialize the queue"""
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the first item in the queue"""
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def size(self):
        """Return the size of the queue"""
        return len(self.queue)


class Node:
    """Class representing a node in a linked list"""

    def __init__(self, data):
        """Initialize the node"""
        self.data = data
        self.next = None


class LinkedList:
    """Class implementing a singly linked list"""

    def __init__(self):
        """Initialize the linked list"""
        self.head = None

    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None

    def add_first(self, data):
        """Add an item to the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        """Add an item to the end of the linked list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_first(self):
        """Remove and return the first item in the linked list"""
        if self.is_empty():
            return None
        removed_item = self.head.data
        self.head = self.head.next
        return removed_item


    def print_list(self):
        """Print the linked list"""
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next

    def reverse_list(self):
        """Reverse the linked list"""
        if self.is_empty():
            return
        current = self.head
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


class TreeNode:
    """Class representing a node in a binary tree"""

    def __init__(self, data):
        """Initialize the node"""
        self.data = data
        self.left = None
        self.right = None

class Tree:
    """Methods for Binary Tree operations using TreeNode"""

    def __init__(self):
        """Initialize the tree"""
        self.root = None

    def is_empty(self):
        """Check if the tree is empty"""
        return self.root is None

    def add(self, data):
        """Add an item to the binary tree"""
        if self.is_empty():
            self.root = TreeNode(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    current = current.left if current.left else TreeNode(data)
                    break
                elif data > current.data:
                    current = current.right if current.right else TreeNode(data)
                    break
                else:
                    break

    def height(self):
        """Return the height of the tree"""
        if self.is_empty():
            return 0
        else:
            return self.__height_node(self.root)

    def __height_node(self, node):
        """Return the height of the node"""
        if node is None:
            return 0
        else:
            return max(self.__height_node(node.left), self.__height_node(node.right)) + 1

    def search(self, data):
        """Search for an item in the tree"""
        if self.is_empty():
            return False
        else:
            current = self.root
            while current:
                if data < current.data:
                    current = current.left
                elif data > current.data:
                    current = current.right
                else:
                    return True
            return False

    def remove(self, data):
        """Delete an item from the binary tree"""
        if self.is_empty():
            return
        else:
            self.root = self.__remove_node(self.root, data)

    def __remove_node(self, node, data):
        """Delete the node"""
        if node is None:
            return None
        else:
            if data < node.data:
                node.left = self.__remove_node(node.left, data)
            elif data > node.data:
                node.right = self.__remove_node(node.right, data)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.__min_value_node(node.right)
                node.data = temp.data
                node.right = self.__remove_node(node.right, temp.data)
            return node

    def invert_tree(self):
        """Invert the tree"""
        if self.is_empty():
            return
        else:
            self.__invert_tree(self.root)

    def __invert_tree(self, node):
        """Invert the tree"""
        if node is None:
            return
        else:
            node.left, node.right = node.right, node.left
            self.__invert_tree(node.left)
            self.__invert_tree(node.right)

    def __min_value_node(self, node):
        """Return the minimum value node"""
        while node.left:
            node = node.left
        return node

    def print_tree(self, traversal='inorder'):
        """Print the tree"""
        if self.is_empty():
            print("Tree is empty")
        else:
            if traversal == 'inorder':
                self.__inorder_traversal(self.root)
            elif traversal == 'preorder':
                self.__preorder_traversal(self.root)
            else:
                self.__postorder_traversal(self.root)
    
    def __inorder_traversal(self, node):
        """Inorder traversal"""
        if node is not None:
            self.__inorder_traversal(node.left)
            print(node.data, end=' ')  # Print without newline
            self.__inorder_traversal(node.right)
    
    def __preorder_traversal(self, node):
        """Preorder traversal"""
        if node is not None:
            print(node.data, end=' ')
            self.__preorder_traversal(node.left)
            self.__preorder_traversal(node.right)
    
    def __postorder_traversal(self, node):
        """Postorder traversal"""
        if node is not None:
            self.__postorder_traversal(node.left)
            self.__postorder_traversal(node.right)
            print(node.data, end=' ')
    
    def __print_node(self, node, traversal):
        """Print the node"""
        if node is None:
            return
        else:
            if traversal == 'inorder':
                self.__inorder_traversal(node)
            elif traversal == 'preorder':
                self.__preorder_traversal(node)
            else:
                self.__postorder_traversal(node)

    def __inorder_traversal(self, node):
        """Inorder traversal"""
        if node:
            self.__inorder_traversal(node.left)
            print(node.data)
            self.__inorder_traversal(node.right)

    def __preorder_traversal(self, node):
        """Preorder traversal"""
        if node:
            print(node.data)
            self.__preorder_traversal(node.left)
            self.__preorder_traversal(node.right)

    def __postorder_traversal(self, node):
        """Postorder traversal"""
        if node:
            self.__postorder_traversal(node.left)
            self.__postorder_traversal(node.right)
            print(node.data)


class Graph:
    """Methods for Graph operations"""

    def __init__(self):
        """Initialize the graph"""
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge to the graph"""
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

    def remove_vertex(self, vertex):
        """Remove a vertex from the graph"""
        if vertex in self.graph:
            del self.graph[vertex]
            for key in self.graph:
                if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)

    def remove_edge(self, vertex1, vertex2):
        """Remove an edge from the graph"""
        if vertex1 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

    def print_graph(self):
        """Print the graph"""
        for key in self.graph:
            print(key, ":", self.graph[key])

    def breadth_first_search(self, start):
        """Breadth first search"""
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(self.graph[vertex])
        return visited

    def depth_first_search(self, node, visited=[]):
        """Depth first search"""
        if node not in visited:
            visited.append(node)
            for i in self.graph[node]:
                self.depth_first_search(i, visited)
        return visited