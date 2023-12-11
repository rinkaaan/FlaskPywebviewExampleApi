from flask import send_from_directory, Flask
from flask_cors import CORS

import api.resources.time.api

app = Flask(__name__)
CORS(app, supports_credentials=False)


@app.get("/")
def serve_index():
    return send_from_directory("static", "index.html")


@app.get("/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)


api.resources.time.api.register_routes(app)

if __name__ == "__main__":
    app.run(port=34200, debug=True)
