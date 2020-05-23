function display_scoreboard(scoreboard){
  $("#teams").empty();
  $.each(scoreboard, function(index, team){
    addTeamView(team.id, team.name, team.score);
  });
}

function addTeamView(id, name, score){
var div_id = id + "-score";

  var team_template = $("<div class = row></div>");
  var name_template = $("<div class = col-md-5></div>");
  var score_template = $("<div class = col-md-2 id = "+div_id+"></div>");
  var button_template = $("<div class = col-md-2></div>");
  var increase_button = $("<button class = increase-button>+</button>");
  $(increase_button).click(function(){
    increase_score(id);
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
      //console.log(scoreboard[0]);
      //var score = 0;
      //for (var i = 0; i < scoreboard.length; i++) {
      //  console.log(scoreboard[i]);
      //  if(scoreboard[i].id == team_id){
      //    score = sccoreboard[i].score;
      //  }
      //}

      //console.log(score);
      //var score = result[].score;
      //console.log(result);
      //console.log(result.score)
      //var jQueryXml = $(result);
      //console.log(jQueryXml);
      //var textElement = jQueryXml.find("score");
      //console.log(textElement);
      var score = result.score;
      console.log('#' + result.id + '-score' + '.col-md-2');
      $('#' + result.id + '-score' + '.col-md-2').html(score);
      
    },
    error: function(request, status, error){
        console.log("Error");
        console.log(request)
        console.log(status)
        console.log(error)
    }
  });
  //return +score+1;
}

$(document).ready(function(){
  display_scoreboard(scoreboard);
})
