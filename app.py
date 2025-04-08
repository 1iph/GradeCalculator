from flask import Flask, render_template, request

app = Flask(__name__)


def get_grade(score):
    score = float(score)
    if score > 95:
        return "A+"
    elif score == 95:
        return "A"
    elif score >= 90:
        return "A-"
    elif score > 85:
        return "B+"
    elif score == 85:
        return "B"
    elif score >= 80:
        return "B-"
    elif score > 75:
        return "C+"
    elif score == 75:
        return "C"
    elif score >= 70:
        return "C-"
    elif score > 65:
        return "D+"
    elif score == 65:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"


@app.route("/", methods=["GET", "POST"])
def index():
    scores = []
    average = None
    highest = None
    lowest = None
    final_grade = None

    if request.method == "POST":
        scores_input = request.form["scores"]
        try:
            scores = [float(s.strip()) for s in scores_input.split(",")]
            average = sum(scores) / len(scores)
            highest = max(scores)
            lowest = min(scores)
            final_grade = get_grade(average)
        except:
            return render_template("index.html", error="Please enter valid comma-separated numbers!")

    return render_template("index.html", scores=scores, average=average,
                           highest=highest, lowest=lowest, final_grade=final_grade)


if __name__ == "__main__":
    app.run(debug=True)
