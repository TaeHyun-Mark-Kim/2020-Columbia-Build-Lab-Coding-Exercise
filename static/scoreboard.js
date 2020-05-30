function display_scoreboard(scoreboard){
  $("#teams").empty();
  $.each(scoreboard, function(index, team){
    addTeamView(team.id, team.name, team.score);
  });
}

function addTeamView(id, name, score){
  var team_template = $("<div class = row></div>");
  var name_template = $("<div class = col-md-5></div>");
  var score_template = $("<div class = col-md-2></div>");
  var button_template = $("<div class = col-md-2></div>");
  var increase_button = $("<button class = increase-button>+</button>");
  $(increase_button).click(function(){
    console.log("Buttom clicked")
    increase_score(id);
    // $("#teams").empty();
    // $.each(scoreboard, function (index, team) {
    //   addTeamView(team.id, team.name, team.score);
    // });

    // console.log("This is the scoreboard:", scoreboard)
    
  });
  name_template.text(name);
  score_template.text(score);
  button_template.append(increase_button);
  team_template.append(name_template);
  team_template.append(score_template);
  team_template.append(button_template);
  $("#teams").append(team_template);
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
      console.log("Success has happened?")
      console.log("The Result")
      // console.log(result)
      console.log(result["scoreboard"])
      // scoreboard=result
      // console.log("The new sb:")
      // console.log(scoreboard)
      display_scoreboard(result["scoreboard"])

    },
    error: function(request, status, error){
        console.log("Error");
        console.log(request)
        console.log(status)
        console.log(error)
    }
  });
  console.log("Success has happened?-1")

}

$(document).ready(function(){
  display_scoreboard(scoreboard);
})
