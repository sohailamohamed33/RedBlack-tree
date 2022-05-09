import none as none

class node() :
    def __init__ (self,val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val
        self.color = 1  #red=1 and black=0

    def size (self):
        if self.left is None or self.right is None:
            #print('done')
            return 0
        else:
            #print('okay')
            return self.left.size()+1+self.right.size()

    def height (self):
        if self.left is None or self.right is None:
            return -1
        else :
            left = self.right.height()
            right = self.left.height()
            if left > right:
                return 1+left
            else :
                return 1+right

    def search (self,k):
        if self.val == None:
            return None
        elif k == self.val:
            return self.val
        else:
            if k < self.val:
                return self.left.search(k)
            else:
                return self.right.search(k)


class RBTree():
    def __init__(self):
        self.TNULL=node(0)
        self.TNULL.color=0
        self.TNULL.val=None
        self.root=self.TNULL
        self.sizeoftree=0

    def __str__(self):
        return str(self.root.val)

    def leftrotate(self,x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightrotate (self,x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fixinsert(self,s):
       # s.parent.color
        while s.parent is not None and s.parent.parent is not None and s.parent.color == 1:
            if s.parent == s.parent.parent.right:
                u=s.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    s.parent.color = 0
                    s.parent.parent.color = 1
                    s = s.parent.parent
                else:
                    if s==s.parent.left:
                        s=s.parent
                        self.rightrotate(s)
                    s.parent.color=0
                    s.parent.parent.color=1
                    self.leftrotate(s.parent.parent) #right left case
            else:
                u=s.parent.parent.right
                if u.color==1:
                    u.color=0
                    s.parent.color=0
                    s.parent.parent.color=1
                    s=s.parent.parent
                else:
                    if s==s.parent.right:
                        s=s.parent
                        self.leftrotate(s)
                    s.parent.color=0
                    s.parent.parent.color = 1
                    self.rightrotate(s.parent.parent)
                if s==self.root:
                    break
        self.root.color = 0

    def insert (self , value):
        Node= node(value)
        Node.parent = None
        Node.val = value
        Node.color = 1
        Node.left=self.TNULL
        Node.right=self.TNULL
        self.sizeoftree+=1
      #  print(self.sizeoftree)
        y=None
        x=self.root
        #parent & root at the same time
        while x!=self.TNULL:
            y=x
            if Node.val < x.val:
                x=x.left
            else:
                x=x.right
        #y is the parent no root involved
        Node.parent = y
        if y == None:
            self.root = Node
        elif Node.val < y.val:
            y.left = Node
        else:
            y.right=Node
        #new node is root
        if Node.parent == None:
            Node.color = 0 #root must be black
            return
        if Node.parent.parent == None:
            return

        self.fixinsert(Node)

    def search1(self,k):
        x=self.root.search(k)
        return x

    def size1(self):
        x=self.root.size()
        return x

    def height1(self):
        x=self.root.height()
        return x























