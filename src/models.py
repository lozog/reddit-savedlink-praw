from src import db

class SavedLink(db.Model):
    id       = db.Column(db.Integer, primary_key =True)
    fullname = db.Column(db.String(12),  index = True, unique = True)
    title    = db.Column(db.String(120), index = True, unique = True)
    url      = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return '<SavedLink %r: %r>' % (self.fullname, self.title)
