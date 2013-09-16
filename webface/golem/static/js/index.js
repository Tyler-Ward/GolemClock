
$(document).ready(function(){
  bind_controls();
});

function bind_controls(){
  // Bind snooze
  $('#btn-snooze').click(function(){
    $.ajax(
      { 
        url: '/snooze-alarm',
        method: 'get',
        success: function(){
          console.log("Alarm snoozed");
        },
        error: function(){
          console.log("Alarm not snoozed");
        }
      }
    );
  });
  
  // Bind stop
  $('#btn-stop').click(function(){
    $.ajax(
      {
        url: '/stop-alarm',
        method: 'get',
        success: function(){
          console.log("Alarm stopped");
        },
        error: function(){
          console.log("Alarm not stopped");
        }
      }
    );
  });
  
}
