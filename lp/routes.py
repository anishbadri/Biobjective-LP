from lp import app
from lp.test import bolp

@app.route('/')
def index():
    # t = bolp([[1.2,1.0,1.1]],[[-64.6,-59.5,-43.9]],[[1,1,1],[432,321,168],[-8,5,8]],[[1000],[320000],[3500]]) 
    # print(t)
    bolp([[1.2,1.0,1.1]],[[-64.6,-59.5,-43.9]],[[1,1,1],[432,321,168],[-8,5,8]],[[1000],[320000],[3500]]) 
    return 'This is Gehendras application'