class BTreeClass:
    
    #Creating root and giving the minimal 10 degree
    def __init__(self, degree = 10):
        self.rootNode = BTreeNode(True)
        self.degree = 10
    
    #Insert Command
    def splitNode(self, curNode, i):
        d = self.degree
        childNode = curNode.children[i]
        
        #Creating new node for the newly split data
        newNode = BTreeNode(leaf=childNode.leaf)
        
        #Getting the key from the middle and applying to the curNode
        mkey = childNode.keys[d-1]
        curNode.keys.insert(i, mkey)
        
        #The new node is on the right of d and the old node is to the left of d
        newNode.keys = childNode.keys[d: (2 * d) - 1]
        childNode.keys = childNode.keys[0: d - 1]
        
        #Handles the nodes being promoted
        if not childNode.leaf:
            newNode.children = childNode.children[d: 2 * d]
            childNode.children = childNode.children[0: d]
        curNode.children.insert(i + 1, newNode)

    def insertNode (self, curNode, key):
        i = len(curNode.keys) - 1
        if curNode.leaf:
            
            # Empty node to make space for new node
            curNode.keys.append(None)
            
            #Making room for new key
            while i >= 0 and curNode.keys[i] > key:
                curNode.keys[i + 1] = curNode.keys[i]
                i -= 1
            curNode.keys[i + 1] = key
        else:
            while i >= 0 and curNode.keys[i] > key:
                i -= 1
            i += 1
            if len(curNode.children[i].keys) == (2 * self.degree) - 1:
                self.splitNode(curNode, i)
                if key > curNode.keys[i]:
                    i += 1
            self.insertNode(curNode.children[i], key)
    def insertFull(self, curNode, key):
        root = self.rootNode
        
        #When the tree is full, it gets split into two nodes
        if len(root.keys) == (2 * self.degree) - 1:
            tempNode = BTreeNode(leaf = False)
            self.rootNode = tempNode
            tempNode.children.append(root)
            self.splitNode(tempNode, 0)
            self.insertNode(tempNode, key)
        else:
            self.insertNode(root, key)

#Representing every node of the Btree
class BTreeNode:
    def __init__(self, leaf = True):
        self.leaf = leaf
        self.keys = []
        self.children = []
        
    #displaying the tree by the keys of each node
    def display(self, node=0):
        print(f"Level {node}: {self.keys}")
        if not self.leaf:
            for c in self.children:
                c.display(node + 1)

if__name__ == "main":
main()

