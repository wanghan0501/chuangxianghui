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


# 暴力强行判断是否登陆，只要有一个用户登陆了，所有人都可以访问
# 只要logout，所有人都不能访问
flag = 0


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
            flag = 1
            return redirect(manage)
    return render_template('login.html', error=error)


@app.route('/manage', methods=["GET", "POST"])
def manage():
    if flag == 1:
        comments = comment_helper.get_all_comments()
        count = {'visit': 0, 'com_len': len(comments)}
        return render_template('manage.html', comments=comments, count=count)
    else:
        return redirect(login)


@app.route('/add_comment', methods=["GET", "POST"])
def add_comment():
    return


@app.route('/logout', methods=["GET", "POST"])
def logout():
    flag = 0
    return


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
