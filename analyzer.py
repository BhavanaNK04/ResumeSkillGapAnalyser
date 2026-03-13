def find_skill_gap(resume_skills, job_skills):

    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills