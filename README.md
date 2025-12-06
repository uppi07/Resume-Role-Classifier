# Resume Role Classifier

A simple NLP-based machine learning project that predicts the job role from resume text.

## Features
- TF-IDF text vectorization
- Logistic Regression classifier
- Accuracy evaluation
- Saved model (`model.pkl`) for reuse
- Easy to extend with more resume data

## Tech Stack
- Python
- scikit-learn
- pandas
- pickle

## How to Train


python src/train.py


## How to Predict


python src/predict.py "Your resume text here"


## Web UI

1. Install deps: `pip install -r requirements.txt`
2. Train once: `python src/train.py`
3. Launch the UI: `python app.py` and open http://localhost:5000
   - If port 5000 is busy, run `python app.py --port 5001`

## Folder Structure
resume-role-classifier/
 ├── data/
 ├── src/
 ├── model/
 ├── README.md
 ├── requirements.txt

## Codex Prompt to Generate the Entire Project Code

Paste this into ChatGPT-Codex:

Create a complete Python project for a Resume Role Classifier using scikit-learn.

Requirements:
- Load CSV from data/resume_data.csv
- Use TF-IDF vectorizer
- Train Logistic Regression
- Print accuracy
- Save both the vectorizer and model in model/model.pkl
- Create a predict.py file that loads the saved model and predicts a label for an input text
- Create requirements.txt with sklearn, pandas
- Follow clean folder structure: data/, src/, model/
