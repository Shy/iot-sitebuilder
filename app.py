"""Iot Site Builder app."""
import os
from flask import Flask, render_template
import contentful
from dotenv import load_dotenv

load_dotenv()

SPACE_ID = os.getenv('SPACE_ID')
DELIVERY_API_KEY = os.getenv('DELIVERY_API_KEY')

CLIENT = contentful.Client(
    SPACE_ID,
    DELIVERY_API_KEY)

APP = Flask(__name__)


# def format_datetime(value):
#     """Format date time object using jinja filters"""
#     return value.strftime('%B %-d, %Y')


# APP.jinja_env.filters['datetime'] = format_datetime


@APP.route('/')
@APP.route('/home')
def index():
    """index route. Gathers page from contentful and builds it."""
    page = CLIENT.entries({'content_type': 'page', 'include': 10})
    # section_one = CLIENT.entry(page[0].section_one.id)
    return render_template("page.html", page=page, carousel=page[0].section_one.carousal_item)


if __name__ == '__main__':
    APP.run(debug=True)
