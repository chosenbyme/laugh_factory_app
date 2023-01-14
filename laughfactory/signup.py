from flask import ( Blueprint, render_template, request, redirect ) 
from . import models
bp = Blueprint(
    'signup',
    __name__,
    url_prefix="/signup"
)

@bp.route('/', methods=['POST','GET'])
def signup():
    print(request.form)
    if request.method == 'POST':
        print(request.form)
        new_user = models.User(
            first_name = request.form['fname'],
            last_name = request.form['lname'],
            email = request.form['email'],
            password = request.form['password']
        )

        models.db.session.add(new_user)
        models.db.session.commit()

    return render_template('signup.html')


