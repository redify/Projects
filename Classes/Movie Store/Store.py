import Account
import Movie

import Movie, Account

class store:
    """
    This class will manage all the accounts and movies.
    
    Account will check out a movie.  The movie will be assigned a return date.
    New accounts can be created.
    
    Movies will be created at init.
    """
    
    def __init__(self):
        self.movies = []
        self.accounts = []
    
    def findAccount(self, name):
        account = [account for account in self.accounts if account.getName() == name]
        
        if account == []:
            raise LookupError("Account name not found: {0}".format(name))
        
        return account[0]
    
    def findMovie(self, title):
        movie = [movie for movie in self.movies if movie.getTitle() == title]
        
        if movie == []:
            raise LookupError("Movie title not found: {0}".format(title))
        
        return movie[0]
        
    def createAccount(self, name):
        
#         if self.findAccount(name) is not None:
#             raise ValueError("Account with name already exist.")
        
        self.accounts.append(Account.account(name))
        
    def createMovie(self, title):
        
#         if self.findMovie(title) is not None:
#             raise ValueError("Movie title already exist.")
        
        self.movies.append(Movie.movie(title))
    
        
    def checkMovie(self, acc_name, mov_title): 
        """
        This is a pretty docstring...
        """       
        
        account = self.findAccount(acc_name)
        movie = self.findMovie(mov_title)
        
        account.takeMovie(movie)
        movie.setReturnDate(10301987) #random return date for now
        
    def dumpAccountInfo(self, acc_name):
        
        account = self.findAccount(acc_name)
        
        print("Account name: {0}".format(account.getName()))
        
        
        
            