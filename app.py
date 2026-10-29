from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="Hello from the CI/CD Pipeline Capstone")


if __name__ == "__main__":
    print("SERVICERUNNING", flush=True)
    print("Application listening on port 8000", flush=True)
    app.run(host="0.0.0.0", port=8000)
