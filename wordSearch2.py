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


#For testing
#grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

#ws = WordSearch(grid_data)

#wordsToFind = ["guy", "no", "fg", "hello", "aga", "fyo"]

#for word in wordsToFind:
    #if ws.is_present(word):
        #print(f"found {word}")


#For testing multithreading:
#grid_data = 'adfguytnoighytuiopnh' * (RL * RL // 20)  

#ws = WordSearch(grid_data)

#words_to_find = ["guy", "no", "fg", "hello", "aga", "fyo"]

#print("Starting search")
#found_words = search_parallel(ws, words_to_find)

#for word in found_words:
    print(f"Found: {word}")