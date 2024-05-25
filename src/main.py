from flask import Flask, request

from services.load_balancer import LoadBalancer

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
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    lb = LoadBalancer()
    app.run(debug=True)
