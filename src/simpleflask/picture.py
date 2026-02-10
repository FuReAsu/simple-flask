from flask import Blueprint, render_template, session, redirect, url_for

picture_bp = Blueprint('picture', __name__)

@picture_bp.route("/picture", methods=["GET"])
def picture():
    if not "session_id" in session:
        return redirect(url_for('home.home'))
    return render_template('picture.html')
