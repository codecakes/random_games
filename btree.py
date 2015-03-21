"""Implement a Binary Search Tree

A binary tree would be an object.
A Tree object will be a collection of nodes.

You can:
    
    - Insert nodes
    - Delete nodes
    - Merge Trees
    - Rebalance Trees
"""


class bnode(object):
    """Node level operations"""
    
    def __init__(self, root_node, value=None, left_node = None, right_node = None, parent_node = None):
        self.height = 0  #height of this node in a tree
        self.root_node = root_node
        self.val = value
        #add left and right nodes as bnode class
        self.add_left(left_node)
        self.add_right(right_node)
        self.add_parent(parent_node)
    
    def set_node_val(self, value):
        self.val = value    
    
    def add_left(self, left_node):
        if isinstance(left_node, bnode) and left_node.root_node <= self.root_node:
            self.left_node = left_node
            self.left_node.add_parent(self)
    
    def add_right(self, right_node):
        if isinstance(right_node, bnode) and right_node.root_node > self.root_node:
            self.right_node = right_node
            self.right_node.add_parent(self)
    
    def add_parent(self, parent_node):
        """
        Point current Node to a Parent Node.
        Add current height as Parent height + 1.
        """
        if isinstance(parent_node, bnode):
            self.parent_node = parent_node
            self.height = self.parent_node.height + 1
    
    def hasRightChild(self):
        """Whether this node has a right child node"""
        return True if hasattr(self, 'right_node') else False
    
    def hasLeftChild(self):
        """Whether this node has a left child node"""
        return True if hasattr(self, 'left_node') else False
    
    def isRightChild(self):
        """Whether this node is a right child node to a parent"""
        return self.parent_node.right_node == self if hasattr(self, 'parent_node') else False
    
    def isLeftChild(self):
        """Whether this node is a left child node to a parent"""
        return self.parent_node.left_node == self if hasattr(self, 'parent_node') else False
    
    def isLeaf(self):
        """
        return False If it has no left or right child, then it is a leaf 
        else return True
        """
        return not (self.hasLeftChild() or self.hasRightChild())
    
    def add_child_node(self, node):
        """Add a child node to left or right child position whichever is legit"""
        if node.root_node <= self.root_node:
            if self.hasLeftChild():
                #if left child node already exists
                self.left_node.add_child_node(node)
            else:
                #add to left node
                self.add_left(node)
        else:
            if self.hasRightChild():
                #if right child node already exists
                self.right_node.add_child_node(node)
            else:
                #add to right node
                self.add_right(node)
        return        
    
    def getMaxHeight(self):
        """get maximum height/depth till leaf nodes treating current node as root"""
        left = right = 0
        if not self.isLeaf():
            if self.hasLeftChild():
                left = self.left_node.getMaxHeight()
            if self.hasRightChild():
                right = self.right_node.getMaxHeight()
            print "left {} right {}".format(left, right)
            return max(left, right)
        else:
            return self.height
            
    
    def __str__(self):
        return "Root Node %s with parent %s with left child %s right child %s" %(\
        self.root_node, self.parent_node.root_node if hasattr(self, 'parent_node') else "None",\
        (self.left_node.root_node) if hasattr(self, 'left_node') else "None", \
        (self.right_node.root_node) if hasattr(self, 'right_node') else "None")





class btree(object):
    """A Binary Search Tree Implementation.
    It can:
        - Insert a value
        - Search for a value
        - Delete a subtree/node.
        - Minor misc. utilities.
        
    """
    
    def __init__(self, root_node, node_val=None):
        """root_node is a numeric value"""
        self.size = 0
        self.treeheight = 0
        self.min_key = None
        self.insert(root_node, node_val)
        self.setMaxTreeHeight()
        self.find_min_key()
        
    
    # All about setting a Node in the tree
    def insert(self, node_key, node_val=None):
        """Insert a root node if tree is emtpy else a new node under it"""
        
        if isinstance(node_key, (int, float, long)):
            new_node = bnode(node_key, value=node_val)    
            if hasattr(self, 'root_node'):
                self.root_node.add_child_node(new_node)
            else:
                self.root_node = new_node
            self.size += 1
        else:
            raise Exception("Not a bnode class")
    #
    
    # All about searching for a Node
    @classmethod
    def get_node(cls, bnode_instance, node_key):
        """ A recursive search for node_key. Returns the Node instance
        if present else None. Can be called directly. 
        node_key: A numeric value."""
        
        if node_key == bnode_instance.root_node:
            return bnode_instance
        elif node_key < bnode_instance.root_node:
            return cls.get_node(bnode_instance.left_node, node_key) if bnode_instance.hasLeftChild() else None
        elif node_key > bnode_instance.root_node:
            return cls.get_node(bnode_instance.right_node, node_key) if bnode_instance.hasRightChild() else None
    
    def __contains__(self, node_key):
        """Returns True if the specified key exists in the Tree ele
        False. 
        This way keys can be searched like:
            5 in btree1.
        node_key: A numeric value."""
        return True if self.get_node(self.root_node, node_key) != None else False
    
    def find_min_key(self):
        root_node = self.root_node
        min_key = root_node.root_node
           
        while root_node.hasLeftChild():
            root_node = root_node.left_node
            if min_key > root_node.root_node:
                min_key = root_node.root_node
        self.min_key = min_key
        del min_key
        return self.min_key
    # 
    
    # All About Getting the Max Tree Height of the Tree and Settign it
    # 
    def getMaxTreeHeight(self):
        """calculate the maximum height of tree starting from tree root"""
        self.treeheight = self.root_node.getMaxHeight()
        return self.treeheight
    
    @classmethod
    def imprint_height(cls, bnode_instance, tree_height):
        """
        
        The idea is to have each node in the btree have the same information 
        i.e. the maximum tree height of that btree so cutting back to recalculating 
        the same each time;
        
        This function is called from btree and is recursive.
        should be classmethod.
        
        Given a bnode class instance and the maximum tree height:
            (tree height = self.treeheight)
            
        1. Go through each node in the tree
        2. Find its left and right child nodes and go back to step 1
        3. Set a new class instance attribute 'maxtreeheight'
        on bnode instance with value tree height.
        """
        
        if not bnode_instance.isLeaf():
            if bnode_instance.hasLeftChild():
                cls.imprint_height(bnode_instance.left_node, tree_height)
            if bnode_instance.hasRightChild():
                cls.imprint_height(bnode_instance.right_node, tree_height)
        setattr(bnode_instance, 'maxtreeheight', tree_height)
        return
    
    
    def setMaxTreeHeight(self):
        """ Sets the maximum height attribute in each node in the tree
        so each node knows the current maximum height."""
        self.imprint_height(self.root_node, self.getMaxTreeHeight())
    #