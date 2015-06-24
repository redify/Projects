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
        
    def createAccount(self, name):
        self.accounts.append(Account.account(name))
        
    def createMovie(self, title):
        self.movies.append(Movie.movie(title))
        
    def checkMovie(self, name, movie): 
        
        for item in self.accounts:
            if item.getName() == name:
                break;
        
#         for account in self.accounts:
#             if account.getName() == name:
#                 account.

#         if self.accounts.contains(name, self.accounts.getName()):
#             pass
            
            
        index = self.accounts.index(account.getName())
             
        self.accounts[index].takeMovie()
        
    