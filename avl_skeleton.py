#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - 209087592
#name2    - Yael Toledano



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
        if value is None:
            self.value = None
            self.left = None
            self.right = None
            self.height = -1
            self.size = 0
        else:
            self.value = value
            self.left = AVLNode(None)
            self.right = AVLNode(None)
            self.height = 0
            self.size = 1
        self.parent = None
        self.balanceFactor = 0
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left if self.left.isRealNode() else None


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right if self.right.isRealNode() else None

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
                self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
                self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
                self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
                self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
                self.height = h

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return False if self.getValue() == None else True
	
	###########################################
	        """retrieves the node with the maximum rank in a subtree

        @type node: AVLnode
        @pre: node != none
        @param node: the root of the subtree
        @rtype: AVLNode
        @returns: the node with the maximum rank in a subtree
        """
        def getMax(self):
                if !self.getRight().isRealNode():
                        return self
                return self.getRight().getMax()

	 """retrieves the node with the minimum rank in a subtree

        @type node: AVLnode
        @pre: node != none
        @param node: the root of the subtree
        @rtype: AVLNode
        @returns: the node with the minimum rank in a subtree
        """
        def getMin(self):
                if !self.getLeft().isRealNode():
                        return self
                return self.getLeft().getMin()
	
	
                """retrieves the successor

        @type node: AVLnode
        @pre: node != none
        @rtype: AVLNode
        @returns: the successor of node,  None if there is no left child
        """
	def getSuccessor(self):
                if self.getRight().isRealNode():
                        return slef.getRight.getMin()
                node = self
                parent = node.getParent()
                while parent is not None and node = parent.getRight():
                        node = parent
                        parent = node.getParent()
                return parent
 
        """retrieves the predecessor

        @type node: AVLnode
        @pre: node != none
        @rtype: AVLNode
        @returns: the predecessor of node,  None if there is no left child
        """    
        def getPredecessor(self, node):
                if self.getLeft().isRealNode():
                        return slef.getRight.getMax()
                node = self
                parent = node.getParent()
                while (temp is not None and node = parent.getLeft()):
                        node = parent
                        parent = node.getParent()
                return parent
        
        """returns node size

        @rtype: int
        @returns: the node's size""" ########### needs test ###########
        def getSize(self): 
                return self.size
        

        def setSize(self, i):
                self.size = i

        """update the size of the node
        @rtype: None
        @returns: None
        """

        def updateSize(self):
        ]       self.size = self.getRight().getSize() + self.getLeft().getSize() + 1


        """update balance factor
        """
        def updateBalanceFactor(self):
                self.balanceFactor = self.getLeft().getHeight() - self.getRight().getHeight()

        """return balance factor
        @rtype: int
        @return: balanceFactor
        """

        def getBalanceFactor(self):
                return self.balanceFactor

        """update the height
        """

        def updateHeight(self):
                self.setHeight(max(self.getLeft().getHeight(), self.getRight().getHeight()) + 1)


        """Increase Size by 1
        @param node: a node
        """

        def increaseSizeByOne(self):
                self.size = self.size + 1

	#########################################


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.first = None
		self.last = None

        ############################################
	""" @pre: |node's balance factor| <= 1 """
	def setRoot(self, node)
                self.root = node
        ###########################################
	
	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return True if self.getRoot() is None else False


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	"""


	def retrieve(self, i):
                return self.treeSelect(i+1)

        
	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
                nodeToInsert = AVLNode(val)
                if i == 0 and self.root is None:
                    self.first = nodeToInsert
                    self.last = nodeToInsert
                    self.root = nodeToInsert

                    return 0
                if i == 0:
                    self.first = nodeToInsert
                if i == self.length():
                    self.last = nodeToInsert

                self.insertRec(i, self.getRoot(), nodeToInsert)
                parentNode = nodeToInsert.getParent()
                counter = self.fixTree(parentNode)
                return counter		

        ########################################
            """recursive function for insert the node

                @type i: AVlnode
                @pre: 0 <= i <= self.length()
                @param i: The intended index in the list to which we insert val depend on ths suptree
                @rtype: None
                """

            def insertRec(self, i, root, nodeToInsert):
                root.increaseSizeByOne()

                if i == 0 and not root.getLeft().isRealNode():
                    root.setLeft(nodeToInsert)
                    nodeToInsert.setParent(root)
                    return

                if i == 1 and not root.getRight().isRealNode() and not root.getLeft().isRealNode():
                    root.setRight(nodeToInsert)
                    nodeToInsert.setParent(root)
                    return

                leftTreeSize = root.getLeft().getSize()

                if i <= leftTreeSize:
                    self.insertRec(i, root.getLeft(), nodeToInsert)
                else:
                    self.insertRec(i - (leftTreeSize + 1), root.getRight(), nodeToInsert)
                return

            """rebalance the tree after insertion

                @type AVLnode
                @pre: 0 <= i <= self.length()
                @param i: the last parent of th node that inserted to the tree
                @rtype: int
                @returns: the number of rebalancing operation due to AVL rebalancing
                """

            def fixTree(self, node):
                counter = 0
                while node is not None and node.isRealNode():
                    parentLastHeight = node.getHeight()
                    node.updateHeight()
                    node.updateBalanceFactor()
                    bf = node.getBalanceFactor()
                    if abs(bf) <= 1 and node.getHeight() == parentLastHeight:
                        return counter
                    elif abs(bf) <= 1 and node.getHeight() != parentLastHeight:
                        node = node.getParent()
                        continue

                    elif abs(bf) == 2:
                        if bf == -2:
                            rightNode = node.getRight()
                            if rightNode.getBalanceFactor() == -1:
                                self.leftRotate(node)
                                counter += 1
                            elif rightNode.getBalanceFactor() == 1:
                                self.rightThenLeft(node)
                                counter += 1

                        elif bf == 2:
                            leftNode = node.getLeft()
                            if leftNode.getBalanceFactor() == -1:
                                self.leftThenRight(node)
                                counter += 1
                            elif leftNode.getBalanceFactor() == 1:
                                self.rightRotate(node)
                                counter += 1
                    node = node.getParent()

                return counter

            """right then left rotate operation
                @type AVLnode()
                @param i: the node that need to be rotated
                """

            def rightThenLeft(self, B):
                self.rightRotate(B.getRight())
                self.leftRotate(B)

            """left then right rotate operation
                    @type AVLnode()
                    @param i: the node that need to be rotated
                    """

            def leftThenRight(self, B):
                self.leftRotate(B.getLeft())
                self.rightRotate(B)

            """left rotate operation
                    @type AVLnode()
                    @param i: the node that need to be rotated
                    """

            def leftRotate(self, B):
                isLeftSon = False
                if B.getParent() is not None and B.getParent().getLeft() == B:
                    isLeftSon = True
                A = B.getRight()

                B.setRight(A.getLeft())
                B.getRight().setParent(B)
                A.setLeft(B)
                if B.getParent() is not None:
                    A.setParent(B.getParent())
                    if isLeftSon:
                        A.getParent().setLeft(A)
                    else:
                        A.getParent().setRight(A)
                else:
                    A.setParent(None)
                    self.root = A

                B.setParent(A)
                A.updateHeight()
                B.updateHeight()
                A.updateBalanceFactor()
                B.updateBalanceFactor()
                A.setSize(B.getSize())
                B.setSize(B.getLeft().getSize() + B.getRight().getSize() + 1)

            """right rotate operation
                    @type AVLnode()
                    @param i: the node that need to be rotated
                    """

            def rightRotate(self, B):
                isRightSon = False
                if B.getParent() is not None and B.getParent().getRight() == B:
                    isRightSon = True
                A = B.getLeft()

                B.setLeft(A.getRight())
                B.getLeft().setParent(B)
                A.setRight(B)
                if B.getParent() is not None:

                    A.setParent(B.getParent())
                    if isRightSon:
                        A.getParent().setRight(A)
                    else:
                        A.getParent().setLeft(A)
                else:
                    A.setParent(None)
                    self.root = A

                B.setParent(A)
                A.updateHeight()
                B.updateHeight()
                A.updateBalanceFactor()
                B.updateBalanceFactor()
                A.setSize(B.getSize())
                B.setSize(B.getLeft().getSize() + B.getRight().getSize() + 1)

        ############################################

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.first.getValue() if !self.empty() else None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.last.getValue() if !self.empty() else None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
                return self.listToArrayRec(self.getRoot())

        ##########################################
        def listToArrayRec(self, node):
                if node is None:
                        return []
		return self.listToArray(node.getLeft()) + self.getValue() + self.listToArray(node.getRight())
        ########################################## 



	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
                return self.getRoot().getSize() if !self.empty() else 0 
                

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i): 
                x = self.retrieve(i)
                __init__(
                list1 = AVLTreeList()
                list1.setRoot(x.getLeft())
                list2 = AVLTreeList()
                list2.setRoot(x.getRight())
                while (x.getParent() is not None):
                        if x == x.getParent().getRight():
                                join(x.getParent().getLeft(), x.getParent() , list1)
                        else: #x == x.getParent().getLeft()
                                join(x.getParent().getRight(), x.getParent() , list2)
                        x = x.getParent()
		return [list1, x, list2]


	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
                ### missing rotation ###
                x = self.last()
                self.delete(x)
                self.join(self, x,lst)
                return Math.abs(lst.getRoot().getHeight() - self.getRoot().getHeight())
        
        #################################################
        def join(list1, x, list2):
                a = list1.getRoot()
		b = list2.getRoot()
                if Math.abs(b.getHeight() - a.getHeight()) <= 1:
                        list1.setRoot(x)
                else if b.getHeight() - a.getHeight() < -1:
                        while(a.getHeight() > b.getHeight()):
                                a = a.getRight()
                        x.setParent(a.getParent)
                else: #b.height - a.height > 1:
                        while(b.getHeight > a.getHeight):
                                b = b.getLeft()
                        x.setParent(b.getParent)
                        list1.setRoot(list2.getRoot())     
                x.setLeft(a)
                x.setRight(b)
        ###############################################                


	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
                return self.searchRec(val, self.first(), 0)

        ##################################################
        def searchRec(self, val, node, i):
                if i >= self.length():
                        return -1
                if node.getValue() == val:
                        return i
                return self.searchRec(val, node.getSuccessor, i+1)
        ##################################################

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root

	##########################################
        def treeSelcet(self, i):
                return self.treeSelectRec(self.getRoot(),i)
                
        def treeSelect(self, node,i):
                rank = self.node.getLeft().getSize() + 1
                if i == rank:
                        return node
                else if i < rank:
                        return self.treeSelectRec(node.getLeft(), i)
                else: #i > rank
                        return self.treeSelectRec(node.getRight(), i-rank)
                
        
        """@pre node is a real node """
        def getRank(self, node):
                rank = self.getRoot().getLeft().getSize() + 1
                node = node.getParent()
                while (node is not None):
                        if node == node.getParent().getRight():
                                rank += node.getParent().getLeft().getSize() + 1
                        node = node.getParent()
                return rank
        ###########################################
