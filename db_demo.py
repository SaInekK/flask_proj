#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 13:54:31 2021

@author: alex
"""
import os
import sqlite3
import random
from string import ascii_letters, digits
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY =  ''.join(random.choices(ascii_letters + digits, k = 20))

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
    
# if __name__ == "__main__": # Запуск вебсервера
#     app.run(debug=True)