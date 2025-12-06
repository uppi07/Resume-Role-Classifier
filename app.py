"""Flask UI for the Resume Role Classifier."""

import argparse
import os
from typing import Optional, Tuple

from flask import Flask, jsonify, render_template, request

from src.predict import MODEL_PATH, load_model

app = Flask(__name__)

_model_bundle: Optional[Tuple] = None


def get_model():
    """Lazy-load and cache the vectorizer/model bundle."""
    global _model_bundle
    if _model_bundle is None:
        _model_bundle = load_model()
    return _model_bundle


@app.get("/")
def index():
    return render_template("index.html", model_ready=MODEL_PATH.exists())


@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    text = str(payload.get("text", "")).strip()
    if not text:
        return (
            jsonify({"error": "Please paste some resume text before predicting."}),
            400,
        )

    try:
        vectorizer, model = get_model()
    except FileNotFoundError:
        return (
            jsonify(
                {
                    "error": f"Trained model not found at {MODEL_PATH}. "
                    "Run python src/train.py first."
                }
            ),
            500,
        )
    except ValueError as exc:
        return (
            jsonify({"error": f"Model file looks malformed. Retrain it. Details: {exc}"}),
            500,
        )

    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    return jsonify({"prediction": prediction})


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Resume Role Classifier web UI."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("PORT", 5000)),
        help="Port to run the server on (default: 5000 or $PORT).",
    )
    parser.add_argument(
        "--host",
        default=os.environ.get("HOST", "0.0.0.0"),
        help='Host interface to bind (default: "0.0.0.0" or $HOST).',
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=os.environ.get("FLASK_DEBUG") == "1",
        help="Enable Flask debug mode.",
    )
    parser.add_argument(
        "--no-debug",
        action="store_false",
        dest="debug",
        help="Disable Flask debug mode.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    app.run(debug=args.debug, host=args.host, port=args.port)
