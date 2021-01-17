# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, flash, url_for
from flask import request, g
from app.models.task import Task

blueprint = Blueprint('home', __name__)

@blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('home/index.html')
    elif request.method == 'POST':
        if request.form['task-desc']:
            task_desc = request.form['task-desc']
            user_id = g.user.id
            Task.add_task(task_desc, user_id)
            return render_template('home/index.html')
        else:
            flash('A task can\'t be blank, boss!', 'info')
            return render_template('home/index.html')