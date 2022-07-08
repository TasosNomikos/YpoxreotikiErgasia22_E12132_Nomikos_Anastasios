$("form[name=register_form]").submit(function(e){

	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({

		url: "/user/register/", 
		type: "POST", 
		data: data, 
		dataType: "json",


		success: function(resp){
			window.location.href = "/main/";
		},

		error: function(resp){
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}

	})

	e.preventDefault();

});

$("form[name=login_form]").submit(function(e){

	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();
	$.ajax({

		url: "/user/login/", 
		type: "POST", 
		data: data, 
		dataType: "json",


		success: function(resp){
			window.location.href = "/main/";
		},

		error: function(resp){
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}

	})

	e.preventDefault();

});

$("form[name=notes_form]").submit(function(e){

	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();
	$.ajax({

		url: "/user/new_note/", 
		type: "POST", 
		data: data, 
		dataType: "json",


		success: function(resp){
			window.location.href = "/main/";
		}
	})

	e.preventDefault();

});

$("form[name=note").submit(function(e){

	var $form = $(this);
	var data = $form.serialize();

	$.ajax({

		url: "/user/delete_note/", 
		type: "POST", 
		data: data, 
		dataType: "json",
	})


});

$("form[name=searchbar").submit(function(e){

	var $form = $(this);
	var data = $form.serialize();
	var $error = $form.find(".error");

	$.ajax({

		url: "/user/find_note/", 
		type: "POST", 
		data: data, 
		dataType: "json",

		success: function(resp){
			window.location.href = "/findNote/" + "?" + data;
		},

		error: function(resp){
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}
	})

	e.preventDefault();


});

$("form[name=edit").submit(function(e){

	var $form = $(this);
	var data = $form.serialize();
	var $error = $form.find(".error");

	$.ajax({

		url: "/user/edit_note/", 
		type: "POST", 
		data: data, 
		dataType: "json",

		success: function(resp){
			window.location.href = "/editNote/" + "?" + data;
		},

		error: function(resp){
			$error.text(resp.responseJSON.error).removeClass("error--hidden");
		}
	})

	e.preventDefault();
});

$("form[name=update_note]").submit(function(e){

	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();
	$.ajax({

		url: "/user/update_note/", 
		type: "POST", 
		data: data, 
		dataType: "json",


		success: function(resp){
			window.location.href = "/main/";
		}
	})

	e.preventDefault();

});
