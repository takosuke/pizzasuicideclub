from flask.ext.wtf import Form, TextField, SelectField, TextAreaField, BooleanField
from flask.ext.wtf import Required, NumberRange


    
class PostForm(Form):
    title = TextField('title', [Required(message="write some stupid title")])
    body = TextAreaField('body', validators= [Required(message="dont leave this blank your retard")], default = "agh")
    category = SelectField('category', choices = [("", "----"),("0", "news"), ("1", "events"), ("2", "art pieces"), ("3", "releases"), ("4", "random")])
    front_page = BooleanField('front page')

class DeleteForm(Form):
    delete_confirm = BooleanField('Delete confirm')

