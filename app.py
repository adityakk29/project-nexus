from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    tracks = [
        {"icon": "⌘", "level": "Core · 6 weeks", "title": "DSA for senior engineers", "description": "Patterns, proofs, and trade-offs—built for the conversations expected at senior-level loops.", "lessons": "42 lessons", "color": "violet"},
        {"icon": "◈", "level": "Architecture · 5 weeks", "title": "System design depth", "description": "Design resilient systems, defend your choices, and navigate ambiguity with confidence.", "lessons": "36 lessons", "color": "coral"},
        {"icon": "↗", "level": "Data · 4 weeks", "title": "Data systems at scale", "description": "Streaming, lakehouses, consistency and cost: the systems thinking for modern data leaders.", "lessons": "28 lessons", "color": "cyan"},
    ]
    return render_template("index.html", tracks=tracks)


if __name__ == "__main__":
    app.run(debug=True)
