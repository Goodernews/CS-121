class BSTNode:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def searchPath(self, k):
      if self[k]==None:
        return []
      def node_search(n):
        if n.key==k:
          return []
        elif n.key < k:
          return ["R"] + node_search(n.right)
        elif n.key > k:
          return ["L"] + node_search(n.left)

      return node_search(self.root)

    def height(self):
      if self.root == None:
        return -1
      n_search = [self.root]
      height_tree=-1

      while n_search!=[]:
        holder = []
        for n in n_search:
          if n.left!=None:
            holder.append(n.left)
          if n.right!=None:
            holder.append(n.right)
        n_search = holder
        height_tree+=1

      return height_tree


    def deleteMax(self):
      if self.root!=None:
        n = self.root
        if n.left==None and n.right==None:
          self.root=None
        elif n.left!=None and n.right==None:
          self.root = n.left
        elif n.left==None and n.right!=None:
          self.root = n.right
        else:
          while n.right.right!=None: # Finds parent of max node
            n = n.right
          if n.right.left!=None: # Max value has a child
            n.right = n.right.left
          else:
            n.right=None

    def isEmpty(self):
        return self.root == None

    def apply(self, func):

      def node_apply(n):
        n.value = func(n.value)
        if n.left!=None:
          node_apply(n.left)
        if n.right!=None:
          node_apply(n.right)

      if self.root!=None:
        node_apply(self.root)

    def get(self, k):
        n = self.root
        while n != None:
            if n.key == k:
                return n.value
            elif n.key > k:
                n = n.left
            else:
                n = n.right
        return None

    def setVal(self, k, v):
        p = None
        n = self.root

        while n != None:
            p = n
            if n.key == k:
                n.value = v
                return
            elif n.key > k:
                n = n.left
            else:
                n = n.right

        e = BSTNode(k,v)
        if p == None:
            self.root = e
        elif p.key > k:
            p.left = e
        else:
            p.right = e

    def minKey(self):
        if self.isEmpty():
            return None
        else:
            n = self.root
            while n.left != None:
                n = n.left
            return n.key

    def size(self):

        def subtreeSize(n):
            if n == None:
                return 0
            else:
                return 1 + subtreeSize(n.left) + subtreeSize(n.right)

        return subtreeSize(self.root)

    def asList(self):

        def subtreeList(n):
            if n == None:
                return []
            else:
                return subtreeList(n.left) + [(n.key,n.value)] + subtreeList(n.right)

        return subtreeList(self.root)

    def asString(self):
        kvs = self.asList()
        if len(kvs) == 0:
            return "{}"
        else:
            s = "{"
            for kv in kvs[:-1]:
                s += repr(kv[0])+": "+repr(kv[1])+", "
            kv = kvs[-1]
            s += repr(kv[0])+": "+repr(kv[1])+"}"
            return s

    def __repr__(self):
        return self.asString()

    __str__ = __repr__

    def __bool__(self):
        return not self.isEmpty()

    def __contains__(self,k):
        return self.get(k) != None

    def __len__(self):
        return self.size()

    def __getitem__(self,k):
        return self.get(k)

    def __setitem__(self,k,v):
        return self.setVal(k,v)