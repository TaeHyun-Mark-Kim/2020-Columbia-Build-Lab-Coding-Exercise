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
    # render template using name of template and the variables you want to pass to the template engine as keyword arguments
    # template = scoreboard.html
    # argument for template engine = scoreboard (list of dictionaries with each team's ID, name, and score)

    return render_template('scoreboard.html', scoreboard = scoreboard) 

@app.route('/increase_score', methods=['GET', 'POST'])
def increase_score():
    global scoreboard

    # parse request as JSON
    json_data = request.get_json()   
    
    # determine ID of the team to increase score
    team_id = json_data["id"]  

    i = 0

    while True:
        new_score = 0
        
        if scoreboard[i]["id"] == team_id:
            scoreboard[i]["score"] += 1
            new_score = scoreboard[i]["score"]
            
            j = i
            while True:
                if ((j>0) and (new_score > scoreboard[j-1]["score"])):
                    # swap the positions of the two teams in the list
                    temp_team = scoreboard[j].copy()
                    scoreboard[j] = scoreboard[j-1].copy()
                    scoreboard[j-1] = temp_team.copy()
                    j-=1
                else:
                    break

            break
        else:
            i+=1

    # return the scoreboard as JSON
    return jsonify(scoreboard=scoreboard)


if __name__ == '__main__':
   app.run(debug = True)




