from psc_app import psc_db, app
from psc_app.users import user_constants as USER



class User(psc_db.Model):
    id = psc_db.Column(psc_db.Integer, primary_key = True)
    username = psc_db.Column(psc_db.String(64), index = True, unique = True)
    email = psc_db.Column(psc_db.String(120), index = True, unique = True)
    password = psc_db.Column(psc_db.String(20))
    role = psc_db.Column(psc_db.SmallInteger, default=USER.GUEST)
    description = psc_db.Column(psc_db.String(500))
    posts = psc_db.relationship('Post', backref = 'author', lazy = 'dynamic')
    homepage = psc_db.Column(psc_db.String(80))
    zodiac = psc_db.Column(psc_db.SmallInteger)
    profile_pic = psc_db.Column(psc_db.String(120))

        
    def is_authenticated(self):
        return True
        
        
        
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
        
    def getRole(self):
        return USER.ROLE[self.role]
        
    def getZodiac(self):
        return USER.ZODIAC[self.zodiac]
        
    def __repr__(self):
        return '<User %r>' % (self.username)
        
    def get_id(self):
        return unicode(self.id)

