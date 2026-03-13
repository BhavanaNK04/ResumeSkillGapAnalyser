import PyPDF2
import pandas as pd
def extract_text_from_pdf(file):
    text = ""
    pdf = PyPDF2.PdfReader(file)

    for page in pdf.pages:
        text += page.extract_text()

    return text.lower()

def extract_skills(text):

    skills_df = pd.read_csv("skills.csv")

    skills_list = skills_df['skills'].tolist()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
