import streamlit as st
import openai
import fitz  # PyMuPDF
from docx import Document
import json

# ✅ Streamlit page config
st.set_page_config(
    page_title="Andrei’s Resume Assistant",
    page_icon="📄",
    layout="centered"
)

# ✅ OpenAI API key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 🔧 Extract text from PDF or DOCX
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()
        return text

    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        return ""

# ✅ UI layout
st.title("🎯 Andrei’s AI Job Application Assistant")
st.markdown("""
Upload or paste your **resume** and a **job description** to receive:
- A match score
- Tailored resume bullet points
- A custom cover letter
""")

# 🔁 Resume Input
st.subheader("📄 Resume")
resume_input_method = st.radio("Choose input method for resume:", ["Upload File", "Paste Text"])
resume_text = ""
uploaded_resume = None

if resume_input_method == "Upload File":
    uploaded_resume = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"], key="resume")
    if uploaded_resume:
        resume_text = extract_text_from_file(uploaded_resume)
        st.success("✅ Resume uploaded successfully.")
else:
    resume_text = st.text_area("Paste your resume here:", height=250)

# 🔁 Job Description Input
st.subheader("📝 Job Description")
job_input_method = st.radio("Choose input method for job description:", ["Upload File", "Paste Text"])
job_description = ""
uploaded_job = None

if job_input_method == "Upload File":
    uploaded
