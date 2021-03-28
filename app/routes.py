from flask import render_template, request, redirect, url_for, jsonify
import random, glob, os
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('quiz'))
    else:
        return render_template('index.html')

@app.route('/quiz')
def quiz():
    files = [os.path.basename(f) for f in glob.glob('app/static/images/*.jpg')]
    images = random.sample(files, len(files))
    return render_template('quiz.html', images=images)