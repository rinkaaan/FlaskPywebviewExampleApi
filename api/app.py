from datetime import datetime

from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)


@app.route("/api/time")
def time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return {"time": current_time}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
