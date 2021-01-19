# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, flash, url_for
from flask import request, g, session
from app.models.task import Task
from datetime import date

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')

@blueprint.route('/create', methods=['POST'])
def create():

    # Login-less logic
    if not 'access_token' in session:
        if not 'tasks' in session:
            session['tasks'] = []
        elif len(session['tasks']) == 5:
            flash("Wanna create more? Login with your Github Account first, will Ya?", 'info')
            return redirect(url_for('home.index'))

        if request.form['task-desc']:
            task_id = len(session['tasks']) # To be used for temporary task_id
            task = {}
            task['id'] = task_id
            task['create_date'] = date.today()
            task['description'] = request.form['task-desc']
            session['tasks'].append(task)
            # Session won't be written in the response unless modified is set to True when modifying nested objects
            session.modified = True 
            return redirect(url_for('home.index'))
        else:
            flash('A task can\'t be blank, boss!', 'info')
            return redirect(url_for('home.index'))

    # Logged in logic
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
    # Login-less logic
    if not 'access_token' in session:
        task_id = int(request.form['task-id'])
        del session['tasks'][task_id]

        # This is to reset all the ids for deletion by index
        for index, task in enumerate(session['tasks'][:]):
            task['id'] = index

        session.modified = True
        return redirect(url_for('home.index'))
    
    # Logged in logic
    task_id = request.form['task-id']
    Task.delete_task(task_id)
    return redirect(url_for('home.index'))
    