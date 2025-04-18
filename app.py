import streamlit as st
from openai import OpenAI
import fitz  # PyMuPDF
from docx import Document
import json

# ✅ Page config
st.set_page_config(
    page_title="Andrei’s Resume Assistant",
    page_icon="📄",
    layout="centered"
)

# ✅ OpenAI client setup
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ✅ Text extraction helper
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        return "".join([page.get_text() for page in pdf])
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

# ✅ App intro
st.title("🎯 Andrei’s AI Job Application Assistant")
st.markdown("""
Upload or paste your **resume** and a **job description** to receive:
- A match score
- Tailored resume bullet points
- A custom cover letter
""")

# 📄 Resume input
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

# 📝 Job description input
st.subheader("📝 Job Description")
job_input_method = st.radio("Choose input method for job description:", ["Upload File", "Paste Text"])
job_description = ""
uploaded_job = None

if job_input_method == "Upload File":
    uploaded_job = st.file_uploader("Upload job description (PDF or DOCX)", type=["pdf", "docx"], key="job")
    if uploaded_job:
        job_description = extract_text_from_file(uploaded_job)
        st.success("✅ Job description uploaded successfully.")
else:
    job_description = st.text_area("Paste the job description here:", height=250)

# 🚀 Generate suggestions
if st.button("Generate AI Suggestions"):
    if resume_input_method == "Upload File" and not uploaded_resume:
        st.warning("Please upload your resume.")
    elif resume_input_method == "Paste Text" and not resume_text.strip():
        st.warning("Please paste your resume text.")
    elif job_input_method == "Upload File" and not uploaded_job:
        st.warning("Please upload the job description.")
    elif job_input_method == "Paste Text" and not job_description.strip():
        st.warning("Please paste the job description.")
    else:
        with st.spinner("Generating tailored results..."):
            prompt = f"""
You are an AI Job Application Assistant.

Compare the resume and job description below.

Resume:
{resume_text}

Job Description:
{job_description}

Tasks:
1. Score the match (0-100).
2. Suggest 3 tailored resume bullet points.
3. Generate a custom cover letter.

Return in this JSON format:
{{
  "match_score": <int>,
  "suggested_bullets": ["bullet 1", "bullet 2", "bullet 3"],
  "custom_cover_letter": "..."
}}
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                output = response.choices[0].message.content

                try:
                    result = json.loads(output)

                    st.subheader("🧠 Match Score")
                    st.success(f"{result['match_score']} / 100")

                    st.subheader("💼 Suggested Resume Bullets")
                    for bullet in result["suggested_bullets"]:
                        st.markdown(f"- {bullet}")

                    st.subheader("✉️ Custom Cover Letter")
                    st.text_area("Generated Cover Letter", result["custom_cover_letter"], height=300)

                except json.JSONDecodeError:
                    st.error("⚠️ Couldn’t parse response as JSON. Here’s the raw output:")
                    st.code(output)

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
