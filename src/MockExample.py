class DB:
    def __init__(self):
        pass
    def persist(self,person):
        pass



class Person:
    def __init__(self,name,db):
        self.name = name
        self.db = db

    def save(self):
        self.db.persist(self)