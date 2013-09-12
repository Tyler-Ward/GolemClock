$(document).ready(function(){
	bind_controls();
});

function bind_controls(){
	$('#btn-test-display').click(function(){
		test_display();
	});
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
