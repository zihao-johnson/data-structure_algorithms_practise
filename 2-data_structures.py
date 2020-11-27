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
    '''
        thought to use undrescores to mongle elements to let variables as like "private",
        but it can be still accessed
    '''
    def __init__(self,data = None, if_root = False):
        self.__data = data
        self.__child_nodes = []
        self.__if_root = if_root
        if not self.__if_root:
            self.__parent = None
        
    def get_data(self):
            return self.__data
    def get_childs(self):
            return self.__child_nodes
    def add_child(self,node):
            self.__child_nodes.append(node)
    def del_child(self,node):
            try:
                self.__child_nodes.remove(node)
            except:print("Node being deleted is not child of the current node !")
    def set_parent(self,node):
            if self.__if_root:
                print("Warning, adding parent to current root node, it and its descendants will be a descendants tree the parent")
                self.__parent = node
                self.__if_root = False
            else:
                self.__parent = node
    def get_parent(self):
            if self.__if_root:
                print("Root node has not parent !")
            elif self.__parent==None:
                print("Node has not been assigned with parent yet !")
            else:
                return self.__parent
            
class tree():
    def __init__(self, if_subtree = False, if_binary_tree =  False):
        self.__root = tree_node(if_root=True)
        self.__tree_nodes = []
        self.__if_subtree = if_subtree
        self.__if_binary_tree = if_binary_tree
        # as the tree stucture is not simple as lists that can be easily linked when initiation
        # the relations between them has to be added manually
    
    def root(self):
        return self.__root
    
    def get_all_nodes(self):
        return [self.__root] + self.__tree_nodes 
    
    def add_node(self,node,parent):
        # add node in the tree as child of parent:
        if node == parent:
            print("cannot add a node as the cild of itself !")
        else:
            its_descandents = self.__pre_order(node = node)
            try:
                its_descandents.index(node)
                try:
                    if parent != self.__root:
                        self.__tree_nodes.index(parent)     
                    node.set_parent(parent)
                    parent.add_child(node)
                    self.__tree_nodes.append(node)
                except:print("New node adding failed, parent node does not exist in the tree !")
            except:print("Cannot add a node as the child of its current descandents node !")
    def del_node(self,node):
        try:
            self.__tree_nodes.remove(node)
            node.get_parent().del_child(node)
            node.set_parent(None)
            # get and del all child nodes of the relevant node
            nodes = self.__pre_order(node)
            for node in nodes:
                try:
                    self.__tree_nodes.remove(node)
                except: pass 
        except:
            print("node is not in the tree")
    # Traversal methods:
    
    def __pre_order(self, node = None, action_func = None, args = []):
        if node ==None:
            node = self.__root
        # restructure action functions:
        temper_args = args
        for i,a in enumerate(args):
            if args == "infunction_node":
                temper_args[i] = node
        
        if action_func !=None:        
            action_func(temper_args)
        nodes_buffer = [node]
        childs = node.get_childs()
        for c in childs:
            nodes_buffer += self.__pre_order(c,action_func,args)
            if action_func !=None:    
                action_func(temper_args)
        return nodes_buffer
    
    def __post_order(self, node = None, action_func = None):
        if node == None:
            node = self.__root
        nodes_buffer = []
        childs = node.get_childs()
        for c in childs:
            nodes_buffer += self.__post_order(c)
        nodes_buffer += [node]

        return nodes_buffer

    def __in_order_main(self,node = None,action_func = None):
        if node ==None:
            node = self.__root
        if self.__if_binary_tree:
            nodes = self.__in_order(node,action_func)
            return nodes
        else:
            print("Sorry, In-order Traversal cannot be used in non-binary tree !")
    def __in_order(self, node=None, action_func = None):
        nodes_buffer = []

        '''
            first element of the childs of the node will be the left, and second is right by default.
        '''
        childs = node.get_childs()
        nodes_buffer = []
        if len(childs)==0:
            nodes_buffer +=[node]
        else:
            nodes_buffer += self.__in_order(childs[0])
            nodes_buffer +=[node]
            if len(childs)==2:
                nodes_buffer += self.__in_order(childs[1])
        return nodes_buffer

    # Eular Traversal:
    # currently print nodes data along traversal path on the console 
    def eular_traversal(self, node, travel_method = None):
        travel_method(node,self.print_node_data,["infunction_node"])
    def print_node_data(self,node):
        print(node[0].get_data())
        
# test...:

# ------------ t1:
'''
list_test_1 = []
if not list_test_1:
    print("list_test_1 empty")
list_test_2 = [[],[]]
if not list_test_2:
    print("list_test_2 empty")
'''
# ------------ t2:
'''
class test():
    def __init__(self):
        pass
    def __data(self):
        return 1
    def inner_get(self):
        return self.__data()

test = test()
print(test._test__data())
print(test.inner_get())
print(test.__data())
'''
# ------------ t3:
"""def func1():
    print("1")

def func2():
    print("2")

def func_print(x):
    print("value of x: ",x)

def main_func(funcs = None, args = ()):
    for i in range(0,3):
        funcs(i)
x = "this is perfect"
main_func(funcs=func_print,args = (x))"""

test = tree(if_binary_tree = True)
test_node_1 = tree_node(data = 1)
test_node_2 = tree_node(data = 2)
test_node_3 = tree_node(data = 3)
test.add_node(test_node_1,test.root())
test.add_node(test_node_2,test.root())
test.add_node(test_node_3,test_node_2)
x = test.get_all_nodes()
print(x)
x = test._tree__pre_order()
print(x)
x = test._tree__post_order()
print(x)
x = test._tree__in_order_main()
print(x)
test.del_node(test_node_2)
x= test.get_all_nodes()
print(x)
# did not finished, add a node to its child