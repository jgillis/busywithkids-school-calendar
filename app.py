from flask import Flask, render_template
import markdown
import yaml
import os
from datetime import datetime


with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

app = Flask(__name__)

def load_markdown(lang, page):
    file_path = f"content/{lang}/{page}.md"
    if not os.path.exists(file_path):
        return "Page not found", 404
    with open(file_path, "r") as f:
        return markdown.markdown(f.read().format(**config))

@app.route("/")
def home_redirect():
    return home(config["default_language"])

@app.route("/<lang>/index")
def home(lang):
    content = load_markdown(lang, "index")
    return render_template("base.html", content=content, title="Home", lang=lang, config=config, year=datetime.now().year)

@app.route("/<lang>/<page>")
def page(lang, page):
    content = load_markdown(lang, page)
    return render_template("base.html", content=content, title=page.replace("-", " ").title(), lang=lang, config=config, year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)
