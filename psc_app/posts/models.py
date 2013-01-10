from psc_app import psc_db, app
from psc_app.posts import category_constants as CATEGORY

class Post(psc_db.Model):
    id = psc_db.Column(psc_db.Integer, primary_key = True)
    title = psc_db.Column(psc_db.String(140), index = True)
    timestamp = psc_db.Column(psc_db.DateTime)
    image = psc_db.Column(psc_db.String())
    user_id = psc_db.Column(psc_db.Integer, psc_db.ForeignKey('user.id'))
    body = psc_db.Column(psc_db.String())
    category = psc_db.Column(psc_db.SmallInteger, default = CATEGORY.NEWS)
    
    
    def __repr__(self):
        return '<Post %r>' % (self.body)
    
    def getCategory(self):
        return CATEGORY.TYPE[self.category]
