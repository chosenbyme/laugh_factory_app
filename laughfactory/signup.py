from flask import ( Blueprint, render_template, request, redirect ) 
from . import models
bp = Blueprint(
    'signup',
    __name__,
    url_prefix="/signup"
)

@bp.route('/', methods=['POST','GET'])
def signup():
    if request.method == "POST":
       print("testing")
    return render_template('signup.html')



