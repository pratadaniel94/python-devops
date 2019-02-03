from flask import Blueprint, render_template
from gitlab import Gitlab

gitlab = Blueprint('gitlab', __name__, url_prefix='/gitlab')
con = Gitlab('http://127.0.0.1:8000', private_token='qzbT82u-2EPEGqhs7oFz')

@gitlab.route('')
def index():
    projects = con.projects.list(all=True)
    users = con.users.list(all=True)
    print(users[0].attributes)
    
    return render_template('gitlab.html', users=users, projects=projects)