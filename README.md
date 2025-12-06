# Resume Role Classifier

A lightweight, production-ready Resume Role Classifier that automatically detects the most likely job role from raw resume text. Built so recruiters and hiring teams can quickly sort candidates, prioritize outreach, and reduce screening time.

Why recruiters should care

- Speed up screening: Automatically tag resumes with role labels (e.g., Data Scientist, Backend Engineer, Product Manager) so recruiters can filter candidates instantly.
- Consistent triage: Removes manual variability in initial resume sorting and surfaces candidates who match open roles.
- Easy integration: Use the CLI, Web UI, or embed the model in your pipeline to make resume classification part of your workflow.

At-a-glance

- Tech: Python, scikit-learn, pandas
- Model: TF-IDF vectorization + Logistic Regression
- Output: Predict role label for a resume text or batch of resumes
- Reuse: Trained model saved to model/model.pkl for fast predictions

Quick demo (3 commands)

1. Install dependencies

pip install -r requirements.txt

2. Train (one-time)

python src/train.py

3. Predict a single resume

python src/predict.py "Experienced software engineer with 5 years of backend development..."

Or run the Web UI:

python app.py
# open http://localhost:5000

How recruiters can use this today

- Bulk classify candidate pools to identify top-role matches.
- Add a quick pre-screen step to your ATS: run resumes through the model and store predicted role as metadata.
- Use predicted labels to prioritize outreach and create targeted email templates.

Integration ideas

- Wrap src/predict.py behind a simple Flask/FastAPI endpoint for your internal tools.
- Add to applicant pipelines to set candidate tags automatically in your ATS.
- Extend labels and training data to match your company's role taxonomy for higher accuracy.

Project layout

resume-role-classifier/
 ├── data/            # training data (CSV)
 ├── src/             # training and prediction scripts
 ├── model/           # saved model & vectorizer
 ├── app.py           # optional Web UI
 ├── README.md
 └── requirements.txt

What I admire in a candidate (skills showcased by this project)

- Practical ML for product: building models with immediate recruiter impact
- Clean code & reproducibility: single-command training and a saved model
- Python data stack: scikit-learn, pandas, TF-IDF

Want to try it with your resume database?

If you're a recruiter or hiring manager and would like a demo, integration help, or a forked version tailored to your roles and labels, please reach out:

- GitHub: https://github.com/uppi07

I can:
- Provide a short demo and run a sample batch on your anonymized resumes
- Customize label taxonomy to match your job families
- Deliver a Dockerized or API-wrapped version for production

License

MIT
