class Book:
    '''
    Class: Book contains the detail of the books. It allows comparing 
    two instances accoring to the rank.
    for example b1 < b2 if  b1.rank < b2.rank 
    '''

    def __init__(self, key, title, group, rank, similar):
        self.key = key
        self.title = title
        self.group = group
        self.rank = int(rank)
        self.similar = similar

    def check(self, a):
        no = self.title.lower()
        noo = a.title.lower()
        for index in range(min(len(no), len(noo))):
            if no[index] != noo[index]:
                return index
        return -1

    def __lt__(self, a):
        '''
        This function allows to make direct comparation using the operator <
        '''
        # find when letters differ then compare those
        indo = self.check(a)
        return ord(self.title[indo]) < ord(a.title[indo])
        #return self.rank < a.rank

    def __le__(self, a):
        '''
        This function allows to make a direct comparation using the operator <=
        '''
        indo = self.check(a)
        return ord(self.title[indo]) <= ord(a.title[indo])


    def __gt__(self, a):
        '''
        This function allows to make direct comparation using the operator >
        '''
        indo = self.check(a)
        return ord(self.title[indo]) > ord(a.title[indo])
        #return self.rank > a.rank
    
    def __ge__(self, a):
        '''
        This function allows to make direct comparation using the operator >=
        '''
        indo = self.check(a)
        return ord(self.title[indo]) >= ord(a.title[indo])
    
    def __eq__(self, a):
        '''
        This function allows to make direct comparation using the operator ==
        '''
        return self.title.lower() == a.title.lower() and self.key == a.key
    
    def __str__(self):
        '''
        function returns a string containting the book information
        '''
        return f"\n\tBook: {self.key}\n\tTitle: {self.title}\n\tGroup: {self.group}\n\tRank: {self.rank}"
