import Book
import ArrayList
import ArrayQueue
#import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
import BinaryHeap
#import AdjacencyList
import MaxQueue
import time


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue() #MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                #self.bookIndices.add(key, self.bookCatalog.size() - 1)
                self.sortedTitleIndices.add(title, self.bookCatalog.size() - 1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s}) \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt : int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        cookieMonster123 = 0
        for penguin in self.bookCatalog:
            if infix in str(penguin.title):
                print(penguin)
                cookieMonster123 += 1
            if cookieMonster123 >= cnt:
                break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        '''
        getCartBestSeller: returns best-seller amongst the rest of the books in the cart
        '''
        print(f'getCartBestSeller returned')
        print(self.shoppingCart.max().title)
        return self.shoppingCart.max().title
    
    def addBookByKey(self, key):
        start_time = time.time()
        indicieisadiashujashdjkadsjhkl = self.bookIndices.find(key)
        if indicieisadiashujashdjkadsjhkl == None:
            print('Book not found.')
        else:
            ihukjfsdiuhjlnsfdijuohlsfdlhjiksfdwljhkn = self.bookCatalog.get(indicieisadiashujashdjkadsjhkl)
            self.shoppingCart.add(ihukjfsdiuhjlnsfdijuohlsfdlhjiksfdwljhkn)
            print(f'Added title: {ihukjfsdiuhjlnsfdijuohlsfdlhjiksfdwljhkn.title}')
        elapsed_time = time.time() - start_time
        print(f'addBookByKey Completed in {elapsed_time} seconds')

    def addBookByPrefix(self, prefix):
        book = self.sortedTitleIndices.find_smallest_greater_node(prefix)
        if book.k[0:len(prefix)] == prefix:
            if len(prefix) > 0:
                self.shoppingCart.add(self.bookCatalog.get(book.v))
                print("Added first matched title: " + book.k)
            else:
                print('Error: Prefix was not found.')
        else:
            print('Error: Prefix was not found.')
    
    def bestsellers_with(self, infix, structure, n):
        if n == '':     n = 0
        n = int(n)
        if infix == '': print('Invalid infix.')
        elif n < 0:     print('Invalid number of titles.')
        else:
            abcdefghijklmnopqrstuvwxyz = time.time()
            if structure == '1':
                BS = BinarySearchTree.BinarySearchTree()
                for goo in self.bookCatalog:
                    if infix in goo.title:
                        BS.add(goo.rank, goo)
                yeets = BS.in_order()
                yeets.reverse()
                for yoot, yeet in enumerate(yeets):
                    if yoot >= n and n > 0:
                        break
                    print(yeet.v)
            elif structure == '2':
                BS = BinaryHeap.BinaryHeap()
                for goo in self.bookCatalog:
                    if infix in goo.title:
                        goo.rank *= -1
                        BS.add(goo)
                for _ in range(BS.size()):
                    if _ >= n and n > 0:
                        break
                    yo = BS.remove()
                    yo.rank *= -1
                    print(yo)
            else:   print('Invalid data structure.')
            yo0123456789101112231415161718192021 = time.time() - abcdefghijklmnopqrstuvwxyz
            print(f'Displayed bestsellers_with({infix}, {structure}, {n}) in {yo0123456789101112231415161718192021} seconds')