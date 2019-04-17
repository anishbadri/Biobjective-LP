from lp import app
from lp.test import bolp
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template

class UserInputForm(FlaskForm):
    input1 = StringField('Input 1', validators=[DataRequired()])
    output = 0
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET', 'POST'])
def index():
    # t = bolp([[1.2,1.0,1.1]],[[-64.6,-59.5,-43.9]],[[1,1,1],[432,321,168],[-8,5,8]],[[1000],[320000],[3500]]) 
    # print(t)
    form = UserInputForm()
    if form.validate_on_submit():
        mylist = [float(x) for x in form.input1.data.split(',')]
        out = 0
        for num in mylist:
            out += num
        form.output =  out
        return render_template('index.html', form = form)
    l = bolp([[1.2,1.0,1.1]],[[-64.6,-59.5,-43.9]],[[1,1,1],[432,321,168],[-8,5,8]],[[1000],[320000],[3500]]) 
    return render_template('index.html', form = form)