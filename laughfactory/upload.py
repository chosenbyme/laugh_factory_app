from flask import ( Blueprint, render_template, request, redirect ) 
from . import models
bp = Blueprint(
    'upload',
    __name__,
    url_prefix="/upload"
)

@bp.route('/', methods=['POST','GET'])
def upload():
    fname = request.args['fname']
    lname = request.args['lname']
    # if request.method == 'POST':
    #     new_meme = models.Comment(
    #         url = request.memeurl
    #     )

    #     models.db.session.add(new_meme)
    return render_template('upload.html',firstname=fname,lastname=lname)

