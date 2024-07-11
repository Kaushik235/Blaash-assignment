from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/check_endpoint", methods=["GET","POST"])
def check_endpoint():
    data = request.get_json()
    api_endpoint = data.get("api_endpoint")

    if not api_endpoint:
        return jsonify({"error": "No API endpoint provided"}), 400

    try:
        response = requests.get(api_endpoint)
        response_code = response.status_code
        is_alive = response_code == 200
    except requests.RequestException as e:
        response_code = None
        is_alive = False

    result = {
        "QueriedAt": datetime.now().isoformat(),
        "ResponseCode": response_code,
        "IsAlive": is_alive
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=8083)