from flask import render_template, request, redirect, url_for
import random, time, pandas as pd
from app import app

@app.route('/', methods=['GET', 'POST'])
def main():
    aircraft_list = pd.read_pickle('E:/Coding/spot_the_plane/app/static/dicts/otherModels.pickle')
    airbus_models = pd.read_pickle('E:/Coding/spot_the_plane/app/static/dicts/airbusModels.pickle')
    boeing_models = pd.read_pickle('E:/Coding/spot_the_plane/app/static/dicts/boeingModels.pickle')
    planes_and_names = pd.read_pickle('E:/Coding/spot_the_plane/app/static/dicts/planes_and_names.pickle')
    aircraft_list = random.sample(aircraft_list, len(aircraft_list))
    quiz_list = random.sample(planes_and_names, len(planes_and_names))
    quiz_counter = 0
    current_plane = quiz_list[quiz_counter]
    aircraft_true = current_plane[0]
    aircraft_false = []
    pic = current_plane[1]
    for k, i in boeing_models.items():
        if aircraft_true not in i:
            aircraft_false.append(random.choice(i))

    for k, i in airbus_models.items():
        if aircraft_true not in i:
            aircraft_false.append(random.choice(i))

    for n in range(21):
        a = aircraft_false.append(random.choice(aircraft_list))

    for a in aircraft_false:
        if a == aircraft_true:
            aircraft_false.remove(a)
    aircraft_false = random.sample(aircraft_false, 3)
    choices = random.sample(aircraft_false + [aircraft_true], 4)
    answer_1 = choices[0]
    answer_2 = choices[1]
    answer_3 = choices[2]
    answer_4 = choices[3]
    image = '/static/pics/{}'.format(pic)
        
    if request.method == 'POST':
        time.sleep(1)
        return redirect(url_for('main'))
    else:
        time.sleep(1)
        return render_template('main.html', aircraft_true=aircraft_true, image=image, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4)