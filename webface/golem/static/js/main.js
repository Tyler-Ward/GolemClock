$(document).ready(function(){
	bind_controls();
});

function bind_controls(){
	$('#btn-test-display').click(function(){
		test_display();
	});

	$('.alarm-mondays, .alarm-tuesdays, .alarm-wednesdays, .alarm-thursdays, .alarm-fridays, .alarm-saturdays, .alarm-sundays, .alarm-activated, .alarm-suppressed').change(function(){
		console.log("Editing a thing.");
	});

	$('.alarm-delete').click(function(){
			console.log("Deleting a thing.");
			delete_alarm(this);
	});
}

function delete_alarm(alarm){
	
}

function update_checkbox_value(alarm){
	
}

function test_display(){
	$.ajax({
		url: "/test/display",
		method: "get",
		success: function(){
			console.log("Display test fired successfully");
		},
		error: function(){
			console.log("Failed whilst firing display test.");
		},
	});
}
