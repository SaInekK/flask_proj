# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:23:28 2021

@author: User
"""
import sqlite3
import random
from string import ascii_letters, digits
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY =  ''.join(random.choices(ascii_letters + digits, k = 20))


app = Flask(__name__)
app.config['SECRET_KEY'] = ''.join(random.choices(ascii_letters + digits, k = 18))





menu = [{"name": "Installing", "url": "install-flask"},
        {"name": "First app", "url": "first-app"},
        {"name": "Feedback", "url": "contact"} ]

@app.route("/")
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about_fl.html', menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():

        
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Message sent.', category='success')
        else:
            flash('Error sending message.', category='error')
        print(request.form['username'])
        
    return render_template('contact.html', title="Feedback", menu=menu)

@app.route("/profile/<username>") # <path:username> для текста за /, туда же int, float
def profile(username):
    # print(url_for('profile'))
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"User: {username}"

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Page not found", menu=menu), 404 # по умолчанию возвращает 200

@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'sainekk' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    
    return render_template('login.html', title='Authorisation', menu=menu)


# with app.test_request_context(): # Искуственный контекст запроса
#     print(url_for('index'))      # Работает без app.run()

# with app.test_request_context(): # Искуственный контекст запроса
#     print(url_for('index'))
#     print(url_for('about'))   
#     print(url_for('profile', username="sainekk"))   

if __name__ == "__main__": # Запуск вебсервера
    app.run(debug=True)