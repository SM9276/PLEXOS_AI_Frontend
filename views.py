from flask import Blueprint, render_template

# Define a new Flask blueprint called 'views'
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    """
    This function handles requests to the root URL ("/") of the 'views' blueprint.

    When someone visits this URL, the function returns the 'index.html' webpage.

    Returns:
        A rendered HTML page (index.html).
    """
    return render_template("index.html")
