class movie:
    """
    movie will track if it is checked out and when it's return date is.
    """
    
    def __init__(self, title):
        self.checked = False
        self.return_date = None
        self.title = title
    
    def getTitle(self):
        return self.title
    
    def setReturnDate(self, date):
        self.return_date = date #lets standardize this as monthdayyear (10301987)