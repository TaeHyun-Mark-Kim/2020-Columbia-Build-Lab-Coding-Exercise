from flask import Flask
from flask import render_template
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

@app.route('/increase_score', methods=['GET', 'POST'])
def increase_score():
    global scoreboard

    json_data = request.get_json()   
    team_id = json_data["id"]  
    
    for team in scoreboard:
        if team["id"] == team_id:
            team["score"] += 1

    return jsonify(scoreboard=scoreboard)

#added helper fn
def sortSecond(val): 
    return val[1] 

#added to display teams based on score
@app.route('/sort_teams', methods=['GET', 'POST'])
def sort_teams():
    global scoreboard

    json_data = request.get_json()  
    this_id = json_data["id"]  
    
    myList=[]
    temp_scoreboard=[]
    for team in scoreboard:
        myList.append((team["id"], team["score"])) #tuple of (id, score)
    myList.sort(key = sortSecond, reverse=True) #sort list of tuples by score
    print(myList)

    for element in myList:
        for team in scoreboard:
            if team["id"]==element[0]:
                temp_scoreboard.append(team)
    print(temp_scoreboard)

    return jsonify(scoreboard=temp_scoreboard)


if __name__ == '__main__':
   app.run(debug = True)

