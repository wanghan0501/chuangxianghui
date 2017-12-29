# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 27/12/2017 15:28.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""

from flask import render_template, flash, redirect, request, url_for, g, session, jsonify

from app import app, comment_helper
from config import manager
import random


@app.route('/comment', methods=["GET", "POST"])
def comment():
    # get total comment number
    count = comment_helper.get_comment_count()
    # random comment offset
    random_comment_offset = random.randint(0, count - 1)
    # get comment
    comment = comment_helper.get_comment_by_offset(random_comment_offset)
    return render_template('comment.html', text=comment.text)


@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != manager['manager_name']:
            error = "Invalid Manager Name"
        elif request.form['password'] != manager['password']:
            error = 'Invalid Password'
        else:
            return redirect(url_for('manage'))
    return render_template('login.html', error=error)


@app.route('/manage', methods=["GET", "POST"])
@app.route('/manage<int:page>', methods=["GET", "POST"])
def manage(page=1):
    comments = comment_helper.get_all_comments()
    length = len(comments)
    p_list, start, end = comment_helper.get_page(length, pagesize=20, page=page)
    count = {'visit': 0, 'com_len': length, 'page_list': p_list}
    return render_template('manage.html', comments=comments[start:end], count=count)


@app.route('/add_comment', methods=["GET", "POST"])
def add_comment():
    cm = request.args.get('comment')
    comment_helper.add_comment(cm)
    return jsonify(res=True)


@app.route('/del_comment', methods=["GET", "POST"])
def del_comment():
    id = request.args.get('id')
    comment_helper.delete_comment(id)
    return jsonify(res=True)


@app.route('/logout', methods=["GET", "POST"])
def logout():
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
