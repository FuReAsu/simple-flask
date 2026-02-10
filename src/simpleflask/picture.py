from flask import Blueprint, render_template

picture_bp = Blueprint('picture', __name__)

@picture_bp.route("/picture", methods=["GET"])
def picture():
    return render_template('picture.html')
