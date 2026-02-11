from flask import Blueprint, render_template, request, session, redirect, url_for
import socket
import logging

logger = logging.getLogger(__name__)
status_bp = Blueprint("status", __name__)

@status_bp.route("/status", methods=["GET"])
def status():
    if not "session_id" in session:
        return redirect(url_for('home.home'))
   
    server_name = socket.gethostname()
    client_ip = request.remote_addr
    host_header = request.host
    is_secure = request.is_secure
    
    return render_template("status.html", 
                           server_name=server_name,
                           client_ip=client_ip,
                           host_header=host_header,
                           is_secure=is_secure)
