# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 27/12/2017 18:53.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""
from app.models import Visit
from app import db
from sqlalchemy import func


def add_visit(visit_day, visit_times):
    v = Visit(visit_day, visit_times)
    db.session.add(v)
    db.session.commit()


def check_visit_exist(visit_day):
    v = select_visit(visit_day)
    return False if v is None else True


def select_visit(day):
    v = Visit.query.filter_by(visit_day=day).first()
    return v


def update_visit(visit_day):
    v = select_visit(visit_day)
    v.visit_count += 1
    db.session.commit()


def get_all_count():
    try:
        count = db.session.query(func.sum(Visit.visit_count)).scalar()
    except Exception:
        count = 0
    return count
