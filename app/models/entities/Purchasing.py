import datetime

class Purchasing():

    def __init__(self, uuid, book, user, date = None):
        self.uuid = uuid
        self.book = book
        self.user = user
        self.date = date
    
    def formatted_date(self):
        return datetime.datetime.strftime(self.date, '%d/%m/%Y - %H:%M:%S')