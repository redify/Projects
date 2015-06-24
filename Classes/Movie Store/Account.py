class account:
    """
    This class will track the movies checked out and overdue fees related to the given account owner
    """
    
    def __init__(self, name):
        self.name = name
        self.fees = 0;
        self.checked_movies = []
        
    def getName(self):
        return self.name
        
    def takeMovie(self, movieTitle):
        pass