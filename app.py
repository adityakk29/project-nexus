from flask import Flask, render_template


app = Flask(__name__)


SECTIONS = {
    "dsa": {
        "icon": "⌘",
        "label": "DSA foundations",
        "kicker": "Core path · 6 weeks",
        "title": "Think in patterns,\nnot puzzles.",
        "description": "Build the fluency to recognize structure quickly, explain your choices clearly, and write solutions that hold up under pressure.",
        "color": "violet",
        "stats": [("42", "lessons"), ("12", "patterns"), ("6", "mock loops")],
        "topics": [
            ("01", "Arrays & hashing", "Turn messy inputs into clean invariants and make the first useful observation early."),
            ("02", "Trees & graphs", "Navigate recursive structure, choose the right traversal, and reason about complexity."),
            ("03", "Dynamic programming", "Define state with intent, then make the recurrence feel inevitable."),
        ],
        "next": "Sliding window patterns",
    },
    "system-design": {
        "icon": "◈",
        "label": "System design",
        "kicker": "Architecture path · 5 weeks",
        "title": "Design systems\nworth trusting.",
        "description": "Practice the full architecture conversation: clarify the problem, establish constraints, and defend the trade-offs that shape a resilient system.",
        "color": "coral",
        "stats": [("36", "lessons"), ("9", "case studies"), ("4", "design reviews")],
        "topics": [
            ("01", "Requirements first", "Separate must-haves from nice-to-haves and give every design decision a measurable target."),
            ("02", "Scale & reliability", "Reason about load, bottlenecks, failure domains, and graceful degradation."),
            ("03", "Trade-off defense", "Make your constraints visible so the room can follow the shape of your thinking."),
        ],
        "next": "Designing a notification platform",
    },
    "data-systems": {
        "icon": "↗",
        "label": "Data systems",
        "kicker": "Data path · 4 weeks",
        "title": "Make scale\nfeel legible.",
        "description": "Learn to discuss streaming, storage, consistency, and cost as one connected system instead of a list of technologies.",
        "color": "cyan",
        "stats": [("28", "lessons"), ("8", "architectures"), ("3", "build briefs")],
        "topics": [
            ("01", "Streaming foundations", "Choose delivery semantics deliberately and make lateness, ordering, and replay concrete."),
            ("02", "Storage decisions", "Match data shape and access patterns to systems that can support them economically."),
            ("03", "Pipelines at scale", "Trace data from source to serving layer while keeping correctness observable."),
        ],
        "next": "Designing an event lake",
    },
}


LESSONS = {
    "dsa": [
        ("Recognize the shape", "Start with constraints. A sorted input suggests two pointers; repeated lookup suggests a set or map; a range query suggests a prefix structure.", "Explain the signal before naming the pattern."),
        ("Protect the invariant", "Write down what stays true after every iteration. In a sliding window, the window is always valid before you expand it again.", "State the invariant in one sentence while coding."),
        ("Test the edges", "Walk through empty input, one item, duplicates, and the largest legal input. These cases reveal whether the model is sound.", "Close with complexity and one failure case."),
    ],
    "system-design": [
        ("Clarify the contract", "Define who calls the system, what a successful response means, and which guarantees matter: latency, durability, ordering, or freshness.", "Ask three high-value questions before drawing boxes."),
        ("Find the pressure points", "Estimate traffic and storage, then identify the first bottleneck. Partitioning, caching, queues, and replication each solve a different pressure.", "Tie every component to a constraint."),
        ("Design for failure", "Describe what happens when a dependency is slow, a region is unavailable, or a message is delivered twice. Reliability is part of the main design.", "Name the trade-off you would revisit at 10x scale."),
    ],
    "data-systems": [
        ("Choose delivery semantics", "At-most-once is simple but lossy; at-least-once is durable but needs idempotency; exactly-once is a system property with a real cost.", "Explain where duplicates can appear."),
        ("Separate compute from storage", "Use immutable raw events for replay, curated data for consumption, and a serving layer shaped around the query rather than the source.", "Describe the path from event to decision."),
        ("Make correctness observable", "Track freshness, volume, schema changes, late data, and bad records. A pipeline without quality signals is only quietly failing.", "Choose two alerts and justify their thresholds."),
    ],
}


def navigation(active="overview"):
    return {
        "active": active,
        "items": [
            ("overview", "Overview", "⌂"),
            ("dsa", "DSA foundations", "⌘"),
            ("system-design", "System design", "◈"),
            ("data-systems", "Data systems", "↗"),
        ],
        "secondary": [("method", "The method"), ("outcomes", "Outcomes")],
    }


@app.route("/")
def home():
    return render_template("index.html", navigation=navigation())


@app.route("/section/<slug>")
def section(slug):
    content = SECTIONS.get(slug)
    if content is None:
        return render_template("index.html", navigation=navigation()), 404
    content = {**content, "lessons": LESSONS[slug]}
    return render_template("section.html", content=content, navigation=navigation(slug))


@app.route("/section/<slug>/lesson/<int:number>")
def lesson(slug, number):
    content = SECTIONS.get(slug)
    lessons = LESSONS.get(slug)
    if content is None or lessons is None or not 1 <= number <= len(lessons):
        return render_template("index.html", navigation=navigation()), 404
    title, note, prompt = lessons[number - 1]
    return render_template("lesson.html", content=content, lesson={
        "number": number, "title": title, "note": note, "prompt": prompt,
    }, navigation=navigation(slug))


@app.route("/method")
def method():
    return render_template("section.html", content={
        "icon": "◎", "label": "The Nexus method", "kicker": "A repeatable interview ritual",
        "title": "Practice the way\nyou perform.",
        "description": "Senior interviews reward more than a correct answer. This framework turns every prompt into a repeatable performance ritual.",
        "color": "violet", "stats": [("03", "moves"), ("01", "shared language"), ("∞", "reps")],
        "topics": [("01", "Frame", "Surface constraints, clarify the real problem, and establish decision criteria."), ("02", "Design", "Build from first principles, then articulate trade-offs with useful precision."), ("03", "Defend", "Handle curveballs, failure modes, and scale questions without losing the narrative.")],
        "next": "Try the framework on a fresh prompt",
    }, navigation=navigation("method"))


@app.route("/outcomes")
def outcomes():
    return render_template("section.html", content={
        "icon": "✦", "label": "Outcomes", "kicker": "What changes with practice",
        "title": "Bring your\nexperience forward.",
        "description": "The goal is not to memorize more answers. It is to make your judgment visible, structured, and useful in the room.",
        "color": "coral", "stats": [("2.4x", "more clarity"), ("100+", "prompts"), ("5+", "years supported")],
        "topics": [("01", "Sharper openings", "Start with the problem that actually needs solving, not the solution you happen to know."), ("02", "Calmer pivots", "Use constraints and principles to absorb new information without losing direction."), ("03", "Stronger closes", "Summarize the decision, the risk, and the next step with confidence.")],
        "next": "Choose your first learning path",
    }, navigation=navigation("outcomes"))


if __name__ == "__main__":
    app.run(debug=True)
