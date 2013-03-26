from flask.ext.wtf import Form, TextField, SelectField, TextAreaField, BooleanField, FileField
from flask.ext.wtf import Required, NumberRange


    
class PostForm(Form):
    title = TextField('title', [Required(message="write some stupid title")],                                     
                                    #delete next line in production
                                    default = "shithead post post lalalala"
                                    )
    body = TextAreaField('body', validators= [Required(message="dont leave this blank your retard")], 
                                    #delete next line in production
                                    default = "shithead"
                                    )
    category = SelectField('category',choices = [("0", "news"), ("1", "events"), ("2", "art pieces"), ("3", "releases"), ("4", "random")])
    front_page = BooleanField('front page')
    image = FileField("foto" )
    
class DeleteForm(Form):
    delete_confirm = BooleanField('Delete confirm')



