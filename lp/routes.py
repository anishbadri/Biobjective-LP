from lp import app
from lp.test import bolp
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import render_template

class UserInputForm(FlaskForm):
    input1 = StringField('Objective Function 1', validators=[DataRequired()])
    input2 = StringField('Objective Function 2', validators=[DataRequired()])
    c1 = StringField('Constraint 1', validators=[DataRequired()])
    c2 = StringField('Constraint 2', validators=[DataRequired()])
    c3 = StringField('Constraint 3', validators=[DataRequired()])
    b1 = StringField('b 1', validators=[DataRequired()])
    b2 = StringField('b 2', validators=[DataRequired()])
    b3 = StringField('b 3', validators=[DataRequired()])
    output = 0
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET', 'POST'])
def index():
    # t = bolp([[1.2,1.0,1.1]],[[-64.6,-59.5,-43.9]],[[1,1,1],[432,321,168],[-8,5,8]],[[1000],[320000],[3500]]) 
    # print(t)
    form = UserInputForm()
    if form.validate_on_submit():
        of1 = [float(x) for x in form.input1.data.split(',')]
        of2 = [float(x) for x in form.input2.data.split(',')]
        con1 = [float(x) for x in form.c1.data.split(',')]
        con2 = [float(x) for x in form.c2.data.split(',')]
        con3 = [float(x) for x in form.c3.data.split(',')]
        bb1 = int(form.b1.data)
        bb2 = int(form.b2.data)
        bb3 = int(form.b3.data)

        # out = 0
        # for num in mylist:
        #     out += num
        form.output =  bolp([of1],[of2],[con1,con2,con3],[[bb1],[bb2],[bb3]]) 
        return render_template('index.html', form = form)
    # l = bolp([[1.2,1.0,1.1]],[[-64.6,-59.5,-43.9]],[[1,1,1],[432,321,168],[-8,5,8]],[[1000],[320000],[3500]]) 
    return render_template('index.html', form = form)