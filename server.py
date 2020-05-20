from flask import Flask
from flask import render_template, redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)

scoreboard = [
    {
    "id": 1,
    "name": "Boston Bruins",
    "score": 7
    },

    {
    "id": 2,
    "name": "Tampa Bay Lightning", 
    "score": 5
    },

    {
    "id": 3,
    "name": "Toronto Maple Leafs", 
    "score": 2
    },

    {
    "id": 4,
    "name": "Florida Panthers", 
    "score": 1
    },

    {
    "id": 5,
    "name": "Buffalo Sabres", 
    "score": 1
    },
]


@app.route('/')
def show_scoreboard():
    return render_template('scoreboard.html', scoreboard = scoreboard)

@app.route('/sort_score', methods=['GET', 'POST'])
def sort_scoreboard():
    global scoreboard

    team_id = request.get_json()
    for team in scoreboard:
        if int(team["id"]) == int(team_id):
            team["score"] += 1

    new_scoreboard = sorted(scoreboard, key = lambda i: i['score'], reverse = True)
    scoreboard = new_scoreboard

    return redirect(url_for('show_scoreboard'))


if __name__ == '__main__':
   app.run(debug = True)




