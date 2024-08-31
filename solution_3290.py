class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self, key):
        self.key = key

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()

    def insert_left(self, new_node):
        self.left = new_node

    def insert_right(self, new_node):
        self.right = new_node

    def search(self, key):
        if self.key == key:
            return self
        if self.left is not None:
            temp =  self.left.search(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp =  self.right.search(key)
            return temp
        return None

    def print_left_boundary(self):
        current = self
        while True:
            if current.left is not None:
                print(current.key, end=' ')
                current = current.left
            elif current.right is not None:
                print(current.key, end=' ')
                current = current.right
            else:
                break

    def print_right_boundary(self):
        if self.right is not None:
            self.right.print_right_boundary()
            print(self.key, end=' ')
        elif self.left is not None:
            self.left.print_right_boundary()
            print(self.key, end=' ')


    def print_leaves(self):
        if self.left is not None:
            self.left.print_leaves()
        if self.right is not None:
            self.right.print_leaves()
        if (self.left is None
            and self.right is None):
            print(self.key, end=' ')

    def print_border(self):
        print(self.key, end=' ')
        if self.left is not None:
            self.left.print_left_boundary()
            self.left.print_leaves()
        if self.right is not None:
            self.right.print_leaves()
            self.right.print_right_boundary()


btree = None

print('Menu (this assumes no duplicate keys)')
print('insert <data> at root')
print('insert <data> left of <data>')
print('insert <data> right of <data>')
print('border')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        new_node = BinaryTree(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
                btree = new_node
        else:
            position = do[4].strip().lower()
            key = int(position)
            ref_node = None
            if btree is not None:
                ref_node = btree.search(key)
            if ref_node is None:
                print('No such key.')
                continue
            if suboperation == 'left':
                ref_node.insert_left(new_node)
            elif suboperation == 'right':
                ref_node.insert_right(new_node)

    elif operation == 'border':
        if btree is not None:
            print('Border of tree: ')
            btree.print_border()
            print()

    elif operation == 'quit':
        break