import struct

class BTree:
    
    class HeaderFormat:
        def __init__(self, rootID=0, nextAvailableID=1):
            self.magicNumber = b"4337PRJ3"
            self.rootID = rootID
            self.nextAvailableID = nextAvailableID

        #This method serves in converting each piece of header data into bytes
        def packToBytes(self):

            # Magic Number is in Byte literal
            magicNumberData = self.magicNumber("utf-8")

            #RootID and nextAvailableID is in integer
            rootIDData = self.rootID.to_bytes(8, 'big')
            nextAvailableIDData = self.nextAvailableID.to_bytes(8, 'big')
            headerData =  magicNumberData + rootIDData + nextAvailableIDData

            #Data must be stored as a 512 block
            padded_headerData = headerData + b'\x00' * (512 - len(headerData))
            return padded_headerData

        #This method will take reconvert the header data into its respective data types
        def unpackFromBytes(data):
            magicNumber = data[:8]
            rootID = int.from_bytes(data[8:16], 'big')
            nextAvailableID = int.from_bytes(data[16:24], 'big')

            #Header Object created with the reconverted data
            return HeaderFormat(magicNumber, rootID, nextAvailableID)
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


