


"""
Top-down design: you start by describing your solution in English and then mark the phrases that correspond directly to python statements
Those that don't correspond are then rewrtten in more detail in English , until everything in your description can be written in python 


Programmers(good programmers, at least) deal with it by testing their code as they write it. 


use programming terms when describing the algorithm in English 


"""


#first Algorithm 

def find_two_smallest(L):
    
    """
    (list of float) -> tuple of (int, int)
    Return a tupple of the indices of the two smallest values in list L

    find_two_smallest([809, 834,477,478,307,122,96,102,324,476])
    (6,7)
    """
    #find the index of the minimum item in L 
    #Remove that item from the list 
    #Find the index of the new minimum item in the list
    #Put the smallest item back in the list 
    #If necessary, adjust the second index
    # Return the two indices 

    """
    Find the index of the minimum item in L we skim the output produced by help(list)
    No method that does that. we refine it 
    """
    
     #Get the minimum item in L
     #Find the index of that minimum item 
     #Remove that item from the list
     #Find the index of the new minimum item in the list
     #Put the smallest item back in the list 
     #If necessary, adjust the second index
     # Return the two indices
     
     #find the index of the minimum and remove that item 
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

     #Find the index of teh new minimum 
    next_smallest = min(L)
    min2 = L.index(next_smallest)
     
     #Put the smallest item back in the list 
     #If necessary, adjust the second index
     #Return the twwo indices

     #Put smallest back into L 
    L.insert(min1, smallest)

     #Fix min2 in case it was affected by the reinsertion 

    if min1 <= min2:
        
        min2 += 1


    return (min1, min2)



def find_two_smallest_V2(L):
    """
    """
    #sort a copy L 
    #Get the two smallest numbers 
    #Find their indices in the orginal list L 
    # Return the two indices 

    #Get a sorted copy of teh list so that the two smallest items are at the front 

    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    #Find their indices in teh original list L 
    #Return the two indices 
    #Find the indices in teh original list L 

    min1 = L.index(smallest)
    min2 = L.index(next_smallest)

    return (min1, min2)






def find_two_smallest_V3(L):
    
    
   # Set min1 and min2 to teh indicies of teh smallest and next-smallest
   #values at teh begining of L 

    if L[0] < L[1]:
     
        min1,min2 = 0,1

    else: 
        min1, min2 = 1,0 

    #Examine each value in the list in order 
    
    for i in range(2, len(L)):
        #New smallest?
        if L[i] < L[min1]:
            min2 = min1
            min1 = i 
        #New second samllest?

        elif L[i] < L[min2]:
            min2 = i 

    return (min1, min2)



if __name__ == '__main__':
    L = [809, 834,477,478,307,122,96,102,324,476]
    print(find_two_smallest(L))
    print(find_two_smallest_V2(L))
    print(find_two_smallest_V3(L))


