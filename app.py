from flask import Flask, render_template, make_response, url_for, request
import psycopg2
import re
from config import DB_NAME, DB_HOST, DB_USER, DB_PASSWORD

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('AdminSettings.html', title = 'Будни Студента')

@app.route('/download')
def download():
    return render_template('DownloadGame.html', title = 'Скачать')

@app.route('/galery')
def galery():
    return render_template('Galery.html', title = 'Галерея')

@app.route('/MPET')
def MPET():
    return render_template('MPET.html', title = 'МПЭТ')

@app.route('/cont')
def Contacts():
    return render_template('Contacts.html', title = 'Контакты')

@app.route('/answer')
def Answer():
    return render_template('AnswerSettings.html', title = 'Частые вопросы')

@app.route('/about')
def About():
    return render_template('About.html', title = 'О проекте')

from flask import render_template
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)