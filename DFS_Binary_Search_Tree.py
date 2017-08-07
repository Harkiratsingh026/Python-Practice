class node:
    def __init__(self,data):
        self.value=data;
        self.count=0;
        self.left=None;
        self.right=None;

class Tree:
    def __init__(self):
        self.head=None;

    def search(self,node,data):
        count=0;
        while(node is not None):
            if (node.value==data):
                count=1;
            elif(data<node.value):
                node=node.left;
            elif(data>node.value):
                node=node.right;
            if(count==1):
                print("Value Found");
                return;
        print("Value Not Found");
            
        

    def add(self,data):
        newnode=node(data);
        hd=self.head;
        if(self.head is None):
            self.head=newnode;
            self.head.count+=1;
            return;
        while(True):
            if(data<hd.value):
                if(hd.left is not None):
                    hd=hd.left;
                else:
                    hd.left=newnode;
                    hd.left.count=1;
                    return;
            elif(hd.value==data):
                hd.count+=1;
                return;
            else:
                if(hd.right is not None):
                    hd=hd.right;
                else:
                    hd.right=newnode;
                    hd.right.count=1;
                    return;
                    
    def preorder(self,node):
        if(node is None):
            return;
        print(node.value,node.count);
        Tree.preorder(self,node.left);
        Tree.preorder(self,node.right);

    def inorder(self,node):
        if(node is None):
            return;
        Tree.inorder(self,node.left);
        print(node.value,node.count);
        Tree.inorder(self,node.right);

    def postorder(self,node):
        if(node is None):
            return;
        Tree.postorder(self,node.left);
        Tree.postorder(self,node.right);
        print(node.value,node.count);
            
                

if __name__=='__main__':
    bst=Tree();
    bst.add(5);
    bst.add(3);
    bst.add(4);
    bst.add(2);
    bst.add(10);
    bst.add(10);
    bst.add(5);
    print("Pre-Order Traversal:");
    bst.preorder(bst.head);
    print("In-Order Traversal:");
    bst.inorder(bst.head);
    print("Post-Order Traversal:");
    bst.postorder(bst.head);
    a=int(input("Enter the Value You want to search:"));
    bst.search(bst.head,a);
    
