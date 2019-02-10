#!/home/daniel/dashboard/venv/bin/python3
from flask import Flask, render_template, session, redirect, request
from blueprints.docker import docker
from blueprints.jenkins import jenkins
from blueprints.gitlab import gitlab
from ldap3 import Server, Connection
from os import urandom

server = Server('ldap://127.0.0.1:389')


app = Flask(__name__)
app.register_blueprint(docker)
app.register_blueprint(jenkins)
app.register_blueprint(gitlab)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form
        con = Connection(
            server,
            'cn={},dc=4linux,dc=com,dc=br'.format(data['login']),
            data['password']
        )
        if con.bind():
            session['auth'] = True
    return render_template('index.html')


@app.route('/logout')
def logout_session():
    del session['auth']
    return redirect('/')


if __name__ == '__main__':
    app.secret_key = urandom(12)
    app.run(debug=True)
