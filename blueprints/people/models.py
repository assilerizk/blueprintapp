from blueprintapp.app import db

class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    job = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<PERSON {self.name}, Age: {self.age}, Job: {self.job}>"

    def get_id(self):
        return self.pid
