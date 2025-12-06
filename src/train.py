"""Train a resume role classifier and persist the vectorizer and model."""

import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "resume_data.csv"
MODEL_PATH = BASE_DIR / "model" / "model.pkl"


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    if {"text", "label"} - set(df.columns):
        raise ValueError("Data must contain 'text' and 'label' columns")

    texts = df["text"].astype(str)
    labels = df["label"].astype(str)

    # Avoid stratification errors when classes only have a single example.
    stratify_labels = labels if labels.value_counts().min() > 1 else None

    X_train, X_test, y_train, y_test = train_test_split(
        texts,
        labels,
        test_size=0.25,
        random_state=42,
        stratify=stratify_labels,
    )

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    X_train_vec = vectorizer.fit_transform(X_train)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    train_accuracy = model.score(X_train_vec, y_train)
    X_test_vec = vectorizer.transform(X_test)
    test_accuracy = model.score(X_test_vec, y_test)
    print(f"Train accuracy: {train_accuracy:.3f}")
    print(f"Test accuracy: {test_accuracy:.3f}")

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MODEL_PATH.open("wb") as f:
        pickle.dump({"vectorizer": vectorizer, "model": model}, f)

    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
