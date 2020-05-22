function display_scoreboard(scoreboard){
  console.log(scoreboard)
  $("#result_list").empty();
  var i = 1;
  $.each(scoreboard, function(index, team){
    
    addTeamView(team.id, team.name, team.score, i);
    i += 1;
  });
}

function addTeamView(id, name, score, position){
  var list_template = $("<div class = 'list-group-item'></div>");
  var position_template = $("<div class= 'col-md-2'></div>")
  var team_template = $("<div class = ' row teamEntry'></div>");
  var name_template = $("<div class = 'col-md-5 '></div>");
  var score_template = $("<div class = 'col-md-3 '></div>");
  var button_template = $("<div class = 'col-md-2 text-right'></div>");
  var increase_button = $("<button class = 'increase-button btn btn-primary'>+</button>");
  $(increase_button).click(function(){
    increase_score(id);
  });
  position_template.text(position + ".")
  name_template.text(name);
  score_template.text(score);
  button_template.append(increase_button);
  team_template.append(position_template);
  team_template.append(name_template);
  team_template.append(score_template);
  team_template.append(button_template);
  list_template.append(team_template);
  $("#result_list").append(list_template);
}

function increase_score(id){
  var team_id = {"id": id}
  $.ajax({
    type: "POST",
    url: "increase_score",                
    dataType : "json",
    contentType: "application/json; charset=utf-8",
    data : JSON.stringify(team_id),
    success: function(result){
      display_scoreboard(result["scoreboard"])
    },
    error: function(request, status, error){
        console.log("Error");
        console.log(request)
        console.log(status)
        console.log(error)
    }
  });
}

$(document).ready(function(){
  display_scoreboard(scoreboard);
})
