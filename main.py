from flask import Flask, request, jsonify, Response
import os

app = Flask(__name__)

# Health check
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "ok": True,
        "service": "toi-gif-worker",
        "status": "ready"
    })

# Render endpoint (POST /render)
@app.route("/render", methods=["POST"])
def render():
    data = request.get_json(silent=True) or {}

    snap_url = data.get("snapUrl")
    if not snap_url:
        return jsonify({"ok": False, "error": "Missing snapUrl"}), 400

    # TEMP: stub response (we will add Browserless + FFmpeg next)
    return jsonify({
        "ok": True,
        "message": "Render endpoint reached",
        "snapUrl": snap_url
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
