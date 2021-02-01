from flask import render_template
from app import app

@app.route('/main')
def main():
    return render_template('main.html', image="0.jpg", answer_1="Boeing 737", answer_2="Boeing 737", answer_3="Boeing 737", answer_4="Boeing 737",)