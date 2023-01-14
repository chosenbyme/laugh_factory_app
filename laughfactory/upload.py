from flask import ( Blueprint, render_template, request, redirect ) 
from . import models
bp = Blueprint(
    'upload',
    __name__,
    url_prefix="/upload"
)

@bp.route('/', methods=['POST','GET'])
def upload():
    # if request.method == 'POST':
    #     new_meme = models.User(
    #         username = request.username,
    #         password = request.password
    #     )

    #     models.db.session.add(new_meme)
    return render_template('upload.html')
