import re
from jinja2 import evalcontextfilter, Markup, escape
from psc_app import app


_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
_image_re = re.compile(r'http:\/\/([^\r\n]+)\.(jpg|jpeg|png|gif)')

@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
    
def datetimeformat(value, format='%d of %m of %Y at %H:%M'):
    return value.strftime(format)

#@app.template_filter()
#@evalcontextfilter    
#def imageinsert(eval_ctx, value):
#    result = u'<img src="%s">' % i for i in _image_re.split(escape(value))


