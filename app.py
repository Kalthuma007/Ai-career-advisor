from flask import Flask, render_template, request
from advisor import get_career_advice

app = Flask(__name__)

# Define a set of allowed tech skills (lowercase, stripped)
TECH_SKILLS = {
    "python", "data analysis", "machine learning", "web development",
    "html", "css", "javascript", "ai", "deep learning",
    "nlp", "sql", "tensorflow", "pytorch", "react",
    "node.js", "java", "c++", "ruby", "django", "flask"
}

def is_tech_skill(skills_input):
    # Normalize user input and check if any known tech skill is included
    user_skills = {s.strip().lower() for s in skills_input.split(",")}
    return any(skill in TECH_SKILLS for skill in user_skills)

@app.route("/", methods=["GET", "POST"])
def index():
    advice = None
    if request.method == "POST":
        interests = request.form.get("interests", "")
        skills = request.form.get("skills", "")

        if not is_tech_skill(skills):
            advice = ("Thanks for sharing! Currently, this AI Career Advisor is focused on tech-related careers. "
                      "Please try entering skills like Python, data analysis, machine learning, web development, etc.")
        else:
            advice = get_career_advice(interests, skills)

    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
