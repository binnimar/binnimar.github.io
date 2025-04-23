from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html', active_page="about")

@main.route('/projects')
def projects():
    return render_template('projects.html', active_page="projects")