import os

from flask import Flask, request
from dotenv import dotenv_values

from services.load_balancer import LoadBalancer

config = {
    **dotenv_values('.env'),
    **dotenv_values('.env.dist'),
    **os.environ,
}

app = Flask(__name__)


@app.route("/wallets", methods=["POST"])
def wallets():
    try:
        data = request.get_json()
        res = lb.get_instance().handle_request(data)
        return res, 200
    except Exception:
        return "Invalid request", 400


@app.route("/networks", methods=["POST"])
def networks():
    try:
        data = request.get_json()
        res = lb.get_instance().handle_request(data)
        return res, 200
    except Exception:
        return "Invalid request", 400


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    lb = LoadBalancer(
        aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY'],
        region_name=config['REGION_NAME'],
        image_id=config['IMAGE_ID'],
        security_group_ids=config['SECURITY_GROUP_IDS'].split(','),
        key_name=config['KEY_NAME'],
        subnet_id=config['SUBNET_ID'],
    )
    if 'DEBUG' not in config:
        config['DEBUG'] = 0
    if 'PORT' not in config:
        config['PORT'] = 5000

    app.run(debug=bool(config['DEBUG']), port=config['PORT'])
