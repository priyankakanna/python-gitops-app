from flask import Flask,jsonify
app = Flask(__name__)
VERSION = "v1.0.0"

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to GitOps CI/CD Demo!",
        "version":  VERSION

})

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": VERSION
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
