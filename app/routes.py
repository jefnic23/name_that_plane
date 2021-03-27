from flask import render_template, request, redirect, url_for, jsonify
import random, time, glob, os
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('quiz'))
    else:
        return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    files = [os.path.basename(f) for f in glob.glob('app/static/images/*.jpg')]
    filename = random.choice(files)
    plane_true = filename.split('_')[0]
    planes_false = random.sample(set([f.split('_')[0] for f in files if f not in [plane_true]]), 3)
    choices = random.sample(planes_false + [plane_true], 4)
    answer_1 = choices[0]
    answer_2 = choices[1]
    answer_3 = choices[2]
    answer_4 = choices[3]
    image = '/static/images/{}'.format(filename)
        
    if request.method == 'POST':
        time.sleep(1)
        return redirect(url_for('quiz'))
    else:
        time.sleep(1)
        return render_template('quiz.html', aircraft_true=plane_true, image=image, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4)