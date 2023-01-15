from flask import ( Blueprint, render_template, request, redirect ) 
from . import models
bp = Blueprint('loggedin', __name__, url_prefix="/loggedin")

@bp.route('/', methods=['GET', 'POST'])
def login():
        if request.method == "POST":
            user_email = request.form['email'] 
            user_password = request.form['password'] 
            find_email = models.User.query.filter_by(email=user_email).first()
            find_psw = models.User.query.filter_by(password=user_password).first()
            if find_email is None or find_psw is None:
                return render_template('login.html')
            else:
                return render_template('loggedin.html')
