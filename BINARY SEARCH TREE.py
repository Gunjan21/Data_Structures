class Binary_Search_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def set_root_value(self,data):
        self.data = data

    def get_root_value(self):
        return self.data

    def insert(self,data):
        if(data<self.data):
            if(self.left==None):
                self.left=Binary_Search_Tree(data)
            else:
                self.left.insert(data)
        else:
            if(self.right==None):
                self.right=Binary_Search_Tree(data)
            else:
                self.right.insert(data)
    def search(self, data):
        found = False
        if (data < self.data):
            if (self.left != None):
                found = self.left.search(data)
        elif (data > self.data):
            if (self.right != None):
                found = self.right.search(data)
        else:
            found = True
        return found

    def min_elem(self):
        curr = self
        while (curr.left != None):
            curr = curr.left
        return curr.data

    def max_elem(self):
        curr = self
        while (curr.right != None):
            curr = curr.right
        return curr.data

    def delete(self,data):
        result = self
        if data < self.data:
            #delete from left subtree. self.left may change in process
            if self.left != None:
                self.left=self.left.delete(data)
        elif data > self.data:
            #delete from right subtree. self.right may change in process
            if self.right != None:
                self.right=self.right.delete(data)
        else:
            #delete the current node #three cases 1- leaf 2-one child 3-two children
            if (self.left==None) and (self.right==None):
                #case 1 - Leaf
                result = None #current node deleted. returned tree is empty
            elif (self.left == None) or (self.right == None):
                #case 2 - one leaf
                if (self.left!= None):
                    result = self.left
                else:
                    result = self.right
            else:
                #case 3 - two childrem
                #successor is leftmost node in right subtree (smallest item
                #bigger than root)
                parent = self
                succ = self.right

                while (succ.left != None):
                    parent = succ
                    succ = succ.left
                #copy data of succ into self
                self.data  = succ.data
                #remove the succ node, taking care of attaching right
                #subtree of succ

                if (parent == self):
                    self.right = succ.right
                else:
                    parent.left = succ.right                    
        return result                
        
    def print_edges(self):
        if self.left != None:
            print(self.data, ", ", self.left.data)
            self.left.display()
        if self.right != None:
            print(self.data, ", ", self.right.data)
            self.right.display()

    def inorder_print(self):
        if self.left != None:
            self.left.inorder_print()
        print(self.data)
        if self.right != None:
            self.right.inorder_print()

    def preorder_print(self):
        print(self.data)
        if self.left != None:
            self.left.preorder_print()
        if self.right != None:
            self.right.preorder_print()

    def postorder_print(self):
        if self.left != None:
            self.left.postorder_print()
        if self.right != None:
            self.right.postorder_print()
        print(self.data)


    def iterative_inorder(self):
        stack = [ ]
        curr = self
        while (curr != None):
            stack.append(curr)
            curr = curr.left

        while (len(stack) != 0):
            curr = stack.pop()
            print(curr.data)
            curr = curr.right
            while (curr != None):
                stack.append(curr)
                curr = curr.left


        
