# Resume Skill Gap Analyzer

## Overview

The **Resume Skill Gap Analyzer** is a web-based application that analyzes a candidate’s resume and compares it with a job description to identify missing skills.

It helps job seekers understand the **skill gap between their current profile and job requirements**, allowing them to improve their resumes and prepare better for job opportunities.

---

## Problem Statement

Many candidates apply for jobs without knowing whether their skills match the job requirements. Recruiters often use automated systems to filter resumes based on skills.

This project helps solve this problem by:

* Extracting skills from resumes
* Extracting required skills from job descriptions
* Identifying missing skills
* Showing a resume-job match score

---

## Goal

The main goal of this project is to analyze a resume and compare it with a job description to identify missing skills.




# Features

* Upload resume in PDF format
* Extract text from resumes
* Detect technical skills from resume and job description
* Identify missing skills
* Calculate resume-job similarity score
* Simple and interactive web interface using Streamlit

---

# Technology Stack

### Programming Language

* Python

### Libraries Used

* **Streamlit** – Web application interface
* **spaCy / NLTK** – Natural language processing
* **scikit-learn** – TF-IDF similarity calculation
* **PyPDF2** – Resume text extraction from PDF
* **Pandas** – Data handling

### Deployment

* Streamlit Cloud
* GitHub

# How It Works

1. User uploads a resume in PDF format.
2. The system extracts text from the resume.
3. Skills are detected using a predefined skill dataset.
4. Job description skills are extracted.
5. The system compares both skill sets.
6. Missing skills and similarity score are displayed.


# Future Enhancements

* AI-based resume parsing
* Automatic skill extraction using NLP models
* Course recommendations for missing skills
* ATS compatibility scoring
* Visualization dashboard
* Integration with job portals

---

# Advantages

* Helps candidates identify missing skills
* Improves job preparation
* Saves time for recruiters
* Provides automated resume analysis

---

# Conclusion

The **Resume Skill Gap Analyzer** is a practical application of **Natural Language Processing and Machine Learning** that helps candidates understand how well their resumes match job requirements.

It provides insights into missing skills and helps users improve their profiles for better career opportunities.


