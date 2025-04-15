import streamlit as st
import openai
import json

# Sidebar for API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Page layout
st.title("🎯 AI Job Application Assistant")
st.markdown("Paste your resume and a job description below. Get tailored resume bullets, a match score, and a personalized cover letter.")

# Inputs
resume = st.text_area("📄 Paste Your Resume:", height=250)
job_description = st.text_area("📝 Paste the Job Description:", height=250)

# Main Action
if st.button("🚀 Generate AI Suggestions"):
    if not openai_api_key:
        st.warning("⚠️ Please enter your OpenAI API key in the sidebar.")
    elif not resume or not job_description:
        st.warning("⚠️ Please paste both your resume and the job description.")
    else:
        with st.spinner("🤖 Thinking..."):
            openai.api_key = openai_api_key

            prompt = f"""
You are an AI Job Application Assistant.

Compare the resume and job description below.

Resume:
{resume}

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
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )

                output = response["choices"][0]["message"]["content"]

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
                    st.error("❌ Could not parse the response as JSON.")
                    st.text(output)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
