class node:
    def __init__(self,data):
        self.value=data;
        self.next=None;

class Linked_List:
    def __init__(self):
        self.head=None;

    def insertnode(self,data):
        last=self.head;
        nnode=node(data);
        if(self.head==None):
            self.head=nnode;
            return

        while(last.next):
            last=last.next;

        last.next=nnode;

    def printall(hd):
        last=hd.head;
        if(hd.head!=None):
            while(last!=None):
                print(last.value);
                last=last.next;
    def merge(h1,h2):
        c=0;
        head1=h1.head;
        head2=h2.head;
        mergelist=Linked_List();
        mainhead=mergelist.head;
        if(head1==None and head2==None):
            print("Both Linked List EMPTY!")
            return
        elif(head1==None):
            mergelist.head=head2;
            print("1st Linked List EMPTY");
        elif(head2==None):
            mergelist.head=head1;
            print("2nd Linked List EMPTY");
        else:
            while(head1 is not None and head2 is not None):
                if(head1.value<=head2.value):
                    c+=1;
                    if(c==1):
                        mainhead=head1;
                        head1=head1.next;
                        mergelist.head=mainhead;
                    else:
                        mainhead.next=head1;
                        mainhead=mainhead.next;
                        head1=head1.next;
                        
                elif(head1.value>head2.value):
                    c+=1;
                    if(c==1):
                        mainhead=head2;
                        head2=head2.next;
                        mergelist.head=mainhead;
                    else:
                        mainhead.next=head2;
                        mainhead=mainhead.next;
                        head2=head2.next;
            if(head1 is not None):
                mainhead.next=head1;
            if(head2 is not None):
                mainhead.next=head2;
        Linked_List.printall(mergelist);
        

            
if __name__=='__main__':
    llist=Linked_List();
    llist1=Linked_List();
    llist.insertnode(1);
    llist.insertnode(1);
    llist1.insertnode(1);
    
    Linked_List.merge(llist,llist1);
    

