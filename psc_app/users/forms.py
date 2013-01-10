from flask.ext.wtf import Form, TextField, BooleanField, PasswordField, SelectField
from flask.ext.wtf import Required, Email, EqualTo, Length, validators



class RegistrationForm(Form):
    username = TextField('username', [
                                    Required(message="you are big faggot"),
                                    Length(min=4, max=35, message="you are faggot"),
                                    
                                    ])
    email = TextField('email', [
                                Length(min=6, max=50), 
                                Email()
                                ])
    password = PasswordField('new_password', [
        Required(), 
        Length(min = 8, max = 50),
        EqualTo('confirm', message = 'Passwords must match faggot')
    ])
    confirm = PasswordField('Repeat Password Faggot')
    description = TextField('description', [
                                            Required(message="say something about yourself retard"),
                                            Length(min=10, max=500, message="shut up already")
                                            ])
    homepage = TextField('homepage')
    zodiac = SelectField('zodiac', choices = [('0', 'Aries'),('1', 'Taurus'), ('2', 'Gemini'), ('3', 'Cancer'),('4', 'Leo'),('5', 'Virgo'), ('6', 'Libra'), ('7', 'Scorpio'), ('8', 'Sagitarius'),('9', 'Capricorn'), ('10','Aquarius'),('11','Pisces')])
    role = SelectField('role', choices = [('0', 'Guest'),('1', 'Member'),('2', 'Staff'),('3', 'Admin')])



class LoginForm(Form):
    username = TextField('username', [Required(message="you are faggot gaffot")])
    password = PasswordField('password', [Required()])
    remember_me = BooleanField('remember_me', default = False)

