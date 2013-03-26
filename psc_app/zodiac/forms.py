from flask.ext.wtf import Form, TextField, SelectField, TextAreaField
from flask.ext.wtf import Required, NumberRange


    
class ZodiacForm(Form):

    body = TextAreaField('body', [Required(message="write some stupid title")],                   
                                    #delete next line in production
                                    default = "shithead"
                                    )
'''    sign = SelectField('category',choices = [
                                    ('0', 'Aries'),
                                    ('1', 'Taurus'),
                                    ('2', 'Gemini'),
                                    ('3', 'Cancer'),
                                    ('4', 'Leo'),
                                    ('5', 'Virgo'),
                                    ('6', 'Libra'),
                                    ('7', 'Scorpio'),
                                    ('8', 'Sagitarius'),
                                    ('9', 'Capricorn'),
                                    ('10','Aquarius'),
                                    ('11','Pisces')
                                    ])
    
'''

