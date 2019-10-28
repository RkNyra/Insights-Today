from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class SharePostForm(FlaskForm):
    '''
    The blog-post sharing form
    '''
    topic = SelectField('', choices=[('TechSavy', 'TechSavy'), ('MoneySmart','MoneySmart'), ('Life & Laughter', 'Life & Laughter')], validators=[Required()])
    content = TextAreaField('', validators=[Required()], render_kw={"placeholder": "Write your story here :)"})
    submit = SubmitField('Share')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')