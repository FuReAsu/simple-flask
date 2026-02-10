from flask import Blueprint, render_template, request, session, redirect, url_for
import logging

cookies_bp = Blueprint("cookies", __name__)
logger = logging.getLogger(__name__)

@cookies_bp.route("/cookies", methods=["GET","POST"])
def cookies():
    if request.headers.get("X-Forwarded-For"):
        client_ip = request.headers.get("X-Forwarded-For")
    elif request.headers.get("X-Real-IP"):
        client_ip = request.headers.get("X-Real-IP")
    else:
        client_ip = request.remote_addr

    message = ""

    if "session_id" in session:
        message = f"Your session_id is {session["session_id"]}"
    else:
        return redirect(url_for('home.home'))
           
    if request.method == "POST":
        button_clicked = request.form.get("button")
        if button_clicked == "releaseButton":
            message = f"Your session_id has been cleared"
            session.pop("session_id", None)
            logger.info (f"{client_ip} | cookie has been cleared for client")
    
    return render_template("cookies.html", message=message)
