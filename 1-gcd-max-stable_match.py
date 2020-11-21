#------------------- week 1: introduction to algorithm.-----------------------------------------------
'''Learning notes : 
(running time is generally used to describe how long does an algorithm solve problems, will be covered in detial next week)

    Effcient algorithm:
        1. Low polynomial running time.
        2. Exponential running times are infesible except for small problem or carefuuly designed algorithm.
        3. Solve general problems
    
    Design algorithms (3 steps):
        1. Describe it
            use plain English and optionally with pseudocode or figures
        2. Argue correctness
            generally approved
        3. Analysis running time

    Pseudocode:
        1. if ... then ...[else] (condition statements)
        2. while ... do ...
           for ... do ...
           repeat ...  until     (loop statements)
        3. method declaration

            def method(arg[,arg...])
                input ...
                output ...
        4. remeber to use indentation to replace braces

    Problems:
        1. Greatest Common Divisor (GCD) --> gcd(a,b)
        2. Find Maximum value of an array of integers --> max_value(array)
        3. Stable matching --> stable_match(dict_1,dict_2)
            3.1 extensions: stable roommate problem
            3.2 matching residents to hospital
                Variant 1, Some participants declare unacceptable list
                Variant 2, Unequal number of hospital and residents
                Variant 3, Limited polygamy (a hospital wants 3 residents)

''' 
# Implementation of Problems:
def gcd(a, b) ->int:
    '''gcd: (greatest common divide - 两数的最大公约数)
            Divides operation in plain English:
                "2 divides into 6 exactly 2 times" or "6 divided by 2 is 3"
            
            Solution: 
                Euclid's algorithm, based on principle that 
                GCD does not change if the larger number is replaced by its difference with the smaller number.
                
                see we have two integers 'a', 'b' ('a' > 'b'),  assume 'a' consists of 'n' times 'b' with a remainder of 'c'
                and 'c' consistes of 'm' times 'b' with no remainder. 'c' is the GCD of 'a' and 'b', 
                where 'c' * 'm' = 'b', 'c' * ( 1 + 'm' * 'n' ) = 'a'

                pesudocode (from lecture):
                    def gcd (a,b)
                        if b= 0 then
                            return a
                        else
                            return gcd(b, a mod b)
                a mod b is the remainder of a divided by b

        inputs:
            int a > int b
        return:
            int GCD 
    '''
    if int(a) != a or int(b) != b:
        print("Error: args are not integer: ", a, ", ",b)
    else:
        if b == 0:
            return a
        else: return gcd(b, a%b)


def max_value(A) -> int:
    '''find max value
            pesudocode (from lecture):
                def max(A)
                    max <-- A[0]
                    for i <-- 1, i < length(A), i++ do
                        if A[i] > max then
                            max <-- A[i]
        input:
            an int array
        return:
            max value of the array
    '''
    max = A[0]
    for i in range(1,len(A)):
        max = A[i] if A[i] > max else max
    return max


def stable_match(dict1,dict2) ->list:
    '''Stable matching problem:
            take men and women's perferance table and return a man-woman pair list.
            meets no pair is unstable pair.

            unstable pair (block pair): 
                when man A and woman a prefer each other than their currently assigned woman b and man B.
                pair (A,a) is a block pair.
            
            see example:
                A likes a than b        a likes A than B
                B likes a than b        b likes A than B
                matching pairs (A,b) and (B,a) where A and a is unstable and the pair (A,a) is a block pair
            
            obersivations:
                there are only four type of pair: 
                    1> man and weman prefer each than other. 
                    2> man prefer others than his partner. 
                    3> weman prefer others than her partner.
                    4> both prefer others than theiir partner.
                    think that if all men got his most prefered, avaliable partner:
                        no weman can elope with man that she prefers because men prefer their partner than woman wanted to elope with him.
                    or all women got his most prefered, avaliable partner:
                        no man can elope with woman that he prefers because women prefer their partner than man wanted to elope with her.
            
            solution: (Gale Shapley algorithm or propose-and-reject algorithm) 
                      with  time complexity as O(n**2).

        inputs:
            dict_1 and dict_2, both of them are dict with values as preference list
            e.g. {A:[a,b,c],B:[b,c,a],C:[a,c,b]} where A prefer c > b > a (perfered reversed)
        return:
            list of stable pairs, 1-d list
    '''
    # initialization
    #------------------------ does not need when performing man-optimal assignment ------------------------
    #men_partners = {}
    #for key in dict1:
    #    men_partners[key] = 0

    #------------------------ does not need when performing woman-optimal assignment ------------------------
    women_partners = {}  ## used to record women's partners, will be changed if women are proposed by their more prefered man than current partner 
    for key in dict2:
        women_partners[key] = 0

    unmatched_men = []  ## used to record unmatched men for looping, programming will end if this list has no element.
    for key in dict1:  
        unmatched_men.append(key)

    for k, v in dict2.items(): # add index information for each elements to indicates the prefered level
        temp = {}
        for i,e in enumerate(v):
            temp[e] = i
        dict2[k] = temp

    # Gale Shapley algorithm:    
    while len(unmatched_men)!=0:
        unmatched_man = unmatched_men[-1] # get last man from unmatched man list
        man_prefer_list = dict1[unmatched_man] # get the man's preference list
        while len(man_prefer_list) != 0:    # loop woman in preference list, notes that preference list is reserved when input in as an arg
            woman = man_prefer_list[-1]     # get weman's name
            woman_partner = women_partners[woman] #get weman's current partner (0 or name str)
            if woman_partner != 0:
                if dict2[woman][woman_partner] < dict2[woman][unmatched_man]:
                    women_partners[woman] = unmatched_man # updates weman's parter
                    del unmatched_men[-1] # delete the new man from unmatched men list
                    unmatched_men.append(woman_partner) # set forsaken man as unmatched by add him into unmatched men list
                    del dict1[unmatched_man][-1] # delete women from man's preference list
                    break
                else:
                    del dict1[unmatched_man][-1] # delete women from man's preference list
                    pass
            else:
                women_partners[woman] = unmatched_man
                del unmatched_men[-1] # delete the new man from unmatched men list
                del dict1[unmatched_man][-1] # delete women from man's preference list
                break
    return women_partners
    
    
    
# Run functions:
#print(gcd(270,192))
#print(max_value([8,1,6,-1,9,0]))

dict1 = {"X":["C","B","A"],"Y":["C","A","B"],"Z":["C","B","A"]}
dict2 = {"A":["Z","X","Y"],"B":["Z","Y","X"],"C":["Z","Y","X"]}
print(stable_match(dict1,dict2))