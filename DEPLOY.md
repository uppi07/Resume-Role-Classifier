# Deployment Guide - Resume Role Classifier

## 🚀 Quick Deploy Options

### Option 1: Render (Recommended - FREE)

1. **Push to GitHub** (already done!)
2. **Go to Render.com**
   - Sign up/login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repo: `uppi07/Resume-Role-Classifier`
   - Render will auto-detect `render.yaml`
   - Click "Create Web Service"
3. **Done!** Your app will be live at `https://resume-role-classifier.onrender.com`

### Option 2: Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

### Option 3: Docker (Self-hosted)

```bash
# Build
docker build -t resume-classifier .

# Run
docker run -p 5000:5000 resume-classifier

# Visit http://localhost:5000
```

### Option 4: Heroku

```bash
heroku create resume-role-classifier
git push heroku main
heroku open
```

---

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py

# Visit http://localhost:5000
```

---

## 📦 Environment Variables

See `.env.example` for configuration options.

For production, set:
- `FLASK_DEBUG=0`
- `HOST=0.0.0.0`
- `PORT=5000` (or use platform default)

---

## ✅ Production Checklist

- [x] Dockerfile created
- [x] render.yaml configured
- [x] GitHub Actions CI workflow
- [x] .env.example added
- [x] Gunicorn for production server
- [x] Health check endpoint
- [ ] Custom domain (optional)
- [ ] SSL certificate (auto with Render/Railway)

---

## 🐛 Troubleshooting

**Model not found error:**
```bash
# Train the model first
python src/train.py
```

**Port already in use:**
```bash
# Change port
export PORT=8000
python app.py --port 8000
```

---

## 📊 Post-Deployment

After deploying, test your API:

```bash
curl -X POST https://your-app.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Python developer with 5 years experience in Django and Flask"}'
```

Expected response:
```json
{"prediction": "Software Engineer"}
```

---

**🎉 Your app is production-ready!**
