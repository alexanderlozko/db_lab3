from app import db

class Brand(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    year = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<{}>'.format(self.name)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    brand = db.Column(db.String(64), db.ForeignKey('brand.name'))

    def __repr__(self):
        return '<{}>'.format(self.name)