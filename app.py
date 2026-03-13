import streamlit as st
from skill_extractor import extract_text_from_pdf, extract_skills
from analyzer import find_skill_gap
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.title("Resume Skill Gap Analyzer")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    resume_text = extract_text_from_pdf(resume_file)

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description.lower())

    missing = find_skill_gap(resume_skills, job_skills)

    st.subheader("Skills in Resume")
    st.write(resume_skills)

    st.subheader("Skills Required for Job")
    st.write(job_skills)

    st.subheader("Skill Gap")
    st.write(missing)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_description])

    score = cosine_similarity(vectors)[0][1]
    scores=score*100
    st.metric(label="Resume Match Score", value=f"{score*100:.2f}%")
    