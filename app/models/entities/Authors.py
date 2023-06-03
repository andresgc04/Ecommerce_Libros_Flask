class Authors():

    def __init__(self, author_id, last_names, names, date_birth = None):
        self.author_id = author_id
        self.last_names = last_names
        self.names = names
        self.date_birth = date_birth

    def full_name(self):
        return '{0}, {1}'.format(self.last_names, self.names)