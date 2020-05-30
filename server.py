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
    print("We're here! in / ")
    return render_template('scoreboard.html', scoreboard = scoreboard) 

@app.route('/increase_score', methods=['GET', 'POST'])
def increase_score():
    global scoreboard
    print("We're here in /inc score")

    json_data = request.get_json()   
    team_id = json_data["id"]  
    
    for team in scoreboard:
        if team["id"] == team_id:
            team["score"] += 1

    for team in scoreboard:
        if team["id"] == team_id and team["id"] != 1:
            print("Elligible for shuffle?")
            for team_2 in scoreboard:
                if team_2["id"]==(team["id"]-1):
                    print("Eureka")
                    if team["score"] > team_2["score"]:
                        print("Let's swap!!")
                        team["id"] += -1
                        team["id"] += 1
                        # tmp_1 = team["id"]
                        # team["id"] = team_2["id"]
                        # team_2["id"] = tmp_1
                        
                        tmp_id = team["id"]
                        tmp_name = team["name"]
                        tmp_score = team["score"]
                        # team["id"] = team_2["id"]

                        team["name"] = team_2["name"]
                        team["score"] = team_2["score"]

                        # team_2["id"] = tmp_id
                        team_2["name"] = tmp_name
                        team_2["score"] = tmp_score

                        



    print("This is what the scoreboard looks like after increment:")
    print(scoreboard)
    return jsonify(scoreboard=scoreboard)


if __name__ == '__main__':
   app.run(debug = True)




