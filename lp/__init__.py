from flask import Flask


app=Flask(__name__)
app.config['SECRET_KEY'] = 'cac873583f189291c68823d86860459a'

from lp import routes
