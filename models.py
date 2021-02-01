from main import db

class User(db.Model):
    __tablename__="Users"
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.string(50), unique=false, nullable=False)
    Surname = db.Column(db.string(50), unique=false, nullable=False)
    DateofBirth = db.Column(db.string(50), unique=false, nullable=False)
    Residentialaddress = db.Column(db.string(50), unique=false, nullable=False)
    Nationality = db.Column(db.string(50), unique=false, nullable=False)
    NIN = db.Column(db.string(50), unique=false, nullable=False)

    def __repr__(self):
        return"<Register {}>".format(self.id)