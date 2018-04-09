from flask import Flask, render_template, url_for, abort
import contentful
import os
from dotenv import load_dotenv

load_dotenv()

SPACE_ID = os.getenv('SPACE_ID')
DELIVERY_API_KEY = os.getenv('DELIVERY_API_KEY')

client = contentful.Client(
    SPACE_ID,
    DELIVERY_API_KEY)

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    """index route. Gathers all shows from contentful and uses that to render page"""
    return render_template("headline.html")

if __name__ == '__main__':
    app.run(debug=True)
