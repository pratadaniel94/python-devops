from flask import Blueprint, render_template, redirect
from docker import DockerClient

try:
    con = DockerClient('tcp://127.0.0.1:2376')
except Exception as e:
    print('erro: {}'.format(e))


docker = Blueprint('docker', __name__, url_prefix='/docker')

@docker.route('')
def index():
    ctrs = con.containers.list(all=True)
    return render_template('docker.html', ctrs=ctrs)

@docker.route('/start/<string:short_id>')
def start_container(short_id):
    con.containers.get(short_id).start()
    return redirect('/docker')

@docker.route('/stop/<string:short_id>')
def stop_container(short_id):
    con.containers.get(short_id).stop()
    return redirect('/docker')