"""Load the trained model and predict the role for input resume text."""

import argparse
import pickle
from pathlib import Path
from typing import Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"


def load_model() -> Tuple[TfidfVectorizer, LogisticRegression]:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found at {MODEL_PATH}. Run train.py first."
        )

    with MODEL_PATH.open("rb") as f:
        bundle = pickle.load(f)

    try:
        vectorizer = bundle["vectorizer"]
        model = bundle["model"]
    except (TypeError, KeyError) as exc:
        raise ValueError("Model file is malformed. Retrain the model.") from exc

    return vectorizer, model


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Predict the job role from resume text."
    )
    parser.add_argument(
        "text",
        help="Resume text to classify (quote the text to include spaces).",
    )
    args = parser.parse_args()

    vectorizer, model = load_model()
    features = vectorizer.transform([args.text])
    prediction = model.predict(features)[0]
    print(f"Predicted role: {prediction}")


if __name__ == "__main__":
    main()
