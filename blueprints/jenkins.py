from flask import Blueprint, render_template, redirect, request
from jenkins import Jenkins
from time import sleep
from pprint import pprint

con = Jenkins(
    'http://127.0.0.1:8080',
    username='admin',
    password='4linux123')
jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')


@jenkins.route('')
def index():
    jobs = [[con.get_build_info(job['name'],con.get_job_info(job['name'])['lastBuild']['number'])['timestamp'], job['name'],job['color']]for job in con.get_all_jobs()]
    return render_template('jenkins.html', jobs=jobs)


@jenkins.route('/update/<string:job>')
def update_job(job):
    xml=con.get_job_config(job)
    return render_template('jenkins_update.html', job=job, xml=xml)


@jenkins.route('/reconfig/<string:job>', methods=['POST'])
def reconfig_job(job):
    con.reconfig_job(job, request.form['xml'])
    return redirect('/jenkins')


@jenkins.route('/build/<string:job>')
def build_job(job):
    con.build_job(job)
    sleep(10)
    return redirect('/jenkins')
