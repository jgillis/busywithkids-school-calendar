from flask_frozen import Freezer
from app import app, config

freezer = Freezer(app)

@freezer.register_generator
def page_urls():
    for lang in config["languages"].keys():
        yield f"/{lang}/index"
        yield f"/{lang}/add-calendar"
        yield f"/{lang}/modify-events"
        yield f"/{lang}/setup-another-school"

if __name__ == "__main__":
    freezer.freeze()
