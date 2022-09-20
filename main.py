
from flask import Flask, render_template

from candidates_manager import CandidatesManager

from config import CANDIDATES_DATA_LOCATION

app = Flask(__name__)

manager = CandidatesManager(CANDIDATES_DATA_LOCATION)

@app.route("/")
def page_main():
    candidates = manager.get_all()
    return render_template("list.html", candidates=candidates)

@app.route("/candidate/<int:can_id>")
def page_single_candidate(can_id):
    candidate = manager.get_one(can_id)

    if candidate is None:
        return render_template("404.html")

    return render_template("single.html", candidate=candidate)

@app.route("/search/<can_name>")
def page_single_by_name(can_name):
    candidates = manager.by_name(can_name)
    candidates_len = len(candidates)

    return render_template("search.html",
                           candidates=candidates,
                           candidates_len=candidates_len
                           )

@app.route("/skill/<skill_name>")
def page_single_by_skill(skill_name):
    candidates = manager.by_skill(skill_name)
    candidates_len = len(candidates)
    skill = skill_name
    return render_template("skill.html",
                           candidates=candidates,
                           candidates_len=candidates_len,
                           skill=skill
                           )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)