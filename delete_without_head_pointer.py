class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to delete a node without any reference to head pointer.
    def deleteNode(self, del_node):
        if del_node is None or del_node.next is None:
            # If the node is None or the last node, we cannot delete it.
            return
        
        # Copy the data of the next node to the current node.
        del_node.data = del_node.next.data
        
        # Point the current node to the node after the next node.
        del_node.next = del_node.next.next
