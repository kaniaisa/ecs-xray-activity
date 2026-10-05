import os
from flask import Flask, jsonify
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app_config = os.environ.get('MY_APP_CONFIG')
db_password = os.environ.get('MY_DB_PASSWORD')
service_name = os.environ.get('SERVICE_NAME', 'kania-flask-xray-service')

app = Flask(__name__)

xray_recorder.configure(
    service=service_name,
    daemon_address='127.0.0.1:2000'
)

XRayMiddleware(app, xray_recorder)

@app.route("/")
def index():
    return jsonify({
        "message": "Hello from Flask!",
        "app_config": app_config,
        "db_password": db_password
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
