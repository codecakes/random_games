## Singly Linked List
## Each Node is relatively Head to the next node it refers to.
## The Linked List can be broken down into:
## Nodes.

"""
Single Linked List can:
    - Insert at Head, Tail, Inbetween
    - Delete at Head, Tail, Inbetween
    - Add another LinkedList to Existing
"""


class LinkedNode(object):
    """
    Nodes have following attributes:
        1. Node Value
        2. Next Node
        3. Head Node?
        4. Last Node?
    """
    def __init__(self):
        self.val = None
        self.nxt = None
        #this is telling the length of orphan node self or the length of chain 
        #so far including the self node
        self.len = 1
        #set the following if part of a linked list chain
        self.head = 0
        self.last = 0
        #this ptr in each node tells the head node ptr
        self.headptr = None

    
    def setVal(self, val):
        self.val = val
    
    def getVal(self): return self.val
    
    def getLen(self): return self.len
            
    def setNxt(self, other):
        self.nxt = other  #O(1)
    
    def setHead(self):
        """If there is a successive node, set this as Head node"""
        if self.hasNxt() and self.head==0:
            self.head = 1
            self.headptr = self
        
    def setLast(self):
        """If this is the last node, set this as Last node"""
        if not self.hasNxt() and self.last==0:
            self.last = 1
    
    def insertHead(self, newNode):
        """Insert newNode as Head node"""
        if self.isHead():
            node = self
        else:
            node = self.headptr
        if node:
            newNode.len = 1
            newNode.setNxt(node)  #O(1)
            newNode.setHead()
    
    def insertLast(self, newNode):
        """insert newNode as Last node"""
        newNode.setLast()
        
        node = self    
        #O(k<=n)
        while not node.isLast():
            node = node.getNxt()
        node.last = 0
        node.setNxt(newNode)
        newNode.len = node.len + 1
        newNode.headptr = self.headptr
    
    def getNxt(self): return self.nxt
    
    def hasNxt(self): return self.getNxt() != None
    
    def disconnectNxt(self):
        if self.hasNxt():
            self.nxt = None
            self.head = 0
    
    def isHead(self): return self.head == 1
    
    def isLast(self): return self.last == 1
    

            
                

            
class SingleLinkedList(object):
    
    def __init__(self, link_node):
        self.head_node = link_node
        self.last_node = None
        self.master_ln = 0
        self.updateHead(self.head_node)
    
    def add_node(self, val):
        assert self.head_node == self.last_node.headptr
        newNode = LinkedNode()
        newNode.setVal(val)
        self.last_node.setNxt(newNode)
        self.last_node = newNode
        newNode.len = self.master_ln + 1
        self.master_ln = newNode.len
        newNode.headptr = self.head_node
    
    def deleteNode(self, val):
        prev = node = self.head_node
        node_val = node.val
        while node_val != val and node.hasNxt():
            prev = node
            node = node.getNxt()
            node_val = node.val
            if node_val == val: break
        
        if node_val == val:
            if node.isLast():
                #if its last node
                prev.disconnectNxt()
                head = prev.headptr
            elif node.isHead():
                #if its head node
                nxt = node.getNxt()
                node.disconnectNxt()
                nxt.setHead()
                head = nxt
            elif node.hasNxt():
                #if its somewhere between
                nxt = node.getNxt()
                node.disconnectNxt()
                nxt.len = prev.len + 1
                prev.setNxt(nxt)
                head = prev.headptr
            self.updateHead(head)
            
    
    def updateHead(self, headptr):
        """
        Set each node's headptr to head node of Chain.
        Set incremental length as node increases
        """
        node = headptr
        self.head_node = node.headptr = headptr
        node.head = 1
        node.len = 1
        ln = node.len
        #till the end of chain
        while node.hasNxt():
            #get next node
            node = node.getNxt()
            #Set each node's headptr to head node of Chain
            node.headptr = headptr
            node.head = 0
            #Set incremental length as node increases
            node.len = ln + 1
            ln = node.len
        node.setLast()
        self.last_node = node
        self.master_ln = ln
        assert node.headptr.len == 1
        
    
    def updateList(self, otherlist):
        """Merge another linked list from end to current linked list"""
        other = otherlist.head_node
        if other.isHead(): other.head = 0
        #Ripple headptr and inc length across nodes
        self.last_node.setNxt(other)
        self.updateHead(self.head_node)
    
    def insertPos(self, val, pos):
        """Insert newNode as position pos if legit. 
        Current Pos is always 1 and relatively current node is the start node.
        But each node gives absolute chain/linked-list length.
        """
        if pos < 0 or pos > self.master_ln: return
        
        newNode = LinkedNode()
        newNode.setVal(val)
        
        if pos == self.master_ln:
            self.last_node.insertLast(newNode)
            self.master_ln += 1
            #newNode.headptr = self.head_node
            self.last_node = newNode
            
            return
        elif pos == self.head_node.len:
            self.head_node.insertHead(newNode)
            self.head_node = newNode
            self.updateHead(self.head_node)
            return
        
        node = self.head_node
        while node.len < pos-1:
            node = node.getNxt()
            if node.len == pos-1: break
        
        assert node.len == pos-1
        nxt_node = node.getNxt()
        node.setNxt(newNode)  #newNode has nxt_node's postion
        newNode.setNxt(nxt_node)  #nxt_node's position is incremented by 1
        self.updateHead(self.head_node)
        return


#just for testing
if __name__ == "__main__":
    a,b,c,d,n = [LinkedNode() for _ in xrange(5)]
    n.setVal(1)
    map(lambda x: x[0].setVal(x[1]), ((a,2), (b,3), (c,4), (d,5)))
    
    n.setNxt(a)
    
    a.setNxt(b)
    
    b.setNxt(c)
    
    L = SingleLinkedList(n)
    node = L.head_node
    print "="*10
    while node.hasNxt():
        print node.val 
        print node.headptr.val
        print node.len
        print
        node = node.getNxt()
    print node.val 
    print node.headptr.val
    print node.len

    L.insertPos(40, 2)
    #L.insertPos(1, 30)
    node = L.head_node
    print "="*10
    while node.hasNxt():
        print node.val 
        print node.headptr.val
        print node.len
        print
        node = node.getNxt()
    print node.val 
    print node.headptr.val
    print node.len
    
    L.deleteNode(40)
    L.deleteNode(3)
    L.deleteNode(1)
    L.deleteNode(2)
    print "="*10
    node = L.head_node
    while node.hasNxt():
        print node.val 
        print node.headptr.val
        print node.len
        print
        node = node.getNxt()
    print node.val 
    print node.headptr.val
    print node.len
    
    L.add_node(40)
    L.insertPos(20, 1)
    print "="*10
    node = L.head_node
    while node.hasNxt():
        print node.val 
        print node.headptr.val
        print node.len
        print
        node = node.getNxt()
    print node.val 
    print node.headptr.val
    print node.len