from flask import Blueprint, render_template, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route("/", methods=["GET"])
def home():
    routes = {
        "Test Session Cookies": url_for('cookies.cookies'),
        "Test Input"          : url_for('input.input'),
        "Test Picture"        : url_for('picture.picture'),
        "Health"              : url_for('health.health')
    }
    return render_template('home.html', routes=routes)
