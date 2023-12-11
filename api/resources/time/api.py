import datetime


def register_routes(app):
    @app.get("/api/time")
    def get():
        return datetime.datetime.now(datetime.timezone.utc).isoformat()
