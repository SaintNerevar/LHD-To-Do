# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, flash, url_for
from flask import request, g
from app.models.task import Task

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')

@blueprint.route('/create', methods=['POST'])
def create():
    if request.form['task-desc']:
        task_desc = request.form['task-desc']
        user_id = g.user.id
        Task.add_task(task_desc, user_id)
        return redirect(url_for('home.index'))
    else:
        flash('A task can\'t be blank, boss!', 'info')
        return redirect(url_for('home.index'))

@blueprint.route('/delete', methods=['POST'])
def delete():
    task_id = request.form['task-id']
    Task.delete_task(task_id)
    return redirect(url_for('home.index'))
    