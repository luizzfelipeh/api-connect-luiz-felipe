from flask import Flask, jsonify
from routes.user_routes import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)


@app.route("/")
def status():
    return jsonify({"status": "API rodando"}), 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)