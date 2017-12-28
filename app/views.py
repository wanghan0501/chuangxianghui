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


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/comment', methods=["GET", "POST"])
def comment():
    # get total comment number
    count = comment_helper.get_comment_count()
    # random comment offset
    random_comment_offset = random.randint(0, count - 1)
    # get comment
    comment = comment_helper.get_comment_by_offset(random_comment_offset)
    return render_template('comment.html', text=comment.text)


@app.route('/manage', methods=["GET", "POST"])
def manage():
    error = None
    if request.method == 'POST':
        if request.form['username'] != manager['manager_name']:
            error = "Invalid Manager Name"
        elif request.form['password'] != manager['password']:
            error = 'Invalid Password'
        else:
            comments = comment_helper.get_all_comments()
            count = {'visit': 0, 'com_len': 0}
            return render_template('manage.html', comments=comments, count=count)
    return render_template('login.html', error=error)


@app.route('/addcomment', methods=["GET", "POST"])
def add_momment():
    return 0;



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
