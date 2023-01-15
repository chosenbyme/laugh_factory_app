from flask import ( Blueprint, render_template, request, redirect ) 
from . import models
bp = Blueprint('login', __name__, url_prefix="/login")

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        new_user = models.User(
            first_name = request.form['fname'],
            last_name = request.form['lname'],
            email = request.form['email'],
            password = request.form['password']
        )
        models.db.session.add(new_user)
        models.db.session.commit()

    return render_template('login.html')

