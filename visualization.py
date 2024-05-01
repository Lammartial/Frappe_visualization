from flask import Blueprint, render_template

# Create a blueprint for visualization routes
visualization = Blueprint('visualization', __name__)

# Define your visualization route
@visualization.route("/visualizations")
def visualizations():
    return render_template('visualizations.html')
