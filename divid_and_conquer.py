'''
1. binary search
'''
def binary_search(st,l):
    index = -1

    if l:
        left_bound = 0
        right_bound = len(l) -1
        middle_index = len(l)//2
        while True:
            if ord(l[middle_index]) > ord(st):
                right_bound = middle_index
                if middle_index - left_bound < 2:
                    if ord(l[left_bound]) < ord(st):
                        index = middle_index
                    else:
                        index = left_bound
                    break
            elif l[middle_index] == st:
                index = middle_index
                break
            else:
                left_bound = middle_index
                if right_bound - middle_index < 2:
                    if ord(l[right_bound]) > ord(st):
                        index = right_bound
                    else:
                        index = right_bound + 1
                        ## python support to insert element at the end of the list by specify insert(index,element) as long as index is bigger than length of the list
                        ## otherwise can use string as a signal to notify all elements in current list are less than element to be inserted
                        ## e.g.
                        ## index = "inserted element is bigger than all others"
                        ## then use condition statement to take control.
                    break
            
            middle_index = (right_bound - left_bound)//2 + left_bound
    return index



'''
2. insert sort
'''
def insert_sort(string, reverse = False):
    return_list = []
    for e in string:
        print(return_list)
        print(e)
        insert_index = binary_search(e,return_list)
        return_list.insert(insert_index,e)
    if reverse == True:
        temp = []
        for e in return_list:
            temp.insert(0,e)
        return_list = temp
    return "".join(return_list)


print(insert_sort("98563589654hsijaADFA"))
