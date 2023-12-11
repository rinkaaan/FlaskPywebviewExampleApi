import datetime

from flask import Blueprint

time_bp = Blueprint("time", __name__, url_prefix="/api/time")


@time_bp.get("/")
def get():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()
