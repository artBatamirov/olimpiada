from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('a_sensors.html', do=[[1, 1, 1, 5, 2, 1], [], [], [], []], da=[[10, 27], [15, 12], [14, 25], [18, 19]])

