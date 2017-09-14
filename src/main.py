'''
Created on Sep 14, 2017

@author: jlearx
'''

import random

if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    # One line solution
    c = set(a) & set(b)
    print("Overlap:")
    print(c)
    
    # Randomly generate Lists
    print("Randomly generating lists...")
    a.clear()
    b.clear()
    seed = random.seed()
    
    # Populate A
    count = random.randint(1,100)
    a = random.sample(range(100), count)
    print("List a = ", end="")
    print(a)
    
    # Populate B
    count = random.randint(1,100)
    b = random.sample(range(100), count)
    print("List b = ", end="")    
    print(b)
    
    # Determine Overlapped
    # One line solution
    c = set(a) & set(b)
    print("Overlap:")
    print(c)
    