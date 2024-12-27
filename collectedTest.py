import timeit
import matplotlib.pyplot as plt

test0 ="""
import concurrent.futures  #For bonus question

RL = 10 #Set row length

class WordSearch(object):  #Pass grid for instantiation

    def __init__(self, grid):

        self.grid = grid   
        self.h = set() #Containers for word search - h for horisontal words and v for vertical words. 
        self.v = set() #Note: these could have been declared in the "is_present" function, but I personally prefer declaring member variables here.      

    def is_present(self, word): 

         
        for i in range(0, len(self.grid), RL):
            row = self.grid[i:i + RL]
            for s in range(RL):
                if row[s] == word[0]:
                    for l in range(len(word) + 1): 
                        self.h.add(row[s:s + l])

        for i in range(RL):  
            column = ''.join(self.grid[j * RL + i] for j in range(RL))
            for s in range(RL):
                if column[s] == word[0]:
                    for l in range(len(word) + 1):
                        self.v.add(column[s:s + l])

        return word in self.h or word in self.v


grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

ws = WordSearch(grid_data)

wordsToFind = ["guy", "no", "fg", "hello", "aga", "fyo"]

for word in wordsToFind:
    if ws.is_present(word):
        print(f"found {word}")
"""

execT0 = timeit.timeit(test0, number = 100)
print(f'time was {execT0:.6f}')


test1 = """
import concurrent.futures  #For bonus question

RL = 10 #Set row length

class WordSearch(object):  #Pass grid for instantiation

    def __init__(self, grid):

        self.grid = grid   
        self.h = set() 
        self.v = set()    
          
        for i in range(0, len(self.grid), RL):
            row = self.grid[i:i + RL]
            for s in range(RL):
                for l in range(1, min(25, RL - s + 1)): 
                    self.h.add(row[s:s + l])

        for i in range(RL):  
            column = ''.join(self.grid[j * RL + i] for j in range(RL))
            for s in range(RL):
                for l in range(1, min(25, RL - s + 1)):
                    self.v.add(column[s:s + l]) 

    def is_present(self, word): 

        return word in self.h or word in self.v


grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

ws = WordSearch(grid_data)

wordsToFind = ["guy", "no", "fg", "hello", "aga", "fyo"]

for word in wordsToFind:
    if ws.is_present(word):
        print(f"found {word}")
"""

execT1 = timeit.timeit(test1, number = 100)
print(f'time was {execT1:.6f}')


test2 = """
import concurrent.futures  #For bonus question

RL = 10 #Set row length

class WordSearch(object):  #Pass grid for instantiation

    def __init__(self, grid):

        self.grid = grid   
        self.h = "" 
        self.v = ""  
          
        for i in range(0, len(self.grid), RL):
            row = self.grid[i:i + RL]
            self.h += row+"0"

        for i in range(RL):  
            column = ''.join(self.grid[j * RL + i] for j in range(RL))
            self.v += column+"0"

    def is_present(self, word): 

        return word in self.h or word in self.v


grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

ws = WordSearch(grid_data)

wordsToFind = ["guy", "no", "fg", "hello", "aga", "fyo"]

for word in wordsToFind:
    if ws.is_present(word):
        print(f"found {word}")
"""

execT2 = timeit.timeit(test2, number = 100)
print(f'time was {execT2:.6f}')


test3="""
import concurrent.futures  #For bonus question

RL = 10 #Set row length

class WordSearch(object):  #Pass grid for instantiation

    def __init__(self, grid):

        self.grid = grid   
        self.h = set() #Containers for word search - h for horisontal words and v for vertical words. 
        self.v = set() #Note: these could have been declared in the "is_present" function, but I personally prefer declaring member variables here.      

    def is_present(self, word): 

         
        for i in range(0, len(self.grid), RL):
            row = self.grid[i:i + RL]
            for s in range(RL):
                if row[s] == word[0]:
                    for l in range(len(word) + 1): 
                        self.h.add(row[s:s + l])

        for i in range(RL):  
            column = ''.join(self.grid[j * RL + i] for j in range(RL))
            for s in range(RL):
                if column[s] == word[0]:
                    for l in range(len(word) + 1):
                        self.v.add(column[s:s + l])

        return word in self.h or word in self.v


#Bonus question: multithreading
def search_parallel(ws, words_to_find):  #ws is a WordSearch object

    found = [] 
    exec = concurrent.futures.ThreadPoolExecutor() #For managing multiple threads
    futures = []  

    for word in words_to_find:
        futures.append(exec.submit(ws.is_present, word))    

    for i, future in enumerate(futures):
        if future.result():  
            found.append(words_to_find[i])  

    exec.shutdown()  

    return found


#For testing:
grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

ws = WordSearch(grid_data)

words_to_find = ["guy", "no", "fg", "hello", "aga", "fyo"]

found_words = search_parallel(ws, words_to_find)

for word in found_words:
    print(f"Found: {word}")
"""

execT3 = timeit.timeit(test3, number = 100)
print(f'time was {execT3:.6f}')


test4 = """
import concurrent.futures  #For bonus question

RL = 10 #Set row length

class WordSearch(object):  #Pass grid for instantiation

    def __init__(self, grid):

        self.grid = grid   
        self.h = set() 
        self.v = set()    
          
        for i in range(0, len(self.grid), RL):
            row = self.grid[i:i + RL]
            for s in range(RL):
                for l in range(1, min(25, RL - s + 1)): 
                    self.h.add(row[s:s + l])

        for i in range(RL):  
            column = ''.join(self.grid[j * RL + i] for j in range(RL))
            for s in range(RL):
                for l in range(1, min(25, RL - s + 1)):
                    self.v.add(column[s:s + l]) 

    def is_present(self, word): 

        return word in self.h or word in self.v


#Bonus question: multithreading
def search_parallel(ws, words_to_find):  #ws is a WordSearch object

    found = [] 
    exec = concurrent.futures.ThreadPoolExecutor() #For managing multiple threads
    futures = []  

    for word in words_to_find:
        futures.append(exec.submit(ws.is_present, word))    

    for i, future in enumerate(futures):
        if future.result():  
            found.append(words_to_find[i])  

    exec.shutdown()  

    return found


#For testing:
grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

ws = WordSearch(grid_data)

words_to_find = ["guy", "no", "fg", "hello", "aga", "fyo"]

found_words = search_parallel(ws, words_to_find)

for word in found_words:
    print(f"Found: {word}")
"""

execT4 = timeit.timeit(test4, number = 100)
print(f'time was {execT4:.6f}')


test5 = """
import concurrent.futures  #For bonus question

RL = 10 #Set row length

class WordSearch(object):  #Pass grid for instantiation

    def __init__(self, grid):

        self.grid = grid   
        self.h = "" 
        self.v = ""  
          
        for i in range(0, len(self.grid), RL):
            row = self.grid[i:i + RL]
            self.h += row+"0"

        for i in range(RL):  
            column = ''.join(self.grid[j * RL + i] for j in range(RL))
            self.v += column+"0"

    def is_present(self, word): 

        return word in self.h or word in self.v


#Bonus question: multithreading
def search_parallel(ws, words_to_find):  #ws is a WordSearch object

    found = [] 
    exec = concurrent.futures.ThreadPoolExecutor() #For managing multiple threads
    futures = []  

    for word in words_to_find:
        futures.append(exec.submit(ws.is_present, word))    

    for i, future in enumerate(futures):
        if future.result():  
            found.append(words_to_find[i])  

    exec.shutdown()  

    return found

    
#For testing:
grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

ws = WordSearch(grid_data)

words_to_find = ["guy", "no", "fg", "hello", "aga", "fyo"]

found_words = search_parallel(ws, words_to_find)

for word in found_words:
    print(f"Found: {word}")
"""

execT5 = timeit.timeit(test5, number = 100)
print(f'time was {execT5:.6f}')


x = ["WS1", "WS2", "WS3", "WS1_M", "WS2_M", "WS3_M"]
y = [execT0, execT1, execT2, execT3, execT4, execT5]

fig, ax = plt.subplots(figsize=(8, 6)) 

ax.bar(x, y, color = ["purple", "blue", "red", "pink", "cyan", "orange"])

ax.set_xticklabels(x)
ax.set_xlabel("Word search code")
ax.set_ylabel("Avaraged runtime over 100 runs (seconds)")

plt.tight_layout()
plt.show()