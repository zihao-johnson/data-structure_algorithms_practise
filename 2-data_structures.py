''' concepts:

A. Abstract Data Type (ADT) : is theoretical concepts of data structure from user's view
   1. index-based list: i -- index, e -- element.
        a. size()
        b. isEmpty()
        c. get(i)
        d. set(i,e)
        e. add(i,e)
        f. remove(i)   
   2. positional list: p -- potion, e -- element.
        a. size()
        b. isEmpty()
        c. first()
        d. last()
        e. before(p)
        f. after(p)
        g. insertBefore(p,e)
        h. insertAfter(p,e)
        i. remove(p)
    
    Conclusion:
        all lists ADT type and their implementation could be used to structure data type (or ADT):
            a. Stack (LIFO)
            b. Queue (FIFO)
        with different rules applied on behaviors of naive lists
    
    3. Tree (abstract model of hierarchical data structure):
        traversal:
            1. post order
            2. pre order
            3. in order (for binary tree only)
            4. eular traversal (for binary tree only)

            a. get_root()
            b. get_leavesNodes()   external nodes compared to internal nodes
            c. get_ancestors(node)
            d. get_descenants(node)
            e. get_siblings(node)
            f. get_depth(node)
            g. get_height()
            h. get_level(integer)  return all nodes in level integer

B. Data Structure : concrete representation from implementer's view
   1. Array-based Lists --> see "array class"
        python has not arrary data type without libraries imported, it has only four built-in data type (list, tuple, set and dictionaries),
        from my understanding, python list is an array-based built-in data structure with much richer operations.
        python does not have any as pointers.
        class array is implemented by list with some of its built-in functions
   2. concrete data structure for positional list ADT:
    a. Singly Linked List --> see "linked_list class"
    b. Doubly Linked List --> see "linked_list class"   (same class but argu if_Doubly_linked indicates whether it is singly or doubly linked list)
    C. Notes, if the all argus {p,e} are given as the data that stored in nodes, the functions will noe be used and all functions will be run in O(n) if pointers are not given !

'''


# ----------B.1 array class----------
# I decide to practise it even useless lol...
class array:
    def __init__(self,list_data):
        self.data = list_data
    def size(self):
        return len(self.data)
    def get(self,i):
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:return self.data[i]
    def set(self,i,e):
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:self.data[i] = e
    def add(self,i,e): # python has insert(i,e) built-in function...
        # but maunally implement will be...:
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:
            list_temper = self.data[i:]
            self.data[i] = e
            for j,e in enumerate(list_temper):
                if i+1+j < self.size():
                    self.data[i+1+j] = e
                else: self.data.append(e)
            # time comlexity equals to theoretically shiftting elements to the left of element i down.  
    def remove(i):
        # python conveniently supports functions to remove from specific index of list:
        #   1. del list[i]
        #   2. list.pop(i)
        # but manually implement will be ...:
        if i > self.size() - 1 or i < 0:
            print("index out of range")
        else:
            for j,e in enumerate(self.data):
                if j >=i:
                    if j<self.size-1:
                        self.data[j] = self.data[j+1]
                    else:
                        del self.data[j]
    def isEmpty(self, absolutely = True):
        '''
            seems there is no any built-in function to check if a list contains values, if a list contains two empty list, check statement using if does not work (see test part t1)
        '''
        if absolutely == True: # list contains nothing, even empty lists
            if not self.data:
                return True
            else: return False
        if absolutely == False:
            return self.check_list_empty(self.data)
    
    def check_list_empty(self,data):
        # recursively checking...
        if type(data)!=type(["list_element_1","list_element_1"]):
            return False
        else:
            if not data:
                flag = True
            else:
                flags = [self.check_list_empty(e) for e in data]
                if flags.count(True) == len(data):
                    flag = True
                else : flag = False
            return flag

                
# ----------B.2.a singly linked list class----------
class LL_node():
    # Linked list element definition 
    def __init__(self, pre_node=None, next_node=None, if_head = False, if_Doubly_linked = False, data = None):
        # pointers is two element list if singly linked, else three elements list
        self.next_node = next_node
        self.if_Doubly_linked = if_Doubly_linked
        self.if_head = if_head
        if self.if_head==False:
            self.data = data
            if self.if_Doubly_linked == True:
                self.previous_node = pre_node

class linked_list():
    def __init__(self, nodes, if_Doubly_linked = False):
        # nodes is a list start with header node,
        # initially will linked all nodes in order.
        if len(nodes) == 0:
            print("warning: list's header and elements does not exist, the object does not represent a list. ")
            self.header = None
            self.nodes = nodes
            self.if_Doubly_linked = if_Doubly_linked
            self.size = 0  # size include header node
        elif nodes[0].if_head!=True:
            print("error: first node is not header, linked list creates UNsuccessfully !")
        else:
            self.header = nodes[0]
            self.nodes = nodes
            self.if_Doubly_linked = if_Doubly_linked
            self.size = 1  # size include header node
            for i in range(0,len(nodes)-1):
                nodes[i].next_node = nodes[i+1]
                self.size += 1
            if self.if_Doubly_linked == True:
                for i in range(1,len(nodes)):
                    nodes[i].pre_node = nodes[i-1]

    def get_size(self):
        if self.size ==0:
            print("list does not exist ! return ture")
            return self.size
        return self.size - 1  # not count header node

    def ifEmpty(self):
        if self.size ==0:
            print("list does not exist ! return ture")
            return True
        elif self.size ==1:
            return True
        else: return False
    
    def first(self):
        if type(self.header) != type(LL_node()):
            print("error: the linked list does not exsit, return None value !")
            return None
        elif self.header.next_node == None:
            print("warning: the linked list is empty, return header node !")
            return self.header
        return self.header.next_node
    
    def last(self):  
        if self.header==None:
            print("error: the linked list does not exsit, return None value !")
            return None
        elif self.header.next_node == None:
            print("warning: the linked list is empty, return header node value !")
            return self.header
        last = self.header
        for i in range(0,self.size):
            if last.next_node == None:
                return last
            last = last.next_node
    
    def after(self,p):
        try:
            return self.nodes[self.nodes.index(p)].next_node
        except:
            print('error: node "',p,'" does not exist in current list !')
    def before(self,p):
        try:
            self.nodes.index(p)
            if self.if_Doubly_linked == False:
                last = self.header
                for i in range(0,self.size):
                    if last.next_node==p:
                        return last
                    last = last.next_node
            else:
                return self.nodes[self.nodes.index(p)].pre_node
        except:
            print('error: node "',p,'" does not exist in current list !')
    
    def insertAfter(self,p,e):
        try:
            e.next_node = self.nodes[self.nodes.index(p)].next_node
            self.nodes[self.nodes.index(p)].next_node = e
            if self.if_Doubly_linked == True:
                e.pre_node = self.nodes[self.nodes.index(p)].next_node.pre_node
                self.nodes[self.nodes.index(p)].next_node.pre_node = e
            self.size += 1
            self.nodes.append(e)
        except:
            print('error: node "',p,'" does not exist in current list !')

    def insertBefore(self,p,e):
        try:
            self.nodes.index(p)
            if p ==self.header:
                print("error: cannot insert new node before the header node !")
            else:
                last = self.header
                for i in range(0,self.size):
                    if last.next_node==p:
                        e.next_node = last.next_node
                        last.next_node = e
                        break
                    last = last.next_node
                if self.if_Doubly_linked == True:
                    e.pre_node = self.nodes[self.nodes.index(p)].pre_node
                    self.nodes[self.nodes.index(p)].pre_node = e
                self.size += 1
                self.nodes.append(p)
        except:
            print('error: node "',p,'" does not exist in current list !')


    def remove(self,p):
        try:
            self.nodes.index(p)
            if p == self.header and self.size > 1:
                print("error: cannot remove header when list is not empty")
            
            elif self.size == 1:
                self.header = None
                self.size -= 1
                self.nodes.remove(p)
            else:    
                if self.if_Doubly_linked == False:
                    start = self.header
                    for i in range(0,self.size):
                        if start.next_node == p:
                            start.next_node = p.next_node
                            p.next_node = None
                else:
                    p.pre_node.next_node = p.next_node
                    p.next_node.pre_node = p.pre_node
                    p.next_node = None
                    p.pre_node = None
                self.size -= 1
                self.nodes.remove(p)
            if self.size == 0:
                self.get_size()
        except:
            print('error: node "',p,'" does not exist in current list !')
        
    def get_nodes_data(self):
        if self.size!=0:
            start = self.header
            to_return = ["header"]
            for i in range(0,self.size):
                start = start.next_node
                if start == None:
                    break
                to_return.append(start.data)
        return to_return
                
class tree_node():
    def __init__(self,data = None):
        self.parent = None
        self.data = data
        self.chind_nodes = []
class tree():
    def __init__(self):
        pass

# test...:

# ------------ t1
'''
list_test_1 = []
if not list_test_1:
    print("list_test_1 empty")
list_test_2 = [[],[]]
if not list_test_2:
    print("list_test_2 empty")
'''
# ------------ t2

#print(list1.after(list1_node4).data,"hree")

