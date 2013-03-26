from psc_app import psc_db, app
from psc_app.zodiac import zodiac_constants as SIGN



class Zodiac(psc_db.Model):
    id = psc_db.Column(psc_db.Integer, primary_key = True)
    timestamp = psc_db.Column(psc_db.DateTime)
    body = psc_db.Column(psc_db.String())
    sign = psc_db.Column(psc_db.SmallInteger)



    def __repr__(self):
        return '<Zodiac %r ni %r>' % (self.sign, self.timestamp)

