'''
stack in / out scheduling
'''

import copy
class Stack_simulation:
    
    def __init__(self, elements):
        self.buff_stack = elements
        self.__stack = elements
        self.__step_list = []
        self.solutions = []
    

    def build_result(self):
        
        solution = self.test(0,[])
        return solution

    def test(self, element_index, stack):
        
        # 0. get element:
        element = self.__stack[element_index]

        if element_index < len(self.__stack)-1:
            element_index += 1
            solution = []
            # 1. in
            stack.append(element)

            x = copy.deepcopy(stack)
            solutions = self.test(element_index, x)
            
            solution.extend(solutions)
            seq = []
            while stack:
                # 2
                # 2.1 element in but did not out yet:
                
                # 2.2 element out immediately after in
                
                seq.append(stack.pop())
                x = copy.deepcopy(stack)
                solutions = self.test(element_index, x)
                for e in solutions:
                    x = copy.deepcopy(seq)
                    x.extend(e)
                    solution.append(x)
            return solution
        else:
            element = self.__stack[element_index]
            stack.append(element)
            solution = [e for e in reversed(stack)]
            return [solution]
            




sample = Stack_simulation([1,2,3,4])
youguess = sample.build_result()
print((youguess))
