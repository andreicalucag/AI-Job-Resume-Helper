# 🎯 Andrei’s AI Job Application Assistant

A smart, AI-powered tool that helps you tailor your job applications by comparing your resume to a job description — and delivering custom bullet points, a match score, and a personalized cover letter.

> ✨ Now supports **PDF/DOCX uploads** for both resumes and job descriptions!

---

## 🚀 Live Demo  
🔗 [Try the App on Streamlit](https://andreicalucag-resumeai.streamlit.app)

---

## 🔧 Features

- 📎 Upload resume or job description as **PDF or Word** file
- ✍️ Paste resume and job description as plain text (fallback)
- ✅ Receive a **match score** (0–100)
- 🧠 Get 3 **tailored resume bullet points**
- ✉️ Instantly generate a **custom cover letter**
- 🔐 Uses **Streamlit secrets** for secure OpenAI API key management

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Streamlit** | Front-end UI |
| **OpenAI GPT-4** | Language model |
| **PyMuPDF** | Extract text from PDF |
| **python-docx** | Extract text from Word files |
| **GitHub + Streamlit Cloud** | Hosting & Deployment |

---

## 📁 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/andreicalucag/ai-job-assistant.git
cd ai-job-assistant
2. Set up environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3. Create .streamlit/secrets.toml
Create a folder called .streamlit and inside it, create secrets.toml with:

toml
Copy
Edit
OPENAI_API_KEY = "sk-...your-secret-key..."
4. Run the app
bash
Copy
Edit
streamlit run app.py
🌐 Deployment Instructions
Deploy easily via Streamlit Cloud:

Push your app to GitHub

Set app.py as the main file

Set your API key via Settings > Secrets

Done ✅

📌 Project Purpose
This was built as part of a generative AI capstone project focused on automating tedious job application tasks.
The tool integrates:

File input parsing

GPT-4 prompt chaining

JSON-based structured output

Personal branding

📬 Contact
👤 Andrei Calucag

LinkedIn https://www.linkedin.com/in/andreicalucag

GitHub https://github.com/andreicalucag

🌺 Based in Hawaiʻi, passionate about tech + sustainability

