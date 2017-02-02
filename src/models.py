from src import db

class SavedLink(db.Model):
    id           = db.Column(db.Integer, primary_key =True)
    fullname     = db.Column(db.String(12),  index = True, unique = False)
    kind         = db.Column(db.String(2),   index = True, unique = False)
    title        = db.Column(db.String(120), index = True, unique = False)
    url          = db.Column(db.String(512), index = True, unique = False)
    thumbnail    = db.Column(db.String(512), index = True, unique = False)
    subreddit    = db.Column(db.String(120), index = True, unique = False)
    subreddit_id = db.Column(db.String(120), index = True, unique = False)

    def __repr__(self):
        return '<SavedLink %r: %r>' % (self.fullname, self.title)
