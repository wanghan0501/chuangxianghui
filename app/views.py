# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 27/12/2017 15:28.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""

from flask import render_template, flash, redirect, request, url_for, g, session, jsonify

from app import app


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/comment', methods=["GET", "POST"])
def comment():
    return render_template('comment.html')
