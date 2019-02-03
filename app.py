#!/home/daniel/dashboard/venv/bin/python3
from flask import Flask, render_template
from blueprints.docker import docker
from blueprints.jenkins import jenkins

app = Flask(__name__)
app.register_blueprint(docker)
app.register_blueprint(jenkins)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)