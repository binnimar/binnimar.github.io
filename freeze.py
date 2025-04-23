from flask_frozen import Freezer
from app import create_app

app = create_app()
# Optionally, tell Frozen-Flask to write into ./docs instead of ./build:
app.config['FREEZER_DESTINATION'] = 'docs'
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
