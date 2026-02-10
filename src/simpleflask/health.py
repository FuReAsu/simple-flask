from flask import Blueprint, jsonify
import logging

logger = logging.getLogger(__name__)
health_bp = Blueprint("health", __name__)

@health_bp.route("/health")
def health():
    logger.info("/health endpoint called")
    return jsonify({"Status": "Running"})
