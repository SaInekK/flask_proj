# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:23:28 2021

@author: User
"""

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

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
        print(request.form['username'])
        
    return render_template('contact.html', title="Feedback", menu=menu)

@app.route("/profile/<username>") # <path:username> для текста за /, туда же int, float
def profile(username, path):
    # print(url_for('profile'))
    return f"User: {username}, {path}"

# with app.test_request_context(): # Искуственный контекст запроса
#     print(url_for('index'))      # Работает без app.run()

# with app.test_request_context(): # Искуственный контекст запроса
#     print(url_for('index'))
#     print(url_for('about'))   
#     print(url_for('profile', username="sainekk"))   

if __name__ == "__main__": # Запуск вебсервера
    app.run(debug=True)