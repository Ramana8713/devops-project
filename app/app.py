from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! DevOps project running on Kubernetes 🚀"

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/slow")
def slow():
    time.sleep(5)
    return "Slow response for testing alerts"

app.run(host="0.0.0.0", port=5000)
