def get_career_advice(interests, skills):
    # Normalize and split inputs
    interests_list = [i.strip() for i in interests.lower().replace(",", " ").split()]
    skills_list = [s.strip() for s in skills.lower().replace(",", " ").split()]

    tech_keywords = {
    "python": "Python Developer, Data Analyst, or Machine Learning Engineer",
    "data": "Data Analyst or Data Scientist",
    "ml": "Machine Learning Engineer",
    "machine learning": "Machine Learning Engineer",
    "ai": "AI Researcher or AI Engineer",
    "deep learning": "Deep Learning Specialist",
    "web": "Web Developer (Frontend, Backend, or Fullstack)",
    "html": "Frontend Web Developer",
    "css": "Frontend Web Developer",
    "javascript": "Frontend or Fullstack Developer",
    "react": "Frontend Developer with React expertise",
    "sql": "Database Administrator or Data Engineer",
    "linux": "DevOps Engineer or Systems Administrator",
    "cloud": "Cloud Engineer, Cloud Architect, or AWS/GCP/Azure Specialist",
    "cybersecurity": "Cybersecurity Analyst, Ethical Hacker, or Security Engineer",
    "network": "Network Engineer or Network Administrator",
    "networking": "Network Engineer or Network Security Specialist",
    "devops": "DevOps Engineer",
    "docker": "DevOps Engineer or Containerization Specialist",
    "kubernetes": "Cloud-Native Engineer or DevOps Engineer",
    "aws": "AWS Solutions Architect or Cloud Engineer",
    "azure": "Azure Cloud Engineer or Microsoft Cloud Specialist",
    "gcp": "Google Cloud Engineer"
}

    found_matches = []

    for keyword in tech_keywords:
        if keyword in interests_list or keyword in skills_list:
            found_matches.append(tech_keywords[keyword])

    if not found_matches:
        return (
            "Thanks for sharing! Currently, this AI Career Advisor is focused on tech-related careers. "
            "Please try entering skills like Python, data analysis, machine learning, web development, etc."
        )

    # Remove duplicates
    suggestions = list(set(found_matches))

    # Format the response nicely
    response = "Based on your skills and interests, here are some suitable tech career paths:\n\n"
    for s in suggestions:
        response += f"- {s}\n"

    return response
