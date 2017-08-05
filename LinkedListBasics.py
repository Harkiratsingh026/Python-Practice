class node:
    def __init__(self,data):
        self.val=data;
        self.next=None;

class Linked_List:
    def __init__(self):
        self.head=None;

    def insert_at_end(self,data):
        nnode=node(data);
        last=self.head;

        if(self.head==None):
            self.head=nnode;
            return;
        while(last.next):
            last=last.next;
        last.next=nnode;

    def printall(self):
        last=self.head;
        if(self.head!=None):
            while(last!=None):
                print(last.val);
                last=last.next;
            

if __name__=='__main__':
    llist=Linked_List();
    llist.insert_at_end(2);
    llist.insert_at_end(2);
    llist.insert_at_end(2);
    llist.insert_at_end(2);
    llist.printall();
    
    
