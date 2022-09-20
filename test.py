
    # return render_template("list.html")

    candidates = utils.get_candidates_all()
    result = "<br>"

    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += ""

    return f"<pre> {result} </pre>"

@app.route("/candidate/<int:id>")

def get_candidate(id):

    candidate = utils.get_candidate(id)
    result = "<br>"
    result += candidate["name"] + "<br>"
    result += candidate["position"] + "<br>"
    result += candidate["skills"] + "<br>"
    result += "<br>"

    return f"""
        <img src="({candidate["picture"]})">
        <pre> {result} </pre>
    """
def candidate_skills(skill):

    candidates = utils.get_candidates_by_skill(skill.lower())
    result = "<br>"

    for candidate in candidates:
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += ""

    return f"<pre> {result} </pre>"